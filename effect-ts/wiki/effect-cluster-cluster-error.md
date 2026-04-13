---
title: ClusterError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ClusterError (unstable)

Tagged error classes describing failures raised by the cluster runtime: routing, serialization, persistence, and delivery failures. Each is a `Schema.ErrorClass` so it can cross RPC boundaries.

## Key Exports
- `EntityNotAssignedToRunner` — runner received a message for an entity it does not own
- `MalformedMessage` — envelope/payload failed to encode or decode (with `refail` helper)
- `PersistenceError` — persisting a message or reply into storage failed
- `MailboxFull` — entity mailbox at capacity for a request
- `AlreadyProcessingMessage` — duplicate request for an in-flight message id
- `RunnerUnavailable` — remote runner could not be reached
- `EntityNotManagedByRunner` — entity lifecycle managed elsewhere

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ClusterError.ts`

## Related
- [[effect-cluster]]
- [[effect-ts-v4]]
- [[effect-cluster-sharding]]
