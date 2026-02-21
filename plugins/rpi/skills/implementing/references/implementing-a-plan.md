# Implementing from a Plan

Treat the plan as a living document that tracks both progress and deviations during implementation.

**CRITICAL: You must actively update the plan file as you work.** This is not optional - it's how work resumes across multiple LLM sessions.

## What to Update in the Plan File

### 1. Check off completed items

Replace `- [ ]` with `- [x]` in the plan file at each level as you complete them:

**As you work through tasks:**
- **Steps** - Check as you complete each individual action
- **Checks** - Check after running verification commands and they pass
- **Tasks** - Check when all steps and checks in the task are complete

This provides real-time visibility into progress and enables tight feedback loops.

### 2. Update frontmatter status

Edit the plan file's frontmatter as work progresses:
- `status: planned` → `status: in-progress` (when starting first task)
- `status: in-progress` → `status: completed` (when all tasks done)

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

## Resuming Work Across Sessions

When opening a plan file to continue work:

1. **Read the plan** - Architecture section provides all context needed
2. **Check progress** - Unchecked items show what remains
3. **Find starting point** - First unchecked task
4. **Load into TodoWrite** - Add upcoming tasks
5. **Continue implementation** - No prior session context needed

## Plan vs TodoWrite

Use both tools in parallel:

| Tool | Purpose | Persistence |
|------|---------|-------------|
| **Plan file** | Long-term record with full context | Persists across sessions |
| **TodoWrite** | Active work tracking for current session | Ephemeral, session-specific |

**Workflow:**
1. Load upcoming tasks into TodoWrite
2. Mark items complete in **both** TodoWrite and the plan file
3. Work through tasks sequentially

## Task Verification

Each task has inline checks for verification:

### Running Checks
1. Complete all steps in the task
2. Run verification commands specified in checks
3. All checks must pass before marking task complete
4. Check off check items in the plan file

### If Checks Fail
1. Debug and fix the issue
2. Re-run checks until they pass
3. Only then mark the task complete

### Natural Stopping Points
After completing several tasks, assess context usage:
- If context is getting large (many files read, long conversation): **Recommend stopping** and resuming in a fresh session with `/implement path/to/plan.md`
- If context is still manageable: Continue with next tasks
- Plan file shows all progress; next session picks up seamlessly

## Completion & Summary Document

When all tasks complete:

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
