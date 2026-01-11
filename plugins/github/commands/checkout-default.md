---
description: Switch to default branch and sync with remote
allowed-tools: Bash, Skill, AskUserQuestion
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Use AskUserQuestion if input is unclear

2. Determine the default branch (main or master)

3. Gather context (current branch, staged/unstaged changes)

4. Use AskUserQuestion to confirm and (if changes exist) ask if they want to stash/pop changes

5. If confirmed, stash changes (if any)

6. Switch to the default branch

7. Fetch from remote

8. Pull latest changes

9. Pop the stash if changes were stashed

10. Use AskUserQuestion to ask if they want to clean dead branches, use Skill tool to run `/clean-branches` if yes

Input: $ARGUMENTS
