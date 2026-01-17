---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: [plan-file] [--max-iterations N] [--commit]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum to implement plan tasks iteratively with tight feedback loops.

## Process

1. Gather inputs if not provided:
   - Plan file path (default: search `.thoughts/plans/` for recent plans, ask user to select)
   - Max iterations (default: 10)
   - Auto-commit flag (default: false)

2. Execute Ralph Wiggum script:
   ```bash
   $PLUGIN_DIR/.support/scripts/ralph_wiggum.py <plan-file> [--max-iterations N] [--commit]
   ```

3. Monitor output and report completion status

Ralph Wiggum methodology (from the `ralph-wiggum` skill):
- Finds first uncompleted task in plan
- Implements task following learnings from previous iterations
- Runs verification/tests
- Updates plan and progress files
- Repeats until done or max iterations reached

Input: $ARGUMENTS
