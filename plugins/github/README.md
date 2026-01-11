# GitHub Plugin

Git and GitHub workflow automation with best practices for commits, PRs, and branch management.

## Commands

### `/create-branch`

Create a new git branch with AI-suggested name.

**What it does:**
1. Uses branch-namer agent to suggest branch name
2. Gathers context (current branch, uncommitted changes)
3. Confirms branch name and stash preferences with user
4. Stashes changes if needed
5. Creates and checks out new branch
6. Pops stash if changes were stashed

### `/submit-pr`

Commit changes, push to remote, and create/update draft PR.

**What it does:**
1. Creates branch if on default branch (via `/create-branch`)
2. Commits any pending changes (confirms with user first)
3. Pushes and creates/updates draft PR
4. Shows PR URL
5. Offers to update title/description (via `/describe-pr`)
6. Offers to mark PR as ready for review (publish)

### `/describe-pr`

Generate and update PR title and description from branch diff.

**What it does:**
1. Uses pr-describer agent to analyze branch changes
2. Generates PR title and description
3. Displays generated content
4. Confirms with user
5. Updates PR using `gh pr edit`

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
1. Uses dead-branch-finder agent to identify stale branches
2. Displays list of branches with their status (merged/closed)
3. Confirms which branches to delete
4. Deletes confirmed branches

### `/create-issue`

Create a GitHub issue with AI-generated content.

**What it does:**
1. Gathers input from user (issue type, description, context)
2. Generates issue title and description following template format
3. Displays generated content
4. Confirms with user and asks about labels/assignees
5. Creates issue using `gh issue create`
6. Shows issue URL and number

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
**Manual:** Run `scripts/setup-templates.sh` from the plugin directory

## Installation

**From this repository:**
```bash
/plugin marketplace add /path/to/claude-hub
/plugin install github@claude-hub
```

**From GitHub:**
```bash
/plugin marketplace add username/claude-hub
/plugin install github@claude-hub
```

## Version

1.0.0
