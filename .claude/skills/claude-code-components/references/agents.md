# Agents

Agents are autonomous specialists that perform tasks in separate sessions. They are invoked via the Task tool.

## How Agents Work

```
┌─────────────────────────────────────┐
│         MAIN SESSION                │
│  (full conversation context)        │
│                                     │
│  User: "help me refactor auth"      │
│  Claude: analyzing...               │
│  User: "also check for security"    │
│  Claude: I'll spawn an agent...     │
│          │                          │
│          │ Task(prompt)             │
│          ▼                          │
│  ┌─────────────────────────────┐    │
│  │       AGENT SESSION         │    │
│  │   (only receives prompt)    │    │
│  │                             │    │
│  │   "check auth for security" │    │
│  │         ...works...         │    │
│  │   "Found 3 issues: ..."     │    │
│  └──────────────┬──────────────┘    │
│                 │                   │
│                 │ output            │
│                 ▼                   │
│  Claude: The agent found 3 issues   │
│                                     │
└─────────────────────────────────────┘
```

The agent has no memory of prior conversation - it only sees the prompt you pass. Its output is returned to the main session.

## Location

```
.claude/agents/
├── code-reviewer.md
├── codebase-analyzer.md
└── pattern-finder.md
```

## Naming

**Pattern:** `{noun-role}`

Name them like job titles. Lowercase, hyphens, 3-50 characters.

**Litmus test:** Could say "the {name}" or "ask the {name}"

| Good | Bad |
|------|-----|
| `codebase-analyzer` | `analyze-codebase` (verb, not role) |
| `code-reviewer` | `review` (action, not worker) |
| `web-researcher` | `researching` (gerund, not role) |
| `pattern-finder` | `patterns` (thing, not worker) |
| `bug-hunter` | `hunt-bugs` (command, not role) |

## Frontmatter

```yaml
---
name: agent-name (required)
description: "Use this agent when..." with <example> blocks (required)
model: sonnet | opus | haiku | inherit (required)
color: blue | cyan | green | yellow | magenta | red (required)
tools: ["Read", "Grep", "Glob"] (optional)
skills: skill1, skill2 (optional)
permissionMode: default | inherit (optional)
---
```

## Writing Guidelines

- **Scope:** Keep agents focused on a single responsibility
- **Tools:** Only include tools the agent actually needs
- **Skills:** Load skills for methodology the agent should follow (agents use skills, not vice versa)

## Example

```markdown
---
name: codebase-analyzer
description: "Use this agent when you need to understand how a specific component or system works in the codebase."
model: sonnet
color: cyan
tools: ["Read", "Grep", "Glob", "LS"]
---

You are a codebase analyzer. Your role is to investigate and explain how code works.

## Approach

1. Start with the entry point or main file
2. Trace dependencies and data flow
3. Document key patterns and abstractions
4. Summarize findings with file:line references

## Output

Provide a clear explanation of how the system works, including:
- Architecture overview
- Key files and their responsibilities
- Data flow between components
```

## Source

- [Subagents](https://code.claude.com/docs/en/sub-agents)
