---
title: Flag (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Flag (unstable)

Constructors for named command-line flags/options. Produces `Flag<A>` values (specialized `Param`s with `kind = "flag"`) for use in `Command` configs. Boolean flags support `--name`/`--no-name` negation, and the module provides the full range of primitives plus enum and redacted variants.

## Key Exports
- `Flag<A>` — flag parameter interface (alias of `Param.Param<"flag", A>`)
- `string(name)`, `boolean(name)`, `integer(name)`, `float(name)`, `date(name)` — primitive flags
- `file(name, { mustExist? })` / `directory(name, { mustExist? })` — path flags
- `choice(name, choices)` — enum flag with typed value mapping
- `redacted(name)` — redacted-string flag
- `keyValue(name)` / `keyValueMap(name)` — `key=value` pair flag
- Combinators via shared `Param` (map, optional, withDefault, withAlias, variadic, etc.)

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Flag.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-argument]]
- [[effect-cli-param]]
