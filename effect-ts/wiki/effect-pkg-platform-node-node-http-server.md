---
title: NodeHttpServer (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeHttpServer (@effect/platform-node)

Implements `HttpServer` on top of `node:http`. Handles request and upgrade (WebSocket via `ws`) lifecycle, client-abort interruption, graceful shutdown with optional preemptive timeout, and conversion of Effect response bodies to Node responses.

## Key Exports
- `make` — build HttpServer from a factory and listen options
- `layer` — HttpServer layer
- `layerConfig` — layer variant reading listen options from Config
- `makeHandler` — low-level request handler factory
- `makeUpgradeHandler` — WebSocket upgrade handler factory

## Source
- `raw/effect-smol/packages/platform-node/src/NodeHttpServer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-http-server]]
