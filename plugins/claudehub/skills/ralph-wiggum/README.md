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
  claude --dangerously-skip-permissions \
    -p "@PLAN.md @PROGRESS.md" \
    "Complete next unchecked task. Learn from PROGRESS.md."
} until all tasks complete in PLAN.md
```

That's it. Agent orchestrates the loop, decides when to continue or stop, parses nondeterministic output.

## Core Principles

- **Task**: The fundamental unit—a small, verifiable piece of work. Not a feature. Not a story. One task per iteration.
- **Tight Context**: Each iteration gets PLAN.md and last 200 lines of PROGRESS.md. No conversation history.
- **Learn and Adapt**: When tasks fail, document what happened. Next iteration reads these learnings and tries differently.
- **Tests Must Pass**: Only mark complete when verification succeeds. Tight feedback loop.
- **Watch the Loop**: When you see a failure domain, resolve it and engineer a solution so it never happens again. Your learning comes from watching the loop.

## Philosophy

Ralph is context engineering. Get the most out of models by programming tight feedback loops.

When something doesn't work, adjust the instructions (improve learnings). Software is clay—throw it back on the wheel and refine it.

## Usage

```bash
/ralph .thoughts/plans/my-feature.md
```

Prompts for auto-commit (default: Yes) and max iterations (suggested: 1.5x task count).

Runs autonomous loops: finds tasks, implements, updates files, creates commits. Agent orchestrator makes intelligent decisions about failures and continuation.

## References

- [Ralph Methodology](https://ghuntley.com/ralph/) - Original article by Geoffrey Huntley
- [Loop Philosophy](https://ghuntley.com/loop/) - The mindset shift behind Ralph Wiggum
- [Building Coding Agents](https://www.youtube.com/geoffreyhuntley) - Geoffrey Huntley's workshops
- `agents/ralph-task-implementer.md` - Agent that implements individual tasks
- `commands/ralph.md` - Orchestrator command that manages the loop
