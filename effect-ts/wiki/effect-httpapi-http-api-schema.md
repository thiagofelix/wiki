---
title: HttpApiSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiSchema (unstable)

Schema annotations and helpers for describing HTTP-specific metadata: response status codes, payload/response encodings, empty bodies, and multipart forms. `HttpApiBuilder`, `HttpApiClient`, and `OpenApi` read these annotations when building runtime and documentation.

## Key Exports
- `status` — set the HTTP status on a schema
- `Empty` / `NoContent` / `Created` / `Accepted` — empty-body schemas for common statuses
- `asNoContent` — decode a 204 into a custom value
- `asJson` / `asFormUrlEncoded` / `asText` / `asUint8Array` — force response/payload encoding
- `asMultipart` / `asMultipartStream` — mark payload as multipart form
- `PayloadEncoding` / `ResponseEncoding` — internal encoding tags
- `httpApiStatus` / `~httpApiEncoding` — annotation keys (augments `Schema.Annotations`)

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiSchema.ts`

## Related
- [[effect-httpapi]]
- [[effect-schema]]
- [[effect-httpapi-http-api-endpoint]]
