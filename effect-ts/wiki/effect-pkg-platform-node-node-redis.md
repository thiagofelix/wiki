---
title: NodeRedis (@effect/platform-node)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# NodeRedis (@effect/platform-node)

Wraps `ioredis` as an Effect service and bridges it into the core `Redis` persistence service. Provides a `NodeRedis` tag exposing the raw client and a `use` helper, plus layers that accept either direct `RedisOptions` or a Config-wrapped variant.

## Key Exports
- `NodeRedis` — Context.Service tag with `client` and `use`
- `layer` — layer from direct options
- `layerConfig` — layer pulling options from Config

## Source
- `raw/effect-smol/packages/platform-node/src/NodeRedis.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-node]]
- [[effect-unstable-persistence-redis]]
