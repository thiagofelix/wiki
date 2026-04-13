---
title: DeliverAt (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DeliverAt (unstable)

Trait for payloads that carry a scheduled future delivery time. Cluster messaging uses this to defer dispatch until the `DateTime` returned by the symbol method.

## Key Exports
- `symbol` — property key used to implement the trait
- `DeliverAt` — interface producing a `DateTime` via `[symbol]()`
- `isDeliverAt` — type guard
- `toMillis` — read the scheduled epoch millis or `null` if not a `DeliverAt`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/DeliverAt.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-message-storage]]
- [[effect-ts-v4]]
