---
title: HttpStaticServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpStaticServer (unstable)

Builds an Effect handler that serves files from a directory, with optional index, SPA fallback, cache-control headers, and custom MIME types. Depends on `FileSystem`, `Path`, and `HttpPlatform` to stream file content efficiently.

## Key Exports
- `make` — create a handler Effect that serves files rooted at a directory
- `defaultMimeTypes` — built-in extension-to-mime-type map

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpStaticServer.ts`

## Related
- [[effect-http]]
- [[effect-http-http-platform]]
- [[effect-http-http-router]]
