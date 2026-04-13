---
title: BrowserStream (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserStream (@effect/platform-browser)

Helpers for turning DOM event targets into Effect `Stream`s. Wraps `window.addEventListener` and `document.addEventListener` so that event callbacks become pull-based, back-pressured streams.

## Key Exports
- `fromEventListenerWindow` — stream of events from `window`
- `fromEventListenerDocument` — stream of events from `document`

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserStream.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-stream]]
