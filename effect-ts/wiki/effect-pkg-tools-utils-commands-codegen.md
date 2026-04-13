---
title: commands/codegen (@effect/utils)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# commands/codegen (@effect/utils)

`codegen` subcommand of the `@effect/utils` CLI that wires the `BarrelGenerator` service to discover annotated barrel files and rewrite them. Accepts `--cwd` and `--pattern` flags with sensible defaults matching `src/**/index.ts`.

## Key Exports
- `codegen` — `Command.make("codegen", ...)` instance with flags and handler
- Flags: `--cwd` (directory, defaults to `.`), `--pattern` (defaults to `src/**/index.ts`)
- Provides a merged Layer of `Codegen.layer` and `Glob.layer`

## Source
- `raw/effect-smol/packages/tools/utils/src/commands/codegen.ts`
- `raw/effect-smol/packages/tools/utils/src/bin.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-utils-codegen]]
