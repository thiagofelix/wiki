---
title: Multipart (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Multipart (unstable)

Effect-first wrapper around the `multipasta` streaming multipart parser. Parses `multipart/form-data` request bodies into a stream of `Field` and `File` parts, with optional persistence to temp files, size/count limits, and Schema decoders for typed fields.

## Key Exports
- `Part` — tagged union `Field | File`
- `Field` / `File` — part variants with key, contentType, value/stream
- `Persisted` — stored form data with fields and files on disk
- `MultipartError` — tagged error (ParseError, TooLarge, etc.)
- `stream` — parse an incoming message into a Stream of parts
- `persisted` — parse and persist files via `FileSystem`
- `withLimits` — apply count/size limits
- `schemaJson` / `schemaFields` — decode parsed fields into Schemas
- `isPart` / `isField` / `isFile` — guards

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/Multipart.ts`

## Related
- [[effect-http]]
- [[effect-http-multipasta]]
- [[effect-http-http-server-request]]
