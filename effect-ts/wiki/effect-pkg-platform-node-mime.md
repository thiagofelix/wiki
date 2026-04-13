---
title: Mime (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Mime (@effect/platform-node)

Thin re-export of the `mime` package (content-type detection by filename). Used internally by NodeHttpPlatform to pick a `content-type` for file responses when none is set.

## Key Exports
- default `Mime` — the `mime` singleton
- Re-exports all named exports of `mime`

## Source
- `raw/effect-smol/packages/platform-node/src/Mime.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-pkg-platform-node-node-http-platform]]
