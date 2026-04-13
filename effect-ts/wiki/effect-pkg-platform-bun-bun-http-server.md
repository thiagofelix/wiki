---
title: BunHttpServer (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunHttpServer (@effect/platform-bun)

Implements `HttpServer` on top of `Bun.serve`, including native WebSocket upgrade support. Handles request lifecycle, abort propagation via `AbortSignal`, graceful shutdown with optional preemptive timeout, cookie/Set-Cookie bridging, and conversion of Effect response bodies (Empty/Raw/FormData/Stream) to Bun `Response`.

## Key Exports
- `ServeOptions` — Bun serve options union with routes
- `make` — constructs a live HttpServer from serve options
- `layer` — layer form using a given listen address
- `layerConfig` — layer form pulling address from Config
- `layerWebSocketUpgrade` — helper to route WebSocket upgrades

## Source
- `raw/effect-smol/packages/platform-bun/src/BunHttpServer.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-http-http-server]]
