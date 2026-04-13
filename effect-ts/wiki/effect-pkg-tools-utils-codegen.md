---
title: Codegen (@effect/utils)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Codegen (@effect/utils)

Barrel-file generator service used across the monorepo. Scans source files for an `// @barrel(pattern)` annotation comment and regenerates the file to re-export every matching sibling module, preserving the header above the annotation and deriving module names from relative paths.

## Key Exports
- `BarrelGenerator` — service tag `{ discoverFiles, processFile }`
- `BarrelFile` — `{ path, pattern, offset }`
- `layer` — Layer depending on `FileSystem`, `Path`, `Glob`
- Annotation format: `// @barrel("*.ts")` comment above the generated section

## Source
- `raw/effect-smol/packages/tools/utils/src/Codegen.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-utils-glob]]
- [[effect-pkg-tools-utils-commands-codegen]]
