---
title: BunServices (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunServices (@effect/platform-bun)

Bundles the full set of Bun platform services into one layer. Merges ChildProcessSpawner, FileSystem, Path, Stdio, and Terminal so applications can provide everything at once via a single import.

## Key Exports
- `BunServices` — union type of provided services
- `layer` — merged Layer providing all services

## Source
- `raw/effect-smol/packages/platform-bun/src/BunServices.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-pkg-platform-bun-bun-file-system]]
- [[effect-pkg-platform-bun-bun-path]]
