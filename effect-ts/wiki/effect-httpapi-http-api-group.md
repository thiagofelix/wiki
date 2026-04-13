---
title: HttpApiGroup (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiGroup (unstable)

Named collection of `HttpApiEndpoint`s representing a subdomain of an API. Groups can be top-level (routes mounted directly on the API root) or namespaced, have their own middleware, and can be prefixed. A group's identifier becomes the name accessed on the derived client.

## Key Exports
- `HttpApiGroup<Id, Endpoints, TopLevel>` — interface
- `Any` / `AnyWithProps` — unconstrained variants
- `make` — construct an empty group
- `add` — add one or more endpoints
- `prefix` — path prefix all endpoints
- `middleware` — attach middleware reference
- `annotate` / `annotateMerge` — annotation helpers
- `topLevel` — mark group as top-level (endpoints hoisted to API)
- `isHttpApiGroup` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiGroup.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api]]
- [[effect-httpapi-http-api-endpoint]]
