---
title: Resource
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Resource

A `Resource<A, E>` is a value loaded into memory that can be refreshed manually or on a `Schedule`. Internally it holds a `ScopedRef` so refreshes release the previous value before acquiring the new one. Useful for cached configuration, signing keys, feature flags, or any resource that must be periodically rebuilt.

## Key Exports
- `Resource<A, E>` — pipeable resource handle
- `manual(acquire)` — scoped constructor requiring explicit `refresh`
- `auto(acquire, schedule)` — scoped constructor with background refresh
- `get(self)` — read current value (fails with last `E` if acquisition failed)
- `refresh(self)` — force reacquire
- `isResource` — guard

## Source
- `raw/effect-smol/packages/effect/src/Resource.ts`

## Related
- [[effect-ts-v4]]
- [[effect-scoped-ref]]
- [[effect-schedule]]
