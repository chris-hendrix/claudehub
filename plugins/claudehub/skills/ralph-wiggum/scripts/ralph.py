#!/usr/bin/env python3
"""
Ralph Orchestrator

Spawns Claude Code sessions to execute tasks from .ralph/TASKS.md
Each session uses the engineering workflow agents:
researcher → coder → verifier → reviewer
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time

from allowed_tools import get_allowed_tools_args
from prompts import build_system_prompt, build_user_prompt, CommitMode


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Ralph Orchestrator")
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=50,
        help="Maximum iterations (default: 50)",
    )
    parser.add_argument(
        "--commit-mode",
        type=lambda x: CommitMode(x),
        choices=list(CommitMode),
        default=CommitMode.COMMIT_PUSH,
        help="Commit behavior (default: commit-push)",
    )
    return parser.parse_args()


def validate_setup():
    """Check if required files exist."""
    required_files = [
        ".ralph/TASKS.md",
        ".ralph/ARCHITECTURE.md",
        ".ralph/VERIFICATION.md",
    ]

    for f in required_files:
        if not os.path.exists(f):
            print(f"Error: Required file not found: {f}", file=sys.stderr)
            print("Run /plan first to create planning documents.", file=sys.stderr)
            return False

    return True


def find_next_task():
    """Find next unchecked task from TASKS.md."""
    with open(".ralph/TASKS.md", "r") as f:
        for line in f:
            if line.startswith("- [ ]"):
                # Extract task description (everything after "- [ ] ")
                return line[6:].strip()
    return None


def is_task_complete(task_name):
    """Check if task is now complete (checkbox marked)."""
    with open(".ralph/TASKS.md", "r") as f:
        content = f.read()

    # Escape special regex characters in task name
    escaped_task = re.escape(task_name)
    pattern = rf"^- \[x\] {escaped_task}"
    return bool(re.search(pattern, content, re.MULTILINE))


def count_tasks():
    """Count total and remaining tasks."""
    with open(".ralph/TASKS.md", "r") as f:
        content = f.read()

    total = len(re.findall(r"^- \[[x ]\]", content, re.MULTILINE))
    remaining = len(re.findall(r"^- \[ \]", content, re.MULTILINE))
    return total, remaining


def get_last_iteration():
    """Get last iteration number from PROGRESS.md."""
    if not os.path.exists(".ralph/PROGRESS.md"):
        return 0

    with open(".ralph/PROGRESS.md", "r") as f:
        content = f.read()

    matches = re.findall(r"^## Iteration (\d+)", content, re.MULTILINE)
    if not matches:
        return 0

    return int(matches[-1])


def init_progress_file():
    """Initialize PROGRESS.md if it doesn't exist."""
    if not os.path.exists(".ralph/PROGRESS.md"):
        with open(".ralph/PROGRESS.md", "w") as f:
            f.write("# Ralph Progress\n\nTracking implementation progress for this project.\n\n")


def init_gitignore():
    """Create .ralph/.gitignore to exclude logs."""
    gitignore_path = ".ralph/.gitignore"
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w") as f:
            f.write("# Ralph logs are local-only\nlogs/\n")


def push_changes():
    """Push committed changes to remote, setting up tracking if needed."""
    try:
        subprocess.run(
            ["git", "push", "-u", "origin", "HEAD"],
            capture_output=True,
            check=True,
        )
        print("📤 Pushed to remote")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to push: {e}", file=sys.stderr)


def get_latest_iteration_content():
    """Get the content of the latest iteration from PROGRESS.md."""
    if not os.path.exists(".ralph/PROGRESS.md"):
        return None

    with open(".ralph/PROGRESS.md", "r") as f:
        content = f.read()

    # Find the last iteration section
    matches = list(re.finditer(r"^## Iteration \d+.*?(?=^## Iteration |\Z)", content, re.MULTILINE | re.DOTALL))
    if matches:
        return matches[-1].group(0).strip()
    return None


def commit_task(task: str, iteration: int, commit_mode: CommitMode):
    """Commit changes after a task completes."""
    if commit_mode == CommitMode.NO_COMMIT:
        return

    # Get the iteration content for the commit body
    iteration_content = get_latest_iteration_content() or ""

    # Build commit message
    commit_msg = f"""Ralph: Task {iteration} - {task}

{iteration_content}
"""

    try:
        # Stage all changes
        subprocess.run(
            ["git", "add", "-A"],
            capture_output=True,
            check=True,
        )

        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
        )
        if not result.stdout.strip():
            print("📝 No changes to commit")
            return

        # Commit
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            capture_output=True,
            check=True,
        )
        print(f"📝 Committed: Task {iteration} - {task[:50]}...")

        # Push if commit-push mode
        if commit_mode == CommitMode.COMMIT_PUSH:
            push_changes()

    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to commit: {e}", file=sys.stderr)


def commit_planning_files(commit_mode: CommitMode):
    """Commit planning files before starting implementation."""
    if commit_mode == CommitMode.NO_COMMIT:
        return

    planning_files = [
        ".ralph/ARCHITECTURE.md",
        ".ralph/TASKS.md",
        ".ralph/VERIFICATION.md",
        ".ralph/PROGRESS.md",
        ".ralph/.gitignore",
    ]

    # Check if any planning files need to be committed
    result = subprocess.run(
        ["git", "status", "--porcelain"] + planning_files,
        capture_output=True,
        text=True,
    )

    if not result.stdout.strip():
        return  # Nothing to commit

    try:
        # Stage planning files
        subprocess.run(
            ["git", "add"] + planning_files,
            capture_output=True,
            check=True,
        )
        # Commit
        subprocess.run(
            ["git", "commit", "-m", "Ralph: Planning docs"],
            capture_output=True,
            check=True,
        )
        print("📋 Committed planning files")
        if commit_mode == CommitMode.COMMIT_PUSH:
            push_changes()
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Failed to commit planning files: {e}", file=sys.stderr)


