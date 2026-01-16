# Branch Naming Conventions

Guidelines for naming git branches to maintain clarity and consistency.

## Context for Branch Names

Branch names can be derived from multiple sources:

**Issue/ticket numbers:**
- Check if the user provided an issue number or references a GitHub issue
- Use `gh issue view <number>` to fetch issue details
- Extract the issue type and description

**Uncommitted or staged changes:**
- Run `git status` to see modified files
- Run `git diff` for staged changes or `git diff HEAD` for all changes
- Analyze the changes to infer the type (feature, fix, refactor, etc.) and description

**User input:**
- Direct description from the user about what they're working on
- Clarify with the user if the context is unclear

## Standard Format

```
<type>/<description>
```

**Type prefixes:**
- `feature/` - New features or enhancements
- `fix/` - Bug fixes
- `refactor/` - Code refactoring without changing behavior
- `docs/` - Documentation changes
- `test/` - Adding or updating tests
- `chore/` - Maintenance tasks, dependencies, tooling

**Description:**
- Use lowercase with hyphens
- Keep it concise but descriptive (2-5 words)
- Describe what, not how

## Examples

**Good:**
```
feature/user-authentication
fix/checkout-race-condition
refactor/simplify-api-client
docs/update-readme
test/add-integration-tests
chore/update-dependencies
```

**Bad:**
```
my-branch                    # No type prefix
feature/updateTheUserAuth    # camelCase instead of kebab-case
fix/bug                      # Too vague
feature/add-new-feature-for-user-authentication-with-oauth  # Too long
johns-work                   # Doesn't describe the change
```

## Short-Lived Branches

Branch names should reflect temporary work:
- Merge frequently (aim for 1-3 days)
- Delete after squash merge
- Don't overthink naming for quick fixes

## Optional: Ticket or Issue References

If using issue tracking, you can include ticket or issue numbers:
```
feature/123-user-authentication
fix/456-checkout-race-condition
```

Format: `<type>/<ticket-or-issue>-<description>`

## Main Branch

- Primary branch: `main` (or `master` in older repos)
- Protected and long-lived
- All feature branches merge here via squash merge

## Common Commands

**Creating and switching branches:**
```bash
# Create and switch to new branch
git checkout -b feature/feature-name

# Switch to existing branch
git checkout branch-name

# Create branch without switching
git branch feature/feature-name
```

**Pushing branches:**
```bash
# Push and set upstream
git push -u origin feature/feature-name

# Push to existing upstream
git push
```

**Deleting branches:**
```bash
# Delete local branch (after merge)
git branch -d feature/feature-name

# Force delete local branch
git branch -D feature/feature-name

# Delete remote branch
git push origin --delete feature/feature-name
```

**Listing branches:**
```bash
# List local branches
git branch

# List all branches (local and remote)
git branch -a

# List remote branches
git branch -r
```

**Cleaning up dead branches:**
```bash
# Update remote tracking info and remove stale remote references
git fetch --prune

# List all local branches with their remote tracking status
git branch -vv

# Identify branches marked with [gone] - these have been deleted on the remote (likely merged)
# Delete them using:
git branch -D branch-name
```
