---
title: Context Engineering
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Context Engineering

Context engineering is the practice of precisely controlling what goes into an AI agent's context window to maximize output quality. The context window is like a "Commodore 64 with a small amount of memory" — every allocation matters, and poor management leads to degraded performance, compaction, and the "dumb zone."

## The Context Window as Memory

Every coding agent's context is an array of slots:

- **Slot 0** — Harness/system prompt (system instructions)
- **Slot 1** — [[agents-md|agents.md]] (permanently allocated every session)
- **Remaining slots** — Actual work: file reads, tool calls, responses

When the context fills up, a **compaction event** occurs — the agent summarizes and drops older context. [[source-ghuntley-collected|Geoffrey Huntley]] calls this "evil" because information is lost through lossy compression. Critical specs and goals can vanish during compaction.

## The Dumb Zone

Proven scientific research confirms the existence of a "dumb zone" in context window operations. Performance degrades noticeably at 60-70% context fill:

> "Once you go like 60-70% over that, the LLM starts getting dumber, actually dumber. So you want to minimize the amount of time in your dumb zone."

Staying out of the dumb zone requires: minimal token allocation for permanent context, only outputting failing tests (not all test results), and creating fresh context windows per loop iteration rather than accumulating.

## Fresh Context vs Compaction

The [[ralph-loops|Ralph]] approach: create a brand new context window for every loop iteration, avoiding compaction entirely. "You create a brand new context window every array on every loop. You tell it to only do one thing. So you don't get compaction."

[[source-anthropic-harness-design|Anthropic]] validated this position: context resets (clearing the window entirely with structured handoff) are superior to compaction. Compaction preserves continuity but doesn't give the agent a clean mental slate. Sonnet 4.5 exhibited context anxiety strongly enough that compaction alone wasn't sufficient — context resets became essential. Opus 4.6 reduced but didn't eliminate the need.

## Context Anxiety

Some models exhibit "context anxiety" — wrapping up work prematurely as they approach what they believe is their context limit:

> "Sonnet 4 had context anxiety... when it had context anxiety, it would go in a simple implementation, 'I'm running out of time. I'm just going to comment out this thing and...'"

This manifests as rushed implementations, commented-out code, and premature task completion. Context resets (not just compaction) address this by giving the agent a completely clean slate.

## Token Budget Heuristics

- ~5,000 tokens for specs/goals allocation per loop
- [[agents-md|Agents.md]] should be ~70 lines maximum to minimize waste on permanently-allocated instructions
- Test runners should only output failures, not passing tests — "most test runners are trash" for agent loops because they waste tokens on passing test output
- JSON preferred over Markdown for structured feature lists — the model is less likely to inappropriately modify JSON files
- A full 200K token context window is only ~136 KB on disk — "only about 2 movies" worth of data (Star Wars script reference)

## Chat Hygiene

One context window = one activity = one goal. Never reuse context across unrelated goals:

> "A failure mode I see is software developers... they make my website pink and then they set another goal that's completely nothing to do with the website being pink and then they say make me an API and all of a sudden they've got this backend API controller with pink REST endpoints... you need to be thinking about a new chat is a new array."

## Cross-Provider Context Handoff

The [[pi-coding-agent]] demonstrates context serialization/deserialization across providers — Anthropic thinking traces are converted to `<thinking>` tags when switching to OpenAI. Providers insert signed blobs into event streams that must be replayed on subsequent requests. This enables multi-model workflows but requires careful abstraction.

## Related

- [[ralph-loops]] — Fresh context per iteration is core to Ralph
- [[agents-md]] — Permanent context allocation that must be minimized
- [[building-an-agent]] — Understanding context mechanics
- [[failure-domains]] — Context-related failure patterns
- [[multi-agent-harness-design]] — Context resets between agent sessions
- [[back-pressure]] — Test output optimization saves context space
- [[pi-coding-agent]] — Agent built around context engineering principles
