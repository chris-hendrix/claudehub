# ClaudeHub Coordinator Plugin

Setup coordinator that installs the claudehub ecosystem: plugins, MCP servers, and skills.

## Installation

See the [main README](../../README.md) for marketplace setup.

```
claude plugin install claudehub@claudehub
```

## Commands

| Command | Description |
|---------|-------------|
| `/claudehub:setup` | Install the full ecosystem (runs all install commands) |
| `/claudehub:install-plugins` | Install rpi, ralph, and github plugins from marketplace |
| `/claudehub:install-mcps` | Install context7 and playwright MCP servers |
| `/claudehub:install-skills-cli` | Install the skills.sh CLI for 3rd party skill discovery |
| `/claudehub:install-statusline` | Install custom statusline with repo, branch, model, and context info |
| `/claudehub:find-skills` | Discover and install 3rd party skills from skills.sh |

## Quick Start

Run `/claudehub:setup` to install everything, or use individual install commands for selective setup.

## Statusline

The statusline displays repo name, branch, model, and context usage:

```
claude-hub | main | [Sonnet] | --------- 50%
```
