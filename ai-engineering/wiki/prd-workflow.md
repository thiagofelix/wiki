---
title: PRD Workflow
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PRD Workflow

The PRD (Product Requirements Document) workflow is a two-stage [[claude-code-skills|skill]] chain that turns a shared understanding into an actionable implementation plan: first writing a PRD that describes the destination, then breaking it into vertical slices as GitHub issues that describe the journey.

## Stage 1: Write a PRD

After reaching shared understanding via [[design-trees-and-planning|Grill Me]], the Write a PRD skill is invoked. Its steps:

1. Ask the user for a long, detailed description (may skip if already grilled)
2. Explore the repo to verify assertions
3. Interview the user relentlessly (copy of Grill Me — serves as backup)
4. Sketch out major modules to build or modify
5. Write the PRD using a template and submit as a **GitHub issue**

### What a Good PRD Contains

From [[source-pocock-claude-code-skills|Matt Pocock's]] example (adding document editing to a video editor):
- **Problem statement** — "The article writing page currently regenerates the entire document on every AI interaction"
- **Solution overview** — "Add a split pane document editing experience"
- **User stories** — Many stories describing desired behavior in natural language (agile methodology)
- **Implementation decisions** — High-level, not overprescriptive (to stay durable as code evolves)

The PRD describes the **destination** but not the journey.

## Stage 2: PRD to Issues

This skill takes a PRD and turns it into a kanban board of independently grabbable GitHub issues.

### Process

1. Locate the PRD (fetch from GitHub if not in context)
2. Draft **vertical slices** — thin slices that cut through all integration layers

### Vertical Slices vs. Horizontal Slices

The key principle: each issue should be a **tracer bullet** — a thin vertical slice through all layers, not a horizontal slice of one layer. This flushes out unknown unknowns quickly.

**Example:** A complex PRD was broken into just 4 slices:
1. Document editing engine + tests (the core engine — if this doesn't work, flush it out fast)
2. Independent UI work (not blocked by #1, can run in parallel)
3. Integration work (blocked by #1)
4. Monaco editor toggle (blocked by #2)

### Blocking Relationships

The skill establishes dependencies between issues:
- Some issues can be picked up in parallel (useful for background agents)
- Blocking relationships ensure correct sequencing
- Future QA issues or improvements can be added with their own blocking relationships

### Autonomous Execution

Once issues are created, a "Ralph loop" picks them up:
1. Claude Code reads the issue + parent PRD
2. Implements the solution
3. Comments on the issue with results (e.g., "28 tests covering all acceptance criteria")
4. Closes the issue
5. Next blocked issue becomes unblocked

## The Full Chain

1. [[design-trees-and-planning|Grill Me]] → shared understanding
2. **Write a PRD** → destination document (GitHub issue)
3. **PRD to Issues** → journey plan (GitHub issues with blocking relationships)
4. [[test-driven-development|TDD]] → quality implementation per issue
5. [[codebase-architecture|Architecture review]] → keep the codebase clean

## In the 7 Phases Framework

In [[source-pocock-7-phases|Pocock's 7 Phases of AI Development]], the PRD workflow spans Phases 4-5, preceded by optional Research (Phase 2) and Prototyping (Phase 3) that cache context for agents. Phase 6 (Execution) runs [[ralph-loops]] against the kanban board, and Phase 7 (QA) creates new tickets, cycling back through 5-7 until polished.

## Automated by Multi-Agent Harness

[[source-anthropic-harness-design|Anthropic's planner agent]] automates Phase 4 entirely — expanding a 1-4 sentence prompt into a full product spec. Their evaluator automates Phase 7 by testing the running application via Playwright. This transforms the manual PRD workflow into a fully automated [[multi-agent-harness-design|multi-agent pipeline]].

## Related

- [[design-trees-and-planning]] — The preceding planning step
- [[claude-code-skills]] — The skills ecosystem
- [[test-driven-development]] — How each issue gets implemented
- [[claude-code]] — The tool that executes the workflow
- [[ralph-loops]] — The loops that execute the issues
- [[porting-with-ai]] — Uses the same specs-to-implementation principle
- [[source-pocock-7-phases]] — The full 7-phase framework
- [[multi-agent-harness-design]] — Automated version of this workflow
- [[source-anthropic-harness-design]] — Anthropic's planner/generator/evaluator
