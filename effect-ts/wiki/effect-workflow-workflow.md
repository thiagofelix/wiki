---
title: Workflow (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Workflow (unstable)

Top-level workflow definition. A workflow is a named durable process with payload/success/error schemas and an execute function that is registered with a `WorkflowEngine`. The engine replays workflows from persisted activity state, supports idempotency keys, discard semantics, polling for results, and interrupting executions.

## Key Exports
- `Workflow` — interface exposing `execute`, `poll`, `interrupt`, annotation helpers
- `make` — build a workflow from name, payload, and idempotency key
- `withCompensation` — attach compensation effects for the saga pattern
- `Execution` — context reference for the current workflow execution name
- `Registration` — layer that registers a workflow with the engine
- `layer` — layer variant attaching an execute handler
- `Result` — tagged union describing workflow outcomes (Complete, Suspended, Interrupted)
- `AnyStructSchema` / `AnyWithProps` — erased type helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/Workflow.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow-engine]]
- [[effect-workflow-activity]]
- [[effect-workflow-durable-deferred]]
