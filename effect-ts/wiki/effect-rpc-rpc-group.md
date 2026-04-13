---
title: RpcGroup (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcGroup (unstable)

Collection of `Rpc` endpoints tied together as a service definition. Supports composition (`add`, `merge`), prefixing, middleware application, handler derivation via `toHandlers` / `toLayer`, and acts as the surface used by both clients and servers.

## Key Exports
- `RpcGroup<R>` — interface with `requests` map, composition, and handler helpers
- `make` — build a group from a set of rpcs
- `add` / `merge` — add rpcs or combine groups
- `middleware` — attach middleware to the group's rpcs
- `prefix` — prefix tags with a common string
- `toHandlers` / `toLayer` — build a context / layer implementing the group
- `HandlersFrom` / `HandlersServices` — type helpers
- `accessHandlers` — read handlers from context

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcGroup.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc]]
- [[effect-rpc-rpc-middleware]]
- [[effect-rpc-rpc-server]]
