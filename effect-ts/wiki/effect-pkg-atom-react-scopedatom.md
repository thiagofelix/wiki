---
title: ScopedAtom (@effect/atom-react)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ScopedAtom (@effect/atom-react)

Utility for binding an `Atom` instance to a React context-scoped provider. Useful when you need a distinct atom instance per subtree (e.g. per feature, per user input), rather than sharing a single module-level atom. The factory may optionally accept an `Input` so consumers can parameterize the atom from props.

## Key Exports
- `ScopedAtom` — interface with `use()`, `Provider`, and `Context`
- `make` — constructor from a factory `() => Atom` or `(input) => Atom`
- `TypeId` — brand type id `"~@effect/atom-react/ScopedAtom"`

## Usage Shape
- `Counter = ScopedAtom.make(() => Atom.make(0))`
- Wrap subtree in `<Counter.Provider>` (or `<Counter.Provider value={input}>`)
- Inside descendants: `const atom = Counter.use(); const value = useAtomValue(atom)`
- Throws if `use()` is called outside its `Provider`

## Source
- `raw/effect-smol/packages/atom/react/src/ScopedAtom.ts`

## Related
- [[effect-pkg-atom]]
- [[effect-pkg-atom-react-hooks]]
- [[effect-reactivity-atom]]
- [[effect-ts-v4]]
