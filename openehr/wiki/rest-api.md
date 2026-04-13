---
title: REST API (ITS-REST)
type: entity
sources:
  - raw/its-rest-ehr.md
  - raw/its-rest-query.md
  - raw/its-rest-definition.md
created: 2026-04-13
updated: 2026-04-13
---

# REST API (ITS-REST)

The openEHR REST API defines standardized HTTP endpoints for interacting with an openEHR platform. Defined as OpenAPI 3.0 specifications.

## API Groups

### EHR API

Manages EHR records and their contents.

#### EHR Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/ehr` | Create new EHR (system-assigned ehr_id) |
| PUT | `/ehr/{ehr_id}` | Create EHR with specified ehr_id |
| GET | `/ehr/{ehr_id}` | Get EHR by ehr_id |
| GET | `/ehr?subject_id=...&subject_namespace=...` | Get EHR by subject |

#### EHR_STATUS Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | `/ehr/{ehr_id}/ehr_status` | Get current EHR_STATUS |
| PUT | `/ehr/{ehr_id}/ehr_status` | Update EHR_STATUS |
| GET | `/ehr/{ehr_id}/ehr_status/{version_uid}` | Get specific version |

#### COMPOSITION Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/ehr/{ehr_id}/composition` | Create Composition |
| PUT | `/ehr/{ehr_id}/composition/{uid}` | Update Composition |
| DELETE | `/ehr/{ehr_id}/composition/{uid}` | Delete (logical) Composition |
| GET | `/ehr/{ehr_id}/composition/{uid}` | Get Composition |
| GET | `/ehr/{ehr_id}/composition/{uid}?version_at_time=...` | Get at specific time |

#### DIRECTORY Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/ehr/{ehr_id}/directory` | Create directory |
| PUT | `/ehr/{ehr_id}/directory` | Update directory |
| DELETE | `/ehr/{ehr_id}/directory` | Delete directory |
| GET | `/ehr/{ehr_id}/directory` | Get directory |

#### CONTRIBUTION Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/ehr/{ehr_id}/contribution` | Create contribution |
| GET | `/ehr/{ehr_id}/contribution/{uid}` | Get contribution |

### Content Negotiation

Supports multiple formats via `Accept` / `Content-Type` headers:
- `application/json` — JSON format
- `application/xml` — XML format

### Versioning Headers

| Header | Purpose |
|--------|---------|
| `If-Match` | Optimistic locking — must match current version UID |
| `ETag` | Current version UID in response |
| `Location` | URL of created/updated resource |

### Query API

Execute [[archetype-query-language|AQL]] queries against the platform.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/query/aql?q=...` | Execute ad-hoc AQL query |
| POST | `/query/aql` | Execute AQL with body parameters |
| GET | `/query/{qualified_query_name}` | Execute stored query |
| POST | `/query/{qualified_query_name}` | Execute stored query with parameters |
| GET | `/query/{qualified_query_name}/{version}` | Execute specific version |

#### Query Parameters
- `q` — AQL query string
- `query_parameters` — map of parameter name → value
- `offset` / `fetch` — pagination
- `ehr_id` — scope to specific EHR

#### Result Structure (RESULT_SET)
```json
{
  "meta": { "href": "...", "type": "RESULTSET", "executed_aql": "..." },
  "name": "...",
  "columns": [
    { "name": "systolic", "path": "/data[at0001]/.../items[at0004]/value" }
  ],
  "rows": [
    [{ "_type": "DV_QUANTITY", "magnitude": 120, "units": "mm[Hg]" }]
  ]
}
```

### Definition API

Manage archetypes, templates, and stored queries.

#### Template Management
| Method | Path | Description |
|--------|------|-------------|
| POST | `/definition/template/adl1.4` | Upload OPT 1.4 template |
| GET | `/definition/template/adl1.4` | List templates |
| GET | `/definition/template/adl1.4/{template_id}` | Get template |
| POST | `/definition/template/adl2` | Upload ADL2 template |
| GET | `/definition/template/adl2` | List templates |
| GET | `/definition/template/adl2/{template_id}` | Get template |

#### Stored Query Management
| Method | Path | Description |
|--------|------|-------------|
| GET | `/definition/query` | List stored queries |
| PUT | `/definition/query/{qualified_query_name}` | Store/update query |
| GET | `/definition/query/{qualified_query_name}` | Get stored query |
| DELETE | `/definition/query/{qualified_query_name}` | Delete stored query |

#### Qualified Query Names
Format: `{namespace}::{query-name}`

Example: `org.example::active-medications`

Versioning follows semantic versioning. The `LATEST` tag always points to the most recent version.
