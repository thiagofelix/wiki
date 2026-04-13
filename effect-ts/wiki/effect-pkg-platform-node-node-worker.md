---
title: NodeWorker (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeWorker (@effect/platform-node)

Implements `WorkerPlatform` for both `node:worker_threads` Workers and `node:child_process` ChildProcess instances. Setup handles graceful postMessage-based shutdown with a 5 second fallback to `terminate`/`kill SIGKILL`; listen wires message/messageerror/error/exit events into the generic runner.

## Key Exports
- `layer` — merged platform layer plus spawner
- `layerPlatform` — WorkerPlatform layer

## Source
- `raw/effect-smol/packages/platform-node/src/NodeWorker.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-workers-worker]]
