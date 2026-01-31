---
description: Run Ralph execution loop, using /claudehub:ralph-plan if docs are missing
argument-hint: "[description] [--max-iterations N] [--commit-mode MODE]"
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Glob", "Task", "Skill"]
references-skills: claudehub:ralph-wiggum
---

# Run

Start the Ralph execution loop. If planning docs don't exist, runs `/claudehub:ralph-plan` first to create them.

## Process

1. **Load the `ralph-wiggum` skill** using the Skill tool

2. **Check if planning docs exist**:
   ```bash
   test -f .ralph/TASKS.md && test -f .ralph/ARCHITECTURE.md && test -f .ralph/VERIFICATION.md
   ```

3. **If planning docs are missing**, run `/claudehub:ralph-plan` with the description from `$ARGUMENTS`
   - If no description provided and no planning docs, tell user to provide one and stop

4. **Validate script exists**:
   ```bash
   test -f "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/ralph.py"
   ```
   - If script not found, tell user: "Ralph orchestrator script not found. Please reinstall the claudehub plugin."

5. **Run the Python orchestrator in background**:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/ralph.py" --max-iterations <N> --commit-mode <MODE>
   ```
   Use `run_in_background: true`.

6. **Confirm startup**:

   Generate compare URL (see "Tracking Progress Remotely" in skill).

   > "Ralph started (task ID: `<id>`). Use `/claudehub:ralph-cancel` to stop.
   >
   > View commits: `<compare-url>`"

## Arguments

- First positional: Description of what to build (required if no planning docs)
- `--max-iterations N`: Stop after N iterations (default: 50)
- `--commit-mode MODE`: `no-commit`, `commit`, or `commit-push` (default: `commit-push`)

## Examples

```bash
# With description (creates planning docs automatically)
/claudehub:ralph-run "add user authentication with JWT"

# If planning docs already exist
/claudehub:ralph-run

# With options
/claudehub:ralph-run "refactor payment flow" --max-iterations 20
```

Input: $ARGUMENTS
