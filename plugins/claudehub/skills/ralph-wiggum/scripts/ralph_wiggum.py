#!/usr/bin/env python3
"""Ralph Wiggum - Autonomous implementation agent for Claude Code plans."""

import argparse
import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime


def get_progress_file(plan_file: Path) -> Path:
    """Generate progress file path from plan file: plan-name.md -> plan-name-progress.md"""
    return plan_file.parent / f"{plan_file.stem}-progress.md"


def initialize_progress_file(progress_file: Path):
    """Create progress file if it doesn't exist."""
    if not progress_file.exists():
        progress_file.write_text("""# Ralph Wiggum Implementation Progress

## Learnings

Patterns and insights that help future iterations succeed:
- Key commands (tests, build, etc.)
- File patterns and conventions
- Common pitfalls to avoid

---

## Iteration Log

""")


def run_claude(plan_file: Path, progress_file: Path, iteration: int) -> str:
    """Run Claude with the Ralph prompt."""

    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""You are Ralph Wiggum (iteration {iteration}), an autonomous implementation agent.

## Context
- **Plan file**: Architecture and tasks
- **Progress file**: Learnings from previous iterations - READ LEARNINGS SECTION FIRST

## Process

1. **Check progress** - Read Learnings section for patterns that work
2. **Find next task** - First `- [ ] **Task N.M: ...**` in plan
3. **Implement** - Complete all steps, follow discovered patterns
4. **Verify** - Run tests/checks
5. **Update files**:
   - Plan: mark `- [x]`, add to Tracked Changes: **[{today}]** Iteration {iteration}: Task N.M brief
   - Progress: append iteration entry with what worked

## Progress Entry Format

```
### Iteration {iteration} - Task N.M
- Result: TASK_COMPLETE/TASK_FAILED
- Files: [list]
- What worked/failed: [approach and outcome]
- Learnings: [add reusable patterns to Learnings section above]
```

## Rules
- ONE task only
- Tests must PASS before marking complete
- Note failures in progress for next iteration

## Output
- Tests PASS → <promise>TASK_COMPLETE</promise>
- Tests FAIL → <promise>TASK_FAILED</promise>
- All done → <promise>ALL_COMPLETE</promise> (update plan status: completed)
"""

    cmd = [
        "claude", "--dangerously-skip-permissions", "--output-format", "text",
        "-p", f"@{plan_file}",
        "-p", f"@{progress_file}",
        prompt
    ]
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def commit_changes(iteration: int, output: str):
    """Auto-commit if tests passed."""
    task_match = re.search(r'Task ([\d.]+)', output)
    task_id = task_match.group(1) if task_match else "task"

    subprocess.run(["git", "add", "."], check=True)
    msg = f"feat: Complete Task {task_id}\n\nIteration {iteration}\n\nCo-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
    subprocess.run(["git", "commit", "-m", msg], capture_output=True)


def main():
    parser = argparse.ArgumentParser(description="Ralph Wiggum - Autonomous implementation agent")
    parser.add_argument("plan_file", type=Path, help="Path to plan file")
    parser.add_argument("--max-iterations", type=int, default=10, help="Max iterations (default: 10)")
    parser.add_argument("--commit", action="store_true", help="Auto-commit successful tasks")
    args = parser.parse_args()

    if not args.plan_file.exists():
        print(f"Error: Plan file not found: {args.plan_file}")
        sys.exit(1)

    # Setup progress file
    progress_file = get_progress_file(args.plan_file)
    initialize_progress_file(progress_file)

    print(f"Starting Ralph Wiggum - {args.plan_file.name} (max {args.max_iterations} iterations)")
    print(f"Progress: {progress_file.name}\n")

    for i in range(1, args.max_iterations + 1):
        print(f"{'='*60}\nIteration {i}/{args.max_iterations}\n{'='*60}")

        result = run_claude(args.plan_file, progress_file, i)
        print(result)

        if "<promise>ALL_COMPLETE</promise>" in result:
            print("\n🎉 Implementation complete!")
            sys.exit(0)

        if "<promise>TASK_COMPLETE</promise>" in result and args.commit:
            print("\nCommitting changes...")
            commit_changes(i, result)
        elif "<promise>TASK_FAILED</promise>" in result:
            print("\n⚠️  Task failed, continuing...")

        print()

    print(f"⚠️  Reached max iterations ({args.max_iterations})")
    sys.exit(1)


if __name__ == "__main__":
    main()
