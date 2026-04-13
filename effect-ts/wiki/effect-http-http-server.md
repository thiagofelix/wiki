---
title: HttpServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpServer (unstable)

Abstract HTTP server service. An `HttpServer` exposes a `serve` method that accepts an `HttpServerResponse` effect (optionally with middleware) and a concrete bound `Address` (TCP or Unix). Platform packages (Node, Bun, Deno, Web/workerd) provide implementations; this module only defines the common interface.

## Key Exports
- `HttpServer` — Context Service with `serve` and `address`
- `Address` / `TcpAddress` / `UnixAddress` — address variants
- `make` — adapt a raw serve function into an `HttpServer` service
- `serve` — Layer helper that runs a handler effect via the current server
- `serveEffect` — Effect variant

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpServer.ts`

## Related
- [[effect-http]]
- [[effect-http-http-router]]
- [[effect-http-http-middleware]]
