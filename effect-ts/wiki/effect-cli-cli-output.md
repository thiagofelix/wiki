---
title: CliOutput (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# CliOutput (unstable)

Service abstraction for formatting CLI output: help documents, errors, and version strings. Allows swapping the default text renderer for custom formats (markdown, JSON, colored/uncolored) via a `Formatter` interface supplied as a layer.

## Key Exports
- `Formatter` — interface: `formatHelpDoc`, `formatCliError`, `formatError`, `formatErrors`, `formatVersion`
- `Formatter` tag — `Context.Service` for injecting the current formatter
- `defaultFormatter` — built-in text formatter with optional ANSI colors
- `layer` — builds a `Layer<Formatter>` from a `Formatter` instance
- `layerDefault` — layer providing `defaultFormatter`
- Integrates with `HelpDoc` and `CliError` to render user-facing strings

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/CliOutput.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-help-doc]]
- [[effect-cli-cli-error]]
