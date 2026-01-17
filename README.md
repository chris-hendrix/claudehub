# ClaudeHub

A marketplace of Claude Code plugins for GitHub workflows and systematic development.

## Installation

Add the marketplace:
```bash
claude plugin marketplace add /path/to/claudehub
```

Or use the Makefile:
```bash
make install              # Install marketplace and all plugins
make install-marketplace  # Install just the marketplace
make install-plugins      # Install all plugins
```

## Plugins

### [ClaudeHub Plugin](./plugins/claudehub)

Research-plan-implement workflow automation for systematic development.

**Commands:**
- `/claudehub:brainstorm` - Brainstorm an idea into a validated design
- `/claudehub:create-plan` - Create detailed implementation plans through research
- `/claudehub:implement` - Implement from a plan or description
- `/claudehub:ralph` - Run Ralph Wiggum autonomous implementation iterations
- `/claudehub:evaluate` - Assess output across relevant quality dimensions
- `/claudehub:create-doc` - Create a new document in .thoughts/

**Skills:**
- `researching-codebase` - Investigate and document codebases
- `writing-plans` - Create detailed implementation plans
- `implementing` - Execute implementation with review checkpoints
- `ralph-wiggum` - Loop-based autonomous implementation methodology
- `brainstorming` - Refine ideas into designs through dialogue
- `evaluating` - Dimension-based artifact assessment
- `writing-documentation` - .thoughts/ document conventions

**Workflow:**
1. **Research**: Use researching-codebase skill to understand codebases
2. **Brainstorm**: `/claudehub:brainstorm` to explore design alternatives
3. **Plan**: `/claudehub:create-plan` to create detailed implementation plans
4. **Implement**: `/claudehub:implement` to execute with confidence checks and phase verification
5. **Evaluate**: `/claudehub:evaluate` to assess output quality

**Installation:**
```bash
/plugin install claudehub@claudehub
```

[Read more →](./plugins/claudehub/README.md)

---

### [GitHub Plugin](./plugins/github)

Git and GitHub workflow automation with best practices for commits, PRs, and branch management.

**Commands:**
- `/github:create-branch` - Create a new git branch with AI-suggested name
- `/github:submit-pr` - Commit changes, push to remote, and create/update draft PR
- `/github:describe-pr` - Generate and update PR title and description from branch diff
- `/github:checkout-default` - Switch to default branch and sync with remote
- `/github:clean-branches` - Delete local branches that were merged or closed in origin
- `/github:create-issue` - Create a GitHub issue with AI-generated content

**Skills:**
- `github` - Workflow methodology using GitHub Issues, GitHub PRs, and raw git commands

**Installation:**
```bash
/plugin install github@claudehub
```

[Read more →](./plugins/github/README.md)

## Development

This repository includes development skills for creating your own plugins:

| Skill | Description |
|-------|-------------|
| [claude-code-components](./.claude/skills/claude-code-components) | Guidelines for creating Claude Code components including skills, slash commands, agents, and hooks |
| [creating-plugins](./.claude/skills/creating-plugins) | Guidelines for creating and publishing Claude Code plugins with marketplace configuration |
