---
title: RcMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RcMap

A reference-counted map of scoped resources keyed by arbitrary `K`. On `get`, the resource is lazily acquired via a `lookup` function, and its ref count is incremented; when all handles close their scopes, an idle TTL clock starts before actual release. Useful for pooling per-key resources (DB connections per tenant, clients per host) with bounded capacity and automatic cleanup.

## Key Exports
- `RcMap<K, A, E>` — pipeable map of ref-counted resources
- `make({ lookup, capacity?, idleTimeToLive? })` — scoped constructor
- `get(self, key)` — acquire/increment; returns scoped Effect
- `invalidate(self, key)` — force release
- `touch(self, key)` — reset idle timer
- `keys(self)` — current keys
- `State.Open`, `State.Closed`, `State.Entry` — internal state models

## Source
- `raw/effect-smol/packages/effect/src/RcMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-rc-ref]]
- [[effect-pool]]
