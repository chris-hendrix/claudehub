# Context Files

These files are loaded at the start of each Ralph iteration to provide context. Created by `/ralph:deep-plan` or `/ralph:quick-plan`.

## ARCHITECTURE.md

Technical approach for the feature. Structure based on what the feature needs - no fixed template.

**Always include:**
- Overview (1-2 sentences)
- Testing strategy (unit, integration, E2E, manual)
- Enough detail that a developer could implement without asking questions

**Common sections** (include what's relevant):
- BE services - backend services, business logic
- DB schema - database changes, migrations
- API contracts - endpoints, request/response schemas
- FE components - UI components, pages, routes
- Dependencies - external systems, third-party services
- Feature flags - flag names, registration locations

**Be specific:**
- Exact file paths, not "somewhere in components/"
- Code snippets (TypeScript interfaces, GraphQL queries, etc.)
- Component hierarchies as tree structures when relevant
- Integration points showing WHERE to make changes

**Sections emerge from the feature** - a frontend migration needs component details and routes; a backend service needs API contracts and database schema. Let the feature dictate the structure.

## TASKS.md

Three-level hierarchy: **Phase → Task → Step**

### Phases

Logical groupings (e.g., "Database Layer", "API Endpoints", "UI Components")
- Each phase groups related tasks
- Final phase is always "Final Verification" to run all tests and catch regressions

### Tasks

A unit of work Ralph completes in one iteration
- Each task includes implementation AND tests for that implementation
- Tests are written alongside code (TDD), not deferred to later
- Task is not done until its tests pass
- Each task runs full test suite to catch regressions early

### Steps

Sub-bullets under each task specifying exactly what to do:
- `Implement:` - specific code to write
- `Test:` - specific tests to write (unit, integration, E2E as appropriate)
- `Seed:` - (optional) specific data to create for manual testing
- `Verify:` - what to check passes (always includes running full test suite)

### TDD Philosophy

Tests are written WITH implementation, not after:
- Backend service task → include unit/integration tests in that task
- UI component task → include component tests in that task
- User flow task → include E2E test AND manual testing with screenshots
- Every task verifies no regression (runs full suite)
- Final phase only RUNS existing tests - no new tests written there

**When E2E is required, manual browser testing is also required.** E2E tests prove the code runs; manual testing proves it looks/works right. Screenshots provide visual proof.

### Anti-patterns

- ❌ "Phase 3: Testing" - never create a separate testing phase
- ❌ "Task 4.1: Write E2E tests" - E2E tests go with the UI tasks they test
- ❌ "Task 5.2: Add manual test coverage" - manual tests go with the features they verify
- ✅ Each task is self-contained: implement → test → verify

### Example

```markdown
## Phase 1: [Phase Name]

- [ ] Task 1.1: [Task description]
  - Implement: [specific code/file to create or modify]
  - Test: [unit test for this code]
  - Test: [integration test if applicable]
  - Verify: run full test suite, all tests pass

- [ ] Task 1.2: [Task description with UI]
  - Implement: [component code]
  - Test: [component test]
  - Test: [E2E test for user flow]
  - Seed: [create test user/data needed for manual testing]
  - Verify: run full test suite, all tests pass
  - Verify: manual test [specific flow], screenshot each step

## Phase 2: [Phase Name]

- [ ] Task 2.1: [Task description]
  - Implement: [code]
  - Test: [tests for this code]
  - Verify: run full test suite, all tests pass

## Phase N: Final Verification

- [ ] Task N.1: Full regression check
  - Verify: all unit tests pass
  - Verify: all integration tests pass
  - Verify: all E2E tests pass
  - Verify: linting and type checking pass

- [ ] Task N.2: Full manual smoke test
  - Verify: [complete user flow 1], screenshot each step
  - Verify: [complete user flow 2], screenshot each step
  - Verify: [edge case scenario], screenshot each step
```

## PROGRESS.md

Each iteration appends a report:

```markdown
## Iteration N - Task X.Y: [Task Name]

**Status:** SUCCESS / FAILURE
**Research:** [Key findings]
**Implementation:** [What was built]
**Verification:** [Check results]
**Review:** [Assessment and notes]
**Learnings:** [What to remember for future tasks]
```

### Screenshots

Reference screenshots captured during manual testing:

```markdown
**Screenshots:**
- `iteration-001-login-form-displayed.png` - Initial form state
- `iteration-001-validation-error-shown.png` - Email validation working
```

## VERIFICATION.md

Environment setup and test commands. Structure varies by project but typically includes:

- **Environment setup** - How to run the app locally
- **Test commands** - Commands for each test type (unit, integration, E2E, lint, typecheck)
- **Ports and URLs** - Local service addresses
- **Test credentials** - Accounts for manual testing
- **Feature flags** - Flags that must be enabled for the feature
- **Seed data** - How to create test data
