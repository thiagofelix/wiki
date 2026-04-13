---
title: Hydration (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Hydration (unstable)

SSR/client handoff support for the reactive system. Dehydrates the `AtomRegistry` into an array of `DehydratedAtom` values that can be serialized on the server and re-applied to a fresh registry on the client, including optional async-result continuation across the boundary.

## Key Exports
- `DehydratedAtom`, `DehydratedAtomValue` — opaque/record types
- `dehydrate(registry, options?)` — serialize current registry state
- `options.encodeInitialAs` — `"ignore" | "promise" | "value-only"`
- `hydrate(registry, dehydratedState)` — apply state to a new registry
- `toValues` — unwrap to `DehydratedAtomValue[]`
- Subscribes to `Initial` atoms to forward resolved values via `resultPromise`
- Only `Serializable` atoms are dehydrated

## Source
- `raw/effect-smol/packages/effect/src/unstable/reactivity/Hydration.ts`

## Related
- [[effect-reactivity]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-atom-registry]]
