import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const root=path.resolve(import.meta.dirname,'..');
const external=process.env.KCL_NODE_MODULES || path.join(process.env.USERPROFILE || '', 'Desktop','KCL','study-runtime','frontend','node_modules');
const modules=fs.existsSync(path.join(root,'node_modules','typescript'))?path.join(root,'node_modules'):external;
const compiler=path.join(modules,'typescript','bin','tsc');
const sourceConfig=JSON.parse(fs.readFileSync(path.join(root,'tsconfig.json'),'utf8'));
const temporary=fs.mkdtempSync(path.join(os.tmpdir(),'kcl-study-check-'));
const configPath=path.join(temporary,'tsconfig.json');
const slash=value=>value.replaceAll('\\','/');

const config={
 ...sourceConfig,
 compilerOptions:{
  ...sourceConfig.compilerOptions,
  paths:{
   'react':[slash(path.join(modules,'@types','react','index.d.ts'))],
   'react/*':[slash(path.join(modules,'@types','react','*'))],
   'react-dom':[slash(path.join(modules,'@types','react-dom','index.d.ts'))],
   'react-dom/*':[slash(path.join(modules,'@types','react-dom','*'))],
   '*':[slash(path.join(modules,'*'))],
  },
 },
 include:[slash(path.join(root,'app','**','*'))],
};

try{
 fs.writeFileSync(configPath,JSON.stringify(config),{encoding:'utf8'});
 const result=spawnSync(process.execPath,[compiler,'--noEmit','-p',configPath],{cwd:root,stdio:'inherit'});
 if(result.error)throw result.error;
 if(result.status!==0)process.exit(result.status??1);
 console.log('TypeScript check passed.');
}finally{
 fs.rmSync(temporary,{recursive:true,force:true});
}
