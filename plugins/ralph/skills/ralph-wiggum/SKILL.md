---
description: This skill should be used when executing engineering tasks using the Ralph workflow methodology. Applies to task execution with researcher, coder, verifier, and reviewer agents in sequence.
---

# Ralph Engineering Workflow

The Ralph engineering workflow executes tasks through a structured agent pipeline. Each task follows the same sequence: research, code, verify, review.

## Task Execution Flow

For each task from TASKS.md:

1. **Find task** - Locate first unchecked `- [ ]` item
2. **Research** - Use `researcher` agent to gather context
3. **Code** - Use `coder` agent to implement + write tests
4. **Verify** - Use `verifier` agent to run all checks
5. **Review** - Use `reviewer` agent to assess quality
6. **Complete** - Mark `[x]` in TASKS.md, append to PROGRESS.md

### Cleanup Phase

A dedicated Cleanup phase runs after all feature phases and before Final Verification. It contains a single triage task that reads ALL of PROGRESS.md, identifies every unaddressed item (failures, blocks, reviewer caveats, deferred work), and creates individual fix tasks in TASKS.md. Each fix task goes through the full agent sequence (researcher → coder → verifier → reviewer). One triage pass only — remaining issues are caught by Final Verification. See `references/context-files.md` for format and examples.

## Agent Sequence

```
researcher → coder → verifier → reviewer
```

Each agent receives context from the previous. The session orchestrates the handoff.

## File Locations

All Ralph files live in `.ralph/`:

| File | Purpose |
|------|---------|
| `ARCHITECTURE.md` | Technical approach (services, schema, APIs, components) |
| `TASKS.md` | Tasks with checkboxes at task level (`- [ ] Task 1.1:`), NOT on steps |
| `VERIFICATION.md` | How to verify (test commands, env setup, feature flags) |
| `PROGRESS.md` | Learnings and results from each iteration |
| `screenshots/` | Visual proof from manual testing (tracked) |
| `logs/` | Flat session logs: `{timestamp}-{branch}-{task}.jsonl` (gitignored) |

For context file formats (loaded each iteration), see `references/context-files.md`.

## Task Granularity

When creating TASKS.md (via `/ralph:plan-deep`), you'll be asked to choose task granularity:

| Granularity | Description | Best For |
|-------------|-------------|----------|
| **Small** | Smallest chunks of verifiable work. Each task is highly focused (e.g., "Create schema", "Add endpoints", "Write tests" as separate tasks) | Catching issues early, maintaining steady progress, clear milestones |
| **Medium** (Recommended) | Balanced task sizes. Each task covers a complete feature component (e.g., "Implement auth service with tests") | Good balance between granularity and task count |
| **Large** | Fewer, larger tasks. Each task covers significant functionality (e.g., "Implement complete authentication system") | Less overhead, fewer tasks to track |

**Medium granularity is recommended** because:
- Each task covers a complete feature component, reducing overhead
- Good balance between progress tracking and task count
- Fewer context switches between tasks
- Still granular enough to isolate issues and resume after interruptions

See `references/context-files.md` for concrete examples of the same feature at different granularities.

## Branch Naming

**Format:** `ralph/yyyymmdd-hhmm-short-description`

Examples:
- `ralph/20260126-1430-user-auth`
- `ralph/20260127-0915-payment-flow`

```bash
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
git checkout $DEFAULT_BRANCH && git pull
git checkout -b ralph/$(date +%Y%m%d-%H%M)-short-description
```

## Tracking Progress Remotely

Generate a compare URL to view all commits made during a Ralph run. Display this URL whenever showing status or confirming execution start.

```bash
REPO_URL=$(git remote get-url origin | sed 's/\.git$//' | sed 's/git@github.com:/https:\/\/github.com\//')
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "${REPO_URL}/compare/${DEFAULT_BRANCH}...${CURRENT_BRANCH}"
```

Example: `https://github.com/org/repo/compare/main...ralph/20260128-1123-feature`

## Task Completion Criteria

A task is complete ONLY when BOTH conditions are met:
1. Verifier reports all checks **PASS**
2. Reviewer assessment is **APPROVED**

**NEEDS_WORK is NOT complete.** Implement all reviewer feedback immediately and re-verify until APPROVED.

**Test failures are NOT complete.** Fix all failures immediately and re-verify until passing.

Only BLOCKED (fundamental architectural issues) defers to next iteration.

## Session Instructions

When spawned by the Ralph orchestrator:

1. Read `.ralph/TASKS.md` and find first `- [ ]` task
2. Read `.ralph/ARCHITECTURE.md` for context
3. Read `.ralph/VERIFICATION.md` for check commands
4. Read last 50 lines of `.ralph/PROGRESS.md` for learnings
5. Execute agent sequence: researcher → coder → verifier → reviewer
6. If all checks pass and review APPROVED:
   - Mark task `[x]` in TASKS.md
   - Append iteration report to PROGRESS.md
7. If checks fail: fix NOW and re-verify until passing
8. If review returns NEEDS_WORK: implement ALL feedback NOW and re-verify until APPROVED
9. If review returns BLOCKED: keep task `[ ]`, append details to PROGRESS.md

## Commit Modes

| Mode | Behavior |
|------|----------|
| `no-commit` | Leave changes uncommitted |
| `commit` | Commit on success |
| `commit-push` | Commit and push on success (default) |

Commit message format: `"Ralph: Task X.Y - [task name]"`

## Testing Types — The Agent Does ALL of Them

**There is no human in the loop.** Every check in VERIFICATION.md — automated or manual — is performed by the agent. If the environment isn't ready, the agent sets it up. If a service isn't running, the agent starts it.

| Type | Purpose | Agent Action |
|------|---------|--------------|
| Unit tests | Test isolated functions | Run test commands |
| Integration tests | Test components together | Start services (Docker, DB) if needed, then run tests |
| E2E tests (automated) | Scripted regression tests | Start the app, run E2E suite |
| Manual testing (FE) | Visual/UX verification | Open browser with Playwright (installed locally), navigate, interact, screenshot |
| Manual testing (BE) | API endpoint verification | Curl endpoints, verify responses, test error cases |
| Linting | Code style/errors | Run linter |
| Type checking | Static type verification | Run type checker |
| Feature flags | Gate feature availability | Enable flags locally, mock if needed |

For detailed guidance on each testing type, see `references/testing-types.md`. For Playwright installation and usage, see `references/playwright.md`.

**E2E tests ≠ Manual testing.** E2E tests prove code runs; manual testing proves it looks/works right. When E2E is required, manual browser testing with screenshots is also required.

## Screenshots

During manual testing with Playwright, capture screenshots as visual proof:

**Location:** `.ralph/screenshots/` (tracked in git)

**Naming:** `iteration-{NNN}-{description}.png`

**When to capture:** Key states, before/after actions, error states, final success.

## Environment Validation

Before starting Ralph execution, validate AND fix the environment so all verification steps can run:

1. Parse VERIFICATION.md for test commands
2. For each test suite, run ONE existing test to verify runner works. **If it doesn't, install dependencies / fix config until it does.**
3. For URLs/endpoints listed, verify they're reachable. **If they're not, start the services yourself.**
4. If manual verification requires browser, check Playwright is installed. **If not, install it** (see `references/playwright.md`).
5. If feature flags mentioned, verify required flags are enabled locally. **If not, enable or mock them.**
6. Report what works, what was fixed, and what's still broken

The goal is a working environment, not just a report. Fix problems, don't just list them.

Use the `ralph-validator` agent to perform this check.
