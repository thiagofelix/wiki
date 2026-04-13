---
title: Folder Structure
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Folder Structure

The three-folder architecture is the foundation of an [[llm-knowledge-bases|LLM Knowledge Base]]. It separates unprocessed sources from organized knowledge and generated outputs, giving the LLM clear boundaries for where to read and where to write.

## The Three Folders

```
my-knowledge-base/
  raw/          — source material (articles, notes, transcripts, screenshots)
  wiki/         — LLM-maintained organized wiki
  outputs/      — generated reports, answers, analyses
```

### raw/

The "junk drawer" of source material. You dump everything here without organizing, renaming, or cleaning it — that's the AI's job. Contents include:
- Articles and papers (clipped as .md or .txt)
- YouTube transcripts
- Meeting notes and recordings
- Screenshots and diagrams
- Project docs, datasets, repo readmes

**Rule: never modify files in raw/.** They are the immutable source of truth.

### wiki/

Where the LLM turns raw material into something organized. Contains:
- **INDEX.md** — Master list of every topic with one-line descriptions
- **Topic articles** — One .md file per concept, entity, or theme
- **Backlinks and cross-references** — Articles link to each other using `[[topic]]` format
- **LOG.md** (optional) — Operation history tracking ingestion events

The LLM writes and maintains everything in wiki/. You rarely touch it directly.

### outputs/

Where answers to your questions live. When you query the knowledge base, the LLM can render:
- Markdown reports
- Slide shows (Marp format)
- Visualizations (matplotlib, charts)
- Research briefings

Outputs can be "filed back" into the wiki to enhance it — this is the [[compounding-knowledge]] loop.

## Variations

[[source-herk-llm-wiki-setup|Nate Herk]] showed two variations:
- **Flat structure** — Wiki articles are just .md files with no subfolders. Karpathy prefers this: "super simple and flat"
- **Categorized structure** — Wiki has subfolders like `analysis/`, `concepts/`, `entities/`, `sources/`. Better for larger, topic-specific knowledge bases (e.g., YouTube transcript collections)

Both approaches work. The [[schema-files|schema file]] determines which structure the LLM uses.

## Additional Files

- **[[schema-files|CLAUDE.md]]** — Lives in the project root, not inside any folder. Tells the LLM the rules.
- **hot.md** (optional) — A "hot cache" of ~500 words with the most recent context. Useful when the wiki is accessed by an external agent (like an executive assistant) that doesn't need to crawl the full wiki for routine tasks.

## Related

- [[llm-knowledge-bases]] — The overall system
- [[schema-files]] — The instruction file
- [[data-ingestion]] — How to fill the raw/ folder
- [[wiki-compilation]] — How wiki/ gets populated
