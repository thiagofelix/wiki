---
title: Runners (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Runners (unstable)

Service encapsulating communication with peer runners. Provides local and remote send paths, request/response streaming, ping, and handles persistence semantics before dispatch. Also defines the shared `Rpcs` group used by `RunnerServer` and the `RpcClientProtocol` tag used to plug transports.

## Key Exports
- `Runners` — service with `ping`, `sendLocal`, `send`, `notify`, and stream helpers
- `Rpcs` — the runner-to-runner rpc group (`Ping`, `Notify`, `Effect`)
- `RpcClientProtocol` — context tag for the client protocol factory
- `layer` — default layer wiring up runners from a client protocol
- `layerNoop` — in-process layer (no remote runners)

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/Runners.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-runner-server]]
- [[effect-cluster-sharding]]
- [[effect-rpc-rpc-client]]
