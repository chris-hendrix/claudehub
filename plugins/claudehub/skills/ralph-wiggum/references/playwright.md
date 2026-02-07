# Playwright Reference

How to install Playwright locally and use it for browser-based verification in Ralph. **Do NOT use the Playwright MCP server — install Playwright directly and run scripts via Bash.**

## Installation

### Node.js

```bash
# Install the library
npm install playwright
# or
pnpm add playwright

# Install browser binaries (Chromium, Firefox, WebKit)
npx playwright install

# Install just Chromium (fastest, usually sufficient)
npx playwright install chromium

# On Linux, install OS-level dependencies too
npx playwright install --with-deps chromium
```

### Python

```bash
pip install playwright

# Install browser binaries
playwright install

# Install just Chromium
playwright install chromium

# On Linux, install OS-level dependencies too
playwright install --with-deps chromium
```

## Running Headless (Default)

Playwright runs **headless by default** — no display needed. This is what you want in Ralph.

### Python (recommended for Ralph scripts)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()  # headless=True is the default
    page = browser.new_page()
    page.goto("http://localhost:3000")
    page.screenshot(path=".ralph/screenshots/task-1-homepage.png")
    browser.close()
```

### Node.js

```javascript
const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch(); // headless by default
  const page = await browser.newPage();
  await page.goto("http://localhost:3000");
  await page.screenshot({ path: ".ralph/screenshots/task-1-homepage.png" });
  await browser.close();
})();
```

## Common Operations

### Navigate and Screenshot

```python
page.goto("http://localhost:3000/login")
page.screenshot(path=".ralph/screenshots/task-1-login-page.png", full_page=True)
```

### Fill Forms and Submit

```python
page.locator('input[name="email"]').fill("test@example.com")
page.locator('input[name="password"]').fill("password123")
page.locator('button[type="submit"]').click()

# Wait for navigation after submit
page.wait_for_url("**/dashboard")
page.screenshot(path=".ralph/screenshots/task-1-after-login.png")
```

### Click Elements

```python
page.locator("text=Sign In").click()
page.get_by_role("button", name="Submit").click()
page.locator("#menu-toggle").click()
```

### Wait for Elements

```python
# Wait for element to appear
page.locator(".success-message").wait_for(state="visible")

# Wait for element to disappear
page.locator(".loading-spinner").wait_for(state="hidden")

# Wait for specific text
page.locator("h1").wait_for(state="visible")
```

### Read Text and Attributes

```python
# Get text content
heading = page.locator("h1").text_content()
print(f"Page heading: {heading}")

# Get attribute
href = page.locator("a.logo").get_attribute("href")

# Check visibility
is_visible = page.locator(".error-message").is_visible()
```

### Select Dropdowns and Checkboxes

```python
page.select_option("select#country", "US")
page.locator('input[type="checkbox"]').check()
page.locator('input[type="checkbox"]').uncheck()
```

### Assertions (verify things are correct)

```python
# Check text content
assert "Dashboard" in page.locator("h1").text_content()

# Check element exists and is visible
assert page.locator(".welcome-banner").is_visible()

# Check element count
assert page.locator(".list-item").count() == 5

# Check URL
assert "/dashboard" in page.url
```

## Inline Scripts via Bash

The simplest way for Ralph agents to run Playwright is inline via Bash. No separate file needed.

### Python one-liner pattern

```bash
python3 -c "
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.screenshot(path='.ralph/screenshots/task-1-homepage.png', full_page=True)
    print('Title:', page.title())
    print('URL:', page.url)
    browser.close()
"
```

### Node.js one-liner pattern

```bash
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://localhost:3000');
  await page.screenshot({ path: '.ralph/screenshots/task-1-homepage.png', fullPage: true });
  console.log('Title:', await page.title());
  console.log('URL:', page.url());
  await browser.close();
})();
"
```

## Full Verification Example

A complete manual verification flow for a login feature:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # 1. Navigate to login page
    page.goto("http://localhost:3000/login")
    page.screenshot(path=".ralph/screenshots/task-3-login-page.png")
    assert page.locator("form").is_visible(), "Login form not visible"

    # 2. Submit empty form — verify validation
    page.locator('button[type="submit"]').click()
    page.locator(".error-message").wait_for(state="visible")
    page.screenshot(path=".ralph/screenshots/task-3-validation-error.png")
    assert page.locator(".error-message").is_visible(), "Validation error not shown"

    # 3. Fill valid credentials and submit
    page.locator('input[name="email"]').fill("test@example.com")
    page.locator('input[name="password"]').fill("password123")
    page.locator('button[type="submit"]').click()

    # 4. Verify redirect to dashboard
    page.wait_for_url("**/dashboard", timeout=10000)
    page.screenshot(path=".ralph/screenshots/task-3-dashboard.png")
    assert "/dashboard" in page.url, f"Expected dashboard, got {page.url}"
    assert page.locator("h1").text_content() == "Dashboard", "Wrong heading"

    print("All manual checks PASSED")
    browser.close()
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `browserType.launch: Executable doesn't exist` | Run `npx playwright install chromium` or `playwright install chromium` |
| `Host system is missing dependencies` | Run `npx playwright install --with-deps chromium` or `playwright install --with-deps chromium` |
| `page.goto: net::ERR_CONNECTION_REFUSED` | The app isn't running. Start it first. |
| `Timeout waiting for selector` | Element doesn't exist or isn't visible. Check selectors, check if page loaded. |
| `Cannot find module 'playwright'` | Run `npm install playwright` or `pip install playwright` |
