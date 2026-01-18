---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Loop-Based Implementation

**Script:** `scripts/ralph-wiggum.sh`

Ralph Wiggum is a loop methodology that runs autonomous implementation iterations. Execute tasks from a plan file one at a time, learning from failures through a progress file.

## What Ralph Wiggum Does

The methodology:
1. Reads PLAN.md (tasks) and PROGRESS.md (learnings)
2. Finds first uncompleted task
3. Implements that task
4. Repeats until done or max iterations

Each iteration maintains tight context:
- PLAN.md (task list + architecture)
- PROGRESS.md (learnings + iteration log)
- No conversation history

## Output Signals

Use these promise tags to communicate status:
- `<promise>TASK_COMPLETE</promise>` - Current task completed successfully, tests passed
- `<promise>COMPLETE</promise>` - All tasks checked off, implementation done

## Optional Auto-Commit

Ralph can automatically commit after each successful task completion:
- Pass "commit" as third argument to script
- Creates commits with task info after each successful iteration
- Useful for tracking progress and enabling easy rollback

## Key Principle

One task per iteration. Tests must pass. Learn from failures. Software is clay on a wheel—iterate and refine.
