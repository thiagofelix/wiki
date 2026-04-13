---
title: HttpApiEndpoint (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiEndpoint (unstable)

Describes a single route (path + method) with Schemas for path params, URL query, headers, payload, success, and error. Provides method-specific constructors (`get`, `post`, `put`, etc.) and chaining helpers to set each part. Endpoints are added to `HttpApiGroup`s.

## Key Exports
- `HttpApiEndpoint<Name, Method, Path, Params, Query, Payload, Headers, Success, Error, ...>` — full interface
- `get` / `post` / `put` / `patch` / `del` / `head` / `options` — constructors per method
- `setPath` / `setParams` / `setQuery` / `setHeaders` / `setPayload` — schema setters
- `addSuccess` / `addError` — add response schemas (with status annotations)
- `middleware` — attach a middleware reference
- `annotate` / `annotateContext` — annotations
- `PayloadMap` — internal map of content types to schemas
- `isHttpApiEndpoint` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiEndpoint.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-schema]]
- [[effect-httpapi-http-api-group]]
