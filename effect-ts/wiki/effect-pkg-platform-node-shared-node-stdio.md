---
title: NodeStdio (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeStdio (@effect/platform-node-shared)

Builds the core `Stdio` service from `process.stdout`, `process.stderr`, `process.stdin`, and `process.argv.slice(2)`. Uses `NodeSink.fromWritable` / `NodeStream.fromReadable` so user code interacts with stdio as Effect Streams and Sinks.

## Key Exports
- `layer` — Stdio layer

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeStdio.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-stdio]]
