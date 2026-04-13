---
title: Test-Driven Development
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Test-Driven Development

Test-Driven Development (TDD) is a [[claude-code-skills|Claude Code skill]] that forces AI agents to follow a red-green-refactor loop when implementing code. It is the most consistent method [[source-pocock-claude-code-skills|Matt Pocock]] has found for improving the quality of AI-generated code.

## The Red-Green-Refactor Loop

1. **Red** — Write one failing test
2. **Green** — Write the minimum code to make that test pass
3. **Refactor** — Look for refactor candidates
4. Repeat until complete

The AI writes the test **first**, then the implementation. This inverts the typical AI pattern of generating code and hoping it works.

## The TDD Skill Workflow

1. **Confirm interface changes** — Ask the user what interface changes are needed (this is the most important step)
2. **Confirm behaviors to test** — Which behaviors matter?
3. **Design interfaces for testability** — Structure code so it can be tested at boundaries
4. **Write one test at a time** — Red-green-refactor loop
5. **Look for refactor candidates** — After all tests pass

## Why Interfaces Matter

When an AI looks at a badly structured codebase, it sees many tiny, undifferentiated modules with unclear relationships. It has to work hard to figure out what's responsible for what.

When you restructure into **larger modules with thin interfaces** (the functions actually exported/called), it's much easier for AI to:
- Navigate the codebase
- Understand dependencies
- Test at module boundaries

The TDD skill makes interface changes "top of mind" for the AI — when it changes an interface, that's an important decision worth taking time over.

## Limitations

- LLMs are **reluctant to refactor their own code** while it sits in their context window. Clearing context makes them less precious about what they've written.
- TDD is **hard in badly structured codebases** because test boundaries are unclear. This is why [[codebase-architecture]] improvement is a complementary skill.
- The refactor step hasn't been "brilliant" in practice — the red-green loop is where the real value is.

## TDD and Architecture

TDD demands a lot of your codebase. It's hard to do in a badly structured codebase because module boundaries and test boundaries are unclear. This creates a virtuous cycle:

1. [[codebase-architecture|Improve architecture]] → clearer module boundaries
2. Clearer boundaries → easier to write tests
3. Better tests → higher quality implementations
4. Higher quality code → easier to maintain architecture

## Relationship to the Workflow

TDD is the **execution phase** in the skills chain:
1. [[design-trees-and-planning|Grill Me]] → understand the problem
2. [[prd-workflow|Write PRD]] → document the destination
3. [[prd-workflow|PRD to Issues]] → plan the journey
4. **TDD** → implement each issue with quality
5. [[codebase-architecture|Architecture review]] → maintain quality over time

## TDD as Back-Pressure

In [[source-ghuntley-collected|Geoffrey Huntley's]] framework, TDD is a form of [[back-pressure]] — the test suite provides resistance that rejects invalid AI generations. A fast test suite that provides good signal without spinning too slowly is the ideal tuning for a [[ralph-loops|Ralph loop]].

## Related

- [[claude-code-skills]] — The skills ecosystem
- [[codebase-architecture]] — Prerequisite for effective TDD
- [[prd-workflow]] — What produces the issues TDD implements
- [[claude-code]] — The tool that runs the TDD loop
- [[ralph-loops]] — TDD as a form of Ralph loop
- [[back-pressure]] — TDD provides back-pressure to AI agents
