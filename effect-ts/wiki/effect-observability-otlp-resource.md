---
title: OtlpResource (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpResource (unstable)

OTLP `Resource` model construction with environment variable fallback (`OTEL_RESOURCE_ATTRIBUTES`, `OTEL_SERVICE_NAME`, `OTEL_SERVICE_VERSION`). Also provides attribute-value conversion helpers used by the logger, metrics, and tracer modules to encode arbitrary JavaScript values into OTLP `AnyValue` / `KeyValue` structures.

## Key Exports
- `Resource` — interface with `attributes` and `droppedAttributesCount`
- `make` — builds a Resource from `{ serviceName, serviceVersion, attributes }`
- `fromConfig` — `Effect` that reads env vars and merges user options
- `serviceNameUnsafe` — extracts `service.name` attribute
- `entriesToAttributes` — iterable-to-`KeyValue[]` helper
- `unknownToAttributeValue` — JS to `AnyValue` (string/int/double/bool/array/kvlist)
- Types: `KeyValue`, `AnyValue`, `Fixed64`

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpResource.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-logger]]
- [[effect-observability-otlp-metrics]]
- [[effect-observability-otlp-tracer]]
