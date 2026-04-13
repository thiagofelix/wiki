---
title: Latch
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Latch

A one-shot or reusable synchronization primitive for coordinating fibers. A `Latch` starts open or closed; `await` suspends until the latch is open, while `open`/`close` toggle state. Use it to gate execution on a condition that another fiber will eventually signal.

## Key Exports
- `Latch` — interface with `open`, `close`, `release`, `await`, `whenOpen`
- `make` — effectful constructor returning `Effect<Latch>`
- `makeUnsafe` — synchronous constructor
- `open` / `openUnsafe` — open the latch, releasing waiters
- `close` / `closeUnsafe` — close the latch
- `release` — release all waiters without opening
- `await` — suspend until the latch is open
- `whenOpen` — run an effect only while the latch is open

## Source
- `raw/effect-smol/packages/effect/src/Latch.ts`

## Related
- [[effect-ts-v4]]
