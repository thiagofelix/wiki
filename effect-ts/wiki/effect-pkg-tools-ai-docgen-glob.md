---
title: Glob (@effect/ai-docgen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Glob (@effect/ai-docgen)

Context service wrapping the `glob` npm package for use within the ai-docgen CLI. Provides effectful pattern matching with tagged errors and a default Layer using `GlobLib.glob`.

## Key Exports
- `Glob` — Context service class `{ glob(pattern, options) }`
- `GlobError` — tagged error with `pattern` and `cause`
- `layer` — Layer providing the default implementation

## Source
- `raw/effect-smol/packages/tools/ai-docgen/src/Glob.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-docgen-main]]
