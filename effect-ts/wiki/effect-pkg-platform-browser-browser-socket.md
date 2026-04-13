---
title: BrowserSocket (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserSocket (@effect/platform-browser)

Provides the core `Socket` service backed by the browser `WebSocket` global. Useful to obtain an Effect `Socket` pointing at a remote WebSocket URL without having to manually wire the constructor service.

## Key Exports
- `layerWebSocket` — Socket layer connecting to a given URL
- `layerWebSocketConstructor` — layer providing `WebSocketConstructor` using `globalThis.WebSocket`

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserSocket.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-socket-socket]]
