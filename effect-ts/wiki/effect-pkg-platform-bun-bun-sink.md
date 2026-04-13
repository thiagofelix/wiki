---
title: BunSink (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunSink (@effect/platform-bun)

Re-exports `@effect/platform-node-shared/NodeSink` so that Bun users get the same `Sink` combinators that adapt Node-style writable streams into Effect `Sink`s.

## Key Exports
- All exports of `NodeSink` (fromWritable, stdout, stderr, ...)

## Source
- `raw/effect-smol/packages/platform-bun/src/BunSink.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-sink]]
