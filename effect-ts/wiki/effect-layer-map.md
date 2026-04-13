---
title: LayerMap
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# LayerMap

A dynamic map of `Layer`s keyed by an arbitrary value, backed by an `RcMap` for reference counting and idle expiry. Use it when you need to provide different service instances per-request, per-tenant, or per-environment while sharing construction across callers.

## Key Exports
- `LayerMap` — interface with `get`, `contextEffect`, `invalidate`, plus `rcMap`
- `make` — construct a LayerMap from a `lookup` function; supports `idleTimeToLive` and `preloadKeys`
- `fromRecord` — build a LayerMap from a static record of layers
- `get` — retrieve a `Layer` for a key (re-materializes context on demand)
- `contextEffect` — directly acquire a built context in a scope
- `invalidate` — drop the cached resource for a key

## Source
- `raw/effect-smol/packages/effect/src/LayerMap.ts`

## Related
- [[effect-ts-v4]]
- [[effect-layer]]
- [[effect-rc-map]]
