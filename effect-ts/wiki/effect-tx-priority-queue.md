---
title: TxPriorityQueue
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxPriorityQueue

Transactional priority queue ordered by a user-supplied `Order<A>`. Backed by a sorted `Chunk` inside a `TxRef`, `take` returns the smallest element (retrying the transaction if empty) and `peek` observes it without removing. All mutations participate in STM so fibers can atomically coordinate producer/consumer patterns with priority semantics.

## Key Exports
- `empty` — construct with an `Order` instance
- `fromIterable` — sorted construction from iterable
- `make` — variadic curried constructor
- `offer` — insert preserving order
- `take` — remove and return smallest (retries when empty)
- `peek` — observe smallest without removing
- `size` / `isEmpty` — observers
- `toChunk` — snapshot as sorted `Chunk`

## Source
- `raw/effect-smol/packages/effect/src/TxPriorityQueue.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-queue]]
- [[effect-chunk]]
