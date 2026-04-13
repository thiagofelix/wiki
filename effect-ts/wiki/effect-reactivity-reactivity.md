---
title: Reactivity (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Reactivity (unstable)

Generic key-based invalidation bus used by `Atom`, `EventLog`, and SQL integration layers. Consumers subscribe to sets of keys and register mutation/query helpers that automatically invalidate dependent subscribers when keyed effects complete.

## Key Exports
- `Reactivity` — service with `invalidate`, `invalidateUnsafe`, `mutation`, `query`, `stream`, `registerUnsafe`, `withBatch`
- `make` — constructs a reactivity instance
- `layer` — provides the service
- Keys may be arrays or records of arrays (hashed deterministically)
- `mutation(keys, effect)` — runs effect then invalidates keys
- `query(keys, effect)` — returns a `Queue` of updated results
- `stream(keys, effect)` — returns a `Stream` of updated results
- `withBatch` — batches invalidations until the inner effect finishes

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/Reactivity.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-eventlog-event-log]]
