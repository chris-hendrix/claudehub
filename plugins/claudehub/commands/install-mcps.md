---
description: Install context7 and playwright MCP servers
allowed-tools: Bash, AskUserQuestion
---

## Process

1. **Install context7 MCP server**

   - Tell the user: "context7 provides up-to-date library documentation. You'll need an API key from https://context7.com/dashboard (free tier available)."
   - Use `AskUserQuestion` to ask: "What is your context7 API key? (Get one at https://context7.com/dashboard)"
   - Run the install command with their key:
     ```bash
     claude mcp add context7 --transport stdio --env CONTEXT7_API_KEY=<key> -- npx -y @upstash/context7-mcp@latest
     ```
   - Note to user: "This passes the API key as an environment variable to the MCP process. This is generally fine for a personal API token that can be rotated/deleted. For manual install without sharing the key in conversation, run: `claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp --header \"CONTEXT7_API_KEY: YOUR_API_KEY\"`"

2. **Install playwright MCP server**

   Run:
   ```bash
   claude mcp add playwright --transport stdio -- npx -y @playwright/mcp@latest
   ```

3. **Report results**
   - List which MCP servers were installed successfully
   - Suggest running `claude mcp list` to verify
