---
title: Software Factories
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Software Factories

Software factories are autonomous systems that evolve software products and optimize them automatically, representing the furthest evolution of [[ralph-loops]]. [[source-ghuntley-collected|Geoffrey Huntley]] describes this as moving from "spinning plates and orchestration" to "evolutionary software" — systems where products are developed, tested, shipped, and improved by AI agents with minimal human intervention.

## The Levels

Huntley describes a progression:
- **Brick by brick** — Traditional software development (Jenga-style, manual)
- **Ralph loops** — Agent runs in a loop, one task at a time, human watches
- **Gastown** — Orchestration layer for spinning plates across multiple loops
- **The Weaving Loom** — Infrastructure for evolutionary software; agents evolve products and optimize automatically for revenue generation
- **Level 9** — Autonomous loops that evolve products and optimize for business outcomes

## Rapid Application Development (RAD) Is Back

Huntley argues we're returning to an era of hyper-personalized software, similar to the Microsoft Access/Delphi/Visual Basic era of 2000:

> "Back in the year 2000, every business had hyper-personalized software. They didn't have to bend or conform to someone else's product vision."

His platform Latent Patterns demonstrates this: the product itself is the IDE. Users can enter "designer mode" and modify the application from within it, then click "Launch Agent" to ship changes through a risk-based deployment pipeline.

## The Embedded Factory Pattern

In Latent Patterns, Huntley demonstrated building by "ripping farts into the coding harness":
- "Hey, I want PostHog" → first-party analytics
- "Hey, I want PipeDrive, Trello, and ZenDesk" → CRM, project management, support desk
- Clone Calendly → meeting scheduling with AI transcription bot
- Sales automation using Challenger/SPIN selling as LLM prompts over meeting transcripts

Everything is first-party, vertically integrated, and built by agents. This is what [[model-first-companies]] look like in practice.

## Risk-Based Shipping

Instead of manual code review for everything:
- Low risk changes → ship automatically
- High risk (e.g., database schema migrations) → halt for manual review
- "You need to watch the loops. Watch the inferencing because that's where your learning is at."

The goal: "On the loop, not in the loop."

## Killing CI/CD

Huntley questions whether CI/CD as it exists today is an anti-pattern in this new world:
> "Every second counts; even the 60 seconds for CI/CD deployments is too long."

The logical destination: live-editing a program's memory and control flow, where the product is developed from within the product itself.

## Multi-Agent Harness Architecture

[[source-anthropic-harness-design|Anthropic's harness research]] demonstrates a concrete path from Ralph loops to software factories via a three-agent architecture (planner → generator → evaluator). Their system produced a working Digital Audio Workstation in under 4 hours for $125, with the evaluator agent using Playwright to click through the running application and grade against sprint contracts. As models improve, harness complexity can be reduced — components that encode assumptions about model limitations should be stripped when no longer needed.

## Related

- [[ralph-loops]] — The foundational pattern
- [[loom]] — The infrastructure orchestrator
- [[multi-agent-harness-design]] — Planner/generator/evaluator architectures
- [[back-pressure]] — How loops maintain quality
- [[model-first-companies]] — The business model this enables
- [[ai-industry-disruption]] — The economic implications
- [[software-development-vs-engineering]] — Engineers design the factories
- [[source-anthropic-harness-design]] — Anthropic's research on autonomous coding harnesses
