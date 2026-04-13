---
title: "Source: Matt Pocock — My 7 Phases of AI Development"
type: summary
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Source: Matt Pocock — My 7 Phases of AI Development

Matt Pocock outlines a seven-phase framework for AI-assisted development that consistently leads to shipping production-quality work. The framework applies regardless of the specific tooling — [[ralph-loops|Ralph loops]], GSD, Spec Kit, or any other approach — and represents a common pattern across successful AI engineering workflows.

## Metadata

- **Author:** Matt Pocock (aihero.dev)
- **Source:** https://www.aihero.dev/my-7-phases-of-ai-development
- **Raw file:** `raw/My 7 Phases Of AI Development.md`

## The Seven Phases

### Phase 1: The Idea
Every project starts with an idea — an app, a feature, a bug fix, or a refactor. Refine iteratively using the [[design-trees-and-planning|Grill Me]] skill before investing in research or prototypes. Scales from massive projects to narrow tasks.

### Phase 2: Research (Optional)
If the idea involves external dependencies or difficult exploration, create a `RESEARCH.md` asset that caches relevant information where agents can access it. Research assets are temporary — they go stale and can cause agents to take wrong turns if kept too long.

### Phase 3: Prototyping (Optional)
Essential when you need to impose **taste** on the outcome. Create multiple variations on throwaway routes, letting the LLM show different approaches. Commit the winning design to the codebase so agents can reference concrete examples during implementation.

### Phase 4: Product Requirements Document (PRD)
With research and prototyping complete, describe the destination (not the journey). Focus on user-visible behavior and outcomes, not implementation details. Hammer out every decision point by prompting the agent to grill you on edge cases. Uses the [[prd-workflow|Write a PRD]] skill.

### Phase 5: Implementation Planning (Kanban Board)
Break the PRD into vertical slices with blocking relationships. Find all non-blocking tickets and parallelize. Uses the [[prd-workflow|PRD to Issues]] skill. GitHub Issues works but lacks built-in blocking relationships; Linear is better.

### Phase 6: Execution
Run a coding agent against all tickets. Sequential is usually sufficient, but parallelization is possible with well-structured kanban boards. Uses [[ralph-loops|Ralph loops]]. With proper setup (research + prototype + kanban + PRD), execution can run **away from keyboard (AFK)**.

### Phase 7: Quality Assurance
Agent creates a QA plan for human review. QA uncovers issues → more kanban tickets → another execution loop. Iterate through phases 5-7 until polished. Involves humans reading generated code for logic errors, security vulnerabilities, performance issues, maintainability, and adherence to project patterns.

## Summary Table

| Phase | Purpose | Key Deliverable |
|-------|---------|-----------------|
| 1. Idea | Define what to build | Problem statement |
| 2. Research | Explore dependencies | `research.md` asset |
| 3. Prototype | Test design and UX | Working prototype |
| 4. PRD | Document end state | Product requirements |
| 5. Kanban Board | Break down work | Tasks with dependencies |
| 6. Execution | Build implementation | Working code |
| 7. QA | Verify the work | QA plan + feedback |

## Key Principles

- **AFK execution** requires all context to be pre-cached: research assets, prototype code, clear PRD, well-defined tickets with acceptance criteria
- **Research assets are ephemeral** — they live only for the duration of the sprint
- **Prototyping imposes taste** — concrete examples are more valuable than abstract descriptions by Phase 4
- **QA is iterative** — expect multiple cycles through phases 5-7
- **This is for engineers, not vibe coders** — "people serious about AI engineering and building applications that are built to last"

## Relationship to Other Workflows

This framework subsumes and organizes the individual [[claude-code-skills]] from [[source-pocock-claude-code-skills|Pocock's earlier video]]:
- Phase 1 → Grill Me skill
- Phase 4 → Write a PRD skill
- Phase 5 → PRD to Issues skill
- Phase 6 → TDD skill + Ralph loops
- Phase 7 → QA plan

It also parallels [[source-anthropic-harness-design|Anthropic's three-agent architecture]]:
- Phase 4 → Planner agent
- Phase 6 → Generator agent
- Phase 7 → Evaluator agent

## Related

- [[claude-code-skills]] — The individual skills used across phases
- [[design-trees-and-planning]] — Phase 1 deep dive
- [[prd-workflow]] — Phases 4-5 deep dive
- [[test-driven-development]] — Phase 6 execution method
- [[ralph-loops]] — Phase 6 execution engine
- [[multi-agent-harness-design]] — How this maps to automated architectures
- [[source-anthropic-harness-design]] — Anthropic's automated version of this workflow
