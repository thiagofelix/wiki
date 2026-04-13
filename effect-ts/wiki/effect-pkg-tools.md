---
title: @effect/tools (hub)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# @effect/tools (hub)

Umbrella for Effect's internal tooling monorepo section under `packages/tools/`. Groups six sub-packages that each ship their own CLI/service bundle: AI provider SDK codegen, example markdown docgen, bundle size reporting, OpenAPI to Effect source generation, custom Oxlint rules, and shared barrel-file codegen utilities.

## Sub-packages
- `@effect/ai-codegen` — discovers `codegen.{json,yaml}` for AI providers and regenerates Effect HttpClient sources
  - [[effect-pkg-tools-ai-codegen-config]], [[effect-pkg-tools-ai-codegen-discovery]], [[effect-pkg-tools-ai-codegen-generator]], [[effect-pkg-tools-ai-codegen-glob]], [[effect-pkg-tools-ai-codegen-postprocess]], [[effect-pkg-tools-ai-codegen-specfetcher]], [[effect-pkg-tools-ai-codegen-main]]
- `@effect/ai-docgen` — renders a directory of TS examples into Markdown
  - [[effect-pkg-tools-ai-docgen-glob]], [[effect-pkg-tools-ai-docgen-main]]
- `@effect/bundle` — Rollup-based fixture bundling and gzipped size reports
  - [[effect-pkg-tools-bundle-cli]], [[effect-pkg-tools-bundle-fixtures]], [[effect-pkg-tools-bundle-plugins]], [[effect-pkg-tools-bundle-reporter]], [[effect-pkg-tools-bundle-rollup]]
- `@effect/openapi-generator` — OpenAPI 3.x to Effect Schema / HttpApi / HttpClient code generation
  - [[effect-pkg-tools-openapi-generator-openapigenerator]], [[effect-pkg-tools-openapi-generator-jsonschemagenerator]], [[effect-pkg-tools-openapi-generator-httpapitransformer]], [[effect-pkg-tools-openapi-generator-openapitransformer]], [[effect-pkg-tools-openapi-generator-parsedoperation]], [[effect-pkg-tools-openapi-generator-openapipatch]], [[effect-pkg-tools-openapi-generator-utils]], [[effect-pkg-tools-openapi-generator-main]]
- `@effect/oxc` — Oxlint plugin shipping Effect-specific lint rules
  - [[effect-pkg-tools-oxc-oxlint]]
- `@effect/utils` — shared utility CLI, currently a barrel-file codegen command
  - [[effect-pkg-tools-utils-codegen]], [[effect-pkg-tools-utils-glob]], [[effect-pkg-tools-utils-commands-codegen]]

## Source
- `raw/effect-smol/packages/tools/`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-vitest]]
