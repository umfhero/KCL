import asyncio, hashlib, json, os, re, secrets, shutil, subprocess, sys, threading, uuid
from pathlib import Path
from urllib.parse import urlparse
from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from . import store
from .catalog import MODULES,ELECTIVES
from .model import model,validate_response,MODEL
from .collector import collect

app=FastAPI(title='KCL study space',docs_url=None,redoc_url=None)
TOKEN=secrets.token_urlsafe(32)
PORT=int(os.environ.get('KCL_PORT','4826'))
CHAT_BUSY=threading.Lock()
LOGIN_PROCESS=None
SYNC_BUSY=threading.Lock()

def all_modules():
    return [dict(m) for m in MODULES]
def module(code):
    found=next((m for m in all_modules() if m['id']==code),None)
    if not found: raise HTTPException(404,'Module not found')
    return found

@app.middleware('http')
async def local_only(request:Request,call_next):
    host=request.headers.get('host','').split(':')[0].lower()
    if host not in {'127.0.0.1','localhost','testserver'}: return JSONResponse({'detail':'Local access only'},status_code=403)
    origin=request.headers.get('origin')
    if origin and origin not in {f'http://127.0.0.1:{PORT}',f'http://localhost:{PORT}'}:
        return JSONResponse({'detail':'Origin not allowed'},status_code=403)
    if request.method not in {'GET','HEAD','OPTIONS'} and request.headers.get('x-study-token')!=TOKEN:
        return JSONResponse({'detail':'Refresh this page before making changes'},status_code=403)
    if int(request.headers.get('content-length','0') or '0')>52*1024*1024:
        return JSONResponse({'detail':'Upload exceeds 50 MB'},status_code=413)
    response=await call_next(request)
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['Referrer-Policy']='no-referrer'
    response.headers['X-Frame-Options']='SAMEORIGIN'
    response.headers['Content-Security-Policy']="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self' data:; connect-src 'self'; frame-src 'self'; object-src 'none'; base-uri 'self'"
    if request.url.path.startswith('/api'): response.headers['Cache-Control']='no-store'
    return response

@app.on_event('startup')
def startup():
    store.init()
    threading.Thread(target=model.status,daemon=True).start()
@app.on_event('shutdown')
def shutdown(): model.close()

@app.get('/api/health')
def health(): return {'ok':True,'app':'kcl-study-space','version':'0.1.0','model':model.last_status}

@app.get('/api/bootstrap')
def bootstrap():
    sources=store.list_sources()
    with store.db() as c:
        jobs=[dict(r) for r in c.execute('SELECT * FROM jobs ORDER BY created DESC LIMIT 15')]
        feeds=[dict(r) for r in c.execute('SELECT * FROM feeds ORDER BY created DESC')]
        notes=c.execute('SELECT COUNT(*) FROM notes').fetchone()[0]
    modules=[]
    for m in all_modules():
        modules.append(dict(m,tasks=[],done_minutes=0,planned_minutes=0,progress=0,sources=sum(s['module']==m['id'] and s['status']=='Indexed' for s in sources)))
    return {'token':TOKEN,'modules':modules,'electives':ELECTIVES,'selected_electives':{},'sources':sources,'progress':{},'jobs':jobs,'feeds':feeds,'model':model.last_status,'data_path':str(store.DATA),'source_path':str(store.SOURCES),'notes_count':notes,'dates':[],'readings':{},'snapshot':'5 September 2026','retrieval':'Local full-text search','version':'0.2.0'}

class Progress(BaseModel):
    task:str
    done:bool
class Elective(BaseModel):
    term:str
    code:str
@app.put('/api/elective')
def elective(body:Elective):
    if body.term not in ELECTIVES or body.code not in {o['id'] for o in ELECTIVES[body.term]}|{''}: raise HTTPException(400,'Unknown elective')
    chosen=store.preference('electives',{}); chosen[body.term]=body.code; store.set_preference('electives',chosen)
    if body.code: (store.SOURCES/body.code).mkdir(parents=True,exist_ok=True)
    return {'ok':True}

@app.get('/api/guide')
def guide(): return {'content':(store.ROOT/'readme.md').read_text(encoding='utf-8')}
@app.get('/api/preparation')
def preparation(): return {'content':(store.ROOT/'summer revision.md').read_text(encoding='utf-8')}
@app.get('/api/sessions')
def list_sessions(scope:str,module_id:str|None=None):
    if scope not in {'module','global'}: raise HTTPException(400,'Unknown chat scope')
    if scope=='module': module(module_id or '')
    return store.sessions(scope,module_id if scope=='module' else None)

class SessionCreate(BaseModel):
    scope:str
    module:str|None=None
    title:str='New chat'
@app.post('/api/sessions')
def create_session(body:SessionCreate):
    if body.scope not in {'module','global'}: raise HTTPException(400,'Unknown chat scope')
    if body.scope=='module': module(body.module or '')
    return store.create_session(body.scope,body.module,body.title)
