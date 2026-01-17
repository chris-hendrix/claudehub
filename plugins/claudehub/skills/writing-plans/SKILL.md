---
name: writing-plans
description: This skill should be used when the user wants to "create a plan", "write an implementation plan", "plan a feature", "design a solution", "plan implementation", mentions "implementation plan", "technical plan", "architecture plan", or is working on creating detailed implementation plans for features or changes.
version: 1.0.0
allowed-tools: Write, Read, Bash, AskUserQuestion, Glob, Task, Grep, TodoWrite
---

# Writing Implementation Plans

Create detailed, actionable implementation plans with enough specificity for an LLM to implement.

**For file naming and frontmatter**: See the `writing-documentation` skill.

**Location**: Plans are always saved to `.thoughts/plans/`

## Purpose

Plans are for **diving into the solution**. They bridge the gap between a validated design (from brainstorming) and actual implementation.

**Critical: Plans are designed for multi-session implementation.** The entire implementation is too large for a single LLM context window. The plan serves as the persistent source of truth that allows work to be resumed across multiple sessions.

A good plan has:

1. **Architecture specification** - Self-contained context: all technical details needed to implement without conversation history
2. **Implementation checklist** - Granular breakdown into tasks with inline verification for tight feedback loops
3. **Living document** - Checkboxes show progress; any session can pick up where the last one left off

## Philosophy

- **Self-contained context**: Architecture section must include all details needed to implement without prior conversation history
- **Task-level verification**: Each task is independently verifiable with inline checks for tight feedback loops
- **Enough detail for LLM implementation**: Include code structure and patterns, not full code
- **Balance specificity with context**: Provide enough detail without consuming excessive context
- **Actionable and granular**: Break work down to specific actions an LLM can execute
- **Living document**: Checkboxes track progress; the plan is the source of truth across sessions
- **Ralph-compatible**: Structure supports autonomous implementation through iterative loops

## Plan Structure

### Specification Sections (Beginning)

**Overview** - What we're building and why

**Current State** - Existing files, patterns, architecture (with `file:line` references)

**What We're NOT Doing** - Explicit scope boundaries

**Architecture** - Technical design with enough detail but not full code. Include relevant subsections:
- Database/Storage (if applicable) - Schema changes, migrations with key snippets
- API/Backend (if applicable) - Endpoints, services with function signatures
- Frontend/UI (if applicable) - Components, state management with component structure
- Integration Points - How parts connect, data flow

### Implementation Checklist (Core)

The **most important section**. Breaks work into **Tasks → Steps → Checks** with inline verification:

- **Task**: A small, verifiable chunk of work (e.g., "Add GET /users endpoint with pagination")
  - Has checkbox - checked when all steps and checks complete
  - Atomic unit that can be completed in one iteration (may depend on previous tasks)
  - Self-contained and verifiable on its own
  - Should be completable in one focused work session
  - Usually touches 1-3 related files
  - Numbered sequentially (Task 1, Task 2, Task 3...)
  - **Ralph compatibility**: One task per Ralph iteration

- **Step**: Specific action within a task
  - Has checkbox - checked when action complete
  - Concrete and actionable (e.g., "Add route handler in `src/routes/users.ts`")
  - Include file references when possible

- **Check**: Verification that proves the task is complete
  - Has checkbox - checked when verification passes
  - Appears inline after steps within each task
  - Exact command with success criteria (e.g., "Run `npm test users.test.ts` - all tests pass")
  - Numbered per check (Check 1, Check 2, etc.)

**Key principle:** Tasks are small, verifiable chunks. Implement steps → run checks → verify complete → next task. This enables tight feedback loops for autonomous implementation (Ralph) or manual execution.

### Tracking Sections (End)

**Tracked Changes** - Record significant deviations during implementation with rationale

**References** - Links to tickets, brainstorms, similar implementations

## Planning Process

Planning is interactive, not linear. These phases may overlap:

### 1. Context Gathering

Research the codebase deeply. Read files fully, include `file:line` references, identify patterns to follow.

### 2. Resolving Ambiguity

Surface unstated assumptions by identifying:
- Edge cases and error handling
- Integration points and dependencies
- Scope boundaries
- Technical constraints
- Backward compatibility concerns

Ask questions clearly and wait for answers.

### 3. Iterative Writing

Don't write the full plan in one shot. Propose structure first, get feedback, then fill in details. Present:
- High-level task breakdown
- Key architectural decisions
- Any concerns or risks

**Wait for user confirmation** before diving into detailed checklist.

## Code Snippets in Architecture

Include code structure to show patterns, not full implementation:

**Good:**
```typescript
async function handleUserCreate(req: Request): Promise<Response> {
  // 1. Validate input with zod schema
  // 2. Check authorization
  // 3. Create user in DB
  // 4. Return user object
}
```

**Bad (too much detail):**
```typescript
async function handleUserCreate(req: Request): Promise<Response> {
  const schema = z.object({ name: z.string(), email: z.string().email() })
  const validated = schema.parse(req.body)
  if (!req.user?.isAdmin) throw new Error('Unauthorized')
  // ... full implementation
}
```

## Living Document During Implementation

As you implement from the plan:

1. **Check off items at all levels** as completed: `- [ ]` → `- [x]`
   - Check steps as you complete each action
   - Check task-level checks after running verification commands
   - Check tasks when all their steps and checks are done
2. **Tight feedback loop** - implement steps → run checks → mark complete → next task
3. **Record significant changes** in Tracked Changes:
   - Changed approach due to constraint
   - Added unexpected requirement
   - Discovered better pattern
   - Removed unnecessary work
4. **Don't record minor changes** like variable names

## Important Rules

1. **No open questions in final plan** - Research or ask before writing
2. **Verify everything** - Research to verify facts yourself
3. **Task-by-task verification** - Each task has exact verification command and success criteria
4. **Include scope boundaries** - Explicitly state what we're NOT doing

## References

- `references/plan-template.md` - Full template with examples and hierarchy guidelines
