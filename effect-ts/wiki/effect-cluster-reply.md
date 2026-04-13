---
title: Reply (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Reply (unstable)

Reply types produced by entity handlers for their in-flight requests. Replies come as `WithExit` (full success/error/defect) or `Chunk` (for streaming rpcs), and can be serialized/deserialized via schema. `ReplyWithContext` additionally keeps handler context so callbacks can encode in the right environment.

## Key Exports
- `Reply<R>` — union of `WithExit` and `Chunk`
- `Encoded` — wire-format reply union
- `WithExit` / `WithExitEncoded` — terminal reply with an `Exit`
- `Chunk` / `ChunkEncoded` — stream chunk reply keyed by sequence
- `ReplyWithContext` — reply bundled with handler context and its rpc
- `serialize` / `deserialize` — schema-driven codecs
- `isReply` — type guard

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Reply.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-message]]
- [[effect-cluster-envelope]]
