---
title: HttpClientError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpClientError (unstable)

Tagged error hierarchy for the HttpClient module. Wraps a `reason` that can be a transport failure, a response error, or a schema/parse error, and exposes the offending request and (optionally) response through getters.

## Key Exports
- `HttpClientError` — top-level tagged error with a `reason` discriminator
- `TransportError` — network/fetch-level failure
- `ResponseError` — non-2xx response or decode failure
- `RequestError` — request construction failure
- `isHttpClientError` — type guard
- `HttpClientErrorReason` — union of reason variants

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpClientError.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client]]
- [[effect-ts-v4]]
