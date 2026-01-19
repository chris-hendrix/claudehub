---
description: Archive Ralph PLAN.md and PROGRESS.md to .thoughts/ralph/
argument-hint: [short-description]
allowed-tools: Read, Write, Bash, Skill, Glob
---

## Important

- Always load referenced skills using the Skill tool

## Skills

- `claudehub:writing-documentation` - Document naming and frontmatter conventions

## Process

1. Verify `PLAN.md` exists in working directory

2. Determine short description from `$ARGUMENTS`, `parent-plan:` frontmatter field, or by generating from PLAN.md content

3. Archive to `.thoughts/ralph/YYYY-MM-DD-short-description.PLAN.md` with frontmatter (date, topic, commit)

4. Archive `PROGRESS.md` if it exists to `.thoughts/ralph/YYYY-MM-DD-short-description.PROGRESS.md` with frontmatter

5. Delete original `PLAN.md` and `PROGRESS.md` files

Input: $ARGUMENTS
