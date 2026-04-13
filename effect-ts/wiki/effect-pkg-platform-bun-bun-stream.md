---
title: BunStream (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunStream (@effect/platform-bun)

Re-exports the Node shared `NodeStream` helpers and adds a Bun-optimized `fromReadableStream` that uses Bun's `readMany` API to pull multiple values per read, reducing scheduling overhead for high-throughput stream consumption.

## Key Exports
- All exports of `NodeStream` (fromReadable, toReadable, ...)
- `fromReadableStream` — optimized `ReadableStream` to Effect `Stream` adapter

## Source
- `raw/effect-smol/packages/platform-bun/src/BunStream.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-stream]]
- [[effect-stream]]
