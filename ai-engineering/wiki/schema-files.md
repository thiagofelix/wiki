---
title: Schema Files
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Schema Files

A schema file is a plain-text instruction document (typically CLAUDE.md or AGENTS.md) placed at the root of a knowledge base project that tells the LLM how the wiki is structured, what conventions to follow, and what workflows to use when ingesting sources, answering questions, or maintaining the wiki. It is the single most important file in an [[llm-knowledge-bases|LLM Knowledge Base]].

## Purpose

The schema file acts as the AI's instruction manual for your specific knowledge base. It defines:
- What the knowledge base is about
- How it's organized (folder roles, naming conventions)
- Rules for wiki maintenance (one file per topic, summaries, linking format)
- What workflows to follow for ingestion, querying, and linting

## Naming

- **CLAUDE.md** — Used with [[claude-code|Claude Code]]
- **AGENTS.md** — Used with OpenAI Codex or general-purpose agents
- **README.md** — Works as a fallback; the name doesn't matter, the content does

Karpathy keeps his schema "super simple and flat" in an AGENTS.md file. No database, no plugin — just a text file that tells the AI the rules.

## Example Template

From [[source-spisak-second-brain|Nick Spisak's guide]]:

```markdown
# Knowledge Base Schema

## What This Is
A personal knowledge base about [YOUR TOPIC].

## How It's Organized
- raw/ contains unprocessed source material. Never modify these files.
- wiki/ contains the organized wiki. AI maintains this entirely.
- outputs/ contains generated reports, answers, and analyses.

## Wiki Rules
- Every topic gets its own .md file in wiki/
- Every wiki file starts with a one-paragraph summary
- Link related topics using [[topic-name]] format
- Maintain an INDEX.md that lists every topic with a one-line description
- When new raw sources are added, update relevant wiki articles

## My Interests
[List 3-5 things you want this knowledge base to focus on]
```

## Customization

Karpathy intentionally left his idea "vague so that you can hack it and customize it." Different projects produce different schemas:

- A **YouTube transcript vault** might have categorized subfolders (concepts/, entities/, sources/) and strict tagging rules
- A **personal second brain** might keep everything flat with no subfolders
- An **executive assistant vault** might add a hot cache path and rules about when to read vs. skip the wiki

The schema is what makes each knowledge base unique even though the [[folder-structure]] is always the same.

## Cross-Project References

[[source-herk-llm-wiki-setup|Nate Herk]] demonstrated pointing one project's CLAUDE.md at another project's wiki. His executive assistant's schema includes a wiki path directive: "Whenever you need to read things about me and my business, go to my herkbrain vault." This lets one agent query another project's knowledge base without duplicating data.

## Relationship to Agents.md

Schema files for knowledge bases are the same concept as [[agents-md-history|agents.md]] for coding projects. The same design principles apply: keep it concise (~70 lines), focus on rules and conventions, let the AI fill in details from its latent knowledge. Huntley's advice: "just enough to tickle the latent space."

## Related

- [[llm-knowledge-bases]] — The overall system
- [[folder-structure]] — What the schema describes
- [[claude-code]] — The primary tool that reads schema files
- [[wiki-compilation]] — The process the schema governs
- [[agents-md-history]] — The engineering equivalent of schema files
