---
description: Monitor CI/CD runs and auto-fix failures until green (up to 5 attempts)
argument-hint: [--max-attempts N]
allowed-tools: Bash, Agent, AskUserQuestion, Skill
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `github:github` - Git/GitHub workflow, branch naming, and PR conventions (see references/gha.md)

## Agents

- `ci-watcher` - Monitors GHA runs on the current branch, reports pass/fail
- `ci-fixer` - Diagnoses failures from logs, fixes code, commits & pushes

## Process

Parse `--max-attempts N` from arguments if provided (default: 5).

### 1. Preflight

- Verify you are on a feature branch (not main/master)
- Verify GitHub Actions runs exist for this branch: `gh run list --branch "$(git branch --show-current)" --limit 1`
- If no runs found, inform user and exit

### 2. Watch-Fix Loop

Set `attempt = 0`. Loop:

#### Watcher Phase

Spawn the `ci-watcher` agent. It will monitor runs for the current HEAD and return a status summary with overall PASS/FAIL and any failed run IDs.

**Do not read any files while waiting for the watcher to return.**

If **Overall: PASS**, report success and exit the loop.

#### Fixer Phase

If **Overall: FAIL**, increment `attempt`. If `attempt >= max_attempts`, report the failure summary and exit.

Otherwise, spawn the `ci-fixer` agent with the failed run IDs. It will read failure logs, diagnose the issue, fix the code, and push.

If the fixer reports **UNABLE_TO_FIX**, report to user and exit. Otherwise, loop back to the Watcher Phase.

### 3. Final Report

After the loop exits (success or max attempts), display a summary:
- Total attempts made
- Final CI status
- If failed: the last failure logs and what was tried

Input: $ARGUMENTS
