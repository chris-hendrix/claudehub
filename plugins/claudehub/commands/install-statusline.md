---
description: Install the claudehub statusline to your Claude Code settings
allowed-tools: Read, Edit, Write, Bash
---

## Overview

This command installs the claudehub statusline script that displays:
- Repository name
- Current git branch
- Model name
- Context usage with color-coded progress bar (green < 40%, yellow 40-60%, orange 60-80%, red ≥ 80%)

**Example output:**
```
claude-hub │ main │ [Sonnet] │ ▓▓▓▓▓░░░░░ 50%
```

## Process

1. **Check if statusLine is already configured**
   - Read `~/.claude/settings.json`
   - If statusLine exists, inform the user and ask if they want to replace it

2. **Find the statusline script using bash**
   - Run this exact command to locate the script:
     ```bash
     find ~/.claude/plugins/cache -path "*/claudehub/*/.support/scripts/statusline.py" 2>/dev/null | head -1
     ```
   - If no result, the claudehub plugin may not be installed — inform the user
   - **Validate** the found path exists before using it: `test -f "$SCRIPT_PATH"`

3. **Update settings.json**
   - Add or update the statusLine configuration using the exact path found in step 2
   - The path MUST end with `/.support/scripts/statusline.py` — do NOT append extra directory segments
   - Example of a correct path: `~/.claude/plugins/cache/claudehub/claudehub/1.0.0/.support/scripts/statusline.py`

4. **Confirm installation**
   - Inform the user that the statusline has been installed
   - Explain that it will appear on their next interaction with Claude Code

## Settings Configuration

The statusLine configuration should use an absolute path (not `${CLAUDE_PLUGIN_ROOT}` as that variable is not supported in statusLine commands):

```json
{
  "statusLine": {
    "type": "command",
    "command": "/home/user/.claude/plugins/cache/claudehub/claudehub/1.0.0/.support/scripts/statusline.py"
  }
}
```

## Important Notes

- The statusline script requires Python 3 (which is already available)
- The statusline updates after each assistant message, permission mode change, or vim mode toggle
- If the user has an existing statusline, ask before replacing it
