---
title: NodeHttpClient (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeHttpClient (@effect/platform-node)

HTTP client implementations for Node. Re-exports the Fetch client and adds an `Undici`-backed client service with a tunable `Dispatcher`, plus a legacy `node:http`/`node:https` implementation. The Undici client supports streaming bodies, custom `UndiciOptions`, and maps all failures to tagged `HttpClientError`s.

## Key Exports
- `Fetch`, `layerFetch`, `RequestInit` — re-exports from FetchHttpClient
- `Dispatcher` — Context.Service tag for an Undici Dispatcher
- `layerDispatcher`, `dispatcherLayerGlobal` — Dispatcher layer variants
- `UndiciOptions` — context reference for per-request dispatcher options
- `makeUndici`, `layerUndici` — Undici HttpClient constructor and layer
- `layerHttp` — legacy node:http/https HttpClient layer

## Source
- `raw/effect-smol/packages/platform-node/src/NodeHttpClient.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-http-client]]
- [[effect-pkg-platform-node-undici]]
