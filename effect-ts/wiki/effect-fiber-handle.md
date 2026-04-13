---
title: FiberHandle
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FiberHandle

A scoped container for a single fiber. Running a new effect through the handle interrupts any previously stored fiber, and closing the associated `Scope` interrupts the current occupant. Useful for "latest-wins" patterns — debouncing, replacing a subscription, or guaranteeing at most one in-flight background task.

## Key Exports
- `FiberHandle<A, E>` — single-slot fiber container
- `make` — scoped constructor
- `makeUnsafe` — unscoped constructor
- `run` — fork an effect into the handle (interrupts prior)
- `set`, `get`, `clear` — low-level slot management
- `join`, `awaitEmpty` — wait for completion
- `isFiberHandle` — guard

## Source
- `raw/effect-smol/packages/effect/src/FiberHandle.ts`

## Related
- [[effect-ts-v4]]
- [[effect-fiber]]
- [[effect-fiber-map]]
- [[effect-fiber-set]]
