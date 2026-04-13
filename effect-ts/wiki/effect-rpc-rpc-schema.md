---
title: RpcSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcSchema (unstable)

Schema extensions specific to RPC: the `Stream` schema (used to model streaming rpc success values) and the `ClientAbort` cause annotation used by servers to describe client-aborted requests in traces.

## Key Exports
- `Stream` — schema constructor representing a `Stream.Stream<A, E>` over the wire
- `isStreamSchema` — guard for stream-wrapped schemas
- `getStreamSchemas` — extract success/error schemas from a stream schema
- `ClientAbort` — cause-annotating service marking client-initiated aborts

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcSchema.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc]]
- [[effect-stream]]
