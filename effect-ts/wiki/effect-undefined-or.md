---
title: UndefinedOr
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# UndefinedOr

Allocation-free helpers for values of type `A | undefined`, where `undefined` means "no value". Offers an `Option`-like API without the wrapper cost, suitable when your domain already treats `undefined` as absence and `A` itself never includes `undefined`.

## Key Exports
- `map` — transform the defined value
- `match` — eliminate with `onUndefined` / `onDefined`
- `getOrThrow` / `getOrThrowWith` — unwrap or throw
- `liftThrowable` — convert throwing fn to `A | undefined`
- `makeReducer` — first-wins / combine Reducer
- `makeCombinerFailFast` / `makeReducerFailFast` — fail-fast on any undefined

## Source
- `raw/effect-smol/packages/effect/src/UndefinedOr.ts`

## Related
- [[effect-ts-v4]]
- Lighter-weight alternative to Option; pairs with Combiner/Reducer
