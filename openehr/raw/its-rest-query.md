# Query API - OpenEHR REST Specifications

## Overview

This specification describes service endpoints and data models for querying openEHR systems using the Archetype Query Language (AQL).

**Status**: STABLE
**License**: Creative Commons Attribution-NoDerivs 3.0 Unported
**Contact**: info@openehr.org

---

## Table of Contents

1. [Introduction](#introduction)
2. [Query Types](#query-types)
3. [Qualified Query Names](#qualified-query-names)
4. [Request Details](#request-details)
5. [Response Details](#response-details)
6. [API Endpoints](#api-endpoints)
7. [Resource Schemas](#resource-schemas)

---

## Introduction

### Purpose

This document specifies REST service endpoints and data models for querying openEHR systems. The primary query language is the Archetype Query Language (AQL).

### Related Documents

- [Archetype Query Language (AQL)](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)
- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)
- [openEHR Platform Abstract Service Model](https://specifications.openehr.org/releases/SM/latest/openehr_platform.html)

### Amendment History

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| 5.1 | SPECITS-66: Migrate to OpenAPI Specification | S Iancu | 19 Dec 2022 |
| 4.1 | SPECITS-41: Add double quotes to ETag headers | S Iancu | 21 Mar 2021 |
| 4.0 | SPECITS-47: Fix query_parameter(s) inconsistency | P Pazos, S Iancu | 06 Mar 2021 |
| 3.1 | SPECITS-37: Fix endpoint and content-type errors | P Pazos, J Smolka, S Iancu | 01 Oct 2019 |

---

## Query Types

### Single EHR Queries

Execute queries within a specific EHR by supplying either:
- Query parameter: `ehr_id`
- Request header: `openEHR-EHR-id`

Both contain an EHR identifier taken from `EHR.ehr_id.value`.

### Population Queries

Execute queries across multiple EHRs without specifying an `ehr_id` parameter. Use cases include:

- Ward lists
- Pandemic correlation analysis
- Research (epidemiology, population health)

### Stored Queries

Queries with definitions registered on the server, identified by qualified name and optional version. Advantages:

- Separation of concerns between query authors and consumers
- Reduced network overhead (no long query strings)
- Query reusability

Query definitions can be managed via the [Definition API](definition.html#tag/Query).

### Ad-hoc Queries

Unregistered queries executed as-is via the Execute ad-hoc AQL endpoint. Query definition supplied in request body or parameter without server-side storage.

---

## Qualified Query Names

Stored queries are identified by `qualified_query_name` with optional version.

### Format

```
[{namespace}::]{query-name}[@version]
```

- **Namespace**: Optional; uses reverse domain notation (e.g., `org.openehr`)
- **Query name**: Alphanumeric, underscore, period, hyphen characters only: `[a-zA-Z0-9_.-]`
- **Version**: Optional SEMVER format (e.g., `1.2.3`, `1.2`, `1`)

### Valid Examples

```
org.openehr::my_compositions
my_compositions
ehr::all_influenza_vacc_candidates
org.openehr::my_compositions@1.0.2
```

### Version Matching

When partial version supplied or omitted, the system uses the latest version matching the prefix:

- `1` matches highest version starting with `1.x.x`
- `1.0` matches highest version starting with `1.0.x`
- Omitted version matches latest available

---

## Request Details

### Example Query Request

```json
{
  "q": "SELECT o/data[at0002]/events[at0003]/data[at0001]/items[at0004]/value/magnitude AS temperature FROM EHR[ehr_id/value='554f896d-faca-4513-bddf-664541146308d'] CONTAINS Observation o[openEHR-EHR-OBSERVATION.body_temperature-zn.v1] WHERE o/data[at0002]/events[at0003]/data[at0001]/items[at0004]/value/magnitude > $temperature",
  "query_parameters": {
    "temperature": 38.5
  }
}
```

### GET vs POST

**GET method limitations**:
- URI length restrictions
- Character encoding requirements

**Recommendation**: Use POST for complex queries with extensive parameters or large result sets.

### Common Headers and Query Parameters

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ehr_id` | string | No | Execute within specific EHR context; from `EHR.ehr_id.value` |
| `offset` | integer | No | Row number to start from (0-based); default: 0 |
| `fetch` | integer | No | Maximum rows to return; implementation-dependent default |
| `query_parameters` | object | No | Named placeholders replacing `$variable` patterns in AQL |

#### Request Headers

| Header | Type | Description |
|--------|------|-------------|
| `openEHR-EHR-id` | string | EHR identifier; alternative to `ehr_id` parameter |
| `Content-Type` | string | `application/json` (for POST requests) |

#### Response Headers

| Header | Type | Description |
|--------|------|-------------|
| `ETag` | string | Unique identifier of the result set |

### About the ehr_id Parameter

- Supply when executing single EHR queries
- MAY enable backend routing, optimization
- MUST NOT be supplied for population/multi-patient queries
- Use either as query parameter or `openEHR-EHR-id` header

### Query Parameters

Query parameters replace placeholders within AQL queries. They must NOT be prefixed with `$` in requests.

#### Parameter Example

**AQL Query Definition**:
```aql
SELECT c/name/value FROM COMPOSITION c WHERE c/uid/value = $uid
```

**Request**:
```
GET https://openEHRSys.example.com/v1/query/myQuery?uid=90910cf0-66a0-4382-b1f8-c0f27e81b42d::openEHRSys.example.com::1
```

**Multiple Parameters**:
```
GET https://openEHRSys.example.com/v1/query/com.vendor::compositions?temperature_from=36&temperature_unit=Cel
```

The server adds `$` prefix and formats parameters as valid AQL.

See [AQL Parameters specification](https://specifications.openehr.org/releases/QUERY/latest/AQL.html#_parameters) for details.

---

## Response Details

### RESULT_SET Response Structure

```json
{
  "meta": {
    "_href": "https://openEHRSys.example.com/v1/query/org.openehr::compositions",
    "_type": "RESULTSET",
    "_schema_version": "1.0.0",
    "_created": "2017-08-19T00:25:47.568+02:00",
    "_generator": "openEHRSys.ResultSets.Serialization.Json.ResultSetJsonWriter",
    "_executed_aql": "SELECT e/ehr_id/value... WHERE obs/data[...]/value/magnitude >= 50"
  },
  "name": "org.openehr::compositions",
  "q": "SELECT e/ehr_id/value... WHERE obs/data[...]/value/magnitude >= $systolic_bp",
  "columns": [
    {
      "name": "#0",
      "path": "/ehr_id/value"
    },
    {
      "name": "startTime",
      "path": "/context/start_time/value"
    }
  ],
  "rows": [
    [
      "81433066-c417-4813-9b29-79783e7bed23",
      "2017-02-16T13:50:11.308+01:00",
      140,
      "90910cf0-66a0-4382-b1f8-c0f27e81b42d::openEHRSys.example.com::1",
      {
        "_type": "DV_TEXT",
        "value": "Labs"
      }
    ]
  ]
}
```

### RESULT_SET Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `meta` | object | Yes | Result metadata (implementation-dependent) |
| `name` | string | No | Qualified name of stored query |
| `q` | string | Yes | Original AQL query |
| `columns` | array | Yes | Column specifications from SELECT clause |
| `rows` | array | Yes | Result row data |

### Metadata Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `_href` | URI | No | URL of executed query (GET only) |
| `_type` | string | No | Type of serialized result object |
| `_schema_version` | string | No | Specification version for object |
| `_created` | date-time | No | Result creation timestamp (ISO 8601) |
| `_generator` | string | No | Application identifier (for debugging) |
| `_executed_aql` | string | No | Actual AQL executed after parameter substitution |

---

## API Endpoints

### Execute Ad-hoc AQL (GET)

Execute unregistered AQL query using query parameters.

```
GET /v1/query/aql
```

#### Query Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `q` | string (AQL) | Yes | `SELECT e/ehr_id/value... FROM EHR e...` |
| `ehr_id` | string | No | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| `offset` | integer | No | `10` |
| `fetch` | integer | No | `10` |
| `query_parameters.*` | mixed | No | `systolic_bp=140` |

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input (missing required params, syntax errors) |
| 408 | Query execution timeout |

#### Response Example

```json
{
  "meta": {
    "_created": "2017-08-19T00:25:47.568+02:00",
    "_executed_aql": "SELECT e/ehr_id/value... >= 50"
  },
  "q": "SELECT e/ehr_id/value...",
  "columns": [],
  "rows": [[]]
}
```

---

### Execute Ad-hoc AQL (POST)

Execute unregistered AQL query using request body.

```
POST /v1/query/aql
Content-Type: application/json
```

#### Request Body

```json
{
  "q": "SELECT e/ehr_id/value... WHERE obs/data[...]/value/magnitude >= $systolic_bp",
  "offset": 10,
  "fetch": 10,
  "query_parameters": {
    "ehr_id": "7d44b88c-4199-4bad-97dc-d78268e01398",
    "systolic_bp": 140
  }
}
```

#### Request Body Schema

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string (AQL) | Yes | AQL query to execute |
| `offset` | integer | No | Row start position (0-based) |
| `fetch` | integer | No | Maximum rows to return |
| `query_parameters` | object | No | Named parameter values |

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input (missing/malformed params) |
| 408 | Query execution timeout |

---

### Execute Stored AQL (GET)

Execute registered query by name at latest version.

```
GET /v1/query/{qualified_query_name}
```

#### Path Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `qualified_query_name` | string | Yes | `org.openehr::compositions` |

#### Query Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `ehr_id` | string | No | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| `offset` | integer | No | `10` |
| `fetch` | integer | No | `10` |
| `query_parameters.*` | mixed | No | `systolic_bp=140` |

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input (missing/malformed params) |
| 404 | Query not found |
| 408 | Query execution timeout |

---

### Execute Stored AQL (POST)

Execute registered query by name at latest version using request body.

```
POST /v1/query/{qualified_query_name}
Content-Type: application/json
```

#### Path Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `qualified_query_name` | string | Yes | `org.openehr::compositions` |

#### Request Body

```json
{
  "offset": 10,
  "fetch": 10,
  "query_parameters": {
    "ehr_id": "7d44b88c-4199-4bad-97dc-d78268e01398",
    "systolic_bp": 140
  }
}
```

#### Request Body Schema

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `offset` | integer | Yes | Row start position (0-based) |
| `fetch` | integer | Yes | Maximum rows to return |
| `query_parameters` | object | Yes | Named parameter values |

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input |
| 404 | Query not found |
| 408 | Query execution timeout |

---

### Execute Stored AQL Version (GET)

Execute registered query by name at specific version.

```
GET /v1/query/{qualified_query_name}/{version}
```

#### Path Parameters

| Parameter | Type | Required | Example | Notes |
|-----------|------|----------|---------|-------|
| `qualified_query_name` | string | Yes | `org.openehr::compositions` | Fully qualified name |
| `version` | string | Yes | `1.0` | SEMVER; can be partial (e.g., `1` for latest 1.x.x) |

#### Query Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `ehr_id` | string | No | `7d44b88c-4199-4bad-97dc-d78268e01398` |
| `offset` | integer | No | `10` |
| `fetch` | integer | No | `10` |
| `query_parameters.*` | mixed | No | `systolic_bp=140` |

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input |
| 404 | Query or version not found |
| 408 | Query execution timeout |

---

### Execute Stored AQL Version (POST)

Execute registered query by name at specific version using request body.

```
POST /v1/query/{qualified_query_name}/{version}
Content-Type: application/json
```

#### Path Parameters

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `qualified_query_name` | string | Yes | `org.openehr::compositions` |
| `version` | string | Yes | `1.0` |

#### Request Body

```json
{
  "offset": 10,
  "fetch": 10,
  "query_parameters": {
    "ehr_id": "7d44b88c-4199-4bad-97dc-d78268e01398",
    "systolic_bp": 140
  }
}
```

#### Responses

| Status | Meaning |
|--------|---------|
| 200 | Query executed successfully |
| 400 | Invalid input |
| 404 | Query or version not found |
| 408 | Query execution timeout |

---

## Resource Schemas

### AdhocQueryExecute (Ad-hoc Query Request)

Request schema for ad-hoc query execution.

```json
{
  "q": "SELECT e/ehr_id/value FROM EHR e...",
  "offset": 10,
  "fetch": 10,
  "query_parameters": {
    "ehr_id": "7d44b88c-4199-4bad-97dc-d78268e01398",
    "systolic_bp": 140
  }
}
```

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string (AQL) | Yes | AQL query text |
| `offset` | integer | No | Row start position (0-based); default: 0 |
| `fetch` | integer | No | Maximum rows; implementation-dependent |
| `query_parameters` | object | No | Parameter name-value pairs |

---

### StoredQueryExecute (Stored Query Request)

Request schema for stored query execution.

```json
{
  "offset": 10,
  "fetch": 10,
  "query_parameters": {
    "ehr_id": "7d44b88c-4199-4bad-97dc-d78268e01398",
    "systolic_bp": 140
  }
}
```

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `offset` | integer | Yes | Row start position (0-based); default: 0 |
| `fetch` | integer | Yes | Maximum rows to return |
| `query_parameters` | object | Yes | Parameter name-value pairs |

---

### RESULT_SET (Query Response)

Response schema for all query executions.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `meta` | object | Yes | Metadata (see below) |
| `name` | string | No | Stored query name (qualified format) |
| `q` | string | Yes | Original AQL query |
| `columns` | array | Yes | Column definitions from SELECT |
| `rows` | array | Yes | Result rows (array of arrays) |

### RESULT_SET_COLUMN

Column specification object.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Column name or generated identifier |
| `path` | string | Yes | Path expression from AQL SELECT |

### ResultSetMetadata

Optional metadata properties (implementation-dependent).

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `_href` | URI | No | Executed query URL (GET only) |
| `_type` | string | No | Object type identifier |
| `_schema_version` | string | No | Specification version |
| `_created` | date-time | No | Creation timestamp (ISO 8601) |
| `_generator` | string | No | Application identifier |
| `_executed_aql` | string | No | AQL after parameter substitution |
| Additional properties | any | No | Implementation-specific attributes |

---

## References

- **AQL Specification**: https://specifications.openehr.org/releases/QUERY/latest/AQL.html
- **Service Model**: https://specifications.openehr.org/releases/SM/latest/openehr_platform.html

---

**Source:** https://specifications.openehr.org/releases/ITS-REST/latest/query.html
