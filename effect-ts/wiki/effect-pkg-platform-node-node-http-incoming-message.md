---
title: NodeHttpIncomingMessage (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeHttpIncomingMessage (@effect/platform-node)

Abstract base class that adapts a Node `http.IncomingMessage` to the core `HttpIncomingMessage` interface. Provides cached `text`, `json`, `urlParamsBody`, `arrayBuffer`, and `stream` accessors using the `MaxBodySize` reference for safety.

## Key Exports
- `NodeHttpIncomingMessage` — abstract base implementing HttpIncomingMessage over Node

## Source
- `raw/effect-smol/packages/platform-node/src/NodeHttpIncomingMessage.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-http-http-incoming-message]]
