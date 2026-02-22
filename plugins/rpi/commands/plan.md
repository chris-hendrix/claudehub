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

- `rpi:researching-codebase` - gathering context
- `rpi:writing-plans` - planning methodology
- `rpi:writing-documentation` - file naming and frontmatter

## Process

1. Gather context from input

2. Research codebase for patterns, architecture, and existing implementations

3. Align with user until at least 90% confident you understand what they want:
   - 100% alignment on the plan → ~80% alignment in code
   - 90% alignment on the plan → ~60% alignment in code
   - 80% alignment on the plan → code that misses the mark
   - Draft success criteria and confirm with user
   - Ask clarifying questions to resolve ambiguity (use AskUserQuestion)
   - Propose high-level approach and key decisions, get confirmation
   - Report confidence after each round: "Current confidence: X% - [gaps]"
   - Keep asking until you could explain the plan back and the user would say "yes, exactly"
   - Do NOT proceed to writing the plan until alignment is reached

4. Write specification sections (Overview, Success Criteria, Current State, Architecture with code snippets)

5. Create detailed implementation checklist broken into phases → tasks → steps

6. Save to `.thoughts/plans/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`

Input: $ARGUMENTS
