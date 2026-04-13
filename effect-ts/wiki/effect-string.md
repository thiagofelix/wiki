---
title: String
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# String

Utilities and typeclass instances for the primitive `string` type. Provides type-level string concatenation, case conversions that track literal types, guards, ordering, equivalence, and standard string combinators.

## Key Exports
- `String` — reference to the global `String` constructor
- `isString` — type refinement guard
- `Order` — lexicographic order instance
- `Equivalence` — strict equality instance
- `empty` — the `""` literal
- `Concat<A, B>` — type-level concatenation
- `concat` — runtime concat (dual form)
- `toUpperCase` / `toLowerCase` / `capitalize` / `uncapitalize` — case transforms with literal-type tracking

## Source
- `raw/effect-smol/packages/effect/src/String.ts`

## Related
- [[effect-ts-v4]]
- Related to Equivalence, Order, Predicate, Reducer
