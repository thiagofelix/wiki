---
title: TxSubscriptionRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxSubscriptionRef

Transactional reference that broadcasts every committed change to subscribers. Internally pairs a `TxRef<A>` (current value) with a `TxPubSub<A>` (change notifications). Subscribers receive the current value followed by every subsequent update through a `TxQueue`, or as a `Stream`. Updates and publishes happen atomically within the same transaction, so subscribers never miss or observe partial state.

## Key Exports
- `make` — create with an initial value
- `get` — read the current value
- `set` — write a new value and publish it
- `update` — apply a function and publish the result
- `modify` — apply `[return, newValue]` function and publish
- `changes` — scoped subscription returning a `TxQueue<A>`
- `changesStream` — subscription as a `Stream<A>`

## Source
- `raw/effect-smol/packages/effect/src/TxSubscriptionRef.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-pub-sub]]
- [[effect-tx-queue]]
- [[effect-subscription-ref]]
