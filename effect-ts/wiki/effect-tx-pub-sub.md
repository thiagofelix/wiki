---
title: TxPubSub
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxPubSub

Transactional publish/subscribe hub built from TxRefs and TxQueues. Each subscriber gets its own `TxQueue` and receives a copy of every message published while subscribed. Supports four backpressure strategies — `bounded` (publisher retries on full), `unbounded`, `dropping` (discard new), and `sliding` (evict oldest) — all under STM so publish and subscribe operations compose atomically.

## Key Exports
- `bounded` — publisher retries until space available
- `unbounded` — unlimited per-subscriber capacity
- `dropping` — newest messages dropped when full
- `sliding` — oldest messages evicted when full
- `subscribe` — scoped acquisition of a subscriber `TxQueue`
- `publish` — broadcast a message to all subscribers
- `publishAll` — broadcast multiple messages
- `shutdown` — terminate the hub and all subscribers
- `isShutdown` / `size` / `capacity` — observers

## Source
- `raw/effect-smol/packages/effect/src/TxPubSub.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-queue]]
- [[effect-pub-sub]]
- [[effect-tx-subscription-ref]]
