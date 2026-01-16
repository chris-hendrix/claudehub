---
description: Commit, push, and create/update draft PR
allowed-tools: AskUserQuestion, Skill, Bash
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions (see references/pull-requests.md)

## Process

1. Create branch if on default branch

2. Commit any changes

3. Push and create/update draft PR

4. Show PR URL

5. Offer to update title/description

6. Offer to mark as ready for review if in draft state

Input: $ARGUMENTS
