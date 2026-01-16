---
name: implementing
description: This skill should be used when the user wants to "implement this", "execute a plan", "work on a ticket or issue", "build from a description", mentions implementation execution, or is working on implementing from plans, tickets or issues, or descriptions.
version: 1.0.0
allowed-tools: Read, Write, Bash, Edit, AskUserQuestion, Glob, Task, Grep, TodoWrite
---

# Implementing

Execute implementation from plans, tickets or issues, or descriptions with mandatory review checkpoints.

**Multi-session implementation**: Large implementations span multiple sessions. The plan file is the source of truth - checkboxes show progress, and any session can resume where the previous one left off.

## Philosophy

- **Critical Review Before Starting**: Read plans skeptically. Assess confidence and raise concerns before executing.
- **Phase-by-Phase Execution**: Complete one phase fully before moving to the next.
- **Mandatory Review Checkpoints**: Run success criteria after each phase, get user sign-off.
- **Fail Fast**: Stop on blockers rather than proceeding speculatively.

## Confidence Assessment

Before starting execution, assess confidence in three areas:

| Area | What to evaluate |
|------|------------------|
| **Task** | Is the goal clear? Are requirements unambiguous? |
| **Existing Code** | Is the codebase understood? Are dependencies clear? |
| **Plan** | Are steps actionable? Are success criteria verifiable? |

Rate each as **Low**, **Medium**, or **High** with visual indicators:

- 🟢 **High**: Ready to proceed without concerns
- 🟡 **Medium**: Some uncertainty but manageable - explain what's unclear
- 🔴 **Low**: Significant gaps - must resolve before proceeding

Present all three ratings to the user. For any rating below High, explain:
- What specific concerns exist
- What information would increase confidence
- Whether to proceed, investigate further, or revise the plan

**Low confidence**: Recommend further planning or design exploration before proceeding with implementation.

See [references/confidence-assessment.md](references/confidence-assessment.md) for the detailed template and examples.

Do not begin implementation until user acknowledges the assessment.

## Phase Confirmation & Resuming Work

After confidence assessment, present phases and get user confirmation before starting. If resuming work from a previous session, identify where to start based on checkboxes.

See [references/implementing-a-plan.md](references/implementing-a-plan.md) for detailed instructions on phase confirmation and resuming work across sessions.

## Execution Model

**CRITICAL: Update the plan file continuously as you work.** The plan is a living document - check off items, record changes, update status. This enables resuming work across sessions.

### Phase Processing

Execute phases sequentially:

1. **Load phase**: Add phase tasks to TodoWrite
2. **Implement task by task**: Complete steps, update both TodoWrite and plan file
3. **Verify phase**: Run checks, get user sign-off
4. **Move to next phase**: Clear TodoWrite, load next phase

**See [references/implementing-a-plan.md](references/implementing-a-plan.md) for detailed instructions on:**
- What to check off in the plan file and when
- How to update Tracked Changes section
- How to update frontmatter status
- Handling deviations during implementation

### Agent Selection

Select agents based on semantic understanding of task requirements:
- Analyze what the task actually requires
- Match to agent capabilities and domain expertise
- Consider task complexity

### Stop Conditions

Halt execution immediately when encountering:
- Missing dependencies or prerequisites
- Test failures that indicate broken assumptions
- Unclear or contradictory instructions
- Blocked status from agents

## Handling Deviations

When tasks cannot proceed as planned or a better approach is discovered, present options to the user and get approval before deviating. Update the plan file's Tracked Changes section with significant deviations.

See [references/implementing-a-plan.md](references/implementing-a-plan.md) for detailed instructions and examples.

## Phase Verification & Completion

After completing each phase, run phase-level checks (automated tests, manual verification) and get user sign-off before proceeding. When all phases complete, write implementation summary to `.thoughts/implementations/`.

See [references/implementing-a-plan.md](references/implementing-a-plan.md) for detailed verification steps and summary document structure.
