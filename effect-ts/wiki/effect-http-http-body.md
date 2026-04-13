---
title: HttpBody (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpBody (unstable)

Tagged union representing the body of an HTTP request or response: `Empty`, `Raw`, `Uint8Array`, `FormData`, or `Stream`. Provides constructors that encode JSON, text, URL params, files, and Schema-derived values, plus the `HttpBodyError` raised when encoding fails.

## Key Exports
- `HttpBody` — tagged union of body variants
- `Empty` / `Raw` / `Uint8Array` / `FormData` / `Stream` — variants
- `HttpBodyError` — tagged error with ErrorReason
- `empty` / `text` / `json` / `unsafeJson` — constructors
- `uint8Array` / `formData` / `urlParams` / `stream` — constructors
- `file` / `fileWeb` / `fileInfo` — file-backed bodies (platform)
- `jsonSchema` — Schema-based encoder
- `isHttpBody` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpBody.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client-request]]
- [[effect-http-http-server-response]]
