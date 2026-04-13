---
title: EventLogSessionAuth (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# EventLogSessionAuth (unstable)

Challenge/response session authentication scheme using Ed25519 signatures. Defines the session-auth payload layout, signing/verification helpers, and challenge lifetime constants. Clients sign a server-issued challenge with their ed25519 key to establish an authenticated session.

## Key Exports
- `SessionAuthPayload` — `{ remoteId, challenge, publicKey, signingPublicKey }`
- `encodeSessionAuthPayload` — length-prefixed encoding
- `signSessionAuthPayloadBytes` — signs a payload with a private key
- `verifySessionAuthPayloadBytes` — server-side verification
- `AuthPayloadContext` — `"eventlog-auth-v1"` domain separator
- `Ed25519PublicKeyLength = 32`, `Ed25519SignatureLength = 64`
- `SessionAuthChallengeLength = 32`
- `SessionAuthChallengeTimeToLiveMillis = 30_000`
- `EventLogSessionAuthError` — tagged error for invalid payload/context

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/EventLogSessionAuth.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-log-remote]]
- [[effect-eventlog-event-log-server]]
