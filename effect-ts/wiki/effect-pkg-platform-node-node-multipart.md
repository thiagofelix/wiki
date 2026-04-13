---
title: NodeMultipart (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeMultipart (@effect/platform-node)

Node-specific multipart body parser. Reads a `Readable` stream plus `IncomingHttpHeaders`, runs it through `multipasta`'s Node transform, and yields Effect `Stream<Part>`s or persisted files on disk.

## Key Exports
- `stream` — Stream of multipart `Part`s from a Readable
- `persisted` — persisted `Multipart.Persisted` writing files via pipeline
- `fileToReadable` — accessor to recover the raw Readable from a File part

## Source
- `raw/effect-smol/packages/platform-node/src/NodeMultipart.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-multipart]]
