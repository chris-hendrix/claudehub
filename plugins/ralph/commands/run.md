---
description: Run Ralph execution loop, using /ralph:plan if docs are missing
argument-hint: "[description] [--max-iterations N] [--commit-mode MODE] [--skip-permissions]"
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Glob", "Task", "Skill", "AskUserQuestion"]
references-skills: ralph:ralph-wiggum
---

# Run

Start the Ralph execution loop. If planning docs don't exist, runs `/ralph:plan` first to create them.

## Process

1. **Load the `ralph:ralph-wiggum` skill** using the Skill tool

2. **Check if Ralph is already running**:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/find_ralph.py" --count
   ```
   - If count > 0, show running processes and ask user:
     - "Ralph is already running (PID: X, started: Y). Use `/ralph:cancel` to stop it first, or continue anyway?"
   - If user says cancel/stop, stop here

3. **Check if planning docs exist**:
   ```bash
   test -f .ralph/TASKS.md && test -f .ralph/ARCHITECTURE.md && test -f .ralph/VERIFICATION.md
   ```

4. **If planning docs are missing**, run `/ralph:plan` with the description from `$ARGUMENTS`
   - If no description provided and no planning docs, tell user to provide one and stop

5. **Ensure proper branch isolation**:

   Detection:
   1. Get current branch: `git rev-parse --abbrev-ref HEAD`
   2. Check if in a worktree: compare `git rev-parse --show-toplevel` with the first worktree path from `git worktree list --porcelain`

   Decision:
   - If current branch starts with `ralph/` → already on a Ralph branch, proceed
   - If in a worktree (toplevel differs from main worktree) → proceed
   - Otherwise → create a Ralph branch:
     - Read description from `.ralph/CONFIG.md` if it exists
     - Fallback: parse from `$ARGUMENTS`, or ask user
     - Create branch:
       ```bash
       DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
       git checkout $DEFAULT_BRANCH && git pull
       git checkout -b ralph/$(date +%Y%m%d-%H%M)-<description>
       ```
     - Untracked `.ralph/` files carry over naturally

6. **Validate script exists**:
   ```bash
   test -f "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/ralph.py"
   ```
   - If script not found, tell user: "Ralph orchestrator script not found. Please reinstall the claudehub plugin."

7. **Ask about permissions if not specified**:
   - Parse `$ARGUMENTS` to check if `--skip-permissions` is present
   - If NOT present, use `AskUserQuestion` to ask:
     - Question: "Would you like to skip permission prompts during Ralph execution?"
     - Header: "Permissions"
     - Options:
       - "Yes (Recommended)" - Skip all permission prompts for faster execution
       - "No" - Require permission prompts for each operation
   - Store the user's choice to determine whether to add `--skip-permissions` flag

8. **Run the Python orchestrator in background**:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/ralph-wiggum/scripts/ralph.py" --max-iterations <N> --commit-mode <MODE> [--skip-permissions]
   ```
   Use `run_in_background: true`.
   - Add `--skip-permissions` flag if:
     - It was present in `$ARGUMENTS`, OR
     - User selected "Yes (Recommended)" in the permissions question

9. **Confirm startup**:

   Generate compare URL (see "Tracking Progress Remotely" in skill).

   > "Ralph started (task ID: `<id>`). Use `/ralph:cancel` to stop.
   >
   > View commits: `<compare-url>`"

## Arguments

- First positional: Description of what to build (required if no planning docs)
- `--max-iterations N`: Stop after N iterations (default: 50)
- `--commit-mode MODE`: `no-commit`, `commit`, or `commit-push` (default: `commit-push`)
- `--skip-permissions`: Bypass all permission prompts (uses bypassPermissions mode)

## Examples

```bash
# With description (creates planning docs automatically)
/ralph:run "add user authentication with JWT"

# If planning docs already exist
/ralph:run

# With options
/ralph:run "refactor payment flow" --max-iterations 20

# Skip permission prompts (for trusted environments)
/ralph:run --skip-permissions
```

Input: $ARGUMENTS
