---
title: Back-Pressure
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Back-Pressure

Back-pressure is the engineering discipline of providing "just enough" resistance in a [[ralph-loops|Ralph loop]] to reject invalid AI generations (hallucinations) without slowing the loop so much that it becomes unproductive. It is part art, part engineering, and a core component of context engineering for AI-assisted development.

## The Principle

From [[source-ghuntley-collected|Geoffrey Huntley]]: "If you aren't capturing your back-pressure then you are failing as a software engineer."

The metaphor comes from woodworking: work with the grain, not against it. Back-pressure shapes the grain of AI output.

## Tuning Back-Pressure

Too little back-pressure → hallucinations and invalid code slip through undetected.
Too much back-pressure → the loop spins too slowly (long compile times, slow test suites) and becomes unproductive.

### Methods of Back-Pressure

1. **Choice of programming language** — Statically typed languages with strict compilation provide natural back-pressure. Huntley recommends "strict compilation" for best outcomes in [[porting-with-ai|porting]] and code generation.

2. **Fast test suites** — Tests provide signal on whether generated code is correct. The suite must be fast enough to not bottleneck the loop. This connects directly to [[test-driven-development]] — red-green-refactor is a form of back-pressure.

3. **Pre-commit hooks ("prek")** — Huntley's favorite. Under normal circumstances, pre-commit hooks are annoying because they slow down humans. But "now that humans aren't the ones doing the software development, it really doesn't matter anymore." Pre-commit hooks can enforce linting, formatting, type checking, and basic validation on every commit.

4. **Type systems** — Strong type systems catch errors at compile time, providing immediate feedback to the agent.

5. **[[codebase-architecture|Clean architecture]]** — Well-structured codebases with clear module boundaries make it easier for the agent to produce valid code and for tests to catch problems.

## Relationship to Context Engineering

Back-pressure is a key component of context engineering — the practice of shaping the AI's context to produce better outputs. The feedback from back-pressure mechanisms (test failures, type errors, lint violations) tells the agent what went wrong and guides the next iteration.

## Evaluator as Back-Pressure

In [[multi-agent-harness-design]], the evaluator agent serves as structured back-pressure for the generator. [[source-anthropic-harness-design|Anthropic's research]] found that separating evaluation from generation makes skeptical grading tractable — it's far easier to tune a standalone evaluator to be strict than to make a generator self-critical. The evaluator grades against concrete criteria with hard pass/fail thresholds, rejecting sprints that don't meet quality bars.

## Related

- [[ralph-loops]] — The loops that back-pressure governs
- [[test-driven-development]] — TDD as a form of back-pressure
- [[software-factories]] — Where back-pressure is automated at scale
- [[secure-code-generation]] — Back-pressure for security
- [[codebase-architecture]] — Architecture that enables effective back-pressure
