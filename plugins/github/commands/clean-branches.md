---
description: Delete local branches that were merged or closed in origin
allowed-tools: AskUserQuestion, Skill, Bash, Task
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context from input (if unclear)

2. Use `dead-branch-finder` agent to identify branches that can be deleted

3. Display list of branches with their status (merged/closed)

4. Confirm which branches to delete

5. Delete confirmed branches

Input: $ARGUMENTS
