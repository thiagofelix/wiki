---
title: Reporter (@effect/bundle)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Reporter (@effect/bundle)

Service that drives Rollup bundling for all fixtures and renders markdown tables comparing current vs. previous gzipped sizes. Supports a selected-file-only report and a visualize mode that writes `*.min.js` outputs and rollup-plugin-visualizer artifacts.

## Key Exports
- `Reporter` — Context service `{ report, reportSelected, visualize }`
- `ReporterError` — tagged error for reporter failures
- `ReportOptions` / `VisualizeOptions` / `ReportSelectedOptions`
- `Reporter.layer` — Layer composing `Fixtures.layer` and `Rollup.layer`

## Source
- `raw/effect-smol/packages/tools/bundle/src/Reporter.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-bundle-rollup]]
- [[effect-pkg-tools-bundle-fixtures]]
