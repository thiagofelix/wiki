# openEHR Platform Service Model

**Issuer**: openEHR Specification Program
**Release**: SM development
**Status**: TRIAL
**Keywords**: openehr, service, API
**Copyright**: 2017 - 2024 The openEHR Foundation
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [Overview](#overview)
4. [Common Package](#common-package)
5. [Definition Package](#definition-package)
6. [EHR Service](#ehr-service)
7. [Demographic Service](#demographic-service)
8. [EHR Index Service](#ehr-index-service)
9. [Query Service](#query-service)
10. [Message Service](#message-service)
11. [Subject Proxy Service](#subject-proxy-service)
12. [Terminology Service](#terminology-service)
13. [Admin Service](#admin-service)

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica; openEHR Foundation Management Board

### Contributors

- Pablo Pazos Gutierrez, CaboLabs, Uruguay

### Trademarks

- 'openEHR' is a registered trademark of the openEHR Foundation

---

## Preface

### 1.1. Purpose

This specification defines core openEHR platform components in abstract form for development of concrete service APIs across various interface technologies including SOAP, REST, protocol buffers, and others.

**Intended audience**:
- Standards bodies in health informatics
- Solution vendors

### 1.2. Related Documents

**Prerequisite documents**:
- openEHR Architecture Overview

**Related documents**:
- openEHR REST APIs

### 1.3. Status

This specification is in TRIAL state. Development version available at specifications.openehr.org.

Sections marked "TBD" indicate areas to be determined.

### 1.4. Feedback

- Technical mailing list: discourse.openehr.org
- Problem reports: specifications.openehr.org Problem Report tracker
- Change requests: SM component Change Request tracker

### 1.5. Conformance

Conformance is determined through formal testing against openEHR Implementation Technology Specifications (ITSs), such as REST API interfaces or XML schemas.

---

## Overview

### 2.1. General Assumptions

This specification provides formal, abstract platform interface definitions independent of specific implementation technologies. The intent is to establish semantic clarity while allowing flexibility in concrete implementations.

Native APIs are network-accessible via multiple protocols:
- Text-based: SOAP/WSDL, REST
- Binary: Protocol Buffers, Apache Thrift, Kafka, ZeroC ICE, AMPQ

This specification focuses on the nominal native API accessed through these methods.

### 2.2. openEHR Platform Model

The abstract openEHR Platform consists of the following logical components and their interfaces:

| Service | Description |
|---------|-------------|
| Definitions | Upload and querying of archetypes, templates, and queries |
| EHR | Versioned persistence service for EHRs |
| Demographic | Versioned persistence service for demographic data |
| EHR Index | EHR id / demographic subject cross-reference service |
| Query | AQL query retrieval across services |
| Terminology | Access to terminology and value sets |
| Message | Message import/export supporting multiple formats and EHR Extracts |
| System Log | IHE ATNA-compliant system logging |
| Subject Proxy | Subject-focused data-sets providing temporal proxy pictures |
| Admin | Administrative facilities across all services |

### 2.3. Interface Calls

Logical interface calls follow standard computer science conventions as callable routines with formal, typed signatures. Following command/query separation principle, calls are either:

- **Queries**: Return data without changing state
- **Commands**: Change state without returning data

**Function signature forms**:
```
func: T                                    // function with no arguments
func(arg1: X, arg2: Y, arg3: Z): T        // function with arguments

proc                                       // procedure with no arguments
proc(arg1: X, arg2: Y)                    // procedure with arguments
```

### 2.4. Anatomy of an Abstract Call Specification

Call specifications include semantics stated through pre-conditions, post-conditions, exceptions, and documentation. Example structure:

**Call**: `create_ehr_with_id`

Creates a new EHR in the persistence service.

**Arguments**:
- `an_id: UUID` - EHR identifier

**Pre-conditions**:
- `Valid_id`: No EHR with this id currently exists

**Post-conditions**:
- `Ehr_created`: EHR with specified id has been created

**Exceptions**:
- `Ehr_already_exists` - EHR with id already exists
- `Auth_error` - Caller authorization failure

### 2.5. Global Conventions

#### 2.5.1. Functional Style

This specification uses a nearly stateless approach where error status is determined through explicit status check calls:

```
// Service interface pattern
interface I_EHR_SERVICE : I_STATUS {
    Boolean has_ehr(UUID an_ehr_id);
    UUID create_ehr();
    UUID create_ehr_with_id(UUID an_ehr_id);
}

// Typical call sequence
I_EHR_SERVICE i_ehr_service;
CALL_STATUS call_status;
UUID result;

try {
    result = i_ehr_service.create_ehr_with_id(an_ehr_id);
    if (i_ehr_service.last_call_error())
        call_status = i_ehr_service.last_call_status();
}
catch (PreConditionException e) {
    // handle precondition violations
}
```

Authentication and authorization are handled prior to call execution using standard technologies (OAuth, RFC 7235) and role-based access control.

#### 2.5.2. List Handling

Calls producing large container results use database cursor-style management:

- `item_offset`: Zero-based offset in query results to start returning items
- `items_to_fetch`: Number of items to return from offset (zero means "all")

#### 2.5.3. Global Naming Conventions

| Term | Description |
|------|-------------|
| `_ehr_id_` | EHR identifier value, typically UUID or GUID |
| `_versioned_object_uid_` | VERSIONED_OBJECT unique identifier |
| `_version_uid_` | VERSION unique identifier (e.g., `uuid::domain::version`) |
| `_preceding_version_uid_` | Previous VERSION unique identifier |
| `_object_id_` | Placeholder for versioned_object or version identifier |
| `_time_` | ISO 8601 formatted date-time |

### 2.6. Package Structure

The openEHR Platform Service Model consists of interconnected packages:

- `platform.common`: Common elements (status, versioning, audit)
- `platform.interface.definitions`: Definition artefacts
- `platform.interface.ehr`: EHR operations
- `platform.interface.demographic`: Demographic operations
- `platform.interface.ehr_index`: Index cross-references
- `platform.interface.query`: Query execution
- Additional specialized services (message, terminology, admin, subject proxy)

---

## Common Package

### 3.1. Overview

The `platform.common` package defines foundational elements:

- `I_STATUS` / `CALL_STATUS`: Call execution status representation
- `UPDATE_VERSION`: Version information structure for versioned stores
- `UPDATE_AUDIT`: Audit details for committal
- Service enumerations

### 3.2. Representing Call Status

Call status is represented using `CALL_STATUS` objects with:
- `code`: Value from `CALL_STATUS_TYPE` enumeration
- Informational fields for errors
- Service-specific codes via inheritance

### 3.3. Version Update Semantics

When calls create or update versioned objects (COMPOSITION, PARTY, etc.), the server-side implicitly:
1. Creates new `CONTRIBUTION`
2. Creates new `ORIGINAL_VERSION` objects
3. Creates new `VERSIONED_OBJECTS` for new items

The `UPDATE_VERSION<T>` structure supplies caller metadata while allowing server generation of:
- `_time_committed_`
- `_system_id_`

The `_preceding_version_uid_` must be specified except for first versions. The `_lifecycle_state_` must always be supplied using openEHR terminology values (e.g., `532|complete|`, `553|incomplete|`, `523|deleted|`).

Concrete types derived from `UPDATE_VERSION<T>` include:
- `UV_COMPOSITION` for COMPOSITION objects
- `UV_FOLDER` for FOLDER objects
- `UV_PARTY` for PARTY objects

### 3.4. Class Definitions

#### 3.4.1. I_STATUS Interface

**Description**: Interface to obtain status of previous calls; use by inheritance.

| Function | Return Type | Meaning |
|----------|-------------|---------|
| `last_call_failed()` | Boolean | Returns true if last call generated an error other than success |
| `last_call_status()` | CALL_STATUS | Returns status object for last call |

#### 3.4.2. CALL_STATUS Class

**Description**: Object representing call execution status.

| Attribute | Type | Meaning |
|-----------|------|---------|
| `code` | CALL_STATUS_TYPE | Call status code |
| `call_name` | String | Name of call documented |
| `call_string` | String | Full call in stringified form with arguments |
| `meaning` | String | Meaning of result status |
| `message` | String | Error message text |

#### 3.4.3. CALL_STATUS_TYPE Enumeration

| Value | Meaning |
|-------|---------|
| `success` | Call succeeded |
| `auth_failure` | Authorization failure |
| `precondition_violation` | Precondition violation occurred |
| `object_version_does_not_exist` | Referenced object version not found |
| `versioned_object_does_not_exist` | Versioned object not found |
| `exception` | Exception other than precondition violation |
| `ehr_id_does_not_exist` | EHR with provided id not found |
| `party_id_does_not_exist` | Party with provided id not found |
| `file_not_writable` | File system locator cannot be written |
| `version_mismatch` | Version mismatch error |

#### 3.4.4. UPDATE_VERSION Class

**Generic Type**: `UPDATE_VERSION<T>` (abstract)

**Description**: Represents an update to existing VERSION within VERSIONED_OBJECT, provided by client to platform. Server constructs full VERSION<T> from this plus server-generated data.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `preceding_version_uid` | OBJECT_VERSION_ID | 0..1 | Current version uid; required except for first version |
| `lifecycle_state` | Terminology_code | 1..1 | Lifecycle state using openEHR terminology |
| `attestations` | List<ATTESTATION> | 0..1 | Attestations relating to this version |
| `data` | T | 1..1 | Data item being provided in this version |
| `audit` | UPDATE_AUDIT | 1..1 | Audit details for this update |

#### 3.4.5. UPDATE_AUDIT Class

**Description**: Attributes required to document committal of information item to repository. Server uses this to create AUDIT_DETAILS object.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `change_type` | Terminology_code | 1..1 | Type of change from openEHR audit change type group |
| `description` | String | 0..1 | Reason for committal |
| `committer` | PARTY_PROXY | 1..1 | Identity of user who committed the item |

**Invariant**: `Change_type_valid` - change_type must be valid in openEHR terminology audit change type group

#### 3.4.6. I_VALIDITY_CHECKER Interface

**Description**: Utility functions for checking validity of definitions within data.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `definitions_valid()` | a_content: LOCATABLE | Boolean | Returns true if definition identifiers are known in definitions service |
| `content_valid()` | a_content: LOCATABLE | Boolean | Returns true if content structure is valid RM instance |

---

## Definition Package

### 4.1. Overview

The `platform.interface.definitions` package provides service interface to the definitions component, enabling storage and retrieval of:
- Archetypes
- Templates
- Queries
- Query sets

### 4.2. Archetypes and Templates

**ADL2 Support**: `I_DEFINITION_ADL2` interface enables upload, update, and removal of ADL 2-based archetypes and templates. All identified via ARCHETYPE_HRID and UUID. Supports:
- Source archetypes
- Operational Templates (OPTs)

**ADL 1.4 Support**: `I_DEFINITION_ADL14` interface manages older ADL 1.4 artifacts:
- Archetypes identified by ARCHETYPE_ID
- OPTs identified by UUID
- XML-based OPTs

### 4.3. Registered Queries

Queries stored in system for later execution. Identified by qualified names using schemes:
- `<namespace>::<query-name>`
- `<namespace>::<formalism>::<query-name>`

**Examples**:
- `"ehr::all_influenza_vacc_candidates"` - vaccination candidates query
- `"demographic::inpatients_rns"` - demographic query for hospital inpatients
- `"task_planning::aql::chemotherapy_plans"` - AQL query for chemotherapy plans

Default namespace is "misc" if not supplied.

#### 4.3.1. Query Formalism

Query text has associated formalism (query language) provided via `_a_type_` parameter, treated case-insensitively. Format:
- `"AQL"` or `"aql"` - language name only
- `"AQL::1"` - language with major version
- `"AQL::1.0.3"` - language with semver.org version

Default version is major "1" if not specified. These are equivalent:
- "AQL"
- "aql"
- "AQL::1"

### 4.4. Class Definitions

#### 4.4.1. I_DEFINITION_ADL2 Interface

**Description**: Interface to ADL2 definitions in an EHR system.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_artefact()` | an_id: ARCHETYPE_HRID | Boolean | Returns true if AOM2 artefact with id exists |
| `valid_artefact()` | an_artefact: AUTHORED_ARCHETYPE | Boolean | Tests validity of artefact |
| `upload_artefact()` | an_artefact: AUTHORED_ARCHETYPE | void | Uploads ADL2 artefact; replaces if exists; must be valid |
| `get_artefact()` | an_id: ARCHETYPE_HRID | AUTHORED_ARCHETYPE | Retrieves AOM2 artefact with id |
| `list_artefacts()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_HRID> | Lists all AOM2 artefacts |
| `list_archetypes()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_HRID> | Lists all archetypes |
| `list_templates()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_HRID> | Lists all templates |
| `list_opts()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_HRID> | Lists all OPTs |
| `list_matching_artefacts()` | id_pattern: String, item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_HRID> | Lists artefacts matching regex pattern |
| `delete_artefact()` | an_id: ARCHETYPE_HRID | void | Deletes AOM2 artefact with id |
| `artefacts_count()` | none | Integer | Returns total artefacts count |
| `archetypes_count()` | none | Integer | Returns total archetypes count |
| `templates_count()` | none | Integer | Returns total templates count |
| `opts_count()` | none | Integer | Returns total OPTs count |

**Pre-condition**: `valid_artefact(an_arch)` required for upload

**Post-condition**: `has_artefact(an_arch.identifier)` after successful upload

**Errors**:
- `invalid_artefact` with specific messages
- `artefact_does_not_exist`
- `invalid_id_pattern`

#### 4.4.2. I_DEFINITION_ADL14 Interface

**Description**: Interface to ADL 1.4 definitions (archetypes and OPTs) in an EHR system.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_archetype()` | an_id: ARCHETYPE_ID | Boolean | Returns true if ADL 1.4 archetype exists |
| `valid_archetype()` | an_arch: ARCHETYPE | Boolean | Tests validity of archetype |
| `upload_archetype()` | an_arch: ARCHETYPE | void | Uploads valid ADL 1.4 archetype; replaces if exists |
| `get_archetype()` | an_id: ARCHETYPE_ID | ARCHETYPE | Gets ADL 1.4 archetype |
| `list_archetypes()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_ID> | Lists all ADL 1.4 archetypes |
| `list_matching_archetypes()` | id_pattern: String, item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_ID> | Lists archetypes matching regex |
| `delete_archetype()` | an_id: ARCHETYPE_ID | void | Deletes archetype |
| `has_opt()` | an_opt_id: UUID | Boolean | Returns true if ADL 1.4 OPT exists |
| `valid_opt()` | an_opt: ARCHETYPE | Boolean | Tests validity of OPT |
| `upload_opt()` | an_opt: ARCHETYPE | void | Uploads ADL 1.4 OPT; must be valid |
| `get_opt()` | an_opt_id: UUID | ARCHETYPE | Gets ADL 1.4 OPT |
| `list_opts()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<UUID> | Lists all ADL 1.4 OPTs |
| `list_matching_opts()` | id_pattern: String, item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<ARCHETYPE_ID> | Lists OPTs matching regex |
| `delete_opt()` | an_id: UUID | void | Deletes ADL 1.4 OPT |
| `archetypes_count()` | none | Integer | Returns total archetypes count |
| `opts_count()` | none | Integer | Returns total OPTs count |

**Post-condition**: `has_archetype(an_arch.identifier)` after successful upload

**Errors**:
- `invalid_archetype`
- `invalid_template`
- `artefact_does_not_exist`
- `invalid_id_pattern`

#### 4.4.3. I_DEFINITION_QUERY Interface

**Description**: Interface for storing queries and query sets.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_query()` | a_query_name: String | Boolean | Returns true if query with qualified name is registered |
| `valid_query()` | a_query_text: String, a_type: String | Boolean | Returns true if query text is valid instance of formalism |
| `store_query()` | a_query_text: String, a_type: String, a_query_name: String (0..1) | QUERY_DESCRIPTOR | Registers query under qualified name or auto-generates; returns descriptor |
| `store_query_set()` | a_query_set_name: String (0..1) | UUID | Registers a query set |
| `list_queries()` | item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<QUERY_DESCRIPTOR> | Lists all registered queries |
| `list_matching_queries()` | id_pattern: String, artefact_id_pattern: String, item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<QUERY_DESCRIPTOR> | Lists queries matching identifier pattern and artefact pattern |
| `delete_query()` | a_query_name: String | void | Deletes query with name |
| `queries_count()` | none | Integer | Returns total queries count |

**Pre-condition**: `is_valid_query(a_query_text)` for store_query

**Pre-condition**: `has_query(a_query_name)` for delete_query

**Post-condition**: `has_query(a_query_name)` after store_query

**Errors**:
- `invalid_query`
- `invalid_id_pattern`

#### 4.4.4. DEFINITION_CALL_STATUS_TYPE Enumeration

| Value | Meaning |
|-------|---------|
| `invalid_archetype` | Invalid archetype provided |
| `invalid_template` | Invalid template provided |
| `invalid_artefact` | Invalid artefact provided |
| `invalid_query` | Invalid query provided |
| `invalid_id_pattern` | Invalid archetype identifier regex pattern |
| `artefact_does_not_exist` | Provided archetype identifier does not exist |
| `template_does_not_exist` | Provided template identifier does not exist |

#### 4.4.5. QUERY_DESCRIPTOR Class

**Description**: Describes a query in terms of unique identifier, current registered name, and registration time.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `qualified_query_name` | String | 1..1 | Unique qualified name following pattern `<namespace>::<query_name>` |
| `version` | String | 0..1 | Query semver.org version number |
| `registration_time` | Iso8601_date_time | 1..1 | Time query was registered in service |
| `formalism` | String | 1..1 | Query formalism: "aql" or other value |
| `source` | String | 0..1 | Source query text prior to parameter substitution |

---

## EHR Service

### 5.1. Overview

The `platform.interface.ehr` package defines service interface to the EHR persistence component. Primary functions:
- EHR creation and management
- EHR_STATUS operations
- Directory structure management
- Composition versioning
- Contribution tracking

### 5.2. Class Definitions

#### 5.2.1. I_EHR_SERVICE Interface

**Description**: Primary interface to EHR_SERVICE persistent repository.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_ehr()` | ehr_id: UUID | Boolean | Returns true if EHR with identifier exists |
| `has_ehr_for_subject()` | a_subject_id: PARTY_REF | Boolean | Returns true if EHR(s) exist for subject id |
| `create_ehr()` | an_ehr_status: EHR_STATUS (0..1) | UUID | Creates new EHR with system-generated id; returns id |
| `create_ehr_with_id()` | an_ehr_id: UUID, an_ehr_status: EHR_STATUS (0..1) | UUID | Creates new EHR with provided id; returns id as safety check |
| `create_ehr_for_subject()` | a_subject_id: PARTY_REF, an_ehr_status: EHR_STATUS (0..1) | UUID | Creates EHR with subject id; returns EHR id |
| `create_ehr_for_subject_with_id()` | an_ehr_id: UUID, a_subject_id: PARTY_REF, an_ehr_status: EHR_STATUS (0..1) | UUID | Creates EHR with both EHR id and subject id |
| `get_ehr()` | an_ehr_id: UUID | EHR_SUMMARY | Retrieves summarized EHR and EHR_STATUS |
| `get_ehrs_for_subject()` | a_subject_id: PARTY_REF | List<EHR_SUMMARY> | Retrieves EHRs with specified subject id |
| `i_ehr()` | ehr_id: UUID | I_EHR | Provides I_EHR interface instance for EHR parts access |

**Pre-conditions**:
- `no_subject`: an_ehr_status.subject = Void
- `no_duplicate`: not has_ehr(an_ehr_id)
- `has_ehr`: has_ehr(an_ehr_id)

**Post-conditions**:
- `has_ehr`: has_ehr(Result)
- Default EHR_STATUS created with is_modifiable=true, is_queryable=true
- Default subject containing PARTY_SELF generated

**Errors**:
- `ehr_create_fail_duplicate_id`
- `ehr_for_subject_already_exists`
- `ehr_id_does_not_exist`
- `subject_id_does_not_exist`

#### 5.2.2. I_EHR Interface

**Description**: Interface for single patient EHR-level operations.

| Attribute | Type | Meaning |
|-----------|------|---------|
| `ehr_status` | I_EHR_STATUS | Access to I_EHR_STATUS interface |
| `directory` | I_EHR_DIRECTORY | Access to I_EHR_DIRECTORY interface |
| `compositions` | I_EHR_COMPOSITION | Access to I_EHR_COMPOSITION interface |
| `contributions` | I_EHR_CONTRIBUTION | Access to I_EHR_CONTRIBUTION interface |

#### 5.2.3. I_EHR_STATUS Interface

**Description**: Interface to EHR_STATUS with implicit Contribution creation.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_ehr_status_version()` | an_ehr_id: UUID, a_version_uid: UUID | Boolean | True if version uid is one of EHR_STATUS versions |
| `get_ehr_status()` | an_ehr_id: UUID | EHR_STATUS | Gets current version of EHR_STATUS |
| `get_ehr_status_at_time()` | a_time: Iso8601_date_time (0..1) | EHR_STATUS | Gets EHR_STATUS version extant at time; if no time supplied, gets latest |
| `set_ehr_queryable()` | an_ehr_id: UUID | void | Sets is_queryable flag to true; ensures EHR included by query engine |
| `set_ehr_modifiable()` | an_ehr_id: UUID | void | Sets is_modifiable flag to true; ensures EHR treated as active and updatable |
| `clear_ehr_queryable()` | an_ehr_id: UUID | void | Clears is_queryable flag; ensures EHR ignored by query engine |
| `clear_ehr_modifiable()` | an_ehr_id: UUID | void | Clears is_modifiable flag; ensures EHR treated as inactive |
| `update_other_details()` | an_ehr_id: UUID, a_details: ITEM_TREE | void | Updates other_details part of EHR_STATUS |
| `get_ehr_status_at_version()` | an_ehr_id: UUID, a_version_uid: UUID | EHR_STATUS | Gets particular EHR_STATUS version |
| `get_versioned_ehr_status()` | an_ehr_id: UUID | VERSIONED_EHR_STATUS | Gets VERSIONED_EHR_STATUS object |

**Pre-conditions**: `has_ehr`: has_ehr(an_ehr_id)

**Post-conditions**:
- `is_queryable_set`: get_ehr_status(an_ehr_id).is_queryable
- `is_modifiable_set`: get_ehr_status(an_ehr_id).is_modifiable
- `is_queryable_cleared`: not get_ehr_status(an_ehr_id).is_queryable
- `is_modifiable_cleared`: not get_ehr_status(an_ehr_id).is_modifiable

**Errors**:
- `ehr_id_does_not_exist`

#### 5.2.4. I_EHR_DIRECTORY Interface

**Description**: Operations on EHR directory with implicit Contribution creation.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_directory()` | ehr_id: UUID | Boolean | True if EHR has directory structure |
| `has_path()` | ehr_id: UUID, a_path: String | Boolean | True if path exists in directory (slash-separated folder names) |
| `create_directory()` | ehr_id: UUID, a_dir_struct: UV_FOLDER | void | Creates directory from provided structure; creates VERSIONED_OBJECT, ORIGINAL_VERSION, CONTRIBUTION |
| `get_directory()` | ehr_id: UUID | FOLDER | Gets current directory version if exists |
| `get_directory_at_time()` | an_ehr_id: UUID, a_time: Iso8601_date_time (0..1) | FOLDER | Gets directory version extant at time; if no time supplied, gets latest |
| `update_directory()` | ehr_id: UUID, a_dir_struct: UV_FOLDER | void | Creates or updates directory from complete structure; creates ORIGINAL_VERSION and CONTRIBUTION |
| `delete_directory()` | ehr_id: UUID | void | Logically deletes directory by creating new version with removed contents |
| `has_directory_version()` | an_ehr_id: UUID, a_version_uid: UUID | Boolean | True if directory has version with specified id |
| `get_directory_at_version()` | an_ehr_id: UUID, a_version_uid: UUID | FOLDER | Gets particular directory version |
| `get_versioned_directory()` | an_ehr_id: UUID | VERSIONED_FOLDER | Gets VERSIONED_FOLDER object |

**Pre-conditions**:
- `has_ehr`: has_ehr(an_ehr_id)
- `definitions_valid`: definitions_valid(a_dir_struct)
- `no_directory`: not has_directory(ehr_id)
- `content_valid`: valid_content(a_dir_struct)
- `has_directory`: has_directory(ehr_id)

**Errors**:
- `ehr_id_does_not_exist`
- `definition_unknown`
- `content_invalid`
- `version_does_not_exist`

#### 5.2.5. I_EHR_COMPOSITION Interface

**Description**: Interface for commit and retrieve of Compositions with implicit Contribution creation.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_composition()` | an_ehr_id: UUID, a_version_uid: OBJECT_VERSION_ID | Boolean | Returns true if Composition version with identifier exists |
| `get_composition_latest()` | an_ehr_id: UUID, a_versioned_object_uid: UUID | COMPOSITION | Retrieves latest Composition version |
| `get_composition_at_time()` | an_ehr_id: UUID, a_versioned_object_uid: UUID, a_time: Iso8601_date_time (0..1) | COMPOSITION | Retrieves Composition version extant at given time; if no time supplied, gets latest |
| `get_composition_at_version()` | an_ehr_id: UUID, a_version_uid: OBJECT_VERSION_ID | COMPOSITION | Gets particular Composition version by id |
| `get_versioned_composition()` | an_ehr_id: UUID, a_versioned_object_uid: UUID | VERSIONED_COMPOSITION | Retrieves VERSIONED_COMPOSITION object |
| `create_composition()` | an_ehr_id: UUID, a_comp: UV_COMPOSITION | UUID | Creates first version of new Composition; creates VERSIONED_OBJECT, ORIGINAL_VERSION, CONTRIBUTION |
| `update_composition()` | an_ehr_id: UUID, a_comp: UV_COMPOSITION | UUID | Updates existing Composition; creates ORIGINAL_VERSION and CONTRIBUTION |
| `delete_composition()` | an_ehr_id: UUID, a_version_uid: UUID | void | Logically deletes Composition by creating new version with removed content and lifecycle state 523|deleted| |

**Pre-conditions**:
- `has_ehr`: has_ehr(an_ehr_id)
- `composition_definitions_valid`: definitions_valid(a_comp)
- `content_valid`: valid_content(a_comp)
- `has_composition`: has_composition(an_ehr_id, a_version_uid)

**Post-conditions**:
- `has_composition`: has_composition(an_ehr_id, Result)

**Errors**:
- `ehr_id_does_not_exist`
- `composition_already_exists`
- `composition_does_not_exist`
- `definition_unknown`
- `content_invalid`

#### 5.2.6. I_EHR_CONTRIBUTION Interface

**Description**: Interface for explicit Contribution-level operations.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_contribution()` | an_ehr_id: UUID, a_contrib_id: UUID | Boolean | Returns true if Contribution with id exists in EHR |
| `get_contribution()` | an_ehr_id: UUID, a_contrib_id: UUID | CONTRIBUTION | Returns Contribution with id from EHR |
| `commit_contribution()` | an_ehr_id: UUID, versions: List<UPDATE_VERSION>, an_audit: UPDATE_AUDIT | UUID | Commits CONTRIBUTION containing any number of UPDATE_VERSION objects |
| `list_contributions()` | an_ehr_id: UUID, time_range: Interval<Iso8601_date_time> (0..1), item_offset: Integer (0..1), items_to_fetch: Integer (0..1) | List<UUID> | Obtains list of Contribution identifiers in EHR |
| `contribution_count()` | ehr_id: UUID, time_range: Interval<Iso8601_date_time> (0..1) | Integer | Obtains count of Contributions in EHR |

**Pre-conditions**:
- `has_ehr`: has_ehr(an_ehr_id)
- `has_contribution`: has_contribution(a_contrib_id)

**Post-conditions**:
- `has_contribution`: has_contribution(a_contrib_id)

**Errors**:
- `ehr_id_does_not_exist`
- `contribution_does_not_exist`
- `ehr_does_not_exist`

#### 5.2.7. EHR_SUMMARY Class

**Description**: Summary form of EHR + EHR_STATUS objects convenient for service interface.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `ehr_id` | UUID | 1..1 | EHR identifier |
| `system_id` | String | 1..1 | Copy of EHR._system_id_ |
| `ehr_status` | EHR_STATUS | 1..1 | Copy of EHR._ehr_status_ |
| `time_created` | Iso8601_date_time | 1..1 | Copy of EHR._time_created_ |
| `contribution_count` | Integer | 1..1 | Number of Contributions in EHR |
| `composition_count` | Integer | 1..1 | Number of versioned Compositions in EHR |

#### 5.2.8. UV_FOLDER Class

**Description**: Form of UPDATE_VERSION specific to FOLDER.

**Inherits**: `UPDATE_VERSION`

#### 5.2.9. UV_COMPOSITION Class

**Description**: Form of UPDATE_VERSION specific to COMPOSITION.

**Inherits**: `UPDATE_VERSION`

---

## Demographic Service

### 6.1. Overview

The `platform.interface.demographic` package defines service interface to the DEMOGRAPHIC_SERVICE component. Primary functions:
- PARTY creation and versioning
- PARTY_RELATIONSHIP management
- Demographic data persistence with change control

### 6.2. Class Definitions

#### 6.2.1. I_DEMOGRAPHIC_SERVICE Interface

**Description**: Primary interface to DEMOGRAPHIC_SERVICE.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `create_party()` | a_version: UV_PARTY | UUID | Creates first PARTY version; creates VERSIONED_OBJECT, ORIGINAL_VERSION, CONTRIBUTION |
| `create_party_relationship()` | a_version: UV_PARTY_RELATIONSHIP | UUID | Creates first PARTY_RELATIONSHIP version; creates VERSIONED_OBJECT, ORIGINAL_VERSION, CONTRIBUTION |
| `i_party()` | a_versioned_party_id | I_PARTY | Creates I_PARTY interface |
| `i_party_relationship()` | a_versioned_party_rel_id | I_PARTY_RELATIONSHIP | Creates I_PARTY_RELATIONSHIP interface |

**Pre-conditions**:
- `party_definitions_valid`: definitions_valid(a_version)
- `content_valid`: valid_content(a_version)

**Errors**:
- `definition_unknown`
- `content_invalid`
- `versioned_object_does_not_exist`

#### 6.2.2. I_PARTY Interface

**Description**: Interface for PARTY-level operations.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_party()` | a_versioned_party_id: UUID | Boolean | Returns true if Party exists |
| `has_party_version_id()` | a_party_version_id: UUID | Boolean | True if particular Party version exists |
| `get_party()` | a_versioned_party_id: UUID | PARTY | Gets current PARTY version |
| `get_party_at_time()` | a_versioned_party_id: UUID, a_time: Iso8601_date_time | PARTY | Gets PARTY version current at time |
| `update_party()` | a_versioned_party_id: UUID, a_version: UV_PARTY | UUID | Updates PARTY with new version; creates ORIGINAL_VERSION and CONTRIBUTION |
| `delete_party()` | a_versioned_party_id: UUID | void | Deletes existing PARTY |
| `get_party_at_version()` | a_party_version_id: UUID | PARTY | Gets particular PARTY version |

**Pre-conditions**:
- `party_definitions_valid`: definitions_valid(a_version)
- `has_party`: has_party(a_versioned_party_id)

**Post-conditions**:
- `party_deleted`: not has_party(a_versioned_party_id)

**Errors**:
- `versioned_object_does_not_exist`
- `object_version_does_not_exist`
- `definition_unknown`
- `content_invalid`

#### 6.2.3. I_PARTY_RELATIONSHIP Interface

**Description**: Interface for PARTY_RELATIONSHIP operations.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `has_party_relationship()` | a_versioned_party_rel_id: UUID | Boolean | Returns true if Party relationship exists |
| `get_party_relationship()` | a_versioned_party_rel_id: UUID | PARTY_RELATIONSHIP | Gets current PARTY_RELATIONSHIP version |
| `get_party_relationship_at_time()` | a_versioned_party_rel_id: UUID, a_time: Iso8601_date_time | PARTY_RELATIONSHIP | Gets PARTY_RELATIONSHIP version current at time |
| `update_party_relationship()` | a_versioned_party_rel_id: UUID, a_version: UV_PARTY_RELATIONSHIP | UUID | Updates PARTY_RELATIONSHIP with new version; creates ORIGINAL_VERSION and CONTRIBUTION |
| `delete_party_relationship()` | a_versioned_party_rel_id: UUID | void | Deletes existing PARTY_RELATIONSHIP |
| `get_party_relationship_at_version()` | a_party_rel_version_id: UUID | PARTY_RELATIONSHIP | Gets particular PARTY_RELATIONSHIP version |

**Pre-conditions**:
- `party_definitions_valid`: definitions_valid(a_version)
- `has_relationship`: has_party_relationship(a_versioned_party_rel_id)

**Post-conditions**:
- `relationship_deleted`: not has_party_relationship(a_versioned_party_rel_id)

**Errors**:
- `versioned_object_does_not_exist`
- `object_version_does_not_exist`
- `definition_unknown`
- `content_invalid`

#### 6.2.4. UV_PARTY Class

**Description**: Form of UPDATE_VERSION specific to PARTY.

**Inherits**: `UPDATE_VERSION`

#### 6.2.5. UV_PARTY_RELATIONSHIP Class

**Description**: Form of UPDATE_VERSION specific to PARTY_RELATIONSHIP.

**Inherits**: `UPDATE_VERSION`

---

## EHR Index Service

### 7.1. Overview

The `platform.interface.ehr_index` package defines service interface to the EHR_INDEX component. Primary functions:
- Record associations of subject identifiers with EHR identifiers
- Manage multiple subject/EHR associations
- Track resource status and location information

In privacy-supporting environments, this enables EHRs persisted with only EHR id; the Index is used to obtain subject identifier, which keys into demographic or MPI service, ultimately linking EHR data with correct patient demographics.

No limit on associations:
- Multiple subject identifiers for one EHR: dangerous error condition indicating shared EHR
- Multiple EHRs for one subject: common error from duplicate EHR creation

### 7.2. Class Definitions

#### 7.2.1. I_EHR_INDEX Interface

**Description**: Interface object for EHR_INDEX service.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `add_ehr_subject()` | an_ehr_id: UUID, a_subject_id: OBJECT_REF, a_status: RESOURCE_STATUS (0..1), a_loc_desc: LOCATION_DESC (0..1) | void | Adds subject identifier for EHR with optional resource status and location descriptor |
| `update_ehr_subject_status()` | an_ehr_id: UUID, a_subject_id: OBJECT_REF, a_status: RESOURCE_STATUS | void | Updates subject resource status for EHR-subject association |
| `update_ehr_subject_loc_desc()` | an_ehr_id: UUID, a_subject_id: OBJECT_REF, a_loc_desc: LOCATION_DESC (0..1) | void | Updates location descriptor for EHR-subject association |
| `remove_ehr_subject()` | an_ehr_id: UUID, a_subject_id: OBJECT_REF | void | Removes subject identifier association with EHR |
| `remove_subject()` | a_subject_id: OBJECT_REF | void | Removes all entries for a subject |

**Errors**:
- `subject_id_does_not_exist`
- `ehr_id_does_not_exist`

#### 7.2.2. RESOURCE_STATUS Class

**Description**: Object describing status of reference to resource.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `instance_type` | RESOURCE_INSTANCE_TYPE | 1..1 | Type of resource instance |
| `start_valid_time` | date-time | 0..1 | First time point at which resource can be assumed available |
| `end_valid_time` | date-time | 0..1 | Last time point at which resource can be assumed available |
| `notes` | String | 0..1 | Human-readable notes on resource |

#### 7.2.3. RESOURCE_INSTANCE_TYPE Enumeration

| Value | Meaning |
|-------|---------|
| `Primary` | Primary instance of resource |
| `Duplicate` | Duplicate instance of resource |
| `Supplementary` | Supplementary instance |

#### 7.2.4. LOCATION_DESC Class

**Description**: Descriptor containing location information for the EHR with which it is associated.

---

## Query Service

### 8.1. Overview

The `platform.interface.query` package defines service interface to the QUERY_SERVICE component. Query execution model based on:
- Stored queries in DEFINITION service
- Ad hoc queries executed at runtime

For both types, parameters must be provided for open parameters in stored query.

Successful execution returns RESULT_SET with:
- Meta-data
- Column definitions
- Row data

Parameters `_item_offset_` and `_items_to_fetch_` handle large result sets efficiently.

Stored query identified by:
```
reverse-domain-name '::' semantic-id [ '/' version ]
```

Example: `org.example.departmentx.test::diabetes-patient-overview/1.0.2`

### 8.2. Class Definitions

#### 8.2.1. I_QUERY_SERVICE Interface

**Description**: Query execution service interface.

| Function | Parameters | Return | Meaning |
|----------|-----------|--------|---------|
| `execute_stored_query()` | exec_spec: STORED_QUERY_EXECUTE_SPEC, row_offset: Integer (0..1), rows_to_fetch: Integer (0..1), ehr_ids: List<UUID> (0..1) | RESULT_SET | Executes query stored in definition service by qualified name with provided parameters |
| `execute_ad_hoc_query()` | exec_spec: ADHOC_QUERY_EXECUTE_SPEC, row_offset: Integer (0..1), rows_to_fetch: Integer (0..1), ehr_ids: List<UUID> (0..1) | RESULT_SET | Executes ad hoc query with supplied text |

**Parameters**:
- `exec_spec`: Execution specification with query name/text and parameters
- `row_offset`: Zero or negative = 0; specifies result row offset for large sets
- `rows_to_fetch`: Zero or negative = "all"; specifies rows to fetch from offset
- `ehr_ids`: Specific EHRs to query; if none supplied, full population query on EHRs with is_queryable=true

**Errors**:
- `ehr_id_does_not_exist`

#### 8.2.2. STORED_QUERY_EXECUTE_SPEC Class

**Description**: Query execution specification for stored queries with name, parameters, and optional version.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `qualified_query_name` | String | 1..1 | Qualified name of form `reverse_domain::name` |
| `version` | String | 0..1 | If supplied, semver.org version to execute; if not supplied, latest version used |
| `query_parameters` | Hash<String, String> | 1..1 | Parameters as tagged String key-value pairs; tags must match query parameter names |

#### 8.2.3. ADHOC_QUERY_EXECUTE_SPEC Class

**Description**: Query execution specification for ad hoc queries with text and parameters.

| Attribute | Type | Cardinality | Default | Meaning |
|-----------|------|-------------|---------|---------|
| `source` | String | 1..1 | - | AQL text of query |
| `formalism` | String | 0..1 | "aql" | Query language formalism |
| `query_parameters` | Hash<String, String> | 1..1 | - | Parameters as tagged String key-value pairs |

#### 8.2.4. RESULT_SET Class

**Description**: Structured query execution result with column definitions and row data.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `columns` | List<RESULT_SET_COLUMN> | 1..1 | Column definition structure |
| `id` | String | 1..1 | Unique result set identifier |
| `creation_time` | Iso8601_date_time | 1..1 | Result set creation time by execution engine |
| `query` | RESULT_QUERY_DESCRIPTOR | 0..1 | Query descriptor |
| `rows` | List<RESULT_SET_ROW> | 0..1 | Row data |

#### 8.2.5. RESULT_SET_COLUMN Class

**Description**: Query column definition.

| Attribute | Type | Cardinality | Meaning |
|-----------|------|-------------|---------|
| `name` | String | 1..1 | Column name for caller use |
| `archetype_id` | String | 0..1 | Archetype identifier |
| `path` | String | 0..1 | RM path of data item |

---

## Message Service

### 9.1. Overview

The `platform.interface.message` package defines service interfaces for message import/export supporting multiple formats and EHR extract generation.

### 9.2. Class Definitions

#### 9.2.1. I_MESSAGE_SERVICE Interface

**Description**: Primary interface to message service for imports and exports.

#### 9.2.2. I_EHR_EXTRACT_SERVICE Interface

**Description**: Interface for EHR Extract service operations.

#### 9.2.3. I_TDD_SERVICE Interface

**Description**: Interface for Templated Data Description (TDD) service.

---

## Subject Proxy Service (SPS)

### 10.1. Overview

The Subject Proxy Service enables registration of subject-focused data-sets providing a "proxy" picture of the subject over time. Manages:
- Subject variables and data specifications
- Multiple sample types (data frame, openEHR, HL7v2, FHIR)
- Data bindings for environment variables
- Temporal tracking of subject data

### 10.2. Subject Variable Naming

Variables follow naming conventions:
- Subject identifiers: prefixed or specially marked
- Time-indexed variables for temporal series
- Data frame columns mapped to subject variables

### 10.3. Service Interface

Central interface: `I_SUBJECT_PROXY_SERVICE` providing:
- Data-set registration
- Sample collection and retrieval
- Binding management
- Persistence operations

### 10.4. Data Structures

Core data structures:
- `SUBJECT_PROXY`: Represents subject proxy instance
- `SUBJECT_VARIABLE`: Defines subject variable
- `SUBJECT_DATA_SET`: Specifies data-set composition
- `SAMPLE`: Abstract sample type
- `DATA_FRAME_SAMPLE`: Tabular data sample
- `OPENEHR_SAMPLE`: openEHR-format sample
- `HL7v2_SAMPLE`: HL7 v2 message sample
- `HL7_FHIR_SAMPLE`: FHIR resource sample
- `VARIABLE_SAMPLE`: Variable value sample
- `VARIABLE_VALUE`: Abstract variable value container
- `VARIABLE_VALUE_SINGLE`: Single-value container
- `VARIABLE_VALUE_LIST`: List value container
- `VARIABLE_VALUE_TIME_SERIES`: Time-series value container

---

## Terminology Service

### 11.1. Overview

The `platform.interface.terminology` package defines service interface to the TERMINOLOGY_SERVICE component. Provides:
- Terminology access and queries
- Intentional value set management
- Term relationships and definitions
- Term code lookups and mappings

### 11.2. Class Definitions

#### 11.2.1. I_TERMINOLOGY_SERVICE Interface

**Description**: Primary interface to Terminology Service.

#### 11.2.2. Terminology_description Class

**Description**: Descriptor for terminology system.

#### 11.2.3. Terminology_extract Class

**Description**: Extract of terminology content.

#### 11.2.4. Terminology_relation Class

**Description**: Represents relationships between terminologies.

#### 11.2.5. Term_relationship Class

**Description**: Represents relationships between terms.

#### 11.2.6. Term_code Class

**Description**: Represents term code identifier.

#### 11.2.7. Defined_term Class

**Description**: Represents defined term with code and description.

---

## Admin Service

### 12.1. Overview

The `platform.interface.admin` package defines service interface to the ADMIN_SERVICE component. Provides administrative facilities across all installed services:
- Backup and restore operations
- Data export and import
- System-level maintenance
- Archive operations

### 12.2. Class Definitions

#### 12.2.1. I_ADMIN_SERVICE Interface

**Description**: Primary interface to Admin Service.

#### 12.2.2. I_ADMIN_ARCHIVE Interface

**Description**: Interface for archive operations.

#### 12.2.3. I_ADMIN_DUMP_LOAD Interface

**Description**: Interface for system dump and load operations.

#### 12.2.4. DUMP_LOAD_FAIL_REPORT Class

**Description**: Report detailing failures in dump/load operations.

| Attribute | Type | Meaning |
|-----------|------|---------|
| `failed_count` | Integer | Number of failed items |
| `error_messages` | List<String> | Detailed error messages |
| `recovery_suggestions` | List<String> | Suggested recovery actions |

#### 12.2.5. EXPORT_SPEC Class

**Description**: Specification for data export operations.

---

**Source:** https://specifications.openehr.org/releases/SM/latest/openehr_platform.html
