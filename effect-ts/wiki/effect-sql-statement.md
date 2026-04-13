---
title: Statement (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# Statement (unstable)

Tagged-template DSL for building parameterised SQL fragments and statements. A `Fragment` is a sequence of `Segment`s (literal, identifier, parameter, array/record helpers, custom nodes). A `Statement<A>` is both a `Fragment` and an `Effect` that executes on the current connection, with variants for raw, values, unprepared, streaming, and compile-only outputs.

## Key Exports
- `Constructor` — callable template-tag producing `Statement<A>` with helpers `insert`, `update`, `updateValues`, `in`, `and`, `or`, `literal`, `join`, `onDialect`, `onDialectOrElse`, `reserve`, `withTransaction`
- `Statement` / `Fragment` — core interfaces
- `Dialect` — `"sqlite" | "pg" | "mysql" | "mssql" | "clickhouse"`
- `Segment` and constructors (`literal`, `identifier`, `parameter`, `arrayHelper`, `RecordInsertHelper`, `RecordUpdateHelper`, `Custom`)
- `Compiler` — driver-facing interface that turns fragments into `[sql, params]` with `withoutTransform` variant
- `make` — build the callable tagged-template client from connection acquirer, compiler, span attrs, and row transformer
- `Transformer` / `CurrentTransformer` — mid-flight statement rewriting hook
- `isFragment` / `isCustom` — guards

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/Statement.ts`

## Related
- [[effect-sql-sql-client]]
- [[effect-sql-sql-connection]]
