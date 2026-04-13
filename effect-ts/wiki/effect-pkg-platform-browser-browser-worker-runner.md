---
title: BrowserWorkerRunner (@effect/platform-browser)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BrowserWorkerRunner (@effect/platform-browser)

Implements `WorkerRunnerPlatform` for code running inside a browser Worker, SharedWorker, or Window. Handles `onconnect` for SharedWorkers, tracks multiple message ports, forwards messages into the runner queue, and wires error propagation through Deferred.

## Key Exports
- `make` — builds a runner service for a given MessagePort or Window
- `layer` — runner platform layer for the current `self`
- `layerMessagePort` — runner platform layer for an explicit port/window

## Source
- `raw/effect-smol/packages/platform-browser/src/BrowserWorkerRunner.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-browser]]
- [[effect-workers-worker-runner]]
