---
title: WorkflowEngine (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WorkflowEngine (unstable)

Service abstraction that runs and persists workflows. Engines register workflows, execute them with a given execution id, record activity results, schedule durable clocks, resume suspended instances, and surface polling APIs. Concrete engines are provided by `ClusterWorkflowEngine` and in-memory implementations for tests.

## Key Exports
- `WorkflowEngine` — service with `register`, `execute`, `poll`, `interrupt`, `activityExecute`, `deferredResult`, `scheduleClock`, `resume`
- `WorkflowInstance` — per-execution service describing the running workflow (name, execution id, mailbox)
- `WorkflowInstance.Service` — struct holding instance state (pending activities, deferreds, clocks)
- `layerMemory` — in-memory engine for testing

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/WorkflowEngine.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow]]
- [[effect-cluster-cluster-workflow-engine]]
- [[effect-workflow-activity]]
