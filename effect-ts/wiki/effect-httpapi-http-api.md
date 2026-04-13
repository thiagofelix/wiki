---
title: HttpApi (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApi (unstable)

Top-level declarative API description: an `HttpApi` is an identifier plus a record of `HttpApiGroup`s. From one definition you can derive a server, a type-safe client, and OpenAPI/Scalar/Swagger docs. The module provides constructors, middleware/prefix combinators, and annotation helpers.

## Key Exports
- `HttpApi<Id, Groups>` — interface describing a named API
- `Any` / `AnyWithProps` — unconstrained variants for internal use
- `make` — construct an empty `HttpApi` with an identifier
- `add` — add one or more `HttpApiGroup`s
- `addHttpApi` — merge groups from another API
- `prefix` — add a path prefix to every group
- `middleware` — attach a middleware to all contained endpoints
- `annotate` / `annotateContext` — annotation helpers
- `isHttpApi` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApi.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-group]]
- [[effect-httpapi-http-api-builder]]
