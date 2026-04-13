---
title: DevToolsClient (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# DevToolsClient (unstable)

Client that streams span and metric data to a DevTools server over an NDJSON duplex `Socket` channel. Also installs a `Tracer` that intercepts span creation, events, and endings to push them to the DevTools UI in real time.

## Key Exports
- `DevToolsClient` — service with `sendUnsafe(Span | SpanEvent)`
- `make` — `Effect` producing the client; requires `Scope` and `Socket`
- `layer` — `Layer<DevToolsClient, never, Socket>`
- `makeTracer` — builds a wrapping `Tracer` that emits spans to the client
- `layerTracer` — `Layer<never, never, Socket>` providing `Tracer.Tracer`
- Sends periodic `Ping` and handles `MetricsRequest` by snapshotting `Metric`
- Uses `Ndjson.duplexSchemaString` with `DevToolsSchema` request/response codecs

## Source
- `raw/effect-smol/packages/effect/src/unstable/devtools/DevToolsClient.ts`

## Related
- [[effect-devtools]]
- [[effect-devtools-dev-tools-schema]]
- [[effect-unstable-encoding-ndjson]]
- [[effect-socket]]
