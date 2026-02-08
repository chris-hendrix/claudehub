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

2. **Find the installed plugin path**
   - Use bash to find the latest claudehub plugin version: `ls -d ~/.claude/plugins/cache/claudehub/claudehub/*/ | tail -1`
   - Construct the absolute path to the statusline script

3. **Update settings.json**
   - Add or update the statusLine configuration to point to the claudehub statusline script
   - Use the absolute path found in step 2

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

Note: The exact path will vary based on the installed plugin version. Use bash to detect it dynamically.

## Important Notes

- The statusline script requires Python 3 (which is already available)
- The statusline updates after each assistant message, permission mode change, or vim mode toggle
- If the user has an existing statusline, ask before replacing it
- The script is located in the plugin's .support folder and will work as long as the claudehub plugin is installed
