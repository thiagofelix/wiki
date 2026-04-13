---
title: WorkflowProxyServer (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WorkflowProxyServer (unstable)

Provides layers implementing the `RpcGroup` / `HttpApiGroup` produced by `WorkflowProxy`. Each derived endpoint forwards to the underlying workflow's `execute`/`resume` functions with structured logging, so a `RpcServer` or `HttpApi` can publish workflows transparently.

## Key Exports
- `layerHttpApi` — layer implementing an http api group for the given workflows
- `layerRpcHandlers` — layer implementing the rpc handlers derived by `WorkflowProxy.toRpcGroup`

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/WorkflowProxyServer.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow-proxy]]
- [[effect-workflow-workflow-engine]]
- [[effect-httpapi-http-api-builder]]
