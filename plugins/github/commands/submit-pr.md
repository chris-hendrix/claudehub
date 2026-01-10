---
description: Commit, push, and create/update draft PR
allowed-tools: Bash, AskUserQuestion, Skill
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context (current branch, PR status, uncommitted changes)
2. If on default branch, help user create a feature branch
3. Commit any pending changes (confirm with user first)
4. Push and create/update draft PR
5. Show PR URL
6. Offer to update title/description or mark ready for review

Input: $ARGUMENTS
