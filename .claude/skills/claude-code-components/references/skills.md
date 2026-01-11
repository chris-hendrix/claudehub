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

## Example

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
