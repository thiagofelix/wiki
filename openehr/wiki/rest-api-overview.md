---
title: REST API Overview
type: entity
sources:
  - raw/its-rest-overview.md
created: 2026-04-13
updated: 2026-04-13
---

# REST API Overview

The openEHR REST API Overview specification (ITS-REST Release 1.0.3, STABLE) defines the general conventions, request/response patterns, headers, status codes, and data representation rules that apply across all openEHR REST API endpoints. It serves as the foundational document for the EHR, Query, Definition, and other API specifications. See [[rest-api]] for the specific endpoint details.

## HTTP Methods

| Method | Description |
|--------|-------------|
| GET | Transfer current representation of the target resource |
| HEAD | Check resource existence; return status without content |
| POST | Perform resource-specific processing on the request payload |
| PUT | Replace all current representations of the target resource |
| DELETE | Remove all current representations of the target resource |
| OPTIONS | Describe communication options for the target resource |

## Authentication and Authorization

The specification does not mandate a specific authentication scheme but requires:

- Services MUST use `WWW-Authenticate` and/or `Proxy-Authenticate` headers appropriately
- Services MUST return `401 Unauthorized`, `403 Forbidden`, or `407 Proxy Authentication` when applicable
- Clients MUST use `Authorization` and `Proxy-Authorization` headers

## Custom Headers

### openEHR-VERSION and openEHR-AUDIT_DETAILS

For committing change-controlled resources (COMPOSITION, EHR_STATUS, FOLDER, etc.), services accept custom headers for client-provided committal metadata:

```http
openEHR-VERSION.lifecycle_state: code_string="532"
openEHR-AUDIT_DETAILS.change_type: code_string="251"
openEHR-AUDIT_DETAILS.description: value="Updated composition"
openEHR-AUDIT_DETAILS.committer: name="John Doe", external_ref.id="BC8132EA..."
```

These are optional. Provided values merge with server-side defaults at commit time.

**Lifecycle state codes:** 532 (complete), 553 (incomplete), 523 (deleted)

**Change type codes:** 249 (creation), 250 (amendment), 251 (modification), 252 (synthesis), 523 (deleted), 666 (attestation), 253 (unknown)

### openEHR-TEMPLATE_ID

Must be used when committing COMPOSITIONs via PUT or POST using simplified data formats that do not include `LOCATABLE.archetype_details.template_id` (see [[simplified-formats]]).

## Resource Identification

### Identifier Types

- **versioned_object_uid** -- identifies the VERSIONED_OBJECT container (HIER_OBJECT_ID format, e.g., `8849182c-82ad-4088-a07f-48ead4180515`)
- **version_uid** -- identifies a specific VERSION within the container (OBJECT_VERSION_ID format: `object_id::creating_system_id::version_tree_id`, e.g., `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2`)
- **ehr_id** -- identifies an EHR (UUID format)

### Explicit vs Implicit Identification

Resources can be addressed in two ways:

**Explicit (version_uid):** Returns a specific version:
```
GET /ehr/{ehr_id}/composition/8849182c...::openEHRSys.example.com::5
```

**Implicit (versioned_object_uid):** Returns the latest version:
```
GET /ehr/{ehr_id}/composition/8849182c...
```

The implicit form is a moving target -- it references the latest version, which changes over time.

## Optimistic Concurrency

The `If-Match` header prevents accidental overwrites when multiple agents act on the same resource:

```http
If-Match: "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2"
```

If the condition evaluates to false, the service returns HTTP `412 Precondition Failed` with the latest `version_uid` in `Location` and `ETag` headers.

## Response Negotiation

The `Prefer` header controls response verbosity:

- `Prefer: return=minimal` -- only essential response content; `Location` header required; use `204 No Content` when appropriate (this is the default)
- `Prefer: return=representation` -- full resource representation in response body
- `Prefer: return=representation, resolve_refs` -- additionally resolve OBJECT_REF identifiers to full/partial representations

## ETag and Last-Modified

- `ETag` provides an opaque validator for the resource version (typically the `version_uid`)
- `Last-Modified` contains the modification datetime from `VERSION.commit_audit.time_committed.value`

Both headers should be present in responses targeting VERSION, VERSIONED_OBJECT, or similar versioned resources.

## Status Codes

Key status codes and their openEHR-specific usage:

| Code | Meaning | openEHR Usage |
|------|---------|---------------|
| 200 | OK | Successful retrieval |
| 201 | Created | Resource created (POST) |
| 204 | No Content | Success with minimal response |
| 400 | Bad Request | Malformed syntax or invalid content |
| 404 | Not Found | Resource does not exist |
| 406 | Not Acceptable | Requested format not supported |
| 409 | Conflict | Duplicate or conflicting resource |
| 412 | Precondition Failed | If-Match condition failed |
| 415 | Unsupported Media Type | Payload format not supported |
| 422 | Unprocessable Entity | Well-formed but semantically invalid |

### Error Response Format

When `Prefer: return=representation` is set, services may return structured errors:

```json
{
  "message": "Error message",
  "code": 90000,
  "errors": [
    {
      "_type": "DV_CODED_TEXT",
      "value": "Error message",
      "defining_code": {
        "terminology_id": { "value": "local" },
        "code_string": "9000"
      }
    }
  ]
}
```

## Supported Data Formats

Services must support at least one of XML or JSON canonical formats.

| Format | Content-Type | Description |
|--------|-------------|-------------|
| Canonical XML | `application/xml` | Valid against published XSDs |
| Canonical JSON | `application/json` | Valid against published JSON-Schemas; attributes in lowercase snake_case |
| Flat JSON | `application/openehr.wt.flat+json` | Simplified flat format (see [[simplified-formats]]) |
| Structured JSON | `application/openehr.wt.structured+json` | Simplified structured format |
| Near-Canonical Flat JSON | `application/openehr.nc.flat+json` | ECISFLAT format |
| TDS XML | `application/openehr.tds2+xml` | Template Data Schema XML |
| Text | `text/plain` | ADL2 templates or AQL queries |

### JSON Conventions

- Attribute names must be lowercase snake_case matching the RM
- Metadata attributes are prefixed with `_` (e.g., `_type` for RM type discrimination)
- Null values, empty lists, and empty arrays should be absent in JSON
- `_type` is required when polymorphism is involved or the RM type is abstract

### Datetime Format

All date/time values must comply with ISO 8601. The recommended form is extended format for human readability: `YYYY-MM-DDThh:mm:ss.sss[Z|+/-hh:mm]`. Timezone should only be supplied when needed.

## OpenAPI Specification

The API is formally defined as OpenAPI Specification 3.0 YAML files in two variants:

- **Codegen variant** -- optimized for code generation tools (uses `allOf` inheritance and discriminators)
- **Validation variant** -- optimized for data validation (uses flattened schemas and `oneOf` union types)

## System Conformance

The `OPTIONS` method on the API root returns a conformance manifest:

```json
{
  "solution": "openEHRSys",
  "solution_version": "v0.9",
  "vendor": "My-openEHR",
  "restapi_specs_version": "v1.0.3",
  "conformance_profile": "STANDARD",
  "endpoints": ["/ehr", "/definition", "/query"]
}
```

## Related Pages

- [[rest-api]] -- specific API endpoint definitions for EHR, Query, and Definition services
- [[simplified-formats]] -- developer-friendly data formats accepted by the REST API
- [[reference-model]] -- the canonical RM that API payloads represent
