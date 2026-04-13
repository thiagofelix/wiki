---
title: Plugins (@effect/bundle)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Plugins (@effect/bundle)

Rollup plugin pipeline used by the `bundle` CLI to build fixture bundles. Configures node resolution, constant replacement for `process.env.NODE_ENV`, esbuild transform targeting a node version, terser minification, optional visualizer, and a custom resolver that maps `@effect/*` and `effect` imports to their local `dist` directories.

## Key Exports
- `PluginOptions` — `{ nodeTarget, minify, mangle, visualize }`
- `createResolveLocalPackageImports` — custom plugin resolving Effect packages locally
- `createPlugins` — returns the full Rollup plugin pipeline

## Source
- `raw/effect-smol/packages/tools/bundle/src/Plugins.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-tools]]
- [[effect-pkg-tools-bundle-rollup]]
