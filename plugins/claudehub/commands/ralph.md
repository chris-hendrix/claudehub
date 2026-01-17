---
description: Autonomous agent to implement plan tasks iteratively
argument-hint: [plan-file] [--max-iterations N] [--commit]
allowed-tools: Bash, AskUserQuestion, Glob
---

Run Ralph - an autonomous implementation agent that executes plan tasks without user interaction.

## Process

1. Gather input if not provided:
   - Plan file path (default: search `.thoughts/plans/` for recent plans, ask user to select)
   - Max iterations (default: 10)
   - Auto-commit flag (default: false)

2. Execute Ralph script and monitor output:
   ```bash
   $PLUGIN_DIR/.support/scripts/ralph.py <plan-file> [--max-iterations N] [--commit]
   ```

Ralph runs in a loop:
- Find first uncompleted task in plan
- Implement all steps
- Run tests/verification
- Update plan file and progress file
- Repeat until done or max iterations

Input: $ARGUMENTS
