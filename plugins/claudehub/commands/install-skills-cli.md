---
description: Install the skills.sh CLI for 3rd party skill discovery
allowed-tools: Bash
---

## Process

1. **Verify/install the skills CLI**

   Run:
   ```bash
   npx skills --help
   ```

   This will install the skills CLI if not already present and display available commands.

2. **Explain the skills CLI**
   - The skills CLI (from skills.sh) lets you discover and install 3rd party skills for Claude Code
   - Browse available skills: `npx skills list`
   - Search for skills: `npx skills search <query>`
   - Install a skill: `npx skills add <skill-name>`
   - Skills integrate automatically with Claude Code once installed

3. **Report result**
   - Confirm the skills CLI is available
   - Suggest running `/claudehub:find-skills` to discover skills
