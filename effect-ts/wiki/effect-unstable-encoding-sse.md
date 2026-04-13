---
title: Sse (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Sse (unstable)

Server-Sent Events decoder implemented as a `Channel` transform. Parses an incoming string stream into `Event` records and surfaces `retry` directives as a typed `Retry` error that downstream consumers can handle for reconnection backoff.

## Key Exports
- `Event` — `{ id?, event, data }` record type
- `Retry` — tagged error carrying a `Duration` retry hint
- `decode` — `Channel` from `NonEmptyReadonlyArray<string>` to `NonEmptyReadonlyArray<Event>`
- `decodeSchema(schema)` — typed decoder mapping `Event` to `Schema.Decoder` output
- Stateful parser buffering partial lines and dispatching on `event`/`data`/`id`/`retry`
- Used for HTTP streaming APIs (e.g. AI chat completions)

## Source
- `raw/effect-smol/packages/effect/src/unstable/encoding/Sse.ts`

## Related
- [[effect-unstable-encoding]]
- [[effect-channel]]
- [[effect-unstable-http-client]]
