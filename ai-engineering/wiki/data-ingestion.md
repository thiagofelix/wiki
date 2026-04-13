---
title: Data Ingestion
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Data Ingestion

Data ingestion is the process of getting source material into the raw/ folder of an [[llm-knowledge-bases|LLM Knowledge Base]]. The guiding principle is simple: dump everything in without organizing it. Don't rename, don't clean up — that's the AI's job during [[wiki-compilation]].

## What to Ingest

Anything that contains knowledge you want to preserve:
- Articles and blog posts (.md or .txt)
- Research papers and PDFs
- YouTube transcripts
- Meeting notes and recordings
- Project documentation
- Screenshots and diagrams
- Bookmarks you've been hoarding
- X/Twitter posts and threads
- Code repositories and READMEs

## Ingestion Methods

### Manual Copy-Paste
The simplest approach. Copy article text, paste into a .md file, save to raw/. Works but doesn't handle JavaScript-heavy sites or images well.

### Obsidian Web Clipper
Karpathy's preferred method. A Chrome extension that clips web articles directly into your [[obsidian|Obsidian]] vault as .md files. Setup:
1. Install the Obsidian Web Clipper extension in Chrome
2. In extension options, set the default folder to `raw/`
3. When viewing an article, click the extension → select your vault → click "Add to Obsidian"

The clipper preserves article structure and metadata. Karpathy also uses a hotkey to download related images locally so the LLM can reference them.

### Agent Browser (Automated Scraping)
[[agent-browser]] is a CLI tool that lets AI agents control a real browser. For knowledge bases, it handles pages that copy-paste can't: JavaScript-heavy sites, pages behind logins, content requiring scrolling or "load more" clicks.

```bash
agent-browser open https://some-article.com
agent-browser get text "article"
```

The AI opens the page, grabs the text, and pipes it into a file in raw/. Uses 82% fewer tokens than Playwright MCP, allowing 5-6x more pages per session.

### YouTube Transcripts
Transcripts can be extracted and saved directly as text files in raw/. [[claude-code|Claude Code]] can be instructed to fetch transcripts and save them. [[source-herk-llm-wiki-setup|Nate Herk]] batch-ingested 36 YouTube transcripts in one go.

### Batch Ingestion
You can drop multiple sources into raw/ at once and tell the LLM to ingest everything. Batch processing of 36 YouTube transcripts took ~14 minutes. A single article takes ~10 minutes.

## After Ingestion

Once sources are in raw/, tell the LLM to ingest them:
> "I just added [description] to raw/. Please ingest it into the wiki."

The LLM may ask clarifying questions about:
- What to emphasize from the source
- How granular to be
- What your focus or interests are
- How this relates to the overall project

These questions help it produce better [[wiki-compilation|wiki articles]].

## Related

- [[llm-knowledge-bases]] — The overall system
- [[folder-structure]] — Where ingested sources live
- [[wiki-compilation]] — What happens after ingestion
- [[agent-browser]] — Automated scraping tool
- [[obsidian]] — Frontend with web clipper
