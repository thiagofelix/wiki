---
title: SqlError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlError (unstable)

Schema-backed tagged error classes covering the common failure modes of SQL drivers. Each error carries `cause`, optional `message`, and optional `operation`, and exposes an `isRetryable` flag so higher-level layers can apply retry policies.

## Key Exports
- `ConnectionError` — retryable connection-level failure
- `AuthenticationError` — credential failure
- `AuthorizationError` — permission denied
- `SqlSyntaxError` — malformed SQL
- `ConstraintError` — constraint violation (unique, fk, check)
- `ResultLengthMismatch` — expected vs actual row count mismatch
- `SqlError` — union of the above
- `SqlError.make` — helper for wrapping arbitrary driver errors

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlError.ts`

## Related
- [[effect-sql-sql-client]]
- [[effect-schema]]
