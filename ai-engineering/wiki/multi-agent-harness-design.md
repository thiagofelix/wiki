---
title: Multi-Agent Harness Design
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Multi-Agent Harness Design

Multi-agent harness design is the practice of decomposing autonomous coding tasks across specialized agents — typically a planner, generator, and evaluator — to achieve results that exceed what a single agent can produce. Inspired by Generative Adversarial Networks (GANs), this architecture addresses the two biggest failure modes in long-running agentic coding: context degradation and poor self-evaluation.

## The Core Problem

Single agents working on complex tasks exhibit two persistent failure modes:

1. **Context anxiety** — As the context window fills, agents lose coherence and begin wrapping up prematurely. Compaction (in-place summarization) doesn't fully solve this because the agent never gets a clean mental slate.

2. **Self-evaluation blindness** — Agents confidently praise their own mediocre work. "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre."

## The Three-Agent Architecture

From [[source-anthropic-harness-design|Anthropic's harness research]]:

### Planner
- Expands a short user prompt into a full product spec
- Stays high-level to avoid cascading errors from over-specification
- Can weave in AI features, design language, and architectural decisions
- Analogous to Phase 4 (PRD) in [[source-pocock-7-phases|Pocock's 7 Phases]]

### Generator
- Implements the spec in sprints or continuous sessions
- Self-evaluates at end of each unit of work before QA handoff
- Can negotiate **sprint contracts** with the evaluator before building
- Analogous to Phase 6 (Execution) in Pocock's framework

### Evaluator
- Tests the running application like a real user (via Playwright MCP)
- Grades against concrete criteria with hard pass/fail thresholds
- Provides specific, actionable feedback on failures
- Analogous to Phase 7 (QA) + [[back-pressure]] + [[test-driven-development]]

## Key Design Principles

### Separation of Generation and Evaluation
The single most important principle. A generator agent cannot reliably evaluate its own output. Tuning a separate evaluator to be skeptical is far more tractable than making a generator self-critical.

### Context Resets vs. Compaction
When agents need to work across many iterations:
- **Context resets** (fresh context + structured handoff) are superior to compaction
- This validates [[source-ghuntley-collected|Huntley's]] claim that compaction is "evil"
- Newer models (Opus 4.5+) exhibit less context anxiety, reducing the need for resets

### Sprint Contracts
Before building, the generator and evaluator agree on what "done" looks like. This bridges the gap between high-level specs and testable implementation, preventing the evaluator from testing against vague criteria.

### Grading Criteria Make Subjective Quality Measurable
Even subjective qualities (design, aesthetics) can be graded when decomposed into concrete criteria:
- Design quality (coherent whole vs. collection of parts)
- Originality (custom decisions vs. "AI slop" patterns)
- Craft (technical execution)
- Functionality (usability)

### Harnesses Should Simplify Over Time
> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."

As models improve, strip away components that are no longer load-bearing. The space of interesting harness combinations doesn't shrink — it moves.

## Relationship to Ralph Loops

[[ralph-loops|Ralph]] is a single-agent loop pattern: one process, one task, one repository. Multi-agent harness design extends this by:
- Adding a planner that automates spec creation (replaces manual spec writing)
- Adding an evaluator that provides structured [[back-pressure]] (replaces human review)
- Orchestrating multiple specialized agents instead of one general agent

Anthropic explicitly references Ralph as convergent discovery in their harness research.

## Cost-Quality Tradeoffs

| Approach | Duration | Cost | Quality |
|----------|----------|------|---------|
| Solo agent | 20 min | $9 | Broken core features |
| Full 3-agent harness | 6 hr | $200 | Working, polished application |
| Simplified harness (newer model) | 3 hr 50 min | $125 | Working application, some gaps |

The evaluator's value depends on where the task sits relative to what the model can do reliably solo. For tasks within the model's comfort zone, the evaluator is unnecessary overhead. For edge-of-capability tasks, it provides real lift.

## Related

- [[ralph-loops]] — The single-agent foundation
- [[source-anthropic-harness-design]] — Anthropic's full research on this architecture
- [[source-pocock-7-phases]] — The human-driven version of the same workflow
- [[back-pressure]] — Evaluator as structured back-pressure
- [[software-factories]] — Where harness automation leads at scale
- [[prd-workflow]] — Planner automates the PRD creation step
- [[test-driven-development]] — Complementary quality mechanism
- [[building-an-agent]] — Understanding the agents that compose the harness
