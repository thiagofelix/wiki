---
title: Effect Pkg Sql D1 Client
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

### D1Client (@effect/sql-d1)

SqlClient for Cloudflare D1 (`@cloudflare/workers-types` `D1Database`). Uses a prepared-statement cache and the SQLite compiler. Transactions are not supported by D1 and will die if attempted; `updateValues` is also unsupported. The module exposes a single-connection acquirer suitable for Workers.

## Key Exports
- `D1Client` (tag, interface) — SqlClient specialization
- `D1ClientConfig` — `{ db, prepareCacheSize, prepareCacheTTL, transformResultNames, transformQueryNames, spanAttributes }`
- `make(config)` — constructor `Effect<D1Client, never, Scope | Reactivity>`
- `layer(config)` — Layer providing `D1Client` and `SqlClient`
- `layerConfig(config)` — Layer from `Config.Wrap`
- `TypeId` — branded identifier

## Notes
- `executeStream` throws at runtime (D1 does not stream)
- Transactions are disabled (`transactionAcquirer` dies)

## Source
- `raw/effect-smol/packages/sql/d1/src/D1Client.ts`

## Related
- [[effect-pkg-sql]]
- [[effect-sql]]
- [[effect-ts-v4]]
