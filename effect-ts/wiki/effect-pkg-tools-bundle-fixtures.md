---
title: Fixtures (@effect/bundle)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Fixtures (@effect/bundle)

Service that discovers the set of fixture TypeScript files shipped alongside the bundle package. Uses `glob` to enumerate `*.ts` files in a fixed `../fixtures/` directory and exposes the sorted list with the resolved directory path.

## Key Exports
- `Fixtures` — Context service `{ fixtures: string[], fixturesDir: string }`
- `Fixtures.make` — effect that globs and sorts fixture filenames
- `Fixtures.layer` — Layer built from `make`

## Source
- `raw/effect-smol/packages/tools/bundle/src/Fixtures.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-bundle-reporter]]
