# Confidence Assessment Template

Use this template before starting implementation to assess readiness.

## Template

```markdown
---
## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Task understanding | 🟢 High | [Clear requirements, unambiguous goal] |
| Existing code patterns | 🟡 Medium | [What's understood vs unclear] |
| Implementation approach | 🔴 Low | [Plan quality, actionability of steps] |

### Concerns:

- [List any specific concerns or blockers]
- [Information needed to increase confidence]

### Recommendation:

[Proceed / Investigate further / Revise plan first]
```

## Confidence Levels

| Indicator | Level | Meaning |
|-----------|-------|---------|
| 🟢 | **High** | Ready to proceed without concerns |
| 🟡 | **Medium** | Some uncertainty but manageable |
| 🔴 | **Low** | Significant gaps - must resolve first |

## Areas to Evaluate

### Task Understanding
- Is the goal clear and unambiguous?
- Are acceptance criteria well-defined?
- Are edge cases identified?

### Existing Code Patterns
- Have relevant files been reviewed?
- Are dependencies understood?
- Are existing patterns to follow identified?

### Implementation Approach
- Are steps actionable and specific?
- Are success criteria verifiable?
- Is the scope realistic?

## Example

```markdown
---
## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Task understanding | 🟢 High | Clear plan with detailed phases and acceptance criteria |
| Existing code patterns | 🟢 High | Reviewed BEST_PRACTICES.md and local plugin structure |
| Implementation approach | 🟢 High | Brainstorm has clear architecture, flow diagram, and examples |

### Concerns:

- None identified

### Recommendation:

Proceed with implementation
```

## Low Confidence Protocol

If any area is rated 🔴 **Low**:

1. Do NOT proceed with implementation
2. Suggest `/eng:brainstorm` to clarify requirements
3. Or suggest `/eng:create-plan` to develop a proper approach
4. Re-assess after addressing gaps
