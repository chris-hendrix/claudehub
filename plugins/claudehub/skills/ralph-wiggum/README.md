# Ralph Wiggum - Loop-Based Implementation

Ralph Wiggum is a methodology for autonomous software development through iterative loops with tight feedback cycles. Instead of building software vertically brick-by-brick like Jenga, Ralph Wiggum treats software as clay on a pottery wheel—malleable, refinable, and shaped through continuous iteration.

## The Paradigm Shift

**Traditional Development**: Build vertically, brick-by-brick
- Engineer builds software manually
- Linear progression through features
- Changes are expensive and risky

**Ralph Wiggum Development**: Program loops that build autonomously
- Engineer programs the loop
- Iterative refinement through cycles
- Changes are cheap—throw it back on the wheel

Ralph Wiggum recognizes that LLMs are "a new form of programmable computer." You're not building software anymore; you're programming loops that build software.

## Core Principles

### Tight Context Loops

Each iteration operates with minimal context:
- **Plan file**: Task list and architectural decisions
- **Progress file**: Learnings section + iteration log
- **Current iteration number**

No conversation history accumulates. This keeps context windows efficient and focused.

### One Task Per Loop

Complete one task, verify it passes, document learnings, move to next.

- Single process, monolithic design
- No multi-agent complexity or non-determinism
- Scales vertically, not through distributed systems
- Predictable and debuggable

### Learn and Adapt

When tasks fail, document what happened. The next iteration reads these learnings and tries differently.

Successful patterns get promoted to the **Learnings section** of the progress file, so all future iterations benefit from discovered approaches.

### Tests Must Pass

Only mark a task complete when verification succeeds. Failed tests mean the task remains incomplete for the next iteration to continue.

This creates a tight feedback loop where problems are caught immediately, not at the end of a long implementation cycle.

### Watch the Loop

> "It's important to watch the loop as that is where your personal development and learning will come from."

When you see a failure domain:
1. Put on your engineering hat
2. Resolve the problem
3. Engineer a solution so it never happens again

## The Process

### Per Iteration

1. **Read Learnings First**: Check the progress file's Learnings section for patterns that work (commands, conventions, pitfalls)

2. **Find Next Task**: Locate the first uncompleted task in the plan file (format: `- [ ] **Task N.M: ...**`)

3. **Implement**: Complete all steps for that task only. Keep changes focused.

4. **Verify**: Run tests—must PASS before proceeding. If they fail, document why for the next iteration.

5. **Document**: Update both files:
   - **Plan**: Mark `- [x]`, add to Tracked Changes: `**[YYYY-MM-DD]** Iteration N: Task N.M brief`
   - **Progress**: Append iteration entry with Result (TASK_COMPLETE/TASK_FAILED), files changed, what worked/failed, and promote successful patterns to Learnings section

### Output Signals

Ralph Wiggum uses promise tags to communicate task status:
- `<promise>TASK_COMPLETE</promise>` - Task implemented and tests pass
- `<promise>TASK_FAILED</promise>` - Task attempted but verification failed
- `<promise>ALL_COMPLETE</promise>` - All tasks in plan completed

## File Structure

### Plan File

Contains the implementation roadmap:
```markdown
# Feature Implementation Plan

## Architecture
[Key decisions and patterns]

## Tasks
- [ ] **Task 1.1: Setup database schema**
- [ ] **Task 1.2: Create API endpoints**
- [x] **Task 1.3: Add validation** ✓

## Tracked Changes
**[2026-01-17]** Iteration 1: Task 1.3 completed
```

### Progress File

Maintains continuity across iterations:
```markdown
# Ralph Wiggum Implementation Progress

## Learnings

Patterns and insights that help future iterations succeed:
- Tests require `npm run build` before `npm test`
- Use `--watch` flag when developing to catch errors early
- Auth tests need TEST_USER env var set

---

## Iteration Log

### Iteration 1 - Task 1.3
- Result: TASK_COMPLETE
- Files: src/validators/user.ts, tests/user.test.ts
- What worked: Used existing validator pattern from auth module
- Learnings: Validator tests need mock data—added to Learnings above

### Iteration 2 - Task 1.4
- Result: TASK_FAILED
- Files: src/api/users.ts
- What failed: Missing database migration, tests couldn't connect
- Learnings: Check migrations before implementing DB-dependent features
```

## Philosophy

### Context Engineering

Ralph Wiggum is fundamentally about "getting the most out of how underlying models work through context engineering."

This pattern is **GENERIC and works for ALL TASKS**—not just software implementation. Whether building, testing, documenting, or analyzing, the loop + context engineering pattern applies universally.

### Deterministic Degradation

Ralph Wiggum produces identifiable, resolvable defects through systematic prompt tuning rather than unpredictable failures. Each misstep becomes calibration data for improving instructions.

When something doesn't work, the solution is to adjust the instructions (improve the Learnings section), not to abandon the approach.

### Faith in Eventual Consistency

Persistent iteration yields convergence toward objectives, despite intermediate failures. Each iteration is a calibration opportunity, not a final attempt.

Software is clay: when something isn't right, throw it back on the wheel and refine it.

## Three Operational Modes

Ralph Wiggum encompasses multiple ways of working:

### Forward Mode
Building autonomously
- Implement features while AFK (away from keyboard)
- Greenfield projects and feature development
- Let the loop construct software continuously

### Reverse Mode
Clean rooming
- Deconstructing and reconstructing existing systems
- Understanding through rebuilding
- Learning and refactoring

### Mindset Mode
How you think about development
- Software as malleable clay, not brittle bricks
- Loops as the fundamental development unit
- Context engineering as the core skill

## Usage

```bash
# Using the slash command
/claudehub:ralph [plan-file] [--max-iterations N] [--commit]

# Direct script usage
bash scripts/ralph-wiggum.sh /path/to/project 20
```

### Options

- `plan-file`: Path to the plan file (default: prompts to select from `.thoughts/plans/`)
- `--max-iterations N`: Maximum iterations to run (default: 10)
- `--commit`: Auto-commit when tasks complete successfully

### Automation Levels

**Manual**: Run iterations yourself through prompting
- Good for learning and understanding the pattern
- Full control and observation

**Semi-automated**: Script with pauses
- Balance between automation and oversight
- Press CTRL+C to continue to next iteration

**Fully automated**: Continuous loop
- Appropriate when patterns are well-established
- Maximum throughput for understood tasks

Even manual prompting is "ralphing" because it's about the context engineering pattern, not the automation level.

## The Future

> "Software development is dead. Software can now be developed cheaper than minimum wage and built autonomously while AFK."

Engineers who understand how to program LLMs through context engineering and loop design will thrive. Those still building Jenga stacks will not.

Ralph Wiggum represents a recognition that:
- LLMs are a new form of programmable computer
- Software engineers must learn to program this new computer
- The future belongs to those who understand loop-based development
- Traditional vertical building is obsolete

If you haven't built your own coding agent yet, that's the fundamental knowledge gap.

## References

- [Ralph Methodology](https://ghuntley.com/ralph/) - Original article by Geoffrey Huntley
- [Loop Philosophy](https://ghuntley.com/loop/) - The mindset shift behind Ralph Wiggum
- [Building Coding Agents](https://www.youtube.com/geoffreyhuntley) - Geoffrey Huntley's workshops
- `scripts/ralph-wiggum.sh` - Bash implementation script that manages the loop
