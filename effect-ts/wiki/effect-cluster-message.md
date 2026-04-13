---
title: Message (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Message (unstable)

Internal message wrappers that sit between `Envelope`s and entity handlers. Each message carries an envelope plus respond callbacks and any last-sent reply used for idempotent delivery. Distinguishes incoming (received by a runner) from outgoing (about to be dispatched) and local vs remote variants.

## Key Exports
- `Incoming<R>` / `IncomingLocal<R>` — union of incoming request + envelope types
- `IncomingRequest` / `IncomingRequestLocal` — wrapped request with respond callback
- `IncomingEnvelope` — wrapped ack/interrupt envelope
- `Outgoing<R>` / `OutgoingRequest` / `OutgoingEnvelope` — analogous outgoing wrappers
- `incomingLocalFromOutgoing` — promote an outgoing message to a local incoming one

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Message.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-envelope]]
- [[effect-cluster-reply]]
