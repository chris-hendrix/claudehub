# Deep-Dive Questioning

Reference for the `/ralph:deep-plan` command's confidence-building process.

## Confidence Requirement

**You MUST reach 90% confidence before writing any planning documents.**

After each round of questions, report your current confidence level to the user:
- "Current confidence: X% - I still need to understand [specific gaps]"
- Keep asking questions until you reach 90%+ confidence
- Be thorough - don't be shy about asking clarifying questions
- It's better to ask too many questions than to make wrong assumptions

Confidence should reflect your certainty that:
- You understand ALL acceptance criteria and functional requirements
- You know the exact technical approach for each requirement
- You've identified all edge cases and error scenarios
- You understand how this integrates with existing code
- You can break this into atomic, verifiable tasks
- **You know what tests will prove each requirement works** (TDD mindset)

## Question Categories

Ask questions aggressively in each category until gaps are filled.

### Requirements Clarity

- What exactly does [ambiguous term] mean?
- What happens when [edge case]?
- Is [assumption] correct?
- What's the expected behavior for [scenario]?
- What error messages should the user see?
- What are the success/failure states?

### Technical Decisions

- Should this use [pattern A] or [pattern B]?
- Where should [component] live in the codebase?
- What existing code should this integrate with?
- Are there performance requirements?
- What's the data model / schema changes?
- How does this affect existing APIs?

### Scope Boundaries

- Is [feature] in or out of scope?
- What's the MVP vs nice-to-have?
- Are there related changes we should NOT make?
- What can be deferred to a follow-up?
- Are there dependencies on other teams/services?

### Feature Flags & Third-Party Setup

- Does this feature need a feature flag? (e.g., Flagsmith, LaunchDarkly)
- What flags need to be enabled in dev/staging environments?
- Are there third-party services that need configuration? (API keys, webhooks, etc.)
- Do any external dashboards need setup before development can proceed?
- What credentials/accounts are needed?

### Testing & Verification (TDD Mindset)

- For each requirement, what test would prove it works?
- What are the unit test boundaries for this feature?
- What integration points need test coverage?
- For UI features: what E2E test scenarios prove the flow works?
- What edge cases need automated test coverage?
- What manual verification is needed that can't be automated?
- What test data/fixtures are required?

## Confidence Progression

After each question round, state:
> "Current confidence: X%. [Reason for gaps if below 90%]"

Example progression:
- 30% - "I understand the high-level goal but not the edge cases or technical approach"
- 50% - "Requirements are clearer, but I'm unsure about integration points and testing strategy"
- 70% - "Technical approach is solid, still need clarity on [specific gaps]"
- 90% - "Ready to write planning docs. Remaining 10% will be discovered during implementation."

Continue until reaching 90%+ confidence, then proceed to writing planning documents.
