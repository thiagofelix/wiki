---
title: Utils
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Utils

Internal support for generator-based monadic syntax (`Effect.gen`, `Option.gen`, `Result.gen`, ...) and higher-kinded variance encodings. Provides `SingleShotGen`, a one-shot `IterableIterator` wrapper that lets yieldable types participate in `yield*`, plus type-level `Gen` and `Variance` signatures for TypeLambdas.

## Key Exports
- `SingleShotGen<T, A>` — one-shot iterator yielding its wrapped value once
- `Variance<F, R, O, E>` — type-level variance marker for a TypeLambda
- `Gen<F>` — type-level signature for `gen`-style APIs over a TypeLambda
- Related `Kind` / `TypeLambda` usage from HKT

## Source
- `raw/effect-smol/packages/effect/src/Utils.ts`

## Related
- [[effect-ts-v4]]
- Works with HKT and [[effect-types]]; enables generator syntax across modules
