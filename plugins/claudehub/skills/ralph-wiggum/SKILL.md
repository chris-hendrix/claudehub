---
description: This skill should be used when implementing through autonomous loops with tight context windows. Ralph Wiggum runs one task per iteration, learns from failures, and maintains continuity through plan and progress files.
---

# Ralph Wiggum: Loop-Based Implementation

Ralph Wiggum is a loop methodology that runs autonomous implementation iterations. The script executes tasks from a plan file one at a time, learning from failures through a progress file.

## What Ralph Wiggum Does

The ralph.py script:
1. Reads plan file (tasks) and progress file (learnings)
2. Finds first uncompleted task
3. Invokes Claude to implement that task
4. Repeats until done or max iterations

Each iteration maintains tight context:
- Plan file (task list + architecture)
- Progress file (learnings + iteration log)
- No conversation history

## Output Signals

Watch for these in the script output:
- `<promise>TASK_COMPLETE</promise>` - Task done, tests passed
- `<promise>TASK_FAILED</promise>` - Task failed, documented for next iteration
- `<promise>ALL_COMPLETE</promise>` - All tasks complete

## Key Principle

One task per iteration. Tests must pass. Learn from failures. Software is clay on a wheel—iterate and refine.

## Running Ralph Wiggum

You can run this process using `scripts/ralph_wiggum.py`
