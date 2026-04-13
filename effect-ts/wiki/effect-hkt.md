---
title: HKT
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HKT

Higher-Kinded Type encoding used internally by Effect to express type classes that abstract over type constructors (Array, Option, Effect, etc.). A `TypeLambda` encodes the "shape" of a type constructor with four positions — `In` (contravariant), `Out2` and `Out1` (covariant), and `Target` (invariant) — and `Kind` resolves a lambda to a concrete type. Rarely needed directly by application code but essential for library authors writing generic combinators.

## Key Exports
- `TypeLambda` — base interface with `In`, `Out2`, `Out1`, `Target` slots
- `Kind<F, In, Out2, Out1, Target>` — resolve a TypeLambda
- `TypeClass<F>` — base interface for type classes
- `URI` — unique symbol tying type classes to lambdas

## Source
- `raw/effect-smol/packages/effect/src/HKT.ts`

## Related
- [[effect-ts-v4]]
- [[effect-function]]
- [[effect-types]]
