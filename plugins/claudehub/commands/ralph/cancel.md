---
description: Cancel the active Ralph execution loop
allowed-tools: ["Bash", "Read", "AskUserQuestion"]
---

# Cancel

Stop the currently running Ralph execution loop and optionally discard uncommitted changes.

## Process

1. **Find running Ralph processes**:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --json
   ```

2. **Kill all Ralph processes and Claude Code sessions**:
   ```bash
   ALL_PIDS=$(python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --pids)

   if [ -n "$ALL_PIDS" ]; then
     echo "Terminating Ralph orchestrator and Claude Code sessions..."
     echo "$ALL_PIDS" | xargs kill
     sleep 0.5

     # Force kill any remaining processes
     REMAINING=$(python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --count)
     if [ "$REMAINING" -gt 0 ]; then
       echo "Force killing remaining processes..."
       echo "$ALL_PIDS" | xargs kill -9
     fi

     echo "All Ralph processes terminated"
   else
     echo "No running Ralph processes found"
   fi
   ```

3. **Check for uncommitted changes**:
   ```bash
   git status --porcelain
   ```

4. **Ask about discarding changes** (if there are uncommitted changes):

   Use AskUserQuestion:
   - Question: "Ralph has been cancelled. Would you like to discard all uncommitted changes?"
   - Header: "Discard changes?"
   - Options:
     - "Keep changes (Recommended)" - Keep all uncommitted work for review
     - "Discard all changes" - Run `git reset --hard && git clean -fd` to discard everything

   If user chooses "Discard all changes":
   ```bash
   git reset --hard
   git clean -fd
   echo "All uncommitted changes discarded"
   ```

5. **Show progress**:
   - Read last 20 lines of `.ralph/PROGRESS.md` to show where it stopped
   - Count remaining tasks with: `grep -c "^- \[ \]" .ralph/TASKS.md`

## Notes

- Uses find_ralph.py utility to locate all running Ralph processes and child sessions
- Kills both the orchestrator and any active Claude Code sessions
- Optionally discards uncommitted changes (useful if Ralph made bad changes)
- Progress is preserved in PROGRESS.md - you can resume with `/claudehub:ralph/run`
