---
description: Create ARCHITECTURE.md, TASKS.md, and VERIFICATION.md for Ralph execution
argument-hint: "[PRD path] [--designs PATH]"
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Glob", "AskUserQuestion", "WebFetch", "WebSearch", "Task"]
references-skills: claudehub:ralph-wiggum
---

# Ralph Plan Deep

Interactively create the three planning documents required for Ralph execution:
- `.ralph/ARCHITECTURE.md`
- `.ralph/TASKS.md`
- `.ralph/VERIFICATION.md`

**Requires 90% confidence before writing docs.** See `claudehub:ralph-wiggum/references/deep-dive.md` for questioning framework.

## Process

1. **Load the `claudehub:ralph-wiggum` skill** using the Skill tool

2. **Create new Ralph branch** (always create fresh, never checkout existing):

   Ask user for a short description (2-4 words, kebab-case) for the feature.

   ```bash
   DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
   git checkout $DEFAULT_BRANCH && git pull
   git checkout -b ralph/$(date +%Y%m%d-%H%M)-<description>
   ```

3. **Create `.ralph/` directory** if it doesn't exist

4. **Gather inputs**:
   - Parse `$ARGUMENTS` for PRD path
   - If PRD path not provided, ask user using AskUserQuestion
   - Ask about design specs location (Figma links, design docs)

5. **Read inputs**:
   - Read the PRD document
   - Note ACs (Acceptance Criteria) and FRs (Functional Requirements)
   - Gather design information if provided

6. **Deep-dive questioning** (REQUIRED - iterate until 90% confidence):

   Follow the questioning framework in `claudehub:ralph-wiggum/references/deep-dive.md`. Cover all categories:
   - Requirements clarity
   - Technical decisions
   - Scope boundaries
   - Feature flags & third-party setup
   - Testing & verification

   After each round: "Current confidence: X%. [Gaps if below 90%]"

7. **Create ARCHITECTURE.md** (only after 90% confidence):

   Follow the format in `claudehub:ralph-wiggum/references/context-files.md`.
   Research codebase as needed to understand existing patterns.

8. **Ask user about task granularity** using AskUserQuestion:

   Question: "What level of task granularity do you prefer for TASKS.md?"

   Options:
   - **Small (Recommended)**: Smallest chunks of verifiable work. Each task is highly focused and can be completed quickly. More tasks overall, but each task has clear, minimal scope. Best for catching issues early and maintaining steady progress.
   - **Medium**: Balanced task sizes. Each task covers a logical feature component with reasonable scope. Good middle ground between granularity and task count.
   - **Large**: Fewer, larger tasks. Each task covers significant functionality. Fewer tasks to track, but each takes longer to complete and verify. Best when you want less overhead.

   Store the user's choice and use it when breaking down work in the next step.

9. **Create TASKS.md**:

   Follow the format in `claudehub:ralph-wiggum/references/context-files.md`.

   **CRITICAL FORMAT REQUIREMENTS:**
   - Checkboxes ONLY on task lines: `- [ ] Task 1.1: Description`
   - Steps are indented bullets WITHOUT checkboxes: `  - Implement: Details`
   - Tasks are list items, NEVER headings (never use `### 1.1`)

   **Task Granularity Guidelines:**
   - **Small**: Each task should be completable in 1 iteration. Break features into smallest verifiable units (e.g., "Create user schema", "Add user endpoints", "Write user tests" as separate tasks)
   - **Medium**: Each task should cover a complete feature component (e.g., "Implement user authentication service with tests")
   - **Large**: Each task should cover a major feature area (e.g., "Implement complete authentication system with all endpoints and tests")

   Pay attention to TDD philosophy - tests go WITH implementation tasks.

   Ask user to confirm task breakdown before writing.

10. **Create VERIFICATION.md**:

    Scan repo for infrastructure (Dockerfile, docker-compose, package.json). Ask user about:
    - How to run locally, environment variables, test credentials
    - Feature flags to enable, third-party service setup

    Include all discovered ports, URLs, and feature flag requirements.

11. **Validate environment** (optional):

    Ask user if they want to validate the environment now.

    If yes, spawn the `ralph-validator` agent to verify test infrastructure works.

12. **Summary**:
    - List created files and task count
    - Show environment validation results
    - State final confidence level
    - Instruct user to run `/claudehub:ralph/run`

## Arguments

- First argument: Path to PRD document
- `--designs PATH`: Path to design specs or Figma links

## Example

```
/claudehub:ralph/plan-deep docs/prd-user-auth.md --designs docs/designs/
```

Input: $ARGUMENTS
