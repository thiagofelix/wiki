---
title: ClusterWorkflowEngine (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# ClusterWorkflowEngine (unstable)

Implementation of `WorkflowEngine` that runs durable workflows on top of cluster sharding. Each registered workflow becomes an entity whose execution, activities, durable deferred, and resume messages are routed through the sharded mailbox. Provides exit persistence, resume/interrupt semantics, and integration with `DurableClock`.

## Key Exports
- `make` — effect that builds the `WorkflowEngine` service on top of `Sharding` and `MessageStorage`
- `layer` — layer providing `WorkflowEngine` for cluster deployments

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/ClusterWorkflowEngine.ts`

## Related
- [[effect-cluster]]
- [[effect-workflow]]
- [[effect-workflow-workflow-engine]]
- [[effect-cluster-sharding]]
