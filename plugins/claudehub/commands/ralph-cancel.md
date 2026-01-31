---
description: Cancel the active Ralph execution loop
allowed-tools: ["Bash", "Read"]
---

# Cancel

Stop the currently running Ralph execution loop.

## Process

1. **Check for running Ralph process**:
   ```bash
   pgrep -f "skills/ralph-wiggum/scripts/ralph.py" || echo "No Ralph process found"
   ```

2. **If found, kill the process**:
   ```bash
   pkill -f "skills/ralph-wiggum/scripts/ralph.py"
   ```
   - More specific pattern includes full path to avoid killing wrong processes

3. **Verify termination**:
   ```bash
   sleep 1 && pgrep -f "skills/ralph-wiggum/scripts/ralph.py" && echo "Warning: Process still running" || echo "Ralph stopped"
   ```

4. **Report status**:
   - If process was found and killed: "Ralph execution stopped"
   - If no process found: "No active Ralph execution found"

5. **Show progress**:
   - Read last 20 lines of `.ralph/PROGRESS.md` to show where it stopped
   - Count remaining tasks in `.ralph/TASKS.md`

## Notes

- This only stops the orchestrator script
- Any currently running Claude Code session will complete its current task
- Progress is preserved - you can resume with `/ralph:run`
