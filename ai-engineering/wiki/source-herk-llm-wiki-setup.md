---
title: "Source: Nate Herk — LLM Wiki Setup Tutorial"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Nate Herk — LLM Wiki Setup Tutorial

Nate Herk's YouTube video is a practical walkthrough of setting up [[source-karpathy-llm-knowledge-bases|Karpathy's LLM Knowledge Base]] system using [[obsidian|Obsidian]] and [[claude-code|Claude Code]]. It demonstrates the full process from creating a vault to ingesting an article and watching the graph view populate in real time, and includes a comparison of [[llm-wiki-vs-rag|LLM Wiki vs. traditional RAG]].

## Metadata

- **Author:** Nate Herk
- **Platform:** YouTube
- **Video ID:** sboNwYmH3AY
- **Raw file:** `raw/sboNwYmH3AY-transcript.txt`

## Key Contributions

### Live Demo
- Created an Obsidian vault from scratch
- Pasted Karpathy's idea file into Claude Code
- Claude Code created raw/, wiki/, INDEX.md, LOG.md, and subfolder structure
- Ingested the AI2027 article → Claude Code generated 23 wiki pages in ~10 minutes
- Showed the graph view populating in real time with hubs and relationship clusters

### Two Vault Examples

1. **YouTube Transcript Vault** — 36 videos organized into an interconnected knowledge system. Categorized subfolders (concepts/, entities/, sources/). Used for content research and querying patterns across videos.

2. **Personal Second Brain ("Herk Brain")** — Meeting recordings, business docs, ClickUp summaries, personal notes. Flat structure (no subfolders). Connected to an executive assistant agent.

### Hot Cache Concept
Introduced **hot.md** — a ~500 word file caching the most recent context. The executive assistant reads this first before crawling the full wiki, saving tokens on routine interactions.

### Cross-Project Wiki Access
Demonstrated pointing one project's [[schema-files|CLAUDE.md]] at another project's wiki path. His executive assistant's schema includes: "Whenever you need to read things about me and my business, go to my herkbrain vault."

### LLM Wiki vs. RAG Comparison
Generated a comparison chart showing:
- Wiki uses index navigation + backlinks vs. similarity search
- Infrastructure: just markdown vs. embedding model + vector DB + chunking
- Cost: tokens only vs. ongoing compute + storage
- Scale limit: hundreds of pages vs. millions of documents
- Verdict: wiki wins for personal scale, RAG needed for enterprise

### Practical Tips
- Set Obsidian Web Clipper default folder to `raw/`
- Give the LLM context about the project's purpose before first ingest
- Karpathy prefers "super simple and flat" structure — no over-organizing
- Batch ingest of 36 transcripts took ~14 minutes
- One X user reported 95% token reduction after switching to wiki format

### Token Efficiency Claim
"One X user turned 383 scattered files and over 100 meeting transcripts into a compact wiki and dropped token usage by 95% when querying with Claude."

## Notable Quotes

> "Normal AI chats are ephemeral — knowledge disappears after the conversation. But this method makes knowledge compound like interest in a bank."

> "There's not really a GitHub repo you go copy. You literally just say 'hey Claude Code, read this idea from Karpathy and implement it.'"

> "This is how 2026 AI agentic software and products will be made. You just give it a high-level idea and it goes and builds it out."
