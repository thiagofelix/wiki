---
title: RcRef
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RcRef

A single reference-counted handle to a scoped resource. The resource is lazily acquired on the first `get` and released when the last scoped consumer closes, optionally after an idle TTL. Simpler than `RcMap` when only one shared resource is needed (e.g. a singleton DB client that should exist only while in use).

## Key Exports
- `RcRef<A, E>` — pipeable ref-counted reference
- `make({ acquire, idleTimeToLive? })` — scoped constructor
- `get(self)` — returns scoped Effect that shares the acquired value
- `invalidate(self)` — force release

## Source
- `raw/effect-smol/packages/effect/src/RcRef.ts`

## Related
- [[effect-ts-v4]]
- [[effect-rc-map]]
- [[effect-resource]]
