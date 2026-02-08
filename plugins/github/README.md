# GitHub Plugin

Git and GitHub workflow automation with best practices for commits, PRs, and branch management.

## Commands

### `/create-branch`

Create a new git branch with AI-suggested name.

**What it does:**
1. Gathers context and suggests appropriate branch name
2. Handles uncommitted changes appropriately
3. Creates and checks out new branch

### `/submit-pr`

Commit changes, push to remote, and create/update draft PR.

**What it does:**
1. Creates branch if on default branch
2. Commits any changes
3. Pushes and creates/updates draft PR
4. Shows PR URL
5. Offers to update title/description
6. Offers to mark as ready for review if in draft state

### `/describe-pr`

Generate and update PR title and description from branch diff.

**What it does:**
1. Gathers context and generates PR title and description
2. Displays generated content
3. Confirms with user
4. Updates PR

### `/checkout-default`

Switch to default branch and sync with remote.

**What it does:**
1. Determines the default branch (main or master)
2. Gathers context (current branch, uncommitted changes)
3. Confirms and asks about stashing changes
4. Stashes changes if needed
5. Switches to default branch
6. Fetches and pulls latest changes
7. Pops stash if changes were stashed
8. Offers to clean dead branches (via `/clean-branches`)

### `/clean-branches`

Delete local branches that were merged or closed in origin.

**What it does:**
1. Fetches and prunes remote tracking info
2. Identifies stale branches marked as [gone]
3. Displays list of branches that can be deleted
4. Confirms which branches to delete
5. Deletes confirmed branches

### `/create-issue`

Create a GitHub issue with AI-generated content.

**What it does:**
1. Gathers input from user (issue type, description, context)
2. Generates issue title and description following template format
3. Displays generated content
4. Confirms with user and asks about labels/assignees
5. Creates issue using `gh issue create`
6. Shows issue URL and number

### `/setup-templates`

Set up GitHub PR and issue templates in the repository.

**What it does:**
1. Creates `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` if it doesn't exist
2. Creates `.github/ISSUE_TEMPLATE/issue_template.md` if it doesn't exist
3. Skips existing templates to avoid overwriting customizations

## Skills

### `github`

Workflow methodology using GitHub Issues, GitHub PRs, and raw git commands.

**Provides:**
- Draft PR-first development strategy
- Squash and merge methodology
- GitHub Issues tracking and templates
- Branch naming conventions
- Pull request best practices
- Common git and gh CLI commands

**References:**
- `workflows.md` - Detailed draft PR-first workflow
- `issues.md` - Issue creation, management, and templates
- `branches.md` - Branch naming conventions
- `pull-requests.md` - PR guidelines, best practices, and template

## Scripts

### `setup-templates.sh`

Creates GitHub templates in your repository if they don't exist:
- `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/issue_template.md`

**Automatic:** Runs on session start via hook
**Manual:** Run `.support/scripts/setup-templates.sh` from the plugin directory

## Installation

**From this repository:**
```bash
/plugin marketplace add /path/to/claudehub
/plugin install github@claudehub
```

**From GitHub:**
```bash
/plugin marketplace add username/claudehub
/plugin install github@claudehub
```

## Version

1.0.0
