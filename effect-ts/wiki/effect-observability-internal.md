---
title: observability/internal (unstable)
type: concept
sources: []
created: 2026-04-12
updated: 2026-04-12
---

# observability/internal (unstable)

Aggregate note covering internal OTLP protobuf encoding utilities used by `OtlpSerialization.layerProtobuf`. Not part of the public API, but documents the wire-format approach used for OpenTelemetry export.

## Key Modules
- `internal/protobuf.ts` — low-level protobuf wire encoders (varint, fixed32/64, length-delimited, tag); `WireType` constants
- `internal/otlpProtobuf.ts` — `encodeAnyValue`, `encodeKeyValueList`, `encodeResource`, `encodeTracesData`, `encodeMetricsData`, `encodeLogsData` following `opentelemetry-proto` definitions
- Emits `Uint8Array` payloads for `application/x-protobuf` bodies
- Handles `AnyValue` oneof fields (string/int/double/bool/array/kvlist/bytes)

## Source
- `raw/effect-smol/packages/effect/src/unstable/observability/internal/protobuf.ts`
- `raw/effect-smol/packages/effect/src/unstable/observability/internal/otlpProtobuf.ts`

## Related
- [[effect-observability]]
- [[effect-observability-otlp-serialization]]
