---
title: Index (@effect/atom-vue)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Index (@effect/atom-vue)

Vue 3 bindings for Effect's `Atom` reactive system. Provides composables (`useAtom`, `useAtomValue`, `useAtomSet`, `useAtomRef`) that wrap atoms as Vue `Ref`/`ComputedRef`, plus an injection key for supplying a shared `AtomRegistry`. Also re-exports core reactivity modules (`Atom`, `AtomRef`, `AtomRegistry`, `AsyncResult`, `AtomHttpApi`, `AtomRpc`) under namespaces for ergonomic import.

## Key Exports
- `registryKey` — `InjectionKey<AtomRegistry>` for `provide`/`inject`
- `defaultRegistry` — fallback registry used when none injected
- `injectRegistry` — composable returning the current registry
- `useAtomValue` — subscribes an atom, returns `Readonly<Ref<A>>`
- `useAtomSet` — setter with `"value" | "promise" | "promiseExit"` modes; promise modes accept `{ signal }`
- `useAtom` — combined `[Ref<R>, setter]` tuple
- `useAtomRef` — subscribes an `AtomRef`, returns `Readonly<Ref<A>>`
- `Atom`, `AtomRef`, `AtomRegistry`, `AsyncResult` — namespace re-exports from `effect/unstable/reactivity`
- `AtomHttpApi`, `AtomRpc` — re-exports enabling HTTP/RPC atom bindings

## Notes
- Unlike react/solid bindings this package is a single `index.ts` module — no submodules.
- Atoms are accepted as thunk functions (`() => Atom<A>`) and wrapped in `computed` for re-evaluation.

## Source
- `raw/effect-smol/packages/atom/vue/src/index.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-reactivity-atom]]
- [[effect-reactivity-atom-registry]]
- [[effect-ts-v4]]
