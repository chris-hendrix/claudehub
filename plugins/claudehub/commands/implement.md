---
description: Implement from a plan or description
argument-hint: [plan file or description]
allowed-tools: Read, Write, Bash, Edit, AskUserQuestion, Glob, Task, Grep, TodoWrite, Skill
model: opus
---

## Skills

- `implementing` - execution methodology
- `researching-codebase` - understanding context when needed
- `writing-documentation` - summary file naming and frontmatter

## Process

1. Gather context from input (ask user if unclear)
   - Plan file: search `.thoughts/plans/` if name given
   - Description: clarify scope and requirements
2. Assess confidence (task, existing code, plan) - present ratings and concerns to user
3. Present phases to user for confirmation
4. Create TodoWrite with all phases (only after user confirms)
5. For each phase:
   - Mark phase as in_progress
   - Implement all changes in the phase
   - Run automated verification from success criteria
   - Present results and wait for user sign-off
   - Mark phase complete only after confirmation
6. After all phases: run full verification, write summary to `.thoughts/implementations/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`

Input: $ARGUMENTS
