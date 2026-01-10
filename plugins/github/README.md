# GitHub Plugin

Git and GitHub workflow automation with best practices for commits, PRs, and branch management.

## Commands

### `/submit-pr`

Commit changes, push to remote, and create/update draft PR.

**What it does:**
1. Gathers context (branch, PR status, uncommitted changes)
2. Commits any pending changes (confirms with user first)
3. Pushes and creates/updates draft PR
4. Shows PR URL
5. Offers to update title/description or mark ready for review

### `/checkout-default`

Switch to default branch and sync with remote.

**What it does:**
1. Determines the default branch (main or master)
2. Switches to the default branch
3. Fetches from remote
4. Pulls latest changes

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
