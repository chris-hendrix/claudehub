---
name: implementing
description: This skill should be used when the user wants to "implement this", "execute a plan", "work on a ticket or issue", "build from a description", mentions implementation execution, or is working on implementing from plans, tickets or issues, or descriptions.
version: 1.0.0
allowed-tools: Read, Write, Bash, Edit, AskUserQuestion, Glob, Task, Grep, TodoWrite
---

# Implementing

Execute implementation from plans, tickets or issues, or descriptions with mandatory review checkpoints.

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

## Phase Confirmation

After confidence assessment, present the phases to the user:
- List each phase with a brief description
- Highlight dependencies between phases
- Note estimated scope/complexity per phase

Wait for explicit user confirmation before creating todos and beginning implementation. This allows the user to:
- Reorder phases if needed
- Split or combine phases
- Adjust scope before work begins

## Execution Model

### Phase Processing

Plans are organized into phases with success criteria. Execute phases sequentially:
1. Load phase tasks into TodoWrite
2. Implement all changes in the phase
3. Run automated verification (from phase success criteria)
4. Present results and get user confirmation
5. Proceed to next phase only after sign-off

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

When implementation diverges from the plan:

### BLOCKED Status Protocol

When tasks cannot proceed as planned, never auto-approve deviations. Present options:
1. Approve the deviation with justification
2. Revise the plan to address the issue
3. Enforce adherence to original plan
4. Investigate further before deciding

### Plan Updates

If the plan needs modification during execution:
- Document the deviation and reasoning
- Get explicit user approval
- Update the plan file if changes are significant

## Phase Verification

After completing each phase, run success criteria from the plan:

### Automated Verification
- Tests, linting, type checks as specified
- Build verification if applicable
- All automated checks must pass before proceeding

### Manual Verification
- Present manual verification steps to user
- Wait for explicit confirmation
- Do not proceed to next phase without sign-off

## Completion

When all phases complete:
- Run full verification suite
- Write implementation summary to `.thoughts/implementations/YYYY-MM-DD-[ticket-or-issue-id-]<topic>.md`
- Present remaining manual verification steps

### Summary Document

Follow `writing-documentation` skill for frontmatter. The summary should capture:
- What was implemented (high-level)
- Any deviations from original plan with reasoning
- Verification results
- Link to original plan file
