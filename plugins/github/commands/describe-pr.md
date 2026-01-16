---
description: Generate and update PR title and description from branch diff
allowed-tools: AskUserQuestion, Skill, Bash, Task
agents:
  - pr-describer
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather context from input (if unclear)
   - Determine PR number (from current branch or user input)

2. Use `pr-describer` agent to return a PR title and description

3. Display the generated title and description to user

4. Confirm with user

5. Apply changes to PR using `gh pr edit`

6. Show GitHub URL

Input: $ARGUMENTS
