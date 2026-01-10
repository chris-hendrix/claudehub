#!/bin/bash

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  exit 0
fi

# Get the repository root
REPO_ROOT=$(git rev-parse --show-toplevel)

# Get the plugin root (where this script is located)
PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Check if PR template already exists
if [ ! -f "$REPO_ROOT/.github/PULL_REQUEST_TEMPLATE/pull_request_template.md" ]; then
  mkdir -p "$REPO_ROOT/.github/PULL_REQUEST_TEMPLATE"
  cp "$PLUGIN_ROOT/templates/pull_request_template.md" "$REPO_ROOT/.github/PULL_REQUEST_TEMPLATE/"
  echo "✓ Created .github/PULL_REQUEST_TEMPLATE/pull_request_template.md"
fi

# Check if issue template already exists
if [ ! -f "$REPO_ROOT/.github/ISSUE_TEMPLATE/issue_template.md" ]; then
  mkdir -p "$REPO_ROOT/.github/ISSUE_TEMPLATE"
  cp "$PLUGIN_ROOT/templates/issue_template.md" "$REPO_ROOT/.github/ISSUE_TEMPLATE/"
  echo "✓ Created .github/ISSUE_TEMPLATE/issue_template.md"
fi
