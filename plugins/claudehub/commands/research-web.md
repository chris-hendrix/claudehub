---
description: Search the web for a topic and save findings to a research doc
argument-hint: [topic]
allowed-tools: AskUserQuestion, Skill, WebSearch, WebFetch, Write, Bash
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `claudehub:researching-web` - Web research methodology (see references for search strategy and synthesis format)

## Process

1. Gather topic from input

2. Execute strategic web searches and rank results

3. Fetch and synthesize findings from top URLs in parallel

4. Aggregate findings into cohesive summary with citations

5. Save to `.thoughts/research/YYYY-MM-DD-<topic-slug>.md`

Input: $ARGUMENTS
