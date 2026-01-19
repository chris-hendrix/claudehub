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

2. Draft success criteria - if unclear from input, create them and confirm with user before proceeding

3. Research codebase for patterns, architecture, and existing implementations

4. Ask clarifying questions to resolve ambiguity

5. Propose high-level phase breakdown and key decisions, get confirmation

6. Write specification sections (Overview, Success Criteria, Current State, Architecture with code snippets)

7. Create detailed implementation checklist broken into phases → tasks → steps

8. Save to `.thoughts/plans/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`

Input: $ARGUMENTS
