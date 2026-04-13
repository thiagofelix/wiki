---
title: Compounding Knowledge
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Compounding Knowledge

Compounding knowledge is the feedback loop at the heart of [[llm-knowledge-bases|LLM Knowledge Bases]] where every query, exploration, and interaction adds value back into the system — making the knowledge base smarter over time, like interest compounding in a bank.

## The Loop

1. **Ask a question** against the wiki
2. **LLM researches** across all wiki articles to produce an answer
3. **File the output** back into the wiki (or into outputs/)
4. **Wiki gets richer** — the next question benefits from the previous answer

Karpathy describes this directly: "Often, I end up filing the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always 'add up' in the knowledge base."

## Why This Matters

Normal AI chats are **ephemeral** — knowledge disappears after the conversation ends. The LLM wiki approach makes knowledge **persistent and cumulative**. As [[source-herk-llm-wiki-setup|Nate Herk]] puts it: "People on X are calling it a game changer because it finally makes AI feel like a tireless colleague who actually remembers everything and it stays organized."

## Types of Compounding

- **Query outputs → wiki updates** — Research answers get filed as new articles or additions to existing ones
- **Gap identification → new ingestion** — [[health-checks-and-linting|Health checks]] find gaps, prompting you to add new sources to raw/
- **Cross-source connections** — Each new source creates links to existing articles, revealing patterns you didn't see before
- **Refined indexes** — The INDEX.md and summaries get more precise with each update

## The Hot Cache

[[source-herk-llm-wiki-setup|Nate Herk]] introduced the concept of a **hot.md** file — a ~500 word cache of the most recent context. This is especially useful when an external agent (like an executive assistant) queries the wiki. The hot cache lets it answer routine questions without crawling the entire wiki, saving tokens while still benefiting from the full knowledge base.

## Token Efficiency

One X user reported turning 383 scattered files and 100+ meeting transcripts into a compact wiki, dropping token usage by **95%** when querying. The compiled wiki is far more token-efficient than raw sources because:
- Summaries replace full documents for most queries
- Indexes let the LLM navigate directly to relevant articles
- Backlinks eliminate redundant searches

## Related

- [[llm-knowledge-bases]] — The overall system
- [[wiki-compilation]] — How the wiki gets built
- [[health-checks-and-linting]] — How gaps get identified
- [[llm-wiki-vs-rag]] — Why this is more efficient than traditional RAG
