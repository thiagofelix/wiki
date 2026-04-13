---
title: BunHttpPlatform (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunHttpPlatform (@effect/platform-bun)

Implements the `HttpPlatform` service (file response generation) for Bun. Uses `Bun.file` for efficient file responses, supporting byte-range slicing, and accepts raw Web `File` objects directly.

## Key Exports
- `layer` — HttpPlatform layer wired to BunFileSystem and Etag

## Source
- `raw/effect-smol/packages/platform-bun/src/BunHttpPlatform.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-unstable-http-http-platform]]
