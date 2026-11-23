from pathlib import Path
from base64 import b64encode
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent / 'dist'
errors = []
for path in ['/', '/cv/', '/blog/']:
    f = root / path.lstrip('/') / 'index.html'
    doc = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    assert doc.select_one('main h1'), path
    for a in doc.select('a[href^="/"]'):
        target = root / a['href'].lstrip('/')
        if target.is_dir() or not target.suffix:
            target = target / 'index.html'
        assert target.exists(), (path, a.get('href'))
    print(path, 'PASS', doc.title.get_text(strip=True))
assert not (root / 'cves').exists()
assert not (root / 'research').exists()
assert not (root / 'writeups').exists()
assert not (root / 'blog/sample-technical-writeup').exists()

# Inlined assets to permit direct browser inspection without a local server.
home = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'assets/styles.css').read_text(encoding='utf-8')
js = (root / 'assets/site.js').read_text(encoding='utf-8')
avatar = b64encode((root / 'assets/avatar.svg').read_bytes()).decode('ascii')
favicon = b64encode((root / 'assets/favicon.svg').read_bytes()).decode('ascii')
home = home.replace('<link rel="stylesheet" href="/assets/styles.css">', '<style>' + css + '</style>')
home = home.replace('<script defer src="/assets/site.js"></script>', '<script>' + js + '</script>')
home = home.replace('/assets/avatar.svg', 'data:image/svg+xml;base64,' + avatar)
home = home.replace('/assets/favicon.svg', 'data:image/svg+xml;base64,' + favicon)
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    desktop = browser.new_page(viewport={'width': 1440, 'height': 920}, device_scale_factor=1, color_scheme='light')
    desktop.on('pageerror', lambda e: errors.append(str(e)))
    desktop.set_content(home, wait_until='load')
    desktop.screenshot(path='/mnt/data/nacho-v2-home-light.png', full_page=True)
    desktop.locator('.theme-switch').click()
    assert desktop.locator('html').get_attribute('data-theme') == 'dark'
    desktop.screenshot(path='/mnt/data/nacho-v2-home-dark.png', full_page=True)
    mobile = browser.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=1, color_scheme='light')
    mobile.set_content(home, wait_until='load')
    mobile.screenshot(path='/mnt/data/nacho-v2-home-mobile.png', full_page=True)
    assert mobile.evaluate('document.documentElement.scrollWidth') <= 390
    assert not errors, errors
    browser.close()
print('Visual checks PASS, JS errors:', errors)
