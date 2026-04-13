---
title: SqlStream (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlStream (unstable)

Utilities for building backpressured `Stream`s from SQL driver callbacks. `asyncPauseResume` wraps a callback-based cursor into a `Stream`, invoking `onPause`/`onResume` hooks when the internal queue fills or drains.

## Key Exports
- `asyncPauseResume` — build a `Stream` from a register callback that emits single items or chunks, with pause/resume flow control and configurable buffer size

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlStream.ts`

## Related
- [[effect-stream]]
- [[effect-sql-sql-connection]]
