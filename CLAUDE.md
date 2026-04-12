# LLM Wiki

A personal knowledge base maintained by an LLM. The human curates sources, directs analysis, and asks questions. The LLM does the summarizing, cross-referencing, filing, and bookkeeping.

## Structure

Each research topic is a self-contained top-level folder:

```
<topic>/
  raw/            # Source documents (articles, papers, notes, images). Immutable — never modify.
  wiki/           # LLM-generated markdown pages. The LLM owns this entirely.
    index.md      # Catalog of all wiki pages in this topic.
    log.md        # Chronological record of operations.
    ...           # Entity pages, concept pages, summaries, etc.
  outputs/        # Finished artifacts — slide decks, reports, comparisons, charts.
```

### Creating a new topic

When the user asks to start a new topic:

1. Create the folder structure: `<topic>/raw/`, `<topic>/wiki/`, `<topic>/outputs/`
2. Create `<topic>/wiki/index.md` with an empty page list
3. Create `<topic>/wiki/log.md` with a header
4. If the topic needs special conventions, create `<topic>/wiki/_schema.md` to document them

Use lowercase kebab-case for topic folder names (e.g., `ai-safety`, `trip-japan`, `book-dune`).

## Page format

All wiki pages use this format:

```markdown
---
title: Page Title
type: <entity|concept|summary|comparison|overview|synthesis>
sources:
  - raw/filename.md
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

Page content here. Use [[wikilinks]] for cross-references within the topic.
```

- Use wikilinks (`[[page-name]]`) for links between wiki pages in the same topic.
- Use standard markdown links for links to raw sources or cross-topic references.
- Keep page filenames lowercase kebab-case matching the title.

## Operations

### Ingest

When the user provides a new source for a topic:

1. Confirm which topic it belongs to.
2. Save/verify the source exists in `<topic>/raw/`.
3. Read the source fully.
4. Discuss key takeaways with the user.
5. Create or update wiki pages:
   - Write a summary page for the source.
   - Update existing entity/concept pages with new information.
   - Create new entity/concept pages as needed.
   - Flag contradictions with existing wiki content explicitly.
6. Update `<topic>/wiki/index.md` — add new pages, update descriptions of modified pages.
7. Append to `<topic>/wiki/log.md`.

A single source may touch many wiki pages. That is expected and desired.

### Query

When the user asks a question about a topic:

1. Read `<topic>/wiki/index.md` to find relevant pages.
2. Read the relevant pages.
3. Synthesize an answer with citations to wiki pages and raw sources.
4. If the answer is substantial and reusable, offer to file it as a new wiki page or output.

Answers can take many forms: markdown pages, comparison tables, slide decks (Marp), charts, diagrams. Finished artifacts go in `<topic>/outputs/`.

### Lint

When the user asks to health-check a topic (or periodically suggest it):

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps — suggest sources to look for or web searches to run

## index.md format

```markdown
# Index

## Entities
- [[page-name]] — one-line description

## Concepts
- [[page-name]] — one-line description

## Sources
- [[source-summary]] — one-line description (from: raw/filename.md)

## Syntheses
- [[page-name]] — one-line description
```

Group pages by type. Keep descriptions to one line. Update on every ingest.

## log.md format

Each entry uses a parseable heading:

```markdown
## [YYYY-MM-DD] <operation> | <description>

Details of what was done: pages created, pages updated, key findings.
```

Operations: `ingest`, `query`, `lint`, `update`, `output`.

Example:
```markdown
## [2026-04-12] ingest | "Attention Is All You Need" (Vaswani et al.)

- Created: [[attention-paper-summary]]
- Updated: [[transformer]], [[self-attention]], [[encoder-decoder]]
- New page: [[multi-head-attention]]
- Contradiction noted: previous claim in [[rnn]] about sequence modeling dominance revised.
```

## Guidelines

- The user never (or rarely) writes wiki pages directly. The LLM writes and maintains all of it.
- Raw sources are immutable. Never edit files in `raw/`.
- When in doubt about which topic something belongs to, ask the user.
- Prefer updating existing pages over creating new ones for the same concept.
- When a wiki page grows too large, split it into focused sub-pages and link them.
- Always preserve existing information when updating pages — add to it, don't replace unless correcting errors.
- Cross-topic references: use relative markdown links (`../other-topic/wiki/page.md`). Use sparingly — most knowledge should live within its topic.
