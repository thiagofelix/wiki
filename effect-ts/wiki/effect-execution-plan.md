---
title: ExecutionPlan
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ExecutionPlan

Declarative fallback plans for running effects across different contexts or layers. An `ExecutionPlan` chains ordered steps, each with its own provided `Context`/`Layer`, retry `attempts`, optional `while` predicate, and retry `schedule`. Used via `Effect.withExecutionPlan` / `Stream.withExecutionPlan` to try each step until success or exhaustion — ideal for AI model fallbacks, multi-region failover, or tiered resource routing.

## Key Exports
- `ExecutionPlan<Config>` — ordered multi-step plan interface
- `make` — construct a plan from one or more step configs
- `isExecutionPlan` — type guard
- `TypeId` — `"~effect/ExecutionPlan"`
- Step config: `provide`, `attempts`, `while`, `schedule`

## Source
- `raw/effect-smol/packages/effect/src/ExecutionPlan.ts`

## Related
- [[effect-ts-v4]]
- [[effect-effect]]
- [[effect-layer]]
- [[effect-schedule]]
