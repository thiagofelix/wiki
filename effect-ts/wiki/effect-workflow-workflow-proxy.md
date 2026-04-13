---
title: WorkflowProxy (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# WorkflowProxy (unstable)

Derives `RpcGroup` and `HttpApiGroup` definitions from a list of workflows so they can be exposed as external APIs. Each workflow produces a normal invocation rpc, a `Discard` variant (fire-and-forget), and a `Resume` variant for completing durable deferreds.

## Key Exports
- `toRpcGroup` — derive a rpc group from workflows with optional tag prefix
- `toHttpApi` — derive an http api group from workflows
- `ResumePayload` — schema used by the `Resume` rpcs
- `ConvertRpcs` — type helper mapping workflows to rpc shapes

## Source
- `raw/effect-smol/packages/effect/src/unstable/workflow/WorkflowProxy.ts`

## Related
- [[effect-workflow]]
- [[effect-workflow-workflow]]
- [[effect-workflow-workflow-proxy-server]]
- [[effect-rpc-rpc-group]]
