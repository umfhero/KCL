import hashlib, json, os, re, sqlite3, threading
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader
from .catalog import MODULES

ROOT=Path(__file__).resolve().parents[1]
DATA=Path(os.environ.get('KCL_STUDY_DATA', str(Path.home()/'Desktop'/'KCL'/'study-data'))).resolve()
SOURCES=ROOT/'sources'/'2026-27'
_lock=threading.RLock()

def now(): return datetime.now(timezone.utc).isoformat()
@contextmanager
def db():
    DATA.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(DATA/'study.sqlite',timeout=30)
    con.row_factory=sqlite3.Row
    con.execute('PRAGMA foreign_keys=ON')
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback(); raise
    finally: con.close()

def init():
    SOURCES.mkdir(parents=True,exist_ok=True)
    with db() as c:
        c.executescript('''
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS sources(id TEXT PRIMARY KEY,module TEXT NOT NULL,title TEXT,path TEXT,origin TEXT,hash TEXT,kind TEXT,status TEXT,pages INTEGER,created TEXT,warning TEXT);
        CREATE TABLE IF NOT EXISTS chunks(id INTEGER PRIMARY KEY,source_id TEXT REFERENCES sources(id) ON DELETE CASCADE,page INTEGER,text TEXT);
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(text,content='chunks',content_rowid='id');
        CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN INSERT INTO chunks_fts(rowid,text) VALUES(new.id,new.text); END;
        CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN INSERT INTO chunks_fts(chunks_fts,rowid,text) VALUES('delete',old.id,old.text); END;
        CREATE TABLE IF NOT EXISTS progress(task TEXT PRIMARY KEY,done INTEGER NOT NULL,updated TEXT);
        CREATE TABLE IF NOT EXISTS preferences(key TEXT PRIMARY KEY,value TEXT);
        CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY,module TEXT,role TEXT,content TEXT,created TEXT);
        CREATE TABLE IF NOT EXISTS chat_sessions(id TEXT PRIMARY KEY,scope TEXT NOT NULL CHECK(scope IN ('module','global')),module TEXT,title TEXT NOT NULL,created TEXT NOT NULL,updated TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,module TEXT,title TEXT,content TEXT,created TEXT);
        CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY,module TEXT,url TEXT,status TEXT,detail TEXT,created TEXT,updated TEXT);
        CREATE TABLE IF NOT EXISTS feeds(id TEXT PRIMARY KEY,module TEXT,url TEXT,created TEXT);
        ''')
        # Existing installations predate saved chats.  Keep that history intact but
        # deliberately unassigned: old implicit conversations must not appear in a
        # newly created notebook.
        if 'session_id' not in {r['name'] for r in c.execute('PRAGMA table_info(messages)')}:
            c.execute('ALTER TABLE messages ADD COLUMN session_id TEXT REFERENCES chat_sessions(id) ON DELETE CASCADE')
        c.execute("UPDATE jobs SET status='Interrupted', detail='App restarted. Run sync again to resume.', updated=? WHERE status IN ('Queued','Collecting','Indexing')",(now(),))
    for module in MODULES:
        (SOURCES/module['id']).mkdir(parents=True,exist_ok=True)
    (SOURCES/'PERSONAL').mkdir(parents=True,exist_ok=True)
    clean_generated_sources()

def clean_generated_sources():
    """Remove only records and files created by the retired startup seeders."""
    generated={
        ('readme.md','guide'):'module-guide.md',
        ('Locally authored preparation notes','preparation'):'number-theory-preparation.md',
        ('Existing repository preparation material','background'):'earlier-revision-guide.md',
    }
    with db() as c:
        rows=c.execute('SELECT id,module,path,origin,kind,hash FROM sources').fetchall()
        stale=[r for r in rows if (r['origin'],r['kind']) in generated]
        for row in stale:
            c.execute('DELETE FROM sources WHERE id=?',(row['id'],))
    for row in stale:
        version=Path(row['path'])
        if version.is_relative_to(SOURCES.resolve()): version.unlink(missing_ok=True)
        original=SOURCES/row['module']/generated[(row['origin'],row['kind'])]
        if original.exists() and hashlib.sha256(original.read_bytes()).hexdigest()==row['hash']:
            original.unlink()

def ingest(path,module,title=None,origin='',kind='document'):
    path=Path(path).resolve()
    if module != 'PERSONAL' and module not in {m['id'] for m in MODULES} and not re.fullmatch(r'[A-Z0-9]{6,12}',module): raise ValueError('Unknown module')
    if not path.is_relative_to(SOURCES.resolve()): raise ValueError('File must be inside the module library')
    raw=path.read_bytes()
    if len(raw)>50*1024*1024: raise ValueError('Files must be smaller than 50 MB')
    digest=hashlib.sha256(raw).hexdigest()
    source_id=hashlib.sha256((module+digest).encode()).hexdigest()[:24]
    with _lock:
        with db() as c:
            if c.execute('SELECT id FROM sources WHERE id=?',(source_id,)).fetchone(): return source_id
        if path.suffix.lower()=='.pdf':
            reader=PdfReader(path)
            if reader.is_encrypted and not reader.decrypt(''): raise ValueError('This PDF is encrypted. Add an accessible copy.')
            if len(reader.pages)>2500: raise ValueError('PDF exceeds the 2,500 page limit')
            pages=[(i+1,page.extract_text() or '') for i,page in enumerate(reader.pages)]
        elif path.suffix.lower() in {'.md','.txt'}:
            pages=[(1,raw.decode('utf-8-sig',errors='replace'))]
        else: raise ValueError('Supported formats: PDF, Markdown and text')
        # Immutable version copy ensures old citations still open their original document.
        version_dir=path.parent/'.versions'; version_dir.mkdir(exist_ok=True)
        version_path=version_dir/(digest+path.suffix.lower())
        if not version_path.exists(): version_path.write_bytes(raw)
        usable=sum(len(t.strip()) for _,t in pages)>60
        empty=sum(1 for _,t in pages if len(t.strip())<30)
        warning=f'{empty} pages have little extracted text; diagrams or scans may need manual review.' if empty else ''
        with db() as c:
            c.execute('INSERT INTO sources VALUES(?,?,?,?,?,?,?,?,?,?,?)',(source_id,module,title or path.stem,str(version_path),origin,digest,kind,'Indexed' if usable else 'Needs OCR',len(pages),now(),warning))
            for page,content in pages:
                content=re.sub(r'[ \t]+',' ',content).strip()
                for start in range(0,len(content),1500):
                    part=content[start:start+1800]
                    if len(part)>30: c.execute('INSERT INTO chunks(source_id,page,text) VALUES(?,?,?)',(source_id,page,part))
        return source_id

