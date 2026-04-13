---
title: NodeWorkerRunner (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeWorkerRunner (@effect/platform-node)

Implements `WorkerRunnerPlatform` for code running inside a Node `worker_threads` parent port or a forked child process. Dispatches incoming messages to the user handler, logs unhandled errors, and wires messageerror/error/exit events to the close deferred.

## Key Exports
- `layer` — default WorkerRunnerPlatform layer

## Source
- `raw/effect-smol/packages/platform-node/src/NodeWorkerRunner.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-workers-worker-runner]]