class SessionRename(BaseModel): title:str=Field(min_length=1,max_length=160)
@app.patch('/api/sessions/{session_id}')
def rename_session(session_id:str,body:SessionRename):
    if not store.get_session(session_id): raise HTTPException(404,'Chat not found')
    return store.rename_session(session_id,body.title)
@app.delete('/api/sessions/{session_id}')
def delete_session(session_id:str):
    if not store.delete_session(session_id): raise HTTPException(404,'Chat not found')
    return {'ok':True}
@app.get('/api/sessions/{session_id}/messages')
def session_messages(session_id:str):
    if not store.get_session(session_id): raise HTTPException(404,'Chat not found')
    return store.history(session_id)

class Chat(BaseModel):
    session_id:str
    question:str=Field(min_length=2,max_length=5000)
    sources:list[str]|None=None
    mode:str='explain'

@app.post('/api/chat')
def chat(body:Chat):
    session=store.get_session(body.session_id)
    if not session: raise HTTPException(404,'Chat not found')
    m=module(session['module']) if session['scope']=='module' else None
    if not CHAT_BUSY.acquire(blocking=False): raise HTTPException(409,'One question is already being answered. Wait for it to finish.')
    try:
        selected=body.sources or []
        if session['scope']=='module':
            allowed={s['id'] for s in store.list_sources(session['module'])}
        else:
            allowed={s['id'] for s in store.list_sources()}
        if session['scope']=='module' and not selected: raise HTTPException(422,'Select one or more sources before asking a question.')
        if not set(selected).issubset(allowed): raise HTTPException(400,'A selected source is outside this chat’s permitted scope.')
        evidence=store.retrieve(session['module'],body.question,selected) if selected else []
        if selected and not evidence: raise HTTPException(422,'No supporting passages found in the selected sources. Select relevant material or add a source.')
        previous=store.history(body.session_id)[-4:]
        context=[]
        for msg in previous:
            text=msg['content'].get('question',msg['content'].get('answer','')) if isinstance(msg['content'],dict) else str(msg['content'])
            context.append({'role':msg['role'],'text':text[:1200]})
        evidence_text='\n\n'.join(f"[{e['ref']}] {e['title']} | {e['kind']} | page {e['page']}\n{e['text']}" for e in evidence)
        guide_context=(store.ROOT/'readme.md').read_text(encoding='utf-8') if session['scope']=='global' else None
        prompt=json.dumps({'module':m['name'] if m else 'MSc Cyber Security programme','course_guide_context_for_programme_questions_only':guide_context,'request_mode':body.mode,'question':body.question,'previous_conversation_for_context_only':context,'evidence':evidence_text},ensure_ascii=False)
        result=validate_response(model.answer(prompt),evidence)
        result['followups']=[str(x)[:250] for x in result.get('followups',[])][:3]
        store.message(session['module'], 'user',{'question':body.question},body.session_id)
        store.message(session['module'], 'assistant',result,body.session_id)
        if session['title']=='New chat': store.rename_session(body.session_id,re.sub(r'\s+',' ',body.question).strip()[:80])
        return result
    except HTTPException: raise
    except Exception as exc: raise HTTPException(503,str(exc)[:500])
    finally: CHAT_BUSY.release()

@app.get('/api/search')
def search(module_id:str,q:str):
    if module_id!='PERSONAL': module(module_id)
    return store.retrieve(module_id,q,limit=12)

@app.post('/api/modules/{code}/upload')
async def upload(code:str,file:UploadFile=File(...)):
    if code!='PERSONAL': module(code)
    name=Path(file.filename or 'document').name
    name=re.sub(r'[^\w .()-]','-',name).strip(' .')[:130]
    if Path(name).suffix.lower() not in {'.pdf','.md','.txt'}: raise HTTPException(400,'Choose a PDF, Markdown or text file.')
    folder=store.SOURCES/code/'uploads'; folder.mkdir(parents=True,exist_ok=True)
    temp=folder/(uuid.uuid4().hex+'.part'); count=0
    try:
        with open(temp,'wb') as out:
            while chunk:=await file.read(1024*1024):
                count+=len(chunk)
                if count>50*1024*1024: raise HTTPException(413,'Upload exceeds 50 MB')
                out.write(chunk)
        digest=hashlib.sha256(temp.read_bytes()).hexdigest()[:10]
        dest=folder/(Path(name).stem+'-'+digest+Path(name).suffix.lower())
        temp.replace(dest)
        sid=await asyncio.to_thread(store.ingest,dest,code,Path(name).stem,'Personal upload')
        return {'id':sid}
    except HTTPException: raise
    except Exception as exc: raise HTTPException(400,str(exc)[:300])
    finally:
        temp.unlink(missing_ok=True)

def source_record(sid):
    with store.db() as c: row=c.execute('SELECT * FROM sources WHERE id=?',(sid,)).fetchone()
    if not row: raise HTTPException(404,'Source not found')
    p=Path(row['path']).resolve()
    if not p.is_relative_to(store.SOURCES.resolve()) or not p.is_file(): raise HTTPException(404,'Source file unavailable')
    return row,p