def list_sources(module=None):
    with db() as c:
        rows=c.execute('SELECT * FROM sources'+(' WHERE module=?' if module else '')+' ORDER BY created DESC',(module,) if module else ()).fetchall()
    return [{k:r[k] for k in r.keys() if k not in {'path','hash'}} for r in rows]

def retrieve(module,question,selected=None,limit=7):
    if selected==[]: return []
    words=re.findall(r'[A-Za-z][A-Za-z0-9]{2,}',question.lower())
    stop={'the','and','for','with','what','how','this','that','from','have','explain','please','could','would','about','module','show'}
    terms=list(dict.fromkeys(w for w in words if w not in stop))[:24]
    where="s.status='Indexed'"; args=[]
    if module:
        where+=' AND s.module=?'; args.append(module)
    if selected is not None:
        where+=' AND s.id IN ('+','.join('?' for _ in selected)+')'; args+=selected
    fields='c.id,c.source_id,c.page,c.text,s.title,s.kind,s.origin'
    with db() as c:
        rows=[]
        if terms:
            query=' OR '.join('"'+w+'"' for w in terms)
            rows=c.execute(f'SELECT {fields},bm25(chunks_fts) AS rank FROM chunks_fts JOIN chunks c ON c.id=chunks_fts.rowid JOIN sources s ON s.id=c.source_id WHERE chunks_fts MATCH ? AND {where} ORDER BY rank LIMIT ?', [query]+args+[limit]).fetchall()
        # Broad requests receive a small module overview; absent specific terms are not silently fabricated.
        if not rows and (not terms or any(x in question.lower() for x in ['overview','start','revise','prepare','topics','teach me'])):
            rows=c.execute(f'SELECT {fields} FROM chunks c JOIN sources s ON s.id=c.source_id WHERE {where} ORDER BY CASE s.kind WHEN \'guide\' THEN 0 ELSE 1 END,c.id LIMIT ?',args+[limit]).fetchall()
    return [dict(r,ref=f'S{i+1}') for i,r in enumerate(rows)]

def preference(key,default=None):
    with db() as c:
        row=c.execute('SELECT value FROM preferences WHERE key=?',(key,)).fetchone()
    return json.loads(row['value']) if row else default

def set_preference(key,value):
    with db() as c: c.execute('INSERT OR REPLACE INTO preferences VALUES(?,?)',(key,json.dumps(value)))

def create_session(scope,module=None,title='New chat'):
    import uuid
    if scope not in {'module','global'} or (scope=='module' and not module): raise ValueError('Invalid chat session')
    if scope=='global': module=None
    sid=uuid.uuid4().hex
    with db() as c: c.execute('INSERT INTO chat_sessions VALUES(?,?,?,?,?,?)',(sid,scope,module,title.strip()[:160] or 'New chat',now(),now()))
    return get_session(sid)

def get_session(session_id):
    with db() as c: row=c.execute('SELECT * FROM chat_sessions WHERE id=?',(session_id,)).fetchone()
    return dict(row) if row else None

def sessions(scope,module=None):
    with db() as c:
        rows=c.execute('SELECT * FROM chat_sessions WHERE scope=? AND module IS ? ORDER BY updated DESC',(scope,module)).fetchall()
    return [dict(r) for r in rows]

def rename_session(session_id,title):
    with db() as c: c.execute('UPDATE chat_sessions SET title=?,updated=? WHERE id=?',(title.strip()[:160] or 'New chat',now(),session_id))
    return get_session(session_id)

def delete_session(session_id):
    with db() as c:
        c.execute('DELETE FROM messages WHERE session_id=?',(session_id,))
        return c.execute('DELETE FROM chat_sessions WHERE id=?',(session_id,)).rowcount

def message(module,role,content,session_id=None):
    with db() as c:
        c.execute('INSERT INTO messages(module,role,content,created,session_id) VALUES(?,?,?,?,?)',(module,role,json.dumps(content),now(),session_id))
        if session_id:
            c.execute('UPDATE chat_sessions SET updated=? WHERE id=?',(now(),session_id))

def history(session_id):
    with db() as c: rows=c.execute('SELECT * FROM messages WHERE session_id=? ORDER BY id DESC LIMIT 60',(session_id,)).fetchall()
    return [dict(r,content=json.loads(r['content'])) for r in reversed(rows)]
