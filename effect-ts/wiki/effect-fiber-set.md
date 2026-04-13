---
title: FiberSet
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FiberSet

An unkeyed collection of fibers, backed by a plain `Set`. When the associated `Scope` closes, all fibers in the set are interrupted; completed fibers are removed automatically. Useful when you need to track a dynamic pool of concurrent workers without key identity.

## Key Exports
- `FiberSet<A, E>` — iterable fiber container
- `make` — scoped constructor
- `run` — fork into the set
- `add`, `remove`, `size`, `clear` — set operations
- `join`, `awaitEmpty` — wait for completion
- `isFiberSet` — guard

## Source
- `raw/effect-smol/packages/effect/src/FiberSet.ts`

## Related
- [[effect-ts-v4]]
- [[effect-fiber]]
- [[effect-fiber-handle]]
- [[effect-fiber-map]]
