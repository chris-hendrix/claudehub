# Implementing from a Plan

Treat the plan as a living document that tracks both progress and deviations during implementation.

**CRITICAL: You must actively update the plan file as you work.** This is not optional - it's how work resumes across multiple LLM sessions.

## What to Update in the Plan File

### 1. Check off completed items

Replace `- [ ]` with `- [x]` in the plan file at each level as you complete them:

**As you work through tasks:**
- **Steps** - Check as you complete each individual action
- **Tasks** - Check when all steps in the task are complete

**After phase completion:**
- **Checks (phase-level)** - Check after running tests and getting user sign-off
- **Phases** - Check when all tasks and checks in the phase are complete

This provides real-time visibility into progress at all levels.

### 2. Update frontmatter status

Edit the plan file's frontmatter as work progresses:
- `status: planned` → `status: in-progress` (when starting first phase)
- `status: in-progress` → `status: completed` (when all phases done)

### 3. Update Tracked Changes section

For significant deviations, add entries to the plan's Tracked Changes section (see "Handling Deviations" below)

## Handling Deviations

Deviations happen when the plan needs to change during implementation.

**When deviations occur:**
1. Present the proposed change and reasoning to the user
2. Get approval
3. Update the affected sections in the plan file
4. Add entry to the "Tracked Changes" section

**Record in Tracked Changes section:**
```markdown
## Tracked Changes

**2026-01-15** - Changed authentication approach from JWT to session-based auth. Original approach had issues with token refresh complexity. Updated Architecture and Phase 2 sections.

**2026-01-16** - Added caching layer (Redis) not in original plan. Performance testing showed N+1 query issues. Added new Phase 2.3 task for cache implementation.
```

**Common deviation types:**
- Better approach discovered during implementation
- Blockers or technical constraints found
- Scope adjustments requested by user
- Performance/security concerns identified
- Discovered existing pattern to follow

**What to record:**
- **Significant changes**: Architectural shifts, added/removed phases, major scope changes
- **Don't record**: Minor refactors, variable renames, small code style adjustments

## Phase Confirmation

After confidence assessment, present the phases to the user:
- List each phase with a brief description
- Highlight dependencies between phases
- Note estimated scope/complexity per phase
- If resuming work, identify which phase to start based on checkboxes

Wait for explicit user confirmation before creating todos and beginning implementation. This allows the user to:
- Reorder phases if needed
- Split or combine phases
- Adjust scope before work begins

## Resuming Work Across Sessions

When opening a plan file to continue work:

1. **Read the plan** - Architecture section provides all context needed
2. **Check progress** - Unchecked items show what remains
3. **Find starting point** - First unchecked phase or task
4. **Load into TodoWrite** - Add current phase tasks
5. **Continue implementation** - No prior session context needed

## Plan vs TodoWrite

Use both tools in parallel:

| Tool | Purpose | Persistence |
|------|---------|-------------|
| **Plan file** | Long-term record with full context | Persists across sessions |
| **TodoWrite** | Active work tracking for current session | Ephemeral, session-specific |

**Workflow:**
1. Load current phase tasks into TodoWrite
2. Mark items complete in **both** TodoWrite and the plan file
3. Move to next phase: clear TodoWrite, load new phase tasks

## Phase Verification

After completing all tasks in a phase, run phase-level checks:

### Automated Checks
1. Run tests, linting, type checks as specified in phase checks
2. Run build verification if applicable
3. All automated checks must pass before proceeding
4. Check off check items in the plan file

### Manual Checks
1. Present manual check steps to user
2. Wait for explicit confirmation
3. Check off check items in the plan file
4. Do not proceed to next phase without sign-off

### After All Checks Pass
1. Check off the phase checkbox in the plan file
2. **Present completion to user** - This is a natural stopping point
3. **Assess context usage and recommend accordingly:**
   - If context is getting large (many files read, long conversation): **Recommend stopping** and resuming in a fresh session with `/implement path/to/plan.md`
   - If context is still manageable: Ask if user wants to continue or stop
4. **If user chooses to continue:** Load next phase into TodoWrite and proceed
5. **If user stops:** Plan file shows all progress; next session picks up seamlessly

## Completion & Summary Document

When all phases complete:

1. Run full verification suite
2. Write implementation summary to `.thoughts/implementations/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`
3. Present remaining manual verification steps to user

### Summary Document Structure

Follow `writing-documentation` skill for frontmatter. Include:

**What was implemented:**
- Brief description of what was built

**Files created/modified:**
- List of key files changed

**Key design decisions:**
- Architectural choices made during implementation

**Implementation Notes:**
- Deviations from original plan (if plan was updated during implementation, note this here)
- Challenges encountered
- Approach refinements

**Verification results:**
- Test results, build status

**References:**
- Link to original plan file

**Example:**
```markdown
## Implementation Notes

The plan was updated during implementation. Key changes:
- Added caching layer for performance (see Tracked Changes 2026-01-16)
- Switched to session-based auth (see Tracked Changes 2026-01-15)

See the [original plan](.thoughts/plans/2026-01-15-user-auth.md) for complete tracked changes.
```
