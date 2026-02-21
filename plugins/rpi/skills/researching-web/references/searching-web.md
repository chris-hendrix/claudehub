# Searching the Web

Methodology for analyzing queries and conducting strategic searches.

## Output Format

When conducting web research, return ranked URLs as a numbered list:

```
1. [Title](URL)
   Snippet describing the content...

2. [Title](URL)
   Snippet describing the content...
```

Return top 5-8 most relevant results after deduplication and ranking by relevance and source authority.

## Query Analysis

Before searching, deconstruct the user's request:

1. **Identify core concepts** - What are the key technical terms?
2. **Determine source types** - What kind of sources will have this information?
   - Official documentation
   - Technical blogs/articles
   - Q&A sites (Stack Overflow)
   - GitHub issues/discussions
3. **Plan multiple angles** - How else might this topic be described?
   - Alternative terminology
   - Related concepts
   - Broader/narrower scope

### Example Analysis

Request: "How do I validate webhook signatures in Stripe?"

- **Core concepts**: webhook, signature, validation, Stripe
- **Source types**: Stripe docs (primary), implementation examples
- **Multiple angles**:
  - "Stripe webhook signature verification"
  - "Stripe webhook security"
  - "verify Stripe webhook payload"

## Strategic Searches

### Search Progression

1. **Broad first** - Understand the landscape
   - `Stripe webhook signature verification`
2. **Refine** - Add specificity based on initial results
   - `Stripe webhook signature verification Node.js`
3. **Target** - Use site-specific queries for authoritative sources
   - `site:docs.stripe.com webhook signature`

### Search Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `"exact phrase"` | Match exact text | `"webhook signature verification"` |
| `site:domain` | Limit to domain | `site:docs.stripe.com` |
| `-term` | Exclude term | `webhook -discord` |
| `filetype:ext` | File type | `filetype:pdf security guide` |

### Site-Specific Targeting

For common source types:

| Source Type | Pattern |
|-------------|---------|
| Official docs | `site:docs.{product}.com` |
| GitHub repos | `site:github.com {repo} {topic}` |
| Stack Overflow | `site:stackoverflow.com {topic}` |
| API references | `site:api.{product}.com` or `{product} API reference` |

## Search Efficiency

- Start with 2-3 well-crafted searches before fetching pages
- Review search result snippets to identify most promising links
- If initial searches miss the mark, refine based on terminology found
- Fetch only the most promising 3-5 pages initially
