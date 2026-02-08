#!/usr/bin/env python3
"""
Claude Code status line for claudehub
Displays: repo | branch | model | context usage
"""

import json
import sys
import subprocess
import os

# Read JSON data from stdin
data = json.load(sys.stdin)

# Extract fields
model = data.get('model', {}).get('display_name', 'Unknown')
directory = data.get('workspace', {}).get('current_dir', os.getcwd())
pct = int(data.get('context_window', {}).get('used_percentage', 0) or 0)

# Color codes
CYAN = '\033[36m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
ORANGE = '\033[38;5;208m'  # 256-color orange
RED = '\033[31m'
BLUE = '\033[34m'
RESET = '\033[0m'

# Get git info
repo_name = ""
repo_url = ""
branch = ""

try:
    # Check if we're in a git repo
    subprocess.check_output(['git', 'rev-parse', '--git-dir'],
                          stderr=subprocess.DEVNULL)

    # Get repository name and URL from remote
    try:
        remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'],
                                       stderr=subprocess.DEVNULL,
                                       text=True).strip()
        # Convert SSH to HTTPS format
        import re
        remote_https = re.sub(r'^git@github\.com:', 'https://github.com/', remote)
        remote_https = re.sub(r'\.git$', '', remote_https)
        repo_url = remote_https

        # Extract just the repo name from URL
        repo_name = os.path.basename(remote_https)
    except:
        # Fallback to directory name
        repo_name = os.path.basename(directory)

    # Get current branch
    branch = subprocess.check_output(['git', 'branch', '--show-current'],
                                    stderr=subprocess.DEVNULL,
                                    text=True).strip()
except:
    # Not a git repo or git not available
    pass

# Determine context bar color based on usage
if pct >= 80:
    bar_color = RED
elif pct >= 60:
    bar_color = ORANGE
elif pct >= 40:
    bar_color = YELLOW
else:
    bar_color = GREEN

# Build progress bar (10 characters)
filled = pct // 10
bar = '▓' * filled + '░' * (10 - filled)

# Build and output status line
parts = []

if repo_name:
    # Make repo name clickable if we have a URL (OSC 8 escape sequence)
    if repo_url:
        # OSC 8 format: \033]8;;URL\aLINK_TEXT\033]8;;\a
        clickable_repo = f"\033]8;;{repo_url}\a{BLUE}{repo_name}{RESET}\033]8;;\a"
        parts.append(clickable_repo)
    else:
        parts.append(f"{BLUE}{repo_name}{RESET}")

if branch:
    parts.append(f"{GREEN}{branch}{RESET}")

parts.append(f"{YELLOW}[{model}]{RESET}")
parts.append(f"{bar_color}{bar}{RESET} {pct}%")

print(f" {CYAN}│{RESET} ".join(parts))
