---
title: TxRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxRef

The core Software Transactional Memory primitive in Effect v4 — a mutable reference readable and writable only within a transaction. Every access is recorded in the transaction's journal (version + value snapshot); at commit time the runtime validates that no concurrent transaction modified any accessed TxRef. On conflict (or explicit `Effect.txRetry`) the entire transaction re-runs. All other `Tx*` primitives are built on TxRef.

## Key Exports
- `make` — create a new TxRef with an initial value (`Effect`)
- `makeUnsafe` — synchronous constructor for outside Effect contexts
- `get` — read the current value within a transaction
- `set` — write a new value
- `update` — apply a function to the value
- `modify` — apply a function returning `[returnValue, newValue]`
- `TxRef<A>` — interface carrying `version`, `pending` waiters, and `value`

## Source
- `raw/effect-smol/packages/effect/src/TxRef.ts`

## Related
- [[effect-ts-v4]]
- [[effect-mutable-ref]]
- [[effect-tx-chunk]]
- [[effect-tx-hash-map]]
- [[effect-tx-queue]]
- [[effect-tx-semaphore]]