@app.get('/api/sources/{sid}/file')
def source_file(sid:str):
    row,path=source_record(sid)
    return FileResponse(path,media_type='application/pdf' if path.suffix=='.pdf' else 'text/plain',filename=row['title']+path.suffix,content_disposition_type='inline')
@app.get('/api/sources/{sid}')
def source_detail(sid:str,page:int=1):
    row,path=source_record(sid)
    with store.db() as c: chunks=c.execute('SELECT text FROM chunks WHERE source_id=? AND page=? ORDER BY id',(sid,page)).fetchall()
    content='\n\n'.join(r['text'] for r in chunks)
    return {'id':sid,'title':row['title'],'page':page,'pages':row['pages'],'text':content,'pdf':path.suffix=='.pdf','warning':row['warning'],'origin':row['origin']}

class ImportURL(BaseModel):
    module:str
    url:str=Field(min_length=8,max_length=2000)
    signed_in:bool=False
@app.post('/api/collect')
def collect_url(body:ImportURL):
    module(body.module)
    parsed=urlparse(body.url)
    if parsed.scheme not in {'https','http'} or not parsed.hostname: raise HTTPException(400,'Enter a valid course or PDF URL')
    # Never store token-bearing URLs in a source manifest.
    if re.search(r'(token|password|session|SIW_|sesskey|auth)=',body.url,re.I): raise HTTPException(400,'Use a stable page URL without a session or authentication token.')
    job=uuid.uuid4().hex
    with store.db() as c:
        active=c.execute("SELECT COUNT(*) FROM jobs WHERE status IN ('Queued','Collecting','Indexing')").fetchone()[0]
        if active>=2: raise HTTPException(409,'Two imports are already running. Wait before adding another.')
        c.execute('INSERT INTO jobs VALUES(?,?,?,?,?,?,?)',(job,body.module,body.url,'Queued','Waiting to collect',store.now(),store.now()))
        c.execute('INSERT OR IGNORE INTO feeds VALUES(?,?,?,?)',(hashlib.sha256((body.module+body.url).encode()).hexdigest()[:20],body.module,body.url,store.now()))
    threading.Thread(target=collect,args=(job,body.module,body.url,body.signed_in),daemon=True).start()
    return {'id':job}

@app.post('/api/browser/login')
def browser_login():
    global LOGIN_PROCESS
    if LOGIN_PROCESS and LOGIN_PROCESS.poll() is None: return {'ok':True,'detail':'The study browser is already open.'}
    LOGIN_PROCESS=subprocess.Popen([sys.executable,'-m','server.collector','--login'],cwd=store.ROOT,creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)
    return {'ok':True,'detail':'Sign into KEATS in the study browser, close it, then collect using your signed-in session.'}

def scan_sources(job):
    from .collector import update
    if not SYNC_BUSY.acquire(blocking=False): update(job,'Failed','A library scan is already running.'); return
    try:
        count=0; errors=[]
        for code in [m['id'] for m in all_modules()]+['PERSONAL']:
            for p in (store.SOURCES/code).rglob('*'):
                if p.suffix.lower() in {'.md','.txt','.pdf'} and '.versions' not in p.parts:
                    try: store.ingest(p,code); count+=1
                    except Exception as e: errors.append(p.name+': '+str(e)[:100])
        update(job,'Complete',f'Checked {count} local documents.'+(' '+errors[0] if errors else ''))
    finally: SYNC_BUSY.release()
@app.post('/api/scan')
def scan():
    job=uuid.uuid4().hex
    with store.db() as c: c.execute('INSERT INTO jobs VALUES(?,?,?,?,?,?,?)',(job,'local','Local library','Indexing','Checking documents',store.now(),store.now()))
    threading.Thread(target=scan_sources,args=(job,),daemon=True).start()
    return {'id':job}

class Note(BaseModel):
    module:str
    title:str=Field(min_length=1,max_length=200)
    content:str=Field(min_length=1,max_length=30000)
@app.post('/api/notes')
def save_note(body:Note):
    module(body.module)
    with store.db() as c: c.execute('INSERT INTO notes(module,title,content,created) VALUES(?,?,?,?)',(body.module,body.title,body.content,store.now()))
    return {'ok':True}
@app.get('/api/notes')
def notes():
    with store.db() as c: return [dict(r) for r in c.execute('SELECT * FROM notes ORDER BY created DESC')]
@app.get('/api/export')
def export():
    with store.db() as c:
        data={t:[dict(r) for r in c.execute(f'SELECT * FROM {t}')] for t in ['progress','preferences','chat_sessions','messages','notes']}
    return JSONResponse(data,headers={'Content-Disposition':'attachment; filename="kcl-study-export.json"'})
@app.post('/api/model/reconnect')
def reconnect(): return model.status()

if (store.ROOT/'dist').exists(): app.mount('/',StaticFiles(directory=store.ROOT/'dist',html=True),name='dashboard')

if __name__=='__main__':
    import uvicorn
    uvicorn.run('server.main:app',host='127.0.0.1',port=PORT,log_level='info')
