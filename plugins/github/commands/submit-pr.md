---
description: Commit, push, and create/update draft PR
allowed-tools: Bash, AskUserQuestion, Skill, Task
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Use AskUserQuestion if input is unclear, then gather context (current branch, PR status, uncommitted changes)
2. If on default branch, use `branch-namer` agent to suggest branch name and create it
3. If unstaged changes exist, use AskUserQuestion to confirm if they want to include them in commit
4. Push and create/update draft PR
5. Show PR URL
6. Use AskUserQuestion to ask if they want to generate title/description, use Skill tool to run `/describe-pr` if yes

Input: $ARGUMENTS
