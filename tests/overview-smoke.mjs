import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawn} from 'node:child_process';

const edge=process.env.KCL_EDGE || 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const profile=fs.mkdtempSync(path.join(os.tmpdir(),'kcl-edge-smoke-'));
const browser=spawn(edge,['--headless=new','--disable-gpu','--remote-debugging-port=0',`--user-data-dir=${profile}`,'about:blank'],{stdio:'ignore'});
let socket;

try{
 const port=await devtoolsPort(profile);
 const page=await fetch(`http://127.0.0.1:${port}/json/new?http://127.0.0.1:4826`,{method:'PUT'}).then(response=>response.json());
 socket=new WebSocket(page.webSocketDebuggerUrl);
 await new Promise((resolve,reject)=>{socket.addEventListener('open',resolve,{once:true});socket.addEventListener('error',reject,{once:true});});
 let id=0;
 const pending=new Map();
 socket.addEventListener('message',event=>{
  const message=JSON.parse(event.data);
  if(!message.id)return;
  const request=pending.get(message.id);
  if(!request)return;
  pending.delete(message.id);
  if(message.error)request.reject(Error(message.error.message));else request.resolve(message.result);
 });
 const send=(method,params={})=>new Promise((resolve,reject)=>{const requestId=++id;pending.set(requestId,{resolve,reject});socket.send(JSON.stringify({id:requestId,method,params}));});
 const evaluate=async expression=>(await send('Runtime.evaluate',{expression,returnByValue:true})).result.value;
 await send('Page.enable');
 await send('Runtime.enable');

 for(const width of [1440,768,390]){
  await send('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:false});
  await send('Page.navigate',{url:'http://127.0.0.1:4826'});
  await waitFor(async()=>await evaluate("document.readyState==='complete' && document.querySelector('h1')?.textContent?.trim()==='MSc Cyber Security'"));
   const state=await evaluate(`(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,heading:document.querySelector('h1')?.textContent?.trim(),cards:document.querySelectorAll('.module-card').length,sidebarModules:document.querySelectorAll('.module-group>button:not(.module-group-toggle)').length,summary:[...document.querySelectorAll('.programme-stats strong')].map(node=>node.textContent?.trim())}))()`);
  assert.equal(state.heading,'MSc Cyber Security');
  assert.equal(state.cards,8);
  assert.equal(state.sidebarModules,9);
  assert.deepEqual(state.summary,['180','9','1 year','Level 7']);
  assert.ok(state.scrollWidth<=state.width,`Overview overflow at ${width}px: ${state.scrollWidth}px document`);
 }

  await evaluate(`(()=>{const button=[...document.querySelectorAll('.module-nav button')].find(node=>node.textContent?.includes('Agent Reasoning and Decision Making')&&!node.classList.contains('module-group-toggle'));button?.click();return Boolean(button)})()`);
 await waitFor(async()=>await evaluate("document.querySelector('h1')?.textContent?.trim()==='Agent Reasoning and Decision Making'"));
  assert.equal(await evaluate("document.querySelectorAll('.source-option input:checked').length"),0);
 await evaluate(`(()=>{const button=[...document.querySelectorAll('button')].find(node=>node.textContent?.trim()==='Course guide');button?.click();return Boolean(button)})()`);
  await waitFor(async()=>await evaluate("document.querySelectorAll('.guide-tile').length>=2"));

 console.log('PASS: complete course overview, 9-module navigation, new module notebook, README guide, and 1440/768/390px overflow checks.');
}finally{
 if(socket?.readyState===WebSocket.OPEN)socket.close();
 if(browser.exitCode===null){
  const exited=new Promise(resolve=>browser.once('exit',resolve));
  browser.kill();
  await Promise.race([exited,new Promise(resolve=>setTimeout(resolve,3000))]);
 }
 fs.rmSync(profile,{recursive:true,force:true,maxRetries:5,retryDelay:100});
}

async function devtoolsPort(directory){
 const file=path.join(directory,'DevToolsActivePort');
 for(let attempt=0;attempt<80;attempt++){
  if(fs.existsSync(file))return Number(fs.readFileSync(file,'utf8').split(/\r?\n/)[0]);
  await new Promise(resolve=>setTimeout(resolve,100));
 }
 throw Error('Edge did not expose a DevTools port.');
}

async function waitFor(check){
 for(let attempt=0;attempt<80;attempt++){
  if(await check())return;
  await new Promise(resolve=>setTimeout(resolve,100));
 }
 throw Error('Timed out waiting for the dashboard.');
}
