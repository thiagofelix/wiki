---
title: Glob (@effect/ai-codegen)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Glob (@effect/ai-codegen)

Thin Effect wrapper around the `glob` npm package, exposed as a Context service so codegen components can match file patterns without directly importing Node APIs.

## Key Exports
- `Glob` — service tag `{ glob(pattern, options) }`
- `GlobError` — tagged error wrapping underlying glob failures
- `layer` — in-memory Layer that calls `GlobLib.glob` via `Effect.tryPromise`

## Source
- `raw/effect-smol/packages/tools/ai-codegen/src/Glob.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-ai-codegen-discovery]]
