# Definition API Specification

**Title:** Definition API openEHR specs
**Version:** latest
**Status:** STABLE
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Introduction](#introduction)
2. [Acknowledgements](#acknowledgements)
3. [API Endpoints](#api-endpoints)
4. [Resource Schemas](#resource-schemas)
5. [Amendment History](#amendment-history)

---

## Introduction

### Purpose

This specification outlines REST service endpoints, resources, and operations for interacting with the Definition openEHR API in a RESTful manner.

### Related Documentation

**Prerequisites:**
- Operational Template 2
- Archetype Query Language (AQL)

**Related Resources:**
- openEHR Architecture Overview
- Archetype Technology Overview
- XML-Schemas (XSD)
- JSON-Schemas and Simplified Data Template (SDT)
- openEHR Platform Abstract Service Model

### Status Notes

The specification is stable and available as an OpenAPI 3.0.3 file in YAML format for both validation and code generation purposes.

---

## Acknowledgements

### Editor

- Sebastian Iancu, Architect, Code24, Netherlands

### Key Contributors

The specification benefited from input across the openEHR community, including contributors from:
- Better (Slovenia)
- DIPS (Norway)
- Karolinska University Hospital (Sweden)
- CaboLabs (Uruguay)
- FreshEHR (UK)
- Cambio Healthcare Systems (Sweden)
- Ocean Informatics (Australia/UK)

### Trademarks

- "openEHR" is a trademark of the openEHR Foundation
- "OpenAPI" is a trademark of The Linux Foundation

---

## API Endpoints

### Base URL

```
https://{baseUrl}/v1
```

---

## ADL 1.4 Template Management

### Upload a Template

**Endpoint:** `POST /definition/template/adl1.4`

**Description:** Upload a new ADL 1.4 operational template (OPT).

**Header Parameters:**

| Parameter | Type | Default | Values |
|-----------|------|---------|--------|
| Prefer | string | return=minimal | "return=representation", "return=minimal" |

**Request Body:**

Content-Type: `application/xml`

Schema: oneOf
- OPERATIONAL_TEMPLATE (object)
- Raw XML string

**Responses:**

| Code | Description |
|------|-------------|
| 201 | Template uploaded successfully; Location header contains template_id; ETag may be present |
| 400 | Invalid content provided |
| 409 | Template with same template_id already exists |

**Example Request:**

```xml
<template xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns="http://schemas.openehr.org/v1">
  <language>
    <terminology_id>
      <value>ISO_639-1</value>
    </terminology_id>
    <code_string>en</code_string>
  </language>
  <template_id>
    <value>Vital Signs</value>
  </template_id>
  <concept>Vital Signs</concept>
  <!-- Additional template structure -->
</template>
```

---

### List Templates

**Endpoint:** `GET /definition/template/adl1.4`

**Description:** List available ADL 1.4 operational templates on the system.

**Response Code:** 200 OK

**Example Response:**

```json
[
  {
    "template_id": "Vital Signs",
    "concept": "Vital Signs",
    "archetype_id": "openEHR-EHR-COMPOSITION.encounter.v1",
    "created_timestamp": "2017-08-14T19:24:56.639Z"
  }
]
```

---

### Get a Template

**Endpoint:** `GET /definition/template/adl1.4/{template_id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string | Template identifier (e.g., "Vital Signs") |

**Header Parameters:**

| Parameter | Type | Required | Values |
|-----------|------|----------|--------|
| Accept | string | Yes | "application/json", "application/xml", "text/plain", "application/openehr.wt+json" |

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Template successfully retrieved |
| 400 | Invalid template_id format |
| 404 | Template not found |
| 406 | Unsupported Accept header value |

**Example Response (XML):**

```xml
<template xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns="http://schemas.openehr.org/v1">
  <language>
    <terminology_id>
      <value>ISO_639-1</value>
    </terminology_id>
    <code_string>en</code_string>
  </language>
  <template_id>
    <value>Vital Signs</value>
  </template_id>
  <!-- Full template structure -->
</template>
```

---

## ADL2 Template Management

### Upload a Template

**Endpoint:** `POST /definition/template/adl2`

**Description:** Upload a new ADL2 operational template.

**Query Parameters:**

| Parameter | Type | Example |
|-----------|------|---------|
| version | string | version=1.0.1 |

**Header Parameters:**

| Parameter | Type | Default | Values |
|-----------|------|---------|--------|
| Prefer | string | return=minimal | "return=representation", "return=minimal" |

**Request Body:**

Content-Type: `text/plain`

**Response Codes:**

| Code | Description |
|------|-------------|
| 201 | Template uploaded successfully |
| 400 | Invalid content |
| 409 | Template version already exists |

---

### List Templates

**Endpoint:** `GET /definition/template/adl2`

**Description:** List available ADL2 operational templates.

**Response Code:** 200 OK

**Example Response:**

```json
[
  {
    "template_id": "openEHR-EHR-COMPOSITION.t_clinical_info_ds_sf.v1.0.0",
    "version": "1.0.1",
    "concept": "Clinical detail",
    "archetype_id": "openEHR-EHR-COMPOSITION.discharge.v1",
    "created_timestamp": "2017-08-14T19:24:56.639Z"
  },
  {
    "template_id": "openEHR-EHR-COMPOSITION.t_vital_signs.v1.0.0",
    "version": "1.0.1",
    "concept": "Vital Signs",
    "archetype_id": "openEHR-EHR-COMPOSITION.encounter.v1",
    "created_timestamp": "2017-08-14T19:24:56.639Z"
  }
]
```

---

### Get Latest Template

**Endpoint:** `GET /definition/template/adl2/{template_id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string | Template identifier (e.g., "Vital Signs") |

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Template retrieved successfully |
| 400 | Invalid template_id |
| 404 | Template not found |

---

### Get Template at Version

**Endpoint:** `GET /definition/template/adl2/{template_id}/{version}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| template_id | string | Template identifier |
| version | string | SEMVER version (e.g., "1.0", "1.0.1", "1") |

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Template retrieved successfully |
| 400 | Invalid template_id or version format |
| 404 | Template not found at specified version |

---

## Stored Query Management

### List Stored Queries

**Endpoint:** `GET /definition/query/{qualified_query_name}`

**Description:** Retrieve all stored queries matching the qualified query name pattern.

**Path Parameters:**

| Parameter | Type | Format |
|-----------|------|--------|
| qualified_query_name | string | `[{namespace}::]{query-name}` |

**Pattern Examples:**

- `org.openehr` - Lists all queries with names starting with "org.openehr"
- `org.openehr::compositions` - Lists all versions of the named query

**Response Code:** 200 OK

**Example Response:**

```json
[
  {
    "name": "org.openehr::compositions",
    "type": "aql",
    "version": "1.0.1",
    "saved": "2017-07-16T19:20:30.450+01:00",
    "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id] CONTAINS COMPOSITION c[$compositionid] WHERE c/name/value = 'Vitals'"
  },
  {
    "name": "org.openehr::compositions",
    "type": "aql",
    "version": "1.1.7",
    "saved": "2018-06-13T09:37:20.530+01:00",
    "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id] CONTAINS COMPOSITION c[$uid] WHERE c/name/value = 'Vitals'"
  }
]
```

---

### Store a Query

**Endpoint:** `PUT /definition/query/{qualified_query_name}`

**Description:** Store a new query or update an existing one.

**Path Parameters:**

| Parameter | Type |
|-----------|------|
| qualified_query_name | string |

**Query Parameters:**

| Parameter | Type | Default |
|-----------|------|---------|
| query_type | string | "AQL" |

**Request Body:**

Content-Type: `text/plain`

Schema: AQL string

**Example Request:**

```
SELECT c FROM
  EHR e
    CONTAINS COMPOSITION c[openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION obs[openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
  obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= $systolic_bp
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Query stored successfully |
| 400 | Invalid query or unknown type |

---

### Store Query at Version

**Endpoint:** `PUT /definition/query/{qualified_query_name}/{version}`

**Description:** Store a query at a specific semantic version.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| qualified_query_name | string | Query identifier |
| version | string | SEMVER version number |

**Query Parameters:**

| Parameter | Type | Default |
|-----------|------|---------|
| query_type | string | "AQL" |

**Request Body:**

Content-Type: `text/plain`

Schema: AQL string

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Query stored successfully |
| 400 | Invalid query content |
| 409 | Query at version already exists |

---

### Get Stored Query at Version

**Endpoint:** `GET /definition/query/{qualified_query_name}/{version}`

**Description:** Retrieve a stored query definition and metadata at specific version.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| qualified_query_name | string | Query identifier |
| version | string | SEMVER version (exact or prefix pattern) |

**Response Code:** 200 OK

**Example Response:**

```json
{
  "name": "org.openehr::compositions",
  "type": "aql",
  "version": "1.0.1",
  "saved": "2017-07-16T19:20:30.450+01:00",
  "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id] CONTAINS COMPOSITION c[$compositionid] WHERE c/name/value = 'Vitals'"
}
```

**Response Codes:**

| Code | Description |
|------|-------------|
| 200 | Query retrieved successfully |
| 404 | Query or version not found |

---

## Resource Schemas

### Template List Schema

Array of template metadata objects.

**Properties:**

| Field | Type | Required |
|-------|------|----------|
| template_id | string | Yes |
| version | string | No |
| concept | string | Yes |
| archetype_id | string | Yes |
| created_timestamp | string (ISO 8601) | Yes |

**Example:**

```json
[
  {
    "template_id": "openEHR-EHR-COMPOSITION.t_vital_signs.v1.0.0",
    "version": "1.0.1",
    "concept": "Vital Signs",
    "archetype_id": "openEHR-EHR-COMPOSITION.encounter.v1",
    "created_timestamp": "2017-08-14T19:24:56.639Z"
  }
]
```

---

### Template Schema

Represents template definitions in multiple formats.

**Supported Formats:**

1. **OPERATIONAL_TEMPLATE** - AOM/ADL 1.4 XML format
2. **OPERATIONAL_TEMPLATE_V2** - AOM/ADL 2 format
3. **WebTemplate** - Simplified JSON-based format

#### WebTemplate Structure

**Properties:**

| Field | Type | Required |
|-------|------|----------|
| templateId | string | Yes |
| version | string | Yes |
| defaultLanguage | string | Yes |
| languages | array of strings | Yes |
| tree | object (Tree) | Yes |

**Tree Properties:**

| Field | Type |
|-------|------|
| id | string |
| name | string |
| localizedName | string |
| rmType | string |
| nodeId | string |
| min | integer |
| max | integer |
| localizedNames | object |
| localizedDescriptions | object |
| aqlPath | string |
| children | array |

**Example:**

```json
{
  "templateId": "Vital_Signs",
  "version": "1.0.0",
  "defaultLanguage": "en",
  "languages": ["en"],
  "tree": {
    "id": "Vital_Signs",
    "name": "Vital Signs",
    "localizedName": "Vital Signs",
    "rmType": "COMPOSITION",
    "nodeId": "openEHR-EHR-COMPOSITION.encounter.v1",
    "min": 1,
    "max": 1,
    "localizedNames": {
      "en": "Vital Signs"
    },
    "localizedDescriptions": {
      "en": "Generic vital signs composition"
    },
    "aqlPath": "",
    "children": []
  }
}
```

---

### Stored Query Schema

Represents a stored query definition.

**Properties:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| name | string (QueryName) | Yes | Format: `[{namespace}::]{query-name}` |
| type | string (QueryType) | Yes | Default: "AQL" |
| version | string (QueryVersion) | Yes | SEMVER format |
| saved | string (ISO 8601) | Yes | Timestamp |
| q | string (AQL) | Yes | Query text |

**Example:**

```json
{
  "name": "org.openehr::compositions",
  "type": "aql",
  "version": "1.0.1",
  "saved": "2017-07-16T19:20:30.450+01:00",
  "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id] CONTAINS COMPOSITION c[$compositionid] WHERE c/name/value = 'Vitals'"
}
```

---

## Amendment History

| Issue | Details | Implementer | Completed |
|-------|---------|-------------|-----------|
| Release-1.0.3 | | | |
| 5.1 | SPECITS-66: Migrate REST API specs to OpenAPI format | S Iancu | 19 Dec 2022 |
| Release-1.0.2 | | | |
| 4.2 | SPECITS-59: Specify mimeType used by adl2 template | S Iancu | 26 Mar 2021 |
| 4.1 | SPECITS-42: Fix TEMPLATE_ID value format | S Iancu | 21 Mar 2021 |
| 4.1 | SPECITS-41: Add double quotes to ETag/If-Match headers | S Iancu | 21 Mar 2021 |
| 4.0 | SPECITS-57: Update ADL1.4 template response examples | E Sundvall, S Iancu | 13 Mar 2021 |
| Release-1.0.1 | | | |
| 3.0 | SPECITS-32: Fix typos and minor documentary errors | Multiple | 1 Sep 2019 |
| 2.2 | SPECITS-24: Added changelog | J Smolka, S Iancu | 12 May 2019 |
| 2.1 | Update links to specifications website | S Iancu | 16 Dec 2018 |
| Release-1.0.0 | Initial release | | |

---

## Copyright and License

(c) 2003-2022 The openEHR Foundation

Licensed under Creative Commons Attribution-NoDerivs 3.0 Unported.
For details: https://creativecommons.org/licenses/by-nd/3.0/

**Support:**
- Issues: Problem Reports
- Web: https://specifications.openehr.org
- Forum: https://discourse.openehr.org
