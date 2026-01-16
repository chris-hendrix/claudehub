---
description: Search the web for a topic and save findings to a research doc
argument-hint: [topic]
allowed-tools: AskUserQuestion, Skill, Task, Write, Bash
---

## Important

- Always load referenced skills using the Skill tool
- When needing input from the user, always use AskUserQuestion tool

## Skills

- `researching-web` - Web research methodology

## Process

1. Parse topic from args (or ask user if not provided)

2. Spawn `web-searcher` agent via Task tool with the topic

3. Receive ranked URLs from searcher (top 5-8)

4. Spawn multiple `web-synthesizer` agents in parallel via Task tool (one per URL)

5. Wait for all synthesizers to complete

6. Aggregate findings from all synthesizers into a cohesive summary

7. Create `.thoughts/research/` directory if needed

8. Generate filename: `YYYY-MM-DD-<topic-slug>.md`

9. Write doc with frontmatter (date, topic) and aggregated findings with citations

10. Display path to user

Input: $ARGUMENTS
