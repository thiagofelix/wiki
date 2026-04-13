---
title: SqlMessageStorage (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# SqlMessageStorage (unstable)

SQL-backed implementation of `MessageStorage`. Uses a migrations runner to provision `cluster_messages` and `cluster_replies` tables, supports Postgres/MySQL/SQLite dialect differences, persists envelopes with deliver-at scheduling, and exposes polling/save APIs backing the durable mailbox.

## Key Exports
- `make` — effect building a `MessageStorage` service from a `SqlClient`
- `layer` — layer providing `MessageStorage` backed by SQL (with optional table prefix)

## Source
- `raw/effect-smol/packages/effect/src/unstable/cluster/SqlMessageStorage.ts`

## Related
- [[effect-cluster]]
- [[effect-cluster-message-storage]]
- [[effect-sql-sql-client]]
- [[effect-sql-migrator]]
