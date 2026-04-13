---
title: TxReentrantLock
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TxReentrantLock

Transactional read/write lock with reentrant semantics. Multiple readers may hold the lock concurrently OR a single writer holds exclusive access. A fiber already holding the write lock can acquire additional read or write locks (reentrancy), and a fiber holding a read lock can upgrade to a write lock. State is a `TxRef<LockState>` keyed by fiber id so acquire/release operations retry cleanly on contention.

## Key Exports
- `make` — create a new unlocked lock
- `acquireRead` / `releaseRead` — shared reader acquisition
- `acquireWrite` / `releaseWrite` — exclusive writer acquisition
- `withReadLock` — scoped read-lock wrapper around an effect
- `withWriteLock` — scoped write-lock wrapper around an effect
- `locked` — check if any lock is held
- `readLocks` / `writeLocks` — inspect current counts

## Source
- `raw/effect-smol/packages/effect/src/TxReentrantLock.ts`

## Related
- [[effect-ts-v4]]
- [[effect-tx-ref]]
- [[effect-tx-semaphore]]
