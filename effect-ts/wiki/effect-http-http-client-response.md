---
title: HttpClientResponse (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpClientResponse (unstable)

Represents an HTTP response received by a client. Extends `HttpIncomingMessage` with the originating `request`, `status`, `cookies`, and lazily-decoded `formData`, and re-exports schema decoders from HttpIncomingMessage. Built via `fromWeb` to adapt a standard `Response`.

## Key Exports
- `HttpClientResponse` — response interface with request/status/cookies
- `fromWeb` — construct from a standard `Response` object
- `schemaJson` — decode JSON body via a Schema codec
- `schemaBodyJson` / `schemaBodyUrlParams` / `schemaHeaders` — re-exported decoders
- `schemaNoBody` — decode 204 responses
- `matchStatus` — branch on status code
- `filterStatus` / `filterStatusOk` — error on non-matching status

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpClientResponse.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client]]
- [[effect-http-http-incoming-message]]
