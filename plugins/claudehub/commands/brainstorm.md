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

1. Gather context from input (if unclear)

2. Research codebase using `researching-codebase` skill (spawn multiple agents)

3. Ask deeper questions informed by codebase context (prefer multiple choice)

4. Present 2-3 approaches with trade-offs, lead with recommendation

5. Once user picks an approach, create `.thoughts/brainstorms/YYYY-MM-DD-<topic>.md` with initial structure

6. Continue design in 200-300 word sections, updating document after each validated section

7. Ask if user wants to create an implementation plan using `/claudehub:create-plan`

Input: $ARGUMENTS
