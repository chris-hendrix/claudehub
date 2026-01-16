# Skills

Skills are domain knowledge Claude applies. They teach Claude *how to think* about a problem - methodology, principles, and decision frameworks that adapt to different situations.

## Location

```
.claude/skills/
├── my-skill/
│   ├── SKILL.md             # Main instructions (required)
│   └── references/          # Supporting docs (optional)
│       └── patterns.md
└── another-skill/
    └── SKILL.md
```

## Naming

**Pattern:** `{gerund}` (e.g., `planning`, `describing-prs`)

For tool-specific skills, the tool name alone is acceptable: `graphite`, `linear`

**Litmus test:** "Help me with {name}" sounds natural

| Good | Bad |
|------|-----|
| `planning` | `plan` (verb, use for command) |
| `writing-documentation` | `documentation` (noun, not activity) |
| `handling-errors` | `error-handler` (role, use for agent) |
| `graphite` | `graphite-commands` (redundant suffix) |
| `linear` | `lin` (abbreviation) |

## Frontmatter

```yaml
---
name: skill-name (required)
description: "This skill should be used when..." (required)
version: 1.0.0 (optional)
allowed-tools: Bash, Read, Glob (optional)
model: sonnet | opus | haiku (optional)
---
```

Note: `allowed-tools` accepts any valid Claude Code tool - the examples above aren't exhaustive. Other tools include `Edit`, `Write`, `Grep`, `WebFetch`, `WebSearch`, `AskUserQuestion`, `Skill`, `Task`, `mcp__*`, etc.

## Context Sections

Skills should include "Context for..." sections that explain where to gather information for generating content. This helps Claude Code understand data sources before taking action.

**Pattern:** Start reference files with a context section explaining:
- What user input to expect
- What commands to run to gather information
- What templates or files to check first
- When to clarify with the user

**Example - Branch naming context:**
```markdown
## Context for Branch Names

Branch names can be derived from multiple sources:

**Issue/ticket numbers:**
- Check if the user provided an issue number or references a GitHub issue
- Use `gh issue view <number>` to fetch issue details
- Extract the issue type and description

**Uncommitted or staged changes:**
- Run `git status` to see modified files
- Run `git diff` for staged changes or `git diff HEAD` for all changes
- Analyze the changes to infer the type (feature, fix, refactor, etc.) and description

**User input:**
- Direct description from the user about what they're working on
- Clarify with the user if the context is unclear
```

**Example - PR description context with template checking:**
```markdown
## Context for Describing PRs

When generating PR descriptions, **always** check for and follow the repo's PR template first:

**PR Template (check first):**
- Read template from `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` or `.github/pull_request_template.md`
- If template exists, follow its exact structure and sections
- If template doesn't exist, use standard format below

**Context sources for PR content:**
- Branch diff: Use `git diff <base-branch>...HEAD` to see all changes since branch divergence
- Commit history: Use `git log <base-branch>..HEAD` to see commit messages
- Linked issues: Check branch name for issue numbers (e.g., `feature/123-add-auth`)
- Existing PR media: Fetch current PR body with `gh pr view --json body -q .body` to preserve images/videos
```

**Key Principles:**
- Put context sections at the top of reference files, before detailed guidelines
- Be specific about commands to run and files to check
- Always mention template checking when applicable (PR templates, issue templates, etc.)
- Order sources by priority (user input first, then automated gathering)

## Example Skill

```markdown
---
name: graphite
description: "This skill should be used when working with Graphite CLI for stacked PRs, branch management, or code review workflows."
---

# Graphite

Guidelines for using Graphite CLI for stacked pull requests.

## Philosophy

Graphite enables stacked PRs - small, focused changes that build on each other. Each PR should be reviewable in isolation.

## Branch Naming

Use descriptive, kebab-case names that reflect the change:
- `add-user-auth`
- `fix-login-redirect`
- `refactor-api-client`

## Common Workflows

### Creating a Stack

Start from trunk, create focused branches for each logical change. Keep commits atomic and well-described.

### Updating a Stack

When rebasing, update from the bottom of the stack upward. Resolve conflicts at each level before proceeding.
```

## Agents

Agents are specialized subagents that can be delegated tasks. They are defined in `.claude/agents/` or `<plugin>/agents/`.

### Agent Frontmatter

```yaml
---
name: agent-name (required)
description: "When Claude should delegate to this subagent" (required)
tools: Bash, Read, Grep (optional, inherits all if omitted)
disallowedTools: Write, Edit (optional, tools to deny)
model: sonnet | opus | haiku | inherit (optional, defaults to sonnet)
permissionMode: default | acceptEdits | dontAsk | bypassPermissions | plan (optional)
skills: skill-name, another-skill (optional, CSV format, injected at startup)
hooks: (optional, lifecycle hooks)
---
```

**Key differences from skills:**
- Agents use `tools` instead of `allowed-tools`
- Agents have `skills` field to inject skill content at startup (subagents don't inherit skills from parent)
- Agents support `permissionMode` and `disallowedTools`
- Skills are specified as comma-separated values, and their full content is injected into the subagent's context

## Sources

- [Agent Skills](https://code.claude.com/docs/en/skills)
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
