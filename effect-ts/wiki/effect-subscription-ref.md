---
title: SubscriptionRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SubscriptionRef

A mutable reference whose updates are broadcast through a PubSub, so subscribers receive a stream of current and subsequent values. Backed by an internal semaphore for serialized writes and a replay-1 PubSub so new subscribers always see the latest value.

## Key Exports
- `SubscriptionRef<A>` — interface with `value`, `semaphore`, `pubsub`
- `isSubscriptionRef` — guard
- `make` — construct with an initial value
- `changes` — `Stream<A>` of current + future values
- `get` / `getUnsafe` — read current value
- `getAndSet` / `getAndUpdate` — atomic update helpers
- `set` / `update` — mutate and publish

## Source
- `raw/effect-smol/packages/effect/src/SubscriptionRef.ts`

## Related
- [[effect-ts-v4]]
- Combines [[effect-synchronized-ref]] semantics with PubSub + [[effect-stream]]
