---
title: HttpApiBuilder (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiBuilder (unstable)

Server-side runtime for `HttpApi` definitions. `HttpApiBuilder.layer` turns an API definition into a `Layer` that registers routes on the current `HttpRouter`; `group` binds implementations to each endpoint of a group, handling schema decoding/encoding, multipart, URL params, response encoding, and OpenAPI path exposure.

## Key Exports
- `layer` — turn an `HttpApi` + group implementations into a Layer
- `group` — implement all endpoints of a named `HttpApiGroup`
- `Handlers` — builder for endpoint handlers with `handle` / `handleRaw`
- `middleware` — provide a middleware implementation via Layer
- `middlewareSecurity` — security middleware for `HttpApiSecurity` schemes
- `middlewareSecurityVoid` — void variant
- `middlewareOpenApi` — expose OpenAPI spec as a JSON endpoint

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiBuilder.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api]]
- [[effect-http-http-router]]
