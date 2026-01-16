---
description: Delete local branches that were merged or closed in origin
allowed-tools: Bash, AskUserQuestion, Skill
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Fetch and prune remote tracking info

2. Identify local branches that have been deleted on the remote

3. Display the list of branches that can be deleted

4. Confirm with the user if they are okay deleting all branches

5. Delete all the branches if confirmed

Input: $ARGUMENTS
