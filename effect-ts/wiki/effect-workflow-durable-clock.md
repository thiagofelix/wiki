---
title: DurableClock (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DurableClock (unstable)

Durable sleep primitive for workflows. Short sleeps are executed in-memory as a regular `Activity`; longer sleeps are scheduled with the `WorkflowEngine` so that the workflow can be suspended and resumed later without keeping a fiber alive. Backed by a `DurableDeferred` that is completed when the timer fires.

## Key Exports
- `DurableClock` — model holding a name, duration, and backing deferred
- `make` — build a `DurableClock` value
- `sleep` — yieldable workflow sleep with configurable in-memory threshold

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/DurableClock.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-durable-deferred]]
- [[effect-workflow-workflow-engine]]
- [[effect-workflow-activity]]
