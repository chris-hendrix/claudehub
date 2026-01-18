---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Agent-Orchestrated Loop Implementation

Ralph Wiggum is an agent-orchestrated loop methodology that runs autonomous implementation iterations. Execute tasks from a plan file one at a time, learning from failures through a progress file, with intelligent decision-making about retries and failures.

## Architecture

**Command:** `/ralph [plan-file]`
**Agent:** `ralph-worker`

The orchestrator manages the outer loop with intelligent failure analysis, while the worker agent handles task discovery, direct implementation, and file updates.

## What Ralph Wiggum Does

The methodology:
1. **Orchestrator** determines starting iteration from PROGRESS.md, counts unchecked tasks, asks user for max iterations
2. **Loop** (up to max iterations):
   - **Orchestrator** spawns fresh `ralph-worker` agent with iteration number
   - **Worker** finds first unchecked task in PLAN.md
   - **Worker** implements task directly using tools (Read, Edit, Bash, Grep)
   - **Worker** runs tests
   - **Worker** updates PLAN.md checkbox on success
   - **Worker** appends iteration report to PROGRESS.md
   - **Worker** creates git commit if autocommit enabled
   - **Worker** returns iteration report
   - **Orchestrator** parses result and decides whether to continue
3. **Orchestrator** stops when complete or after 3 consecutive failures on same task

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
- What was tested: [1-2 sentences]
- Context usage: [context usage]
- Learnings for future iterations:
  - [Patterns discovered]
  - [Gotchas encountered]
  - [Useful context]
```

Special case - when no unchecked tasks remain:
```
Status: COMPLETE
```

Orchestrator parses the `Result:` field to determine success/failure and make continuation decisions.

## Auto-Commit

Ralph can automatically commit after each iteration (success or failure):
- Controlled by `autocommit: true/false` in PLAN.md frontmatter
- User is prompted when running `/ralph` (default: Yes)
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
