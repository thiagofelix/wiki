---
title: effect/unstable/cli (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# effect/unstable/cli (hub)

CLI framework for Effect v4. Build hierarchical command trees with typed flags and positional arguments, auto-generated help, ANSI output, interactive terminal prompts, and shell completion scripts (bash/zsh/fish). Parsing is powered by a lexer+parser that consumes argv into a `ParsedArgs` structure and validates it against a command's `Config` of `Flag` and `Argument` parameters, both built on a shared `Param` implementation over low-level `Primitive` parsers. Errors are returned as a structured `CliError` union rendered by a pluggable `CliOutput.Formatter`.

## Modules
- [[effect-cli-argument]] — positional argument constructors
- [[effect-cli-cli-error]] — tagged CLI error union
- [[effect-cli-cli-output]] — pluggable output/formatter service
- [[effect-cli-command]] — core `Command` model and `run` entrypoint
- [[effect-cli-completions]] — shell completion script generator
- [[effect-cli-flag]] — named flag/option constructors
- [[effect-cli-global-flag]] — action/setting global flags
- [[effect-cli-help-doc]] — format-independent help document model
- [[effect-cli-param]] — shared polymorphic parameter implementation
- [[effect-cli-primitive]] — low-level string→value parsers (incl. config files)
- [[effect-cli-prompt]] — interactive terminal prompts
- [[effect-cli-index]] — barrel re-export of the subsystem
- [[effect-cli-internal]] — lexer, parser, help builder, completions backends

## Related
- [[effect-ts-v4]]
- [[source-effect-smol-repo]]
