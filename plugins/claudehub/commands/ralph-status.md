---
description: Show current Ralph execution status and progress
allowed-tools: ["Bash", "Read", "Grep"]
---

# Status

Report the current status of a Ralph execution.

## Process

1. **Check if Ralph is running**:
   ```bash
   pgrep -f "ralph.py" > /dev/null && echo "RUNNING" || echo "NOT_RUNNING"
   ```

2. **Read TASKS.md** and parse:
   - Count total tasks: `- [x]` and `- [ ]` lines
   - Count completed: `- [x]` lines
   - Find current task: first `- [ ]` line
   - Group by phase (## headers)

3. **Read PROGRESS.md** and extract:
   - Latest iteration number
   - Total cost (sum all `$X.XX` amounts)
   - First iteration timestamp (for runtime calculation)

4. **Check latest log file** (optional, if running):
   ```bash
   ls -t .ralph/logs/*/*.jsonl 2>/dev/null | head -1
   ```
   Read last few lines for current activity.

5. **Get compare URL** (see "Tracking Progress Remotely" in skill)

6. **Display status report**:

   ```
   Ralph Status: [RUNNING | STOPPED | COMPLETE]

   Current: Iteration N - Task X.Y: [task name]

   Progress: X/Y tasks complete
   Cost: $X.XX
   Runtime: Xm
   View commits: <compare-url>

   Phases:
   ┌─────────────────────┬─────────┬───────────┐
   │ Phase               │ Tasks   │ Status    │
   ├─────────────────────┼─────────┼───────────┤
   │ Phase 1: [Name]     │ 1.1-1.3 │ ✅ Done   │
   │ Phase 2: [Name]     │ 2.1-2.2 │ ✅ Done   │
   │ Phase 3: [Name]     │ 3.1     │ 🔄 Active │
   │ Phase 4: [Name]     │ 4.1-4.2 │ ⏳ Pending│
   └─────────────────────┴─────────┴───────────┘
   ```

## Status Icons

- ✅ Complete - all tasks in phase done
- 🔄 In Progress - current task is in this phase
- ⏳ Pending - no tasks started yet
- ❌ Failed - task failed 3 times (check PROGRESS.md)

## Examples

```bash
# Check status while Ralph is running
/ralph:status

# Check status after Ralph stopped
/ralph:status
```
