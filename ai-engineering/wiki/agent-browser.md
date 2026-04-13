---
title: Agent Browser
type: entity
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Agent Browser

Agent Browser is a free, open-source CLI tool (26K+ GitHub stars) that lets AI agents control a real browser for automated web scraping and interaction. In the context of [[llm-knowledge-bases|LLM Knowledge Bases]], it automates [[data-ingestion]] by scraping web content directly into the raw/ folder.

## Why It Matters

Manual copy-paste fails on:
- JavaScript-heavy sites that load content dynamically
- Pages behind logins
- Research papers with interactive figures
- Content that requires scrolling, clicking "load more," or navigating menus

Agent Browser handles all of these by controlling a real Chrome browser via CDP.

## Setup

```bash
npm install -g agent-browser
agent-browser install
```

The second command downloads a dedicated Chrome browser.

## Basic Usage for Knowledge Bases

```bash
agent-browser open https://some-article.com
agent-browser get text "article"
```

The AI opens the page, grabs the article text, and you pipe it into a .md file in raw/. No manual copy-paste, no browser extensions needed.

## Efficiency

[[source-spisak-second-brain|Nick Spisak]] notes that Agent Browser uses **82% fewer tokens than Playwright MCP**, meaning your AI agent can scrape 5-6x more pages within the same session.

## Knowledge Base Workflow

1. Find an article you want to save
2. Tell your AI: "Scrape this URL and save it to raw/"
3. Agent Browser handles the rest
4. The raw/ folder fills itself

This complements the [[obsidian|Obsidian Web Clipper]] approach — use the clipper for simple articles, Agent Browser for complex pages.

## Related

- [[llm-knowledge-bases]] — The system it feeds into
- [[data-ingestion]] — The broader ingestion process
- [[claude-code]] — The agent that drives Agent Browser
