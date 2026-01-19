---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Agent-Orchestrated Loop Implementation

Ralph Wiggum is an agent-orchestrated loop methodology that runs autonomous implementation iterations. Execute tasks from a plan file one at a time, learning from failures through a progress file, with intelligent decision-making about retries and failures.

## Architecture

**Command:** `/ralph [plan-file]`
**Agents:**
- `ralph-preparer` - Sets up PLAN.md and PROGRESS.md, handles git branching and initial commit
- `ralph-worker` - Implements individual tasks

The orchestrator manages the outer loop with intelligent failure analysis. The preparer agent handles all setup, and the worker agent handles task discovery, direct implementation, and file updates.

## What Ralph Wiggum Does

The methodology:
1. **Preparation Phase**:
   - **Orchestrator** spawns `ralph-preparer` agent with plan file path
   - **Preparer** checks if PLAN.md exists to determine fresh start vs resume
   - **If resuming (PLAN.md exists)**:
     - Read autocommit setting from PLAN.md frontmatter
     - Determine starting iteration from PROGRESS.md (last iteration + 1)
     - Skip all setup questions
   - **If fresh start (PLAN.md missing)**:
     - Ask user about autocommit and git branching
     - Copy plan to PLAN.md with frontmatter settings
     - Create empty PROGRESS.md
     - Create initial commit (if autocommit enabled)
   - **Preparer** returns configuration (mode, starting iteration, unchecked task count)
2. **Planning Phase**:
   - **Orchestrator** calculates suggested iterations (1.5x unchecked tasks)
   - **Orchestrator** asks user to confirm max iterations
3. **Implementation Loop** (up to max iterations):
   - **Orchestrator** spawns fresh `ralph-worker` agent with iteration number
   - **Worker** verifies PLAN.md and PROGRESS.md exist (exits with error if missing)
   - **Worker** finds first unchecked task in PLAN.md
   - **Worker** implements task directly using tools (Read, Edit, Bash, Grep)
   - **Worker** runs all checks (tests, linting, type-check, QA)
   - **Worker** updates PLAN.md checkbox on success (all checks pass)
   - **Worker** appends iteration report to PROGRESS.md
   - **Worker** creates git commit if autocommit enabled
   - **Worker** returns iteration report
   - **Orchestrator** parses result and decides whether to continue
4. **Orchestrator** stops when:
   - Worker returns "Status: ERROR" (missing required files)
   - Worker returns "Status: COMPLETE" (no unchecked tasks)
   - 3 consecutive failures on same task

Each worker spawn gets fresh context:
- PLAN.md (task list with frontmatter settings: `autocommit`, `parent-plan`)
- PROGRESS.md last 200 lines (learnings from previous iterations)
- Fresh ~200K token budget (no accumulated context from previous tasks)

## Output Format

Worker agent outputs iteration report that gets appended to PROGRESS.md:

```markdown
## Iteration [N] - Task [M]: [Task Name]
- Result: TASK_SUCCESS or TASK_FAILURE
- What was implemented: [1-2 sentences]
- Checks run: [Which checks were run and their results]
- Context usage: [context usage]
- Learnings for future iterations:
  - [Patterns discovered]
  - [Gotchas encountered]
  - [For failures: What failed and how to fix it]
  - [Useful context]
```

Special case - when no unchecked tasks remain:
```
Status: COMPLETE
```

Orchestrator parses the `Result:` field to determine success/failure and make continuation decisions.

## Resumability

Ralph is fully resumable. You can stop and restart anytime:
- **First run**: Creates PLAN.md and PROGRESS.md, starts from iteration 1
- **Resume run**: Detects existing PLAN.md, reads last iteration from PROGRESS.md, continues where it left off
- All settings (autocommit, parent-plan) stored in PLAN.md frontmatter
- PROGRESS.md tracks full history across sessions

Stop Ralph anytime (Ctrl+C, timeout, failure limit) and restart with same command - it picks up automatically.

## Auto-Commit

Ralph can automatically commit after each iteration (success or failure):
- Controlled by `autocommit: true/false` in PLAN.md frontmatter
- User is prompted on fresh start (default: Yes)
- On resume, uses existing setting from PLAN.md
- Creates commits with format: "Ralph iteration N: [task] - [Result]"
- Useful for tracking progress and enabling easy rollback

## Intelligent Failure Handling

The orchestrator reasons about failures:
- Tracks consecutive failures per task
- Stops after 3 consecutive failures on same task
- Allows Ralph to retry with learnings from PROGRESS.md
- Different from blind retry - uses context to improve

## Key Principles

- **One task per spawn**: Each worker agent implements exactly one task then terminates
- **Context isolation**: Fresh agent spawn prevents context rot across iterations
- **Tests must pass**: Only mark complete when verification succeeds
- **Learn from failures**: Document what happened so next iteration can adapt
- **Software is clay**: Iterate and refine through tight feedback loops

## Architecture Benefits

**Why spawn fresh workers instead of one long-running agent?**

Context isolation. If a single agent implemented all tasks sequentially:
- Iteration 1: 40K tokens used
- Iteration 2: 40K new + 40K old = 80K tokens
- Iteration 10: 400K tokens of accumulated context

By spawning fresh workers:
- Each task gets clean 200K budget
- Worker only sees: PLAN.md + last 200 lines of PROGRESS.md
- No pollution from unrelated previous work
- Consistent decision-making quality across all iterations
