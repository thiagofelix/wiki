---
title: TxQueue
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxQueue

Transactional queue with STM semantics, backed by a `TxChunk` plus a lifecycle `State` (Open → Closing → Done). Supports bounded, unbounded, dropping, and sliding strategies. Splits the interface into write-only `TxEnqueue` and read-only `TxDequeue` for variance-correct APIs. Offers and takes retry the transaction when empty/full, enabling blocking producer/consumer coordination.

## Key Exports
- `bounded` / `unbounded` / `dropping` / `sliding` — strategy constructors
- `offer` / `offerAll` — enqueue (retries or drops depending on strategy)
- `take` / `takeAll` / `takeN` / `poll` — dequeue operations
- `end` / `fail` / `done` — lifecycle transitions
- `awaitDone` — wait for terminal state
- `size` / `capacity` / `isFull` / `isEmpty` — observers
- `TxEnqueue` / `TxDequeue` — variance-typed sub-interfaces
- `State` — union of Open / Closing / Done

## Source
- `raw/effect-smol/packages/effect/src/TxQueue.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-chunk]]
- [[effect-queue]]
- [[effect-tx-pub-sub]]
