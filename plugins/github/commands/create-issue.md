---
description: Create a GitHub issue with AI-generated content
allowed-tools: AskUserQuestion, Skill, Bash, Read, Glob
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions (see references/issues.md)

## Process

1. Gather input from user

2. Generate issue title and description following appropriate template format

3. Confirm and optionally add labels/assignees

4. Create issue and show URL

Input: $ARGUMENTS
