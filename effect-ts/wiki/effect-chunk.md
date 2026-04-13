---
title: Chunk
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Chunk

Immutable, persistent sequence optimized for functional streaming workloads. A `Chunk<A>` supports O(1) amortized append/prepend, O(log min(m,n)) concatenation, and structural sharing, while exposing a rich array-like API. `Chunk` is the unit of element batching inside Effect's `Stream` and `Channel` modules, so you will encounter it any time you work with streaming data.

## Key Exports
- `Chunk<A>` — immutable ordered collection
- `NonEmptyChunk<A>` — non-empty variant
- `empty`, `of`, `make`, `fromIterable`, `fromArray`, `range` — constructors
- `isChunk`, `isNonEmpty` — guards
- `append`, `prepend`, `appendAll`, `concat` — combine (efficient)
- `map`, `flatMap`, `filter`, `partition`, `dedupe` — transformation
- `head`, `last`, `get`, `tail`, `take`, `drop`, `split` — access and slicing
- `reduce`, `scan`, `join` — folds
- `toReadonlyArray`, `toArray` — conversion
- `zip`, `zipWith`, `cross` — combinators
- `Equivalence`, `Order` — typeclass instances

## Source
- `raw/effect-smol/packages/effect/src/Chunk.ts`

## Related
- [[effect-ts-v4]]
- [[effect-array]]
- [[effect-channel]]
