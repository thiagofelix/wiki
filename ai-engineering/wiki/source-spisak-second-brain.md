---
title: "Source: Nick Spisak — How to Build Your Second Brain"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Nick Spisak — How to Build Your Second Brain

Nick Spisak's X post from April 4, 2026 is a detailed step-by-step implementation guide for [[source-karpathy-llm-knowledge-bases|Karpathy's LLM Knowledge Base]] concept. It distills the idea into an actionable 7-step tutorial that takes under 30 minutes, adds [[agent-browser]] as an automated ingestion tool, and provides a copy-paste [[schema-files|schema template]].

## Metadata

- **Author:** Nick Spisak (@NickSpisak_)
- **Platform:** X (Twitter)
- **Date:** April 4, 2026
- **URL:** https://x.com/NickSpisak_/status/2040448463540830705
- **Stats:** 93 replies, 711 reposts, 4,893 likes, 15,655 bookmarks, 2.2M views
- **Raw file:** `raw/NickSpisak-second-brain-post.md`

## Key Contributions

### Step-by-Step Process
1. Create three folders (2 min) — [[folder-structure|raw/, wiki/, outputs/]]
2. Fill raw/ folder (10 min) — dump everything, don't organize
3. Automate with [[agent-browser]] (optional) — CLI scraping tool
4. Write [[schema-files|schema file]] (5 min) — CLAUDE.md with rules
5. Tell AI to [[wiki-compilation|compile the wiki]] (15 min)
6. Ask questions and save answers — [[compounding-knowledge]] loop
7. Run [[health-checks-and-linting|health checks]] (monthly)
8. You don't need [[obsidian]] (but you can use it)

### Schema Template
Provided a complete, copy-paste-ready CLAUDE.md template covering project description, folder roles, wiki rules, and interest areas.

### Agent Browser Integration
First to connect Karpathy's idea with agent-browser for automated scraping. Key stat: 82% fewer tokens than Playwright MCP, enabling 5-6x more page scrapes per session.

### Anti-Tooling Stance
Strong position against over-tooling: "Obsidian with 47 plugins is the Notion trap all over again. Flat files and a good schema will outperform a fancy tool stack 90% of the time."

## Notable Quotes

> "41K people bookmarked Karpathy's post. The difference between bookmarking it and benefiting from it is one weekend of setup."

> "Stop shopping for the perfect tool. Start building."

## Error Compounding Warning
Highlighted @HFloyd's reply: "When outputs get filed back, errors compound too." Solution: periodic [[health-checks-and-linting|health checks]].
