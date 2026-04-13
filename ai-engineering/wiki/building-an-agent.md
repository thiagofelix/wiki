---
title: Building an Agent
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Building an Agent

An AI coding agent is fundamentally simple: ~300 lines of code running in a loop with LLM tokens. [[source-ghuntley-collected|Geoffrey Huntley]] argues that understanding how to build one from first principles is the new fundamental knowledge for software engineers in 2026 — as essential as knowing what a primary key is.

## The Core Architecture

Every coding agent (Cursor, Claude Code, Amp, Windsurf, GitHub Copilot) is:
1. Lines of code running in a loop
2. Feeding LLM tokens
3. The model does all the heavy lifting

The harness (the agent wrapper) provides:
- System prompt (slot 0 in the context array)
- [[agents-md-history|Agents.md]] injection (slot 1)
- Subtle hints: OS version, shell type, forward/backslash conventions
- Tool definitions (file_read, file_write, bash, etc.)

## The Context Window as Memory

The context window is like a "Commodore 64 with a small amount of memory." Every allocation matters:

- **Slot 0** — Harness prompt (system instructions)
- **Slot 1** — Agents.md (permanently allocated)
- **Remaining slots** — Actual work: file reads, tool calls, responses

When the context fills up, a **compaction event** occurs — the agent summarizes and drops older context. This is "evil" because information is lost. [[ralph-loops|Ralph's]] approach: create a brand new context window for every loop iteration, avoiding compaction entirely.

## Not All LLMs Are Agentic

Different models suit different tasks (like different types of cars):
- **Grok** — Security research
- **Claude** — Coding agent work
- Models have distinct personalities: some are "timid" (GPT-5 with firm language), some respond to emphatic instructions (Anthropic)

## Why Build Your Own

> "Knowing how to build an agent transforms you from being a consumer of AI into being a producer."

Building your own agent teaches you:
- How context windows actually work
- How tool calls flow
- How to tune [[back-pressure]]
- How to design effective [[agents-md-history|agents.md]] files
- How to spot failure domains and engineer them away

This is the dividing line in [[software-development-vs-engineering]]: consumers use pre-built agents; engineers understand and build them.

## The Recursive Insight

> "Build yourself an agent and taste building in the recursive latent space."

You can build an agent using an agent. Huntley demonstrated live-coding an agent during a conference talk while simultaneously giving the talk — "concurrency in doing work" is the new normal.

## From Single to Multi-Agent

Once you understand how a single agent works, the next level is [[multi-agent-harness-design]] — composing multiple specialized agents (planner, generator, evaluator) to tackle tasks beyond any single agent's capability. [[source-anthropic-harness-design|Anthropic's research]] shows that a three-agent harness can produce working full-stack applications in multi-hour autonomous sessions, while single agents produce broken results on the same tasks.

## Related

- [[ralph-loops]] — What the agent does once built
- [[agents-md-history]] — How to configure the agent
- [[back-pressure]] — How to provide feedback to the agent
- [[multi-agent-harness-design]] — Composing multiple agents
- [[software-development-vs-engineering]] — Why building agents is engineering
- [[claude-code]] — A production agent you can study
- [[source-anthropic-harness-design]] — Multi-agent harness research
