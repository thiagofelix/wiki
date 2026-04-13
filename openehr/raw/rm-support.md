# Support Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/support.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## 1. Preface

### 1.1 Purpose

This document describes the openEHR Support Information Model, whose semantics are used by all openEHR Reference Models.

### 1.2 Related Documents

Prerequisite: The openEHR Architecture Overview

---

## 2. Support Package

### 2.1 Overview

The Support Reference Model comprises types used throughout the openEHR models, including assumed primitive types defined outside of openEHR. The package structure includes:

- `assumed_types` 'pseudo-package': types assumed to exist in an implementation technology
- Four Support packages: semantics for constants, terminology access, access to externally defined scientific units, and conversion information
- `EXTERNAL_ENVIRONMENT_ACCESS` class: a mixin class providing access to service interface classes

### 2.2 Class Definitions

#### 2.2.1 EXTERNAL_ENVIRONMENT_ACCESS Class

**Class**: `EXTERNAL_ENVIRONMENT_ACCESS` (abstract)
**Description**: A mixin class providing access to services in the external environment.
**Inheritance**: TERMINOLOGY_SERVICE, MEASUREMENT_SERVICE

---

## 3. Assumed Types

**Note**: These sections have been moved to the BASE component Foundation Types specification:
https://specifications.openehr.org/releases/BASE/latest/foundation_types.html

### 3.1 Inbuilt Primitive Types

Now in BASE component Foundation Types specification, Primitive Types section.

### 3.2 Assumed Library Types

Now in BASE component Foundation Types specification, Structure Types section.

### 3.3 Date/Time Types

Now in BASE component Foundation Types specification, Time Types section.

---

## 4. Identification Package

**Note**: Now available in the BASE component Base Types specification:
https://specifications.openehr.org/releases/BASE/latest/base_types.html#_identification_package

---

## 5. Terminology Package

### 5.1 Overview

This section describes the terminology package, containing classes for accessing terminologies and code sets, including the openEHR Support Terminology, from within instances of classes defined in the reference model.

### 5.2 Service Interface

#### 5.2.1 Code Sets

Two types of coded entities are distinguished:

1. **Code Sets**: Terminology where the code stands for itself (e.g., ISO 639-1 language codes). External identifiers not standardized but names like "ISO_639-1" expected.

Code sets needed within openEHR models are referred to via internal constants (e.g., `Code_set_id_languages`, with value "languages"). These constants defined in `OPENEHR_CODE_SET_IDENTIFIERS` class.

#### 5.2.2 Terminologies

Terminologies accessed via `TERMINOLOGY_SERVICE` functions `_terminology()_` and `_terminology_identifiers()_`. Arguments include:
- "openehr"
- "centc251" (for CEN TC/251 codes)
- Names from the US NLM terminologies list

The openEHR Terminology supports groups. The set of groups required by the reference model is defined in `OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS`.

#### 5.2.3 Terms and Codes in the openEHR Reference Model

True coded attributes (type `DV_CODED_TEXT`) defined by invariant in enclosing class:

```
Change_type_valid: terminology(Terminology_id_openehr).has_code_for_group_id
    (Group_id_audit_change_type, change_type.defining_code)
```

### 5.3 Identifiers

#### 5.3.1 Code Set Identifiers

Internal code set identifiers (e.g., "languages") defined in `OPENEHR_CODE_SET_IDENTIFIERS` class.

#### 5.3.2 Terminology Identifiers

Valid identifiers include:
- "openehr"
- "centc251"
- Identifiers from the US NLM UMLS terminology identifiers table (e.g., "ICD10AM_2000", "ICPC93", "SNOMED-CT", "LOINC")

### 5.4 Class Definitions

#### 5.4.1 TERMINOLOGY_SERVICE Class

**Class**: `TERMINOLOGY_SERVICE`
**Description**: Defines an object providing proxy access to a terminology service.
**Inheritance**: OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS, OPENEHR_CODE_SET_IDENTIFIERS

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `terminology(name: String): TERMINOLOGY_ACCESS` | Return interface to named terminology |
| 1..1 | `code_set(name: String): CODE_SET_ACCESS` | Return interface to code_set by external identifier |
| 1..1 | `code_set_for_id(id: String): CODE_SET_ACCESS` | Return interface to code_set by internal openEHR id |
| 1..1 | `has_terminology(name: String): Boolean` | True if terminology known |
| 1..1 | `has_code_set(name: String): Boolean` | True if code_set linked to internal name available |
| 0..1 | `terminology_identifiers(): List<String>` | All terminology identifiers known |
| 1..1 | `openehr_code_sets(): Hash<String, String>` | All code set identifiers known |
| 0..1 | `code_set_identifiers(): List<String>` | All code sets with internal openEHR name |

