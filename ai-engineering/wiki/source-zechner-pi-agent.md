---
title: "Source: What I Learned Building a Minimal Coding Agent (Mario Zechner)"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: What I Learned Building a Minimal Coding Agent (Mario Zechner)

Mario Zechner's blog post documenting the lessons learned building [[pi-coding-agent|pi]], a minimal terminal coding harness. The post provides deep technical insights into unified LLM API design, cross-provider compatibility issues, and the philosophy of building tools that prioritize [[context-engineering]] over features.

## Metadata

- **Author:** Mario Zechner (@badlogic)
- **Source:** https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- **Raw file:** `raw/What I learned building an opinionated and minimal coding agent.md`
- **Product page:** https://pi.dev/

## Motivation

Zechner preferred Claude Code but found it turning into "a spaceship with 80% of functionality I have no use for." System prompt and tools change on every release, breaking workflows. He wanted: exact control over context, full interaction inspection, cleanly documented session format, and simple alternative UI building.

## Key Technical Lessons

### The Four APIs
Only four APIs cover virtually all LLM providers: OpenAI Completions, OpenAI Responses, Anthropic Messages, and Google Generative AI. Provider-specific quirks abound:
- Cerebras, xAI, Mistral don't like the `store` field
- Mistral uses `max_tokens` instead of `max_completion_tokens`
- Google doesn't support tool call streaming
- Different providers return reasoning content in different fields

### Cross-Provider Context Handoff
Thinking traces from Anthropic convert to `<thinking>` tagged text for OpenAI. Providers insert signed blobs into event streams that must be replayed. Token tracking is best-effort — providers report costs inconsistently, some only at end of SSE stream.

### Abort Support
"Entirely unacceptable" that most unified LLM APIs ignore abort support. Pi supports aborts throughout the pipeline including tool calls, returning partial results.

### Structured Split Tool Results
Tool results split into content for the LLM and separate structured data for UI display. Prevents parsing textual tool outputs for rendering.

## Philosophy

"If I don't need it, it won't be built." Features baked into other agents are extensions in pi. The core provides primitives (tools, commands, keyboard shortcuts, events, TUI access), not features. "Yes, Doom runs" as an extension.

## Related

- [[pi-coding-agent]] — The agent this describes
- [[building-an-agent]] — First-principles agent construction
- [[context-engineering]] — Pi's core design focus
- [[agents-md]] — Pi uses AGENTS.md and SYSTEM.md
