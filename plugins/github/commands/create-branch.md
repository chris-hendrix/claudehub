---
description: Create a new git branch with AI-suggested name
allowed-tools: Bash, AskUserQuestion, Skill
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions (see references/branches.md)

## Process

1. Gather context

2. Suggest branch name following format: `<type>/<issue-number>-<description>`

3. Determine base branch (if branching from main, sync with origin first)

4. Handle any uncommitted changes appropriately

5. Create and checkout the new branch

Input: $ARGUMENTS
