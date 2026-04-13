---
title: @effect/platform-node-shared
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/platform-node-shared

Shared implementations used by both `@effect/platform-node` and `@effect/platform-bun` for APIs that are identical (or nearly identical) on Node and Bun. Contains the FileSystem, Path, ChildProcessSpawner, Terminal, Runtime, Stdio, Sink, and Stream adapters, plus TCP Socket/SocketServer and a cluster socket transport. Not intended to be depended on directly by applications; use the runtime-specific package instead.

## Modules
- [[effect-pkg-platform-node-shared-node-child-process-spawner]]
- [[effect-pkg-platform-node-shared-node-cluster-socket]]
- [[effect-pkg-platform-node-shared-node-file-system]]
- [[effect-pkg-platform-node-shared-node-path]]
- [[effect-pkg-platform-node-shared-node-runtime]]
- [[effect-pkg-platform-node-shared-node-sink]]
- [[effect-pkg-platform-node-shared-node-socket]]
- [[effect-pkg-platform-node-shared-node-socket-server]]
- [[effect-pkg-platform-node-shared-node-stdio]]
- [[effect-pkg-platform-node-shared-node-stream]]
- [[effect-pkg-platform-node-shared-node-terminal]]
- [[effect-pkg-platform-node-shared-internal]]

## Source
- `raw/effect-smol/packages/platform-node-shared/src/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-bun]]
