---
title: Msgpack (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Msgpack (unstable)

MessagePack codec implemented as `Channel` transforms built on the `msgpackr` library. Provides stateful pack/unpack streams that buffer incomplete bytes between chunks, plus schema-driven variants that compose with `ChannelSchema` for typed encode/decode pipelines.

## Key Exports
- `MsgPackError` — tagged `Pack`/`Unpack` error
- `encode` — `Channel` from unknown array to `Uint8Array<ArrayBuffer>[]`
- `decode` — `Channel` from `Uint8Array` to unknown, buffering incomplete tails
- `encodeSchema(schema)` — typed encoder via `ChannelSchema.encode`
- `decodeSchema(schema)` — typed decoder
- `duplex`, `duplexSchema` — bidirectional variants over a `Channel`
- `schema<S>` — schema annotation for msgpack serialization
- Uses `Packr`/`Unpackr` instances per stream

## Source
- `raw/effect-smol/packages/effect/src/unstable/encoding/Msgpack.ts`

## Related
- [[effect-unstable-encoding]]
- [[effect-channel]]
- [[effect-schema]]
