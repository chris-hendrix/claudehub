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

      IMPORTANT: Do NOT tell researchers to save their findings to files.
      Researchers return their findings in their agent output - you'll pass these directly to the coder.

   b. Use the `coder` agent with combined research findings from all 3 researchers

   c. Spawn verifier and reviewer IN PARALLEL (single message, 2 Task calls):
      - `verifier` - run tests, lint, type-check
      - `reviewer` - review code quality

      IMPORTANT: Do NOT tell verifier/reviewer to save their reports to files.
      They return their reports in their agent output - you'll include these in PROGRESS.md.

6. Based on results:
   - If verifier PASSES AND reviewer returns APPROVED:
     - Change "- [ ]" to "- [x]" for the task in .ralph/TASKS.md
     - Append iteration report to .ralph/PROGRESS.md

   - If verifier FAILS:
     - The task DOES NOT PASS. Period. No exceptions.
     - Call the coder agent with the failure output to fix it
     - Re-run verifier (and reviewer if code changed)
     - Repeat until verifier passes - do NOT defer to next iteration

   - If reviewer returns NEEDS_WORK:
     - The task DOES NOT PASS. NEEDS_WORK means NOT done.
     - Call the coder agent with ALL reviewer feedback to fix it NOW
     - Re-run verifier and reviewer after fixes
     - Repeat until reviewer returns APPROVED - do NOT defer to next iteration
     - You have full authority to make design decisions when implementing feedback

   - If reviewer returns BLOCKED:
     - Keep "- [ ]" unchanged
     - Append failure details to .ralph/PROGRESS.md
     - Add a FIX sub-task for the blocking issue

## Handling Fundamental Issues

If you discover a fundamental issue during implementation (architecture problem, missing dependency, breaking bug):

1. **Add a sub-task** to TASKS.md immediately after the current task:
   - Format: `- [ ] {{parent}}.1 FIX: {{issue_description}}`
   - Example: Working on "2 Add authentication" → add "- [ ] 2.1 FIX: database auth configuration"
   - Use hierarchical numbering: 1.1, 1.2, 2.1, 2.1.1, etc.

2. **Mark current task incomplete** and document the blocker in PROGRESS.md

3. **Debug mode**: When working on FIX tasks, WebSearch tool is available for finding solutions to errors, configuration issues, or technical problems. Use it if helpful.

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
- Report honestly - only mark tasks complete when verifier PASSES and reviewer APPROVED
- NEEDS_WORK means NOT finished - fix it NOW, do not defer to next iteration
- Test failures mean NOT finished - fix it NOW, do not defer to next iteration
- Make all design decisions autonomously - you have full authority, no human intervention expected
- If testing environment has issues, fix them yourself before proceeding
- Document learnings for future iterations"""

USER_PROMPT_TEMPLATE = """Execute Ralph iteration {iteration}.

Find and implement the next unchecked task from .ralph/TASKS.md.

The next task appears to be: "{task}"

Follow the engineering workflow:
1. 3x researcher IN PARALLEL (LOCATING, ANALYZING, PATTERNS)
2. coder - implement + tests
3. verifier + reviewer IN PARALLEL
4. If tests FAIL: fix and re-verify until they pass. No exceptions.
5. If NEEDS_WORK: implement ALL feedback NOW and re-verify. Do NOT defer.
6. Only mark complete when verifier PASSES and reviewer APPROVED

Then update TASKS.md and PROGRESS.md based on results."""


def build_system_prompt(iteration: int) -> str:
    """Build the system prompt for the session."""
    return SYSTEM_PROMPT_TEMPLATE.format(iteration=iteration)


def build_user_prompt(task: str, iteration: int) -> str:
    """Build the user prompt for the session."""
    return USER_PROMPT_TEMPLATE.format(iteration=iteration, task=task)
