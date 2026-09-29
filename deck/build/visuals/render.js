// Renders a visuals/*.html page to a transparent PNG with headless Chromium.
// Usage: node visuals/render.js globe.html out.png "lat=-24&lon=62"
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const NM = path.join(ROOT, 'node_modules');
const routes = {
  '/three/': path.join(NM, 'three/build/'),
  '/lib/d3-array.min.js': path.join(NM, 'd3-array/dist/d3-array.min.js'),
  '/lib/d3-geo.min.js': path.join(NM, 'd3-geo/dist/d3-geo.min.js'),
  '/lib/topojson-client.min.js': path.join(NM, 'topojson-client/dist/topojson-client.min.js'),
  '/data/': path.join(NM, 'world-atlas/'),
  '/fonts/': path.join(NM, '@fontsource/noto-sans/files/'),
  '/': path.join(__dirname, '/'),
};
const types = { '.js': 'text/javascript', '.json': 'application/json', '.html': 'text/html', '.woff2': 'font/woff2' };

(async () => {
  const [page_, out, query = ''] = process.argv.slice(2);
  const browser = await chromium.launch({
    executablePath: fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined,
    args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'],
  });
  const page = await browser.newPage({ viewport: { width: 2400, height: 2400 } });
  page.on('console', m => console.log('[page]', m.text()));
  page.on('pageerror', e => console.error('[pageerror]', e.message));
  await page.route('http://local/**', route => {
    const url = new URL(route.request().url()).pathname;
    const prefix = Object.keys(routes).find(p => url.startsWith(p));
    const file = routes[prefix].endsWith('/') ? path.join(routes[prefix], url.slice(prefix.length)) : routes[prefix];
    if (!fs.existsSync(file)) return route.fulfill({ status: 404, body: 'missing ' + url });
    route.fulfill({ body: fs.readFileSync(file), contentType: types[path.extname(file)] || 'application/octet-stream' });
  });
  await page.goto(`http://local/${page_}?${query}`);
  await page.waitForFunction('window.__done === true', null, { timeout: 180000 });
  await page.locator('#stage').screenshot({ path: out, omitBackground: true });
  await browser.close();
  console.log('wrote', out);
})();
