# ClaudeHub 🛠️

**Supercharge your development workflow with systematic research, planning, and autonomous implementation.**

The most critical factor in successful LLM-assisted development is **alignment**: ensuring you and the AI are on the same page before writing code. ClaudeHub's spec-driven workflow gets you there through collaborative research, brainstorming, and detailed planning before autonomous implementation.

## ✨ Key Features

### 📋 **Spec Driven Workflow**

Proven methodology for transforming messy ideas into production-ready code.

* **Research & Explore**: Deep codebase understanding before making changes
* **Brainstorm**: Refine rough concepts into validated designs through collaborative dialogue
* **Plan**: Generate detailed, reviewable implementation plans
* **Implement**: Execute with built-in review checkpoints and phase verification
* **Evaluate**: Multi-dimensional quality assessment of your work

_Inspired by [CipherPowers](https://github.com/cipherstash/cipherpowers/), [Superpowers](https://github.com/obra/superpowers), and [HumanLayer](https://github.com/humanlayer/humanlayer)._

### 🔄 **Ralph Wiggum: Autonomous Implementation Agent**

Your autonomous coding companion that implements features while you sleep.

Ralph takes your research and plans, then executes them in tight iterative loops. Unlike one-shot implementations, Ralph validates after each small task, learns from failures, and adapts until success.

**The Problems Ralph Solves:**

1. **Context Rot**: Long sessions accumulate bloated context. Ralph starts each iteration fresh.
2. **Outer Loop Verification**: One-shot implementations only verify at the end. Ralph validates after each task.

**How it works:**

```bash
/ralph PLAN.md
```

Ralph will:

1. 📋 **Load**: Read PLAN.md and PROGRESS.md from previous iterations
2. 🛠️ **Execute**: Implement the first unchecked task with tight context
3. ✅ **Verify**: Run tests and validate the changes
4. 📝 **Document**: Mark task complete and log learnings to PROGRESS.md
5. 🔄 **Iterate**: Start fresh context, retry if failed or move to next task
6. 🎯 **Complete**: Loop until all tasks are checked off

**Critical for success:** Break your feature into small, verifiable tasks. Each task should be independently validatable.

**Perfect for:**

* Complex features that benefit from incremental validation
* Long-running implementations where you want autonomous progress
* Tasks where context efficiency and tight feedback matter

**How Ralph Works Under the Hood:**

Ralph spawns fresh Claude Code sessions in a loop, passing only the plan and last 1000 lines of progress:

```bash
for ((i=1; i<=MAX_ITERATIONS; i++)); do
  # Keep last 1000 lines of progress for context
  tail -n 1000 PROGRESS.md > /tmp/progress_tail.txt

  # Spawn fresh Claude session with tight context
  claude --dangerously-skip-permissions \
         --append-system-prompt "$RALPH_SYSTEM_PROMPT" \
         -p "@PLAN.md @/tmp/progress_tail.txt" \
         "Iteration $i. Implement first unchecked task."

  # Exit if all tasks complete
  grep -q "<promise>COMPLETE</promise>" && break
done
```

Each iteration: fresh context, no bloat, just plan + recent learnings.

_Inspired by Geoffrey Huntley's [Ralph methodology](https://ghuntley.com/ralph/)._

## 🚀 Quick Start

**Installation:**

```bash
/plugin install claudehub@claudehub
```

**Brainstorm an idea:**

```bash
/brainstorm "Add user authentication with OAuth"
```

**Create a detailed plan:**

```bash
/create-plan brainstorm.md
```

**Run Ralph to implement:**

```bash
/ralph PLAN.md
```

## 📦 Additional Plugins

**GitHub Plugin** for streamlined git workflows: intelligent PR creation, branch management, and commit automation.

```bash
/plugin install github@claudehub
```