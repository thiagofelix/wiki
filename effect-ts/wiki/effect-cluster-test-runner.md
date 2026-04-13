---
title: TestRunner (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# TestRunner (unstable)

Convenience layer that assembles an in-memory cluster (sharding + runners + message storage + runner storage) for testing workflows and entities without external dependencies.

## Key Exports
- `layer` — layer exposing `Sharding`, `Runners`, `MessageStorage`, and `MemoryDriver`, backed by in-memory implementations and the noop runner health

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/TestRunner.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-single-runner]]
- [[effect-cluster-sharding]]
- [[effect-cluster-message-storage]]
