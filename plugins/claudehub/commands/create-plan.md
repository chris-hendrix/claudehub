---
description: Create detailed implementation plans through interactive research
argument-hint: [ticket or issue or description]
allowed-tools: Read, Bash, AskUserQuestion, Glob, Grep, Task, Skill, TodoWrite, Write
model: opus
---

## Skills

- `researching-codebase` - gathering context
- `writing-plans` - planning methodology
- `writing-documentation` - file naming and frontmatter

## Process

1. Gather context from input (ask user if unclear)
2. Research codebase using `researching-codebase` skill (spawn multiple agents)
3. **Ask clarifying questions** - DO NOT SKIP, wait for answers
4. Present 2-3 architecture options with trade-offs, get user preference
5. Write plan iteratively with user feedback
6. Save to `.thoughts/plans/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md` (see `writing-documentation` skill)

Input: $ARGUMENTS
