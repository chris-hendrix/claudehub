---
name: researching-web
disable-model-invocation: true
description: This skill should be used when searching the web for information, researching topics online, finding documentation, looking up technical solutions, or gathering information from external sources.
version: 1.0.0
allowed-tools: WebSearch, WebFetch
---

# Researching Web

Methodology for conducting effective web research and synthesizing findings.

## Philosophy

- **Accuracy first** - Verify claims across multiple sources before presenting
- **Always cite** - Every finding must link back to its source
- **Source hierarchy** - Official docs > reputable technical sources > community content
- **Currency awareness** - Note publication dates; flag potentially outdated information
- **Multi-angle coverage** - Explore topics from multiple search angles for completeness

## Critical: Check Current Versions

**LLM knowledge is often outdated.** When researching libraries, frameworks, or tools:

1. **Always search for current version** - Add "2025" or "latest" to queries
2. **Check official docs first** - `site:docs.{library}.com` or `site:{library}.dev`
3. **Look for migration guides** - New versions often have different patterns
4. **Verify best practices** - What was recommended 2 years ago may be deprecated

**Examples of outdated patterns:**
- React: Class components → Hooks → Server Components
- ESLint: `.eslintrc` → Flat config (`eslint.config.js`)
- Node.js: CommonJS (`require`) → ESM (`import`)
- Next.js: Pages Router → App Router

Always include version information in findings and note when patterns have changed.

## Research Types

| Type | Purpose | Tools |
|------|---------|-------|
| **Searching** | Find relevant sources | WebSearch |
| **Synthesizing** | Extract and organize findings | WebFetch |

Choose the appropriate type based on what's needed. They are typically combined: search first, then synthesize from the best results.

## Workflow Overview

1. **Query Analysis** - Deconstruct request, identify key terms, plan multiple search angles
2. **Strategic Searches** - Broad to specific, use site-specific targeting, vary query phrasing
3. **Content Retrieval** - Fetch most promising results, prioritize authoritative sources
4. **Synthesis** - Organize by relevance, cite sources, highlight conflicts, note gaps

See [searching-web](references/searching-web.md) for steps 1-2 and [synthesizing-page](references/synthesizing-page.md) for steps 3-4.

For query-type-specific strategies, see [query-strategies](references/query-strategies.md).

## Output Structure

Structure findings by purpose:

| Section | Content |
|---------|---------|
| Summary | 2-3 sentence key takeaways |
| Detailed Findings | Topic sections with source attribution |
| Sources | Links with descriptions |
| Gaps/Limitations | Unresolved questions, outdated info |

Always include source links. Flag conflicting information explicitly.
