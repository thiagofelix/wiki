---
title: AtomRegistry (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# AtomRegistry (unstable)

Central registry holding mounted atom state, computing dependencies, scheduling updates, and broadcasting changes to subscribers. The registry is the runtime backing the reactive system and exposes imperative `get`/`set`/`update`/`mount`/`subscribe` operations used by UI bindings.

## Key Exports
- `AtomRegistry` — interface with `get`, `set`, `update`, `modify`, `refresh`, `mount`, `subscribe`, `reset`, `dispose`
- `isAtomRegistry`, `TypeId`
- `Node<A>` — internal node with atom, value, subscribers
- `make` — constructs a registry with scheduler config
- `layer` — `Layer` providing `AtomRegistry`
- `getNodes` — inspect registered nodes (for devtools)
- `setSerializable` — hydration entry point
- Hooks `onNodeAdded`/`onNodeRemoved`
- Uses `MixedScheduler` for synchronous + async updates

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/AtomRegistry.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-hydration]]
