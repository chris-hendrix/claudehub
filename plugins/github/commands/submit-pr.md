---
description: Commit, push, and create/update draft PR
allowed-tools: Bash, AskUserQuestion, Skill, Task
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context (current branch, PR status, uncommitted changes)
2. If on default branch, use `branch-namer` agent to suggest branch name and create it
3. If unstaged changes exist, ask user if they want to include them in commit
4. Push and create/update draft PR
5. Show PR URL
6. Ask if they want to generate title/description, use Skill tool to run `/describe-pr` if yes

Input: $ARGUMENTS
