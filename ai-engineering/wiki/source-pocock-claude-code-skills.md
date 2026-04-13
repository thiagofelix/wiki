---
title: "Source: Matt Pocock — Claude Code Skills for Real Engineering"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Matt Pocock — Claude Code Skills for Real Engineering

Matt Pocock's YouTube video presents a system of [[claude-code-skills]] — short markdown files that encode engineering processes for AI agents. The video walks through five skills that chain together into a complete development workflow: Grill Me → Write a PRD → PRD to Issues → TDD → Improve Codebase Architecture.

## Metadata

- **Author:** Matt Pocock
- **Platform:** YouTube
- **Video ID:** EJyuu6zlQCg
- **Raw file:** `raw/EJyuu6zlQCg-transcript.txt`

## Key Contributions

### The Skills Philosophy
- AI agents are "middling to good engineers" with **no memory**
- Skills encode process so the AI follows a strict path every time
- Skills don't have to be long — the Grill Me skill is 3 sentences but drives 30-50 question sessions
- "Choose the right words for the LLM at the right time"
- Treat agents like humans with weird constraints

### Five Skills Presented

1. **[[design-trees-and-planning|Grill Me]]** — "Interview me relentlessly about every aspect of this plan until we reach a shared understanding." Uses the design tree concept from Frederick P. Brooks.

2. **[[prd-workflow|Write a PRD]]** — Turns shared understanding into a Product Requirements Document submitted as a GitHub issue. Includes user stories and implementation decisions.

3. **[[prd-workflow|PRD to Issues]]** — Breaks PRDs into vertical slices (tracer bullets) with blocking relationships. Each issue cuts through all integration layers.

4. **[[test-driven-development|TDD]]** — Red-green-refactor loop. Confirm interface changes → write one failing test → implement → refactor. Most consistent way to improve AI code quality.

5. **[[codebase-architecture|Improve Codebase Architecture]]** — Explore codebase for confusion → present deepening candidates → spawn parallel sub-agents for multiple interface designs → create refactor RFC.

### The "Ralph Loop"
An autonomous loop where [[claude-code]] picks up GitHub issues, implements them with TDD, comments results, and closes them — unblocking the next issue in sequence.

### Deep vs. Shallow Modules
Code restructured into fewer, deeper modules with thin interfaces is easier for AI to navigate, test, and maintain. Many tiny undifferentiated modules confuse AI agents.

## Notable Quotes

> "If you have a garbage codebase, then the AI is going to produce garbage within that codebase."

> "The most successful way to get code quality up from agents is just to treat them like humans."

> "Skills don't have to be long to be impactful."

## Evolution: The 7 Phases Framework

In a later article, Pocock formalized these skills into a broader [[source-pocock-7-phases|7 Phases of AI Development]] framework that adds Research, Prototyping, and explicit QA phases around the core skill chain. The 7 Phases framework is tool-agnostic and represents a common pattern across successful AI-assisted development workflows.

## Course Reference
Matt Pocock offers a course called "Claude Code for Real Engineers" — a 2-week cohort covering sub-agents, LLM constraints, steering, tracer bullets, feedback loops, and autonomous agents.
