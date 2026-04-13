---
title: EventLogServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogServer (unstable)

Shared RPC handler scaffolding for event log servers. Provides authentication middleware and a `layerRpcHandlers` builder parameterized by storage, onWrite, and session binding callbacks. Used by both encrypted and unencrypted server implementations.

## Key Exports
- `layerAuthMiddleware` — `Layer` providing `EventLogAuthentication`
- `layerRpcHandlers(options)` — returns a `Layer` handling `EventLogRemoteRpcs`
- Options include `remoteId`, `getOrCreateSessionAuthBinding`, `onWrite`, `changes`
- Responds to `Authenticate`, `Hello`, `ChangesRpc`, and chunked write messages
- Error translation from storage failures to `EventLogProtocolError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogServer.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-server-encrypted]]
- [[effect-eventlog-event-log-server-unencrypted]]
