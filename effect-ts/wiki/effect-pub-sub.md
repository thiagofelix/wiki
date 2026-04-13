---
title: PubSub
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# PubSub

An asynchronous multi-producer / multi-subscriber message hub. Publishers push values and each subscriber receives every message published after it subscribed. Supports bounded, unbounded, dropping, and sliding backpressure strategies, along with replay windows for late subscribers. Subscriptions are scoped, so they are unsubscribed automatically at scope close.

## Key Exports
- `PubSub<A>` — pipeable pub/sub hub
- `bounded(capacity)`, `unbounded()`, `dropping(capacity)`, `sliding(capacity)` — constructors
- `publish(self, value)`, `publishAll(self, values)` — producer ops
- `subscribe(self)` — scoped subscription
- `take`, `takeAll`, `takeUpTo` — subscriber reads
- `shutdown(self)`, `isShutdown(self)` — lifecycle
- `PubSub.Strategy<A>` — backpressure strategy interface
- `PubSub.Atomic<A>`, `BackingSubscription<A>`, `ReplayWindow<A>` — low-level models

## Source
- `raw/effect-smol/packages/effect/src/PubSub.ts`

## Related
- [[effect-ts-v4]]
- [[effect-queue]]
- [[effect-stream]]
