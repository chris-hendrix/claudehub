# GitHub Actions

CLI patterns for monitoring, diagnosing, and managing GitHub Actions CI/CD runs using the `gh` CLI.

## Listing Runs

```bash
# List recent runs on current branch
gh run list --branch "$(git branch --show-current)" --limit 10

# JSON output for scripting (id, status, conclusion, name, event)
gh run list --branch "$(git branch --show-current)" --limit 10 --json databaseId,status,conclusion,name,event,headSha

# Filter by status
gh run list --branch "$(git branch --show-current)" --status queued
gh run list --branch "$(git branch --show-current)" --status in_progress
gh run list --branch "$(git branch --show-current)" --status completed
```

**Key fields from `--json`:**
- `status`: `queued`, `in_progress`, `completed`
- `conclusion`: `success`, `failure`, `cancelled`, `skipped` (only set when `completed`)
- `databaseId`: numeric run ID used by other commands

## Watching Runs

```bash
# Block until a specific run completes, showing live progress
gh run watch <run_id>

# Watch with exit code matching run result (useful for scripting)
gh run watch <run_id> --exit-status
```

`gh run watch` streams progress to the terminal and exits when the run finishes. The `--exit-status` flag makes it return a non-zero exit code if the run fails.

## Viewing Run Details

```bash
# Summary of a run (jobs, steps, durations)
gh run view <run_id>

# Full log output for failed steps only
gh run view <run_id> --log-failed

# Full log output for all steps
gh run view <run_id> --log

# JSON output for specific fields
gh run view <run_id> --json jobs,conclusion,status
```

**`--log-failed` is the most useful for diagnosis** — it shows only the output from steps that failed, cutting through noise.

## Rerunning

```bash
# Rerun all jobs in a failed run
gh run rerun <run_id>

# Rerun only the failed jobs
gh run rerun <run_id> --failed
```

## Common Failure Patterns

**Test failures:**
- Look for assertion errors, stack traces, exit codes in `--log-failed` output
- Search for `FAIL`, `Error`, `AssertionError`, `expected` in the logs
- Identify the specific test file and test name from the output

**Build failures:**
- TypeScript: look for `TS\d+` error codes
- Lint: look for rule names (e.g., `no-unused-vars`)
- Missing dependencies: `Module not found`, `Cannot find module`

**Environment/infrastructure:**
- Timeouts: often indicate flaky tests or resource issues
- Permission denied: check secrets and token configuration
- Rate limits: GitHub API rate limiting on heavy usage

## Checking if Runs Exist

Before monitoring, verify there are runs for the current branch:

```bash
runs=$(gh run list --branch "$(git branch --show-current)" --limit 1 --json databaseId --jq 'length')
if [ "$runs" -eq 0 ]; then
  echo "No GitHub Actions runs found for this branch"
fi
```

## Waiting for Pending Runs

After a push, runs may take a moment to appear. Poll until runs are available:

```bash
branch=$(git branch --show-current)
for i in $(seq 1 12); do
  runs=$(gh run list --branch "$branch" --limit 5 --json databaseId,status,headSha --jq "[.[] | select(.headSha == \"$(git rev-parse HEAD)\")] | length")
  [ "$runs" -gt 0 ] && break
  sleep 5
done
```
