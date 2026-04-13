---
title: Prompt (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Prompt (unstable)

Interactive terminal prompt builder used by CLI commands. A `Prompt<Output>` is a yieldable Effect that renders frames, processes user input, and submits an `Output` value. Includes built-in prompts (text, confirm, select, multi-select, date, file, number) plus a `custom` constructor for bespoke interactions.

## Key Exports
- `Prompt<Output>` — pipeable/yieldable prompt model
- `isPrompt` — type guard
- `Environment` — required services (`FileSystem`, `Path`, `Terminal`)
- `Action<State, Output>` — `Beep | NextFrame | Submit` tagged union for frame transitions
- `Handlers<State, Output>` — `render`, `process`, `clear` handler triple used to build custom prompts
- `custom` — constructs a prompt from `Handlers` and an initial state
- `text`, `hidden`, `password` — text-input prompts
- `confirm` — yes/no prompt
- `select`, `multiSelect` — list-selection prompts
- `date`, `integer`, `float`, `file` — typed prompts
- Combinators: `map`, `flatMap`, `filter`, `between`, `withValidation`

## Source
- `raw/effect-smol/packages/effect/src/unstable/cli/Prompt.ts`

## Related
- [[effect-ts-v4]]
- [[effect-cli]]
- [[effect-cli-primitive]]
- [[effect-cli-command]]
