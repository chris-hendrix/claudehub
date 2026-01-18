---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Agent-Orchestrated Loop Implementation

Ralph Wiggum is an agent-orchestrated loop methodology that runs autonomous implementation iterations. Execute tasks from a plan file one at a time, learning from failures through a progress file, with intelligent decision-making about retries and failures.

## Architecture

**Command:** `/ralph [plan-file]`
**Agent:** `ralph-task-implementer`

The orchestrator manages the outer loop with intelligent failure analysis, while the agent handles task discovery, implementation, and file updates.

## What Ralph Wiggum Does

The methodology:
1. **Orchestrator** reads PLAN.md to count tasks and ask user for max iterations
2. **Loop** (up to max iterations):
   - **Agent** finds first unchecked task in PLAN.md
   - **Agent** spawns inner Ralph to implement that specific task
   - **Agent** updates PLAN.md checkbox on success
   - **Agent** appends result to PROGRESS.md
   - **Agent** optionally creates git commit
   - **Orchestrator** analyzes result and decides whether to continue
3. **Orchestrator** stops when complete or after 3 consecutive failures on same task

Each iteration maintains tight context:
- PLAN.md (task list with frontmatter settings: `autocommit`, `parent-plan`)
- PROGRESS.md last 200 lines (learnings + iteration log)
- No conversation history

## Output Format

Each iteration produces structured markdown in PROGRESS.md:

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
---
```

Agent returns structured status to orchestrator:
```
Status: TASK_SUCCESS or TASK_FAILURE or COMPLETE
Task: [Task identifier]
Summary: [1-2 sentences explaining result]
Plan updated: Yes/No
Progress updated: Yes/No
Commit created: Yes/No/N/A
```

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

## Key Principle

One task per iteration. Tests must pass. Learn from failures. Software is clay on a wheel—iterate and refine.
