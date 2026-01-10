# GitHub Issues

Guidelines for creating and managing GitHub Issues to track tasks, bugs, and features.

## Issue Template

Use the template in `.github/ISSUE_TEMPLATE/issue_template.md`. If it doesn't exist, ask the user if they want to create it using:

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/setup-templates.sh
```

## When to Create an Issue

**Good reasons:**
- Bug reports
- Feature requests
- Documentation improvements
- Technical debt tracking
- Discussion topics that need tracking

**Don't create issues for:**
- Simple typos (just fix them)
- Questions answered in docs (link to docs instead)
- Duplicate reports (search first, comment on existing)

## Issue Types

**Bug Report:**
- Describe the problem
- Include reproduction steps
- Show expected vs actual behavior
- Add system/environment details

**Feature Request:**
- Explain the use case
- Describe the desired outcome
- Suggest implementation (optional)

**Task/Chore:**
- Clear action item
- Context on why it's needed
- Definition of done

## Creating Issues

**Via gh CLI:**
```bash
# Create with title and body
gh issue create --title "Title" --body "Description"

# Create interactively
gh issue create

# Create with labels
gh issue create --title "Title" --label "bug,priority"

# Create and assign
gh issue create --title "Title" --assignee @me
```

**Via GitHub UI:**
- Navigate to repository → Issues → New Issue
- Fill out title and description
- Add labels, assignees, projects as needed

## Issue Title Format

Use clear, action-oriented titles:

```
Fix race condition in checkout flow
Add OAuth authentication
Update README installation steps
Investigate slow database queries
```

Optional: Use prefixes for clarity:
```
Bug: Unable to save user preferences
Feature: Add dark mode toggle
Docs: Clarify API authentication
Question: Best practice for error handling
```

## Issue Templates

### Bug Report Template

```markdown
## Description

Brief description of the bug.

## Steps to Reproduce

1. Go to...
2. Click on...
3. See error

## Expected Behavior

What should happen.

## Actual Behavior

What actually happens.

## Environment

- OS: [e.g., macOS 13.0]
- Browser: [e.g., Chrome 120]
- Version: [e.g., 1.2.3]

## Screenshots

If applicable, add screenshots.

## Additional Context

Any other relevant information.
```

### Feature Request Template

```markdown
## Problem

Describe the problem or need this feature addresses.

## Proposed Solution

Describe the feature you'd like to see.

## Alternatives Considered

Any alternative solutions or features you've considered.

## Additional Context

Any other context, screenshots, or examples.
```

### Task/Chore Template

```markdown
## Task

Clear description of what needs to be done.

## Context

Why this is needed and any relevant background.

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Notes

Any additional information or considerations.
```

## GitHub Issue Template Files

Create issue templates in `.github/ISSUE_TEMPLATE/` directory:

**Bug report:** `.github/ISSUE_TEMPLATE/bug_report.md`
```yaml
---
name: Bug Report
about: Report a bug or unexpected behavior
title: ''
labels: bug
assignees: ''
---

## Description
[Brief description]

## Steps to Reproduce
1.
2.
3.

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS:
- Browser:
- Version:
```

**Feature request:** `.github/ISSUE_TEMPLATE/feature_request.md`
```yaml
---
name: Feature Request
about: Suggest a new feature
title: ''
labels: enhancement
assignees: ''
---

## Problem
[Describe the problem]

## Proposed Solution
[Describe the feature]

## Alternatives Considered
[Other solutions considered]
```

## Managing Issues

**List issues:**
```bash
gh issue list
gh issue list --label "bug"
gh issue list --assignee @me
gh issue list --state all
```

**View issue:**
```bash
gh issue view 123
gh issue view 123 --web  # Open in browser
```

**Edit issue:**
```bash
gh issue edit 123 --title "New title"
gh issue edit 123 --add-label "priority"
gh issue edit 123 --add-assignee username
```

**Close issue:**
```bash
gh issue close 123
gh issue close 123 --comment "Fixed in #456"
```

**Reopen issue:**
```bash
gh issue reopen 123
```

## Labels

Common label categories:

**Type:**
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Documentation improvements
- `question` - Further information requested

**Priority:**
- `critical` - Urgent, blocking issue
- `high` - Important, should be addressed soon
- `low` - Nice to have

**Status:**
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `wontfix` - This will not be worked on
- `duplicate` - Duplicate of another issue

## Linking Issues to PRs

Reference issues in PR descriptions to automatically link them:

```markdown
Closes #123
Fixes #456
Resolves #789
Related to #101
```

When the PR is merged, issues with `Closes`, `Fixes`, or `Resolves` will automatically close.

## Best Practices

**Be specific:**
- Clear, descriptive titles
- Detailed descriptions
- Include reproduction steps for bugs

**Be respectful:**
- Assume good intent
- Provide constructive feedback
- Stay on topic

**Be helpful:**
- Search before creating duplicates
- Provide context and examples
- Update issues with new information

**Follow up:**
- Respond to questions
- Test proposed fixes
- Close when resolved
