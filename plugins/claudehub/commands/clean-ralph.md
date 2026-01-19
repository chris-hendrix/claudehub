---
description: Archive Ralph PLAN.md and PROGRESS.md to .thoughts/ralph/
argument-hint: [short-description]
allowed-tools: Read, Write, Bash
---

## Important

- Use Write tool for creating files, not bash commands

## Process

1. Verify `PLAN.md` exists

2. Determine short description from `$ARGUMENTS`, or generate from first 10 lines of PLAN.md

3. Move `PLAN.md` and `PROGRESS.md` (if exists) to `.thoughts/ralph/YYYY-MM-DD-{description}.{PLAN|PROGRESS}.md` using `mv` command

4. Update frontmatter in archived PLAN.md to add current commit and branch

Input: $ARGUMENTS
