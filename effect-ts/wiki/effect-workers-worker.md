---
title: Worker (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Worker (unstable)

Platform-agnostic Effect worker abstraction. `WorkerPlatform` is a service tag that spawns `Worker<O, I>` handles; `makePlatform` builds a platform implementation from a setup/listen pair for a specific runtime (Web Workers, Node worker_threads, etc.). Handles message buffering before spawn-ready and lifecycle via `Scope`.

## Key Exports
- `WorkerPlatform` — service tag with `spawn(id)` method
- `Worker<O, I>` — interface with `send`, `run(handler, options?)`
- `makeUnsafe` — builds a `Worker` from raw send/run primitives
- `PlatformMessage` — `[ready: 0] | [data: 1, unknown]` protocol
- `Spawner` — service tag for the platform's spawn function
- `SpawnerFn<W>` — `(id: number) => W`
- `layerSpawner` — provides a `Spawner`
- `makePlatform` — builds `WorkerPlatform` from `{ setup, listen }` hooks
- Buffers outbound messages until port is ready

## Source
- `raw/effect-smol/packages/effect/src/unstable/workers/Worker.ts`

## Related
- [[effect-workers]]
- [[effect-workers-worker-runner]]
- [[effect-workers-worker-error]]
