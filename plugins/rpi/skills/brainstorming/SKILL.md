---
name: brainstorming
description: This skill should be used when creating or developing, before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Don't use during clear 'mechanical' processes.
version: 1.0.0
---

# Brainstorming Ideas Into Designs

Turn rough ideas into fully formed designs through natural collaborative dialogue.

## Purpose

Brainstorming is about **exploring alternatives and making an informed decision**, not creating detailed implementation plans. The key outputs are:
- Understanding what currently exists (codebase/dependencies)
- Evaluating 2-3 different approaches with trade-offs
- Choosing the best approach with clear rationale

**Do not conflate with planning** - detailed architecture, component design, and implementation steps belong in the plan (created with `/rpi:plan`). The brainstorm focuses on the decision of *which* approach to take, not *how* to implement it.

## Research

Brainstorming typically involves research to inform the alternatives:

**Codebase research** (use `researching-codebase` skill):
- When modifying existing features
- To understand current patterns and architecture
- To identify reusable components

**Web research** (use `researching-web` skill):
- When evaluating new libraries or frameworks
- When choosing dependencies for the project
- To understand API capabilities and limitations
- To find best practices for new integrations
- **CRITICAL**: Always research current best practices and latest recommendations when choosing dependencies or technical approaches - LLM knowledge cutoff means you may be unaware of newer, better options or deprecated approaches
- Search for recent comparisons, official docs, and community consensus (e.g., "best React state management 2026", "modern authentication libraries comparison")
- Verify that chosen dependencies are actively maintained and compatible with current project versions

Research both when the task involves integrating new technologies into an existing codebase.

## Principles

- **One question at a time** - Don't overwhelm with multiple questions. Each answer informs the next question.
- **Multiple choice preferred** - Bounded options accelerate decisions. Open-ended is fine for exploratory topics.
- **Research before recommending** - When choosing dependencies, libraries, or technical approaches, research current best practices and recent recommendations. Don't rely solely on potentially outdated LLM knowledge.
- **YAGNI ruthlessly** - Challenge every feature. Remove unnecessary complexity from all designs.
- **Minimal code examples** - Brainstorming is about concepts and decisions, not implementation. Only show code when absolutely necessary to illustrate a specific point. Use brief snippets (5-10 lines max) or pseudo-code. Focus on architecture and trade-offs, not syntax.
- **Explore alternatives** - Always consider 2-3 approaches before settling on one.
- **Incremental validation** - Present design in sections, validate each before continuing.
- **Be flexible** - Go back and clarify when something doesn't make sense.

## Understanding the Objective

**Before exploring alternatives, you must understand:**

1. **The Objective** - What are we trying to achieve? (Could be solving a problem, adding a feature, making a strategic decision, etc.)
2. **Success Criteria** - What does success look like? How will we know if this works?

**Get explicit user confirmation** on both before proceeding. If you misunderstand the objective or what success looks like, all subsequent work is wasted.

Present your understanding of the objective and success criteria, then ask: "Does this accurately capture what we're trying to achieve?"

## Questioning

Focus on understanding purpose, constraints, and context. Prefer multiple choice questions - they're easier to answer and keep momentum. Reserve open-ended questions for genuinely exploratory topics.

Sequential questioning maintains focus. Avoid question dumps.

## Exploring Approaches

Present 2-3 different approaches with their trade-offs. Lead with the recommended option and explain why. Frame trade-offs conversationally.

**When approaches involve dependencies or libraries**: Research current best practices and recent recommendations before presenting options. Don't rely solely on LLM knowledge - verify through web search what the community currently recommends.

Common approach patterns:
- **Minimal** - Smallest viable solution (quick validation, low risk)
- **Balanced** - Pragmatic middle ground (most use cases)
- **Comprehensive** - Full-featured solution (long-term investment)

## Presenting Designs

Break designs into digestible sections (200-300 words each). Validate understanding after each segment before proceeding. Cover architecture, components, data flow, error handling, and testing as relevant.

## Document Template

See [brainstorm-template.md](references/brainstorm-template.md) for the standard structure when saving brainstorms to `.thoughts/brainstorms/YYYY-MM-DD-<topic>.md`.