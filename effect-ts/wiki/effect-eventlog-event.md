---
title: Event (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Event (unstable)

Schema definition for a single event in an `EventLog`. Each event carries a tag, a primary-key derivation function, payload schema, success schema, and error schema. Payloads are additionally wrapped in a msgpack-encoded form for persistence.

## Key Exports
- `Event<Tag, Payload, Success, Error>` — interface
- `TypeId`, `isEvent` — branding and guard
- `make` — constructor taking `{ tag, primaryKey, payload?, success?, error? }`
- `Any`, `AnyWithProps` — existential types for collection storage
- `EventHandler<Tag>` — phantom marker for registered handlers
- `payloadMsgPack` — automatically derived `Msgpack.schema` of payload
- `PayloadWithTag`, `SuccessWithTag`, `ErrorWithTag` — tag-indexed extractors

## Source
- `raw/effect-smol/packages/effect/src/unstable/eventlog/Event.ts`

## Related
- [[effect-eventlog]]
- [[effect-eventlog-event-group]]
- [[effect-eventlog-event-log]]
- [[effect-unstable-encoding-msgpack]]
