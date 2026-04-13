---
title: Wiki Compilation
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Wiki Compilation

Wiki compilation is the core process of an [[llm-knowledge-bases|LLM Knowledge Base]] where the LLM reads everything in the raw/ folder and produces an organized, interlinked wiki of markdown files. The LLM acts as a "compiler" — transforming unstructured source material into structured knowledge with summaries, backlinks, concept articles, and cross-references.

## How It Works

1. **Read the [[schema-files|schema]]** — The LLM loads CLAUDE.md to understand the project's rules and structure
2. **Scan raw/** — Read all source documents (articles, transcripts, notes, images)
3. **Create INDEX.md** — Build a master index listing every topic with a one-line description
4. **Generate topic articles** — Create one .md file per major concept, entity, or theme
5. **Add backlinks** — Link related topics to each other using `[[topic]]` format
6. **Summarize sources** — Each wiki article includes summaries of the raw sources it draws from

## What the LLM Produces

From a single article, the LLM might generate 5–25 wiki pages depending on the richness of the source. [[source-herk-llm-wiki-setup|Nate Herk]] showed that ingesting one article (AI2027) produced 23 wiki pages covering people, organizations, AI systems, technical concepts, geopolitical analysis, and source summaries — all automatically related.

A typical wiki includes:
- **Concept articles** — Explaining ideas, techniques, frameworks
- **Entity articles** — People, organizations, tools
- **Source summaries** — Metadata and key takeaways from each raw file
- **Analysis articles** — Cross-cutting themes, comparisons, gap analyses

## Incremental Compilation

The wiki is not rebuilt from scratch each time. When new sources are added to raw/, the LLM:
- Reads the new source
- Updates existing wiki articles with new information
- Creates new articles for previously unseen concepts
- Updates INDEX.md
- Logs the operation in LOG.md

This incremental approach means the wiki grows organically. Each ingest makes the next one smarter because the LLM has more context about what already exists.

## The Compilation Prompt

The standard prompt (from [[source-spisak-second-brain|Nick Spisak]]):

> "Read everything in raw/. Then compile a wiki in wiki/ following the rules in CLAUDE.md. Create an INDEX.md first, then create one .md file per major topic. Link related topics. Summarize every source."

## Timing

- Single article ingest: ~10 minutes
- Batch of 36 YouTube transcripts: ~14 minutes
- The LLM may ask clarifying questions during ingest about focus areas, granularity, and emphasis

## Related

- [[llm-knowledge-bases]] — The overall system
- [[folder-structure]] — Where compiled output lives
- [[schema-files]] — Rules governing compilation
- [[data-ingestion]] — The preceding step
- [[compounding-knowledge]] — The feedback loop after compilation