def get_branch_name():
    """Get current git branch name, sanitized for filenames."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        branch = result.stdout.strip()
        # Sanitize for filename (replace / with -)
        return branch.replace("/", "-")
    except subprocess.CalledProcessError:
        return "unknown-branch"


def stream_session_output(process, log_file):
    """Stream output to log file, show progress, return final result."""
    message_count = 0
    result = {}

    with open(log_file, "w") as log:
        for line in process.stdout:
            log.write(line)
            log.flush()

            try:
                msg = json.loads(line)
                msg_type = msg.get("type", "")

                if msg_type == "assistant":
                    print(".", end="", flush=True)
                    message_count += 1
                elif msg_type == "result":
                    result = msg

            except json.JSONDecodeError:
                pass

    # Print summary
    if result:
        cost = result.get("total_cost_usd", 0)
        duration = result.get("duration_ms", 0) / 1000
        usage = result.get("usage", {})
        input_tokens = usage.get("input_tokens", 0)
        output_tokens = usage.get("output_tokens", 0)
        print(f"\n[{message_count} msgs | in:{input_tokens:,} out:{output_tokens:,} | ${cost:.4f} | {duration:.1f}s]")

    return result


def spawn_session(task, iteration):
    """Spawn a Claude Code session with JSONL logging."""
    system_prompt = build_system_prompt(iteration)
    user_prompt = build_user_prompt(task, iteration)

    # Set up logging in branch subfolder
    branch = get_branch_name()
    log_dir = f".ralph/logs/{branch}"
    os.makedirs(log_dir, exist_ok=True)
    log_file = f"{log_dir}/iteration-{iteration:03d}.jsonl"

    print(f"\n{'=' * 60}")
    print(f"Iteration {iteration}: {task}")
    print(f"Log: {log_file}")
    print(f"{'=' * 60}\n")

    try:
        cmd = [
            "claude",
            "-p", user_prompt,
            "--system-prompt", system_prompt,
            "--output-format", "stream-json",
            "--verbose",
            "--permission-mode", "acceptEdits",
            *get_allowed_tools_args(),
        ]

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            # CI=true prevents Jest/Cypress from running in watch mode
            env={**os.environ, "CI": "true"},
        )

        stream_session_output(process, log_file)
        process.wait()

        if process.returncode == 0:
            # Check if task was marked complete
            complete = is_task_complete(task)
            if complete:
                print(f"\n✅ Task completed: {task}\n")
            else:
                print(f"\n⚠️ Task not completed, will retry: {task}\n")
            return complete
        else:
            print(f"\n❌ Session exited with code {process.returncode}\n", file=sys.stderr)
            return False

    except FileNotFoundError:
        print("\n❌ Error: 'claude' command not found. Is Claude Code installed?\n", file=sys.stderr)
        return False
    except Exception as e:
        print(f"\n❌ Failed to spawn session: {e}\n", file=sys.stderr)
        return False


def main():
    """Main execution loop."""
    args = parse_args()
    commit_mode = args.commit_mode

    print("🤖 Ralph Orchestrator Starting\n")
    print(f"Max iterations: {args.max_iterations}")
    print(f"Commit mode: {commit_mode.value}")
    print()

    # Validate setup
    if not validate_setup():
        sys.exit(1)

    # Initialize progress file and gitignore
    init_progress_file()
    init_gitignore()

    # Commit planning files (respects commit mode)
    commit_planning_files(commit_mode)

    # Get starting iteration
    iteration = get_last_iteration() + 1
    start_iteration = iteration

    # Count initial tasks
    total, remaining = count_tasks()
    print(f"Tasks: {remaining} remaining of {total} total\n")

    if remaining == 0:
        print("✅ All tasks complete!")
        sys.exit(0)

    # Main loop
    consecutive_failures = 0
    last_failed_task = ""

    while iteration < start_iteration + args.max_iterations:
        task = find_next_task()

        if not task:
            print("\n✅ All tasks complete!")
            break

        # Track consecutive failures on same task
        if task == last_failed_task:
            consecutive_failures += 1
            if consecutive_failures >= 3:
                print(f"\n🛑 Task failed 3 times consecutively: {task}")
                print("Stopping to prevent infinite loop.")
                break
        else:
            consecutive_failures = 0
            last_failed_task = ""

        success = spawn_session(task, iteration)

        # Commit based on result and commit mode
        if success:
            commit_task(task, iteration, commit_mode)
        else:
            last_failed_task = task
            if consecutive_failures == 0:
                consecutive_failures = 1

        iteration += 1

        # Brief pause between iterations
        time.sleep(1)

    # Final summary
    _, final_remaining = count_tasks()
    completed = remaining - final_remaining

    print(f"\n{'=' * 60}")
    print("Ralph Execution Complete")
    print("=" * 60)
    print(f"Iterations run: {iteration - start_iteration}")
    print(f"Tasks completed: {completed}")
    print(f"Tasks remaining: {final_remaining}")

    if final_remaining > 0:
        print("\nRun /run again to continue.")


if __name__ == "__main__":
    main()
