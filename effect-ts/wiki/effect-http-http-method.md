---
title: HttpMethod (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpMethod (unstable)

String-literal HTTP verb type and a handful of helpers. Distinguishes methods that can carry a body from those that cannot (GET, HEAD, OPTIONS, TRACE), and exposes sets/lists for iteration.

## Key Exports
- `HttpMethod` — union type of verbs (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`, `TRACE`)
- `HttpMethod.NoBody` / `HttpMethod.WithBody` — subdivisions
- `hasBody` — refinement for methods that carry a payload
- `all` — ReadonlySet of every method
- `allShort` — aliasing tuples like `["DELETE", "del"]`
- `isHttpMethod` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpMethod.ts`

## Related
- [[effect-http]]
- [[effect-http-http-client-request]]
- [[effect-httpapi-http-api-endpoint]]
