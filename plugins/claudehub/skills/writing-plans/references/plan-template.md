# Plan Template

```markdown
# [Feature/Task Name] Implementation Plan

## Overview

[Brief description of what we're implementing and why]

## Current State Analysis

[What exists now, what's missing, key constraints discovered]

### Key Discoveries:
- [Important finding with file:line reference]
- [Pattern to follow]
- [Constraint to work within]

## Desired End State

[Specification of the desired end state and how to verify it]

## What We're NOT Doing

[Explicitly list out-of-scope items to prevent scope creep]

## Implementation Approach

[High-level strategy and reasoning]

## Phase 1: [Descriptive Name]

### Overview
[What this phase accomplishes]

### Changes Required:

#### 1. [Component/File Group]
**File**: `path/to/file.ext`
**Changes**: [Summary of changes]

[Code snippet if helpful]

### Success Criteria:

#### Automated Verification:
- [ ] Tests pass: [test command discovered during research]
- [ ] Type checking passes: [if applicable]
- [ ] Linting passes: [lint command]

#### Manual Verification:
- [ ] Feature works as expected
- [ ] No regressions in related features

---

## Phase 2: [Descriptive Name]

[Similar structure...]

---

## Testing Strategy

### Unit Tests:
- [What to test]
- [Key edge cases]

### Integration Tests:
- [End-to-end scenarios]

### Manual Testing:
1. [Specific step to verify]
2. [Edge case to test]

## References

- Original ticket or issue: [link or path]
- Related research: [links]
- Similar implementation: [file:line]
```

## Success Criteria Guidelines

Always separate into two categories:

### Automated Verification
Commands that can be run without human intervention. Discover these during research by:
- Checking `Makefile`, `package.json`, `pyproject.toml`, etc.
- Looking at existing test patterns in the codebase
- Finding CI/CD configuration files

Types of automated checks:
- Test commands
- Linting
- Type checking
- Build verification

### Manual Verification
Requires human testing:
- UI/UX functionality
- Performance under real conditions
- Edge cases hard to automate
- User acceptance criteria
