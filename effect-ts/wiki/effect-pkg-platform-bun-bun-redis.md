---
title: BunRedis (@effect/platform-bun)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# BunRedis (@effect/platform-bun)

Effect-wrapped adapter around Bun's native `RedisClient`. Provides a `BunRedis` service that holds the raw client plus a `use` helper, and bridges it into the core `Redis` persistence service so that KeyValueStore-style layers can run on Bun without external dependencies.

## Key Exports
- `BunRedis` — Context.Service tag with client + use
- `layer` — direct layer from RedisOptions
- `layerConfig` — layer wrapping Config-driven options

## Source
- `raw/effect-smol/packages/platform-bun/src/BunRedis.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-platform-bun]]
- [[effect-unstable-persistence-redis]]
