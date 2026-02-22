---
description: Install the full claudehub ecosystem
allowed-tools: Bash, AskUserQuestion, Read, Edit, Write, Skill, WebSearch, WebFetch
---

## Overview

This command sets up the complete claudehub ecosystem by running each install command in sequence.

## Process

Run each of the following commands using the Skill tool, in order:

1. **Install ecosystem plugins**
   - Run `/claudehub:install-plugins` using the Skill tool
   - This installs the rpi, ralph, and github plugins from the claudehub marketplace

2. **Install MCP servers**
   - Run `/claudehub:install-mcps` using the Skill tool
   - This installs context7 (library docs) and playwright (browser automation) MCP servers

3. **Install skills CLI**
   - Run `/claudehub:install-skills-cli` using the Skill tool
   - This installs the skills.sh CLI for discovering 3rd party skills

4. **Install statusline**
   - Run `/claudehub:install-statusline` using the Skill tool
   - This configures the Claude Code statusline with repo, branch, model, and context info

5. **Report overall status**
   - Summarize what was installed and any errors
   - Suggest the user restart their Claude Code session to pick up all changes
