---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: [plan-file] [--max-iterations N] [--commit]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum to implement plan tasks iteratively.

## Process

1. Gather inputs if not provided:
   - Plan file path (search `.thoughts/plans/` for recent plans if needed)
   - Max iterations (default: 10)
   - Auto-commit flag (default: false)

2. **Branch safety**: If --commit flag is used and on default branch, suggest `ralph/<plan-name>` branch and STOP

3. Execute:
   ```bash
   $PLUGIN_DIR/.support/scripts/ralph_wiggum.py <plan-file> [--max-iterations N] [--commit]
   ```

Input: $ARGUMENTS
