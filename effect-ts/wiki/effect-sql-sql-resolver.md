---
title: SqlResolver (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlResolver (unstable)

Batched `RequestResolver` constructors for SQL queries. Groups multiple request payloads into a single execution, validates inputs via a request schema, and decodes results via a result schema. Supports ordered, grouped (multi-result), id-keyed, and void variants.

## Key Exports
- `SqlRequest` — a `Request` carrying an encoded payload with hash/equal by payload
- `request` — run a resolver for a given payload, returning an Effect
- `ordered` — resolver where results are zipped 1:1 with requests (fails on length mismatch)
- `grouped` — resolver that returns non-empty arrays of results grouped by a key
- `findById` — resolver that maps ids to a single result
- `void` — resolver that discards results
- `partitionRequests` — internal helper that encodes and deduplicates request payloads

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlResolver.ts`

## Related
- [[effect-request-resolver]]
- [[effect-sql-sql-schema]]
