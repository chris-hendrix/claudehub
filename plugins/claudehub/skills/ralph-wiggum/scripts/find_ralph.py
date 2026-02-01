#!/usr/bin/env python3
"""
Find running Ralph orchestrator processes.

Returns information about all running ralph.py instances.
"""

import json
import subprocess
import os
from datetime import datetime


def find_ralph_processes():
    """Find all running ralph.py processes.

    Returns list of dicts with: pid, cwd, cmdline, started
    """
    processes = []

    try:
        # Use ps to find Python processes running ralph.py
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True,
            check=True
        )

        for line in result.stdout.split('\n'):
            if 'ralph.py' in line and 'find_ralph.py' not in line:
                # Parse ps output
                parts = line.split(None, 10)
                if len(parts) >= 11:
                    pid = parts[1]

                    # Get process details
                    try:
                        # Get command line
                        with open(f"/proc/{pid}/cmdline", "r") as f:
                            cmdline = f.read().replace('\0', ' ').strip()

                        # Get working directory
                        cwd = os.readlink(f"/proc/{pid}/cwd")

                        # Get start time (elapsed seconds since boot)
                        with open(f"/proc/{pid}/stat", "r") as f:
                            stat = f.read().split()
                            if len(stat) > 21:
                                # starttime is in clock ticks since boot
                                starttime_ticks = int(stat[21])
                                # Get clock ticks per second
                                ticks_per_sec = os.sysconf(os.sysconf_names['SC_CLK_TCK'])
                                # Get system boot time
                                with open("/proc/stat", "r") as boot_f:
                                    for boot_line in boot_f:
                                        if boot_line.startswith("btime"):
                                            boot_time = int(boot_line.split()[1])
                                            # Calculate process start time
                                            start_seconds = boot_time + (starttime_ticks / ticks_per_sec)
                                            start_dt = datetime.fromtimestamp(start_seconds)
                                            starttime = start_dt.strftime("%Y-%m-%d %H:%M:%S")
                                            break
                                    else:
                                        starttime = "unknown"
                            else:
                                starttime = "unknown"

                        processes.append({
                            "pid": int(pid),
                            "cwd": cwd,
                            "cmdline": cmdline,
                            "started": starttime
                        })
                    except (FileNotFoundError, PermissionError):
                        # Process might have ended or we don't have permission
                        continue

    except subprocess.CalledProcessError:
        # ps command failed, try alternative method
        pass

    return processes


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Find running Ralph processes")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Just output count"
    )
    args = parser.parse_args()

    processes = find_ralph_processes()

    if args.count:
        print(len(processes))
        return

    if args.json:
        print(json.dumps(processes, indent=2))
        return

    # Human-readable output
    if not processes:
        print("No running Ralph processes found.")
        return

    print(f"Found {len(processes)} running Ralph process(es):\n")
    for p in processes:
        print(f"PID: {p['pid']}")
        print(f"Started: {p['started']}")
        print(f"Working directory: {p['cwd']}")
        print(f"Command: {p['cmdline']}")
        print()


if __name__ == "__main__":
    main()
