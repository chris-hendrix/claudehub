---
description: Implement from a plan or description
argument-hint: [plan file or description]
allowed-tools: Read, Write, Bash, Edit, AskUserQuestion, Glob, Task, Grep, TodoWrite, Skill
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `implementing` - execution methodology
- `researching-codebase` - understanding context when needed
- `writing-documentation` - summary file naming and frontmatter

## Process

1. Gather context (plan file from `.thoughts/plans/` or clarify description)

2. Assess confidence and present phases for confirmation

3. Create TodoWrite with confirmed phases

4. Execute each phase with verification and user sign-off

5. Complete with full verification and summary to `.thoughts/implementations/`

Input: $ARGUMENTS
