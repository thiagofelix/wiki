---
title: EventLogRemote (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogRemote (unstable)

Client-side service for connecting a local `EventLog` to a remote server. Handles authentication, streaming change subscriptions, and outbound writes while delegating encryption to `EventLogEncryption`. Produces a `Queue.Dequeue` of `RemoteEntry` for ingestion by the local journal.

## Key Exports
- `EventLogRemote` — service with `id`, `changes`, `write`, `whenAuthenticated`
- `EventLogRemoteError` — tagged error with `method` and cause
- `make` — builds a remote from an `RpcClient` over `EventLogRemoteRpcs`
- `layer` — provides `EventLogRemote` from an RPC client layer
- Handles chunked messages and session authentication
- Uses `Cache` for identity binding state

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogRemote.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log]]
- [[effect-eventlog-event-log-encryption]]
- [[effect-eventlog-event-log-session-auth]]
