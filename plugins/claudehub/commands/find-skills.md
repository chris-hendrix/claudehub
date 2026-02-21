---
description: Discover and install 3rd party skills from skills.sh
argument-hint: [search query or topic]
allowed-tools: Bash, WebSearch, WebFetch
---

## Process

1. **Understand what the user is looking for**
   - If `$ARGUMENTS` is provided, use it as the search query
   - If no arguments, browse the skills.sh leaderboard

2. **Search for skills**

   Run:
   ```bash
   npx skills search $ARGUMENTS
   ```

   If the skills CLI is not installed, tell the user to run `/claudehub:install-skills-cli` first.

3. **Present results**
   - Show available skills matching the query
   - Include skill name, description, and install command for each

4. **Install if requested**
   - To install a skill: `npx skills add <skill-name>`
   - Skills integrate automatically with Claude Code once installed
   - The user may need to restart their Claude Code session to pick up new skills
