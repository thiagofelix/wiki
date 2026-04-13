---
title: Scheduler
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Scheduler

Controls how Effect fibers dispatch work and yield control. The default `MixedScheduler` batches tasks by priority and uses `setImmediate` to run them asynchronously, with configurable sync/async mode and yield thresholds to keep fibers fair.

## Key Exports
- `Scheduler` — interface with `executionMode`, `shouldYield`, `makeDispatcher`
- `SchedulerDispatcher` — `scheduleTask(task, priority)` and `flush`
- `Scheduler` (Context.Reference) — service handle, default `MixedScheduler`
- `MixedScheduler` — default implementation with priority buckets
- `MaxOpsBeforeYield` — reference (default 2048) bounding fiber ops per tick
- `DisableYield` — reference to bypass yield checks

## Source
- `raw/effect-smol/packages/effect/src/Scheduler.ts`

## Related
- [[effect-ts-v4]]
- Used by Fiber runtime; complements Effect evaluation loop
