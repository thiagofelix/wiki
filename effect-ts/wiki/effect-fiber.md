---
title: Fiber
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Fiber

Lightweight, user-space threads that are the unit of concurrency in Effect. Fibers execute Effects cooperatively with structured concurrency guarantees — parent fibers manage children, interruption is safe and resource-aware, and millions of fibers can exist concurrently. Each fiber carries an id, scheduler, context, log level, current span, and observer list.

## Key Exports
- `Fiber<A, E>` — runtime fiber interface
- `await` — wait for exit as an Effect
- `join` — wait and rethrow failures
- `interrupt`, `interruptAll` — cooperative cancellation
- `poll` — non-blocking status check
- `roots`, `children` — supervision introspection
- `getCurrentFiber` — retrieve the running fiber
- `Fiber.Variance` — variance encoding for subtype checks

## Source
- `raw/effect-smol/packages/effect/src/Fiber.ts`

## Related
- [[effect-ts-v4]]
- [[effect-effect]]
- [[effect-fiber-handle]]
- [[effect-fiber-map]]
- [[effect-fiber-set]]
