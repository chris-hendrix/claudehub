---
name: claude-code-components
description: "This skill should be used when creating or modifying Claude Code components including skills, slash commands, agents, and hooks. It provides naming conventions, structure guidelines, best practices, and antipatterns."
version: 1.0.0
---

# Claude Component Authoring

Guidelines for creating Claude Code components. All components work via prompt injection - they add instructions to Claude's context.

These components can be used in:
- Project-level configurations (`.claude/` directory)
- Plugins (distributed as packages)
- Standalone setups

## Quick Reference

| Component | Purpose | Invocation | Can Reference | Location | Details |
|-----------|---------|------------|---------------|----------|---------|
| Skill | Domain knowledge | Claude matches context → injects knowledge | Other skills, CLI/MCP tools | `.claude/skills/` | `references/skills.md` |
| Slash Command | User-invoked actions | User types `/command-name` | Skills, agents | `.claude/commands/` | `references/commands.md` |
| Agent | Autonomous specialists | Claude matches context → spawns isolated worker via Task tool | Skills | `.claude/agents/` | `references/agents.md` |
| Hook | Event-driven automation | System triggers script or prompt on events | N/A | `hooks/hooks.json` | `references/hooks.md` |

## Component Relationships

Understanding how components interact is key to effective design:

**Hierarchy:**
```
┌─────────────────────────────────────────────┐
│         Component Hierarchy                  │
│                                              │
│  Slash Commands ──uses──> Skills ──references──> Skills
│        │                     ↑                │
│        │                     │                │
│        └──spawns──> Agents                   │
│                                              │
│  Hooks (standalone, event-driven)           │
└─────────────────────────────────────────────┘
```

**Cross-Referencing Rules:**
- **Skills** are foundational - they provide domain knowledge and methodology. Skills may reference other skills or document external CLI/MCP tools, but should never reference slash commands or agents.
- **Slash Commands** orchestrate skills and spawn agents. If you find yourself writing detailed methodology in a slash command, that content belongs in a skill.
- **Agents** use skills for methodology. Agents are spawned by slash commands or Claude's context matching, and they consume skills but never reference slash commands.
- **Hooks** are standalone and event-driven - they don't follow the hierarchy.

**When to Use Each Component:**
- Use a **Skill** when you need to teach Claude *how to think* about a domain - principles, patterns, and decision frameworks
- Use a **Slash Command** when you need a user-invoked action that follows specific steps
- Use an **Agent** when you need an autonomous specialist to perform work in isolation
- Use a **Hook** when you need automation triggered by system events

## Naming Conventions

**Universal Rules:**
- Use lowercase with hyphens (e.g., `my-component-name`)
- Keep names concise and descriptive
- Avoid acronyms unless widely recognized (e.g., `pr`, `api` are fine; `tkt` for ticket or issue is not)
- Length: Aim for 3-50 characters, prioritizing clarity

**Component-Specific Patterns:**

| Component | Pattern | Litmus Test | Examples (Good → Bad) |
|-----------|---------|-------------|----------------------|
| **Skills** | `{gerund}` or tool name | "Help me with {name}" sounds natural | `planning` → `plan`<br>`writing-documentation` → `documentation`<br>`graphite` → `graphite-commands` |
| **Slash Commands** | `{verb}` or `{verb-noun}` | Could follow "please..." | `commit` → `committer`<br>`create-pr` → `pr-creation`<br>`describe-pr` → `pr` |
| **Agents** | `{noun-role}` | Could say "the {name}" or "ask the {name}" | `codebase-analyzer` → `analyze-codebase`<br>`code-reviewer` → `review`<br>`pattern-finder` → `patterns` |

## Writing Best Practices

**Conciseness:**
Claude is smart - only add context Claude doesn't already have. Challenge each paragraph: "Does this justify its token cost?"

**Voice and Structure:**
- Use imperative form in the body, not second person
- Keep main files under 500 lines (skills)
- Commands should be concise action lists

**Progressive Disclosure:**
For large skills, use a `references/` subdirectory to split out detailed content. This is optional for smaller skills. Keep references one level deep - avoid nested file chains.

**Description Formats by Component:**
- **Skills**: Use third-person ("This skill should be used when..."), include what the skill does AND when to use it. Listing activities is fine (e.g., "including creating, updating, and deleting X").
- **Slash Commands**: Keep brief - shows in command list
- **Agents**: Start with "Use this agent when...", include example invocations

**Tool Reference Documentation:**
Skills are the ideal place to document external tools - both CLI tools (`gh`, `gt`, `npm`) and MCP tools (`mcp__linear__*`, `mcp__slack__*`). This includes tool names, parameters, and usage patterns. This is reference documentation, not to be confused with slash commands.

## Antipatterns

**Universal:**
- **Violating component hierarchy**: Skills referencing slash commands/agents; slash commands containing detailed methodology that belongs in skills

**Skills:**
- **Referencing Slash Commands or Agents**: Skills are foundational knowledge - they should never tell Claude to "run /command" or "spawn the X agent". Slash commands and agents use skills, not the other way around. (CLI and MCP tool references are fine - these are reference documentation.)

**Slash Commands:**
- **Script-Heavy Commands**: A slash command with multiple bash scripts embedded is an antipattern. If the command is mostly shell logic, it should just be a shell script instead.
- **Over-Scripted Questions**: Avoid scripting every question Claude should ask. Key confirmation points are fine (e.g., "Confirm with user before committing"), but trust Claude to gather missing context naturally.
- **Methodology in Commands**: Process steps should be actions, not methodology. If a step explains *how* to think about something, move it to a skill. Note: Output actions ("Show", "Display", "Report") and execution directives ("in parallel", "spawn agent per X", "use Task tool") are valid—these control orchestration, not reasoning.

