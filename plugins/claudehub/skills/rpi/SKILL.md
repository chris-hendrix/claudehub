---
name: rpi
description: Consolidated research-plan-implement workflow. Use when the user wants to brainstorm an idea, research a codebase or the web, create an implementation plan, or implement from a plan. Keywords: brainstorm, research codebase, research web, plan, implement all, implement phase N.
allowed-tools: Read Write Bash Edit AskUserQuestion Glob Grep Task TodoWrite WebSearch WebFetch Agent
metadata:
  version: "1.0"
---

# rpi — Research, Plan, Implement

Unified entry point for the research-plan-implement workflow.

## Usage

```
/claudehub:rpi <keyword> [args]
```

| Keyword | Syntax | What it does |
|---------|--------|--------------|
| `brainstorm` | `brainstorm <topic>` | Explore approaches for an idea |
| `research codebase` | `research codebase <topic>` | Investigate the codebase |
| `research web` | `research web <topic>` | Search the web for information |
| `plan` | `plan <description or .thoughts doc path>` | Create an implementation plan |
| `implement all` | `implement all [plan path]` | Implement all phases from a plan |
| `implement phase N` | `implement phase N [plan path]` | Implement a specific phase from a plan |

## Doc Context

Any keyword can accept a path to an existing `.thoughts/` document as context:

- `plan .thoughts/brainstorms/2026-04-25-my-idea.md` — plan from an existing brainstorm
- `implement all .thoughts/plans/2026-04-25-my-plan.md` — implement from a specific plan

For `implement` with no explicit path, find the most recent `.thoughts/plans/*.md` file and confirm with the user before proceeding. If no plan files exist, tell the user and suggest running `/claudehub:rpi plan` first.

## Dispatch

Parse the first word of the input as the keyword. For `research`, parse the second word (`codebase` or `web`). For `implement`, parse `all` or `phase N`.

Follow the corresponding methodology:

- `brainstorm` → [brainstorming](references/brainstorming.md)
- `research codebase` → [researching-codebase](references/researching-codebase.md)
- `research web` → [researching-web](references/researching-web.md)
- `plan` → [planning](references/planning.md)
- `implement` → [implementing](references/implementing.md) (for doc conventions, see [writing-documentation](references/writing-documentation.md))

## Saving Output

After each workflow completes, offer to save the output. The `implement` workflow handles its own save prompt — for all others, ask: **"Save to .thoughts/?"**

If yes, write to the appropriate subdirectory with a date-prefixed filename:

| Workflow | Subdirectory | Filename pattern |
|----------|-------------|-----------------|
| brainstorm | `.thoughts/brainstorms/` | `YYYY-MM-DD-<topic>.md` |
| research | `.thoughts/research/` | `YYYY-MM-DD-<topic>.md` |
| plan | `.thoughts/plans/` | `YYYY-MM-DD-<topic>.md` |

Follow naming and frontmatter conventions in [writing-documentation](references/writing-documentation.md).

## Unknown or Missing Keyword

If invoked with no keyword or an unrecognized keyword, show the usage table above and ask the user what they'd like to do.