#### 5.4.2 TERMINOLOGY_ACCESS Interface

**Interface**: `TERMINOLOGY_ACCESS`
**Description**: Defines an object providing proxy access to a terminology.

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `id(): String` | Identification of this Terminology |
| 1..1 | `all_codes(): CODE_PHRASE` | Return all codes known |
| 0..1 | `codes_for_group_id(a_group_id: String): List<CODE_PHRASE>` | Codes under grouper |
| 0..1 | `codes_for_group_name(a_lang: String, a_name: String): List<CODE_PHRASE>` | Codes under named grouper |
| 1..1 | `has_code_for_group_id(): Boolean` | True if code in group |
| 1..1 | `rubric_for_code(a_code: String): String` | Return rubric of code |

#### 5.4.3 CODE_SET_ACCESS Interface

**Interface**: `CODE_SET_ACCESS`
**Description**: Defines an object providing proxy access to a code_set.

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `id(): String` | External identifier of this code set |
| 0..1 | `all_codes(): List<CODE_PHRASE>` | All codes known |
| 1..1 | `has_lang(a_lang: String): Boolean` | True if code set knows about language |
| 1..1 | `has_code(a_code: String): Boolean` | True if code set knows about code |

#### 5.4.4 OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS Class

**Class**: `OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS`
**Description**: List of identifiers for groups in the openEHR terminology.

**Constants**:

| Constant | Value |
|---|---|
| `Terminology_id_openehr` | "openehr" |
| `Group_id_audit_change_type` | "audit change type" |
| `Group_id_attestation_reason` | "attestation reason" |
| `Group_id_composition_category` | "composition category" |
| `Group_id_event_math_function` | "event math function" |
| `Group_id_instruction_states` | "instruction states" |
| `Group_id_instruction_transitions` | "instruction transitions" |
| `Group_id_null_flavours` | "null flavours" |
| `Group_id_property` | "property" |
| `Group_id_participation_function` | "participation function" |
| `Group_id_participation_mode` | "participation mode" |
| `Group_id_setting` | "setting" |
| `Group_id_term_mapping_purpose` | "term mapping purpose" |
| `Group_id_subject_relationship` | "subject relationship" |
| `Group_id_version_life_cycle_state` | "version lifecycle state" |

#### 5.4.5 OPENEHR_CODE_SET_IDENTIFIERS Class

**Class**: `OPENEHR_CODE_SET_IDENTIFIERS`
**Description**: List of identifiers for code sets in the openEHR terminology.

**Constants**:

| Constant | Value |
|---|---|
| `Code_set_id_character_sets` | "character sets" |
| `Code_set_id_compression_algorithms` | "compression algorithms" |
| `Code_set_id_countries` | "countries" |
| `Code_set_integrity_check_algorithms` | "integrity check algorithms" |
| `Code_set_id_languages` | "languages" |
| `Code_set_id_media_types` | "media types" |
| `Code_set_id_normal_statuses` | "normal statuses" |

---

## 6. Measurement Package

### 6.1 Overview

The Measurement package defines minimum semantics relating to quantitative measurement, units, and conversion.

Definitions based on:
- CEN ENV 12435 (Medical Informatics - Expression of results of measurements in health sciences)
- UCUM (Unified Code for Units of Measure)

### 6.2 Service Interface

Simple measurement data service interface enabling quantitative semantics.

### 6.3 Class Definitions

#### 6.3.1 MEASUREMENT_SERVICE Class

**Class**: `MEASUREMENT_SERVICE`
**Description**: Defines an object providing proxy access to a measurement information service.

**Functions**:

| Cardinality | Signature | Meaning |
|---|---|---|
| 1..1 | `is_valid_units_string(units: String): Boolean` | True if units string valid per UCUM |
| 1..1 | `units_equivalent(units1: String, units2: String): Boolean` | True if units correspond to same property |

---

## 7. Definition Package

**Note**: Now available in the BASE component Base Types specification:
https://specifications.openehr.org/releases/BASE/latest/base_types.html#_definitions_package
