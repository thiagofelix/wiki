---
title: NodeServices (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeServices (@effect/platform-node)

Bundles the full set of Node platform services into one layer. Merges ChildProcessSpawner, FileSystem, Path, Stdio, and Terminal so applications can provide them with a single import.

## Key Exports
- `NodeServices` — union type of provided services
- `layer` — merged Layer providing all services

## Source
- `raw/effect-smol/packages/platform-node/src/NodeServices.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-node-file-system]]
- [[effect-pkg-platform-node-node-path]]
