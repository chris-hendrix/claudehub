# Hooks

Event-triggered scripts that run automatically for side effects and validation.

## Location

For plugins, hooks are configured in `hooks/hooks.json`:
```
my-plugin/
├── hooks/
│   ├── hooks.json          # Hook configuration
│   ├── pre-commit-lint.sh
│   └── post-edit-format.py
└── plugin.json
```

For project-level hooks (not plugins), use `.claude/settings.json` instead.

## Events

Hooks trigger on these events:

| Event | Trigger |
|-------|---------|
| `UserPromptSubmit` | User submits a prompt |
| `PreToolUse` | Before a tool runs |
| `PermissionRequest` | User shown permission dialog |
| `PostToolUse` | After a tool completes |
| `Stop` | Claude finishes or user stops |
| `SubagentStop` | Agent completes |
| `SessionStart` | Session begins |
| `SessionEnd` | Session ends |
| `PreCompact` | Before context compaction |
| `Notification` | Claude sends notification |

## Types

- **Command hooks:** Deterministic, fast shell scripts (all events)
- **Prompt hooks:** LLM-driven, context-aware checks (Stop and SubagentStop only)

## Matchers

- Exact: `"Bash"`, `"Edit"`
- Wildcard: `"mcp__*"`, `"Bash(git:*)"`
- Regex: `"/^mcp__slack/"`

## Example

In `hooks/hooks.json` (requires top-level `"hooks"` wrapper):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [{ "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/setup.sh" }]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/validate.sh" }]
      }
    ]
  }
}
```

## Source

- [Hooks Reference](https://code.claude.com/docs/en/hooks)
