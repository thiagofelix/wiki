---
title: BunWorkerRunner (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunWorkerRunner (@effect/platform-bun)

Implements `WorkerRunnerPlatform` for code running inside a Bun Worker. Posts the initial handshake, dispatches incoming messages through the user-provided handler, tracks child fibers, and surfaces errors as `WorkerError` with structured reasons.

## Key Exports
- `layer` — default WorkerRunnerPlatform layer

## Source
- `raw/effect-smol/packages/platform-bun/src/BunWorkerRunner.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-unstable-workers-worker-runner]]
