---
title: Predicate
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Predicate

Pure helpers for runtime checks, filtering, and type narrowing. A `Predicate<A>` is any `(a: A) => boolean`, while a `Refinement<A, B>` is a type-guard variant that narrows `A` to `B`. Provides composable combinators (`and`, `or`, `not`, `xor`), input adaptation (`mapInput`), compound checks (`Tuple`, `Struct`), and a battery of runtime type guards (`isString`, `isNumber`, `isObject`, `isIterable`, `isPromise`, etc.).

## Key Exports
- `Predicate<A>` — `(a: A) => boolean` interface
- `Refinement<A, B>` — narrowing type guard
- `and`, `or`, `not`, `xor` — logical combinators
- `mapInput` — contravariant input adaptation
- `compose` — chain refinements
- `Tuple`, `Struct` — lift element/field predicates
- `isString`, `isNumber`, `isBoolean`, `isObject`, `isIterable`, `isPromise`, `isTruthy`, `hasProperty` — runtime guards
- `isTupleOf`, `isTupleOfAtLeast` — length checks

## Source
- `raw/effect-smol/packages/effect/src/Predicate.ts`

## Related
- [[effect-ts-v4]]
- [[effect-filter]]
- [[effect-function]]
