---
description: Implement plan using an agent team with commit-per-phase workflow
argument-hint: [plan file]
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion, Glob, Grep, Skill
model: opus
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool
- **You MUST create an agent team to implement this plan. Do NOT implement code yourself or use subagents. You are the team lead — you coordinate, teammates implement.**

## Skills

- `rpi:implementing` - confidence assessment, plan file update format, phase verification
  - **Read `references/agent-teams.md` for the full agent team orchestration workflow — follow it exactly**
- `rpi:writing-documentation` - summary file naming and frontmatter

## Process

1. Verify `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` is enabled in settings (see `agent-teams.md`). Offer to enable if not. **Stop if not enabled.**

2. Gather context (plan file from `.thoughts/plans/` or clarify with user)

3. **Branch setup**: If on `main`/`master`, suggest a branch name and ask the user to confirm, provide a custom name, or stay on current branch

4. Assess confidence and present phases for confirmation (per `implementing` skill)

5. **Create an agent team now.** Spawn teammates from the plan's phases per `agent-teams.md`. Do NOT use subagents. Do NOT implement code yourself.

6. **Coordinate as team lead**: monitor progress, verify phase checks, update plan file, commit-per-phase, wait for teammates to finish

7. Complete: update plan status, run full verification, write summary to `.thoughts/implementations/`, final commit and push, clean up the agent team

Input: $ARGUMENTS
