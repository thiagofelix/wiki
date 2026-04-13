---
title: Obsidian
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Obsidian

Obsidian is a free markdown editor that serves as the visual frontend ("IDE") for [[llm-knowledge-bases|LLM Knowledge Bases]]. It provides a graph view showing relationships between wiki articles, a file browser for navigating the folder structure, and plugins for rendering data in various formats. Karpathy uses it as his primary interface for viewing raw data, compiled wikis, and derived visualizations.

## Role in the System

Obsidian is **not required** — the knowledge base is just folders and markdown files that work with any editor. But Obsidian adds value through:

- **Graph View** — Visualizes backlinks between wiki articles as an interactive node graph, revealing hubs, clusters, and relationship patterns
- **Backlink Navigation** — Click `[[topic]]` links to jump between articles
- **Live Preview** — Renders markdown with formatting as you browse
- **Vault System** — Each knowledge base is an Obsidian "vault" pointing at the project folder

## Graph View

The graph view is the most compelling feature for knowledge bases. [[source-herk-llm-wiki-setup|Nate Herk]] demonstrated how after ingesting a single article, the graph showed 23 interconnected nodes with clear hubs (major concepts) and peripheral nodes (specific entities). As more sources are ingested, patterns and cross-source relationships emerge visually.

## Obsidian Web Clipper

A Chrome extension for [[data-ingestion|ingesting web content]]:
1. Install the Obsidian Web Clipper extension
2. Set default folder to `raw/` in extension options
3. Click the extension on any article → select vault → "Add to Obsidian"

Karpathy uses this as his primary method for converting web articles to .md files. He also downloads related images locally so the LLM can reference them.

## Plugins

Karpathy mentions using:
- **Marp** — Renders markdown as slide presentations
- Various other plugins for viewing data in different formats

## Multiple Vaults

You can run separate knowledge bases as separate vaults:
- A **YouTube transcript vault** for content research
- A **personal brain vault** for business and personal knowledge
- A **research vault** for a specific topic

These can be kept separate or combined. One project's [[schema-files|CLAUDE.md]] can reference another vault's wiki path.

## Alternatives

As [[source-spisak-second-brain|Nick Spisak]] notes: "You don't need Obsidian. You could use VS Code, Notepad, or anything else. The AI doesn't care what app you open the files in." Karpathy himself said: "I'm trying to keep it super simple and flat. It's just a nested directory of .md files."

The warning: "Obsidian with 47 plugins is the Notion trap all over again. You spend more time configuring the tool than using the knowledge base."

## Related

- [[llm-knowledge-bases]] — The system Obsidian visualizes
- [[data-ingestion]] — Web Clipper for source collection
- [[folder-structure]] — What Obsidian vaults map to
- [[claude-code]] — The engine that works alongside Obsidian
