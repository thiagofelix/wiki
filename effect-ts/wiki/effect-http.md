---
title: effect/unstable/http (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/http (unstable)

Low-level HTTP building blocks for Effect v4: an `HttpClient` abstraction (with a `fetch`-based implementation), a server-side model built around `HttpServerRequest`, `HttpServerResponse`, `HttpRouter`, and `HttpServer`, plus shared primitives (headers, cookies, bodies, URL params, multipart, tracing headers, ETag). Higher-level declarative APIs live in [[effect-httpapi]] which is built on top of this module.

## Client
- [[effect-http-http-client]] — core client service
- [[effect-http-http-client-request]] — request value type
- [[effect-http-http-client-response]] — response value type
- [[effect-http-http-client-error]] — tagged error hierarchy
- [[effect-http-fetch-http-client]] — fetch-backed implementation

## Server
- [[effect-http-http-server]] — server service abstraction
- [[effect-http-http-server-request]] — incoming request
- [[effect-http-http-server-response]] — outgoing response
- [[effect-http-http-server-error]] — server-side errors
- [[effect-http-http-server-respondable]] — respondable interface
- [[effect-http-http-router]] — path router
- [[effect-http-http-middleware]] — logger, tracer, CORS, etc.
- [[effect-http-http-effect]] — effect-to-response bridge
- [[effect-http-http-platform]] — platform-backed file responses
- [[effect-http-http-static-server]] — directory-serving handler

## Primitives
- [[effect-http-http-body]] — request/response bodies
- [[effect-http-http-incoming-message]] — shared message interface
- [[effect-http-http-method]] — HTTP verb literals
- [[effect-http-headers]] — case-insensitive header store
- [[effect-http-cookies]] — cookie jar
- [[effect-http-etag]] — entity tags
- [[effect-http-url]] — safe URL parsing
- [[effect-http-url-params]] — immutable query params
- [[effect-http-multipart]] — multipart form parser
- [[effect-http-multipasta]] — multipasta re-exports
- [[effect-http-find-my-way]] — router package re-export
- [[effect-http-template]] — template-literal body helper
- [[effect-http-http-trace-context]] — tracing header codecs
- [[effect-http-internal]] — private helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/`

## Related
- [[effect-ts-v4]]
- [[effect-httpapi]]
