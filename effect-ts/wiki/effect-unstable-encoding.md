---
title: effect/unstable/encoding (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/encoding (hub)

Streaming codecs for common wire formats implemented as `Channel` transforms. Each module exposes both raw and schema-driven variants so typed data can flow through bidirectional duplex channels. Used across DevTools, sockets, HTTP, and RPC subsystems.

## Entries
- [[effect-unstable-encoding-msgpack]] — MessagePack via `msgpackr`
- [[effect-unstable-encoding-ndjson]] — newline-delimited JSON
- [[effect-unstable-encoding-sse]] — Server-Sent Events parser

## Source
- `raw/effect-smol/packages/effect/src/unstable/encoding/`

## Related
- [[effect-ts-v4]]
- [[effect-channel]]
- [[effect-schema]]
- [[effect-encoding]]
