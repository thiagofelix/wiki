---
title: oxlint (@effect/oxc)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# oxlint (@effect/oxc)

Default export bundling custom Oxlint rules enforced across the Effect monorepo. The `effect` plugin provides three rules targeting barrel package imports, `.js` extension imports, and opaque instance field patterns incompatible with Effect's class semantics.

## Key Exports
- default plugin object `{ meta: { name: "effect" }, rules }`
- `no-import-from-barrel-package` rule
- `no-js-extension-imports` rule
- `no-opaque-instance-fields` rule

## Source
- `raw/effect-smol/packages/tools/oxc/src/oxlint/index.ts`
- `raw/effect-smol/packages/tools/oxc/src/oxlint/rules/*.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
