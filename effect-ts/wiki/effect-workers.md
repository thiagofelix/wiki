---
title: effect/unstable/workers (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/workers (hub)

Platform-agnostic worker abstraction for Effect applications. Defines service tags for the host (`WorkerPlatform`) and the worker runtime (`WorkerRunnerPlatform`), plus a `Transferable` helper for zero-copy data transfer over worker boundaries. Concrete implementations live in platform packages (e.g. `@effect/platform-node`, `@effect/platform-browser`).

## Entries
- [[effect-workers-worker]] — `WorkerPlatform`, `Worker<O, I>`, `makePlatform`
- [[effect-workers-worker-runner]] — in-worker counterpart handling inbound messages
- [[effect-workers-worker-error]] — tagged error schemas for lifecycle failures
- [[effect-workers-transferable]] — `Collector` and schema helpers for `Transferable` values

## Source
- `raw/effect-smol/packages/effect/src/unstable/workers/`

## Related
- [[effect-ts-v4]]
- [[effect-schema]]
- [[effect-scope]]
