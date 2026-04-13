---
title: BunFileSystem (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunFileSystem (@effect/platform-bun)

Exposes a `FileSystem` layer for Bun. In practice this simply re-points to `@effect/platform-node-shared/NodeFileSystem.layer` because Bun ships Node-compatible `fs` APIs.

## Key Exports
- `layer` — FileSystem layer backed by Node's fs module

## Source
- `raw/effect-smol/packages/platform-bun/src/BunFileSystem.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-file-system]]
- [[effect-file-system]]
