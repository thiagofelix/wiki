---
title: Ndjson (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Ndjson (unstable)

Newline-delimited JSON codec implemented as `Channel` transforms. Supports both string and `Uint8Array` variants, line-splitting with incomplete buffer carry-over on decode, and schema-typed encode/decode pipelines and duplex helpers for bidirectional communication.

## Key Exports
- `NdjsonError` — tagged `Pack`/`Unpack` error
- `encodeString`, `encode` — `Channel` from unknown to `string`/`Uint8Array`
- `decodeString`, `decode` — `Channel` to unknown from strings/bytes
- `encodeSchema(schema)`, `decodeSchema(schema)` — schema-typed variants
- `encodeSchemaString`, `decodeSchemaString` — string-only schema variants
- `duplexSchema`, `duplexSchemaString` — bidirectional typed channels
- Used by DevTools client/server and Socket transport

## Source
- `raw/effect-smol/packages/effect/src/unstable/encoding/Ndjson.ts`

## Related
- [[effect-unstable-encoding]]
- [[effect-channel]]
- [[effect-devtools-dev-tools-client]]
