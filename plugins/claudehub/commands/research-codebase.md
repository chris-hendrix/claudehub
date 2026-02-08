---
description: Research codebase and create documentation summarizing findings
argument-hint: [topic]
allowed-tools: AskUserQuestion, Skill, Read, Grep, Glob, Write, Bash, Task
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:researching-codebase` - Codebase investigation methodology (see references for research types and structure)
- `claudehub:writing-documentation` - Documentation creation standards (see references for naming and format)

## Process

1. Gather topic from input

2. Execute codebase research using appropriate research types (locating, analyzing, pattern-finding)

3. Synthesize findings with `file:line` references

4. Save to `.thoughts/research/YYYY-MM-DD-<topic-slug>.md` with proper frontmatter

Input: $ARGUMENTS
