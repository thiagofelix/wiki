# openEHR REST APIs Overview Specification

**Status:** STABLE
**Version:** latest (Release-1.0.3)
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Document Information](#document-information)
2. [Introduction](#introduction)
3. [Glossary and Conventions](#glossary-and-conventions)
4. [Requests and Responses](#requests-and-responses)
5. [Resources](#resources)
6. [Endpoints](#endpoints)

---

## Document Information

### Copyright and License

(c) 2003 - 2021 The openEHR Foundation

The [openEHR Foundation](https://www.openehr.org) is an independent, non-profit foundation facilitating shared health records through open specifications and clinical models.

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported - [https://creativecommons.org/licenses/by-nd/3.0/](https://creativecommons.org/licenses/by-nd/3.0/)

### Support Resources

- **Issues:** [Problem Reports](https://specifications.openehr.org/components/ITS/open_issues)
- **Web:** [specifications.openEHR.org](https://specifications.openehr.org)
- **Forum:** [Implementation Technology Specifications](https://discourse.openehr.org/c/specifications/its/41)
- **Tracker:** [Specifications Problem Reports](https://openehr.atlassian.net/browse/SPECPR)

### Editor

Sebastian Iancu, Architect, Code24, Netherlands

### Contributors

- Birger Haarbrandt, Peter L. Reichertz Institut for Medical Informatics, Germany
- Bjorn Naess, DIPS, Norway
- Bostjan Lah, Senior Architect, Better, Slovenia
- Erik Sundvall, Karolinska University Hospital, Sweden
- Heath Frankel, Ocean Informatics, Australia
- Ian McNicoll MD, FreshEHR, UK
- Jake Smolka, Software Engineer, Better, Slovenia
- Matija Polajnar, PhD, Better, Slovenia
- Pablo Pazos Gutierrez, CaboLabs, Uruguay
- Rong Chen MD, PhD, Cambio Healthcare Systems, Sweden
- Seref Arikan, Centre for Health Informatics and Multi-professional Education, UK
- Thomas Beale, Ars Semantica, openEHR Foundation Management Board

---

## Introduction

### Purpose

This specification defines service endpoints, resources, and operations for interacting with an openEHR API using RESTful principles, including request/response formats and HTTP protocol requirements.

### Related Documents

**Prerequisites:**
- [openEHR Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html)

**Related Resources:**
- [openEHR Global Class Index](https://specifications.openehr.org/classes)
- [XML-Schemas (XSD)](https://specifications.openehr.org/releases/ITS-XML/latest)
- [JSON-Schemas](https://specifications.openehr.org/releases/ITS-JSON/latest)
- [Simplified Data Template (SDT)](simplified_data_template.html)
- [openEHR Platform Abstract Service Model](https://specifications.openehr.org/releases/SM/latest/openehr_platform.html)

### Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| **Release-1.0.3** | | | |
| 4.1 | SPECITS-66: Migrate REST API specs to OpenAPI Specification | S Iancu | 19 Dec 2022 |
| **Release-1.0.2** | | | |
| 3.4 | SPECITS-59: Specify mimeType used by adl2 template | S Iancu | 26 Mar 2021 |
| 3.3 | SPECITS-41: Add double quotes to ETag and If-Match headers | S Iancu | 21 Mar 2021 |
| 3.2 | SPECITS-56: Fix typos, formatting and minor documentary errors | S Iancu | 15 Mar 2021 |
| 3.2 | SPECITS-45: Describe datetime format for REST API | P Pazos, S Iancu | 15 Mar 2021 |
| 3.1 | SPECITS-57: Update info about simplified JSON formats | E Sundvall, S Iancu | 13 Mar 2021 |
| 3.0 | SPECITS-49: Resource Identification clarification | J Smolka, M Polajnar, S Iancu | 08 Mar 2021 |
| **Release-1.0.1** | | | |
| 2.4 | SPECITS-33: Add SDT format specification reference | I McNicoll, T Beale, S Iancu | 17 Oct 2019 |
| 2.3 | SPECITS-32: Fix typos and minor errors | J Smolka, P Pazos, T Beale, S Iancu | 19 Jul 2019 |
| 2.2 | SPECITS-24: Added changelog | J Smolka, S Iancu | 12 May 2019 |
| 2.2 | SPECITS-25, SPECITS-29: Change layout and structure | J Smolka, S Iancu | 12 May 2019 |
| 2.1 | Update links to new specifications website | S Iancu | 16 Dec 2018 |
| **Release-1.0.0** | | | |

---

## Glossary and Conventions

### Key Terminology

| Term | Definition |
|------|-----------|
| **API** | Application Programmer Interface |
| **REST** | [Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer) - Web service allowing client access to textual resource representations |
| **OAS** | [OpenAPI Specification](https://spec.openapis.org/oas/v3.0.3) |
| **AQL** | [Archetype Query Language](https://specifications.openehr.org/releases/QUERY/latest/AQL.html) |
| **RM** | [Reference Model](https://specifications.openehr.org/releases/RM/latest) |
| **SEMVER** | [Semantic Versioning 2.0.0](https://semver.org/) |
| **UUID** | Universally unique identifier ([RFC 4122](https://tools.ietf.org/html/rfc4122)) - e.g., `8849182c-82ad-4088-a07f-48ead4180515` |
| **ehr_id** | EHR identifier (HIER_OBJECT_ID form, usually UUID/GUID) - e.g., `7d44b88c-4199-4bad-97dc-d78268e01398` |
| **versioned_object_uid** | VERSIONED_OBJECT unique identifier (HIER_OBJECT_ID) - e.g., `8849182c-82ad-4088-a07f-48ead4180515` |
| **version_uid** | VERSION unique identifier (OBJECT_VERSION_ID) - e.g., `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2` |
| **uid_based_id** | Abstract identifier: either a version_uid or versioned_object_uid |
| **preceding_version_uid** | Previous VERSION identifier for PUT/DELETE operations - e.g., `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1` |
| **version_at_time** | Time specifier for VERSION retrieval in extended ISO 8601 format - e.g., `2015-01-20T19:30:22.765+01:00` |

### OpenAPI Specification Files

The specification is available as [OpenAPI Specification 3.0](https://spec.openapis.org/oas/v3.0.3) YAML files with two variants:

- **Codegen Variant:** Optimized for code generation tools ([OpenAPI Generator](https://github.com/openapitools/openapi-generator), [Swagger Codegen](https://github.com/swagger-api/swagger-codegen))
- **Validation Variant:** Optimized for data validation in servers and applications

Key differences:
- Codegen uses inheritance with `allOf` and discriminators
- Validation uses flattened schemas and `oneOf` for union-types

**Download:** [openEHR/specifications-ITS-REST/computable/OAS](https://github.com/openEHR/specifications-ITS-REST/tree/master/computable/OAS)

---

## Requests and Responses

### HTTP Methods

HTTP methods are defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-4) and [IANA HTTP Method Registry](https://www.iana.org/assignments/http-methods/http-methods.xhtml).

| Method | Description |
|--------|-------------|
| **GET** | Transfer current representation of target resource |
| **HEAD** | Check resource existence, return status without content |
| **POST** | Perform resource-specific processing on request payload |
| **PUT** | Replace all current target resource representations with request payload |
| **DELETE** | Remove all current target resource representations |
| **OPTIONS** | Describe communication options for target resource |

### Authentication and Authorization

Services SHOULD implement HTTP Authentication and Authorization frameworks but no specific scheme is mandated. See [RFC 7235](https://tools.ietf.org/html/rfc7235) and [Mozilla HTTP Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).

**Requirements:**
- Services MUST use `WWW-Authenticate` and/or `Proxy-Authenticate` headers appropriately
- Services MUST return `403 Forbidden`, `401 Unauthorized`, or `407 Proxy Authentication` when applicable
- Clients MUST use `Authorization` and `Proxy-Authorization` headers

### HTTP Headers

#### openEHR-VERSION and openEHR-AUDIT_DETAILS

For committing change-controlled resources (COMPOSITION, EHR_STATUS, FOLDER, etc.), services perform internal versioning using [CONTRIBUTION](https://specifications.openehr.org/releases/RM/latest/common.html#_contributions) and [VERSION](https://specifications.openehr.org/releases/RM/latest/common.html#_version_class) objects. Services MUST accept custom headers for client-provided committal metadata.

**Example:**

```http
openEHR-VERSION.lifecycle_state: code_string="532"
openEHR-AUDIT_DETAILS.change_type: code_string="251"
openEHR-AUDIT_DETAILS.description: value="Updated composition description"
openEHR-AUDIT_DETAILS.committer: name="John Doe", external_ref.id="BC8132EA-8F4A-11E7-BB31-BE2E44B06B34", external_ref.namespace="demographic", external_ref.type="PERSON"
```

None of these headers are mandatory. Provided values MUST merge with default VERSION and audit_details attributes at commit runtime.

**Lifecycle State Codes:**

| Code | Meaning |
|------|---------|
| 532 | complete |
| 553 | incomplete |
| 523 | deleted |

**Change Type Codes:**

| Code | Meaning |
|------|---------|
| 249 | creation |
| 250 | amendment |
| 251 | modification |
| 252 | synthesis |
| 523 | deleted |
| 666 | attestation |
| 253 | unknown |

#### If-Match and Accidental Overwrites

The `If-Match` header SHOULD prevent accidental overwrites when multiple agents act on the same resource. If a condition evaluates to false, services MUST respond with HTTP `412 Precondition Failed` and SHOULD return the latest `version_uid` in `Location` and `ETag` headers.

**Example:**

```http
If-Match: "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2"
```

See [RFC 7232](https://tools.ietf.org/html/rfc7232#section-3.1) for details.

#### openEHR-TEMPLATE_ID

MUST be used when committing COMPOSITIONs via `PUT` or `POST` using simplified data formats that don't include `LOCATABLE.archetype_details.template_id`.

#### Location and openEHR-uri

Per [RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.2), the `Location` header indicates resource location. Services MUST return this header after create/update operations; it MAY be returned for other operations.

**Example:**

```
Location: https://openEHRSys.example.com/v1/ehr/347a5490-55ee-4da9-b91a-9bba710f730e/composition/8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2
```

Services supporting DV_URI/DV_EHR_URI generation MAY send `openEHR-uri` header:

```
openEHR-uri: ehr:/347a5490-55ee-4da9-b91a-9bba710f730e/compositions/87284370-2D4B-4e3d-A3F3-F303D2F4F34B
```

#### Prefer

The `Prefer` header MAY be used for resource representation negotiation (see [RFC 7240](https://tools.ietf.org/html/rfc7240#section-4.2)).

#### ETag and Last-Modified

Per [RFC 7232](https://tools.ietf.org/html/rfc7232#section-2.3), the `ETag` header provides an opaque validator differentiating resource representations. The value changes when resources change.

**Example ETag:**

```
ETag: "8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::2"
```

The `Last-Modified` header contains resource modification datetime from `VERSION.commit_audit.time_committed.value`.

**Example Last-Modified:**

```
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
```

These headers SHOULD be present in responses targeting VERSION, VERSIONED_OBJECT, or similar resources with unique identifiers.

### HTTP Status Codes

HTTP status codes are defined in [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6) and the [IANA Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml).

| Code | Reason-Phrase | Meaning and Use Case |
|------|---------------|----------------------|
| **200** | OK | Request succeeded; payload depends on request method |
| **201** | Created | Request fulfilled; one or more new resources created |
| **204** | No Content | Request fulfilled; no additional content in response body |
| **400** | Bad Request | Service cannot process request due to client error (malformed syntax, invalid content) |
| **401** | Unauthorized | Request lacks valid authentication credentials for target resource |
| **403** | Forbidden | Service understood request but refuses authorization |
| **404** | Not Found | Origin service did not find target resource or unwilling to disclose existence |
| **405** | Method Not Allowed | Method known but not supported by target resource |
| **406** | Not Acceptable | Target resource has no acceptable current representation |
| **408** | Request Timeout | Request maximum execution time reached |
| **409** | Conflict | Request could not process; might generate duplicate or conflict |
| **412** | Precondition Failed | Condition in request header evaluated to false on server |
| **415** | Unsupported Media Type | Service refusing request; payload format not supported |
| **422** | Unprocessable Entity | Request well-formed but unable to follow due to semantic errors |
| **500** | Internal Server Error | Service encountered unexpected condition preventing fulfillment |
| **501** | Not Implemented | Service does not support functionality required to fulfill request |

Code `400` indicates generic client-side error when no other `4xx` code applies. Clients SHOULD NOT repeat requests without modifications.

**Error Response Example:**

Services MAY return detailed error information when `Prefer: return=representation` header is present:

```json
{
  "message": "Error message",
  "code": 90000,
  "errors": [
    {
      "_type": "DV_CODED_TEXT",
      "value": "Error message",
      "defining_code": {
        "terminology_id": {
          "value": "local"
        },
        "code_string": "9000"
      }
    },
    {
      "_type": "DV_CODED_TEXT",
      "value": "Secondary error message",
      "defining_code": {
        "terminology_id": {
          "value": "local"
        },
        "code_string": "8000"
      }
    }
  ]
}
```

### Representation Details Negotiation

Services SHOULD allow clients to choose response representation via `POST` and `PUT` methods.

#### Minimal Response

Client sends: `Prefer: return=minimal`

Expected behavior:
- Only minimal response content returned on success
- `Location` header indicating direct resource URL MUST be present
- If no payload content, service SHOULD use HTTP `204 No Content`

#### Full Representation Response

Client sends: `Prefer: return=representation`

Expected behavior:
- Full representation returned on success
- `Location` header MAY be present
- Payload SHOULD include complete representation

**Default:** If no `Prefer` header present, default policy is `return=minimal`

#### Resolving OBJECT_REF

Client MAY indicate preference for full/partial resource representations instead of OBJECT_REF identifiers:

```
Prefer: return=representation, resolve_refs
```

Services with this capability SHOULD honor this header.

---

## Resources

A Resource is an instance of a specific openEHR class addressable by the service. Examples include:

- Top-level content structures: COMPOSITION, EHR_STATUS, FOLDER, PARTY
- Version containers: VERSIONED_COMPOSITION, VERSIONED_EHR_STATUS
- Non-versioned resources: EHR, CONTRIBUTION, RESULT_SET
- Definitions: TEMPLATE, ARCHETYPE, QUERY

openEHR types are always capitalized in this specification. Refer to the [class index](https://specifications.openehr.org/classes) for complete type definitions.

### Resource Identification

RESTful services address resources via URIs using HTTP verbs. Each resource has a unique system identifier that never changes after persistence.

#### Identifier Types

- **versioned_object_uid:** Identifies VERSIONED_OBJECT (version container); stored in VERSIONED_OBJECT.uid.value (HIER_OBJECT_ID format)
- **version_uid:** Identifies VERSION within container; stored in VERSION.uid.value (OBJECT_VERSION_ID format)
- **ehr_id:** Identifies EHR
- **template_id:** Identifies Template definition
- **qualified_query_name:** Identifies Query definition

The `version_uid` format is: `object_id::creating_system_id::version_tree_id`, where `object_id` matches the containing VERSIONED_OBJECT identifier.

#### Example URIs

```
GET https://openEHRSys.example.com/v1/ehr/7d44b88c-4199-4bad-97dc-d78268e01398/composition/8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1
```

This uses:
- EHR identifier: `7d44b88c-4199-4bad-97dc-d78268e01398` (from EHR.ehr_id.value)
- COMPOSITION identifier: `8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::1` (from VERSION.uid.value)

#### Dual Identification

A COMPOSITION can be identified by two different approaches:

**Explicit (using version_uid):**

```
https://openEHRSys.example.com/v1/ehr/7d44b88c-4199-4bad-97dc-d78268e01398/composition/8849182c-82ad-4088-a07f-48ead4180515::openEHRSys.example.com::5
```

**Implicit (using versioned_object_uid):**

```
https://openEHRSys.example.com/v1/ehr/7d44b88c-4199-4bad-97dc-d78268e01398/composition/8849182c-82ad-4088-a07f-48ead4180515
```

The implicit form references the same resource only while the latest version remains version 5.

**Note:** Since [RM Release 1.0.4](https://specifications.openehr.org/releases/RM/Release-1.0.4), populating the inherited `uid` attribute in COMPOSITIONs is strongly recommended, copying the UID from the enclosing VERSION object's `uid` field. See [Architecture Overview - Levels of Identification](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html#_levels_of_identification) for details.

### Data Representation

Services MUST support at least one of XML or JSON formats. Alternative formats such as Simplified Data Template (SDT) MAY also be supported.

#### XML Format

When resources are serialized as XML, payloads MUST be valid against [published XSDs](https://specifications.openehr.org/releases/ITS-XML/latest).

- **Request:** Use `Content-Type: application/xml` header
- **Error Response:** HTTP `415 Unsupported Media Type` if format unsupported
- **Preference:** Use `Accept: application/xml` header
- **Error Response:** HTTP `406 Not Acceptable` if format unsupported
- **Response Header:** `Content-Type: application/xml` (except HTTP `204` No Content)

#### JSON Format

When resources are serialized as JSON, payloads SHOULD be valid against [published JSON-Schemas](https://specifications.openehr.org/releases/ITS-JSON/latest).

**Naming Convention:**
- Attribute names must be lowercase snake_case as specified in equivalent RM type

**Example:**

```json
{
  "category": {
    "value": "event",
    "defining_code": {
      "terminology_id": {
        "value": "openehr"
      },
      "code_string": "433"
    }
  }
}
```

**Metadata Attributes:**
- Metadata attributes (not RM attributes) are prefixed with underscore `_`
- Example: `_type` attribute specifies RM type when polymorphism involved or RM type is abstract
- Value MUST be uppercase class name from RM specification

**Example with Polymorphism:**

```json
{
  "_type": "DV_TEXT",
  "value": "Hello world!"
}
```

**Null and Empty Values:**
- RM attributes that are null, empty list, or empty array SHOULD be absent in JSON serialization
- Attribute order MAY follow RM specification order but is not mandatory

**Request/Response Headers:**
- **Request:** Use `Content-Type: application/json` header
- **Error Response:** HTTP `415 Unsupported Media Type` if format unsupported
- **Preference:** Use `Accept: application/json` header
- **Error Response:** HTTP `406 Not Acceptable` if format unsupported
- **Response Header:** `Content-Type: application/json` (except HTTP `204` No Content)

#### Alternative Data Formats

Creating canonical XML/JSON instances can be complex for developers with limited openEHR experience. Alternative formats are documented at [Simplified Data Template (SDT)](simplified_data_template.html).

**Supported Content Types:**

| Format | Content-Type | Description |
|--------|-------------|-------------|
| **Flat IM-SDT JSON** | `application/openehr.wt.flat+json` | Simplified flat JSON (web template format) |
| **Structured IM-SDT JSON** | `application/openehr.wt.structured+json` | Structured JSON (web template format) |
| **Text** | `text/plain` | Textual ADL2 templates or AQL queries |
| **Near-Canonical RM-SDT JSON** | `application/openehr.nc.flat+json` | ECISFLAT format |
| **TDS/TDD Simplification XML** | `application/openehr.tds2+xml` | Template Data Schema XML |

**References:**
- [Better web-template implementation](https://www.ehrscape.com/reference.html)
- [Better examples](https://www.ehrscape.com/examples.html)
- [Better open-source implementation](https://github.com/better-care/web-template)
- [Better conformance tests](https://github.com/better-care/web-template-tests)
- [EHRbase documentation](https://ehrbase.readthedocs.io/en/latest/02_getting_started/05_load_data/index.html#flat-format)
- [ECISFLAT format](https://github.com/ethercis/ethercis/blob/master/doc/flat%20json.md)
- [TDD2canonical project](https://github.com/openEHR/openEHR-TDD2canonical)

**Request/Response Negotiation:**
- **Request:** Use `Content-Type` header to specify simplified format
- **Error Response:** HTTP `415 Unsupported Media Type` if format unsupported
- **Preference:** Use `Accept` header to specify expected format
- **Error Response:** HTTP `406 Not Acceptable` if format unsupported
- **Response Header:** `Content-Type` MUST be present (except HTTP `204` No Content)

#### Datetime Format

Date, time, and datetime types MUST comply with [ISO 8601 Date and Time](https://en.wikipedia.org/wiki/ISO_8601) specification. openEHR semantics are defined in the [base.foundation_types.time package](https://specifications.openehr.org/releases/BASE/latest/foundation_types.html#_time_types).

**Recommendations:**
- Use extended ISO 8601 format for human readability
- Reduces special parsing/formatting needs

**Format:**
- General datetime form: `YYYY-MM-DDThh:mm:ss.sss[Z|+/-hh:mm]`
- Example: `2016-06-23T13:42:16.117+02:00`
- Timezone SHOULD only be supplied when needed; local timezone assumed otherwise

**HTTP Query Parameters and Path Segments:**
- MUST always use extended ISO 8601 format

**Message Body Values:**
- Date/datetime/time values creating/updating resources will be preserved as sent
- Retrieval/querying should return values in original backend format (no conversion)

---

## Endpoints

### OPTIONS: System Options and Conformance

The `OPTIONS` HTTP method allows clients to determine resource, service, or system options/requirements without implying resource action. Services SHOULD respond with appropriate HTTP codes, headers, and potentially a payload revealing system details.

Use case: Exposing service capabilities for a conformance manifest.

**Request:**

```http
OPTIONS https://openEHRSys.example.com/v1/
```

**Response: 200 OK**

Server returns conformance and capability information.

**Response Example:**

```json
{
  "solution": "openEHRSys",
  "solution_version": "v0.9",
  "vendor": "My-openEHR",
  "restapi_specs_version": "v1.0.3",
  "conformance_profile": "STANDARD",
  "endpoints": [
    "/ehr",
    "/definition",
    "/query"
  ]
}
```

---

## Requirements Language

Key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted per [BCP 14](https://tools.ietf.org/html/bcp14) [[RFC 2119](https://tools.ietf.org/html/rfc2119)], [[RFC 8174](https://tools.ietf.org/html/rfc8174)] when appearing in all capitals.

---

## Conformance

Conformance requirements are marked as "TBD" in the current specification version.

---

## Related Specifications

- [openEHR Base Specifications](https://specifications.openehr.org/releases/BASE/latest)
- [openEHR Reference Model (RM)](https://specifications.openehr.org/releases/RM/latest)
- [openEHR Query Specifications (AQL)](https://specifications.openehr.org/releases/QUERY/latest/AQL.html)
