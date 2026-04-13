---
title: HttpEffect (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HttpEffect (unstable)

Bridge between server-side `Effect`s producing `HttpServerResponse` values and the raw serve/response lifecycle. Provides `toHandled`, pre-response handlers, cause-to-response conversion, and the handled marker used by `HttpServer` and `HttpRouter` to dispatch effects to responses.

## Key Exports
- `toHandled` — run an HttpServerResponse effect with a response-writing handler and middleware
- `PreResponseHandler` — type for hooks run before the response is written
- `appendPreResponseHandler` / `preResponseHandler` — attach hooks to the current request
- `handledSymbol` — marker set when a request has been handled
- `currentServerRequest` — extract current `HttpServerRequest` from fiber context

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/HttpEffect.ts`

## Related
- [[effect-http]]
- [[effect-http-http-router]]
- [[effect-http-http-server]]
