---
title: effect/unstable/httpapi (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/httpapi (unstable)

Declarative HTTP API framework built on top of [[effect-http]]. You describe your API once as a tree of `HttpApi -> HttpApiGroup -> HttpApiEndpoint`, each endpoint carrying Schemas for params, query, payload, headers, success, and errors. From that one definition you get a server implementation, a type-safe client, and auto-generated OpenAPI documentation (Scalar or Swagger). Change the definition once and everything stays in sync.

## Definition
- [[effect-httpapi-http-api]] — top-level API container
- [[effect-httpapi-http-api-group]] — collection of related endpoints
- [[effect-httpapi-http-api-endpoint]] — single route with schemas
- [[effect-httpapi-http-api-schema]] — status/encoding annotations
- [[effect-httpapi-http-api-error]] — canonical error schemas
- [[effect-httpapi-http-api-security]] — auth scheme descriptions
- [[effect-httpapi-http-api-middleware]] — declarative middleware tags

## Runtime
- [[effect-httpapi-http-api-builder]] — server implementation from definition
- [[effect-httpapi-http-api-client]] — typed client derived from definition

## Documentation
- [[effect-httpapi-open-api]] — OpenAPI 3.1 spec generation
- [[effect-httpapi-http-api-scalar]] — Scalar docs UI layer
- [[effect-httpapi-http-api-swagger]] — Swagger UI layer
- [[effect-httpapi-internal]] — private helpers (HTML escaping, inlined UIs)

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/`
- `raw/effect-smol/packages/effect/HTTPAPI.md` — introductory guide

## Related
- [[effect-ts-v4]]
- [[effect-http]]
- [[effect-schema]]
