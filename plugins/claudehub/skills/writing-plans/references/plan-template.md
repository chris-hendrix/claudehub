# Plan Template

Template structure for implementation plans. Save plans to `.thoughts/plans/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md` with this structure.

For methodology and guidelines on writing plans, see the parent SKILL.md file.

```markdown
---
date: YYYY-MM-DD
ticket: [ticket/issue number if applicable]
topic: Brief topic description
status: planned
---

# [Feature/Task Name] Implementation Plan

## Overview

[Brief description of what we're implementing and why. Include context about the problem this solves.]

## Success Criteria

How we'll know this implementation is complete and successful:

- [ ] [Functional requirement - e.g., "Users can log in with GitHub OAuth"]
- [ ] [Technical requirement - e.g., "All existing tests pass"]
- [ ] [Technical requirement - e.g., "All new tests pass"]
- [ ] [Quality requirement - e.g., "New feature has >80% test coverage"]
- [ ] [Quality requirement - e.g., "No linting errors - `npm run lint` passes"]
- [ ] [Quality requirement - e.g., "No type errors - `npm run type-check` passes"]
- [ ] [Documentation requirement - e.g., "README updated with new feature"]

## Current State

[What exists now - relevant files, patterns, and architecture]

**Relevant Files:**
- `path/to/file.ts:123` - Description of what this does
- `path/to/file2.ts:45` - Related component or pattern

**Key Discoveries:**
- [Important finding that impacts the plan]
- [Existing pattern to follow]
- [Constraint to work within]

## What We're NOT Doing

[Explicitly list out-of-scope items to prevent scope creep]

## Architecture

[High-level architecture and approach with enough detail for implementation but not full code]

**Database/Storage** (if applicable)
- [Schema changes, migrations, data model updates with key snippets]

**API/Backend** (if applicable)
- [Endpoints, services, business logic with function signatures]

**Frontend/UI** (if applicable)
- [Components, state management, user flows with component structure]

**Integration Points**
- [How parts connect, data flow, dependencies]

## Testing Strategy

**Test Types:**
- Unit tests: [What will be unit tested - models, utilities, pure functions]
- Integration tests: [What will be integration tested - API endpoints, database operations]
- E2E tests: [If applicable - critical user flows]

**Test Locations:**
- Unit tests: `src/**/*.test.ts` (co-located with implementation)
- Integration tests: `tests/integration/**/*.test.ts`
- E2E tests: `tests/e2e/**/*.test.ts`

**Testing Framework:** [Jest / Vitest / Mocha / etc.]

**Code Quality:**
- Linting: [ESLint / Biome / etc.] - command: `npm run lint`
- Type checking: [TypeScript] - command: `npm run type-check`
- Formatting: [Prettier / etc.] - command: `npm run format:check`

**Approach:**
- Set up empty test files first (Task 1)
- Add test cases as each task is implemented
- All tasks involving logic must update relevant tests
- Every task must ensure tests pass before marking complete
- Run linting and type checks as part of task verification

## QA Testing

QA checks are integrated into each task's verification steps (see Implementation Checklist below). Each task with e2e/integration tests includes a simple live validation check to ensure automated tests match real-world behavior.

## Implementation Checklist

> **Note:** This is a living document. As you implement, check off completed tasks and record significant changes in the "Tracked Changes" section below.
>
> Each task is a small, verifiable chunk of work. Tasks are sequential (may depend on previous tasks) but each is self-contained and verifiable. This structure enables tight feedback loops for autonomous implementation.
>
> **Phases are optional** - use only for larger features where logical grouping adds clarity.
>
> **Test-driven approach:** Task 1 typically sets up empty test files. Subsequent tasks add tests and implementation together.

### Phase 1: Test Setup

- [ ] **Task 1: Set up test files**
  - Step 1: Create `src/models/User.test.ts` with basic test structure
  - Step 2: Create `tests/integration/users.test.ts` for API endpoint tests
  - Step 3: Add test helper/fixture files if needed
  - Check 1: Run `npm test` - tests run (no failures, may have 0 tests initially)

### Phase 2: Database Setup

- [ ] **Task 2: Create database migration**
  - Step 1: Create migration file in `db/migrations/YYYYMMDD_add_users.sql`
  - Step 2: Add schema with users table (id, email, name, created_at)
  - Step 3: Add rollback logic to drop table
  - Check 1: Run `npm run migrate:up && npm run migrate:down` - migrations execute without errors

- [ ] **Task 3: Add user model with tests**
  - Step 1: Add test cases to `src/models/User.test.ts` for findById, create, update
  - Step 2: Create `src/models/User.ts` with User interface
  - Step 3: Add findById, create, update methods
  - Step 4: Follow pattern from `src/models/Auth.ts:15-45`
  - Check 1: Run `npm run type-check` - types pass
  - Check 2: Run `npm run lint` - no linting errors
  - Check 3: Run `npm test src/models/User.test.ts` - all tests pass

### Phase 3: API Implementation

- [ ] **Task 4: Create GET /api/users endpoint with tests**
  - Step 1: Add test cases to `tests/integration/users.test.ts` (200, 401, 403, pagination)
  - Step 2: Add route handler in `src/routes/users.ts`
  - Step 3: Implement pagination (limit, offset parameters)
  - Step 4: Add authorization check for admin role
  - Check 1: Run `npm run type-check` - types pass
  - Check 2: Run `npm test tests/integration/users.test.ts` - all cases pass
  - Check 3: Simple QA validation of GET /users endpoint live (test pagination, verify auth)

- [ ] **Task 5: Add input validation with tests**
  - Step 1: Add test cases with invalid payloads to `src/validation/users.test.ts`
  - Step 2: Create zod schemas in `src/validation/users.ts`
  - Step 3: Add validation middleware to user routes
  - Check 1: Run `npm run type-check` - types pass
  - Check 2: Run `npm test src/validation/users.test.ts` - validation catches all edge cases
  - Check 3: Run `npm test tests/integration/users.test.ts` - integration tests still pass
  - Check 4: Simple QA validation of input validation live (submit invalid data, verify error handling)

---

## Tracked Changes

> Record significant deviations from the plan during implementation. Include rationale for changes.

**[YYYY-MM-DD]** - [Description of change and why it was necessary]

**[YYYY-MM-DD]** - [Description of change and why it was necessary]

## References

- Original ticket/issue: [link or path]
- Related brainstorm: [link to brainstorm doc if exists]
- Similar implementation: `file:line`
```
