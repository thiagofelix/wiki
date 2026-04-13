---
title: Loom (The Weaving Loom)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Loom (The Weaving Loom)

Loom is [[source-ghuntley-collected|Geoffrey Huntley's]] infrastructure orchestrator for [[ralph-loops]], representing the next evolution beyond basic agent loops. It is designed around the principle that everything built for the last 40 years of computing assumed human operators — Loom reimagines the development stack for autonomous agents first, humans second.

## Philosophy

> "I really do not like GitHub... everything that we have today has been built under the false assumption for humans. Now that we have this brand new computer, we can reimagine the last 40 years of computing and design it around autonomous agents first."

Loom's predecessor inspiration was Facebook/Meta's **Phabricator** (engineering system used by Facebook and Uber), which Huntley considered "ahead of its time" before GitHub made simpler tools dominant.

## Architecture Levels

Huntley describes a progression of autonomous software systems:

| Level | Name | Description |
|-------|------|-------------|
| Basic | Ralph Loop | Single agent, single repo, one task per loop |
| Mid | Gastown | Spinning plates — orchestrating multiple Ralph loops |
| High | Loom | Infrastructure for evolutionary software |
| Level 9 | Software Factory | Autonomous loops evolve products, optimize for revenue |

## Key Design Principles

- **Agents first, humans second** — UI and workflows designed for autonomous agents, with human oversight as a secondary concern
- **Recursive loops** — Loops on loops on loops. When one Ralph finishes, it can kick off another route with a different prompt
- **Minimal allocation** — Keep agents.md tiny, malloc only what's needed per loop
- **Nix builds** — Binary-based caching for instant deploys instead of traditional cargo builds

## Relationship to Software Factories

Loom is the infrastructure layer that enables [[software-factories]]. Where [[ralph-loops]] are the individual execution units, Loom orchestrates them into a coherent system that can evolve software products autonomously.

## Status

As of March 2026, Loom's source code is on GitHub but explicitly marked as personal infrastructure ("do not use it if your name is not Geoffrey Huntley"). It represents ideas Huntley has been developing for three years, with various prototypes built in 2025.

## Related

- [[ralph-loops]] — The loops Loom orchestrates
- [[software-factories]] — The end goal Loom enables
- [[building-an-agent]] — The basic unit Loom scales
- [[agents-md-history]] — How Loom configures its agents
- [[back-pressure]] — Engineering feedback within Loom's loops
