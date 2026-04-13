---
title: ChannelSchema
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ChannelSchema

Bridges the `Channel` and `Schema` modules by providing encode/decode channels that transform streams of typed chunks into streams of encoded values (and back). Each operator returns a `Channel` whose input is a `NonEmptyReadonlyArray` of one side of a schema and output is a `NonEmptyReadonlyArray` of the other, propagating `SchemaError` in the error channel. Reach for it when building streaming pipelines where data crosses a serialization boundary (e.g. JSON over websockets, binary framing).

## Key Exports
- `encode` — channel that encodes a stream of `Type` chunks to `Encoded` chunks
- `encodeUnknown` — encode variant where output is typed as `unknown`
- `decode` — channel that decodes `Encoded` chunks to `Type` chunks
- `decodeUnknown` — decode variant accepting `unknown` input
- `duplex` — combine input and output schemas around an inner channel for full-duplex schema-aware communication

## Source
- `raw/effect-smol/packages/effect/src/ChannelSchema.ts`

## Related
- [[effect-ts-v4]]
- [[effect-channel]]
