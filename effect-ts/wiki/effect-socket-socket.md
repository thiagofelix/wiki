---
title: Socket (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Socket (unstable)

Abstract bidirectional byte/string socket service used by DevTools, RPC, and other transports. Provides `run` / `runRaw` handler interfaces, a `writer` effect, `CloseEvent` class, `Channel` conversion helpers, and a built-in WebSocket-based implementation that works against any `WebSocketConstructor` (including the global one).

## Key Exports
- `Socket` — service tag with `run`, `runRaw`, `writer`
- `CloseEvent` — close message with `code`, `reason`
- `SocketError`, `SocketCloseError` — tagged errors
- `toChannel`, `toChannelString`, `toChannelWith` — `Channel` adapters
- `fromTransformStream` — build a `Socket` from a Web Streams pair
- `fromWebSocket` — wraps an existing `WebSocket`
- `makeWebSocket`, `layerWebSocket`, `layerWebSocketConstructorGlobal` — WebSocket client layers
- `WebSocketConstructor` — service tag for injecting `WebSocket` implementations

## Source
- `raw/effect-smol/packages/effect/src/unstable/socket/Socket.ts`

## Related
- [[effect-socket]]
- [[effect-socket-socket-server]]
- [[effect-channel]]
