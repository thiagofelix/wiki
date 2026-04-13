---
title: Primitive (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Primitive (unstable)

Low-level parsers that turn raw strings into typed values. `Primitive<A>` is the building block `Param`/`Argument`/`Flag` use to validate user input. Includes parsers for primitives, dates, file/directory paths, and structured config files (JSON/YAML/TOML/INI).

## Key Exports
- `Primitive<A>` — `{ _tag, parse: (value: string) => Effect<A, string, FileSystem | Path> }`
- `string`, `boolean`, `integer`, `float`, `date` — scalar primitives
- `path(kind, mustExist)` — file/directory path primitive
- `choice(choices)` — enum primitive
- `redacted` — wraps a value in `Redacted`
- `config(name, schema)` — loads and parses a config file (`ini`, `toml`, `yaml`, or JSON) into a typed value via `Schema`
- `make` — constructs a custom primitive
- `isTrueValue` / `isFalseValue` / `isBoolean` — internal helpers tied to `Config.TrueValues`/`FalseValues`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Primitive.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-param]]
- [[effect-cli-argument]]
- [[effect-cli-flag]]
