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
- [ ] [Quality requirement - e.g., "New feature has >80% test coverage"]
- [ ] [Technical requirement - e.g., "No TypeScript/linting errors"]
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

## Implementation Checklist

> **Note:** This is a living document. As you implement, check off completed tasks and record significant changes in the "Tracked Changes" section below.
>
> Each task is a small, verifiable chunk of work. Tasks are sequential (may depend on previous tasks) but each is self-contained and verifiable. This structure enables tight feedback loops for autonomous implementation.
>
> **Phases are optional** - use only for larger features where logical grouping adds clarity.

### Phase 1: Database Setup

- [ ] **Task 1: Create database migration**
  - Step 1: Create migration file in `db/migrations/YYYYMMDD_add_users.sql`
  - Step 2: Add schema with users table (id, email, name, created_at)
  - Step 3: Add rollback logic to drop table
  - Check 1: Run `npm run migrate:up && npm run migrate:down` - migrations execute without errors

- [ ] **Task 2: Add user model**
  - Step 1: Create `src/models/User.ts` with User interface
  - Step 2: Add findById, create, update methods
  - Step 3: Follow pattern from `src/models/Auth.ts:15-45`
  - Check 1: Run `npm run type-check` - types pass
  - Check 2: Run `npm test src/models/User.test.ts` - all tests pass

### Phase 2: API Implementation

- [ ] **Task 3: Create GET /api/users endpoint**
  - Step 1: Add route handler in `src/routes/users.ts`
  - Step 2: Implement pagination (limit, offset parameters)
  - Step 3: Add authorization check for admin role
  - Check 1: Run `npm test src/routes/users.test.ts` - all cases pass (200, 401, 403)

- [ ] **Task 4: Add input validation**
  - Step 1: Create zod schemas in `src/validation/users.ts`
  - Step 2: Add validation middleware to user routes
  - Step 3: Add test cases with invalid payloads
  - Check 1: Run `npm test src/validation/users.test.ts` - validation catches all edge cases

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
