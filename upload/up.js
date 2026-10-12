// Chismepón: one Studio upload, scheduled. Filled in by upload/run.py (__META__, __PUBLISH__).
// Adapted from shorts-factory/channels/jjimhaedum/upload/up.js. Checks every field it set and
// only presses Schedule when they all read back right - otherwise the upload stays a private draft.
const M = __META__;
const log = (...a) => console.log(...a);
const r = await fetch('http://127.0.0.1:8765/' + M.file); const b = await r.arrayBuffer();
await fs.writeFile('v.mp4', new Uint8Array(b));
const page = await openTab('https://studio.youtube.com/channel/UCyvXZyFPF3XP9jGb-KaWI_g/videos/upload?d=ud');
await page.waitForSelector('input[type=file]', {state: 'attached', timeout: 20000});
await page.locator('input[type=file]').first().setInputFiles('v.mp4');
await page.waitForSelector('ytcp-uploads-dialog #title-textarea #textbox', {timeout: 30000});
await sleep(2500);
async function setBox(sel, text) {
  const box = page.locator(sel).first();
  await box.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await page.keyboard.insertText(text);
}
await setBox('ytcp-uploads-dialog #title-textarea #textbox', M.title);
await setBox('ytcp-uploads-dialog #description-textarea #textbox', M.description);
await page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click();
await page.locator('ytcp-uploads-dialog #toggle-button').click(); await sleep(1500);   // 자세히 보기
// altered/synthetic content: cartoon pictures + a TTS narrator that is not a real person -> 아니요
const aiNo = await page.evaluate(() => { const r = [...document.querySelectorAll('ytcp-uploads-dialog tp-yt-paper-radio-button')].filter(x => x.innerText.trim() === '아니요'); r.forEach(x => x.click()); return r.length; });
log('ai no', aiNo); await sleep(800);
// tags
const tagIn = page.locator('ytcp-uploads-dialog #tags-container input, ytcp-uploads-dialog ytcp-free-text-chip-bar input').first();
if (await tagIn.count()) { await tagIn.click(); await page.keyboard.insertText(M.tags.join(',') + ','); }
const st = await page.evaluate(() => ({
  title: document.querySelector('ytcp-uploads-dialog #title-textarea #textbox')?.innerText,
  kids: document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')?.getAttribute('aria-checked'),
  aiNo: [...document.querySelectorAll('ytcp-uploads-dialog tp-yt-paper-radio-button')].filter(x=>x.innerText.trim()==='아니요').map(x=>x.getAttribute('aria-checked')).join(),
}));
log(JSON.stringify(st));
for (let i = 0; i < 3; i++) {
  for (let k = 0; k < 30; k++) { const d = await page.evaluate(() => document.querySelector('ytcp-uploads-dialog #next-button')?.getAttribute('aria-disabled')); if (d !== 'true') break; await sleep(1000); }
  await page.locator('ytcp-uploads-dialog #next-button').click(); await sleep(2000);
}
// visibility step: open 예약 and set date + time
await page.locator('ytcp-uploads-dialog #second-container-expand-button').click(); await sleep(1500);
await page.locator('ytcp-uploads-dialog #datepicker-trigger').click(); await sleep(1000);
const dateIn = page.locator('ytcp-date-picker tp-yt-paper-input input, ytcp-date-picker input').first();
await dateIn.click(); await page.keyboard.press('Control+A'); await page.keyboard.insertText(M.dateText); await page.keyboard.press('Enter'); await sleep(1200);
const timeIn = page.locator('ytcp-uploads-dialog #time-of-day-container input').first();
await timeIn.click(); await page.keyboard.press('Control+A'); await page.keyboard.insertText(M.timeText); await page.keyboard.press('Enter'); await sleep(1200);
const sched = await page.evaluate(() => ({
  date: document.querySelector('ytcp-uploads-dialog #datepicker-trigger')?.innerText.trim(),
  time: document.querySelector('ytcp-uploads-dialog #time-of-day-container input')?.value,
  tz: document.querySelector('ytcp-uploads-dialog #timezone-select-button, ytcp-uploads-dialog .timezone')?.innerText?.trim(),
  done: document.querySelector('ytcp-uploads-dialog #done-button')?.innerText.trim(),
}));
log('sched', JSON.stringify(sched));
const ok = st.title === M.title && st.kids === 'true' && sched.date && sched.date.replace(/\s/g, '').includes(M.dateCheck)
  && (sched.time || '').replace(/\s/g, '') === M.timeText.replace(/\s/g, '');
if (!ok || !__PUBLISH__) {
  log('STOP: left as a private draft', ok ? '(publish off)' : '(schedule did not read back)');
  log('DOM', (await page.evaluate(() => document.querySelector('ytcp-uploads-dialog ytcp-visibility-scheduler, ytcp-uploads-dialog #second-container')?.outerHTML || '')).slice(0, 3000));
} else {
  for (let i = 0; i < 120; i++) {   // the file must finish uploading before Schedule is final
    const s = await page.evaluate(() => document.querySelector('ytcp-uploads-dialog .progress-label, ytcp-video-upload-progress')?.innerText || '');
    if (!/업로드 중|Uploading/.test(s)) break;
    await sleep(1000);
  }
  for (let k = 0; k < 40; k++) { const d = await page.evaluate(() => document.querySelector('ytcp-uploads-dialog #done-button')?.getAttribute('aria-disabled')); if (d !== 'true') break; await sleep(1000); }
  await page.locator('ytcp-uploads-dialog #done-button').click();
  await sleep(5000);
  const link = await page.evaluate(() => [...document.querySelectorAll('a')].map(a => a.href).find(h => /youtube\.com\/shorts\/|youtu\.be\//.test(h)));
  log('LINK', link || '(none)');
}
