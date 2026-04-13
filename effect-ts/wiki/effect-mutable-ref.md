---
title: MutableRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# MutableRef

Mutable reference cell with a functional API. Provides atomic compare-and-set, numeric increment/decrement, and boolean toggle helpers. Use where an `Effect`-scoped `Ref` would be overkill and simple imperative state is acceptable.

## Key Exports
- `MutableRef<T>` — interface with a mutable `current` field, `Pipeable`, `Inspectable`
- `make` — construct from an initial value
- `get` / `set` — read/write the current value
- `getAndSet` / `setAndGet` — swap with old/new return
- `compareAndSet` — CAS using `Equal.equals`
- `update` / `updateAndGet` / `getAndUpdate` — functional update
- `increment` / `decrement` — numeric helpers
- `toggle` — boolean flip

## Source
- `raw/effect-smol/packages/effect/src/MutableRef.ts`

## Related
- [[effect-ts-v4]]
