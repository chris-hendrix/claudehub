---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: [plan-file] [--max-iterations N] [--commit]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum to implement plan tasks iteratively.

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `ralph-wiggum` - Autonomous implementation methodology (see references for iteration loop and failure handling)

## Process

1. Load the `ralph-wiggum` skill using the Skill tool first (required)

2. Gather inputs if not provided:
   - Plan file path (search `.thoughts/plans/` for recent plans if needed)
   - Max iterations (suggest: 10)
   - Auto-commit flag (suggest: false)

3. **Branch safety**: If --commit flag is used and on default branch, suggest `ralph/<plan-name>` branch and STOP

4. Follow the Ralph Wiggum iteration loop methodology (see `references/ralph-iteration-loop.md`):
   - Setup: Verify plan file, create progress file if needed
   - Loop: Work through tasks one at a time, updating files after each
   - Report: Keep user informed of progress after each iteration
   - Stop: When all tasks complete or max iterations reached

Input: $ARGUMENTS
