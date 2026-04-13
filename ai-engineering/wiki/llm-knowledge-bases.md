---
title: LLM Knowledge Bases
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# LLM Knowledge Bases

LLM Knowledge Bases are a paradigm for using large language models to build, maintain, and query personal knowledge systems stored as plain markdown files and images. Popularized by Andrej Karpathy in April 2026, the approach replaces scattered notes, bookmarks, and documents with a structured wiki that an LLM incrementally compiles and enhances — turning raw information into organized, interlinked knowledge that compounds over time.

## The Core Idea

Instead of using LLMs primarily for code generation, you redirect token throughput toward **knowledge manipulation**. You collect raw source material (articles, papers, transcripts, repos, datasets, images) into a folder, then instruct an LLM to "compile" that material into a wiki of markdown files with summaries, backlinks, concept articles, and cross-references.

The key insight: **you rarely edit the wiki by hand**. The LLM writes and maintains everything. You read it, query it, and the LLM keeps it current.

## Architecture

The system follows a simple [[folder-structure]]:
- **raw/** — Unprocessed source material (the "junk drawer")
- **wiki/** — LLM-maintained organized wiki with interlinked .md files
- **outputs/** — Generated reports, answers, analyses

A [[schema-files|schema file]] (CLAUDE.md or AGENTS.md) in the project root tells the LLM the rules for organizing the wiki.

## Workflow Stages

1. **[[data-ingestion|Data Ingest]]** — Collect sources into raw/ via copy-paste, [[obsidian|Obsidian Web Clipper]], or [[agent-browser]]
2. **[[wiki-compilation|Compilation]]** — LLM reads raw/ and produces interlinked wiki articles
3. **Q&A** — Ask complex questions against the wiki; the LLM researches answers across all articles
4. **Output** — Render answers as markdown, slideshows (Marp), or visualizations
5. **[[health-checks-and-linting|Linting]]** — Periodic health checks for inconsistencies, gaps, and new connections
6. **[[compounding-knowledge|Compounding]]** — File outputs back into the wiki so every interaction adds up

## Why It Works

- **No infrastructure needed** — Just folders and text files. No vector database, no embeddings, no chunking pipeline. See [[llm-wiki-vs-rag]]
- **Compounding returns** — Every query and exploration enriches the wiki for future use
- **LLM-native** — Modern LLMs are good at maintaining index files and navigating ~100 articles / ~400K words without fancy RAG
- **Interoperable** — Plain files work with any tool: [[claude-code]], [[obsidian]], VS Code, terminal

## Scale Considerations

Karpathy's system works well at personal scale (~100 articles, ~400K words). At this size, the LLM can auto-maintain indexes and find relevant data without vector search. For enterprise scale (millions of documents), traditional [[llm-wiki-vs-rag|RAG pipelines]] are still necessary.

## Origins

The concept was introduced by [[source-karpathy-llm-knowledge-bases|Andrej Karpathy on X]] (Apr 2, 2026) and quickly went viral (18.7M views, 98K bookmarks). [[source-spisak-second-brain|Nick Spisak]] wrote a detailed step-by-step implementation guide, and [[source-herk-llm-wiki-setup|Nate Herk]] published a video walkthrough showing the setup process with Obsidian and Claude Code.

## Related

- [[folder-structure]] — The three-folder architecture
- [[schema-files]] — How to write the instruction file
- [[wiki-compilation]] — The compilation process
- [[compounding-knowledge]] — The feedback loop
- [[llm-wiki-vs-rag]] — Comparison with RAG
