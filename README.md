# ClaudeHub

**Supercharge your development workflow with systematic research, planning, and autonomous implementation.**

The most critical factor in successful LLM-assisted development is **alignment**: ensuring you and the AI are on the same page before writing code. ClaudeHub's spec-driven workflow gets you there through collaborative research, brainstorming, and detailed planning before autonomous implementation.

_Inspired by [CipherPowers](https://github.com/cipherstash/cipherpowers/), [Superpowers](https://github.com/obra/superpowers), and [HumanLayer](https://github.com/humanlayer/humanlayer)._

## Plugins

ClaudeHub is a marketplace of 4 focused plugins:

| Plugin | Description |
|--------|-------------|
| **claudehub** | Setup coordinator - installs ecosystem plugins, MCPs, and skills |
| **rpi** | Research-plan-implement workflow for systematic development |
| **ralph** | Autonomous agent execution through researcher-coder-verifier-reviewer pipeline |
| **github** | Git and GitHub workflow automation with best practices |

## Quick Start

**1. Install the marketplace:**

```bash
# From local clone
claude plugin marketplace add /path/to/claudehub

# Or from GitHub
claude plugin marketplace add chris-hendrix/claudehub
```

**2. Install the coordinator and run setup:**

```bash
claude plugin install claudehub@claudehub
/claudehub:setup
```

This installs all plugins, MCP servers (context7, playwright), the skills CLI, and the statusline.

**3. Or install plugins individually:**

```bash
claude plugin install rpi@claudehub      # Research-plan-implement
claude plugin install ralph@claudehub    # Autonomous execution
claude plugin install github@claudehub   # GitHub workflows
```

## RPI - Research, Plan, Implement

Proven methodology for transforming messy ideas into production-ready code.

```bash
# Research a codebase
/rpi:research-codebase "how does authentication work"

# Brainstorm an idea
/rpi:brainstorm "Add user authentication with OAuth"

# Create a detailed plan
/rpi:plan brainstorm.md

# Implement from the plan
/rpi:implement plan.md

# Evaluate the output
/rpi:evaluate
```

**Commands:**

| Command | Description |
|---------|-------------|
| `/rpi:research-web` | Search the web and save findings to research doc |
| `/rpi:research-codebase` | Investigate code and create documentation |
| `/rpi:brainstorm` | Brainstorm an idea into a validated design |
| `/rpi:plan` | Create detailed implementation plans |
| `/rpi:implement` | Implement from a plan or description |
| `/rpi:evaluate` | Assess output across quality dimensions |
| `/rpi:create-doc` | Create a new document in .thoughts/ |

## Ralph - Autonomous Execution

Your autonomous coding companion that implements features through a structured engineering workflow. Ralph executes tasks through a Python orchestrator that spawns Claude Code sessions, each running a specialized agent pipeline.

```bash
# Quick autonomous planning + execution
/ralph:run "add user authentication with JWT"

# Or plan interactively first (90% confidence required)
/ralph:plan-deep docs/prd.md
/ralph:validate
/ralph:run

# Check status or cancel
/ralph:status
/ralph:cancel
```

**The Agent Pipeline:**

```
3x researcher (parallel) -> coder -> verifier + reviewer (parallel)
```

**Commands:**

| Command | Description |
|---------|-------------|
| `/ralph:run` | Start execution loop (auto-plans if needed) |
| `/ralph:plan` | Quick autonomous planning |
| `/ralph:plan-deep` | Interactive deep planning (90% confidence required) |
| `/ralph:validate` | Validate test environment before execution |
| `/ralph:status` | Show current execution progress |
| `/ralph:cancel` | Stop the active execution loop |

_Inspired by Geoffrey Huntley's [Ralph methodology](https://ghuntley.com/ralph/)._

## GitHub - Workflow Automation

Streamlined git workflows: intelligent PR creation, branch management, and commit automation.

```bash
/github:submit-pr          # Commit, push, create draft PR
/github:create-branch      # Create branch with AI-suggested name
/github:describe-pr        # Generate PR title and description
/github:checkout-default   # Switch to default branch and sync
/github:clean-branches     # Delete merged/closed local branches
/github:create-issue       # Create issue with AI content
/github:setup-templates    # Set up PR and issue templates
```

## Coordinator Commands

| Command | Description |
|---------|-------------|
| `/claudehub:setup` | Install the full ecosystem (runs all install commands) |
| `/claudehub:install-plugins` | Install rpi, ralph, and github plugins |
| `/claudehub:install-mcps` | Install context7 and playwright MCP servers |
| `/claudehub:install-skills-cli` | Install the skills.sh CLI |
| `/claudehub:install-statusline` | Install custom statusline |
| `/claudehub:find-skills` | Discover and install 3rd party skills |

## Makefile

For development and local management:

```bash
make add-all       # Install all 4 plugins
make remove-all    # Uninstall all 4 plugins
make add-rpi       # Install just the rpi plugin
make add-ralph     # Install just the ralph plugin
make help          # Show all available targets
```

## Migration from v1

If you were using the monolithic claudehub plugin, commands have moved to new namespaces:

| Old Command | New Command |
|-------------|-------------|
| `/claudehub:brainstorm` | `/rpi:brainstorm` |
| `/claudehub:create-plan` | `/rpi:plan` |
| `/claudehub:implement` | `/rpi:implement` |
| `/claudehub:evaluate` | `/rpi:evaluate` |
| `/claudehub:research-web` | `/rpi:research-web` |
| `/claudehub:research-codebase` | `/rpi:research-codebase` |
| `/claudehub:create-doc` | `/rpi:create-doc` |
| `/claudehub:ralph:run` | `/ralph:run` |
| `/claudehub:ralph:plan` | `/ralph:plan` |
| `/claudehub:ralph:plan-deep` | `/ralph:plan-deep` |
| `/claudehub:ralph:status` | `/ralph:status` |
| `/claudehub:ralph:cancel` | `/ralph:cancel` |
| `/claudehub:ralph:validate` | `/ralph:validate` |

The github plugin commands are unchanged.
