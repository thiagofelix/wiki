---
title: TxSemaphore
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxSemaphore

Transactional counting semaphore backed by a `TxRef<number>`. Acquire operations retry the enclosing transaction when permits are insufficient, providing STM-style blocking without busy-waiting. Because it's transactional, multiple permit acquisitions across different semaphores can be composed into a single atomic step that either fully succeeds or fully retries.

## Key Exports
- `make` — create with an initial permit count (dies on negative)
- `available` — current permits
- `capacity` — configured maximum
- `acquire` / `acquireN` — take one or more permits (retries if unavailable)
- `release` / `releaseN` — return permits
- `withPermit` / `withPermits` — scoped acquire/release around an effect
- `tryAcquire` / `tryAcquireN` — non-blocking variant returning `boolean`

## Source
- `raw/effect-smol/packages/effect/src/TxSemaphore.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-reentrant-lock]]
