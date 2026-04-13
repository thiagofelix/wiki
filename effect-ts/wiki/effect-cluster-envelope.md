---
title: Envelope (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Envelope (unstable)

Wire-level message types used when routing messages between runners. Every envelope carries a snowflake request id, an `EntityAddress`, and metadata. Comes in three flavors: `Request` (with payload/tag/headers/trace), `AckChunk` (stream backpressure acknowledgement), and `Interrupt` (request cancellation).

## Key Exports
- `Envelope<R>` — union of request, ack, and interrupt for a given rpc
- `Encoded` — wire-format union of encoded envelopes
- `Request` / `PartialRequest` — request envelope (decoded and partial/schema form)
- `AckChunk` / `AckChunkEncoded` — stream chunk acknowledgement
- `Interrupt` / `InterruptEncoded` — request interruption signal
- `TypeId` — envelope discriminator symbol

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Envelope.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-message]]
- [[effect-cluster-snowflake]]
