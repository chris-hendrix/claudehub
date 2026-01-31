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

**Tools:**
- Playwright MCP (for LLM-driven browser control)
- Human testing

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
- Check Playwright MCP is available
- Verify app loads at URL
- Attempt login with test credentials if provided
- Verify required feature flags are enabled (see Feature Flags section)
- Navigate to relevant pages and confirm feature is visible

## API/Backend Verification

Testing backend endpoints directly.

**Tools:**
- curl
- httpie
- Postman/Newman

**Characteristics:**
- Requires backend running
- May require authentication tokens

**Environment validation:**
- Check endpoint is reachable
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
