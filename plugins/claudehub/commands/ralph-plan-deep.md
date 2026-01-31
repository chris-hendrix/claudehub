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

1. **Load the `ralph-wiggum` skill** using the Skill tool

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

8. **Create TASKS.md**:

   Follow the format in `claudehub:ralph-wiggum/references/context-files.md`. Pay attention to TDD philosophy - tests go WITH implementation tasks.

   Ask user to confirm task breakdown before writing.

9. **Create VERIFICATION.md**:

   Scan repo for infrastructure (Dockerfile, docker-compose, package.json). Ask user about:
   - How to run locally, environment variables, test credentials
   - Feature flags to enable, third-party service setup

   Include all discovered ports, URLs, and feature flag requirements.

10. **Validate environment** (optional):

    Ask user if they want to validate the environment now.

    If yes, spawn the `environment-validator` agent to verify test infrastructure works.

11. **Summary**:
    - List created files and task count
    - Show environment validation results
    - State final confidence level
    - Instruct user to run `/claudehub:ralph-run`

## Arguments

- First argument: Path to PRD document
- `--designs PATH`: Path to design specs or Figma links

## Example

```
/claudehub:ralph-plan-deep docs/prd-user-auth.md --designs docs/designs/
```

Input: $ARGUMENTS
