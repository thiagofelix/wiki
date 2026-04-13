---
title: Utils (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Utils (unstable)

Internal helpers shared between `RpcServer` and `RpcClient` to implement the `run` loop. Provide a buffered-write adapter so protocols can be constructed before the actual write function is known, then swapped in when the server/client starts running.

## Key Exports
- `withRun` — helper for server/client services that expose a `run` method, buffering writes until run is invoked
- `withRunClient` — multi-client variant used by servers to manage per-client buffers and writers

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/Utils.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-server]]
- [[effect-rpc-rpc-client]]
