---
description: Create a GitHub issue with AI-generated content
allowed-tools: Bash, AskUserQuestion, Skill, Read, Glob
---

IMPORTANT: Load referenced skills using the Skill tool.

## Skills

- `github` - Git/GitHub workflow, branch naming, and PR conventions

## Process

1. Gather input from user (use AskUserQuestion if unclear)
   - Issue type (bug, feature, task)
   - Brief description or problem statement
   - Optional: additional context

2. Check for issue templates in `.github/ISSUE_TEMPLATE/` or plugin templates

3. Generate issue title and description based on user input following appropriate template format:
   - Bug report: description, steps to reproduce, expected vs actual behavior
   - Feature request: problem, proposed solution, alternatives
   - Task/Chore: description, context, acceptance criteria

4. Display the generated title and description to user

5. Use AskUserQuestion to confirm and optionally add labels/assignees

6. If confirmed, create issue using `gh issue create`

7. Show issue URL and number

Input: $ARGUMENTS
