---
description: Generate and update PR title and description from branch diff
allowed-tools: AskUserQuestion, Skill, Bash
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions (see references/pull-requests.md)

## Process

1. Gather context (ask user if unclear)

2. Generate PR title and description

3. Display the generated content to user

4. Confirm with user

5. Update PR and show URL

Input: $ARGUMENTS
