---
title: NodeHttpPlatform (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeHttpPlatform (@effect/platform-node)

Implements `HttpPlatform` (file response generation) for Node using `fs.createReadStream`. Automatically picks a content-type from the filename via the `Mime` module when one is not already provided, and supports byte ranges via start/end parameters.

## Key Exports
- `make` — Platform implementation
- `layer` — HttpPlatform layer (uses NodeFileSystem + Etag)

## Source
- `raw/effect-smol/packages/platform-node/src/NodeHttpPlatform.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-http-platform]]
- [[effect-pkg-platform-node-mime]]
