---
title: NodeHttpServerRequest (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeHttpServerRequest (@effect/platform-node)

Escape-hatch helpers to recover the underlying Node `IncomingMessage` or `ServerResponse` from an Effect `HttpServerRequest`. Useful when integrating with Node-native middleware or framework code.

## Key Exports
- `toIncomingMessage` — accessor for the raw `http.IncomingMessage`
- `toServerResponse` — accessor for the raw `http.ServerResponse`

## Source
- `raw/effect-smol/packages/platform-node/src/NodeHttpServerRequest.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-http-server-request]]
