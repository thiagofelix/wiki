---
title: HttpApiMiddleware (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpApiMiddleware (unstable)

Declarative middleware for `HttpApi`. A middleware is a Context Tag whose service describes either a plain handler wrap (`HttpApiMiddleware`) or a security-aware wrap (`HttpApiMiddlewareSecurity`) keyed by one or more `HttpApiSecurity` schemes. Client-side middleware variants are also provided so derived `HttpApiClient`s can react to requests.

## Key Exports
- `HttpApiMiddleware<Provides, E, Requires>` — server middleware function type
- `HttpApiMiddlewareSecurity` — security-keyed variant
- `HttpApiMiddlewareClient` — client-side variant
- `Tag` — base class for declaring middleware as a Context service
- `TagSecurity` — security-aware Tag
- `isSecurity` — guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/httpapi/HttpApiMiddleware.ts`

## Related
- [[effect-httpapi]]
- [[effect-httpapi-http-api-security]]
- [[effect-httpapi-http-api-builder]]
