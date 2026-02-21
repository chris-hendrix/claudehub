---
name: writing-documentation
description: This skill should be used when the user wants to "start a doc", "write documentation", "create notes", "research something", "document findings", "write up", "create a thought doc", mentions ".thoughts", "thoughts folder", or mentions needing to capture information, specs, or research in a markdown file. For implementation plans, see the `writing-plans` skill instead.
version: 1.0.0
allowed-tools: Write, Read, Bash, AskUserQuestion, Glob, Task, Grep, TodoWrite
---

# Writing Documentation

Create markdown documents in the `.thoughts/` folder.

**For implementation plans**: See the `writing-plans` skill.

## Naming Convention

Files follow this pattern:
```
yyyy-mm-dd-[ticket-or-issue-id-]short-description.md
```

Examples:
- `2025-01-15-api-rate-limiting-research.md`
- `2025-01-15-auth-refactor-plan.md`

## Organization

Documents can be organized into subdirectories. Common examples:

| Subdir | Content |
|--------|---------|
| `plans/` | Implementation plans, roadmaps |
| `research/` | Investigations, analysis |
| `specs/` | PRDs, ERDs, specifications |

These are suggestions - users may prefer custom subdirs or the root `.thoughts/` folder. Ask if unclear.

## Document Requirements

- Filename starts with today's date (`YYYY-MM-DD-`)
- Short description uses kebab-case
- Include YAML frontmatter with `date` and `topic` fields
- Let content structure emerge from user's needs rather than over-templating

## Getting Today's Date

Always get the current date dynamically - never rely on internal knowledge which may be stale:

```bash
date +%Y-%m-%d
```

Use the output for both the filename prefix and the frontmatter `date` field.

## Frontmatter

| Field | Description |
|-------|-------------|
| `date` | Creation date (YYYY-MM-DD) |
| `topic` | Human-readable title/subject |
