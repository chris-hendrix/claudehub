# Brainstorm Document Template

Save brainstorms to `.thoughts/brainstorms/YYYY-MM-DD-<topic>.md` with this structure:

```markdown
---
date: YYYY-MM-DD
topic: Brief topic description
---

# [Topic Title]

## Context

[Brief overview - why are we doing this? Business motivation, user feedback, strategic initiative, constraints]

## Objective

[What are we trying to achieve? This could be solving a problem, adding a feature, making a strategic decision, etc.]

## Success Criteria

What does success look like? How will we know this works?

- Criterion 1
- Criterion 2
- Criterion 3

## What Exists

**Relevant Files:**
- `path/to/file1.ts:123` - Description of what this file/function does
- `path/to/file2.ts:45` - Related pattern or component

**Current Patterns:**
- [Description of existing architectural patterns]
- [Current approaches to similar problems]

**External Dependencies:**
- Library/API name - [Link to docs](url) - What it's used for

## Approaches Considered

### Approach 1: [Name] (Recommended)

**Description:** [What this approach does]

**Pros:**
- Advantage 1
- Advantage 2

**Cons:**
- Limitation 1
- Limitation 2

**Trade-offs:** [Key considerations and why these matter]

### Approach 2: [Name]

[Similar structure]

### Approach 3: [Name] (if applicable)

[Similar structure]

## Decision

**Selected Approach:** [Name of chosen approach]

**Rationale:** [Why this approach was chosen over the others]
```
