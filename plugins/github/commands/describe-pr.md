---
description: Generate and update PR title and description from branch diff
allowed-tools: Bash, AskUserQuestion, Task, Skill
agents:
  - pr-describer
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context from input (use AskUserQuestion if unclear)
   - Determine PR number (from current branch or user input)

2. Use `pr-describer` agent to return a PR title and description

3. Use AskUserQuestion to confirm with user

4. Apply changes to PR using `gh pr edit`

5. Show GitHub URL

Input: $ARGUMENTS
