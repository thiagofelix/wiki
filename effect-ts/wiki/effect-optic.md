---
title: Optic
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Optic

Composable, immutable accessors — lenses, prisms, isos, optionals, and traversals — for reading and updating deeply nested data structures without mutation. Updates are structurally persistent, cloning only nodes on the path. Use for ergonomic immutable state updates and narrowed access into unions.

## Key Exports
- `Iso` / `Lens` / `Prism` / `Optional` — optic kinds (strongest → weakest)
- `id` — identity iso, entry point for optic chains
- `makeIso` / `makeLens` / `makePrism` / `makeOptional` — builders
- `fromChecks` — build a prism with runtime validation
- `some` / `success` / `failure` — prisms for `Option` and `Result` variants
- `entries` — iso between a record and its entries
- `getAll` — extract all foci from a traversal
- Optic chain methods: `.key`, `.optionalKey`, `.at`, `.tag`, `.refine`, `.check`, `.notUndefined`, `.pick`, `.omit`, `.forEach`, `.compose`
- `replace` / `replaceResult` / `modify` — write operations

## Source
- `raw/effect-smol/packages/effect/src/Optic.ts`

## Related
- [[effect-ts-v4]]
- [[effect-struct]]
- [[effect-newtype]]
