---
title: Queue
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Queue

Asynchronous single-producer/multi-consumer queue (replacing Effect 3.x `Mailbox`). Supports bounded, unbounded, dropping, and sliding strategies, plus explicit done/fail signals so consumers see stream-style completion. Exposes separate `Enqueue` (write-only) and `Dequeue` (read-only) views to enforce direction-of-flow at the type level.

## Key Exports
- `Queue<A, E>` — full-duplex queue
- `Enqueue<A, E>`, `Dequeue<A, E>` — directional views
- `bounded(capacity)`, `unbounded()`, `dropping(capacity)`, `sliding(capacity)` — constructors
- `offer`, `offerAll`, `offerUnsafe` — producer ops
- `take`, `takeAll`, `takeN`, `takeBetween` — consumer ops
- `done`, `fail`, `end`, `shutdown` — termination
- `isQueue`, `isEnqueue`, `isDequeue`, `asEnqueue`, `asDequeue` — guards and conversions

## Source
- `raw/effect-smol/packages/effect/src/Queue.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pub-sub]]
- [[effect-stream]]
