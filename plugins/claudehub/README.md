# ClaudeHub Plugin

Research-plan-implement workflow automation for systematic development.

## Installation

See the [main README](../../README.md) for marketplace setup.

```
/plugin install claudehub@claudehub
```

## Commands

| Command | Description |
|---------|-------------|
| `/claudehub:research-web` | Search the web and save findings to research doc |
| `/claudehub:brainstorm` | Brainstorm an idea into a validated design |
| `/claudehub:create-plan` | Create detailed implementation plans through research |
| `/claudehub:implement` | Implement from a plan or description |
| `/claudehub:ralph-run` | Start Ralph execution loop (auto-plans if needed) |
| `/claudehub:ralph-plan` | Create Ralph planning docs quickly with autonomous decisions |
| `/claudehub:ralph-plan-deep` | Interactive deep planning (90% confidence required) |
| `/claudehub:ralph-validate` | Validate test environment and suites before execution |
| `/claudehub:ralph-status` | Show current Ralph execution progress |
| `/claudehub:ralph-cancel` | Stop the active Ralph execution loop |
| `/claudehub:evaluate` | Assess output across relevant quality dimensions |
| `/claudehub:create-doc` | Create a new document in .thoughts/ |

## Skills

| Skill | Description |
|-------|-------------|
| `researching-web` | Web research methodology and synthesis |
| `researching-codebase` | Investigate and document codebases |
| `writing-plans` | Create detailed implementation plans |
| `implementing` | Execute implementation with review checkpoints |
| `ralph-wiggum` | Loop-based autonomous implementation methodology |
| `brainstorming` | Refine ideas into designs through dialogue |
| `evaluating` | Dimension-based artifact assessment |
| `writing-documentation` | .thoughts/ document conventions |

## .thoughts/ Folder

Local, gitignored directory for working documents during development.

**Common subdirectories:**
- `plans/` - Implementation plans, roadmaps
- `brainstorms/` - Design explorations
- `implementations/` - Implementation summaries
- `evaluations/` - Artifact evaluations

Documents follow: `YYYY-MM-DD-<description>.md`

## Workflow

1. **Research**: Use researching-codebase skill to understand codebases
2. **Brainstorm**: `/claudehub:brainstorm` to explore design alternatives and validate objectives
3. **Plan**: `/claudehub:create-plan` to create detailed specs and implementation checklists (phases → tasks → steps)
4. **Implement**: `/claudehub:implement` to execute from the plan, checking off items and tracking changes as a living document
5. **Evaluate**: `/claudehub:evaluate` to assess output quality

## Ralph Wiggum - Autonomous Implementation

Ralph executes engineering tasks through a Python orchestrator that spawns Claude Code sessions. Each session runs a structured agent pipeline to complete one task.

### Agent Pipeline

```
3x researcher (parallel) → coder → verifier + reviewer (parallel)
```

**Agents:**
- `researcher` - Gather context (LOCATING, ANALYZING, PATTERNS focus modes)
- `coder` - Write implementation + tests
- `verifier` - Run tests, linting, type-checking
- `reviewer` - Code review and quality assessment
- `ralph-validator` - Validate test infrastructure works

### File Structure

All Ralph files live in `.ralph/`:

| File | Purpose |
|------|---------|
| `ARCHITECTURE.md` | Technical approach (services, schema, APIs) |
| `TASKS.md` | Tasks with checkboxes, organized by phase |
| `VERIFICATION.md` | Test commands, environment setup |
| `PROGRESS.md` | Learnings and results from each iteration |
| `screenshots/` | Visual proof from manual testing |
| `logs/{branch}/` | Session logs per iteration (gitignored) |

### Quick Start

```bash
# Quick autonomous planning + execution
/claudehub:ralph-run "add user authentication with JWT"

# Or plan interactively first (90% confidence required)
/claudehub:ralph-plan-deep docs/prd.md
/claudehub:ralph-validate  # Validate test environment works
/claudehub:ralph-run

# Check status
/claudehub:ralph-status

# Stop execution
/claudehub:ralph-cancel
```

### Branch Naming

Format: `ralph/yyyymmdd-hhmm-short-description`

Example: `ralph/20260131-1430-user-auth`

## Hooks

| Hook | Event | Description |
|------|-------|-------------|
| `setup-thoughts.sh` | SessionStart | Adds .thoughts/ to global gitignore |
