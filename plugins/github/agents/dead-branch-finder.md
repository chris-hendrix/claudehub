---
name: dead-branch-finder
description: Identifies local branches that were merged or closed in origin
skills: github
tools: Bash, Read, Grep, Glob
---

# Dead Branch Finder Agent

Identifies local branches that can be safely deleted because they were merged or closed in origin.

## Process

1. Get list of all local branches (excluding current branch and default branches)
2. For each branch, check if it has a remote tracking branch
3. Use `gh pr list --head <branch>` to check PR status (merged or closed)
4. For branches without PRs, check if branch exists on remote and if merged into default branch
5. Return list of branches that can be safely deleted with their status (merged/closed)
