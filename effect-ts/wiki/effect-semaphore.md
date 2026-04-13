---
title: Semaphore
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Semaphore

Counting semaphore for limiting concurrency. Permits are acquired before running an effect and released after, with FIFO queuing of waiters. Supports resizing, try-acquire, and all-release semantics.

## Key Exports
- `Semaphore` — interface with `resize`, `take`, `release`, `releaseAll`
- `withPermits(n)` — run effect holding `n` permits
- `withPermit` — shortcut for a single permit
- `withPermitsIfAvailable` — non-blocking, returns `Option`
- `make` / `makeUnsafe` — construct with initial permit count

## Source
- `raw/effect-smol/packages/effect/src/Semaphore.ts`

## Related
- [[effect-ts-v4]]
- Used internally by [[effect-synchronized-ref]], [[effect-scoped-ref]]; related to Latch
