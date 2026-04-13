---
title: NodeFileSystem (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeFileSystem (@effect/platform-node-shared)

Implements the core `FileSystem` service on top of Node's `fs`, `os`, and `path` modules. Every operation is wrapped with `effectify` and `handleErrnoException` so errors surface as tagged `PlatformError`s (NotFound, PermissionDenied, AlreadyExists, etc.).

## Key Exports
- `layer` — FileSystem layer
- `makeTempFile`, `makeTempDirectory`, `stat`, `readDirectory`, `watch`, ... (all via the FileSystem service shape)

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodeFileSystem.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-file-system]]
