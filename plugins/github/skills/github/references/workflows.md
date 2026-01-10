# Workflow Strategy

Detailed workflow methodology for git and GitHub that emphasizes draft PRs, incremental commits, and clean merge history.

## Core Principles

**NEVER Commit to Default Branch:**
- **CRITICAL:** Never commit or push directly to main/master
- Always work on feature branches
- Default branch is protected - changes only via PR squash merge

**Draft PR-First Development:**
- Every push should create or update a draft PR
- Commits are not standalone - they belong to a draft PR context
- Draft PRs enable early feedback and visibility into work-in-progress

**Clean History via Squash Merge:**
- Always use squash and merge when merging PRs
- Individual commits within a PR branch are working commits
- The squashed commit becomes the canonical history entry

**Graphite-Style Workflow:**
- Work in small, focused PRs
- Stack PRs when working on dependent changes
- Keep branches short-lived and frequently merged

## Workflow Steps

### 1. Starting Work

When beginning a new task or feature:
```bash
# Create a feature branch (see branch naming conventions)
git checkout -b feature/feature-name

# Make initial commit
git add .
git commit -m "Initial work on feature"

# Push and create draft PR
git push -u origin feature-name
gh pr create --draft --title "Feature name" --body "Description"
```

### 2. Iterative Development

As you continue working:
```bash
# Make changes and commit frequently
git add .
git commit -m "Add initial structure"
git push

# The draft PR automatically updates
# No need to create new PRs for each push
```

### 3. Ready for Review

When work is complete:
```bash
# Mark PR as ready for review
gh pr ready

# Or via GitHub UI
```

### 4. Merging

Always use squash and merge:
```bash
# Via gh CLI
gh pr merge --squash --delete-branch

# Or via GitHub UI: select "Squash and merge"
```

## Draft PR Benefits

**Early Visibility:**
- Team sees work in progress
- Can provide early feedback
- Reduces surprises at review time

**Continuous Integration:**
- CI runs on every push
- Catch issues early
- No "works on my machine" at review time

**Documentation:**
- PR description captures the "why"
- Comments track decisions made during development
- History of iterations preserved in PR timeline

## Commit Message Style

Base commit messages on the diff. Describe what changed in a clear, concise way:
- "Add validation logic"
- "Fix linting errors"
- "Address review feedback"

Since commits will be squashed, individual messages should be simple and descriptive. The squash commit message (PR title + description) becomes the canonical history entry.

## When to Create New PRs

Create a new PR when:
- Starting a completely different task or feature
- The change is independent of current work
- Stacking PRs (dependent changes that build on each other)

Don't create new PRs for:
- Addressing review feedback (push to existing PR)
- Fixing CI failures (push to existing PR)
- Making requested changes (push to existing PR)
