---
title: OtlpSerialization (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# OtlpSerialization (unstable)

Pluggable serialization service selecting JSON or Protobuf encoding for OTLP traces, metrics, and logs payloads. Consumers depend on the `OtlpSerialization` service tag; a layer provides the concrete encoder used by the exporter.

## Key Exports
- `OtlpSerialization` — service class with `traces`, `metrics`, `logs` encoders
- `layerJson` — encodes bodies as JSON
- `layerProtobuf` — encodes bodies as `application/x-protobuf` via internal protobuf encoders
- Returns `HttpBody` for exporter consumption

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/OtlpSerialization.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp]]
- [[effect-observability-internal]]
- [[effect-unstable-http-body]]
