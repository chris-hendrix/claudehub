---
description: Brainstorm an idea into a validated design through dialogue
argument-hint: [idea or topic]
allowed-tools: Read, Bash, AskUserQuestion, Glob, Grep, Task, Skill, TodoWrite, Write
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `brainstorming` - dialogue methodology
- `researching-codebase` - gathering project context
- `writing-documentation` - file naming and frontmatter

## Process

1. Gather context from input

2. Research codebase for relevant patterns and context

3. Ask deeper questions informed by findings

4. Present 2-3 approaches with trade-offs and recommendation

5. Create `.thoughts/brainstorms/YYYY-MM-DD-<topic>.md` with validated design

6. Offer to create implementation plan

Input: $ARGUMENTS
