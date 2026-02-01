---
description: Cancel the active Ralph execution loop
allowed-tools: ["Bash", "Read"]
---

# Cancel

Stop the currently running Ralph execution loop.

## Process

1. **Find running Ralph processes**:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --json
   ```

2. **Kill all Ralph processes**:
   ```bash
   RALPH_PIDS=$(python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --json | jq -r '.[].pid')

   if [ -n "$RALPH_PIDS" ]; then
     echo "Found Ralph processes: $RALPH_PIDS"
     echo "$RALPH_PIDS" | xargs kill
     sleep 0.5

     # Force kill any remaining processes
     REMAINING=$(python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --count)
     if [ "$REMAINING" -gt 0 ]; then
       echo "Force killing remaining processes..."
       echo "$RALPH_PIDS" | xargs kill -9
     fi

     echo "All Ralph processes terminated"
   else
     echo "No running Ralph processes found"
   fi
   ```

3. **Show progress**:
   - Read last 20 lines of `.ralph/PROGRESS.md` to show where it stopped
   - Count remaining tasks with: `grep -c "^- \[ \]" .ralph/TASKS.md`

## Notes

- Uses find_ralph.py utility to locate all running Ralph processes
- This is a kill switch that stops everything immediately
- Both the orchestrator and any active Claude Code sessions are terminated
- It's fine if execution stops halfway through a task
- Progress is preserved - you can resume with `/claudehub:ralph-run`
