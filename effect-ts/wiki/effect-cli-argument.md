---
title: Argument (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Argument (unstable)

Constructors for positional command-line arguments. Produces `Argument<A>` values (specialized `Param`s with `kind = "argument"`) that plug into `Command.make` config records. Boolean positionals are intentionally omitted because they are ambiguous without a flag name; use `Flag.boolean` or `choice` instead.

## Key Exports
- `Argument<A>` — positional parameter interface (alias of `Param.Param<"argument", A>`)
- `string(name)` — positional string argument
- `integer(name)` — positional integer
- `float(name)` — positional float
- `date(name)` — ISO date positional
- `file(name, { mustExist? })` — file path positional
- `directory(name, { mustExist? })` — directory path positional
- `choice(name, choices)` — enum positional with typed mapping
- `redacted(name)` — redacted string positional
- `variadic` — combinator turning an argument into a variadic `ReadonlyArray<A>`
- Re-exports combinators (`map`, `withDefault`, `optional`, etc.) via the shared `Param` implementation

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Argument.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-flag]]
- [[effect-cli-param]]
