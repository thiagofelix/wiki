---
title: Design Trees and Planning
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Design Trees and Planning

Design trees are a methodology for systematically exploring all branches of a design decision before committing to code. Combined with the "Grill Me" [[claude-code-skills|skill]], they form the planning foundation of an AI-assisted engineering workflow — ensuring shared understanding between human and LLM before implementation begins.

## The Design Tree Concept

From Frederick P. Brooks' "The Design of Design": as you approach a design, you need to walk down all branches of a decision tree. Each branch point is a design choice, and each choice opens new sub-decisions.

**Example:** Designing a search page:
- Advanced search vs. text box?
  - If advanced search → what filters? What sorting methods?
    - If date filter → date range or relative? Calendar picker or text input?
- Keep walking until the design is as complete as possible

## The Grill Me Skill

[[source-pocock-claude-code-skills|Matt Pocock's]] favorite skill — just three sentences:

> "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. And finally, if a question can be answered by exploring the codebase, explore the codebase instead."

### What It Produces

When invoked, the LLM:
1. Explores the relevant codebase first
2. Asks 10-50+ questions, walking down each branch of the design tree
3. Resolves dependencies between decisions one by one
4. Continues until shared understanding is reached

A typical session: 16 questions on a medium feature (document editing). Complex features can drive 30-50 questions over 30-45 minutes.

### Why It's Needed

"Relatively recently, Claude Code will tend to just spit out a plan really early when I go in plan mode and it tends to just create a document before I feel I've reached a shared understanding with the LLM. But the Grill Me skill forces that conversation."

## From Planning to Implementation

The Grill Me skill is step one in a chain:
1. **Grill Me** → reach shared understanding
2. **[[prd-workflow|Write a PRD]]** → document the destination
3. **[[prd-workflow|PRD to Issues]]** → plan the journey
4. **[[test-driven-development|TDD]]** → execute with quality

## Related

- [[claude-code-skills]] — The skills ecosystem
- [[prd-workflow]] — The next step after planning
- [[claude-code]] — The tool that executes the skill
