---
title: SynchronizedRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SynchronizedRef

A `Ref` whose updates are serialized through an internal semaphore, supporting effectful update functions without race conditions. Useful when the transformation producing the new value is itself an `Effect` that must run with mutual exclusion against other updates.

## Key Exports
- `SynchronizedRef<A>` — extends `Ref<A>` with a backing ref + semaphore
- `make` / `makeUnsafe` — construct
- `get` / `getUnsafe` — read current value
- `getAndSet` / `getAndUpdate` / `getAndUpdateSome` — atomic combinators
- `getAndUpdateEffect` / `modifyEffect` / `modifySomeEffect` — effectful variants
- `modify` / `modifySome` — atomic compute-and-return

## Source
- `raw/effect-smol/packages/effect/src/SynchronizedRef.ts`

## Related
- [[effect-ts-v4]]
- Extends Ref; backs [[effect-scoped-ref]]; relates to [[effect-subscription-ref]]
