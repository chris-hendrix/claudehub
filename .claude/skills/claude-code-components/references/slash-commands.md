# Slash Commands

Slash commands (also simply "commands") are actions users invoke directly via `/command-name`.

## Location

```
.claude/commands/
├── deploy.md
├── create-pr.md
└── run-tests.md
```

## Naming

**Pattern:** `{verb}` or `{verb-noun}`

Keep names short and imperative.

**Litmus test:** Could follow "please..."

| Good | Bad |
|------|-----|
| `commit` | `committer` (role, not action) |
| `create-pr` | `pr-creation` (noun, not verb) |
| `submit-pr` | `graphite-submit` (tool name prefix) |
| `describe-pr` | `pr` (too vague) |
| `checkout-master` | `master-checkout` (noun-verb order) |

## Frontmatter

```yaml
---
description: "Shows in command list" (required)
argument-hint: [placeholder] (optional)
allowed-tools: Bash, Read, Glob (optional)
model: sonnet | opus | haiku (optional)
disable-model-invocation: true (optional, prevents model from invoking)
---
```

## Template

```markdown
---
description: "Command description"
argument-hint: [optional placeholder]
allowed-tools: Tool1, Tool2
---

IMPORTANT: Load referenced skills using the Skill tool. Ask the user for context if input is unclear.

## Skills

- `skill-name` - Brief description of what it provides

## Process

1. First step
2. Second step
3. Third step

Input: $ARGUMENTS
```

## Writing Guidelines

Slash commands should be concise. Use two sections:

- **Skills** (optional): List skills with brief descriptions of what they provide
- **Process**: Numbered steps for execution

Not all slash commands need skills. Simple actions (`checkout-master`, `run-tests`) may just have a Process section. But if you find yourself writing detailed methodology, that belongs in a skill.

**IMPORTANT:**
- Always load any referenced skills using the Skill tool before proceeding with the process
- Always ask the user for context if the input is unclear - don't proceed with assumptions when clarification is cheap

## Example

```markdown
---
description: Submit a PR with auto-generated description
argument-hint: [optional PR title]
allowed-tools: Bash, Read, Glob, Skill
---

IMPORTANT: Load referenced skills using the Skill tool. Ask the user for context if input is unclear.

## Skills

- `graphite` - Submit commands
- `writing-prs` - PR conventions

## Process

1. Check branch and PR status
2. Confirm what to submit
3. Submit the PR
4. Offer to update title/description

Input: $ARGUMENTS
```

## Source

- [Slash Commands](https://code.claude.com/docs/en/slash-commands)
