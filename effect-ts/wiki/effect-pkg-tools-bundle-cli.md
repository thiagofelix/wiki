---
title: Cli (@effect/bundle)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Cli (@effect/bundle)

Command surface for the `bundle` CLI exposing `compare`, `report`, and `visualize` subcommands. Drives the `Reporter` service to bundle fixture files with Rollup and produce markdown size reports or interactive treemap visualizations.

## Key Exports
- `cli` — `Command.make("bundle")` composed with subcommands
- `compare` — writes a markdown bundle-size diff vs. a base directory
- `report` — prints a table for user-selected fixture files
- `visualize` — renders bundle visualizations via multi-select prompt

## Source
- `raw/effect-smol/packages/tools/bundle/src/Cli.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-bundle-reporter]]
