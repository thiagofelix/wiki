---
title: HttpApiClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiClient (unstable)

Derives a type-safe HTTP client from an `HttpApi` definition. Each non-top-level group becomes a property and each endpoint becomes a method with typed params, query, payload, headers, success, and error. Supports configurable `baseUrl`, transformClient hooks, and response modes (decoded, decoded-and-response, response-only).

## Key Exports
- `Client<Groups>` — derived client type
- `ForApi<Api>` — client type derived from an `HttpApi`
- `make` — construct an Effect yielding a client from an API definition
- `makeWith` — variant taking a customized `HttpClient`
- `endpoint` — build an Effect for a single endpoint (lower-level)
- `group` — build a single group's client

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiClient.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api]]
- [[effect-http-http-client]]
