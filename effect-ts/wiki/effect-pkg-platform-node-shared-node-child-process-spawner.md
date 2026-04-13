---
title: NodeChildProcessSpawner (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeChildProcessSpawner (@effect/platform-node-shared)

Node implementation of the core `ChildProcessSpawner` service. Handles environment resolution, working-directory validation, stdin/stdout/stderr + additional FD configuration, Stream/Sink piping, signal handling, and converts `ErrnoException` failures into tagged `PlatformError`s.

## Key Exports
- `layer` — ChildProcessSpawner layer backed by `node:child_process`
- `make` — Effect constructing the spawner (depends on FileSystem, Path)

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeChildProcessSpawner.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-process-child-process-spawner]]
