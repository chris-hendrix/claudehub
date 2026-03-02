# Agent Team Implementation

Orchestrate plan implementation using an agent team. You are the **team lead** — you coordinate work, manage the plan file, handle git operations, and commit after each phase completes. Teammates implement code.

**Prerequisite**: Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` enabled in settings.

## Verify Agent Teams Enabled

Before spawning any team, check that the environment variable is set. Look for it in:
1. `~/.claude/settings.json`
2. `~/.claude/settings.local.json`
3. `.claude/settings.json` (project root)
4. `.claude/settings.local.json` (project root)

Search for `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` set to `"1"` in an `env` block. If not found in any of these files, inform the user that agent teams are not enabled and ask if they want to enable it. If yes, add it to their project-level `.claude/settings.local.json`.

## Lead Responsibilities

The lead (you) owns everything except writing implementation code:

- Reading and parsing the plan
- Branch creation and git operations
- Creating the shared task list (TaskCreate)
- Spawning the team and delegating work
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

## Shared Task List

Use TaskCreate to create tasks from the plan before spawning the team. Include full descriptions with steps and checks from the plan. Set up dependencies between tasks (via TaskUpdate `addBlockedBy`) to reflect the ordering in the plan.

## Spawning the Team

Create the agent team and give it the full plan context — all phases, tasks, and their dependencies. Let the team lead (you) and the agent team infrastructure decide how to distribute work across teammates. The team will determine what can be parallelized based on task dependencies and file scope.

**Teammate prompts must include:**
- The plan file path so they can read architecture context
- Their assigned work with steps and checks verbatim from the plan
- Instruction to NOT modify the plan file or run git commands

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
