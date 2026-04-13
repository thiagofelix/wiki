---
title: Pi Coding Agent
type: entity
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Pi Coding Agent

Pi is a minimal, opinionated terminal coding harness built by Mario Zechner that prioritizes [[context-engineering]] and extensibility over feature bloat. Its philosophy — "if I don't need it, it won't be built" — makes it an instructive contrast to full-featured agents like [[claude-code|Claude Code]], and its architecture provides deep technical insights into how coding agents work under the hood.

## Philosophy

Pi is aggressively extensible so it doesn't dictate workflow. Features other agents bake in (sub-agents, plan mode, permission gates, MCP) are built as extensions instead. The core stays minimal while users shape pi to fit their needs.

> "Over the past few months, Claude Code has turned into a spaceship with 80% of functionality I have no use for."

## Architecture

Built as four packages:
- **pi-ai**: Unified LLM API with 15+ provider support, streaming, tool calling, cross-provider context handoffs, token/cost tracking
- **pi-agent-core**: Agent loop handling tool execution, validation, event streaming
- **pi-tui**: Terminal UI framework with differential rendering for flicker-free updates
- **pi-coding-agent**: CLI wiring it all together with session management, tools, themes

## Key Technical Insights

### Cross-Provider Context Handoff
Designed from the start for switching models mid-session. Anthropic thinking traces convert to `<thinking>` tags for OpenAI. Providers insert signed blobs that must be replayed. Serialization/deserialization works across Claude → GPT → Gemini.

### The Four APIs
Only four APIs needed to talk to virtually any LLM provider: OpenAI Completions, OpenAI Responses, Anthropic Messages, and Google Generative AI. Each provider has quirks (Cerebras doesn't like `store`, Mistral uses `max_tokens` instead of `max_completion_tokens`, Google doesn't support tool call streaming).

### Structured Split Tool Results
Tool results split into LLM portion (text/JSON for context) and UI portion (structured data for display). This prevents having to parse textual tool outputs for UI rendering.

### Abort Support
Most unified LLM APIs completely ignore abort support. Pi supports aborts throughout the entire pipeline including tool calls, returning partial results.

### Context Engineering
Minimal system prompt. AGENTS.md loaded at startup. Custom compaction via extensions (topic-based, code-aware, different summarization models). Skills loaded on-demand for progressive disclosure. Dynamic context injection via extensions before each turn.

## What Pi Doesn't Build

No MCP (build CLI tools with READMEs instead). No sub-agents (spawn pi instances via tmux). No permission popups (run in container). No plan mode (write plans to files). No background bash (use tmux). "Yes, Doom runs" as an extension.

## Related

- [[building-an-agent]] — Pi demonstrates agent construction from first principles
- [[context-engineering]] — Pi's core design focus
- [[agents-md]] — Pi uses AGENTS.md and SYSTEM.md for configuration
- [[source-zechner-pi-agent]] — Mario Zechner's blog post on lessons learned
