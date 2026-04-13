---
title: "Source: Anthropic — Harness Design for Long-Running Application Development"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Anthropic — Harness Design for Long-Running Application Development

Anthropic engineer Prithvi Rajasekaran describes a multi-agent architecture — planner, generator, evaluator — inspired by Generative Adversarial Networks (GANs) that enables autonomous, multi-hour coding sessions producing full-stack applications. The post builds on Anthropic's earlier [[ralph-loops|Ralph]]-adjacent work on long-running agents and addresses two stubborn failure modes: context anxiety and poor self-evaluation.

## Metadata

- **Author:** Prithvi Rajasekaran (Anthropic Labs)
- **Source:** https://www.anthropic.com/engineering/harness-design-long-running-apps
- **Raw file:** `raw/Harness design for long-running application development.md`

## Key Contributions

### Why Naive Implementations Fail

Two persistent failure modes with long-running agents:

1. **Context anxiety** — Models lose coherence as the context window fills; they begin "wrapping up prematurely." Compaction (in-place summarization) helps but doesn't fully solve it. **Context resets** — clearing the window entirely and handing off structured state to a fresh agent — are more effective. (Claude Sonnet 4.5 required these; Opus 4.5/4.6 largely removed the need.)

2. **Poor self-evaluation** — Agents confidently praise their own mediocre work. Separating generation from evaluation makes skeptical grading tractable. "Tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

### The Three-Agent Architecture

- **Planner** — Expands a 1-4 sentence user prompt into a full product spec. Stays high-level to avoid cascading errors from over-specification. Prompted to weave AI features into specs.
- **Generator** — Implements work in sprints (one feature at a time). Uses React/Vite/FastAPI/SQLite stack. Self-evaluates at end of each sprint before QA handoff.
- **Evaluator** — Uses Playwright MCP to click through the running application like a real user. Grades each sprint against criteria with hard thresholds. If any criterion fails, the sprint is rejected with specific feedback.

### Sprint Contracts

Before each sprint, generator and evaluator negotiate a **sprint contract** — agreeing on what "done" looks like before code is written. This bridges the gap between high-level specs and testable implementation.

### Frontend Design: Making Subjective Quality Gradable

Four grading criteria turned "is this beautiful?" into concrete, gradable terms:

1. **Design quality** — Coherent whole vs. collection of parts
2. **Originality** — Evidence of custom decisions vs. template defaults / "AI slop"
3. **Craft** — Typography, spacing, color, contrast (baseline competence)
4. **Functionality** — Usability independent of aesthetics

Design quality and originality were weighted more heavily because Claude already scored well on craft and functionality by default. Penalizing "AI slop" pushed the model toward aesthetic risk-taking.

### Results

| Harness | Task | Duration | Cost |
|---------|------|----------|------|
| Solo agent | Retro game maker | 20 min | $9 |
| Full 3-agent | Retro game maker | 6 hr | $200 |
| Updated (no sprints) | DAW (music app) | 3 hr 50 min | $125 |

Solo runs produced broken core features. Full harness runs produced working applications with polish, though imperfect. The evaluator consistently caught bugs that would have shipped in solo mode.

### Simplification Over Time

As models improve, harness components should be stress-tested:

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing."

With Opus 4.6, sprints were removed entirely (the model could sustain coherent coding for 2+ hours). The evaluator moved to a single pass at the end. The principle: "Find the simplest solution possible, and only increase complexity when needed."

### Notable Evaluator Findings

| Contract Criterion | Finding |
|---|---|
| Rectangle fill tool | Tool only places tiles at start/end instead of filling region |
| Delete entity spawn points | Handler requires both `selection` and `selectedEntityId` but clicking only sets one |
| Reorder animation frames | Route defined after wildcard, FastAPI matches 'reorder' as integer → 422 |

### Connection to Ralph

The post explicitly references [[ralph-loops|Ralph Wiggum]] as convergent discovery:

> "The broader developer community has converged on similar insights, with approaches like the 'Ralph Wiggum' method using hooks or scripts to keep agents in continuous iteration cycles."

## Key Insights

1. **Separation of generation and evaluation** is a general principle, not just a trick
2. **Context resets > compaction** (validating Huntley's "compaction is evil" stance)
3. **Model improvements simplify harnesses** — components should be dropped when no longer needed
4. **The space of interesting harness combinations doesn't shrink as models improve; it moves**
5. **Grading criteria shape output** — phrases like "museum quality" steered generator aesthetics

## Related

- [[ralph-loops]] — The foundational loop pattern this builds upon
- [[multi-agent-harness-design]] — The broader topic of multi-agent coding architectures
- [[failure-domains]] — Concrete failure examples documented here
- [[context-engineering]] — Context resets vs compaction analysis
- [[back-pressure]] — Evaluator provides structured back-pressure
- [[software-factories]] — Where this architecture leads at scale
- [[prd-workflow]] — Planner agent automates the PRD step
- [[test-driven-development]] — Evaluator serves a similar function to TDD
- [[source-anthropic-effective-harnesses]] — Earlier Anthropic research this builds on
- [[source-pocock-claude-code-skills]] — Complementary individual-developer workflow
