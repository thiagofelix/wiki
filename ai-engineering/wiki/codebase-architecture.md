---
title: Codebase Architecture
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Codebase Architecture

The "Improve Codebase Architecture" [[claude-code-skills|skill]] is a periodic process for identifying and fixing structural problems in a codebase so that AI agents produce better code. It is based on the principle that **garbage codebase → garbage AI output**, and complements [[test-driven-development]] by ensuring module boundaries are clear enough for effective testing.

## The Core Problem

When an AI looks at a badly structured codebase with many tiny, undifferentiated modules:
- It doesn't understand how things relate
- It has to bounce between many small files to understand one concept
- It can't identify clear test boundaries
- It produces lower quality code that mirrors the existing mess

When the codebase has **fewer, deeper modules with thin interfaces**:
- AI navigates easily
- Dependencies are clear
- Testing at boundaries is straightforward
- Output quality goes up

## The Skill Process

### 1. Explore the Codebase

The AI explores naturally, looking for confusions:
- Where does understanding one concept require bouncing around between many small files?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called?
- Where do tightly coupled modules create integration risk in the seams between them?

These are the questions a senior engineer would ask.

### 2. Present Candidates

Present a numbered list of "deepening opportunities" — places where shallow modules can be consolidated into deeper ones with cleaner interfaces.

### 3. Design Multiple Interfaces

For the chosen candidate, spawn **3+ sub-agents in parallel**, each producing a radically different interface design for the deepened module. This is powerful because:
- Multiple options reveal trade-offs you wouldn't see with one design
- You don't need deep interface design expertise to evaluate options
- Elements from different designs can be combined into hybrids

After comparing, recommend which design is strongest and why.

### 4. Create a GitHub Issue

Create a refactor RFC as a GitHub issue, then use [[prd-workflow|PRD to Issues]] to break it into implementable vertical slices.

## Deep Modules vs. Shallow Modules

The architecture skill is language-agnostic and framework-agnostic. The key concept is:

- **Shallow module** — Small, with an interface almost as complex as its implementation. Many shallow modules create confusion.
- **Deep module** — Hides significant complexity behind a simple interface. Fewer deep modules are easier to navigate and test.

## Frequency

- Run weekly or after a surge of new feature development
- Only tackle one candidate at a time — these require human taste and judgment
- Requires a human in the loop because "these decisions require taste"

## The Virtuous Cycle

Improving architecture → better AI output → which further improves the codebase:

1. Run architecture skill → identify deepening opportunities
2. Refactor → cleaner module boundaries
3. [[test-driven-development|TDD]] becomes easier → better test coverage
4. Better tests → higher quality AI implementations
5. Repeat

## Related

- [[claude-code-skills]] — The skills ecosystem
- [[test-driven-development]] — Complementary skill (TDD needs clean architecture)
- [[prd-workflow]] — How refactor plans become implementable issues
- [[claude-code]] — The tool that executes architecture improvements
