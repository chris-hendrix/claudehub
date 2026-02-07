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
- **Test-driven approach**: Plans include testing strategy; tests are set up first and updated as implementation progresses
- **Enough detail for LLM implementation**: Include code structure and patterns, not full code
- **Balance specificity with context**: Provide enough detail without consuming excessive context
- **Actionable and granular**: Break work down to specific actions an LLM can execute
- **Living document**: Checkboxes track progress; the plan is the source of truth across sessions
- **Automation-compatible**: Structure supports autonomous implementation through iterative loops

## Plan Structure

### Specification Sections (Beginning)

**Overview** - What we're building and why

**Success Criteria** - Requirements that must pass for implementation to be successful. Checkboxes for acceptance criteria (functional, technical, and documentation). These define "done" for the entire implementation, verified at the end. QA checks are integrated into individual tasks. Should include user-facing documentation updates.

**Current State** - Existing files, patterns, architecture (with `file:line` references)

**What We're NOT Doing** - Explicit scope boundaries

**Architecture** - Technical design with enough detail but not full code. Include relevant subsections:
- Database/Storage (if applicable) - Schema changes, migrations with key snippets
- API/Backend (if applicable) - Endpoints, services with function signatures
- Frontend/UI (if applicable) - Components, state management with component structure
- Integration Points - How parts connect, data flow

**Testing Strategy** - Define the testing approach for the implementation:
- What types of tests will be set up: unit, integration, e2e
- What will be tested at each level
- Test file locations and naming conventions
- Testing framework/tools to use
- Linting and code quality checks (e.g., ESLint, TypeScript, Prettier)
- This establishes the test-driven foundation: tests are set up first, then filled in as implementation progresses

**QA Testing** - QA checks are integrated into task-level verification:
- Each task with e2e/integration tests should include a simple QA check
- Validates that automated tests actually work in the running application
- Brief check tied directly to the test (e.g., "Simple QA: Test GET /users endpoint live")
- Performed as part of task completion for tight feedback loops

### Implementation Checklist (Core)

The **most important section**. Breaks work into **Phases → Tasks → Steps** with task-level verification.

**Test-driven approach**: The first task is typically "Set up test files" which creates empty test files with basic structure. Subsequent tasks add test cases and implementation in parallel. Each task that involves logic should update relevant tests before marking complete.

**Documentation approach**: User-facing documentation (README, guides, API docs) should be its own phase at the end, after implementation is complete. This ensures docs reflect the final implemented feature. Code-level documentation (docstrings, inline comments) should be part of the implementation tasks.

**Phases** (optional):
- Use `### Phase N: [Name]` headings to group related tasks
- Optional for small features/issues - use only when logical grouping adds clarity
- Each phase represents a major milestone or logical grouping
- Example: "### Phase 1: Database Setup", "### Phase 2: API Implementation"

**Tasks**:
- Small, verifiable chunk of work (e.g., "Add GET /users endpoint with pagination")
- Has checkbox - unchecked in plan, checked when complete during implementation
- Atomic unit that can be completed in one iteration (may depend on previous tasks)
- Self-contained and verifiable on its own
- Should be completable in one focused work session
- Usually touches 1-3 related files
- Numbered sequentially (Task 1, Task 2, Task 3...)
- **Automation-compatible**: One task per iteration
- Format: `- [ ] **Task N: [Description]**`

**Steps** (nested under tasks):
- No checkboxes - just actionable bullets
- Concrete and actionable (e.g., "Add route handler in `src/routes/users.ts`")
- Include file references when possible
- Format: `  - Step N: [Action]`

**Checks** (nested under tasks):
- Only include at task level (after all steps)
- Verification that proves the task is complete
- Should include code quality checks (e.g., "Run `npm run type-check` - types pass", "Run `npm run lint` - no errors")
- Should include test execution when task involves logic (e.g., "Run `npm test users.test.ts` - all tests pass")
- All relevant tests and quality checks must pass before marking task complete
- Should include simple QA validation for e2e/integration flows (e.g., "Simple QA: Test GET /users endpoint live with pagination")
- Exact command with success criteria
- Format: `  - Check N: [Command/verification] - [expected result]`

**Key principle:** Tasks are small, verifiable chunks. Implement steps → run checks → mark task complete → next task. This enables tight feedback loops for autonomous or manual execution.

**Success Criteria vs Task Checks:**
- **Success Criteria** = end-to-end requirements verified after all tasks complete (e.g., "feature works in running app", "all tests pass", "docs updated")
- **Task Checks** = verify individual task completion during implementation (e.g., "automated tests pass", "Simple QA validation of X")
- Success Criteria are the gate for "done"; task checks are the building blocks that get you there
- QA checks are integrated at task level for tight feedback loops

### Tracking Sections (End)

**Tracked Changes** - Record significant deviations during implementation with rationale

**References** - Links to tickets, brainstorms, similar implementations

## Planning Process

Planning is interactive, not linear. These phases may overlap:

### 1. Context Gathering

Research the codebase deeply. Read files fully, include `file:line` references, identify patterns to follow.

### 2. Deep-Dive Alignment (90% Confidence Gate)

**Do NOT write any planning documents until you reach 90% confidence.**

Use the deep-dive questioning process (see `references/deep-dive.md`) to build confidence through iterative question rounds. After each round, report your confidence level:
> "Current confidence: X%. [Reason for gaps if below 90%]"

Keep asking until you could explain the plan back and the user would say "yes, exactly." Cover:
- Requirements clarity and edge cases
- Technical decisions and integration points
- Scope boundaries (what's in, what's out)
- Testing and verification strategy (TDD mindset)

This is a hard gate — proceed to writing only at 90%+.

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
2. **Test-driven workflow** - For tasks involving logic:
   - Add/update test cases for new behavior
   - Implement the functionality
   - Run automated tests to verify correctness
   - Run simple QA check if task has e2e/integration tests
   - Only mark task complete when all checks pass
3. **Tight feedback loop** - implement steps → update tests → run automated checks → run QA check → mark complete → next task
4. **Record significant changes** in Tracked Changes:
   - Changed approach due to constraint
   - Added unexpected requirement
   - Discovered better pattern
   - Removed unnecessary work
5. **Don't record minor changes** like variable names

## Important Rules

1. **No open questions in final plan** - Research or ask before writing
2. **Verify everything** - Research to verify facts yourself
3. **Task-by-task verification** - Each task has exact verification command and success criteria
4. **Include scope boundaries** - Explicitly state what we're NOT doing
5. **QA checks in tasks** - Tasks with e2e/integration tests should include simple QA validation checks

## References

- `references/plan-template.md` - Full template with examples and hierarchy guidelines
- `references/deep-dive.md` - Deep-dive questioning categories and confidence progression
