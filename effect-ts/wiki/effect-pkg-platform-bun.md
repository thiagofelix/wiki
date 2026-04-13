---
title: @effect/platform-bun
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/platform-bun

Bun-targeted implementations of Effect's platform services. Implements `HttpServer` with `Bun.serve` (including WebSocket upgrades) and `HttpPlatform` with `Bun.file`, provides a native Redis client via `Bun.RedisClient`, an optimized `fromReadableStream`, and a full cluster layer over HTTP/sockets. Most non-Bun-specific modules (FileSystem, Path, ChildProcess, Sink, Stream, Stdio, Terminal, Socket) are re-exported from `@effect/platform-node-shared`.

## Modules
- [[effect-pkg-platform-bun-bun-child-process-spawner]]
- [[effect-pkg-platform-bun-bun-cluster-http]]
- [[effect-pkg-platform-bun-bun-cluster-socket]]
- [[effect-pkg-platform-bun-bun-file-system]]
- [[effect-pkg-platform-bun-bun-http-client]]
- [[effect-pkg-platform-bun-bun-http-platform]]
- [[effect-pkg-platform-bun-bun-http-server]]
- [[effect-pkg-platform-bun-bun-http-server-request]]
- [[effect-pkg-platform-bun-bun-multipart]]
- [[effect-pkg-platform-bun-bun-path]]
- [[effect-pkg-platform-bun-bun-redis]]
- [[effect-pkg-platform-bun-bun-runtime]]
- [[effect-pkg-platform-bun-bun-services]]
- [[effect-pkg-platform-bun-bun-sink]]
- [[effect-pkg-platform-bun-bun-socket]]
- [[effect-pkg-platform-bun-bun-socket-server]]
- [[effect-pkg-platform-bun-bun-stdio]]
- [[effect-pkg-platform-bun-bun-stream]]
- [[effect-pkg-platform-bun-bun-terminal]]
- [[effect-pkg-platform-bun-bun-worker]]
- [[effect-pkg-platform-bun-bun-worker-runner]]

## Source
- `raw/effect-smol/packages/platform-bun/src/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-shared]]
- [[effect-pkg-platform-browser]]
