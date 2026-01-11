---
description: Delete local branches that were merged or closed in origin
allowed-tools: Bash, AskUserQuestion, Task
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Use AskUserQuestion if input is unclear

2. Use `dead-branch-finder` agent to identify branches that can be deleted

3. Display list of branches with their status (merged/closed)

4. Use AskUserQuestion to confirm which branches to delete

5. Delete confirmed branches

Input: $ARGUMENTS
