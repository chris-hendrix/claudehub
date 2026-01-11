---
description: Create a new git branch with AI-suggested name
allowed-tools: Bash, AskUserQuestion, Task
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Use AskUserQuestion if input is unclear

2. Use `branch-namer` agent to suggest branch name

3. Gather context (current branch, staged/unstaged changes)

4. Use AskUserQuestion to confirm branch name and (if changes exist) ask if they want to stash/pop changes

5. If confirmed, stash changes (if any)

6. Create and checkout the new branch

7. Pop the stash if changes were stashed

Input: $ARGUMENTS
