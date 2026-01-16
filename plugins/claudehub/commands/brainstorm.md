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
- `researching-web` - web research for new libraries/frameworks
- `writing-documentation` - file naming and frontmatter

## Process

1. Gather context from input

2. Define objective and success criteria, get user confirmation before proceeding

3. Research based on task type:
   - **Modifying existing codebase**: Research codebase for current patterns and architecture
   - **New features with external dependencies**: Research web for library docs, APIs, best practices
   - **Both**: Research codebase first, then web for new integrations

4. Ask deeper questions informed by findings

5. Present 2-3 approaches with trade-offs and recommendation

6. Create `.thoughts/brainstorms/YYYY-MM-DD-<topic>.md` with validated design

7. Offer to create implementation plan

Input: $ARGUMENTS
