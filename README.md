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

**Key differentiator:** Agent-orchestrated outer loop with fresh worker spawns per task. The orchestrator manages intelligent decision-making about continuation, retries, and failure handling, while each worker gets clean context to prevent context rot.

**How it works:**

```bash
/ralph PLAN.md
```

**The Core Loop:**

```
repeat {
  spawn fresh ralph-worker agent
    → Finds first unchecked task in PLAN.md
    → Implements task directly using tools
    → Runs tests
    → Updates PLAN.md checkbox on success
    → Appends iteration report to PROGRESS.md
    → Creates commit if autocommit enabled
} until all tasks complete in PLAN.md
```

Orchestrator manages the loop, parsing iteration reports and deciding whether to continue, retry, or stop. Each worker gets fresh context (PLAN.md + last 200 lines of PROGRESS.md) to avoid context pollution across tasks.

**Critical for success:** Break your feature into small, verifiable tasks. Each task should be independently validatable. Plans are never perfect upfront—they evolve during implementation, and Ralph adapts through learnings.

**Architecture benefits:**

* **Context isolation**: Fresh worker spawn per task prevents context rot
* **Consistent quality**: Each task gets clean ~200K token budget
* **Intelligent failure handling**: Learns from PROGRESS.md, retries up to 3 times per task
* **Resume capability**: Picks up from last iteration if interrupted

**Perfect for:**

* Complex features that benefit from incremental validation
* Long-running implementations where you want autonomous progress
* Multi-task workflows where context isolation matters

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