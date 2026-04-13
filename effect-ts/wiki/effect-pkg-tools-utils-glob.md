---
title: Glob (@effect/utils)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Glob (@effect/utils)

Context service wrapping the `glob` npm package for use within `@effect/utils` commands. Provides effectful pattern matching with a tagged error channel.

## Key Exports
- `Glob` — service tag `{ glob(pattern, options) }`
- `GlobError` — tagged error with `pattern` and `cause`
- `layer` — Layer wrapping `GlobLib.glob` via `Effect.tryPromise`

## Source
- `raw/effect-smol/packages/tools/utils/src/Glob.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-utils-codegen]]
