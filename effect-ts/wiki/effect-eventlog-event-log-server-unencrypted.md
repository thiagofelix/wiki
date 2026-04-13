---
title: EventLogServerUnencrypted (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogServerUnencrypted (unstable)

Event log server that persists plaintext entries and runs registered event handlers on writes. Unlike the encrypted variant, it has access to typed payloads via `EventLogSchema`, so it can enforce business logic and reactively derive state on the server side.

## Key Exports
- `EventLogServerUnencrypted` — service with `makeWrite<Groups>(schema)`
- `EventLogServerStoreError` — tagged error
- `makeWrite` — factory for typed write functions
- `layerRpcHandlers` — wires server RPCs to a handler-enabled implementation
- Uses `RcMap` of store handles and `PubSub` for changes
- Integrates with handler registry for server-side event dispatch

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogServerUnencrypted.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-server]]
- [[effect-eventlog-sql-event-log-server-unencrypted]]
