---
title: SqlSchema (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

[[effect-ts-v4]] [[effect-sql]]

# SqlSchema (unstable)

Schema-validated wrappers for one-shot SQL queries. Each constructor takes a request schema, an optional result schema, and an `execute` function; it returns a typed function that encodes the input, runs the query, and decodes the output.

## Key Exports
- `findAll` — decode an array of results for a request
- `findNonEmpty` — like `findAll` but fails with `NoSuchElementError` if empty
- `findOne` — decode and return the first row, failing with `NoSuchElementError` on empty
- `findOneOption` — decode the first row as an `Option`
- `single` — expect exactly one row (fail on zero or multiple)
- `void` — run a mutating query and discard results

## Source
- `raw/effect-smol/packages/effect/src/unstable/sql/SqlSchema.ts`

## Related
- [[effect-schema]]
- [[effect-sql-sql-resolver]]
