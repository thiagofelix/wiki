---
title: Layer
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Layer

`Layer<ROut, E, RIn>` is a recipe for constructing services with dependencies, possibly effectfully and with scoped resource management. Layers compose, share instances via a `MemoMap`, and are the idiomatic way to wire dependency graphs in Effect. Provide them to effects via `Effect.provide`.

## Key Exports
- `Layer` — interface parameterized by output services, error, input services
- `MemoMap` — shared cache ensuring a layer is built at most once per scope
- `isLayer` — type guard
- `succeed` / `sync` — lift a value/thunk into a layer providing a service
- `effect` / `scoped` — build services effectfully, optionally with acquisition/release
- `merge` / `mergeAll` — combine independent layers
- `provide` / `provideMerge` — wire one layer's output into another's input
- `build` / `buildWithScope` / `buildWithMemoMap` — materialize services into a scope
- `fresh` — opt out of memoization for a single use
- `makeMemoMap` / `makeMemoMapUnsafe` — create a MemoMap explicitly

## Source
- `raw/effect-smol/packages/effect/src/Layer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-context]]
- [[effect-scope]]
- [[effect-managed-runtime]]
