---
title: Utils (@effect/openapi-generator)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Utils (@effect/openapi-generator)

String and identifier helpers shared by the code generators. Provides camelCase conversion, operation-id-to-identifier mapping, JSDoc comment rendering, and array spreading helpers.

## Key Exports
- `camelize(self)` — convert a string to camelCase
- `identifier(operationId)` — capitalize a camelized operation id
- `nonEmptyString(a)` — return trimmed string or undefined
- `toComment` — renders a `/** ... */` block from an optional description
- `spreadElementsInto(source, destination)` — imperative concat helper

## Source
- `raw/effect-smol/packages/tools/openapi-generator/src/Utils.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-openapi-generator-httpapitransformer]]
