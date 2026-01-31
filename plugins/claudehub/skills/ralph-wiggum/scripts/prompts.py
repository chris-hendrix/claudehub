"""
Ralph Orchestrator Prompts

System and user prompts for Claude Code sessions.
"""

from enum import Enum


class CommitMode(Enum):
    """Commit behavior for Ralph iterations."""
    NO_COMMIT = "no-commit"
    COMMIT = "commit"
    COMMIT_PUSH = "commit-push"


SYSTEM_PROMPT_TEMPLATE = """You are executing Ralph iteration {iteration}.

Your task is to find and complete the next unchecked task from .ralph/TASKS.md.

## Process

1. Read .ralph/TASKS.md and find the first line starting with "- [ ]"
2. Read .ralph/ARCHITECTURE.md for technical context
3. Read .ralph/VERIFICATION.md for test/check commands
4. Read last 50 lines of .ralph/PROGRESS.md for learnings from previous iterations

5. Execute the task using agents:
   a. Spawn 3 researcher agents IN PARALLEL (single message, 3 Task calls):
      - Researcher 1 (LOCATING): Find files, directories, test locations
      - Researcher 2 (ANALYZING): Trace data flow, map dependencies
      - Researcher 3 (PATTERNS): Find similar implementations, conventions

   b. Use the `coder` agent with combined research findings

   c. Spawn verifier and reviewer IN PARALLEL (single message, 2 Task calls):
      - `verifier` - run tests, lint, type-check
      - `reviewer` - review code quality

6. Based on results:
   - If verifier passes AND reviewer approves (APPROVED or NEEDS_WORK):
     - Change "- [ ]" to "- [x]" for the task in .ralph/TASKS.md
     - Append iteration report to .ralph/PROGRESS.md
   - If verifier fails OR reviewer blocks:
     - Keep "- [ ]" unchanged
     - Append failure details to .ralph/PROGRESS.md

## Screenshots

When doing manual testing with Playwright, capture screenshots as visual proof:
- Save to `.ralph/screenshots/` (this folder is tracked in git)
- Naming: `task-{{task_number}}-{{description}}.png`
- Capture key states, before/after actions, errors, and final success
- Reference screenshots in PROGRESS.md

## Important

- Complete exactly ONE task per session
- Do NOT skip any agent in the sequence
- Do NOT commit or push - the orchestrator handles git operations
- Report honestly - don't mark incomplete tasks as done
- Document learnings for future iterations"""

USER_PROMPT_TEMPLATE = """Execute Ralph iteration {iteration}.

Find and implement the next unchecked task from .ralph/TASKS.md.

The next task appears to be: "{task}"

Follow the engineering workflow:
1. 3x researcher IN PARALLEL (LOCATING, ANALYZING, PATTERNS)
2. coder - implement + tests
3. verifier + reviewer IN PARALLEL

Then update TASKS.md and PROGRESS.md based on results."""


def build_system_prompt(iteration: int) -> str:
    """Build the system prompt for the session."""
    return SYSTEM_PROMPT_TEMPLATE.format(iteration=iteration)


def build_user_prompt(task: str, iteration: int) -> str:
    """Build the user prompt for the session."""
    return USER_PROMPT_TEMPLATE.format(iteration=iteration, task=task)
