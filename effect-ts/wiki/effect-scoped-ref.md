---
title: ScopedRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ScopedRef

A mutable reference whose current value owns a `Scope`. Setting a new value acquires fresh resources inside a new scope and closes the old scope, guaranteeing cleanup of the previous value. Updates are serialized through an internal semaphore.

## Key Exports
- `ScopedRef<A>` — interface wrapping a `SynchronizedRef<[Scope, A]>`
- `make` — create from a pure lazy value
- `fromAcquire` — create from a resourceful acquire effect
- `get` / `getUnsafe` — read current value
- `set` — replace value, releasing old resources and acquiring new ones

## Source
- `raw/effect-smol/packages/effect/src/ScopedRef.ts`

## Related
- [[effect-ts-v4]]
- Built on [[effect-scope]] and [[effect-synchronized-ref]]
