---
title: Command (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Command (unstable)

Core module for defining CLI commands. A `Command` bundles a name, optional description/alias/examples, a typed config record of `Flag`s and `Argument`s, an Effectful handler, and optional subcommand groups. Commands compose hierarchically and parse argv via the internal lexer/parser, producing handler contexts consumed by `run`.

## Key Exports
- `Command<Name, Input, ContextInput, E, R>` — pipeable/yieldable command model
- `Command.Config` — shape of flag/argument configuration objects (nested allowed)
- `Command.Example` — command usage example
- `Command.Any` — any command type alias
- `make` — constructs a command from `(name, config?, handler?)`
- `withDescription`, `withShortDescription`, `withAlias`, `withExamples`, `withAnnotation` — metadata combinators
- `withSubcommands` — attaches subcommand groups
- `withHandler` — replaces or adds a handler
- `provide` / `provideService` — supply dependencies for the handler
- `run` — builds a runnable Effect from a root command and argv; handles help, version, completions, and `CliError` rendering
- `CommandContext` — context tag holding the currently executing command's metadata

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Command.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-flag]]
- [[effect-cli-argument]]
- [[effect-cli-global-flag]]
