---
title: Rollup (@effect/bundle)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Rollup (@effect/bundle)

Service wrapping the Rollup Node API to bundle single files or lists of files, gzip-measure the resulting ESM chunks, and optionally write minified outputs to disk. Uses a scoped `acquireRelease` on the bundle handle and streams chunks through a `FiberSet` for concurrent writes.

## Key Exports
- `Rollup` — Context service `{ bundle, bundleAll }`
- `BundleStats` — tagged class `{ path, sizeInBytes }` (gzipped)
- `BundleOptions` / `BundleAllOptions`
- `RollupError` — tagged error wrapping Rollup failures
- `Rollup.layer` — default Layer

## Source
- `raw/effect-smol/packages/tools/bundle/src/Rollup.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-bundle-plugins]]
- [[effect-pkg-tools-bundle-reporter]]
