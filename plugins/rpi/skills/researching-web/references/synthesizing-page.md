# Synthesizing Web Pages

Methodology for retrieving content and synthesizing findings.

## Content Retrieval

### Prioritizing Sources

From search results, prioritize pages to fetch:

| Priority | Source Type | Rationale |
|----------|-------------|-----------|
| 1 | Official documentation | Authoritative, accurate |
| 2 | Official blogs/announcements | Context, rationale |
| 3 | Reputable tech publications | Quality explanations |
| 4 | Stack Overflow (high votes) | Practical solutions |
| 5 | Community blogs | Varied perspectives |
| 6 | Forums/discussions | Edge cases, gotchas |

### Using WebFetch

- Fetch 3-5 most promising pages initially
- Read full content, not just snippets
- If a page redirects, fetch the redirect URL
- If content is behind authentication, note the limitation

### Extraction Focus

When reading fetched content, extract:

1. **Direct answers** - Exactly what the user asked
2. **Code examples** - Working implementations
3. **Caveats/warnings** - Known issues, limitations
4. **Version information** - What version this applies to
5. **Publication date** - When was this written?

## Synthesis

### Organizing Findings

Structure extracted information by:

1. **Relevance** - Most directly answering the question first
2. **Authority** - Official sources weighted higher
3. **Recency** - Recent information for evolving topics
4. **Consensus** - Where multiple sources agree

### Citation Format

Always attribute findings to sources:

```
According to [Stripe's webhook documentation](https://docs.stripe.com/webhooks):
> "You should verify webhook signatures to ensure..."
```

Include:
- Source name
- Direct link
- Publication date when relevant
- Direct quote when appropriate

### Handling Conflicts

When sources disagree:

1. **Identify the conflict** - State what differs
2. **Consider authority** - Official docs usually win
3. **Check dates** - Newer may supersede older
4. **Present both** - When conflict is unresolved

Example:
> Official docs recommend X, but Stack Overflow answers (2023) suggest Y may work better for high-volume scenarios.

### Identifying Gaps

Note when research is incomplete:

- **Outdated info** - "Most recent information found is from 2022"
- **Missing details** - "Could not find guidance on edge case X"
- **Conflicting without resolution** - "Sources disagree on best practice"
- **Scope limitations** - "Information specific to Node.js; other languages not covered"

## Synthesis Template

```markdown
## Summary
[2-3 sentence overview of key findings]

## Findings

### [Topic 1]
[Information with source attribution]

### [Topic 2]
[Information with source attribution]

## Sources
- [Source Name](url) - Description of what this source covers
- [Source Name](url) - Description

## Gaps/Limitations
- [What could not be definitively answered]
```
