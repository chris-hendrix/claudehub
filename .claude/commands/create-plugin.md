---
description: Create and scaffold a new Claude Code plugin
argument-hint: [plugin-name]
allowed-tools: Bash, Read, Write, Skill, AskUserQuestion
---

IMPORTANT: Load referenced skills using the Skill tool. Ask the user for plugin information if input is unclear.

## Skills

- `creating-plugins` - Plugin structure and marketplace configuration
- `claude-code-components` - Component naming conventions and best practices

## Process

1. Gather plugin information:
   - Plugin name (from $ARGUMENTS or ask)
   - Plugin description
   - What components to include (commands, skills, agents, hooks)
2. Check if we're in an existing plugin repo (check for `.claude-plugin/` directory)
3. Create the appropriate plugin structure:
   - For single-plugin: Create `.claude-plugin/plugin.json` at root
   - For multi-plugin: Create/update `.claude-plugin/marketplace.json` at root, then create plugin directory
4. Scaffold the requested components with proper naming and structure
5. Create a README.md with plugin documentation
6. Show installation instructions and next steps

Input: $ARGUMENTS
