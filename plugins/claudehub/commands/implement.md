---
description: Implement from a plan or description
argument-hint: [plan file or description]
allowed-tools: Read, Write, Bash, Edit, AskUserQuestion, Glob, Task, Grep, TodoWrite, Skill
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `implementing` - execution methodology
- `researching-codebase` - understanding context when needed
- `writing-documentation` - summary file naming and frontmatter

## Process

1. Gather context (plan file from `.thoughts/plans/` or clarify description)

2. Assess confidence and present phases for confirmation

3. Create TodoWrite with confirmed phases

4. **Execute each phase task by task, updating the plan file continuously:**
   - Check off steps, tasks, and phases as you complete them
   - Update Tracked Changes for significant deviations
   - Update frontmatter status (planned → in-progress → completed)
   - See `implementing` skill references for detailed instructions

5. Run phase checks (tests, manual verification) after completing all tasks

6. Get user sign-off on manual checks before moving to next phase

7. Complete with full verification and summary to `.thoughts/implementations/`

Input: $ARGUMENTS
