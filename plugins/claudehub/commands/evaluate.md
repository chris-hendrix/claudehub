---
description: Assess output across the most relevant dimensions for impact
argument-hint: [artifact or content to evaluate]
allowed-tools: Read, Glob, AskUserQuestion, Write, Skill, Task
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `evaluating` - dimension selection, evaluation format, revision methodology
- `researching-codebase` - investigate artifacts in the codebase before evaluation
- `writing-documentation` - file naming and frontmatter for saving evaluations

## Process

1. Gather context from input (if unclear)

2. Propose 5-7 dimensions with reasoning, get user confirmation

3. Evaluate dimensions in parallel (spawn agent per dimension)

4. Synthesize results into final evaluation

5. Save to `.thoughts/evaluations/YYYY-MM-DD-{artifact-name}-evaluation.md`

6. Offer to show 10/10 version or red-team the evaluation

Input: $ARGUMENTS
