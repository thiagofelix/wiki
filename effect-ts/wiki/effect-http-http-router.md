---
title: HttpRouter (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpRouter (unstable)

Path-based HTTP router for Effect servers, backed by `find-my-way-ts`. Routes are added as method/path/handler triples; global and scoped middleware can be layered on top. Exposes a `serve` Layer that installs the router into an `HttpServer`, and `use` for composing layers against an existing router.

## Key Exports
- `HttpRouter` — router interface with `add`, `addAll`, `addGlobalMiddleware`, `asHttpEffect`, `prefixed`
- `Route` — path/method/handler structure
- `PathInput` — branded path string type
- `use` — helper to contribute to the current router from a Layer
- `serve` — Layer adapter turning a router into a full `HttpServer` app
- `Provided` / `GlobalProvided` — context markers for handler env
- `layer` — Layer constructor for a fresh router
- `currentRoutePath` — context key for matched path
- `params` — access route params effectfully

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpRouter.ts`

## Related
- [[effect-http]]
- [[effect-http-http-server]]
- [[effect-http-find-my-way]]
- [[effect-httpapi]]
