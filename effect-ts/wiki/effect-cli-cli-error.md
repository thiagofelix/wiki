---
title: CliError (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# CliError (unstable)

Tagged union of errors raised during CLI parsing. Each variant carries structured context (command path, option name, value, suggestions) that formatters can render into user-friendly messages, and integrates with Effect's `Runtime` failure rendering.

## Key Exports
- `CliError` — tagged union of all variants
- `isCliError` — type guard
- `UnrecognizedOption` — unknown flag with `suggestions` (levenshtein)
- `DuplicateOption` — option specified more than once
- `MissingOption` — required option not supplied
- `MissingArgument` — required positional not supplied
- `InvalidValue` — value failed primitive parsing
- `UnknownSubcommand` — unknown subcommand under a command
- `ShowHelp` — sentinel raised when `--help` is requested, carries `commandPath`
- `UserError` — general user-facing error
- All variants are `Schema.ErrorClass`es tagged under `~effect/cli/CliError/*`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/CliError.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-cli-output]]
- [[effect-cli-command]]
