# openEHR Resource Model Specification

**Issuer:** openEHR Specification Program
**Release:** BASE Release-1.2.0
**Status:** STABLE
**Date:** Last updated 2020-07-27
**Keywords:** openehr, resources

© 2003 - 2021 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Amendment Record](#amendment-record)
2. [Acknowledgements](#acknowledgements)
3. [Preface](#preface)
4. [Resource Package](#resource-package)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| BASE Release 1.2.0: 1.8.3 | Add `_other_contributors_` to `TRANSLATION_DETAILS` | S Garde | 22 Feb 2021 |
| 1.8.1 | Correct UML package nesting and paths | T Beale | 27 Nov 2017 |
| 1.8.0 | Separate from openEHR Common IM 2.1.2 | openEHR SEC | 15 Feb 2016 |
| Release 1.0.1: 1.6.0 | Define `AUTHORED_RESOURCE._current_revision_` | Y S Lim | 08 Apr 2007 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica; openEHR Foundation Management Board

### Contributors

- Silje Ljosland Bakke (National ICT health trust, Norway)
- Diego Boscá (IBIME, Technical University Valencia, Spain)
- Sebastian Garde (Ocean Health Systems, Germany)
- Grahame Grieve (Health Intersections, Australia)
- Heather Leslie (Ocean Health Systems, Australia)
- Ian McNicoll (FreshEHR UK)
- Andrew Patterson (Federation Health Software, Australia)

### Supporters

- University College London - CHIME
- Ocean Informatics

---

## Preface

### Purpose

The document characterizes the openEHR Resource Model, which encompasses "identification, meta-data, annotations and translations" for any authored resource. This specification serves standards bodies, academic institutions, solution vendors, and medical informaticians.

### Related Documents

- The openEHR Architecture Overview

### Status

Content was extracted from RM 1.0.3 Common IM specification to enable reuse across openEHR components. The specification remains in STABLE state.

### Feedback

- Technical feedback: [openEHR Discourse](https://discourse.openehr.org/c/specifications)
- Issues: [Problem Report Tracker](https://specifications.openehr.org/components/BASE/open_issues)

### Conformance

Conformance is determined through formal testing against openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas.

---

## Resource Package

### Overview

The BASE component `resource` package defines "the structure and semantics of the general notion of an online resource which has been created by a human author" with consideration for natural language factors.

#### Natural Languages and Translation

Authored resources contain natural language elements and are created in an original language stored in the `_original_language_` attribute. Translation involves:

- Converting all language-dependent elements to the target language
- Adding a new `TRANSLATION_DETAILS` instance to the translations attribute
- Including translator details, organization, and quality assurance information

The `languages_available` function provides a complete list of supported languages.

#### Meta-data

Resource metadata—author, creation date, purpose, descriptive information—is captured through `RESOURCE_DESCRIPTION` and `RESOURCE_DESCRIPTION_ITEM` classes. Language-dependent elements are represented in `RESOURCE_DESCRIPTION_ITEM` instances, enabling multiple translations.

The `AUTHORED_RESOURCE`.`_description_` attribute is optional, permitting resources without metadata (e.g., partial constructions).

#### Revision History

When `is_controlled` is set to True, changes undergo audit trail recording. The `revision_history` attribute functions as a "documentary copy of the revision history as known inside the repository" for interoperable use across tools.

---

## Class Descriptions

### AUTHORED_RESOURCE Class

**Type:** Abstract

**Purpose:** Represents the abstract concept of an online resource created by a human author.

#### Attributes

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 0..1 | `uid` | UUID | Unique identifier of the archetype family |
| 1..1 | `original_language` | Terminology_code | Initial authorship language (ISO 639-1) |
| 0..1 | `description` | RESOURCE_DESCRIPTION | Descriptive metadata and lifecycle |
| 0..1 | `is_controlled` | Boolean | Indicates change control status |
| 0..1 | `annotations` | Hash | Path-keyed annotations on resource items |
| 0..1 | `translations` | Hash<String, TRANSLATION_DETAILS> | Language-keyed translation details |

#### Functions

| Return | Signature | Meaning |
|---|---|---|
| String | `current_revision()` | Most recent revision or "(uncontrolled)" |
| List<String> | `languages_available()` | All available languages in resource |

#### Invariants

- Original language must be valid per language code set
- Current revision validity depends on control status
- Translations must be non-empty and exclude original language
- Description language codes must match translation keys
- Original language always appears in available languages
- Revision history required if controlled

---

### TRANSLATION_DETAILS Class

**Purpose:** Provides metadata for natural language translations.

#### Attributes

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | `language` | Terminology_code | Translation language (ISO 639-1) |
| 1..1 | `author` | Hash<String, String> | Translator name and demographics |
| 0..1 | `accreditation` | String | Translator registration or membership ID |
| 0..1 | `other_details` | Hash<String, String> | Additional metadata pairs |
| 0..1 | `version_last_translated` | String | Resource version last translated |
| 0..1 | `other_contributors` | List<String> | Additional contributors to translation |

---

### RESOURCE_DESCRIPTION Class

**Purpose:** Defines descriptive metadata of a resource.

#### Attributes

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | `original_author` | Hash<String, String> | Original author with details |
| 0..1 | `original_namespace` | String | Author organization namespace (reverse internet form) |
| 0..1 | `original_publisher` | String | Original publishing organization |
| 0..1 | `other_contributors` | List<String> | Additional contributors in "name <email>" form |
| 1..1 | `lifecycle_state` | Terminology_code | Resource lifecycle status |
| 1..1 | `parent_resource` | AUTHORED_RESOURCE | Reference to owning resource |
| 0..1 | `custodian_namespace` | String | Current custodian namespace |
| 0..1 | `custodian_organisation` | String | Current custodian organization |
| 0..1 | `copyright` | String | Copyright statement |
| 0..1 | `licence` | String | License in "name <URL>" format |
| 0..1 | `ip_acknowledgements` | Hash<String, String> | IP source acknowledgments |
| 0..1 | `references` | Hash<String, String> | Citation references |
| 0..1 | `resource_package_uri` | String | Package URI |
| 0..1 | `conversion_details` | Hash<String, String> | Model conversion metadata |
| 0..1 | `other_details` | Hash<String, String> | Additional non-linguistic metadata |
| 0..1 | `details` | Hash<String, RESOURCE_DESCRIPTION_ITEM> | Language-specific description |

---

### RESOURCE_DESCRIPTION_ITEM Class

**Purpose:** Captures language-specific resource description details.

#### Attributes

| Cardinality | Attribute | Type | Meaning |
|---|---|---|---|
| 1..1 | `language` | Terminology_code | Localized language (ISO 639-1) |
| 1..1 | `purpose` | String | Resource purpose statement |
| 0..1 | `keywords` | List<String> | Indexing and search keywords |
| 0..1 | `use` | String | Usage contexts and applications |
| 0..1 | `misuse` | String | Inappropriate usage contexts |
| 0..1 | `original_resource_uri` | Hash<String, String> | URIs of source clinical documents |
| 0..1 | `other_details` | Hash<String, String> | Language-sensitive metadata pairs |

---

## Additional Information

**Support Resources:**
- Web: [specifications.openEHR.org](https://specifications.openehr.org)
- Issues: [Problem Reports](https://specifications.openehr.org/components/BASE/open_issues)

**Foundation:** The openEHR Foundation facilitates health record sharing through open specifications and clinical models.
