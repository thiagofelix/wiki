---
title: Transferable (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Transferable (unstable)

Support for passing `globalThis.Transferable` values (e.g. `ArrayBuffer`, `MessagePort`, `ImageData`) across worker boundaries without copying. Provides a `Collector` service accumulating transferables during schema encoding, plus schema helpers that attach transferable lists to values as they flow through codecs.

## Key Exports
- `Collector` — service with `addAll`, `read`, `clear` over an in-memory list
- `makeCollectorUnsafe`, `makeCollector`
- `addAll` — contextual effect adding transferables when a collector is in scope
- `getterAddAll` — `SchemaGetter` variant for pipeline integration
- `schema<S>(f)` — annotates a schema to emit transferables on encode
- `ImageData`, `MessagePort`, `Uint8Array` — predefined transferable schemas
- `Transferable<S>` — schema type with decodeTo passthrough

## Source
- `raw/effect-smol/packages/effect/src/unstable/workers/Transferable.ts`

## Related
- [[effect-workers]]
- [[effect-workers-worker]]
- [[effect-schema]]
