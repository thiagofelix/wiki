---
title: Param (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Param (unstable)

Polymorphic implementation shared by `Argument` and `Flag`. A `Param<Kind, A>` pairs a parser over `ParsedArgs` with combinators (map, transform, optional, variadic, withDefault, withAlias). The `Kind` type parameter (`"argument" | "flag"`) keeps positionals and flags type-distinct while reusing the same parse/combinator machinery.

## Key Exports
- `Param<Kind, A>` — polymorphic parameter interface
- `ParamKind` — `"argument" | "flag"`
- `Any`, `AnyArgument`, `AnyFlag` — type aliases
- `argumentKind`, `flagKind` — kind discriminator constants
- `Environment` — services required by parsers (`FileSystem`, `Path`, `Terminal`, `ChildProcessSpawner`)
- `Parse<A>` — parser function type
- `string`, `boolean`, `integer`, `float`, `date`, `file`, `directory`, `choice`, `redacted` — primitive constructors (kind-parameterized)
- Combinators: `map`, `transform`, `optional`, `withDefault`, `withDescription`, `withAlias`, `variadic`, `repeated`
- Integrates with `Primitive` parsers and `Config`/`Redacted`
- Internal module — public API is re-exported via `Argument` and `Flag`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Param.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-argument]]
- [[effect-cli-flag]]
- [[effect-cli-primitive]]
