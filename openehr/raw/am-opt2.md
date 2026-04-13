# Operational Template 2 (OPT2) Specification

**Document Status:** DEVELOPMENT
**Release:** AM Release-2.3.0
**Issuer:** openEHR Specification Program
**Last Updated:** 2022-11-12

---

## Table of Contents

- [Operational Template 2 (OPT2)](#operational-template-2-opt2)
  - [Amendment Record](#amendment-record)
  - [Acknowledgements](#acknowledgements)
  - [1. Preface](#1-preface)
  - [2. Overview](#2-overview)
  - [3. The Raw Operational Template](#3-the-raw-operational-template)
  - [4. The Profiled Operational Template](#4-the-profiled-operational-template)
  - [5. File Formats](#5-file-formats)
  - [References](#references)

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| 0.5.1 | Added 'Purpose' section | T Beale | 08 Jun 2016 |
| 0.5.0 | Initial Writing | T Beale | 28 Oct 2015 |

**Release History:**
- AM Release 2.3.0
- AM Release 2.2.0
- AM Release 2.1.0
- AM Release 2.0.6

---

## Acknowledgements

### Primary Author

Thomas Beale, Ars Semantica, UK; openEHR International Board

### Trademarks

- 'openEHR' is a registered trademark of The openEHR Foundation
- 'SNOMED CT' is a registered trademark of IHTSDO

---

## 1. Preface

### 1.1. Purpose

This specification describes the formal requirements for Operational Templates (OPT) based on ADL2 artefacts. An OPT represents a "first generation 'compiled' artefact based on source archetypes and templates, that serves as the starting point for further downstream format generation (e.g. schemas, APIs) as well as the computational format for operational EHR systems." This document targets software developers.

### 1.2. Related Documents

**Prerequisite Documents:**
- The openEHR Archetype Technical Overview

**Related Documents:**
- The openEHR Archetype Object Model (AOM2)

### 1.3. Nomenclature

The term 'attribute' denotes any stored property of a type defined in an object model, encompassing primitive attributes and relationships such as associations or aggregations. XML 'attributes' are explicitly identified as such.

'Archetype' is used broadly to designate both archetypes (clinical data group specifications/constraints) and templates (data sets based on archetypes), since technically an ADL/AOM 2 template functions as an archetype.

### 1.4. Status

This specification is in DEVELOPMENT state. The development version is available at: https://specifications.openehr.org/releases/AM/latest/OPT2.html

Unresolved items appear as "TBD" (To Be Determined) paragraphs throughout the document.

### 1.5. Feedback

- **Forum:** openEHR ADL forum at discourse.openehr.org
- **Issue Tracker:** specifications Problem Report tracker
- **Change History:** AM component Change Request tracker

### 1.6. Conformance

Conformance to openEHR specifications is determined through formal testing against relevant Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

### 1.7. Tools

Key resources include:

- **ADL Workbench:** reference compiler, visualiser, and editor
- **Downloads:** https://www.openehr.org/downloads/modellingtools
- **Source Projects:** openEHR Github project

### 1.8. Relationship to OPT '1.4'

This specification describes an OPT based on ADL2/AOM2, distinct from the original OPT, which was an XML-schema format based on ADL 1.4 archetypes.

---

## 2. Overview

The Operational Template is a family of technical artefacts generated from source templates and archetypes expressed in ADL2.

### 2.1. Purpose of the OPT

The OPT serves as a compiled form of source archetypes and templates, fulfilling several critical functions:

1. **Safety and Validation:** Production EHR systems must operate exclusively with validated templates and archetypes, never directly using source artefacts.

2. **Specialisation Resolution:** The specialisation relationship between archetypes requires evaluation to produce usable, inheritance-flattened artefacts, analogous to executable class forms in object-oriented programming.

3. **Customisation:** Source artefacts often require adjustments for deployment. An OPT enables selective inclusion of languages and terminology bindings appropriate for specific contexts.

4. **Machine Format Optimization:** OPTs are designed for implementation convenience rather than human use, supporting formats such as ADL, ODIN, JSON, XML, and YAML.

5. **Transformation Basis:** The OPT serves as a standardised input for generating other artefact types, including Template Data Schemas (TDS), Template Data Objects (TDO), and APIs.

### 2.2. Types of OPT

Two OPT types exist: **raw** and **profiled**.

**Raw OPT:** A unified archetype structure derived from flattened source archetypes and templates, containing all content regarding languages and terminology bindings.

**Profiled OPT:** A processed form of the raw OPT with selective removal of languages, terminology bindings, and annotations. Multiple profiled OPTs may derive from a single raw OPT.

```
Archetypes & Templates -> Raw OPT -> Profiled OPT(s)
                           |
                      Other Formats
                    (Schemas, APIs, etc.)
```

OPTs function as top-level, non-specialised archetypes with these distinctions from source artefacts:

- All archetype references resolved to specific identifiers with full versions
- No specialisation statement
- No sibling order markers (`before`/`after`)
- No `use_node` nodes; all internal references expanded
- All slot-fillers and external references resolved and substituted
- Closed slots removed
- Deleted nodes removed (attributes with `existence matches {0}`)
- All template overlays applied (flattening)
- Flattened `terminology` sections consolidated in `component_terminologies`

---

## 3. The Raw Operational Template

A raw OPT represents the initial processing stage, derived from a master source template and all referenced archetypes and templates. All references are resolved, the structure is fully flattened, and deleted nodes are removed.

### 3.1. Artefact Structure

As a top-level standalone artefact, the raw OPT contains no specialisation statement. Its structure follows standard top-level archetype rules:

```antlr
adl_operational_template: 'operational_template' '(' qualifiers? ')'
        ARCHETYPE_HRID
    'language'
        odin_text
    'description'
        odin_text
    'definition'
        cadl_text
    ('rules'
        rules_text)?
    'terminology'
        odin_text
    ('annotations'
        odin_text)?
    'component_terminologies'
        odin_text
    ;
```

### 3.2. Archetype References

All archetype references from source archetypes and templates -- typically lacking full version information -- are resolved to complete archetype identifiers. OPT output guarantees inclusion of full three-part versions.

### 3.3. Flattening

OPT flattening extends beyond standard flattening (described in the AOM specification) through these additional steps:

- **Sibling Sets:** Full expression of object node siblings under container attributes eliminates sibling order markers
- **Internal References:** `use_node` references replaced by inline copies of target structures
- **Slot Processing:**
  - Closed slots removed entirely
  - Slot-filler references replaced by inline archetype copies
- **Node Deletion:** All deleted nodes removed, including attributes with `existence matches {0}` and objects with `occurrences matches {0}`

### 3.4. Terminology

During flattening, the flat form of each constituent archetype or template's `terminology` section (excluding the root template) is consolidated under the `component_terminologies` section.

---

## 4. The Profiled Operational Template

A profiled OPT represents a processed raw OPT tailored for specific operational contexts. It undergoes selective removal of unwanted elements and terminology reference conversion. Tools specify alterations; this section documents resulting outputs only.

### 4.1. Annotations Removal

The `annotations` section may be completely removed from a raw OPT, resulting in a profiled OPT without annotations.

### 4.2. Language Filtering

Since archetypes and templates typically contain multiple language translations while deployment environments target one or two languages, language filtering removes unnecessary translations down to a minimum of one.

The `original_language` property in the resulting OPT's `language` section reflects the root source template's original authoring language, which may differ from referenced archetypes' authoring languages.

### 4.3. Terminology Binding Filtering

Terminology bindings may be globally filtered in the profiled OPT, ranging from selective removal to complete elimination. The resulting OPT contains only bindings not designated for removal in the `terminology` section.

### 4.4. Terminology Substitution

Terminology processing addresses two coded value scenarios in source artefacts:

1. **Archetype Local Value Sets:** Fields constrained with archetype local codes (ac-codes mapping to at-codes or single at-codes)

2. **External Value Sets:** ac-codes bound exclusively to external value sets; recorded data must use external codes

The first case permits a choice between archetype-local or external codes. Selection strategies include:

- **Library-Level Selection:** Choose terminologies by removing unwanted bindings
- **Per-OPT Selection:** Input OPT profiling arguments specific to each OPT
- **Node-Level Selection:** Make choices in the raw OPT (currently unsupported in ADL2)

> **TBD:** Node-level control requires ADL2 implementation allowing path-based node selection with allowed terminology lists.

Results are expressed in profiled OPTs through modified term constraint syntax, detailed in the ADL specification's Terminology Constraints and Terminology Integration sections.

---

## 5. File Formats

### 5.1. File-naming

Raw and profiled OPTs use distinct filenames to prevent confusion. Standard file extensions include:
- `.opt` -- ADL format
- `.optx` -- XML format
- `.optj` -- JSON format
- `.opty` -- YAML format

### 5.2. Concrete Formats

#### 5.2.1. ADL

OPTs may be serialised in ADL format, providing human-readable representation suitable for reference and development tools.

#### 5.2.2. Object-dump Formats -- JSON, YAML

Object-dump formats (JSON and YAML) offer machine-friendly serialisation for system integration and data interchange applications.

#### 5.2.3. XML

XML serialisation provides structured format compatibility with schema-based systems and legacy integration requirements.

---

## References

- openEHR Archetype Technical Overview
- openEHR Archetype Object Model (AOM2)
- ADL2 Specification (Terminology Constraints and Integration sections)
- Implementation Technology Specifications (ITSs)

**Web:** https://specifications.openehr.org

---

## License & Copyright

(c) 2015 - 2024 The openEHR Foundation

Licensed under Creative Commons Attribution-NoDerivs 3.0 Unported: https://creativecommons.org/licenses/by-nd/3.0/
