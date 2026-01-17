---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Loop-Based Implementation

**Script:** `scripts/ralph-wiggum.sh`

Ralph Wiggum is a loop methodology that runs autonomous implementation iterations. Execute tasks from a plan file one at a time, learning from failures through a progress file.

## What Ralph Wiggum Does

The methodology:
1. Reads RALPH_PLAN.md (tasks) and RALPH_PROGRESS.md (learnings)
2. Finds first uncompleted task
3. Implements that task
4. Repeats until done or max iterations

Each iteration maintains tight context:
- RALPH_PLAN.md (task list + architecture)
- RALPH_PROGRESS.md (learnings + iteration log)
- No conversation history

## Output Signal

Use this promise tag when all tasks are complete:
- `<promise>COMPLETE</promise>` - All tasks checked off, implementation done

## Key Principle

One task per iteration. Tests must pass. Learn from failures. Software is clay on a wheel—iterate and refine.
