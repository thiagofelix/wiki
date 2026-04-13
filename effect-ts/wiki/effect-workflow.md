---
title: effect/unstable/workflow (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/workflow (unstable)

Durable workflow primitives on top of the effect runtime. Workflows are named, schema-typed processes whose steps (`Activity`) are persisted so that an execution can be replayed and resumed across restarts. `DurableClock` and `DurableDeferred` let workflows suspend on timers or external events without tying up fibers. Execution is delegated to a `WorkflowEngine`, with a cluster implementation (`ClusterWorkflowEngine`) and an in-memory testing engine available. Workflows can be exposed as RPC or HTTP APIs via the `WorkflowProxy` helpers.

## Modules
- [[effect-workflow-activity]] — replay-safe workflow step
- [[effect-workflow-durable-clock]] — durable sleeps
- [[effect-workflow-durable-deferred]] — external-event suspension
- [[effect-workflow-workflow]] — top-level workflow definition
- [[effect-workflow-workflow-engine]] — engine service and instance context
- [[effect-workflow-workflow-proxy]] — derive rpc/http APIs from workflows
- [[effect-workflow-workflow-proxy-server]] — server layers for the proxies
- [[effect-workflow-internal]] — internal helpers

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/`

## Related
- [[effect-ts-v4]]
- [[effect-cluster]]
- [[effect-cluster-cluster-workflow-engine]]
- [[effect-rpc]]
