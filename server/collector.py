"""Bounded file collector for user-selected course pages and reading URLs."""
import hashlib, ipaddress, os, re, socket, sys, threading, time, uuid
from pathlib import Path
from urllib.parse import urljoin,urlparse,urldefrag
import httpx
from bs4 import BeautifulSoup
from .store import DATA,SOURCES,db,ingest,now

PROFILE=DATA/'browser-profile'
_browser_lock=threading.Lock()

def valid_url(url):
    parsed=urlparse(url)
    if parsed.scheme not in {'http','https'} or not parsed.hostname or parsed.username or parsed.password: raise ValueError('Use a public HTTP or HTTPS course URL.')
    if parsed.port not in (None,80,443): raise ValueError('Only standard web ports are supported.')
    addresses=socket.getaddrinfo(parsed.hostname,parsed.port or 443,type=socket.SOCK_STREAM)
    if any(not ipaddress.ip_address(x[4][0]).is_global for x in addresses): raise ValueError('Local and private network URLs are not allowed.')
    return url

def update(job,status,detail):
    with db() as c: c.execute('UPDATE jobs SET status=?,detail=?,updated=? WHERE id=?',(status,detail[:500],now(),job))

def collect(job,module,url,use_browser=False):
    update(job,'Collecting','Checking the selected page')
    imported=0; examined=0; errors=[]; context=None; browser_driver=None; visited=set(); owns_browser_lock=False
    try:
        valid_url(url)
        client=httpx.Client(timeout=35,follow_redirects=False,headers={'User-Agent':'KCLPersonalStudy/0.1 (personal course resource organiser)'})
        if use_browser:
            if not _browser_lock.acquire(blocking=False): raise ValueError('The study browser is in use. Close its sign-in window, then retry.')
            owns_browser_lock=True
            from playwright.sync_api import sync_playwright
            browser_driver=sync_playwright().start()
            context=browser_driver.chromium.launch_persistent_context(str(PROFILE),channel='msedge',headless=True,accept_downloads=True)
        def get(target):
            for _ in range(6):
                valid_url(target)
                if context:
                    response=context.request.get(target,timeout=35000,max_redirects=0)
                    status=response.status; headers=response.headers; content=response.body()
                else:
                    with client.stream('GET',target) as response:
                        status=response.status_code; headers=response.headers
                        if int(headers.get('content-length','0') or '0')>50*1024*1024: raise ValueError('Download exceeds 50 MB')
                        chunks=[]; size=0
                        for chunk in response.iter_bytes():
                            size+=len(chunk)
                            if size>50*1024*1024: raise ValueError('Download exceeds 50 MB')
                            chunks.append(chunk)
                        content=b''.join(chunks)
                if status in (301,302,303,307,308): target=urljoin(target,headers.get('location','')); continue
                if status>=400: raise ValueError(f'The site returned HTTP {status}')
                if len(content)>50*1024*1024: raise ValueError('Download exceeds 50 MB')
                return target,headers,content
            raise ValueError('Too many redirects')
        pending=[(url,'')]; origin=urlparse(url).hostname
        while pending and examined<35 and imported<20:
            target,label=pending.pop(0)
            if target in visited: continue
            visited.add(target); examined+=1
            try:
                final,headers,raw=get(target)
                if any(x in urlparse(final).path.lower() for x in ['/login','/signin']) or 'login.microsoftonline.com' in final:
                    update(job,'Sign-in required','Open the study browser, sign into KEATS, then retry this page.'); return
                is_pdf=raw.startswith(b'%PDF-')
                if is_pdf:
                    clean=re.sub(r'[^\w .()-]+','-',label or Path(urlparse(final).path).stem or 'reading')[:85].strip(' .') or 'reading'
                    category='handbook' if 'handbook' in (label+target).lower() else 'readings'
                    folder=SOURCES/module/category; folder.mkdir(parents=True,exist_ok=True)
                    dest=folder/(clean+'-'+hashlib.sha256(raw).hexdigest()[:10]+'.pdf')
                    if not dest.exists():
                        temp=dest.with_suffix('.part'); temp.write_bytes(raw); temp.replace(dest)
                    ingest(dest,module,label or clean,target); imported+=1
                    update(job,'Indexing',f'Indexed {imported} PDF(s). Checking remaining links.')
                elif 'html' in headers.get('content-type',''):
                    soup=BeautifulSoup(raw,'html.parser')
                    if soup.select_one('input[type="password"]'):
                        update(job,'Sign-in required','Sign into the study browser, then retry this page.'); return
                    for a in soup.find_all('a',href=True):
                        href=urldefrag(urljoin(final,a['href']))[0]
                        parsed=urlparse(href)
                        # Follow files and Moodle resource/folder pages, never assessments or generic site links.
                        resource=any(x in parsed.path.lower() for x in ['/mod/resource/','/mod/folder/'])
                        pdf=parsed.path.lower().endswith('.pdf') or '.pdf' in parsed.query.lower()
                        if (pdf or resource) and parsed.hostname==origin and href not in visited:
                            label=a.get_text(' ',strip=True)
                            if label.lower() in {'pdf','download','download pdf',''}:
                                siblings=list(a.previous_siblings)
                                label=''.join(x.get_text(' ',strip=True) if hasattr(x,'get_text') else str(x) for x in reversed(siblings)).strip()
                                if not label or len(label)>180: label=Path(parsed.path).stem
                            pending.append((href,label[:180]))
                time.sleep(.2)
            except Exception as exc: errors.append(str(exc)[:120])
        suffix=f' {len(errors)} link(s) need review: '+errors[0] if errors else ''
        if imported: update(job,'Complete',f'Indexed {imported} PDF(s); checked {examined} links.'+suffix)
        else: update(job,'Needs review','No downloadable PDFs found. Add a direct PDF URL, or use signed-in collection.'+suffix)
    except Exception as exc: update(job,'Failed',str(exc))
    finally:
        if context: context.close()
        if browser_driver: browser_driver.stop()
        if owns_browser_lock:
            try: _browser_lock.release()
            except RuntimeError: pass
        if 'client' in locals(): client.close()

def login_browser():
    from playwright.sync_api import sync_playwright
    PROFILE.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        context=p.chromium.launch_persistent_context(str(PROFILE),channel='msedge',headless=False,accept_downloads=True)
        page=context.pages[0] if context.pages else context.new_page()
        page.goto('https://keats.kcl.ac.uk/',wait_until='domcontentloaded')
        try:
            while context.pages: time.sleep(1)
        except Exception: pass
        finally:
            try: context.close()
            except Exception: pass

if __name__=='__main__' and '--login' in sys.argv: login_browser()
