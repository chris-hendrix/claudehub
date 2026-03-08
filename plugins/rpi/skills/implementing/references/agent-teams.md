# Agent Team Implementation

**You MUST create an agent team.** Do NOT use subagents (Agent tool). Do NOT implement code yourself. You are the **team lead** — you coordinate work, manage the plan file, handle git operations, and commit after each phase completes. Teammates implement code.

**Prerequisite**: Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` enabled in settings.

## Verify Agent Teams Enabled

Before spawning any team, check that the environment variable is set. Look for it in:
1. `~/.claude/settings.json`
2. `~/.claude/settings.local.json`
3. `.claude/settings.json` (project root)
4. `.claude/settings.local.json` (project root)

Search for `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` set to `"1"` in an `env` block. If not found in any of these files, inform the user that agent teams are not enabled and ask if they want to enable it. If yes, add it to their project-level `.claude/settings.local.json`:

```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

**Stop here if not enabled — agent teams cannot work without this setting.**

## Lead Responsibilities

The lead (you) owns everything except writing implementation code:

- Reading and parsing the plan
- Branch creation and git operations
- Creating the shared task list
- Creating the agent team and spawning teammates
- Monitoring progress and resolving issues
- Updating the plan file (checkboxes, tracked changes, frontmatter)
- Committing and pushing after each phase

**Teammates never touch the plan file or run git commands.** This prevents conflicts.

## Branch Setup

Before starting implementation, ensure you're on a feature branch:

```bash
branch=$(git branch --show-current)
```

- If on `main` or `master`: derive a branch name from the plan topic. Use AskUserQuestion to ask the user if they want to create a branch, presenting the suggested name as an option alongside "Stay on current branch" and an option to provide a custom name. If confirmed, create and push with `-u`.
- If already on a feature branch: continue on it

## Creating the Agent Team

**This is the critical step.** Create an agent team — not subagents — to implement the plan.

1. Analyze the plan to determine how many teammates are needed (typically 3-5) based on independent phases/tasks
2. Group tasks that can run in parallel vs those with dependencies
3. Create the agent team with a shared task list containing all tasks from the plan, with dependencies reflecting the plan's ordering
4. Spawn teammates, each with a clear prompt

**Each teammate's spawn prompt MUST include:**
- The plan file path so they can read architecture context
- Their specific assigned tasks with steps and checks verbatim from the plan
- **"Do NOT modify the plan file. Do NOT run git commands (git add, git commit, git push). The team lead handles all git operations and plan updates."**

**Wait for teammates to finish their tasks.** Do NOT implement tasks yourself. If the team needs more workers, spawn additional teammates rather than doing the work.

## Commit-Per-Phase Workflow

This is the key constraint. Regardless of how work is distributed across teammates:

1. **After all tasks in a phase complete**: verify phase-level checks from the plan
2. **Update the plan file**: check off completed steps, checks, and tasks (`- [ ]` → `- [x]`). Record any deviations in Tracked Changes.
3. **Commit and push**:

```bash
git add -A
git commit -m "Phase N: <phase name>

<1-2 sentence summary>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
git push
```

4. **Next phase unblocks** and teammates continue

If a teammate gets stuck:
- Message them directly with guidance
- Or shut them down and handle the work yourself

## Completion

After all phases:

1. Update plan frontmatter to `status: completed`
2. Run full verification suite (success criteria from the plan)
3. Write implementation summary to `.thoughts/implementations/`
4. Final commit and push
5. Clean up the agent team

## Error Recovery

| Problem | Action |
|---------|--------|
| Teammate fails checks | Fix as lead or spawn replacement teammate |
| Phase verification fails | Fix before committing — never push broken code |
| Git push fails | Pull, rebase, resolve conflicts, push again |
| Teammate stuck/unresponsive | Shut down and handle work directly |
