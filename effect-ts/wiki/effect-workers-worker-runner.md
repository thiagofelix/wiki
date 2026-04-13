---
title: WorkerRunner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WorkerRunner (unstable)

Counterpart of `Worker` that runs inside a worker context and handles incoming messages. `WorkerRunnerPlatform` is the service tag that creates a `WorkerRunner<O, I>`, which registers a message handler and can send output back to the spawning parent.

## Key Exports
- `WorkerRunner<O, I>` — interface with `run`, `send`, `sendUnsafe`, optional `disconnects` queue
- `WorkerRunnerPlatform` — service tag with `start<O, I>()`
- `PlatformMessage<I>` — `[request: 0, I] | [close: 1]`
- Handler signature `(portId: number, message: I) => Effect | void`
- Errors typed as `WorkerError`

## Source
- `raw/effect-smol/packages/effect/src/unstable/workers/WorkerRunner.ts`

## Related
- [[effect-workers]]
- [[effect-workers-worker]]
- [[effect-workers-worker-error]]
