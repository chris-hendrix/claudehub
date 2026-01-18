---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: [plan-file]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum with LLM agent orchestration for intelligent decision-making.

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:ralph-wiggum` - Autonomous implementation methodology

## Process

1. Load the `claudehub:ralph-wiggum` skill using the Skill tool

2. Parse `$ARGUMENTS` for plan file path. If plan file path unclear, ask user.

3. Ask user: "Auto-commit changes after each iteration?" (suggest "Yes" as default). If yes:
   - Check current branch with `git branch --show-current`
   - Get default branch with `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@'`
   - If on default branch: Ask user if they want to create a new branch (suggest format: `ralph/short-description`), create and checkout if yes
   - Set auto_commit = true
   - Otherwise: Set auto_commit = false

4. Copy plan file to root `PLAN.md` and ensure Ralph settings in frontmatter:
   - Copy the plan content
   - Ensure frontmatter exists with these fields: `autocommit: [true/false from step 3]` and `parent-plan: [original plan path]`
   - Remove existing `PROGRESS.md` if it exists
   - Validate plan has unchecked tasks (lines starting with `- [ ]`)

5. Count unchecked tasks in PLAN.md with `grep -c '^- \[ \]' PLAN.md`, calculate suggested max iterations (1.5x task count), ask user to confirm

6. Main loop (iterate up to max_iterations):
   - Use the `ralph-task-implementer` agent with this input: "Iteration number: {iteration}. Find and implement the next unchecked task from PLAN.md."
   - Parse agent response for "Status:" line
   - If Status is COMPLETE: Stop and output summary
   - If Status is TASK_SUCCESS: Reset consecutive_failures = 0, last_failed_task = ""
   - If Status is TASK_FAILURE: Extract task identifier from response, check if same as last_failed_task, increment consecutive_failures if same (reset to 1 if different), stop if consecutive_failures >= 3
   - Increment iteration

7. Output final summary: iterations completed, final status, remaining tasks if incomplete

## Example Run

```
/ralph .thoughts/plans/my-feature.md

Loading ralph-wiggum skill...
Found 5 tasks in plan. Suggest 8 max iterations. Confirm?
> Use suggested (8)

Auto-commit changes after each successful iteration?
> Yes

Creating branch: ralph/my-feature
Copying plan to PLAN.md...

=== Iteration 1 ===
Spawning ralph-task-implementer agent...
[Agent implements Task 1]
Result: TASK_SUCCESS
Committed: "Ralph iteration 1: Task 1 - Add user model"

=== Iteration 2 ===
Spawning ralph-task-implementer agent...
[Agent implements Task 2]
Result: TASK_SUCCESS
Committed: "Ralph iteration 2: Task 2 - Add validation"

... continues ...

=== Summary ===
All tasks complete after 5 iterations.
```

Input: $ARGUMENTS
