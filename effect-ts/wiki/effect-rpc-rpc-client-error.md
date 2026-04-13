---
title: RpcClientError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcClientError (unstable)

Error classes produced by `RpcClient` when something goes wrong outside of user-defined rpc errors: transport failures, worker errors, protocol defects. Unified so callers can match a single error type and inspect its discriminated `reason`.

## Key Exports
- `RpcClientError` — schema error wrapping a typed `reason` (worker, socket, http, defect)
- `RpcClientDefect` — schema error for unexpected client-side defects

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcClientError.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-http-http-client-error]]
