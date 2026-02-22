# Testing Types

Reference for common testing strategies used in VERIFICATION.md.

## Unit Tests

Fast, isolated tests for individual functions/components.

**Runners:**
- Python: pytest, unittest
- JavaScript/TypeScript: jest, vitest, mocha
- Go: go test

**Characteristics:**
- Run without external dependencies
- Mock external services
- Fast execution (milliseconds per test)

**Environment validation:** Find an existing test file, run one test to verify runner works.

## Integration Tests

Tests that verify multiple components work together.

**Characteristics:**
- May require database, cache, or other services
- Often run in containers (Docker)
- Slower than unit tests

**Environment validation:** Check required services are running before attempting.

## E2E Tests (End-to-End) - Automated

Scripted tests that simulate user interactions through the full stack. **These are automated and run in CI.**

**Runners:**
- Playwright
- Cypress
- Selenium

**Characteristics:**
- Automated, repeatable, deterministic
- Run in CI/CD pipelines
- Test specific scripted flows
- Good for regression testing critical paths
- Cannot catch visual/design issues or UX problems
- Limited to pre-defined scenarios

**What E2E tests cover:**
- Happy path user flows work
- Form submissions succeed
- Navigation works
- Data persists correctly

**What E2E tests DON'T cover:**
- Visual appearance matches design
- UX feels right
- Edge cases not scripted
- Responsive behavior across devices
- Accessibility in practice

**Environment validation:**
- Check browser is installed (`npx playwright install --dry-run`)
- Check app is running at expected URL
- Verify can navigate and interact

## Linting

Static analysis for code style and potential errors.

**Tools:**
- Python: ruff, flake8, pylint
- JavaScript/TypeScript: eslint, prettier
- Go: golint, staticcheck

**Characteristics:**
- No runtime needed
- Fast execution
- Can run on any file

**Environment validation:** Run linter on a single file to verify it works.

## Type Checking

Static type verification.

**Tools:**
- Python: mypy, pyright
- TypeScript: tsc
- Go: built-in

**Characteristics:**
- No runtime needed
- Catches type errors before execution

**Environment validation:** Run type checker to verify configuration is valid.

## Manual Browser Testing

Interactive testing through a browser. **This is NOT the same as E2E tests** - manual testing catches things automated tests cannot.

**YOU are the one doing this. There is no human in the loop.** When VERIFICATION.md lists manual browser checks, the coding agent performs them using Playwright (installed locally). You navigate to pages, interact with elements, take screenshots, and verify the result. If you skip manual checks, the task is NOT complete.

**Tools:**
- Playwright installed locally — run scripts via Bash (see `references/playwright.md`). Do NOT use the Playwright MCP server.

**Characteristics:**
- Exploratory, not scripted
- Verifies visual appearance and UX
- Catches edge cases and unexpected behaviors
- Requires judgment calls
- Often requires feature flags enabled

**What manual testing covers that E2E doesn't:**
- Visual appearance matches design specs
- UI feels right (spacing, alignment, colors)
- Error states display correctly
- Loading states are appropriate
- Responsive behavior works
- Accessibility is usable
- Edge cases beyond scripted scenarios
- Overall UX quality

**When to use each:**
- E2E tests: Automate critical paths for regression safety
- Manual testing: Verify new features look/feel right, explore edge cases

**Both are required for UI work.** E2E tests alone are not sufficient - they only prove the code runs, not that it's correct or usable.

**Environment validation:**
- Check Playwright is installed (`python3 -c "from playwright.sync_api import sync_playwright"` or `node -e "require('playwright')"`)
- If not installed, install it: `pip install playwright && playwright install --with-deps chromium` or `npm install playwright && npx playwright install --with-deps chromium`
- Verify app loads at URL
- Attempt login with test credentials if provided
- Verify required feature flags are enabled (see Feature Flags section)
- Navigate to relevant pages and confirm feature is visible

## API/Backend Verification

Testing backend endpoints directly. **YOU do this yourself.** When VERIFICATION.md lists API checks, use curl or similar tools to hit the endpoints, inspect responses, and verify correctness. Do not skip this and do not assume someone else will do it.

**Tools:**
- curl / httpie (run via Bash)

**Process:**
1. Ensure the backend is running. If it's not, start it yourself.
2. Curl each endpoint listed in VERIFICATION.md
3. Verify response status codes, body structure, and data correctness
4. Test error cases (bad input, missing auth, etc.)
5. If authentication is required, obtain tokens yourself (login endpoint, test credentials from VERIFICATION.md)

**Environment validation:**
- Check endpoint is reachable. If not, start the service yourself.
- Verify authentication works if required

## Feature Flags

Features may be gated behind feature flags that must be enabled for testing.

**Common services:**
- LaunchDarkly
- Split
- Flagsmith
- Unleash
- Custom/internal systems

**Characteristics:**
- Flags may be configured per environment (local, staging, prod)
- Local development may use overrides or mock values
- Flag state affects which code paths execute

**Mocking flags for development:**

If the flag hasn't been created in the third-party service yet, you may need to mock it locally to enable browser testing:
- Environment variable overrides (e.g., `FEATURE_X_ENABLED=true`)
- Local config file overrides
- Code-level defaults for development
- Browser localStorage/sessionStorage overrides

Document the mocking approach in VERIFICATION.md so testing can proceed before the flag is officially created.

**Environment validation:**
- Check if VERIFICATION.md or ARCHITECTURE.md mentions feature flags
- Identify the flag service being used
- Verify flag configuration for local environment:
  - Config files (e.g., `.env`, `flags.json`, `config/features.yaml`)
  - Environment variables
  - Service dashboard/API
- If flag doesn't exist yet, verify mock/override is in place
- Confirm required flags are enabled (or mocked) for the feature being built
- Report flag state so issues are caught before testing
