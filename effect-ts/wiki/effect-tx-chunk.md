---
title: TxChunk
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxChunk

Transactional variant of `Chunk` built on top of `TxRef<Chunk<A>>`. Provides STM-style atomic operations on a sequential collection — appends, prepends, slices, and reads all participate in the enclosing transaction, retrying automatically on conflict. Single operations commit immediately; multi-step sequences wrap in `Effect.tx` for atomicity.

## Key Exports
- `make` — create from an existing `Chunk`
- `empty` — create an empty TxChunk
- `fromIterable` — create from any iterable
- `makeUnsafe` — wrap an existing `TxRef<Chunk<A>>`
- `get` — read current chunk value
- `append` / `prepend` — add elements at either end
- `size` / `isEmpty` — observe shape
- `ref` — underlying `TxRef<Chunk<A>>` for advanced composition

## Source
- `raw/effect-smol/packages/effect/src/TxChunk.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-chunk]]
- [[effect-tx-queue]]
