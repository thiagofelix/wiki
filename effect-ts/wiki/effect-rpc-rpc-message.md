---
title: RpcMessage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# RpcMessage (unstable)

Wire-level messages exchanged between RPC clients and servers. Includes encoded and decoded forms for requests, acknowledgements, interrupts, EOF, ping/pong, and server responses (exit, defect, chunk).

## Key Exports
- `FromClient` / `FromClientEncoded` — union of messages a client may send
- `FromServer` / `FromServerEncoded` — union of messages a server may send
- `RequestId` — branded bigint request identifier
- `Request` / `RequestEncoded` — request envelope
- `Ack` / `AckEncoded` — stream acknowledgement
- `Interrupt` / `InterruptEncoded` — request cancellation
- `ResponseExitEncoded` / `ResponseDefectEncoded` / `ResponseChunkEncoded` — server response variants
- `Ping` / `Eof` / `constPing` / `constPong` / `constEof` — keepalive and stream-termination markers

## Source
- `raw/effect-smol/packages/effect/src/unstable/rpc/RpcMessage.ts`

## Related
- [[effect-rpc]]
- [[effect-rpc-rpc-client]]
- [[effect-rpc-rpc-server]]
