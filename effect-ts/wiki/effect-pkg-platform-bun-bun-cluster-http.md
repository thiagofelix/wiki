---
title: BunClusterHttp (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunClusterHttp (@effect/platform-bun)

Wires up an Effect cluster runner over HTTP/WebSocket using Bun's native HTTP server. Combines sharding, runner health (ping or k8s), and storage (local, sql, or byo) into a single configurable layer, and exposes a bound HTTP server layer that reads its listen address from ShardingConfig.

## Key Exports
- `layerK8sHttpClient` — re-exported from BunClusterSocket
- `layerHttpServer` — HttpServer layer bound to ShardingConfig.runnerAddress
- `layer` — full cluster layer with transport, serialization, storage, health options

## Source
- `raw/effect-smol/packages/platform-bun/src/BunClusterHttp.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-cluster-http-runner]]
- [[effect-cluster-sharding]]
