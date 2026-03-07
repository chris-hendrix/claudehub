---
description: Implement plan using an agent team with commit-per-phase workflow
argument-hint: [plan file]
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion, Glob, Grep, Skill, Task, TaskCreate, TaskUpdate, TaskList, TaskGet
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `rpi:implementing` - execution methodology, confidence assessment, plan updates
  - See `references/agent-teams.md` for team-specific orchestration
- `rpi:writing-documentation` - summary file naming and frontmatter

## Process

1. Verify agent teams are enabled in settings (see `agent-teams.md`), offer to enable if not

2. Gather context (plan file from `.thoughts/plans/` or clarify with user)

3. **Branch setup**: If on `main`/`master`, suggest a branch name and ask the user to confirm, provide a custom name, or stay on current branch

4. Assess confidence and present phases for confirmation (per `implementing` skill)

5. **Spawn team**: Create tasks from the plan (TaskCreate with dependencies), spawn agent team and let it decide how to distribute work

6. **As each phase completes**: Verify checks, update plan file, commit and push

7. Complete: update plan status, run full verification, write summary to `.thoughts/implementations/`, final commit and push, clean up team

See `implementing` skill reference `agent-teams.md` for the full workflow, teammate prompt requirements, and error recovery.

Input: $ARGUMENTS
