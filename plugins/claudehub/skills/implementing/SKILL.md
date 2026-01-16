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

Execute phases sequentially:
1. Load phase tasks into TodoWrite
2. Implement changes, marking items complete in both TodoWrite and the plan file
3. Run automated verification (from phase success criteria)
4. Get user confirmation before proceeding to next phase

See [references/implementing-a-plan.md](references/implementing-a-plan.md) for plan tracking guidance.

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

Deviations can be initiated by you (blockers, better approaches) or the user (preference changes, scope adjustments).

### When You Discover Issues

If tasks cannot proceed as planned, present options:
1. Approve a deviation with justification
2. Revise the plan to address the issue
3. Enforce adherence to original plan
4. Investigate further before deciding

### When Plans Change

After approval of any deviation:
- Update the plan file to reflect the new approach
- Document when and why it was modified

See [references/implementing-a-plan.md](references/implementing-a-plan.md) for details.

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

Follow `writing-documentation` skill for frontmatter. Include:
- What was implemented
- Files created/modified
- Key design decisions
- **Implementation Notes**: Deviations, challenges, approach refinements (if plan was updated during implementation, note this here)
- Verification results
- Link to original plan file
