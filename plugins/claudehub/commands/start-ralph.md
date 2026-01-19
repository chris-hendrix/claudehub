---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: [plan-file]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum with LLM agent orchestration for intelligent decision-making.

**Usage:**
- First run: `/ralph <plan-file>` - Starts fresh implementation
- Resume: `/ralph` or `/ralph <plan-file>` - Continues from where you left off (if PLAN.md exists)

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:ralph-wiggum` - Autonomous implementation methodology

## Process

1. Load the `claudehub:ralph-wiggum` skill using the Skill tool

2. Parse `$ARGUMENTS` for plan file path:
   - If PLAN.md exists in current directory: resuming mode (plan file path optional - preparer will use existing PLAN.md)
   - If PLAN.md does not exist: fresh start (plan file path required - ask user if not provided)

3. Use the `ralph-preparer` agent to set up or resume:
   - Input: "Prepare Ralph for execution. Plan file: {path}"
   - Agent handles:
     - Detects fresh start vs resume (checks if PLAN.md exists)
     - If fresh start: asks about git branch/autocommit, creates files, initial commit
     - If resume: reads config from PLAN.md frontmatter, extracts last iteration from PROGRESS.md
     - Counts total and remaining tasks
     - Asks user to confirm max iterations
   - Parse agent output to extract:
     - starting_iteration (from "Starting iteration: {N}")
     - max_iterations (from "Max iterations: {N}")
   - Verify output contains "Status: READY" before proceeding

4. Main loop:
   - Set current_iteration = starting_iteration
   - Loop while current_iteration <= max_iterations:
     - Use the `ralph-worker` agent with this input: "Iteration number: {current_iteration}. Find and implement the next unchecked task from PLAN.md."
     - Parse agent response:
       - If output contains "Status: ERROR": Output error message and stop immediately
       - If output contains "Status: COMPLETE": Stop and output summary
       - If output contains "Result: TASK_SUCCESS": Reset consecutive_failures = 0, last_failed_task = ""
       - If output contains "Result: TASK_FAILURE": Extract task identifier from "## Iteration [N] - Task [M]: [Title]" line, check if same as last_failed_task, increment consecutive_failures if same (reset to 1 if different), stop if consecutive_failures >= 3
     - Increment current_iteration

5. Output final summary: iterations completed, final status, remaining tasks if incomplete

## Example Run

```
/ralph .thoughts/plans/my-feature.md

Loading ralph-wiggum skill...

=== Preparation Phase ===
Spawning ralph-preparer agent...

## Ralph Preparation Complete

**Configuration:**
- Plan file: .thoughts/plans/my-feature.md
- Autocommit: true
- Starting iteration: 1
- Unchecked tasks: 5

**Files created:**
- PLAN.md (copied from .thoughts/plans/my-feature.md)
- PROGRESS.md (initialized)

**Status:** READY

Initial commit created: "Ralph: Initialize PLAN.md and PROGRESS.md"

=== Iteration Planning ===
Found 5 unchecked tasks. Suggest running 8 new iterations (total: 8). Confirm?
> Use suggested (8 new iterations)

=== Iteration 1 ===
Spawning ralph-worker agent...

## Iteration 1 - Task 1: Add user model
- Result: TASK_SUCCESS
- What was implemented: Created User model with email, password hash, and timestamps
- Checks run: Check 1 (type-check) PASSED; Check 2 (lint) PASSED; Check 3 (unit tests) PASSED - all 8 tests passing
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
- Checks run: Check 1 (type-check) PASSED; Check 2 (validation tests) PASSED - all 12 tests passing; Check 3 (Simple QA) PASSED - validated live
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

## Example Run (Resuming)

```
/ralph .thoughts/plans/my-feature.md

Loading ralph-wiggum skill...

=== Preparation Phase ===
Spawning ralph-preparer agent...

## Ralph Preparation Complete

**Mode:** RESUMING
**Configuration:**
- Plan file: .thoughts/plans/my-feature.md
- Autocommit: true
- Starting iteration: 4
- Unchecked tasks: 2

**Status:** READY

=== Iteration Planning ===
Found 2 unchecked tasks. Suggest running 3 new iterations (total: 6). Confirm?
> Use suggested (3 new iterations)

=== Iteration 4 ===
Spawning ralph-worker agent...

[continues from where it left off...]
```

Input: $ARGUMENTS
