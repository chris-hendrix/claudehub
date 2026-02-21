---
description: Validate that Ralph verification environment and test suites are working
allowed-tools: ["Bash", "Task"]
---

# Validate

Run smoke tests to verify that test suites and environment in VERIFICATION.md are working properly.

## Process

1. **Check if VERIFICATION.md exists**:
   ```bash
   test -f .ralph/VERIFICATION.md && echo "EXISTS" || echo "NOT_FOUND"
   ```

2. **If VERIFICATION.md doesn't exist**:
   - Tell user: "No VERIFICATION.md found. Run `/ralph:plan` or `/ralph:plan-deep` first to create planning docs."
   - Stop

3. **Launch the ralph-validator agent**:
   ```
   Use the Task tool with:
   - subagent_type: "ralph:ralph-validator"
   - description: "Validate Ralph environment"
   - prompt: "Validate that the test suites and environment in .ralph/VERIFICATION.md are working. Run smoke tests for each test command, check URL accessibility, and take screenshots if frontend is involved."
   ```

4. **After validation completes**:
   - Display the agent's results
   - If failures found, suggest: "Review the validation results above. Fix any issues before running `/ralph:run`."
   - If all passed, confirm: "Validation passed! Ready to run `/ralph:run`."

## Examples

```bash
# Validate environment before starting Ralph
/ralph:validate

# After fixing issues, validate again
/ralph:validate
```
