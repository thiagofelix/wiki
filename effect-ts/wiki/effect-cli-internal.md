---
title: CLI internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# CLI internal (unstable)

Internal implementation details powering `effect/unstable/cli`. Not part of the public API; the public `Command`/`Flag`/`Argument`/`Completions` modules re-export only what is needed. Organized into lexer, parser, config merging, help assembly, auto-suggestion, ANSI helpers, and shell-completion backends.

## Contents
- `ansi.ts` — minimal ANSI escape-code helpers used by `Prompt` and `CliOutput` for colored rendering
- `auto-suggest.ts` — Levenshtein-based suggestion helper used to produce `UnrecognizedOption`/`UnknownSubcommand` suggestion lists
- `command.ts` — internal command representation (`TypeId`, `makeCommand`, `makeParser`, `toImpl`, `checkForDuplicateFlags`); the runtime the public `Command` module builds on
- `config.ts` — config record merging (`mergeConfig`) and recursive parsing (`parseConfig`) that walks a `Command.Config` tree and wires flags/arguments to parsers
- `help.ts` — builds `HelpDoc` from a command tree (`getHelpForCommandPath`, `getGlobalFlagsForCommandPath`, `getGlobalFlagsForCommandTree`)
- `lexer.ts` — tokenizes argv into flag/argument/value tokens, handling `--flag=value`, `-abc` bundling, `--`, etc.
- `parser.ts` — consumes lexer tokens and produces `ParsedArgs` (flag map + positional list) validated against a command's config
- `completions/` — subdirectory with `CommandDescriptor.ts` (normalized command tree for completions) and `bash.ts`, `zsh.ts`, `fish.ts` script generators used by the public `Completions.generate`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/internal/` (multiple files)

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-command]]
- [[effect-cli-completions]]
