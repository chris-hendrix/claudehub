#!/bin/bash
# SessionStart hook: Ensures .thoughts/ folder is globally gitignored

set -euo pipefail

# Ensure git uses ~/.gitignore as global excludes (only if not already set)
if [ -z "$(git config --global core.excludesfile)" ]; then
    git config --global core.excludesfile ~/.gitignore
fi

# Add .thoughts/ if not already present
if ! grep -q "^\.thoughts/$" "$HOME/.gitignore" 2>/dev/null; then
    echo ".thoughts/" >> "$HOME/.gitignore"
    echo 'Added .thoughts/ to global gitignore'
fi
