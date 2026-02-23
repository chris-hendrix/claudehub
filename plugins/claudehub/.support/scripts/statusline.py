#!/usr/bin/env python3
"""
Claude Code status line for claudehub
Line 1: repo | branch | model | context bar
Line 2: (reserved for Claude Code messages)
"""

import json
import sys
import subprocess
import os
import re

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
    subprocess.check_output(['git', 'rev-parse', '--git-dir'],
                          stderr=subprocess.DEVNULL)
    try:
        remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'],
                                       stderr=subprocess.DEVNULL,
                                       text=True).strip()
        remote_https = re.sub(r'^git@github\.com:', 'https://github.com/', remote)
        remote_https = re.sub(r'\.git$', '', remote_https)
        repo_url = remote_https
        repo_name = os.path.basename(remote_https)
    except Exception:
        repo_name = os.path.basename(directory)

    branch = subprocess.check_output(['git', 'branch', '--show-current'],
                                    stderr=subprocess.DEVNULL,
                                    text=True).strip()
except Exception:
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

SEP = f" {CYAN}│{RESET} "

# Build parts
parts = []

if repo_name:
    if repo_url:
        parts.append(f"\033]8;;{repo_url}\a{BLUE}{repo_name}{RESET}\033]8;;\a")
    else:
        parts.append(f"{BLUE}{repo_name}{RESET}")

if branch:
    MAX_BRANCH = 30
    display_branch = branch
    if len(branch) > MAX_BRANCH:
        keep = MAX_BRANCH - 1
        head = keep // 2
        tail = keep - head
        display_branch = branch[:head] + '…' + branch[-tail:]
    if repo_url:
        branch_url = f"{repo_url}/tree/{branch}"
        parts.append(f"\033]8;;{branch_url}\a{GREEN}{display_branch}{RESET}\033]8;;\a")
    else:
        parts.append(f"{GREEN}{display_branch}{RESET}")

parts.append(f"{YELLOW}[{model}]{RESET}")
parts.append(f"{bar_color}{bar}{RESET} {pct}%")

# Print status then a blank line so Claude Code messages appear on the next line
print(SEP.join(parts))
print()
