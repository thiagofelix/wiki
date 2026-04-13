---
title: NodeStream (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeStream (@effect/platform-node-shared)

Adapts Node `Readable` and `Duplex` streams into Effect `Stream`s and `Channel`s. Supports chunk size tuning, optional closeOnDone, backpressure via pull-based readable reading, and pairs nicely with `NodeSink.pullIntoWritable` for duplex pipelines.

## Key Exports
- `fromReadable` — Stream from a Readable factory
- `fromReadableChannel` — Channel form of the above
- `fromDuplex` — full Duplex Channel pipeline (read + write)
- `readableToPullUnsafe` — low-level helper used internally

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeStream.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-stream]]
