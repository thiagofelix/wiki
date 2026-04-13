---
title: NodePath (@effect/platform-node-shared)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodePath (@effect/platform-node-shared)

Implements the core `Path` service by adapting Node's `path` module, including posix and win32 variants. Adds Effect-friendly `fromFileUrl` and `toFileUrl` helpers that wrap `node:url` conversions and return `BadArgument` on failure.

## Key Exports
- `layer` — default Path layer (os-dependent)
- `layerPosix` — posix variant
- `layerWin32` — win32 variant

## Source
- `raw/effect-smol/packages/platform-node-shared/src/NodePath.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node-shared]]
- [[effect-path]]
