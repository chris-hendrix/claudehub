---
description: Create detailed implementation plans through interactive research
argument-hint: [ticket or issue or description]
allowed-tools: Read, Bash, AskUserQuestion, Glob, Grep, Task, Skill, TodoWrite, Write
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:researching-codebase` - gathering context
- `claudehub:writing-plans` - planning methodology
- `claudehub:writing-documentation` - file naming and frontmatter

## Process

1. Gather context from input

2. Research codebase for patterns, architecture, and existing implementations

3. Ask clarifying questions to resolve ambiguity

4. Propose high-level phase breakdown and key decisions, get confirmation

5. Write specification sections (Overview, Current State, Architecture with code snippets)

6. Create detailed implementation checklist broken into phases → tasks → steps

7. Save to `.thoughts/plans/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`

Input: $ARGUMENTS
