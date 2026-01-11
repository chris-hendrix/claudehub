#!/bin/bash
# SessionStart hook: Ensures .thoughts/ folder is globally gitignored

set -euo pipefail

# Ensure git uses a global excludes file (only if not already set)
if [ -z "$(git config --global core.excludesfile)" ]; then
    git config --global core.excludesfile ~/.gitignore
fi

# Get the actual excludes file path
EXCLUDES_FILE=$(git config --global core.excludesfile)
EXCLUDES_FILE="${EXCLUDES_FILE/#\~/$HOME}"  # Expand ~ to $HOME

# Create the file if it doesn't exist
touch "$EXCLUDES_FILE"

# Add .thoughts/ if not already present
if ! grep -q "^\.thoughts/$" "$EXCLUDES_FILE" 2>/dev/null; then
    echo ".thoughts/" >> "$EXCLUDES_FILE"
    echo "Added .thoughts/ to global gitignore ($EXCLUDES_FILE)"
fi
