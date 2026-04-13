---
title: HelpDoc (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# HelpDoc (unstable)

Format-independent data structure describing a command's help documentation. Rather than producing a string directly, commands produce a `HelpDoc` that formatters (text, markdown, JSON) consume. Captures description, usage, flags, args, subcommand groups, examples, global flags, and custom annotations.

## Key Exports
- `HelpDoc` — top-level help model
- `FlagDoc` — documentation for a single flag (name, aliases, type, description, required)
- `ArgDoc` — documentation for a positional argument
- `SubcommandGroupDoc` — grouped list of subcommand summaries
- `SubcommandDoc` — summary entry for a subcommand
- `ExampleDoc` — a `command`+`description` example entry
- Consumed by `CliOutput.Formatter.formatHelpDoc`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/HelpDoc.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-cli-output]]
- [[effect-cli-command]]
