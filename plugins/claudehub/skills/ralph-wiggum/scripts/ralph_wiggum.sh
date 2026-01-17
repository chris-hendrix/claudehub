#!/bin/bash
set -e

WORK_DIR=${1:-.}
MAX=${2:-10}

# Change to working directory
cd "$WORK_DIR"

# Create progress.txt if it doesn't exist
touch progress.txt

SYSTEM_PROMPT="You are Ralph, an autonomous coding agent.

Never ask questions or permission.

Find the first line in PLAN.md matching '- [ ] **Task', implement it immediately, run tests, update PLAN.md (mark [x]), append to progress.txt.

Note: You're seeing only the last 1000 lines of progress.txt for context, but append new entries to the full progress.txt file.

Append to progress.txt in this format:
## Iteration [N] - [Task Name] - ✅/❌
- What was implemented: [brief description of code written, files created/modified, functions added, interfaces defined, etc.]
- What was tested: [tests run, commands executed, results]
- Token usage: [input/output tokens from /usage command]
- Learnings for future iterations:
  - Patterns discovered
  - Gotchas encountered
  - Useful context
---

After updating files, check PLAN.md: if there are still unchecked tasks (any [ ] remaining), just stop. If ALL tasks are now [x] with NO [ ] remaining, output <promise>COMPLETE</promise>.

Execute now."

echo "Starting Ralph in $(pwd)"
echo "Max iterations: $MAX"
echo ""

for ((i=1; i<=$MAX; i++)); do
  echo "═══════════════════════════════════════════════════════════"
  echo "   Iteration $i of $MAX"
  echo "═══════════════════════════════════════════════════════════"

  # Keep only last 1000 lines of progress.txt for context (to avoid filling context window)
  tail -n 1000 progress.txt > /tmp/ralph_progress_tail.txt

  result=$(claude --dangerously-skip-permissions --output-format text --append-system-prompt "$SYSTEM_PROMPT" -p "@PLAN.md @/tmp/ralph_progress_tail.txt" "Iteration $i. Implement first unchecked task." 2>&1)
  exit_code=$?

  echo "$result"

  if [ $exit_code -ne 0 ]; then
    echo ""
    echo "⚠️  Error: Claude command failed (exit code $exit_code)"
    echo "Retrying in 5 seconds..."
    sleep 5
    continue
  fi

  if echo "$result" | grep -q "<promise>COMPLETE</promise>"; then
    echo ""
    echo "🎉 All tasks complete!"
    exit 0
  fi

  echo ""
  sleep 2
done

echo "⚠️  Reached max iterations ($MAX). Some tasks may remain."
exit 1