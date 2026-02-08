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

### 🔄 **Ralph Wiggum**

Your autonomous coding companion that implements features through a structured engineering workflow.

Ralph executes tasks through a Python orchestrator that spawns Claude Code sessions. Each session runs a specialized agent pipeline to complete one task with proper research, implementation, verification, and review.

**Key differentiator:** Multi-agent pipeline with parallel execution. The Python orchestrator manages session spawning and progress tracking, while specialized agents handle research, coding, testing, and review for each task.

**How it works:**

```bash
# Quick autonomous planning + execution
/claudehub:ralph:run "add user authentication with JWT"

# Or plan interactively first
/claudehub:ralph:plan-deep docs/prd.md
/claudehub:ralph:run
```

**The Agent Pipeline:**

```
3x researcher (parallel) → coder → verifier + reviewer (parallel)
```

Each task goes through:
1. **Research** - Three parallel researchers gather context (LOCATING, ANALYZING, PATTERNS)
2. **Code** - Coder implements + writes tests
3. **Verify** - Verifier runs tests, linting, type-checking
4. **Review** - Reviewer assesses code quality
5. **Complete** - Mark task done in `.ralph/TASKS.md`, log to `.ralph/PROGRESS.md`

**File Structure:**

All Ralph files live in `.ralph/`:
- `ARCHITECTURE.md` - Technical approach
- `TASKS.md` - Tasks with checkboxes, organized by phase
- `VERIFICATION.md` - Test commands, environment setup
- `PROGRESS.md` - Learnings from each iteration

**Architecture benefits:**

* **Parallel execution**: 3x researcher + verifier/reviewer run concurrently
* **Specialized agents**: Each agent has a focused responsibility
* **Context isolation**: Fresh session per task prevents context rot
* **Built-in planning**: `/claudehub:ralph-plan` for quick autonomous planning or `/claudehub:ralph:plan-deep` for interactive deep planning
* **Progress tracking**: `/claudehub:ralph-status` shows real-time progress

**Perfect for:**

* Complex features with clear requirements (PRDs, design docs)
* Projects needing thorough testing and review
* Teams wanting structured engineering workflow
* Long-running implementations with autonomous progress

_Inspired by Geoffrey Huntley's [Ralph methodology](https://ghuntley.com/ralph/)._

## 🚀 Quick Start

**Installation:**

```bash
/plugin install claudehub@claudehub

# Optional: Install custom statusline
/claudehub:install-statusline
# claudehub │ main │ [Sonnet 4.5] │ ▓▓▓▓▓░░░░░ 50%
```

**Brainstorm an idea:**

```bash
/claudehub:brainstorm "Add user authentication with OAuth"
```

**Create a detailed plan:**

```bash
/claudehub:create-plan brainstorm.md
```

**Run Ralph to implement:**

```bash
# Quick autonomous approach
/claudehub:ralph:run "add user authentication with OAuth"

# Or manual planning first
/claudehub:ralph:plan-deep docs/prd.md
/claudehub:ralph:run
```

## 📦 Additional Plugins

**GitHub Plugin** for streamlined git workflows: intelligent PR creation, branch management, and commit automation.

```bash
/plugin install github@claudehub
```