---
title: BunPath (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunPath (@effect/platform-bun)

Provides the core `Path` service for Bun. Delegates to `@effect/platform-node-shared/NodePath`, which wraps Node's `path` module; Bun re-exposes the same posix and win32 variants.

## Key Exports
- `layer` — default Path layer (os-detected)
- `layerPosix` — posix-only Path layer
- `layerWin32` — win32-only Path layer

## Source
- `raw/effect-smol/packages/platform-bun/src/BunPath.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-path]]
- [[effect-pkg-platform-node-shared-node-path]]
