---
title: DevTools (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DevTools (unstable)

Entry-point layers that wire `DevToolsClient` to a transport. Exposes a ready-to-use WebSocket-based layer for connecting an Effect application to a DevTools server (e.g. the Effect DevTools desktop app), plus a raw `Socket` variant.

## Key Exports
- `layerSocket` — re-export of `DevToolsClient.layerTracer`; requires `Socket`
- `layerWebSocket(url?)` — layers the tracer over a WebSocket client
- `layer(url?)` — fully self-contained layer using the global `WebSocket` constructor
- Default URL `ws://localhost:34437`

## Source
- `raw/effect-smol/packages/effect/src/unstable/devtools/DevTools.ts`

## Related
- [[effect-devtools]]
- [[effect-devtools-client]]
- [[effect-socket]]
