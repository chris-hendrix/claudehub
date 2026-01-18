# Ralph Wiggum - Loop-Based Implementation

Ralph Wiggum is a methodology for autonomous software development through iterative loops with tight feedback cycles. Instead of building software vertically brick-by-brick like Jenga, Ralph treats software as clay on a pottery wheel—malleable, refinable, and shaped through continuous iteration.

**Key differentiator**: Agent-orchestrated outer loop. The agent parses nondeterministic output and makes intelligent decisions about continuation, retries, and failure handling.

**Planning is still critical to Ralph.** You need to break down the work into tasks. But here's the insight: plans are never perfect upfront. When you hand-hold an LLM, things change. You discover gotchas, adjust approach, learn what works. Ralph embraces this. The loop adapts through PROGRESS.md learnings. Start with a good plan, expect it to evolve.

## The Paradigm Shift

- **One-shot approach**: "Build this feature for me" → Bad output. Too broad, no feedback.
- **Hand-holding approach**: You break it down, guide the LLM step-by-step → Good output. Tight feedback loops. But expensive—requires constant engineering time.
- **Ralph approach**: Why don't we get the LLM to do the hand-holding? The loop automates the hand-holding process. You write the plan (break down the work), Ralph guides itself through each step, learning and adapting as it goes.

## The Core Loop

```
repeat {
  spawn ralph-worker agent
    - Finds first unchecked task in PLAN.md
    - Implements task directly using tools
    - Runs tests
    - Updates PLAN.md checkbox on success
    - Appends iteration report to PROGRESS.md
    - Creates commit if autocommit enabled
} until all tasks complete in PLAN.md
```

Orchestrator agent manages the loop, decides when to continue or stop, handles intelligent failure analysis. Worker agent gets fresh context each spawn to avoid context rot.

## Core Principles

- **Task**: The fundamental unit—a small, verifiable piece of work. Not a feature. Not a story. One task per iteration.
- **Tight Context**: Each worker spawn gets PLAN.md and last 200 lines of PROGRESS.md. Fresh context per task prevents context rot.
- **Learn and Adapt**: When tasks fail, document what happened. Next iteration reads these learnings and tries differently.
- **Tests Must Pass**: Only mark complete when verification succeeds. Tight feedback loop.
- **Watch the Loop**: When you see a failure domain, resolve it and engineer a solution so it never happens again. Your learning comes from watching the loop.
- **Context Isolation**: Each task gets a fresh agent spawn with ~200K token budget. No accumulated context across iterations.

## Philosophy

Ralph is context engineering. Get the most out of models by programming tight feedback loops.

When something doesn't work, adjust the instructions (improve learnings). Software is clay—throw it back on the wheel and refine it.

## Usage

```bash
/ralph .thoughts/plans/my-feature.md
```

**First run:**
- Prompts for auto-commit (default: Yes)
- Counts unchecked tasks in plan
- Suggests max iterations (1.5x unchecked task count)
- Displays: "Found X unchecked tasks. Suggest running Y new iterations (total: Y). Confirm?"

**Resume run (if PROGRESS.md exists):**
- Determines last iteration number from PROGRESS.md
- Continues from next iteration
- Displays: "Found X unchecked tasks. Suggest running Y new iterations (total: Z). Confirm?"
  - Where Z = last_iteration + Y

Runs autonomous loops: spawns fresh worker agents to find tasks, implement them, update files, and create commits. Orchestrator makes intelligent decisions about failures and continuation.

## References

- [Ralph Methodology](https://ghuntley.com/ralph/) - Original article by Geoffrey Huntley
- [Loop Philosophy](https://ghuntley.com/loop/) - The mindset shift behind Ralph Wiggum
- [Building Coding Agents](https://www.youtube.com/geoffreyhuntley) - Geoffrey Huntley's workshops
- `agents/ralph-worker.md` - Agent that implements individual tasks
- `commands/ralph.md` - Orchestrator command that manages the loop
