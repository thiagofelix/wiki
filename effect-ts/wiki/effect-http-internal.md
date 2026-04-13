---
title: http/internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# http/internal (unstable)

Private helpers shared between modules under `unstable/http`. Not part of the public API.

## Files
- `preResponseHandler.ts` — a WeakMap of `HttpServerRequest.source` to chained `PreResponseHandler`s, with `appendPreResponseHandlerUnsafe` for registering a handler and `requestPreResponseHandlers` for lookups from `HttpEffect.toHandled`.

## Key Exports
- `requestPreResponseHandlers` — WeakMap of request source to handler
- `appendPreResponseHandlerUnsafe` — chain a new handler onto a request

## Source
- `raw/effect-smol/packages/effect/src/unstable/http/internal/preResponseHandler.ts`

## Related
- [[effect-http]]
- [[effect-http-http-effect]]
- [[effect-http-http-middleware]]
