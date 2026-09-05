const assert = require('node:assert/strict');
const {chromium} = require(process.env.KCL_PLAYWRIGHT || 'playwright');

(async () => {
 const browser = await chromium.launch({channel:'msedge',headless:true});
 const page = await browser.newPage({viewport:{width:1440,height:1000}});
 const errors=[];
 page.on('pageerror',error=>errors.push(error.message));
 try {
  await page.goto('http://127.0.0.1:4826');
  await page.getByRole('heading',{name:'MSc Cyber Security',exact:true}).waitFor();
  assert.equal(await page.locator('.module-card').count(),8);
  await page.getByRole('button',{name:'Cryptography',exact:true}).click();
  await page.getByRole('heading',{name:'This notebook is empty.',exact:true}).waitFor();
  assert.equal(await page.locator('.source-option input:checked').count(),0);

  await page.getByRole('button',{name:'Visual lab',exact:true}).click();
  await page.getByLabel('Prime p',{exact:true}).selectOption('7');
  await page.getByLabel('Prime q',{exact:true}).selectOption('17');
  await page.getByRole('slider',{name:'Message value'}).fill('42');
  const values=await page.locator('.rsa-flow strong').allTextContents();
  assert.equal(values[0],'42');
  assert.equal(values[2],'42');

  await page.getByRole('button',{name:'Course guide',exact:true}).click();
  await page.locator('.document .prose table').first().waitFor();
  await page.getByRole('button',{name:'Source library',exact:true}).click();
  await page.getByRole('button',{name:'Choose local files',exact:true}).waitFor();
  await page.getByRole('button',{name:'Scan local folders',exact:true}).waitFor();

  await page.getByRole('button',{name:'My modules',exact:true}).click();
  for(const width of [1440,1024,768,390]){
   await page.setViewportSize({width,height:900});
   assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`Overview overflow at ${width}`);
  }
  assert.deepEqual(errors,[]);
  console.log('PASS: empty notebook, unselected sources, RSA controls, course guide, source controls and responsive overview.');
 } finally {
  await browser.close();
 }
})().catch(error=>{console.error(error);process.exitCode=1;});
