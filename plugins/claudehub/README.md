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
| `/claudehub:ralph` | Run Ralph Wiggum autonomous implementation iterations |
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

## Hooks

| Hook | Event | Description |
|------|-------|-------------|
| `setup-thoughts.sh` | SessionStart | Adds .thoughts/ to global gitignore |
