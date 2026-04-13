---
title: DevToolsSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DevToolsSchema (unstable)

Schema definitions for the DevTools client/server protocol. Describes span status (Started/Ended), spans, span events, metrics snapshots, ping/pong, and the union request/response types exchanged over the transport.

## Key Exports
- `SpanStatusStarted`, `SpanStatusEnded`, `SpanStatus`
- `Span` — span message schema
- `SpanEvent` — span event payload
- `MetricsSnapshot` — snapshot of the metric registry
- `Request` — union of client-to-server messages (Span, SpanEvent, Ping, MetricsSnapshot)
- `Response` — union of server-to-client messages (MetricsRequest, Pong)
- Uses `Schema.TaggedStruct` and `Schema.toCodecJson` for on-the-wire serialization

## Source
- `raw/effect-smol/packages/effect/src/unstable/devtools/DevToolsSchema.ts`

## Related
- [[effect-devtools]]
- [[effect-devtools-dev-tools-client]]
- [[effect-devtools-dev-tools-server]]
- [[effect-schema]]
