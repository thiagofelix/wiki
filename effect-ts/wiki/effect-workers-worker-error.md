---
title: WorkerError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WorkerError (unstable)

Tagged error types for worker lifecycle failures, defined as `Schema.ErrorClass` variants. A single outer `WorkerError` wraps one of the inner reason classes and exposes the cause through a discriminated `reason` field.

## Key Exports
- `WorkerError` — outer class with `reason: WorkerErrorReason`
- `WorkerSpawnError` — thrown when spawning fails
- `WorkerSendError` — thrown when sending fails
- `WorkerReceiveError` — thrown when receiving/parsing fails
- `WorkerUnknownError` — catch-all
- `WorkerErrorReason` — union type + `Schema.Union` schema
- `isWorkerError` — type guard using the internal `TypeId`
- Each inner error has `_tag`, `message`, optional `cause`

## Source
- `raw/effect-smol/packages/effect/src/unstable/workers/WorkerError.ts`

## Related
- [[effect-workers]]
- [[effect-workers-worker]]
