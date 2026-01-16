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

> **Note:** This is a living document. As you implement, check off completed items and record significant changes in the "Tracked Changes" section below.

- [ ] **Phase 1: [Phase Name - e.g., "Database & Backend Foundation"]**

  **Goal:** [What this phase accomplishes]

  - [ ] **Task 1.1: [Task Name - e.g., "Create database migration"]**
    - [ ] Step 1: [Specific action - e.g., "Create migration file in `db/migrations/`"]
    - [ ] Step 2: [Specific action - e.g., "Add schema changes for X"]
    - [ ] Step 3: [Specific action - e.g., "Test migration runs up and down"]

  - [ ] **Task 1.2: [Task Name]**
    - [ ] Step 1: [Specific action with file reference]
    - [ ] Step 2: [Specific action]

  - [ ] Check 1.1: Run automated tests for this phase
  - [ ] Check 1.2: Manually verify [specific behavior]

---

- [ ] **Phase 2: [Phase Name - e.g., "API Endpoints"]**

  **Goal:** [What this phase accomplishes]

  - [ ] **Task 2.1: [Task Name]**
    - [ ] Step 1: [Specific action]
    - [ ] Step 2: [Specific action]

  - [ ] **Task 2.2: [Task Name]**
    - [ ] Step 1: [Specific action]
    - [ ] Step 2: [Specific action]

  - [ ] Check 2.1: Run automated tests for this phase
  - [ ] Check 2.2: Manually verify [specific behavior]

---

- [ ] **Phase 3: [Phase Name - e.g., "Frontend Integration"]**

  **Goal:** [What this phase accomplishes]

  - [ ] **Task 3.1: [Task Name]**
    - [ ] Step 1: [Specific action]
    - [ ] Step 2: [Specific action]

  - [ ] **Task 3.2: [Task Name]**
    - [ ] Step 1: [Specific action]
    - [ ] Step 2: [Specific action]

  - [ ] Check 3.1: Run automated tests for this phase
  - [ ] Check 3.2: Manually verify [specific behavior]

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
