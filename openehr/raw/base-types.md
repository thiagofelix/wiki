# Base Types

## Table of Contents

- [Base Types](#base-types)
  - [Amendment Record](#amendment-record)
  - [Acknowledgements](#acknowledgements)
    - [Authors](#authors)
    - [Contributors](#contributors)
    - [Trademarks](#trademarks)
  - [1. Preface](#1-preface)
    - [1.1. Purpose](#11-purpose)
    - [1.2. Related Documents](#12-related-documents)
    - [1.3. Status](#13-status)
    - [1.4. Feedback](#14-feedback)
    - [1.5. Previous Versions](#15-previous-versions)
  - [2. Overview](#2-overview)
  - [3. Definitions Package](#3-definitions-package)
    - [3.1. Overview](#31-overview)
    - [3.2. Class Definitions](#32-class-definitions)
      - [3.2.1. BASIC_DEFINITIONS Class](#321-basic_definitions-class)
      - [3.2.2. OPENEHR_DEFINITIONS Class](#322-openehr_definitions-class)
      - [3.2.3. VALIDITY_KIND Enumeration](#323-validity_kind-enumeration)
      - [3.2.4. VERSION_STATUS Enumeration](#324-version_status-enumeration)
  - [4. Builtins Package](#4-builtins-package)
    - [4.1. Overview](#41-overview)
    - [4.2. Class Definitions](#42-class-definitions)
      - [4.2.1. Env Interface](#421-env-interface)
      - [4.2.2. Locale Interface](#422-locale-interface)
      - [4.2.3. Statistical_evaluator Interface](#423-statistical_evaluator-interface)
      - [4.2.4. Math Interface](#424-math-interface)
      - [4.2.5. Quantity_converter Interface](#425-quantity_converter-interface)
  - [5. Identification Package](#5-identification-package)
    - [5.1. Overview](#51-overview)
    - [5.2. Requirements](#52-requirements)
    - [5.3. Design](#53-design)
    - [5.4. Class Descriptions](#54-class-descriptions)
    - [5.5. Syntaxes](#55-syntaxes)

---

## Document Metadata

**Issuer:** openEHR Specification Program

**Release:** BASE Release-1.2.0

**Status:** STABLE

**Revision:** [latest_issue]

**Date:** [latest_issue_date]

**Keywords:** openehr, identifiers, types

**Copyright:** © 2016 - 2021 The openEHR Foundation

**Licence:** Creative Commons Attribution-NoDerivs 3.0 Unported.
https://creativecommons.org/licenses/by-nd/3.0/

**Support:**
- Issues: Problem Reports
- Web: specifications.openEHR.org

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| **BASE Release 1.2.0** | | | |
| 1.2.0 | SPECBASE-26: Add Built-in classes and functions for use in AQL, EL; added `builtins` package. | openEHR SEC | 28 Nov 2020 |
| | SPECBASE-28: Fix `internet_id` and `uid_based_id` confusion in syntax definition; SPECBASE-29: Fix version-id syntax issue in `ARCHETYPE_ID` syntax definition. | S Garde, S Iancu | 05 Nov 2020 |
| | SPECBASE-27: Correct `OBJECT_REF._namespace_` regex so that it is legal. | J Smolka, S Iancu, M Polajnar, D Bosca | 25 Aug 2020 |
| | SPECRM-88: Improve documentation relating to use of `_uid_` in versioning; Improve explanatory text in section 'Identifying Versions within openEHR Versioned Containers'; corrected definition of `UID_BASED_ID._has_extension()_` to 'True if empty' rather than 'True if Void'. | P Pazos, M Polajnar, T Beale | 15 Oct 2019 |
| **BASE Release 1.1.0** | | | |
| 1.1.0 | SPECBASE-19: Broaden `LOCATABLE_REF._as_uri()_` to allow URIs referring to any health data. | T Beale | 09 Jan 2018 |
| | SPECPUB-6: Correct UML package nesting and paths in documents; insert `base` parent package. | T Beale | 27 Nov 2017 |
| | SPECBASE-7: Add Base Types specification to BASE component. | T Beale | 02 Sep 2017 |
| 0.7.0 | Initial Writing; split out from Foundation Types. Taken from openEHR RM Release 1.0.3 Support Model. | T Beale | 17 Aug 2017 |

The Amendment history relevant to the original content in this specification can be found in the openEHR RM Release 1.0.3 Support Model documentation.

---

## Acknowledgements

### Authors

This specification is developed and maintained by the openEHR Specifications Editorial Committee.

### Contributors

This specification has benefited from formal and informal input from the openEHR and wider health informatics community.

### Trademarks

- 'openEHR' is a registered trademark of the openEHR Foundation

---

## 1. Preface

### 1.1. Purpose

This document describes the openEHR Base Types, a collection of general types used by other openEHR specifications.

The intended audience includes:

- Standards bodies producing health informatics standards
- Research groups using openEHR, ISO 13606, archetypes and related technologies
- The open source healthcare community
- Solution vendors

### 1.2. Related Documents

Prerequisite documents for reading this document include:

- The openEHR Architecture Overview

### 1.3. Status

This specification is in the STABLE state. The development version of this document can be found at https://specifications.openehr.org/releases/BASE/Release-1.2.0/base_types.html.

Known omissions or questions are indicated in the text with a 'to be determined' paragraph.

### 1.4. Feedback

Feedback may be provided on the technical mailing list at https://discourse.openehr.org/c/specifications.

Issues may be raised on the specifications Problem Report tracker.

To see changes made due to previously reported issues, see the BASE component Change Request tracker.

### 1.5. Previous Versions

This specification is based on the types originally defined in the openEHR Support Information Model from Release 1.0.3 of the Reference Model.

---

## 2. Overview

The openEHR Base Types (`org.openehr.base_types` package) consists of basic types used globally throughout the openEHR components and specifications, including:

- Definitions
- Various enumerations
- Built-in types providing utility functions
- Identifier types
- Terminology-related types

The latter two categories are intended to support all kinds of references (to terminology terms, informational objects, real world entities).

---

## 3. Definitions Package

### 3.1. Overview

The `base_types.definitions` package defines symbolic definitions used by the openEHR models.

### 3.2. Class Definitions

#### 3.2.1. BASIC_DEFINITIONS Class

| Aspect | Details |
|--------|---------|
| **Class** | **BASIC_DEFINITIONS** |
| **Description** | Defines globally used constant values. |

**Constants:**

| Signature | Meaning |
|-----------|---------|
| **CR**: `char = '\015'` | Carriage return character |
| **LF**: `char = '\012'` | Line feed character |
| **Any_type_name**: `String = "Any"` | Type name for any type |
| **Regex_any_pattern**: `String = ".*"` | Regular expression pattern matching any string |
| **Default_encoding**: `String = "UTF-8"` | Default character encoding |
| **None_type_name**: `String = "None"` | Type name for no type |

#### 3.2.2. OPENEHR_DEFINITIONS Class

| Aspect | Details |
|--------|---------|
| **Class** | **OPENEHR_DEFINITIONS** |
| **Description** | Inheritance class to provide access to constants defined in other packages. |
| **Inherit** | `BASIC_DEFINITIONS` |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **Local_terminology_id**: `String {default = "local"}` | Predefined terminology identifier to indicate it is local to the knowledge resource in which it occurs (e.g., an archetype) |

#### 3.2.3. VALIDITY_KIND Enumeration

| Aspect | Details |
|--------|---------|
| **Enumeration** | **VALIDITY_KIND** |
| **Description** | An enumeration of three values that may commonly occur in constraint models. Used as the type of any attribute expressing constraint on some attribute in a class in a reference model (e.g., to indicate validity of Date/Time fields). |

**Values:**

- **mandatory** — Indicates mandatory presence of something
- **optional** — Indicates optional presence of something
- **prohibited** — Indicates disallowed presence of something

#### 3.2.4. VERSION_STATUS Enumeration

| Aspect | Details |
|--------|---------|
| **Enumeration** | **VERSION_STATUS** |
| **Description** | Status of a versioned artefact, as one of a number of possible values: uncontrolled, prerelease, release, build. |

**Values:**

- **alpha** — Represents a version which is 'unstable', containing an unknown size of change with respect to its base version. Rendered as `N.M.P-alpha.B` (e.g., `2.0.1-alpha.154`)

- **beta** — Represents a version which is 'beta', containing an unknown but reducing size of change with respect to its base version. Rendered as `N.M.P-beta.B` (e.g., `2.0.1-beta.154`)

- **release_candidate** — Represents a version which is 'release candidate', containing only patch-level changes on the base version. Rendered as `N.M.P-rc.B` (e.g., `2.0.1-rc.27`)

- **released** — Represents a version which is 'released', the definitive base version. Rendered as `N.M.P` (e.g., `2.0.1`)

- **build** — Represents a version which is a build of the current base release. Rendered as `N.M.P+B` (e.g., `2.0.1+33`)

---

## 4. Builtins Package

### 4.1. Overview

The `BASE.base_types.builtins` package includes interface classes that provide common utility functions.

### 4.2. Class Definitions

#### 4.2.1. Env Interface

| Aspect | Details |
|--------|---------|
| **Interface** | **Env** |
| **Description** | Class representing the real-world environment, providing basic information like current time, date, etc. |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **current_date()**: `Iso8601_date` | Return today's date in the current locale |
| **current_time()**: `Iso8601_time` | Return current time in the current locale |
| **current_date_time()**: `Iso8601_date_time` | Return current date/time in the current locale |
| **current_time_zone()**: `Iso8601_timezone` | Return the timezone of the current locale |

#### 4.2.2. Locale Interface

| Aspect | Details |
|--------|---------|
| **Interface** | **Locale** |
| **Description** | Class representing current Locale. |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **primary_language()**: `Terminology_code` | Primary language of the current locale |

#### 4.2.3. Statistical_evaluator Interface

| Aspect | Details |
|--------|---------|
| **Interface** | **Statistical_evaluator** |
| **Description** | A basic statistical evaluator class providing common functions on collections of numbers. |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **sum(vals: Container<Numeric>)**: `Double` | Sum of a container of values |
| **avg(vals: Container<Numeric>)**: `Double` | Synonym for `mean()` |
| **mean(vals: Container<Numeric>)**: `Double` | Mean (arithmetic average) of a container of values |
| **median(vals: Container<Numeric>)**: `Numeric` | Return numerically centre value in ordered form of container contents |
| **mode(vals: Container<Numeric>)**: `Numeric` | Mode (most frequent) of a container of values |
| **max(vals: Container<Numeric>)**: `Numeric` | Maximum of a container of values |
| **min(vals: Container<Numeric>)**: `Numeric` | Minimum of a container of values |
| **count(vals: Container<Numeric>)**: `Numeric` | Return the number of items in `vals`, i.e. `vals.count` |
| **std_dev(vals: Container<Numeric>)**: `Double` | Compute standard deviation of a container of values |

#### 4.2.4. Math Interface

| Aspect | Details |
|--------|---------|
| **Interface** | **Math** |
| **Description** | Mathematical computation. |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **ln(v: Numeric)**: `Double` | Compute natural log of v |
| **log(v: Numeric)**: `Double` | Compute base 10 log of v |
| **sin(v: Numeric)**: `Double` | Compute sin(v) |

#### 4.2.5. Quantity_converter Interface

| Aspect | Details |
|--------|---------|
| **Interface** | **Quantity_converter** |
| **Description** | Quantity conversion. |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **convert_value(value: Real, from_units: String, to_units: String, property: Terminology_code)**: `Real` | Convert `value` of physical property type (e.g. 'pressure') from one units to another |

---

## 5. Identification Package

### 5.1. Overview

The `BASE.base_types.identification` package describes a model of references and identifiers for information entities.

### 5.2. Requirements

Identification of entities both in the real world and in information systems is a non-trivial problem. The needs for identification across systems in a health information environment include the following:

- Real world identifiers such as social security numbers, veterans affairs ids, etc. can be recorded as required by health care facilities, enterprise policies, or legislation

- Identifiers for informational entities which represent real world entities or processes should be unique

- It should be possible to determine if two identifiers refer to information entities that represent the same real world entity, even if instances of the information entities are maintained in different systems

- Versions or changes to real-world entity-linked informational entities (which may create new information instances) should be accounted for in two ways:
  - It should be possible to tell if two identifiers refer to distinct versions of the same informational entity in the same version tree
  - It should not be possible to confuse same-named versions of informational entities maintained in multiple systems which purport to represent the same real world entity. For example, there is no guarantee that two systems' "latest" version of the Person "Dr Jones" is the same
  - Medico-legal use of information relies on previous states of information being distinguishable from other previous states and the current state

- It should be possible for an entity in one system or service (such as the EHR) to refer to an entity in another system or service in such a way that:
  - The target of the reference is easily findable within the shared environment
  - The reference remains valid regardless of the physical architecture of servers and applications

#### 5.2.1. Identification of Real World Entities (RWEs)

Real world entities such as people, car engines, invoices, and appointments can all be assigned identifiers. Although many of these are designed to be unique within a jurisdiction, they are often not, due to:

- Data entry errors
- Bad design (identifiers that are too small or incorporate some non-unique characteristic of the identified entities)
- Bad process (e.g., non-synchronized identifier issuing points)
- Identity theft (e.g., via theft of documents of proof or hacking)

In general, while some real world identifiers (RWIs) are "nearly unique", none can be guaranteed to be so. It should be the case that if two RWE identifiers are equal, they refer to the same RWE, but this is often not the case. For practical purposes, RWIs cannot be regarded as computationally safe for making the inferences described in requirements.

#### 5.2.2. Identification of Informational Entities (IEs)

As soon as information systems are used to record facts about RWEs, the situation becomes more complex because of the intangible nature of information. In particular:

- The same RWE can be represented simultaneously on more than one system ('spatial multiplicity')
- The same RWE may be represented by more than one "version" of the same IE in a system ('temporal multiplicity')

At first sight, it appears that there can also be purely informational entities, i.e. IEs which do not refer to any RWE, such as books, online-only documents and software. However, as soon as one considers an example it becomes clear that there is always a notional 'definitive' or 'authoritative' (i.e. trusted) version of every such entity. These entities can better be understood as 'virtual RWEs'. Thus it can still be said that multiple IEs may refer to any given RWE.

The underlying reason for the multiplicity of IEs is that 'reality' - time and space - in computer systems is not continuous but discrete, and each 'entity' is in fact just a snapshot of certain attribute values of a RWE, at a point in time, in a particular system. If identifiers are assigned to IEs without regard to versions or duplicates, then no assertion can be made about the identified RWE when two IE ids are compared.

#### 5.2.3. Identification of Versions

The notion of 'versioning' applies only to informational entities, i.e. distinct instances of content each representing a snapshot of some logical entity. Where such instances are stored and managed in versioned containers within a versioning system of some kind, explicit identification of the versions is required.

Requirements can be summarized as follows:

- It must be possible to distinguish two versions of the same logical entity, i.e. know from the identifier if they are the same or different versions of the same thing

- It must be possible to distinguish two versions of the same logical entity created in two distinct systems

- It must be possible to tell the relationship between the items in a versioned lineage, from the version identifiers

#### 5.2.4. Referencing of Informational Entities

Within a distributed information environment, there is a need for entities not connected by direct references in the same memory space to be able to refer to each other. There are two competing requirements:

- That the separation of objects in a distributed computing environment not compromise the semantics of the model

- That different types of information can be managed relatively independently; for example EHR and demographic information can be managed by different groups in an organization or community, each with at least some freedom to change implementation and model details

### 5.3. Design

This package models only informational identifiers, i.e. transparent identifiers understood by openEHR or related computational systems. Real World Entity Identifiers such as driver's license numbers are modeled using the data type `DV_IDENTIFIER`. This is not to imply that such identifiers are any less systematic or well-managed than the system identifiers defined here, only that from the point of view of openEHR, they have the same status as other informational attributes such as name, address etc. of a Person.

A key design decision has been to choose a string representation for all identifiers, with subparts being made available by appropriate functions which perform simple parsing on the string. This ensures that the data representation of identifiers (e.g. in XML) is as small as possible, while not losing object-oriented typing.

#### 5.3.1. Primitive Identifiers

Three kinds of types are defined in this package. The abstract UID type and its subtypes correspond to permanent, computationally reliable, primitive identifiers. Such identifiers are regarded as 'primitive' because they are treated as having no further internal structure, in the sense that part of such an identifier is not in general meaningful. The three subtypes `UUID`, `ISO_OID` and `INTERNET_ID` all have these properties, and are commonly accepted ways of uniquely identifying entities in computer systems. In openEHR (and generally in health informatics) they are usually used as parts of other identifiers.

**Note:** UUIDs are also commonly known as GUIDs, which may be used as a synonym within implementations.

A consequence of the string representation approach used in these classes is that to set an attribute of type UID from a string value, as would be done when reading from a database, deserializing from XML or another text form, a piece of code that inspects the string structure has to be used in order to decide which of the subtypes of `UID` it is. This is a safe thing to do, since all three subtypes have mutually exclusive string patterns, and can easily be distinguished.

#### 5.3.2. Composite Identifiers

The `OBJECT_ID` type and its hierarchy of subtypes define all of the identifier types used within openEHR systems. Most of these have a multi-part structure, and some are 'meaningful' i.e. human readable. The identifier types can be used to represent identifier values that fall into two groups semantically: those defined by openEHR (which may incorporate generic standard identifiers, such as ISO Oids etc) and those defined by external organizations.

| | openEHR-defined identifiers | Externally defined identifiers |
|---|---|---|
| | `OBJECT_VERSION_ID` | `GENERIC_ID` |
| | `ARCHETYPE_ID` | `HIER_OBJECT_ID` |
| | `TERMINOLOGY_ID` | |
| | `HIER_OBJECT_ID` | |

##### 5.3.2.1. UID-based Identifiers

The abstract type `UID_BASED_ID` and its two subtypes `HIER_OBJECT_ID` and `OBJECT_VERSION_ID` provide respectively, UID-based identifiers for non-versioned and versioned items. The design of the latter subtype is explained in the openEHR Common IM, change_control package.

##### 5.3.2.2. Archetype Identifiers

The `ARCHETYPE_ID` subtype defines a multi-axial identifier for archetypes, meaning that each identifier instance denotes a single archetype within a multi-dimensional space. The space can be thought of as 3-dimensional, or as a versioned 2-dimensional space, consisting of the following axes:

- Reference model entity, i.e. target of archetype, defined as:
  - Name of model issuer
  - Name of model (there may be more than one from the same issuer)
  - Name of concept in model, i.e. class name

- Domain concept

- Version

The three outer sections are delimited by '.' characters, while the parts of the first section are delimited by '-' characters. As with any multi-axial identifier, the underlying principle of an archetype identifier is that all parts of the identifier must be able to be considered immutable. This means that no variable characteristic of an archetype (e.g. accrediting authority, which might change due to later accreditation by another authority, or may be multiple) can be included in its identifier. The explicit inclusion of version as part of the identifier means that two 'versions' of an archetype are actually two distinct archetypes.

**Examples of archetype identifiers:**

- `openEHR-EHR-SECTION.physical_examination.v2`
- `openEHR-EHR-SECTION.physical_examination-prenatal.v1`
- `Hl7-RIM-Act.progress_note.v1`
- `openEHR-EHR-OBSERVATION.progress_note-naturopathy.v2`

**Warning:** Some archetype authoring tools have historically allowed a nonconforming version part within archetype identifiers which included the lifecycle status. This has led to some archetypes having an identifier whose version part is of the form `.v1draft` or similar. The openEHR Foundation will publish guidelines and a timeline on its website for dealing with this problem. New and existing archetype tools may have to support this exception, depending on where they are to be used, and it is recommended that it at least be supported via a command line switch or option. Where such non-conforming archetypes are re-used within a new environment, the identifier should be corrected.

##### 5.3.2.3. Terminology Identifiers

The `TERMINOLOGY_ID` subtype defines a globally unique single string identifier for terminologies. Terminology identifier values may include a version, either as part of the name, and/or according to the syntax defined below.

**Examples of terminology identifiers:**

- "SNOMED-CT"
- "ICD9(1999)"

Currently the best authoritative source for the name part of the identifier (i.e. the part excluding the optional version part in parentheses) is the US National Library of Medicine UMLS identifiers for included terminologies.

The scheme defined by the `TERMINOLOGY_ID` class provides for the situation where major 'versions' of a terminology such as the World Health Organisation's 'ICD10' and 'ICD10AM' (AM = 'Australian modifications') can accommodate a finer grain of versioning or revisioning, e.g.:

- "ICD10AM(3rd_ed)"
- "ICD10AM(4th_ed)"

The version part of a terminology identifier is in theory only absolutely necessary for those terminologies which break the rule that the concept being identified with a code loses or changes its meaning over versions of the terminology. This should not be the case for modern terminologies and ontologies, particularly those designed since the publication of Cimino's 'desiderata' of which the principle of 'concept permanence' is applicable here - "A concept's meaning cannot change and it cannot be deleted from the vocabulary". However, there may be older terminologies, or specialized terminologies which may not have obeyed these rules, but which are still used; version ids should always be used for these. At a practical level, versions may be included routinely in some systems to support the potential medico-legal need to prove that a) a given code was in fact defined in the terminology (it may not have existed in an earlier edition) and b) that the meaning assumed in the system was indeed the one assigned to it in the particular version or edition.

##### 5.3.2.4. Equivalence

Although there are anomalies in some published terminologies and between some versions or editions of the same terminology, two terminology identifiers that are the same, disregarding the version part, can usually be considered as semantic equivalents in the terminology world. However, depending on which source of strings have been chosen for the name part of the identifier, two different identifiers may also indicate the same terminology, e.g. "ICD10AM_2000" (NLM identifier used in UMLS) and "ICD10AM(2nd_ed)" refer to the same thing.

##### 5.3.2.5. Identifying Versions within openEHR Versioned Containers

The `OBJECT_VERSION_ID` defines the semantics of the scheme used in openEHR for identifying versions within a versioned container, and uses a three-part identifier, consisting of:

- `object_id`: the identifier of the version container, in the form of a UID, typically a UUID
- `creating_system_id`: the identifier of the system in which this version was created, of type UID, typically a reverse domain identifier
- `version_tree_id`: the location in the version tree, as a 1- or 3-part numeric identifier, where the latter variant expresses branching; this is modeled using the `VERSION_TREE_ID` type

**Typical example:**

```
87284370-2D4B-4e3d-A3F3-F303D2F4F34B::uk.nhs.ehr1::2
```

Under this scheme, multiple versions in the same container all have the same value for `object_id`, whilst their location in the version tree is given by the combination of the version tree identifier and the identifier of the creating system.

The requirements on the `creating_system_id` part of the identifier are that it be unique per system, and that it be easy to obtain or generate. It is also helpful if it is a meaningful identifier. The two most practical candidates appear to be:

- UUIDs (which are not meaningful, but are easy to generate)
- Reverse internet domain identifiers (these are easy to determine if the system has an internet address, and are meaningful and directly processible, however unconnected systems pose a problem)

ISO Oids might also be used. All of these identifier types are accommodated via the use of UID. A full explanation of the version identification scheme and its capabilities is given in the Common IM, change_control package.

##### 5.3.2.6. Generic and External Identifiers

The `GENERIC_ID` type provides for identifiers of schemes other than defined concretely in the `BASE.base_types.identification` package. It has a single method scheme, which may be used to record the identifier type. The names of schemes are not currently controlled.

##### 5.3.2.7. Hierarchical Identifiers

The `HIER_OBJECT_ID` type is defined to support hierarchical identifiers, often based on UUIDs or other similar machine-readable and machine-resolvable schemes.

##### 5.3.2.8. Composite Identifiers and Case

All composite identifiers should follow two rules with regard to case, namely:

- To be case-preserving — not change case due to persistence, copying, transfer or other computation processes
- To be case-insensitive — two identifiers identical apart from case are considered to be identical, and therefore to identify the same thing

The practical consequences of these rules are as follows:

- Mixed-case identifiers may be used, such as archetype identifiers, mixed-case reverse domain identifiers (the `INTERNET_ID` type)
- The original case chosen in the letters of identifiers on creation within an openEHR system should be as published by the relevant issuing organization (e.g. NLM UMLS terminology names are all upper case)
- If identifiers are used as part of filenames within computer file systems, care must be taken to create and preserve filenames correctly. For this reason, software usually has to handle filename creation and modification differently on Unix-style operating systems, which are case-sensitive (and therefore case-preserving), and Windows-style operating systems, which are case-insensitive but usually case-preserving

These rules do not apply to any identifier constructed in a language in which case does not exist as a concept. For this reason, for identifiers translated in and out of the Turkish language (and possibly in smaller related languages), care must be taken with the 'I/i' characters.

##### 5.3.2.9. Composite Identifiers and Language

In all of the 'meaningful' identifier types above, with the possible exception of `GENERIC_ID`, the human-readable identifier sections are assumed to use only the basic Latin character set, possibly with the addition of other special characters as allowed by the production rules defined below for each identifier. In most cases, the textual parts of these identifiers will be words from the English language, or else they will be recognizable words from other languages, where necessary alliterated into the Latin alphabet. Accented and other diacritical letter variants are not allowed. This limitation is made in the interests of practical computability of identifiers, and is in common with class and attribute naming in shared UML models in the standards world, and also with internet domain names and internet URIs.

#### 5.3.3. References

All `OBJECT_IDs` are used as identifier attributes within the thing they identify, in the same way as a database primary key. To refer to an identified object from another object, an instance of the class `OBJECT_REF` should generally be used, in the same way as a database foreign key. The class `OBJECT_REF` is provided as a means of distributed referencing, and includes the object namespace (typically 1:1 with some service, such as "terminology") and type. The general principle of object references is to be able to refer to an object available in a particular namespace or service. Usually they are used to refer to objects in other services, such as a demographic entity from within an EHR, but they may be used to refer to local objects as well. The type may be the concrete type of the referred-to object (e.g. "GP") or any proper ancestor (e.g. `PARTY`).

### 5.4. Class Descriptions

#### 5.4.1. UID Class

| Aspect | Details |
|--------|---------|
| **Class** | **_UID (abstract)_** |
| **Description** | Abstract parent of classes representing unique identifiers which identify information entities in a durable way. UIDs only ever identify one IE in time or space and are never re-used. |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **value**: `String` | The value of the id |

**Invariants:**

- `Value_valid`: `not value.empty`

#### 5.4.2. ISO_OID Class

| Aspect | Details |
|--------|---------|
| **Class** | **ISO_OID** |
| **Description** | Model of ISO's Object Identifier (oid) as defined by the standard ISO/IEC 8824. Oids are formed from integers separated by dots. Each non-leaf node in an Oid starting from the left corresponds to an assigning authority, and identifies that authority's namespace, inside which the remaining part of the identifier is locally unique. |
| **Inherit** | `UID` |

#### 5.4.3. UUID Class

| Aspect | Details |
|--------|---------|
| **Class** | **UUID** |
| **Description** | Model of the DCE Universal Unique Identifier or UUID which takes the form of hexadecimal integers separated by hyphens, following the pattern 8-4-4-4-12 as defined by the Open Group, CDE 1.1 Remote Procedure Call specification, Appendix A. Also known as a GUID. |
| **Inherit** | `UID` |

#### 5.4.4. INTERNET_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **INTERNET_ID** |
| **Description** | Model of a reverse internet domain, as used to uniquely identify an internet domain. In the form of a dot-separated string in the reverse order of a domain name, specified by IETF RFC 1034. |
| **Inherit** | `UID` |

#### 5.4.5. OBJECT_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **_OBJECT_ID (abstract)_** |
| **Description** | Ancestor class of identifiers of informational objects. Ids may be completely meaningless, in which case their only job is to refer to something, or may carry some information to do with the identified object. Object ids are used inside an object to identify that object. To identify another object in another service, use an `OBJECT_REF`, or else use a UID for local objects identified by UID. If none of the subtypes is suitable, direct instances of this class may be used. |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **value**: `String` | The value of the id in the form defined below |

#### 5.4.6. UID_BASED_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **_UID_BASED_ID (abstract)_** |
| **Description** | Abstract model of UID-based identifiers consisting of a root part and an optional extension; lexical form: `root '::' extension`. |
| **Inherit** | `OBJECT_ID` |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **root()**: `UID` | The identifier of the conceptual namespace in which the object exists, within the identification scheme. Returns the part to the left of the first '::' separator, if any, or else the whole string. |
| **extension()**: `String` | Optional local identifier of the object within the context of the root identifier. Returns the part to the right of the first '::' separator if any, or else an empty String. |
| **has_extension()**: `Boolean` | True if not `extension.is_empty()`. |

**Invariants:**

- `Has_extension_valid`: `extension.is_empty xor has_extension`

#### 5.4.7. HIER_OBJECT_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **HIER_OBJECT_ID** |
| **Description** | Concrete type corresponding to hierarchical identifiers of the form defined by `UID_BASED_ID`. |
| **Inherit** | `UID_BASED_ID` |

#### 5.4.8. OBJECT_VERSION_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **OBJECT_VERSION_ID** |
| **Description** | Globally unique identifier for one version of a versioned object; lexical form: `object_id '::' creating_system_id '::' version_tree_id`. |
| **Inherit** | `UID_BASED_ID` |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **object_id()**: `UID` | Unique identifier for logical object of which this identifier identifies one version; normally the `object_id` will be the unique identifier of the version container containing the version referred to by this `OBJECT_VERSION_ID` instance. |
| **creating_system_id()**: `UID` | Identifier of the system that created the Version corresponding to this Object version id. |
| **version_tree_id()**: `VERSION_TREE_ID` | Tree identifier of this version with respect to other versions in the same version tree, as either 1 or 3 part dot-separated numbers, e.g. 1, 2.1.4. |
| **is_branch()**: `Boolean` | True if this version identifier represents a branch. |

#### 5.4.9. VERSION_TREE_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **VERSION_TREE_ID** |
| **Description** | Version tree identifier for one version. Lexical form: `trunk_version [ '.' branch_number '.' branch_version ]` |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **value**: `String` | String form of this identifier |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **trunk_version()**: `String` | Trunk version number; numbering starts at 1 |
| **is_branch()**: `Boolean` | True if this version identifier represents a branch, i.e. has branch_number and branch_version parts |
| **branch_number()**: `String` | Number of branch from the trunk point; numbering starts at 1 |
| **branch_version()**: `String` | Version of the branch; numbering starts at 1 |

**Invariants:**

- `Value_valid`: `not value.is_empty`
- `Trunk_version_valid`: `trunk_version /= Void and then trunk_version.is_integer and then trunk_version.as_integer >= 1`
- `Branch_number_valid`: `branch_number /= Void implies branch_number.is_integer and then branch_number.as_integer >= 1`
- `Branch_version_valid`: `branch_version /= Void implies branch_version.is_integer and then branch_version.as_integer >= 1`
- `Branch_validity`: `(branch_number = Void and branch_version = Void ) xor (branch_number /= Void and branch_version /= Void )`
- `Is_branch_validity`: `is_branch xor branch_number = Void`
- `Is_first_validity`: `not is_first xor trunk_version.is_equal("1")`

#### 5.4.10. ARCHETYPE_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **ARCHETYPE_ID** |
| **Description** | Identifier for archetypes. Ideally these would identify globally unique archetypes. Lexical form: `rm_originator '-' rm_name '-' rm_entity '.' concept_name { '-' specialisation }* '.v' number`. |
| **Inherit** | `OBJECT_ID` |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **qualified_rm_entity()**: `String` | Globally qualified reference model entity, e.g. `openehr-EHR-OBSERVATION` |
| **domain_concept()**: `String` | Name of the concept represented by this archetype, including specialization, e.g. `Biochemistry_result-cholesterol` |
| **rm_originator()**: `String` | Organization originating the reference model on which this archetype is based, e.g. openehr, cen, hl7 |
| **rm_name()**: `String` | Name of the reference model, e.g. rim, ehr_rm, en13606 |
| **rm_entity()**: `String` | Name of the ontological level within the reference model to which this archetype is targeted, e.g. for openEHR, folder, composition, section, entry |
| **specialisation()**: `String` | Name of specialization of concept, if this archetype is a specialization of another archetype, e.g. cholesterol |
| **version_id()**: `String` | Version of this archetype |

#### 5.4.11. TEMPLATE_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **TEMPLATE_ID** |
| **Description** | Identifier for templates. Lexical form to be determined. |
| **Inherit** | `OBJECT_ID` |

#### 5.4.12. TERMINOLOGY_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **TERMINOLOGY_ID** |
| **Description** | Identifier for terminologies such as accessed via a terminology query service. In this class, the value attribute identifies the Terminology in the terminology service, e.g. SNOMED-CT. A terminology is assumed to be in a particular language, which must be explicitly specified. The value of the id attribute is the precise terminology id identifier, including actual release (i.e. actual version), local modifications etc; e.g. ICPC2. Lexical form: `name [ '(' version ')' ]`. |
| **Inherit** | `OBJECT_ID` |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **name()**: `String` | Return the terminology id (which includes the version in some cases). Distinct names correspond to distinct (i.e. non-compatible) terminologies. Thus the names ICD10AM and ICD10 refer to distinct terminologies. |
| **version_id()**: `String` | Version of this terminology, if versioning supported, else the empty string |

#### 5.4.13. GENERIC_ID Class

| Aspect | Details |
|--------|---------|
| **Class** | **GENERIC_ID** |
| **Description** | Generic identifier type for identifiers whose format is otherwise unknown to openEHR. Includes an attribute for naming the identification scheme (which may well be local). |
| **Inherit** | `OBJECT_ID` |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **scheme**: `String` | Name of the scheme to which this identifier conforms. Ideally this name will be recognizable globally but realistically it may be a local ad hoc scheme whose name is not controlled or standardized in any way. |

#### 5.4.14. OBJECT_REF Class

| Aspect | Details |
|--------|---------|
| **Class** | **OBJECT_REF** |
| **Description** | Class describing a reference to another object, which may exist locally or be maintained outside the current namespace, e.g. in another service. Services are usually external, e.g. available in a LAN (including on the same host) or the internet via Corba, SOAP, or some other distributed protocol. However, in small systems they may be part of the same executable as the data containing the Id. |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **namespace**: `String` | Namespace to which this identifier belongs in the local system context (and possibly in any other openEHR compliant environment) e.g. terminology, demographic. These names are not yet standardized. Legal values for `namespace` are: `"local"`, `"unknown"`, or a string matching the standard regex `[a-zA-Z][a-zA-Z0-9_.:\/&?=+-]*`. Note that the first two are just special values of the regex, and will be matched by it. |
| **type**: `String` | Name of the class (concrete or abstract) of object to which this identifier type refers, e.g. `PARTY`, `PERSON`, `GUIDELINE` etc. These class names are from the relevant reference model. The type name `ANY` can be used to indicate that any type is accepted (e.g. if the type is unknown). |
| **id**: `OBJECT_ID` | Globally unique id of an object, regardless of where it is stored |

#### 5.4.15. PARTY_REF Class

| Aspect | Details |
|--------|---------|
| **Class** | **PARTY_REF** |
| **Description** | Identifier for parties in a demographic or identity service. There are typically a number of subtypes of the `PARTY` class, including `PERSON`, `ORGANISATION`, etc. Abstract supertypes are allowed if the referenced object is of a type not known by the current implementation of this class (in other words, if the demographic model is changed by the addition of a new `PARTY` or `ACTOR` subtypes, valid `PARTY_REFs` can still be constructed to them). |
| **Inherit** | `OBJECT_REF` |

**Invariants:**

- `Type_validity`: `type.is_equal("PERSON") or type.is_equal("ORGANISATION") or type.is_equal("GROUP") or type.is_equal("AGENT") or type.is_equal("ROLE") or type.is_equal("PARTY") or type.is_equal("ACTOR")`

#### 5.4.16. LOCATABLE_REF Class

| Aspect | Details |
|--------|---------|
| **Class** | **LOCATABLE_REF** |
| **Description** | Reference to a `LOCATABLE` instance inside the top-level content structure inside a `VERSION<T>`; the path attribute is applied to the object that `VERSION._data_` points to. |
| **Inherit** | `OBJECT_REF` |

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| **path**: `String` | The path to an instance in question, as an absolute path with respect to the object found at `VERSION._data_`. An empty path means that the object referred to by id being specified. |
| **id**: `UID_BASED_ID` (redefined) | Globally unique id of an object, regardless of where it is stored |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| **as_uri()**: `String` | A URI form of the reference, created by concatenating: scheme (e.g. `ehr:`, derived from `namespace`); `id.value`; `/` + `path`, where `path` is non-empty |

---

## 5.5. Syntaxes

The identifiers defined above are defined in their string form by the following EBNF grammar rules.

```ebnf
(* UID, OID, UUID *)
uid     = iso_oid | uuid | internet_id ;
iso_oid = number, { '.', number } ;
uuid    = hex-number, '-', hex-number, '-', hex-number, '-', hex-number, '-', hex-number ;

(* INTERNET_ID *)
(* According to IETF RFC 1034 and RFC 1035, as clarified by RFC 2181 *)
(* (section 11), and relaxation of RFC 1123 *)
(* The syntax of a domain name follows the grammar below. Slightly *)
(* reduced for the purpose here, plus allows underscores. *)
internet_id      = subdomain ;
subdomain        = label | subdomain, '.', label ;
label            = alphanum | alphanum-ext-str, alphanum ;

(* HIER_BASED_ID, UID_BASED_ID *)
hier_object_id = uid_based_id ;
uid_based_id   = root, [ '::', extension ] ;
root           = uid ;
extension      = ? any string ? ; (* any string *)

(* OBJECT_VERSION_ID *)
object_version_id  = object_id, '::', creating_system_id, '::', version_tree_id ;
object_id          = uid ;
creating_system_id = uid ;

(* VERSION_TREE_ID *)
version_tree_id = trunk_version, [ '.', branch_number, '.', branch_version ] ;
trunk_version   = number ;
branch_number   = number ;
branch_version  = number ;

(* ARCHETYPE_ID *)
archetype_id        = qualified_rm_entity, '.', domain_concept, '.', version_id ;
qualified-rm-entity = rm_originator, '-', rm_name, '-', rm_entity ;
rm-originator       = alphanum-str ;     (* id of org originating the RM on which this archetype is based *)
rm-name             = alphanum-str ;                      (* id of the RM on which the archetype is based *)
rm-entity           = alphanum-str ;                                       (* ontological level in the RM *)
domain-concept      = concept-name, { '-', specialisation } ;
concept-name        = alphanum-str ;
specialisation      = alphanum-str ;
version-id          = 'v', ( '0' | non-zero-digit, [ number ] ) ;            (* numeric version identifier *)

(* TERMINOLOGY_ID *)
terminology_id = name-str, [ '(', name-str, ')' ] ;

(* generic rules *)
alphanum     = letter | digit ;
name-str     = letter, { letter | digit | '_' | '-' | '/' | '+' } ;
alphanum-str = letter, { letter | digit | '_' } ;
alphanum-ext-str = letter, { letter | digit | '_' | '-' } ;
letter       = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G'
             | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N'
             | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U'
             | 'V' | 'W' | 'X' | 'Y' | 'Z' | 'a' | 'b'
             | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i'
             | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p'
             | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w'
             | 'x' | 'y' | 'z' ;

number         = digit, { digit } ;
hex-number     = hex-digit, { hex-digit } ;
digit          = '0' | non-zero-digit ;
non-zero-digit = '1' | '2' | '3' | '4' | '5' | '6' | '7'| '8' | '9' ;
hex-digit      = digit | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' ;
```

---

**Last updated:** 2020-11-02 15:52:49 UTC

**Source URL**: https://specifications.openehr.org/releases/BASE/latest/base_types.html
