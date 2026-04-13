---
title: TxDeferred
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxDeferred

Transactional write-once cell — the STM counterpart to `Deferred`. Backed by a `TxRef<Option<Result<A, E>>>`, readers that call `await` inside a transaction retry until the deferred is completed; the first writer wins and subsequent writes are no-ops returning `false`. Composes with other Tx primitives for atomic rendezvous between fibers.

## Key Exports
- `make` — create an uncompleted TxDeferred
- `await` — read the value, retrying until completed
- `poll` — non-blocking peek returning `Option<Result<A, E>>`
- `done` — complete with a `Result`
- `succeed` — complete with a success value
- `fail` — complete with an error
- `isDone` — check completion state

## Source
- `raw/effect-smol/packages/effect/src/TxDeferred.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-deferred]]
