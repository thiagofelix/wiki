---
title: Agents.md
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Agents.md

An agents.md (or CLAUDE.md) file is a permanently-allocated configuration document that tells an AI coding agent how to behave within a specific project. It occupies slot 1 in the context window and is loaded at every session start, making its size and content critical to loop performance.

## What It Is

The agents.md sits in slot 1 of the context array, permanently allocated on every loop iteration. It configures agent behavior: coding conventions, project structure, testing patterns, and domain-specific instructions. Every token in agents.md is paid for on EVERY single context window.

## History

Originally called CLAUDE.md by Anthropic for Claude Code. The community standardized on agents.md as a cross-agent convention. Different agents read from different locations: [[claude-code|Claude Code]] reads `~/.claude/`, parent directories, and the current directory. The [[pi-coding-agent]] reads from `~/.pi/agent/`, parent directories, and current directory. OpenAI purchased the agents.md domain, further establishing the convention.

## Size Matters

Agents.md should be approximately **70 lines maximum**. Every token is allocated on every loop iteration — bloated files waste context and push the agent toward the [[context-engineering|dumb zone]] faster. "Minimal allocation — malloc only what's needed per loop."

## Per-Model Configuration

Different models need different tonality:

- **GPT-5** is "timid" and responds to firm language
- **Anthropic models** expect emphatic instructions ("you MUST", "NEVER")
- Different models have distinct personalities: some are "like a squirrel that chases tools," some are summarizers

Separate agents.md files per model may be needed for multi-model setups.

## Specs as Lookup Tables

Specifications referenced from agents.md serve as "a lookup table to other specifications." This keeps the agents.md small while giving the agent access to detailed project knowledge through `file_read` tool calls:

> "Every loop I allocate the specifications which is a lookup table to other specifications and that's enough to pin and reframe each loop — this is my domain knowledge."

The specs have "pins" — multiple generative words that improve search tool hit rates when the agent needs to find relevant information.

## What Goes In

- Project-specific coding conventions
- Testing strategy and tool preferences
- Architecture constraints and module boundaries
- Domain-specific instructions
- Pointers to spec files for detailed knowledge

## What Stays Out

- Generic LLM instructions (the harness handles this)
- Information derivable from the codebase
- Anything that doesn't need to be in every single context window
- Long documentation (reference via specs files instead)

## Related

- [[building-an-agent]] — How agents.md fits into agent architecture
- [[context-engineering]] — Why agents.md size matters
- [[ralph-loops]] — Agents.md is loaded fresh each iteration
- [[claude-code]] — Primary consumer of CLAUDE.md
- [[claude-code-skills]] — Skills extend agents.md on demand
- [[source-ghuntley-videos]] — Dedicated 22-minute video on agents.md history
