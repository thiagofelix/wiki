# Definition API - openEHR REST Specifications

## Document Information

- **Status**: STABLE
- **License**: Creative Commons Attribution-NoDerivs 3.0 Unported
- **Copyright**: 2003-2022 The openEHR Foundation
- **Contact**: info@openehr.org
- **Specification Version**: Latest

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [ADL1.4 Template Management](#adl14-template-management)
4. [ADL2 Template Management](#adl2-template-management)
5. [Stored Query Management](#stored-query-management)
6. [Resource Schemas](#resource-schemas)

---

## Acknowledgements

### Editor
- **Sebastian Iancu**, Architect, Code24, Netherlands

### Key Contributors
The specification benefited from input including:
- Birger Haarbrandt (Peter L. Reichertz Institut, Germany)
- Bjorn Naess (DIPS, Norway)
- Erik Sundvall (Karolinska University Hospital, Sweden)
- Ian McNicoll MD (FreshEHR, UK)
- Pablo Pazos Gutierrez (CaboLabs, Uruguay)
- Thomas Beale (Ars Semantica UK, openEHR Foundation)

### Trademarks
- "openEHR" is a trademark of the openEHR Foundation
- "OpenAPI" is a trademark of The Linux Foundation

---

## Preface

### Purpose

This specification defines RESTful service endpoints, resources, and operations for the Definition openEHR API, including request/response details and interaction protocols.

### Related Documents

**Prerequisites:**
- Operational Template 2
- Archetype Query Language (AQL)

**Related Resources:**
- openEHR Architecture Overview
- Archetype Technology Overview
- openEHR Global Class Index
- XML-Schemas (XSD)
- JSON-Schemas and Simplified Data Template (SDT)
- openEHR Platform Abstract Service Model

### Status Notes

The specification is available as OpenAPI 3.0.3 format in YAML. Development versions are accessible at the official specifications website.

---

## ADL1.4 Template Management

### Overview

Management of AOM and ADL 1.4 Operational Templates (OPTs). These simplify openEHR implementations by consolidating template constraints, labels, and requirements into parseable files suitable for UI generation and data validation.

### Upload a Template

**Endpoint**: `POST /definition/template/adl1.4`

**Description**: Upload a new ADL 1.4 operational template (OPT).

#### Request Headers

| Parameter | Type | Required | Values |
|-----------|------|----------|--------|
| `Prefer` | string | No | `return=minimal` (default), `return=representation` |

#### Request Body

- **Content-Type**: `application/xml`
- **Schema**: OPERATIONAL_TEMPLATE (XML structure)

#### Response Codes

| Code | Description |
|------|-------------|
| `201 Created` | Template successfully uploaded. `template_id` returned in `Location` header. `ETag` header MAY contain unique identifier. |
| `400 Bad Request` | Invalid template content. |
| `409 Conflict` | Template with same `template_id` and version already exists. |

#### Request Example

```xml
<template xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns="http://schemas.openehr.org/v1">
    <language>
        <terminology_id>
            <value>ISO_639-1</value>
        </terminology_id>
        <code_string>en</code_string>
    </language>
    <description>
        <original_author id="Original Author">Not Specified</original_author>
        <lifecycle_state>Initial</lifecycle_state>
        <other_details id="MetaDataSet:Sample Set">
            Template metadata sample set
        </other_details>
    </description>
    <uid>
        <value>b4d7f203-b329-4e89-a58a-c605b19e94de</value>
    </uid>
    <template_id>
        <value>Vital Signs</value>
    </template_id>
    <concept>Vital Signs</concept>
    <definition>
        <rm_type_name>COMPOSITION</rm_type_name>
        <occurrences>
            <lower_included>true</lower_included>
            <upper_included>true</upper_included>
            <lower>1</lower>
            <upper>1</upper>
        </occurrences>
        <node_id>at0000</node_id>
    </definition>
</template>
```

---

### List Templates

**Endpoint**: `GET /definition/template/adl1.4`

**Description**: List available ADL 1.4 operational templates on the system.

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Template list successfully retrieved. |

#### Response Example

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

**Endpoint**: `GET /definition/template/adl1.4/{template_id}`

**Description**: Retrieves the ADL 1.4 operational template identified by `template_id`.

Supports both XML (canonical OPT format) via `Accept: application/xml` and JSON "web template" format via `Accept: application/openehr.wt+json`.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `template_id` | string | Yes | Template identifier (e.g., "Vital Signs") |

#### Request Headers

| Parameter | Type | Required | Values |
|-----------|------|----------|--------|
| `Accept` | string | Yes | `application/json`, `application/xml`, `text/plain`, `application/openehr.wt+json` |

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Template successfully retrieved. |
| `400 Bad Request` | Invalid `template_id` format. |
| `404 Not Found` | Template with specified `template_id` does not exist. |
| `406 Not Acceptable` | Service cannot produce response matching `Accept` header. |

#### Response Example (XML)

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
</template>
```

---

## ADL2 Template Management

### Overview

Management of AOM2 templates per AOM2 and ADL2 specifications. These represent the next generation of template definitions.

### Upload a Template

**Endpoint**: `POST /definition/template/adl2`

**Description**: Upload a new ADL2 operational template.

#### Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `version` | string | SEMVER version number (e.g., "1.0.1") |

#### Request Headers

| Parameter | Type | Values |
|-----------|------|--------|
| `Prefer` | string | `return=minimal` (default), `return=representation` |

#### Request Body

- **Content-Type**: `text/plain`
- **Schema**: OPERATIONAL_TEMPLATE_V2 (ADL2 format)

#### Response Codes

| Code | Description |
|------|-------------|
| `201 Created` | Template successfully uploaded. |
| `400 Bad Request` | Invalid template content. |
| `409 Conflict` | Template with same `template_id` and version exists. |

#### Request Example

```
operational_template (adl_version=2.0.6; rm_release=1.0.2; generated)
    openEHR-EHR-COMPOSITION.t_clinical_info_ds_sf.v1.0.0

specialize
    openEHR-EHR-COMPOSITION.discharge.v1

language
    original_language = <[ISO_639-1::en]>

description
    lifecycle_state = <"unmanaged">
    original_author = <
        ["name"] = <"Ian McNicoll">
        ["organisation"] = <"openEHR Foundation">
        ["email"] = <"ian.mcnicoll@openehr.org">
    >
```

---

### List Templates

**Endpoint**: `GET /definition/template/adl2`

**Description**: List available ADL2 operational templates on the system.

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Template list successfully retrieved. |

#### Response Example

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

### Get a Template

**Endpoint**: `GET /definition/template/adl2/{template_id}`

**Description**: Retrieves the latest version of the ADL2 operational template identified by `template_id`.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `template_id` | string | Yes | Template identifier (e.g., "Vital Signs") |

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Template successfully retrieved. |
| `400 Bad Request` | Invalid `template_id` format. |
| `404 Not Found` | Template with specified `template_id` does not exist. |

#### Response Example

```
operational_template (adl_version=2.0.6; rm_release=1.0.2; generated)
    openEHR-EHR-COMPOSITION.t_clinical_info_ds_sf.v1.0.0

specialize
    openEHR-EHR-COMPOSITION.discharge.v1
```

---

### Get a Template at Version

**Endpoint**: `GET /definition/template/adl2/{template_id}/{version}`

**Description**: Retrieves the ADL2 operational template at a specified version.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `template_id` | string | Yes | Template identifier |
| `version` | string | Yes | SEMVER version (e.g., "1.0", "1.7.1"). Supports partial patterns. |

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Template successfully retrieved. |
| `400 Bad Request` | Invalid `template_id` or `version` format. |
| `404 Not Found` | Template with specified `template_id` at given `version` does not exist. |

---

## Stored Query Management

### Overview

Management of stored (registered) queries in the system. Queries are identified by qualified name and version, executable via the query endpoint. Formally described in the `I_DEFINITION_QUERY` Abstract Service Model interface.

---

### List Stored Queries

**Endpoint**: `GET /definition/query/{qualified_query_name}`

**Description**: Retrieves list of all stored queries matching `qualified_query_name` pattern.

Format: `[{namespace}::]{query-name}`. Empty pattern treated as wildcard.

#### Examples

- `GET /v1/definition/query/org.openehr` -- Lists all queries starting with "org.openehr"
- `GET /v1/definition/query/org.openehr::compositions` -- Lists all versions of named query

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `qualified_query_name` | string | Yes | Query name pattern (e.g., "org.openehr::compositions") |

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Query resources successfully retrieved. |

#### Response Example

```json
[
  {
    "name": "org.openehr::compositions",
    "type": "aql",
    "version": "1.0.1",
    "saved": "2017-07-16T19:20:30.450+01:00",
    "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id]\nCONTAINS COMPOSITION c[$compositionid]\nWHERE c/name/value = 'Vitals'"
  },
  {
    "name": "org.openehr::compositions",
    "type": "aql",
    "version": "1.1.7",
    "saved": "2018-06-13T09:37:20.530+01:00",
    "q": "SELECT c FROM EHR e[ehr_id/value=$ehr_id]\nCONTAINS COMPOSITION c[$uid]\nWHERE c/name/value = 'Vitals'"
  }
]
```

---

### Store a Query

**Endpoint**: `PUT /definition/query/{qualified_query_name}`

**Description**: Stores a new query or updates an existing query on the system.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `qualified_query_name` | string | Yes | Query name (e.g., "org.openehr::compositions") |

#### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query_type` | string | "AQL" | Query language/type indicator |

#### Request Body

- **Content-Type**: `text/plain`
- **Content**: AQL query string

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Query successfully stored. |
| `400 Bad Request` | Unable to store query (parsing error, unknown type, etc.). |

#### Request Example

```
SELECT c FROM
  EHR e
    CONTAINS COMPOSITION c[openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION obs[openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
  obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= $systolic_bp
```

---

### Store a Query Version

**Endpoint**: `PUT /definition/query/{qualified_query_name}/{version}`

**Description**: Stores a query at a specified SEMVER version on the system.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `qualified_query_name` | string | Yes | Query name |
| `version` | string | Yes | SEMVER version (e.g., "1.0", "1.7.1"). Supports patterns. |

#### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query_type` | string | "AQL" | Query language/type indicator |

#### Request Body

- **Content-Type**: `text/plain`
- **Content**: AQL query string

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Query successfully stored. |
| `400 Bad Request` | Unable to store query. |
| `409 Conflict` | Query with same name and version already exists. |

---

### Get Stored Query at Version

**Endpoint**: `GET /definition/query/{qualified_query_name}/{version}`

**Description**: Retrieves the definition and metadata of a stored query at specified version.

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `qualified_query_name` | string | Yes | Query name |
| `version` | string | Yes | SEMVER version (e.g., "1.0", "1.7.1"). Supports patterns. |

#### Response Codes

| Code | Description |
|------|-------------|
| `200 OK` | Stored AQL successfully retrieved. |
| `404 Not Found` | Stored query with name and version does not exist. |

#### Response Example

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

## Resource Schemas

### Template List Schema

Array of template metadata objects.

#### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `template_id` | string | Yes | Template identifier |
| `version` | string | No | SEMVER version number |
| `concept` | string | Yes | Template concept name |
| `archetype_id` | string | Yes | Root archetype identifier |
| `created_timestamp` | string (date-time) | Yes | Creation timestamp |

#### Example

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

Templates available in three formats:

#### ADL1.4 Format

- **Schema**: OPERATIONAL_TEMPLATE (XML structure)
- **Format**: XML as per Archetype Model specifications

#### ADL2 Format

- **Schema**: OPERATIONAL_TEMPLATE_V2
- **Format**: ADL2 text-based format

#### Web Template Format

Alternative simplified JSON representation.

#### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `templateId` | string | Yes | Template identifier |
| `version` | string | Yes | Version number |
| `defaultLanguage` | string | Yes | ISO 639-1 language code |
| `languages` | array[string] | Yes | Supported language codes |
| `tree` | object | Yes | Template tree structure |

#### Tree Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Node identifier |
| `name` | string | Human-readable name |
| `localizedName` | string | Localized name |
| `rmType` | string | RM type name |
| `nodeId` | string | Archetype node identifier |
| `min` | integer | Minimum cardinality |
| `max` | integer | Maximum cardinality (-1 for unbounded) |
| `localizedNames` | object | Localized names by language |
| `localizedDescriptions` | object | Localized descriptions by language |
| `aqlPath` | string | AQL path expression |
| `children` | array[object] | Child nodes |
| `annotations` | object | Additional annotations |
| `inputs` | array[object] | Input specifications |
| `inContext` | boolean | Whether in context |

#### Web Template Example

```json
{
  "templateId": "openEHR-EHR-COMPOSITION.encounter.v1",
  "version": "1.0.0",
  "defaultLanguage": "en",
  "languages": ["en"],
  "tree": {
    "id": "encounter",
    "name": "Encounter",
    "localizedName": "Encounter",
    "rmType": "COMPOSITION",
    "nodeId": "openEHR-EHR-COMPOSITION.encounter.v1",
    "min": 1,
    "max": 1,
    "localizedNames": {
      "en": "Encounter"
    },
    "localizedDescriptions": {
      "en": "Generic encounter"
    },
    "aqlPath": "/",
    "children": [
      {
        "id": "context",
        "rmType": "EVENT_CONTEXT",
        "nodeId": "",
        "min": 1,
        "max": 1,
        "aqlPath": "/context",
        "children": []
      }
    ]
  }
}
```

---

### Stored Query Schema

Definition and metadata of a registered query.

#### Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string (QueryName) | Yes | Fully qualified name: `[{namespace}::]{query-name}` |
| `type` | string (QueryType) | Yes | Query language type (default: "AQL") |
| `version` | string (QueryVersion) | Yes | SEMVER version number |
| `saved` | string (date-time) | Yes | Storage timestamp |
| `q` | string (AQL) | Yes | AQL query string |

#### Example

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

## Amendment Record

| Issue | Details | Raiser/Implementer | Completed |
|-------|---------|-------------------|-----------|
| **Release 1.0.3** | | | |
| 5.1 | SPECITS-66: Migrate REST API specs to OpenAPI format | S Iancu | 19 Dec 2022 |
| **Release 1.0.2** | | | |
| 4.2 | SPECITS-59: Specify mimeType used by adl2 template | S Iancu | 26 Mar 2021 |
| 4.1 | SPECITS-42: Fix TEMPLATE_ID value format in examples | S Iancu | 21 Mar 2021 |
| 4.1 | SPECITS-41: Add double quotes to ETag and If-Match headers | S Iancu | 21 Mar 2021 |
| 4.0 | SPECITS-57: Update GET adl1.4 template request/response examples | E Sundvall, S Iancu | 13 Mar 2021 |
| **Release 1.0.1** | | | |
| 3.0 | SPECITS-32: Fix typos and minor documentary errors | J Smolka, P Pazos, E Sundvall, T Beale, S Iancu | 1 Sep 2019 |
| 2.2 | SPECITS-24: Added changelog | J Smolka, S Iancu | 12 May 2019 |
| 2.1 | Update links to new openEHR specifications website | S Iancu | 16 Dec 2018 |
| **Release 1.0.0** | Initial release | | |

---

## Related Resources

- **OpenAPI Specification Files**: Available for validation and code generation
- **Implementation Forum**: discourse.openehr.org
- **Issue Tracking**: openehr.atlassian.net
- **Official Website**: specifications.openehr.org

---

**Source:** https://specifications.openehr.org/releases/ITS-REST/latest/definition.html
