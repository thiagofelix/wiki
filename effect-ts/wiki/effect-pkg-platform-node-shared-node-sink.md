---
title: NodeSink (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeSink (@effect/platform-node-shared)

Adapts Node `Writable` streams into Effect `Sink`s and `Channel`s. Handles backpressure via the `drain` event, optional `end()` on completion, encoding, and error propagation through a user callback.

## Key Exports
- `fromWritable` — Sink from a Writable factory
- `fromWritableChannel` — Channel variant used by piping helpers
- `pullIntoWritable` — low-level Pull combinator used by duplex streams

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeSink.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-sink]]
