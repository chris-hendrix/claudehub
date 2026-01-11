---
name: github
description: This skill should be used when working with git commits, branches, GitHub issues, and GitHub PRs. Provides workflow strategy for draft PRs, squash merging, and Graphite-style development.
version: 1.0.0
---

# GitHub

Workflow methodology for git and GitHub using GitHub Issues, GitHub PRs, and raw git commands.

## Tools

Use these tools for development workflows:
- **GitHub Issues** - Track tasks, bugs, and features
- **GitHub PRs** - Code review and merging via draft-first workflow
- **Raw git** - Local version control and branch management
- **gh CLI** - GitHub operations from the command line

## Workflow Strategy

Follow a draft PR-first approach with squash merging - see `references/workflows.md` for detailed methodology.

**Key principles:**
- **NEVER commit or push directly to the default branch (main/master)** - Always work on feature branches
- Every push creates or updates a draft PR
- Always use squash and merge
- Work in small, focused PRs (Graphite-style)

## GitHub Issues

Use GitHub Issues to track tasks, bugs, and features - see `references/issues.md` for guidelines, templates, and commands.

## Branch Naming

Follow consistent branch naming conventions - see `references/branches.md` for detailed guidelines.

## Pull Requests

Follow PR best practices for effective code review - see `references/pull-requests.md` for detailed guidelines, templates, and commands.

