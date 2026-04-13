---
title: Resource (@effect/opentelemetry)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# Resource (@effect/opentelemetry)

Provides the OpenTelemetry `Resource` service used by tracer, metrics, and logger providers to tag telemetry with service metadata. Supports static configuration, loading from `OTEL_SERVICE_NAME` and `OTEL_RESOURCE_ATTRIBUTES` environment variables, and sensible defaults for SDK name/language.

## Key Exports
- `Resource` — Context service wrapping `Resources.Resource`
- `layer(config)` — Layer from `{ serviceName, serviceVersion?, attributes? }`
- `layerFromEnv(additionalAttributes?)` — Layer that reads OTel env vars
- `layerEmpty` — empty resource Layer
- `configToAttributes(options)` — helper mapping config to OTel semantic attributes

## Source
- `raw/effect-smol/packages/opentelemetry/src/Resource.ts`

## Related
- [[effect-ts-v4]]
- [[effect-pkg-opentelemetry]]
- [[effect-pkg-opentelemetry-nodesdk]]
