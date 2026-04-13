---
title: BrowserKeyValueStore (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserKeyValueStore (@effect/platform-browser)

Implements the core `KeyValueStore` interface on top of the browser Web Storage APIs. Offers two layers: one backed by `localStorage` for persistent data and one backed by `sessionStorage` for session-scoped data.

## Key Exports
- `layerLocalStorage` — KeyValueStore layer using `globalThis.localStorage`
- `layerSessionStorage` — KeyValueStore layer using `globalThis.sessionStorage`

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserKeyValueStore.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-unstable-persistence-key-value-store]]
