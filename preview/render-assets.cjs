// Run from preview/: npm install && npm run vendor && npm run render
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright-core');
const fs = require('node:fs/promises');
const path = require('node:path');
const http = require('node:http');
const os = require('node:os');
const { execFileSync } = require('node:child_process');
const root = path.resolve(__dirname, '..');

(async () => {
  const frames = await fs.mkdtemp(path.join(os.tmpdir(), 'cace-hero-'));
  const server = http.createServer(async (req, res) => {
    try {
      const target = path.resolve(root, '.' + new URL(req.url, 'http://localhost').pathname);
      if (!target.startsWith(root + path.sep)) throw new Error('Invalid path');
      res.setHeader('Content-Type', target.endsWith('.js') ? 'text/javascript' : 'text/html');
      res.end(await fs.readFile(target));
    } catch { res.writeHead(404); res.end(); }
  });
  let browser;
  try {
    await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
    browser = await chromium.launch({
      executablePath: process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      headless: true, args: ['--use-angle=swiftshader', '--enable-webgl']
    });
    const page = await browser.newPage({ viewport: { width: 1200, height: 420 }, deviceScaleFactor: 1 });
    await page.goto(`http://127.0.0.1:${server.address().port}/preview/hero.html`);
    await page.waitForFunction(() => window.sceneReady);
    for (let i = 0; i < 72; i++) {
      await page.evaluate(t => window.renderAt(t), i / 12);
      const frame = path.join(frames, `${String(i).padStart(3, '0')}.png`);
      await page.screenshot({ path: frame });
      if (i === 0) await fs.copyFile(frame, path.join(root, 'assets/profile-hero.png'));
    }
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', '12', '-i', path.join(frames, '%03d.png'),
      '-filter_complex', '[0:v]split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle',
      '-loop', '0', path.join(root, 'assets/profile-hero.gif')]);
    console.log('Rendered profile-hero.png and profile-hero.gif (1200 × 420, 72 frames, 6-second loop).');
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
    await fs.rm(frames, { recursive: true, force: true });
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
