---
name: creating-plugins
description: "This skill should be used when creating, scaffolding, or setting up Claude Code plugins and marketplace configurations."
version: 1.0.0
---

# Creating Claude Code Plugins

Guidelines for creating and publishing Claude Code plugins with proper structure and marketplace configuration.

**Official Documentation:**
- [Plugins](https://code.claude.com/docs/en/plugins)
- [Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)

## Repository Structure

All plugin repositories require a `.claude-plugin/` directory at the repository root:

- **Single plugin repository**: `.claude-plugin/plugin.json` - See `references/single-plugin.md`
- **Multi-plugin repository**: `.claude-plugin/marketplace.json` - See `references/multi-plugin.md`

## Plugin Components

Plugins can contain:
- `commands/` - User-invoked actions (/command-name)
- `skills/` - Domain knowledge (auto-matched)
- `agents/` - Autonomous specialists (Task tool)
- `hooks/` - Event-driven automation

## Installation

**Local installation:**
```bash
# Single plugin
/plugin install /path/to/plugin-name

# Multi-plugin (from marketplace)
/plugin marketplace add /path/to/repo
/plugin install plugin-name@repo-name
```

**GitHub installation:**
```bash
# Add marketplace
/plugin marketplace add username/repo-name

# Install plugin (for single-plugin repos, plugin-name is the repo name)
/plugin install plugin-name@repo-name
```

**Private repositories:** Require SSH authentication.

## Plugin Development Patterns

**Single-purpose plugin:**
- One focused domain or tool
- Minimal components (1-3 skills, 1-5 commands)
- Example: Graphite workflow, Linear integration

**Workflow plugin:**
- Coordinates multiple tools/domains
- Multiple skills for different areas
- Commands that orchestrate workflows
- Example: Development workflow (git, PRs, testing)

**Multi-plugin repository:**
- Group related plugins by audience, team, or domain

## Best Practices

- Start with skills (domain knowledge) before commands
- Keep plugins focused on a single purpose or workflow
- Use semantic versioning for plugin.json
- Test locally before publishing
- Document all components in README
- Follow naming conventions for all components
- Use marketplace.json for repos with 2+ plugins

## Sources

- [Claude Code Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Claude Code Plugin Marketplaces Documentation](https://code.claude.com/docs/en/plugin-marketplaces)
