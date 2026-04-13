---
title: BunMultipart (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunMultipart (@effect/platform-bun)

Bun-specific multipart body parser. Converts a Web `Request` into an Effect `Stream<Multipart.Part>` (using BunStream's optimized readable-stream adapter) or a persisted representation with files written to the file system.

## Key Exports
- `stream` — Stream of multipart `Part`s from a Request
- `persisted` — Effect producing a Multipart.Persisted value with files on disk

## Source
- `raw/effect-smol/packages/platform-bun/src/BunMultipart.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-http-multipart]]
