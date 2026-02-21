# Query-Type Strategies

Specialized search strategies for common research scenarios.

## API/Library Documentation

**Goal**: Find accurate, version-specific technical details.

### Search Approach
1. Start with official docs: `site:docs.{product}.com {feature}`
2. Find changelogs/release notes for version details
3. Locate official code examples from repositories

### Example Searches
- `site:docs.stripe.com payment intents`
- `{library} changelog v3.0`
- `site:github.com {org}/{repo} examples`

### Source Priorities
1. Official documentation
2. Official GitHub repos/examples
3. API reference pages
4. Official blog posts

### Watch For
- Version mismatches (docs may be for different version)
- Deprecated features still appearing in search results
- Beta/experimental features marked as such

---

## Best Practices Research

**Goal**: Find consensus on recommended approaches.

### Search Approach
1. Search for best practices: `{topic} best practices 2025`
2. Search anti-patterns: `{topic} anti-patterns` or `{topic} mistakes to avoid`
3. Cross-reference multiple sources to identify consensus

### Example Searches
- `React state management best practices 2025`
- `API authentication anti-patterns`
- `database indexing common mistakes`

### Source Priorities
1. Official style guides/recommendations
2. Well-known tech blogs (ThoughtWorks, Martin Fowler, etc.)
3. Conference talks/presentations
4. Community consensus (multiple agreeing sources)

### Watch For
- Outdated recommendations (tech evolves quickly)
- Context-specific advice presented as universal
- Opinions vs. evidence-based practices

---

## Technical Solutions

**Goal**: Solve specific problems, debug errors.

### Search Approach
1. Use exact error messages in quotes: `"error message here"`
2. Include technology stack: `{error} React TypeScript`
3. Search GitHub issues: `site:github.com {repo} {error}`

### Example Searches
- `"Cannot read property 'map' of undefined" React`
- `site:github.com facebook/react issues state not updating`
- `CORS error localhost development`

### Source Priorities
1. GitHub issues (especially closed/resolved)
2. Stack Overflow (high-vote answers)
3. Official troubleshooting guides
4. Technical blog posts with solutions

### Watch For
- Solutions that worked for specific versions
- Workarounds vs. proper fixes
- Security implications of suggested solutions

---

## Comparative Analysis

**Goal**: Compare options, evaluate trade-offs.

### Search Approach
1. Direct comparisons: `X vs Y`
2. Migration guides: `migrate from X to Y`
3. Benchmarks: `X Y benchmark performance`

### Example Searches
- `Redux vs Zustand 2025`
- `migrate from Express to Fastify`
- `PostgreSQL vs MySQL performance benchmark`

### Source Priorities
1. Official migration guides
2. Benchmark studies with methodology
3. Comparison articles from neutral sources
4. Community discussions with real-world experience

### Watch For
- Bias (author may prefer one option)
- Outdated comparisons (features change)
- Context mismatch (enterprise vs. startup needs differ)
- Cherry-picked benchmarks
