# Pull Request Strategy

Guidelines for creating effective pull requests that facilitate review and maintain project quality.

## Context for Describing PRs

When generating PR descriptions, **always** check for and follow the repo's PR template first:

**PR Template (check first):**
- Read template from `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` or `.github/pull_request_template.md`
- If template exists, follow its exact structure and sections
- If template doesn't exist, use standard format below

**Context sources for PR content:**
- Branch diff: Use `git diff <base-branch>...HEAD` to see all changes since branch divergence
- Commit history: Use `git log <base-branch>..HEAD` to see commit messages
- Linked issues: Check branch name for issue numbers (e.g., `feature/123-add-auth`)
- Existing PR media: Fetch current PR body with `gh pr view --json body -q .body` to preserve images/videos

## PR Lifecycle

**Draft → Ready → Review → Squash Merge**

1. **Draft PR** - Created on first push, work in progress
2. **Ready for Review** - Mark ready when complete
3. **Review** - Team reviews and provides feedback
4. **Squash Merge** - Merge with squashed commits, delete branch

## Good PR Characteristics

**Small and Focused:**
- Single responsibility - one feature, fix, or refactor
- Easy to review in 15-30 minutes
- Minimal lines changed (aim for <500 lines)

**Well Documented:**
- Clear title describing the change
- Description explains the "why" not just the "what"
- Screenshots/videos for UI changes
- Test plan included

**Self-Contained:**
- Can be merged independently
- All tests pass
- No unrelated changes mixed in

## PR Title Format

Use clear, action-oriented titles:

```
Add user authentication with OAuth
Fix race condition in checkout flow
Refactor API client to use axios
Update README with installation steps
```

## PR Template

Use the template in `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`. If it doesn't exist, ask the user if they want to create it using:

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/setup-templates.sh
```

## Draft PR Guidelines

**When to use draft PRs:**
- Work in progress
- Need early feedback on approach
- Want to run CI before requesting review
- Exploring a solution

**Draft PR checklist before marking ready:**
- [ ] All intended changes complete
- [ ] Tests added and passing
- [ ] Code self-reviewed
- [ ] Documentation updated if needed
- [ ] PR description filled out

## Linking Issues

Use GitHub keywords to automatically close issues:
- `Closes #123`
- `Fixes #123`
- `Resolves #123`

Use for reference without closing:
- `Related to #123`
- `Part of #123`
- `See #123`

## Squash Merge Details

When squashing:
- All commits in the PR become one commit
- Squash commit message defaults to PR title + description
- Edit the squash commit message to be meaningful
- Original PR commits preserved in PR history

**Good squash commit messages:**
```
Add user authentication

Implements OAuth 2.0 authentication flow with GitHub and Google
providers. Includes login, logout, and session management.
```

**Bad squash commit messages:**
```
Merge pull request #123 from user/branch-name

[All the individual commit messages concatenated]
```

## Common Commands

**Creating PRs:**
```bash
# Create draft PR
gh pr create --draft --title "Title" --body "Description"

# Create draft PR interactively
gh pr create --draft

# Create ready PR
gh pr create --title "Title" --body "Description"

# Create with labels and assignees
gh pr create --draft --label "feature" --assignee @me
```

**Managing PRs:**
```bash
# View PR for current branch
gh pr view
gh pr view --web  # Open in browser

# View specific PR
gh pr view 123

# Get PR number for current branch
gh pr view --json number -q .number

# Mark draft as ready for review
gh pr ready

# List PRs
gh pr list
gh pr list --author @me
gh pr list --state all

# Check PR status
gh pr status
```

**Merging PRs:**
```bash
# Merge with squash (recommended)
gh pr merge --squash --delete-branch

# Merge with options
gh pr merge 123 --squash --delete-branch

# Merge interactively
gh pr merge
```

**Editing PRs:**
```bash
# Edit title and body
gh pr edit 123 --title "New title"
gh pr edit 123 --body "New description"

# Add labels
gh pr edit 123 --add-label "priority"

# Add reviewers
gh pr edit 123 --add-reviewer username
```

**IMPORTANT: Preserving Media When Updating PRs**

When updating a PR description using `gh pr edit --body`, you will replace the entire body content. This means any images, videos, or other media embedded in the PR will be lost unless you preserve them.

**Before updating:**
1. Fetch the current PR body to check for media:
   ```bash
   gh pr view 123 --json body -q .body
   ```
2. Look for image references (e.g., `![alt](url)`) or video embeds
3. Copy any media URLs or markdown that should be preserved

**When updating:**
- Include existing media in your new body content
- Preserve image markdown: `![description](url)`
- Preserve video links or embeds
- Keep any other important visual content

**Example:**
```bash
# Fetch current body first
CURRENT_BODY=$(gh pr view 123 --json body -q .body)

# Review for media, then update with preserved content
gh pr edit 123 --body "$(cat <<'EOF'
# Updated Description

New content here...

## Screenshots (preserved)
![Original screenshot](https://user-images.githubusercontent.com/...)

EOF
)"
```

**Closing PRs:**
```bash
# Close without merging
gh pr close 123

# Reopen
gh pr reopen 123
```
