---
title: RpcTest (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcTest (unstable)

Helpers for testing rpc handlers without running a real transport. Wires an in-process server directly to a client so requests short-circuit through the effect runtime, avoiding serialization.

## Key Exports
- `makeClient` — build a client whose messages are routed to an in-memory server implementing the group

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcTest.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-rpc-rpc-server]]
