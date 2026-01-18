#!/bin/bash
set -e

WORK_DIR=${1:-.}
MAX=${2:-10}
COMMIT_MODE=${3:-}

# Change to working directory
cd "$WORK_DIR"

# Create PROGRESS.md if it doesn't exist
touch PROGRESS.md

SYSTEM_PROMPT="You are Ralph, an autonomous coding agent.

Never ask questions or permission.

Find the first line in PLAN.md matching '- [ ] **Task', implement it immediately, run tests, update PLAN.md (mark [x]), append to PROGRESS.md.

Note: You're seeing only the last 1000 lines of PROGRESS.md for context, but append new entries to the full PROGRESS.md file.

Append to PROGRESS.md in this format:
## Iteration [N] - Task [M]: [Task Name] - ✅/❌
- What was implemented: [brief description of code written, files created/modified, functions added, interfaces defined, etc.]
- What was tested: [tests run, commands executed, results]
- Context usage: [run /context to get total context usage]
- Learnings for future iterations:
  - Patterns discovered
  - Gotchas encountered
  - Useful context
---

After updating files, check PLAN.md:
- If task completed successfully (tests passed), output <promise>TASK_COMPLETE</promise>
- If ALL tasks are now [x] with NO [ ] remaining, output <promise>COMPLETE</promise>
- Otherwise just stop

Execute now."

echo "Starting Ralph in $(pwd)"
echo "Max iterations: $MAX"
if [ "$COMMIT_MODE" = "commit" ]; then
  echo "Commit mode: ENABLED (will commit after each successful iteration)"
else
  echo "Commit mode: DISABLED"
fi
echo ""

for ((i=1; i<=$MAX; i++)); do
  echo "═══════════════════════════════════════════════════════════"
  echo "   Iteration $i of $MAX"
  echo "═══════════════════════════════════════════════════════════"

  # Keep only last 1000 lines of PROGRESS.md for context (to avoid filling context window)
  tail -n 1000 PROGRESS.md > /tmp/ralph_progress_tail.txt

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

  # Check if task was completed successfully
  if echo "$result" | grep -q "<promise>TASK_COMPLETE</promise>"; then
    # Commit changes if commit mode is enabled
    if [ "$COMMIT_MODE" = "commit" ]; then
      # Extract task info from PROGRESS.md
      task_info=$(tail -n 20 PROGRESS.md | grep -m 1 "^## Iteration" || echo "Iteration $i")

      # Stage all changes
      git add -A

      # Create commit with task info
      git commit -m "Ralph iteration $i: $task_info

Co-Authored-By: Ralph Wiggum <ralph@claudehub>" || echo "⚠️  No changes to commit"

      echo "✅ Changes committed"
    fi
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