---
name: writing-plans
description: This skill should be used when the user wants to "create a plan", "write an implementation plan", "plan a feature", "design a solution", "plan implementation", mentions "implementation plan", "technical plan", "architecture plan", or is working on creating detailed implementation plans for features or changes.
version: 1.0.0
allowed-tools: Write, Read, Bash, AskUserQuestion, Glob, Task, Grep, TodoWrite
---

# Writing Implementation Plans

Create detailed, actionable implementation plans.

**For file naming and frontmatter**: See the `writing-documentation` skill.

**Location**: Plans are always saved to `.thoughts/plans/`

## Philosophy

- **Be Skeptical**: Question vague requirements, identify issues early, verify with code
- **Be Interactive**: Don't write the full plan in one shot, get buy-in at each step
- **Be Thorough**: Research actual code, include file:line references, write measurable success criteria
- **Be Practical**: Focus on incremental changes, consider edge cases

## Key Planning Phases

Planning is interactive, not linear. These phases may overlap or repeat as understanding deepens.

### Context Gathering

Good plans require deep understanding. Read files fully rather than skimming. Ground all observations with `file:line` references.

### Resolving Ambiguity

Every plan has unstated assumptions. Surface them early by identifying:
- Edge cases and error handling expectations
- Integration points and dependencies
- Scope boundaries (what's explicitly out)
- Design preferences and constraints
- Backward compatibility concerns
- Performance requirements

Present questions clearly and wait for answers. If the user defers ("whatever you think"), state your recommendation explicitly and confirm.

### Architecture Trade-offs

Most problems have multiple valid solutions. Present 2-3 approaches with different trade-offs:

| Approach | Focus | Best When |
|----------|-------|-----------|
| **Minimal** | Smallest change, maximum reuse | Quick fixes, low risk |
| **Clean** | Maintainability, elegant abstractions | Long-term code health |
| **Pragmatic** | Balance of speed + quality | Most features |

Include your recommendation with reasoning. **Wait for explicit user confirmation before proceeding to write the plan.**

### Iterative Development

Don't write the full plan in one shot. Propose structure first, get feedback, then fill in details. Each iteration should incorporate user input.

## Important Rules

1. **No Open Questions in Final Plan**: Research or ask before writing. The plan must be complete and actionable.

2. **Verify Everything**: Don't accept corrections blindly - research to verify facts yourself.

3. **Phase-by-Phase Verification**: Each phase should have clear success criteria. Pause for manual verification between phases.

4. **Include What We're NOT Doing**: Explicitly define scope boundaries.

## References

- `references/plan-template.md` - Full plan template with success criteria guidelines
