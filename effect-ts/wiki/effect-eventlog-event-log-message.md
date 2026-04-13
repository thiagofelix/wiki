---
title: EventLogMessage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogMessage (unstable)

RPC protocol definitions for remote event log communication. Declares the `EventLogRemoteRpcs` RPC group covering authentication, hello, change subscription, and write requests, plus middleware for authentication and the shared error type used across client and server.

## Key Exports
- `StoreId` — branded string type + schema
- `EventLogProtocolError` — tagged error with `code` enum (Unauthorized, Forbidden, NotFound, InvalidRequest, InternalServerError)
- `EventLogAuthentication` — `RpcMiddleware` providing `Identity`
- `EventLogRemoteRpcs` — `RpcGroup` with `Authenticate`, `Hello`, `ChangesRpc`, `WriteEntries`, `WriteEntriesUnencrypted`
- `ChunkedMessage`, `SingleMessage` — message framing helpers
- `HelloResponse`, `Authenticate` — specific Rpc definitions

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogMessage.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-remote]]
- [[effect-rpc]]
