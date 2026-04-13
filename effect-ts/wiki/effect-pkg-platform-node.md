---
title: @effect/platform-node
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/platform-node

Node.js-targeted implementations of Effect's platform services. Provides HTTP client (Fetch/Undici/legacy node:http), HTTP server with WebSocket upgrades via `ws`, multipart parsing, Redis (ioredis), child-process and worker-threads workers, mime detection, cluster layers (HTTP, socket, k8s), plus the usual FileSystem/Path/Sink/Stream/Stdio/Socket/Terminal services (most delegated to `@effect/platform-node-shared`).

## Modules
- [[effect-pkg-platform-node-mime]]
- [[effect-pkg-platform-node-node-child-process-spawner]]
- [[effect-pkg-platform-node-node-cluster-http]]
- [[effect-pkg-platform-node-node-cluster-socket]]
- [[effect-pkg-platform-node-node-file-system]]
- [[effect-pkg-platform-node-node-http-client]]
- [[effect-pkg-platform-node-node-http-incoming-message]]
- [[effect-pkg-platform-node-node-http-platform]]
- [[effect-pkg-platform-node-node-http-server]]
- [[effect-pkg-platform-node-node-http-server-request]]
- [[effect-pkg-platform-node-node-multipart]]
- [[effect-pkg-platform-node-node-path]]
- [[effect-pkg-platform-node-node-redis]]
- [[effect-pkg-platform-node-node-runtime]]
- [[effect-pkg-platform-node-node-services]]
- [[effect-pkg-platform-node-node-sink]]
- [[effect-pkg-platform-node-node-socket]]
- [[effect-pkg-platform-node-node-socket-server]]
- [[effect-pkg-platform-node-node-stdio]]
- [[effect-pkg-platform-node-node-stream]]
- [[effect-pkg-platform-node-node-terminal]]
- [[effect-pkg-platform-node-node-worker]]
- [[effect-pkg-platform-node-node-worker-runner]]
- [[effect-pkg-platform-node-undici]]

## Source
- `raw/effect-smol/packages/platform-node/src/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-browser]]
