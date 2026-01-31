"""
Ralph allowed tools/permissions.

These are pre-approved for Ralph sessions to avoid permission prompts.
"""

ALLOWED_TOOLS = [
    # Git operations
    "Bash(git add *)",
    "Bash(git commit *)",
    "Bash(git push*)",
    "Bash(git status*)",
    "Bash(git diff*)",
    "Bash(git log*)",
]


def get_allowed_tools_args():
    """Build CLI arguments for allowed tools."""
    args = []
    for tool in ALLOWED_TOOLS:
        args.extend(["--allowedTools", tool])
    return args
