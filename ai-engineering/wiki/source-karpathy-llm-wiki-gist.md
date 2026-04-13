---
title: "Source: LLM Wiki Gist (Karpathy)"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: LLM Wiki Gist (Karpathy)

Andrej Karpathy's detailed gist expanding on his viral X post about [[llm-knowledge-bases|LLM knowledge bases]]. This document is "intentionally abstract" — describing the pattern rather than a specific implementation, designed to be shared with an LLM agent that builds out the specifics.

## Metadata

- **Author:** Andrej Karpathy
- **Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Raw file:** `raw/llm-wiki.md`

## The Core Idea

Instead of RAG (retrieving and re-deriving knowledge on every query), the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files. When new sources arrive, the LLM reads them, extracts key information, and integrates it into existing pages. "The wiki is a persistent, compounding artifact."

> "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions."

## Three-Layer Architecture

1. **Raw sources** — Immutable collection of articles, papers, images, data files. LLM reads but never modifies. Source of truth.
2. **The wiki** — LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons. LLM owns this layer entirely.
3. **The schema** — CLAUDE.md/AGENTS.md telling the LLM how the wiki is structured. You and the LLM co-evolve this over time.

## Operations

- **Ingest**: Drop source into raw/, LLM processes it, writes summary, updates index, touches 10-15 existing pages. Can be supervised or batch.
- **Query**: Ask questions, LLM searches wiki via index, synthesizes answers with citations. Good answers filed back as new pages — explorations compound.
- **Lint**: Periodic health checks for contradictions, stale claims, orphan pages, missing cross-references, data gaps.

## Indexing and Logging

- **index.md**: Content-oriented catalog of every page with links and one-line summaries. LLM reads index first when querying. Works at ~100 sources without RAG infrastructure.
- **log.md**: Chronological append-only record. Parseable with unix tools.

## The Memex Connection

Related to Vannevar Bush's Memex (1945) — a personal knowledge store with associative trails between documents. Bush's vision was private and actively curated. The missing piece was maintenance — LLMs handle that.

## Use Cases

Personal (goals, health, self-improvement), research (papers, evolving thesis), reading companion (character/theme wiki), business (Slack, transcripts, project docs), competitive analysis, course notes, hobby deep-dives.

## Related

- [[llm-knowledge-bases]] — The broader concept
- [[source-karpathy-llm-knowledge-bases]] — The original X post
- [[llm-wiki-vs-rag]] — Why this outperforms RAG at moderate scale
- [[compounding-knowledge]] — The query-and-file-back loop
- [[schema-files]] — The configuration layer
- [[health-checks-and-linting]] — The lint operation
