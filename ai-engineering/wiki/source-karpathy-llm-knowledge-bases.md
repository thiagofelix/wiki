---
title: "Source: Karpathy — LLM Knowledge Bases"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Karpathy — LLM Knowledge Bases

Andrej Karpathy's X post from April 2, 2026 introduced the concept of [[llm-knowledge-bases]] to a massive audience (18.7M views, 54K likes, 98K bookmarks). It describes how he redirected his LLM usage from coding to knowledge curation, using raw documents compiled by an LLM into an interlinked markdown wiki.

## Metadata

- **Author:** Andrej Karpathy (@karpathy)
- **Platform:** X (Twitter)
- **Date:** April 2, 2026
- **URL:** https://x.com/karpathy/status/2039805659525644595
- **Stats:** 18.7M views, 8,210 reposts, 54,015 likes, 98,570 bookmarks
- **Raw file:** `raw/karpathy-llm-knowledge-bases.md`

## Key Contributions

This post defined the core architecture and vocabulary that all subsequent guides build on:

- **[[folder-structure]]** — raw/ for sources, wiki/ for compiled output
- **[[wiki-compilation]]** — LLM as a "compiler" turning raw docs into interlinked .md files
- **[[obsidian]]** — Recommended as the IDE/frontend with Web Clipper for ingestion
- **[[health-checks-and-linting]]** — LLM health checks for data integrity
- **[[compounding-knowledge]]** — Filing outputs back to enhance the wiki
- **[[llm-wiki-vs-rag]]** — "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files"
- **[[schema-files]]** — Keeping the schema "super simple and flat" in an AGENTS.md file

## Notable Quotes

> "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge."

> "You rarely ever write or edit the wiki manually, it's the domain of the LLM."

> "I think there is room here for an incredible new product instead of a hacky collection of scripts."

## Future Directions Mentioned

- Synthetic data generation + finetuning to have the LLM "know" data in its weights
- Vibe-coded search engine over the wiki (web UI + CLI tool for LLM)
- Marp slideshows and matplotlib visualizations as output formats

## Impact

This post triggered a wave of implementations, guides ([[source-spisak-second-brain|Nick Spisak]]), video tutorials ([[source-herk-llm-wiki-setup|Nate Herk]]), and community discussion. People on X called it a "game changer" for making AI feel like a colleague that remembers everything.
