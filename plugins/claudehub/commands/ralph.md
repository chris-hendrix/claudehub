---
description: Run Ralph Wiggum autonomous implementation iterations
argument-hint: <plan-file> [max-iterations] [--commit]
references-skills: ralph-wiggum
---

Execute Ralph Wiggum to implement plan tasks iteratively.

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:ralph-wiggum` - Autonomous implementation methodology

## Process

1. Load the `claudehub:ralph-wiggum` skill using the Skill tool first (required)

2. Check if --commit flag is present in arguments

3. If --commit flag is present:
   - Check current branch with `git branch --show-current`
   - Get default branch with `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'`
   - If on default branch:
     - Ask user if they want to create a new branch
     - Suggest format: `ralph/short-description`
     - If yes, create and checkout the branch

4. Handle plan file setup:
   - If no plan file provided:
     - Check if PLAN.md exists
     - If exists: Ask "Continue with existing PLAN.md or provide new plan file?"
     - If doesn't exist: Ask user to provide plan file
   - If plan file provided:
     - Verify it contains task checkboxes (`- [ ] **Task`)
     - Copy to PLAN.md (overwrites if exists)

5. Ask for max iterations (suggestion: 10)

6. Run the Ralph Wiggum script:
   ```bash
   bash /path/to/plugins/claudehub/skills/ralph-wiggum/scripts/ralph-wiggum.sh $(pwd) <max-iterations> <commit-flag>
   ```

   Where <commit-flag> is "commit" if --commit was passed, empty otherwise

   The script will:
   - Work in the project root directory
   - Use PLAN.md and PROGRESS.md
   - Implement tasks one at a time
   - Optionally commit after each iteration (with --commit flag)
   - Stop when all tasks complete or max iterations reached

Input: $ARGUMENTS
