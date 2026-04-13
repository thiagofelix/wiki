# Integration Information Model

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| RM Release 1.1.0 | — | — | — |
| RM Release 1.0.4 | — | — | — |
| Release 1.0.1 | 0.6 | SPEC-203: Release 1.0 explanatory text improvements. Added section on openEHR Extract. Added integration architecture diagram. | T Beale | 22 Jul 2006 |
| Release 1.0 | 0.5 | Initial writing. | T Beale | 15 Sep 2005 |

## Acknowledgements

The work reported in this document has been funded in part by:

- University College London - Centre for Health Informatics and Multi-professional Education (CHIME)
- Ocean Informatics

Special thanks to David Ingram, Emeritus Professor of Health Informatics at UCL, for providing vision and collegial working environment since the GEHR days (1992).

## 1. Preface

### 1.1. Purpose

This document describes the architecture of the openEHR Integration Information Model, designed for use in legacy and other integration situations.

**Intended audience includes:**

- Standards bodies producing health informatics standards
- Academic groups using openEHR
- Open source healthcare community
- Solution vendors
- Medical informaticians and clinicians interested in health information
- Health data managers

### 1.2. Related Documents

Prerequisite documents include:

- The openEHR Architecture Overview

### 1.3. Status

This specification is in the Stable state. The development version can be found at https://specifications.openehr.org/releases/RM/latest/integration.html.

Known omissions or questions are indicated with "TBD" (To Be Determined) paragraphs.

### 1.4. Feedback

- Feedback: openEHR RM specifications forum
- Issues: specifications Problem Report tracker
- Changes: RM component Change Request tracker

### 1.5. Conformance

Conformance of a data or software artifact to an openEHR specification is determined by formal testing against relevant openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

## 2. Integration Package

### 2.1. Requirements

Data exchange represents a fundamental openEHR requirement. Native openEHR structures work seamlessly in greenfield situations and GUI-driven EHR API applications. Most other scenarios involve external or legacy data sources with different syntactic and semantic formats than openEHR data.

**Typical legacy data sources include:**

- Relational databases
- HL7v2 messages
- HL7 CDA documents
- EDIFACT messages
- Proprietary hospital, GP, and desktop system models

Standardized versus non-standardized legacy models present no significant technical difference; reusability varies.

**Key external data category:** ISO 13606 Extracts. Part 1 of ISO 13606 defines an information model nearly identical to openEHR at the COMPOSITION and SECTION levels. The ISO 13606 Entry class is generic with minimal contextual metadata, mapping easily to the openEHR Entry type.

**Primary need:** Converting data from multiple incompatible sources into a single standardized patient-centric EHR enabling longitudinal viewing and querying. This integrates GP and specialist notes, diagnoses, plans, laboratory results, administrative data into a coherent patient journey record.

**Technical incompatibilities requiring resolution:**

- Scope correspondence: incoming documents may map to multiple clinical archetypes
- Structural differences: legacy data typically flatter than target archetype structures
- Terminology variability: existing systems use inconsistent terminology
- Data type mismatches: for example, mapping string "110/80 mmHg" to two DV_QUANTITY objects with separate values and units

### 2.2. Design Basis

#### 2.2.1. Overview

The design foundation separates syntactic and semantic transformations required on data:

1. **Syntactic transformation:** Converts source data to a special openEHR reference model class format, with logical structure and semantics controlled by integration archetypes mimicking source data design. This brings data into openEHR computational context.

2. **Semantic transformation:** Converts intermediate openEHR data into main reference model instances obeying designed clinical archetypes.

**Architecture elements enabling transformation:**

- `GENERIC_ENTRY` class: a sibling of SECTION and ENTRY, containing completely generic, archetypable structures
- Integration archetypes: defined against GENERIC_ENTRY class
- Semantic transformation rules: from GENERIC_ENTRY-based openEHR data to ENTRY subtypes with designed archetypes

The `rm.integration` package contains a single class `GENERIC_ENTRY`. Unlike other openEHR reference model classes, it contains no hard-wired attributes, only a generic `_data_` attribute. No assumptions about actual data shape are made.

