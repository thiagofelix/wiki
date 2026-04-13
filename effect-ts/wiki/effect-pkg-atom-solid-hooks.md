---
title: Hooks (@effect/atom-solid)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Hooks (@effect/atom-solid)

SolidJS composables that adapt Effect's `Atom` reactive system to Solid's fine-grained reactivity. Atoms are supplied as accessor functions (`() => Atom<A>`) so that Solid can re-run subscriptions when the selected atom changes, and results are returned as Solid `Accessor<A>` signals.

## Key Exports
- `useAtomValue` — subscribe to an atom, returns `Accessor<A>`; supports optional map fn
- `useAtomSet` — returns a setter with `"value" | "promise" | "promiseExit"` modes
- `useAtom` — combined `[Accessor<R>, setter]` for a `Writable` atom
- `useAtomMount` — keeps an atom mounted via `createComputed` + `onCleanup`
- `useAtomRefresh` — returns a callback to `registry.refresh` the atom
- `useAtomSubscribe` — runs side-effecting callback via `createEffect`
- `useAtomInitialValues` — seeds atoms once per registry
- `useAtomResource` — bridges `AsyncResult` atom to Solid's `createResource`, with optional `suspendOnWaiting`
- `useAtomRef` — subscribe to an `AtomRef`, returning `Accessor<A>`
- `useAtomRefProp` / `useAtomRefPropValue` — derive child `AtomRef` by property key

## Source
- `raw/effect-smol/packages/atom/solid/src/Hooks.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-solid-registrycontext]]
- [[effect-unstable-reactivity-atom]]
- [[effect-ts-v4]]
