---
title: packages/atom (@effect/atom-*)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# packages/atom (@effect/atom-*)

UI-framework bindings that surface Effect's reactive `Atom` system (defined in `effect/unstable/reactivity`) into component frameworks. Rather than reimplementing state, these packages wrap a shared `AtomRegistry` in a framework-native context/provider and expose idiomatic hooks/composables for reading, writing, subscribing, suspending, and hydrating atoms. All three subpackages track a single `AtomRegistry` per subtree so any atom — including derived, async, and RPC-backed atoms — can drive UI updates.

## Subpackages
- `@effect/atom-react` — React 19 bindings; uses `useSyncExternalStore`, suspense, SSR hydration, scoped atoms
- `@effect/atom-solid` — SolidJS bindings; atoms exposed as `Accessor<A>` signals and via `createResource`
- `@effect/atom-vue` — Vue 3 bindings; atoms exposed as `Ref<A>`/`ComputedRef<A>` with injection-based registry

## Entries — React
- [[effect-pkg-atom-react-hooks]] — `useAtomValue`, `useAtom`, `useAtomSet`, `useAtomSuspense`, `useAtomRef`, etc.
- [[effect-pkg-atom-react-registrycontext]] — `RegistryContext`, `RegistryProvider`, React scheduler integration
- [[effect-pkg-atom-react-reacthydration]] — `HydrationBoundary` for SSR dehydrated atom state
- [[effect-pkg-atom-react-scopedatom]] — context-scoped per-subtree atom factory

## Entries — Solid
- [[effect-pkg-atom-solid-hooks]] — accessor-based composables plus `useAtomResource`
- [[effect-pkg-atom-solid-registrycontext]] — Solid registry context/provider

## Entries — Vue
- [[effect-pkg-atom-vue-index]] — single-module composables + injection key + namespace re-exports

## Shared Concepts
- Registry lifecycle — per-tree registries disposed on unmount (`defaultIdleTTL` ~400ms)
- Writable atom modes — `"value"` (sync set), `"promise"`, `"promiseExit"` for `AsyncResult` atoms
- Hydration path — delegates to `effect/unstable/reactivity/Hydration`

## Related
- [[effect-ts-v4]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-atom-registry]]
- [[effect-reactivity-atom-ref]]
- [[effect-reactivity-hydration]]
