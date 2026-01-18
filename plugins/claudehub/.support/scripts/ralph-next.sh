#!/bin/bash
set -e

ITERATION_NUMBER=${1:-1}
TASK_TITLE=${2:-"Unknown task"}

# Keep only last 200 lines of PROGRESS.md for context (to avoid filling context window)
if [ -f "PROGRESS.md" ]; then
  tail -n 200 PROGRESS.md > /tmp/ralph_progress_tail.txt
else
  touch /tmp/ralph_progress_tail.txt
fi

# Get the script's directory and find template
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_FILE="$SCRIPT_DIR/../templates/ralph-iteration-output-template.md"
OUTPUT_TEMPLATE=$(cat "$TEMPLATE_FILE")

SYSTEM_PROMPT="You are Ralph, an autonomous coding agent.

Never ask questions or permission.

Implement this task: $TASK_TITLE

Run tests after implementation.

IMPORTANT: Do NOT update PLAN.md checkboxes or PROGRESS.md. The orchestrator will handle those based on your result.

Note: You're seeing the last 200 lines of PROGRESS.md for context about previous iterations.

Output your result in this format:
$OUTPUT_TEMPLATE

Execute now."

# Run claude CLI and capture output
result=$(claude --dangerously-skip-permissions \
  --output-format text \
  --append-system-prompt "$SYSTEM_PROMPT" \
  -p "@PLAN.md @/tmp/ralph_progress_tail.txt" \
  "Iteration $ITERATION_NUMBER. Implement: $TASK_TITLE" 2>&1)

exit_code=$?

# Output result (orchestrator/agent will parse this)
echo "$result"

# Always exit 0 - errors handled by orchestrator
exit 0
