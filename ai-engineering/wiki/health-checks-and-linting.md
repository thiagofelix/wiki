---
title: Health Checks and Linting
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Health Checks and Linting

Health checks (or "linting") are periodic LLM-driven audits of an [[llm-knowledge-bases|LLM Knowledge Base]] wiki that catch errors, fill gaps, find connections, and strengthen overall data integrity. They are essential for preventing error compounding — when the AI writes something slightly wrong and future answers build on that mistake.

## Why They Matter

As [[source-spisak-second-brain|Nick Spisak]] highlights, one of the best replies to Karpathy's post came from @HFloyd: "When outputs get filed back, errors compound too." Since the [[compounding-knowledge]] loop feeds outputs back into the wiki, unchecked errors propagate. Health checks are the fix.

## The Health Check Prompt

From [[source-spisak-second-brain|Nick Spisak's guide]]:

> "Review the entire wiki/ directory. Flag any contradictions between articles. Find topics mentioned but never explained. List any claims that aren't backed by a source in raw/. Suggest 3 new articles that would fill gaps."

## What Linting Catches

Karpathy describes running LLM health checks that:
- **Find inconsistent data** — Contradictions between articles
- **Impute missing data** — Use web searches to fill gaps
- **Find interesting connections** — Suggest new article candidates linking existing concepts
- **Identify unbacked claims** — Flag statements not grounded in raw sources
- **Suggest further questions** — LLMs are good at identifying what to investigate next

## Frequency

- **Monthly** — [[source-spisak-second-brain|Nick Spisak]] recommends monthly health checks as a minimum
- **Weekly** — For actively growing knowledge bases with frequent ingestion
- **After large ingests** — Run a lint after batch-ingesting many sources at once

## Linting as Maintenance

[[source-herk-llm-wiki-setup|Nate Herk]] compares linting to the maintenance advantage over traditional [[llm-wiki-vs-rag|RAG]]: "For maintenance, you just run a lint. You clean up things. You add more articles. You give it more context rather than having to re-embed when things change."

The LLM might also proactively say: "I don't fully understand this. Can you give me more info or grab some more articles that might help?"

## Related

- [[llm-knowledge-bases]] — The overall system
- [[compounding-knowledge]] — Why linting is necessary (error compounding)
- [[wiki-compilation]] — The process linting validates
- [[llm-wiki-vs-rag]] — Linting vs. re-embedding
