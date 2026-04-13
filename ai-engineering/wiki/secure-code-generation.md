---
title: Secure Code Generation
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Secure Code Generation

Secure code generation is the challenge of ensuring AI-generated code is safe and secure. [[source-ghuntley-collected|Geoffrey Huntley]] argues that security cannot be bolted on via MCP servers or Cursor rules — it must be engineered into the system through [[back-pressure]] mechanisms, architectural decisions, and proper engineering practices.

## The Anti-Pattern

> "If anyone pitches you on the idea that you can achieve secure code generation via an MCP tool or Cursor rules, run, don't walk."

Security through prompting or tool-level enforcement is insufficient because:
- Prompts are suggestions, not guarantees
- MCP servers operate at the wrong abstraction level
- Rules files can be ignored or circumvented by the model

## The Engineering Approach

Security in AI-generated code must come from the same principles that secure human-written code, amplified for autonomous generation:

1. **[[back-pressure]]** — Type systems, strict compilation, pre-commit hooks, and test suites catch security issues before code is committed
2. **Sandboxing** — Agent execution environments must be isolated
3. **Credential management** — Agents need secure access to secrets without exposing them in context
4. **Risk-based review** — High-risk changes (database migrations, auth changes) halt for manual review; low-risk changes ship automatically (see [[software-factories]])
5. **[[codebase-architecture|Architecture]]** — Well-structured codebases with clear boundaries make it harder for agents to introduce security flaws

## Context

Huntley has not written code by hand for nine months. His perspective: "Within the next year, large swaths of code in business will no longer be artisanal hand-crafted." This makes secure generation not just a nice-to-have but an industry-critical concern.

## Related

- [[back-pressure]] — The primary mechanism for secure generation
- [[software-factories]] — Risk-based shipping at scale
- [[ralph-loops]] — The loops that need securing
- [[software-development-vs-engineering]] — Security is an engineering concern
- [[codebase-architecture]] — Architecture that prevents security flaws
