---
title: BunChildProcessSpawner (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunChildProcessSpawner (@effect/platform-bun)

Re-exports `@effect/platform-node-shared/NodeChildProcessSpawner`. On Bun, the Node shared implementation is used directly because Bun is API-compatible with Node's `child_process` module.

## Key Exports
- All exports of `NodeChildProcessSpawner` (layer, make)

## Source
- `raw/effect-smol/packages/platform-bun/src/BunChildProcessSpawner.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-node-shared-node-child-process-spawner]]
