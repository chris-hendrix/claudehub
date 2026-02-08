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

**CRITICAL FORMAT REQUIREMENTS:**

1. **Phases** are H2 headers: `## Phase 1: Database Layer`
2. **Tasks** are CHECKBOX LIST ITEMS: `- [ ] Task 1.1: Define schemas` (NOT headings like `### 1.1`)
3. **Steps** are INDENTED BULLETS WITHOUT CHECKBOXES: `  - Implement: Create schema file` (NOT `  - [ ] Create schema file`)

**CHECKBOX PLACEMENT - THIS IS NON-NEGOTIABLE:**
- ✅ Checkboxes ONLY on task lines (e.g., `- [ ] Task 1.1: Description`)
- ❌ NEVER put checkboxes on step lines (the indented bullets under tasks)
- ❌ NEVER make task numbers into headings (### 1.1)

Ralph's orchestrator finds the next task by searching for `- [ ]` at the start of a line. If you put checkboxes on steps instead of tasks, Ralph will try to complete individual steps instead of complete tasks, breaking the workflow.

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
- **Format:** `- [ ] Task X.Y: Brief description of what this task accomplishes`

### Task Granularity

Choose granularity based on how you want to track progress:

**Small (Recommended)**: Smallest chunks of verifiable work
- Each task is highly focused with minimal scope
- Example: "Create user schema", "Add user endpoints", "Write user tests" as separate tasks
- Pros: Clear progress, catch issues early, easier to resume after interruptions
- Cons: More tasks to manage, more PROGRESS.md entries

**Medium**: Balanced task sizes
- Each task covers a complete feature component
- Example: "Implement user service with endpoints and tests"
- Pros: Good balance between granularity and task count
- Cons: Less granular progress tracking

**Large**: Fewer, larger tasks
- Each task covers significant functionality
- Example: "Implement complete authentication system with all endpoints, middleware, and tests"
- Pros: Fewer tasks to track, less overhead
- Cons: Takes longer per task, harder to isolate issues, less frequent progress milestones

### Steps

Sub-bullets under each task specifying exactly what to do:
- **Format:** Two-space indent, bullet (no checkbox), prefix label
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

### Granularity Examples

Same feature broken down at different granularities:

**SMALL Granularity** (6 tasks for auth feature):
```markdown
## Phase 1: Authentication

- [ ] Task 1.1: Create user database schema
  - Implement: Create `schema/users.ts` with users table
  - Test: Verify schema compiles
  - Verify: run full test suite

- [ ] Task 1.2: Create auth service
  - Implement: Create `services/auth.service.ts` with token generation
  - Test: Write unit tests for token methods
  - Verify: run full test suite

- [ ] Task 1.3: Create auth controller
  - Implement: Create `controllers/auth.controller.ts` with login/logout
  - Test: Write controller unit tests
  - Verify: run full test suite

- [ ] Task 1.4: Add auth routes
  - Implement: Create `routes/auth.routes.ts` and register in server
  - Test: Write integration tests for endpoints
  - Verify: run full test suite

- [ ] Task 1.5: Create auth middleware
  - Implement: Create `middleware/auth.middleware.ts` for JWT verification
  - Test: Write middleware unit tests
  - Verify: run full test suite

- [ ] Task 1.6: Add frontend auth flow
  - Implement: Create login page and auth context
  - Test: Write component tests and E2E test
  - Verify: run full test suite, manual test with screenshots
```

**MEDIUM Granularity** (3 tasks for auth feature):
```markdown
## Phase 1: Authentication

- [ ] Task 1.1: Implement backend auth system
  - Implement: Create user schema, auth service, and controller
  - Test: Write unit tests for service and controller
  - Test: Write integration tests for auth endpoints
  - Verify: run full test suite

- [ ] Task 1.2: Add auth middleware and routes
  - Implement: Create auth middleware and register routes
  - Test: Write middleware unit tests and endpoint integration tests
  - Verify: run full test suite

- [ ] Task 1.3: Build frontend auth UI
  - Implement: Create login page, auth context, and API client
  - Test: Write component tests and E2E test for login flow
  - Verify: run full test suite, manual test with screenshots
```

**LARGE Granularity** (1 task for auth feature):
```markdown
## Phase 1: Authentication

- [ ] Task 1.1: Implement complete authentication system
  - Implement: Create user schema, auth service, controller, middleware, and routes
  - Implement: Create login page, auth context, and API integration
  - Test: Write unit tests for all backend components
  - Test: Write integration tests for auth endpoints
  - Test: Write component tests and E2E test for frontend flow
  - Verify: run full test suite, manual test with screenshots
```

### Example - CORRECT FORMAT

```markdown
## Phase 1: Database Layer

- [ ] Task 1.1: Define Drizzle schemas
  - Implement: Create `apps/api/src/db/schema/users.ts` with users table schema
  - Implement: Create `apps/api/src/db/schema/trips.ts` with trips table schema
  - Test: Verify schema compilation with `pnpm typecheck`
  - Verify: run full test suite, all tests pass

- [ ] Task 1.2: Generate and run migrations
  - Implement: Run `pnpm db:generate` to create migration SQL
  - Implement: Run `pnpm db:migrate` to apply migration
  - Test: Write integration test to verify tables exist
  - Verify: run full test suite, all tests pass
  - Verify: manual check using Drizzle Studio

## Phase 2: API Endpoints

- [ ] Task 2.1: Create auth endpoints
  - Implement: Create `src/routes/auth.routes.ts` and controller
  - Test: Write integration tests for POST /api/auth/request-code
  - Test: Write integration tests for POST /api/auth/verify-code
  - Verify: run full test suite, all tests pass

## Phase N: Final Verification

- [ ] Task N.1: Full regression check
  - Verify: all unit tests pass
  - Verify: all integration tests pass
  - Verify: all E2E tests pass
  - Verify: linting and type checking pass
```

### WRONG FORMAT - DO NOT DO THIS

```markdown
## Phase 1: Database Layer

### 1.1 Define Drizzle schemas                    ❌ WRONG: Task is a heading
- [ ] Create users table schema                   ❌ WRONG: Checkbox on step
- [ ] Create trips table schema                   ❌ WRONG: Checkbox on step

### 1.2 Generate migrations                       ❌ WRONG: Task is a heading
- [ ] Run pnpm db:generate                        ❌ WRONG: Checkbox on step
- [ ] Run pnpm db:migrate                         ❌ WRONG: Checkbox on step
```

**Why this breaks Ralph:** Ralph's `find_next_task()` searches for lines starting with `- [ ]`. In the wrong format, it finds "Create users table schema" instead of "Task 1.1: Define Drizzle schemas", causing Ralph to work on individual steps instead of complete tasks.

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
