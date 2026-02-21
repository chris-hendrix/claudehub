---
description: Create Ralph planning docs quickly with autonomous design decisions
argument-hint: "<description>"
allowed-tools: ["Bash", "Read", "Write", "Edit", "Grep", "Glob", "AskUserQuestion", "EnterWorktree"]
references-skills: ralph:ralph-wiggum
---

# Ralph Plan

Create Ralph planning docs (ARCHITECTURE.md, TASKS.md, VERIFICATION.md) quickly by making autonomous design decisions.

See `ralph:ralph-wiggum/references/context-files.md` for detailed format specs.

## Process

1. **Load the `ralph:ralph-wiggum` skill** using the Skill tool
2. **Parse description** from `$ARGUMENTS` (first non-flag argument)
   * If no description provided, tell user to provide one and stop
3. **Ask isolation mode** using AskUserQuestion:
   - Question: "How would you like to isolate this work?"
   - Header: "Isolation"
   - Options:
     - "Branch (Recommended)" — Ralph creates a `ralph/` branch when you run `/ralph:run`
     - "Worktree" — Creates an isolated worktree now with its own branch
4. **Handle isolation + write CONFIG.md:**
   - If worktree: call `EnterWorktree` with name `ralph-<short-description>`
   - Create `.ralph/` directory
   - Write `.ralph/CONFIG.md`:
     ```markdown
     # Ralph Config

     - description: <short-description-from-arguments>
     - mode: <worktree|branch>
     ```
5. **Quick codebase scan** - understand the project structure:
   * Check package.json, Cargo.toml, go.mod, etc. for project type
   * Identify test framework and commands
   * Find existing patterns to follow
6. **Write ARCHITECTURE.md** with a "Design Decisions" section:
   ```markdown
   # Architecture

   ## Overview
   [1-2 sentences about what we're building]

   ## Design Decisions

   These decisions were made autonomously by ralph-plan. Review and adjust if needed.

   | Decision | Choice | Rationale |
   |----------|--------|-----------|
   | [area] | [choice] | [why] |
   ...

   ## Technical Approach
   [Details based on codebase patterns]
   ```
7. **Spawn two agents in parallel:**

   a. **Write TASKS.md**
      - Follow format in `ralph:ralph-wiggum/references/context-files.md`
      - **CRITICAL:** Checkboxes ONLY on task lines (`- [ ] Task 1.1:`), NEVER on step lines
      - **CRITICAL:** Tasks are list items, NOT headings (never use `### 1.1`)
      - Include tests WITH implementation tasks (TDD)
      - Add Final Verification phase

   b. **Write VERIFICATION.md**
      - Scan for test commands in package.json scripts, Makefile, etc.
      - Include discovered ports and URLs
      - Add manual testing steps for UI work

8. **Confirm completion**:
   > "Planning docs created with X design decisions - review `.ralph/ARCHITECTURE.md` if needed.
   > Run `/ralph:run` to start execution."

## Design Decisions Section

Document every autonomous decision:

* **Component location** - where new files go
* **Naming conventions** - following existing patterns
* **State management** - approach for frontend
* **API design** - REST vs GraphQL, endpoint structure
* **Testing strategy** - unit vs integration vs E2E balance
* **Error handling** - approach and patterns
* **Dependencies** - new packages to add (if any)

This transparency lets users review and adjust before execution.

## Examples

```bash
# Create planning docs for a feature
/ralph:plan "add user authentication with JWT"

# Then start Ralph execution
/ralph:run
```

Input: $ARGUMENTS
