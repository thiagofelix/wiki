---
title: FiberMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# FiberMap

A keyed collection of fibers backed by a `MutableHashMap`. Running an effect with a key forks it and stores the fiber under that key, interrupting any prior entry. All remaining fibers are interrupted when the parent `Scope` closes, and completed fibers are removed automatically. Ideal for managing per-user sessions, per-request handlers, or any keyed background workers.

## Key Exports
- `FiberMap<K, A, E>` — keyed fiber container (iterable)
- `make` — scoped constructor
- `run` — fork and register under key (replaces existing)
- `set`, `get`, `remove`, `has`, `size` — map operations
- `join`, `awaitEmpty` — wait for completion
- `clear` — interrupt all members
- `isFiberMap` — guard

## Source
- `raw/effect-smol/packages/effect/src/FiberMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-fiber]]
- [[effect-fiber-handle]]
- [[effect-fiber-set]]
