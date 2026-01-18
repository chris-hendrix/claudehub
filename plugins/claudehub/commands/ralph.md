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

5. Determine starting iteration number:
   - If PROGRESS.md exists: Extract last iteration number from lines like "## Iteration [N] -" using `grep '^## Iteration' PROGRESS.md | tail -1 | sed 's/^## Iteration \([0-9]*\) -.*/\1/'`
   - Set current_iteration = (last_iteration + 1), or 1 if PROGRESS.md doesn't exist or has no iterations

6. Count unchecked tasks in PLAN.md with `grep -c '^- \[ \]' PLAN.md`, calculate suggested new iterations (1.5x task count), ask user to confirm:
   - Format: "Found X unchecked tasks. Suggest running Y new iterations (total: Z). Confirm?"
   - Where Y = suggested new iterations (1.5x unchecked tasks), Z = current_iteration - 1 + Y

7. Main loop (iterate up to max_total_iterations):
   - Use the `ralph-worker` agent with this input: "Iteration number: {current_iteration}. Find and implement the next unchecked task from PLAN.md."
   - Parse agent response:
     - If output contains "Status: COMPLETE": Stop and output summary
     - If output contains "Result: TASK_SUCCESS": Reset consecutive_failures = 0, last_failed_task = ""
     - If output contains "Result: TASK_FAILURE": Extract task identifier from "## Iteration [N] - Task [M]: [Title]" line, check if same as last_failed_task, increment consecutive_failures if same (reset to 1 if different), stop if consecutive_failures >= 3
   - Increment current_iteration

8. Output final summary: iterations completed, final status, remaining tasks if incomplete

## Example Run

```
/ralph .thoughts/plans/my-feature.md

Loading ralph-wiggum skill...
Found 5 unchecked tasks. Suggest running 8 new iterations (total: 8). Confirm?
> Use suggested (8 new iterations)

Auto-commit changes after each iteration?
> Yes

Creating branch: ralph/my-feature
Copying plan to PLAN.md...

=== Iteration 1 ===
Spawning ralph-worker agent...

## Iteration 1 - Task 1: Add user model
- Result: TASK_SUCCESS
- What was implemented: Created User model with email, password hash, and timestamps
- What was tested: Ran unit tests with `npm test`, all 8 tests passing
- Context usage: 35K tokens
- Learnings for future iterations:
  - Project uses TypeORM for database models
  - Validation decorators from class-validator
  - Tests in __tests__/models/ directory

Committed: "Ralph iteration 1: Add user model - TASK_SUCCESS"

=== Iteration 2 ===
Spawning ralph-worker agent...

## Iteration 2 - Task 2: Add input validation
- Result: TASK_SUCCESS
- What was implemented: Added validation middleware using existing validator setup
- What was tested: Ran validation tests, all 12 tests passing
- Context usage: 41K tokens
- Learnings for future iterations:
  - Validation middleware in src/middleware/
  - Pattern matches auth validation approach
  - Express middleware chain requires next() calls

Committed: "Ralph iteration 2: Add input validation - TASK_SUCCESS"

... continues ...

=== Summary ===
All tasks complete after 5 iterations.
5 tasks implemented successfully.
```

Input: $ARGUMENTS
