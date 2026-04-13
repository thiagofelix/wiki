---
title: Terminal
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Terminal

Service abstraction over an interactive command-line terminal. Reads keystrokes and lines from stdin, queries column width, and writes text to stdout. A `QuitError` models the user pressing Ctrl+C during a prompt.

## Key Exports
- `Terminal` — interface with `columns`, `readInput`, `readLine`, `display`
- `Terminal` (Context.Service) — service tag
- `Key` — pressed-key descriptor with modifier flags
- `UserInput` — character + key combination
- `QuitError` — Schema error class for user quit
- `isQuitError` — guard
- `make` — construct a Terminal implementation

## Source
- `raw/effect-smol/packages/effect/src/Terminal.ts`

## Related
- [[effect-ts-v4]]
- Complements [[effect-stdio]]; used by CLI prompt libraries
