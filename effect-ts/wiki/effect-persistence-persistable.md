---
title: Persistable (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-persistence]]

# Persistable (unstable)

Request-like objects that carry their own primary key plus success/error schemas, enabling `Persistence` and `PersistedCache` to store and replay their `Exit`s. Provides a `Class` constructor that combines `Request`, `PrimaryKey`, and schema-typed success/error channels.

## Key Exports
- `Persistable` — interface extending `PrimaryKey` with `{ success, error }` schema pair
- `symbol` — brand identifying persistable values
- `Any` — top type
- `SuccessSchema` / `ErrorSchema` / `Success` / `Error` — type extractors
- `Services` / `DecodingServices` / `EncodingServices` — aggregate service types
- `TimeToLiveFn` — `(exit, request) => Duration.Input` signature used by caches
- `Class` — constructor producing a tagged persistable request class with `payload`, `primaryKey`, `success`, `error`
- `serializeExit` / `deserializeExit` — encode/decode an Exit via the success/error schemas

## Source
- `raw/effect-smol/packages/effect/src/unstable/persistence/Persistable.ts`

## Related
- [[effect-persistence-persistence]]
- [[effect-schema]]
