---
description: Set up GitHub PR and issue templates in the repository
allowed-tools: Bash
---

## Process

1. Run the setup-templates script to copy PR and issue templates to `.github/` directory

The script will:
- Create `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` if it doesn't exist
- Create `.github/ISSUE_TEMPLATE/issue_template.md` if it doesn't exist
- Skip existing templates to avoid overwriting customizations

```bash
${CLAUDE_PLUGIN_ROOT}/.support/scripts/setup-templates.sh
```
