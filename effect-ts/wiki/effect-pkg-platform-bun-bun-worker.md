---
title: BunWorker (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunWorker (@effect/platform-bun)

Implements `WorkerPlatform` for Bun `globalThis.Worker`. Setup acquires a close-aware finalizer that posts a shutdown message, waits up to 5 seconds for the worker's `close` event, then forcibly terminates if still alive. Listen wires message/error events into the generic worker runner queue.

## Key Exports
- `layer` — merges platform with a user-provided spawner
- `layerPlatform` — WorkerPlatform layer for Bun workers

## Source
- `raw/effect-smol/packages/platform-bun/src/BunWorker.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-unstable-workers-worker]]
