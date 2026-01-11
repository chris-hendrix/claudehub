---
description: Commit, push, and create/update draft PR
allowed-tools: AskUserQuestion, Skill, Bash, Task
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context from input (if unclear)

2. If on default branch, use Skill tool to run `/create-branch`

3. If unstaged changes exist, confirm if they want to include them in commit

4. Push and create/update draft PR

5. Show PR URL

6. Ask if they want to generate title/description, use Skill tool to run `/describe-pr` if yes

7. Ask if they want to mark PR as ready for review (publish), use `gh pr ready` if yes

Input: $ARGUMENTS
