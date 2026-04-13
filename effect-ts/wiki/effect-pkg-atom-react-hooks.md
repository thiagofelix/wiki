---
title: Hooks (@effect/atom-react)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Hooks (@effect/atom-react)

React hooks for reading, writing, mounting, refreshing, and subscribing to Effect `Atom` values from a shared `AtomRegistry`. Uses `React.useSyncExternalStore` for tear-free reads and supports `AsyncResult` atoms with suspense and promise/exit write modes.

## Key Exports
- `useAtomValue` — read an atom's current value (with optional mapping fn); auto subscribes
- `useAtomSet` — returns a setter for a `Writable` atom; modes `"value" | "promise" | "promiseExit"`
- `useAtom` — combined `[value, set]` tuple for a writable atom
- `useAtomMount` — mount an atom without reading it (keeps it alive)
- `useAtomRefresh` — returns a callback that re-runs the atom
- `useAtomSubscribe` — run a side-effecting callback when an atom changes
- `useAtomInitialValues` — seed atoms with initial values (once per registry)
- `useAtomSuspense` — reads an `AsyncResult` atom, suspending on Initial/Waiting; optionally rethrows Failure
- `useAtomRef` — subscribe to an `AtomRef` and return its current value
- `useAtomRefProp` — derive a child `AtomRef` for a property key
- `useAtomRefPropValue` — shorthand combining the two above

## Source
- `raw/effect-smol/packages/atom/react/src/Hooks.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-react-registrycontext]]
- [[effect-unstable-reactivity-atom]]
- [[effect-ts-v4]]