#### 2.2.2. Semantics of GENERIC_ENTRY

Several useful consequences follow from this modeling approach:

**Archetypability:** GENERIC_ENTRY instances contain inherited LOCATABLE attributes including `_archetype_node_id_`, enabling archetypable treatment identical to all other openEHR reference model classes. The LOCATABLE attribute `feeder_audit` marks every data node with relevant metadata from source system records or messages.

**Composition integration:** As a CONTENT_ITEM subtype, GENERIC_ENTRY is valid for `COMPOSITION._content_`. Identical rules apply: instances commit to records only as COMPOSITION components. GENERIC_ENTRY data receive audit-trailing and versioning.

**Hierarchical organization:** GENERIC_ENTRY instances may occur within SECTION hierarchies, useful for data sources with headings or section equivalents (common in hospital information systems containing physician notes).

**Path construction:** Design-time paths can be constructed for GENERIC_ENTRY archetypes; runtime paths extract from data based on such archetypes. These path sets enable writing data transformation rules.

**Important limitation:** While GENERIC_ENTRY provides standardized syntactic form for externally sourced openEHR data, it provides no semantic coherence. GENERIC_ENTRY representations of identical concepts from different systems lack congruence. Different pathology laboratories implementing the same HL7v2 minor version and message type differ in actual structure and content. Consequently, GENERIC_ENTRY data cannot safely support clinical computation or reliable querying. A GENERIC_ENTRY repository within appropriate COMPOSITION structures constitutes a standardized health information data store for semantic conversion input/output and auditing, not a reliable interoperable health record.

#### 2.2.3. Use with openEHR Extracts

The GENERIC_ENTRY class represents data from non-openEHR systems implementing the openEHR Extract specification for communicating with openEHR systems or other Extract-compliant systems.

#### 2.2.4. Integration with ISO 13606

The GENERIC_ENTRY class provides basis for openEHR ISO 13606 compliance, enabling gateway capability in heterogeneous ISO 13606 environments.

**Conversion pathway:** ISO 13606 EHR Extracts convert to COMPOSITION series containing GENERIC_ENTRY objects obeying integration archetypes. Data then undergoes semantic conversion into orthodox openEHR objects for coherent EHR integration. Conversely, openEHR data converts to GENERIC_ENTRY intermediate form for further conversion to ISO 13606 EHR Extracts.

### 2.3. Data Conversion Architecture

The integration archetype-based strategy for importing data into openEHR systems comprises two steps:

**Step 1 - Syntactic transformation:** Data convert from original syntactic format into openEHR COMPOSITION/SECTION/GENERIC_ENTRY structures via the openEHR integration switch. Most data appears in the GENERIC_ENTRY component, controlled by an integration archetype designed to mimic incoming structure (HL7v2 lab messages, for example). FEEDER_AUDIT structures contain integration metadata. The result expresses data in the openEHR type system as openEHR reference model instances, immediately processable by standard openEHR software.

**Step 2 - Semantic transformation:** Mappings between integration and designed archetypes effect semantic transformation, created by archetype authors using tools. Mapping rules define structural transformations, terminological code usage, and other changes. Heterogeneous system integration challenges remain, with some addressed in Common IM Feeder systems documentation.

### 2.4. Class Descriptions

#### 2.4.1. GENERIC_ENTRY Class

**Class:** GENERIC_ENTRY

**Description:** Creates intermediate representations of data from sources not conforming to openEHR classes, such as HL7 messages and relational databases.

**Inheritance:** CONTENT_ITEM

**Attributes:**

| Cardinality | Name | Type | Meaning |
|-------------|------|------|---------|
| 1..1 | data | ITEM_TREE | The 'data' from the source message or record. |

---

**Document Information**

- **Issuer:** openEHR Specification Program
- **Release:** RM Release-1.1.0
- **Status:** STABLE
- **Keywords:** EHR, integration, openehr
- **Last Updated:** 2021-02-15 13:27:48 UTC

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported (https://creativecommons.org/licenses/by-nd/3.0/)

**Copyright:** © 2003 - 2021 The openEHR Foundation

**Source URL**: https://specifications.openehr.org/releases/RM/latest/integration.html
