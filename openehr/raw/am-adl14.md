# Archetype Definition Language 1.4 (ADL1.4) Specification

**Document Status:** STABLE
**Release:** AM Release-2.3.0
**Date:** Latest Issue
**Keywords:** EHR, ADL, AOM, health records, archetypes, constraint language, ISO 13606, openehr

---

## Table of Contents

1. [Preface](#preface)
2. [Overview](#overview)
3. [File Encoding and Character Quoting](#file-encoding)
4. [dADL - Data ADL](#dadl)
5. [cADL - Constraint ADL](#cadl)
6. [Assertions](#assertions)
7. [ADL Paths](#adl-paths)
8. [ADL - Archetype Definition Language](#adl)
9. [Customising ADL](#customising)
10. [Appendices](#appendices)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| 1.4.6 | SPECAM-84: Fix typographical errors in AOM, ADL 1.4 | R Kavanagh | 03 Apr 2023 |
| 1.4.5 | SPECAM-75: Improve constraint pattern specification; modified Section 5.4.6.1 for timezone constraints | P Pazos, T Beale | 20 Dec 2022 |
| 1.4.4 | SPECAM-69: Support negative durations; add examples in Section 5.4.6.2 | P Bos, S Garde | 09 Sep 2020 |
| 1.4.3 | SPECPUB-7: Convert citations to bibtex form | T Beale | 15 Dec 2019 |
| 1.4.2 | SPECAM-24: Standardise governance meta-data structure; added appendix for extension meta-data | S Garde, et al. | 22 May 2016 |
| 1.4.1 | SPEC-268: Correct missing parentheses in dADL type identifiers | R Chen | 12 Dec 2008 |
| 1.4.0 | Multiple improvements to Release 1.0 specifications | T Beale, S Heard | 13 Mar 2007 |

---

## Acknowledgements

### Primary Author
- Thomas Beale, Ocean Informatics UK; openEHR Architecture Review Board (ARB)

### Contributors
- Sebastian Garde, Central Queensland University, Australia (German translations)

### Trademarks
- Microsoft and .Net are registered trademarks of Microsoft Corporation
- Java is a registered trademark of Oracle Corporation
- Linux is a registered trademark of Linus Torvalds
- openEHR is a registered trademark of The openEHR Foundation
- SNOMED CT is a registered trademark of IHTSDO

### Supporters
- UCL (University College London) - Centre for Health Informatics and Multiprofessional Education (CHIME)
- Ocean Informatics

---

## Preface {#preface}

### Purpose

This specification describes the design basis and syntax of Archetype Definition Language 1.4 (ADL 1.4). The audience includes software developers, technically-oriented domain specialists, and subject matter experts. ADL is designed as an abstract human-readable and computer-processible syntax that can be hand-edited using a normal text editor.

### Related Documents

**Prerequisite Documents:**
- openEHR Architecture Overview
- openEHR Archetype Technical Overview

**Related Documents:**
- openEHR Archetype Object Model (AOM14)

### Nomenclature

The term 'attribute' denotes any stored property of a type defined in an object model, including primitive attributes and relationships such as associations or aggregations. XML attributes are always referred to explicitly as 'XML attributes'.

### Status

This specification is in the STABLE state. Development versions are available at [https://specifications.openehr.org/releases/AM/latest/ADL1.4.html](https://specifications.openehr.org/releases/AM/latest/ADL1.4.html).

**Note:** This is a re-formatted issue of the original ADL 1.4 Specification from openEHR Release 1.0.2 with updated citations, reference corrections, and typographical fixes.

**Important:** Users requiring the most recent archetype technology should consult the Archetype Definition Language 2 (ADL2) specifications, particularly the Archetype Technology Overview.

### Feedback

- **Forum:** openEHR ADL forum (discourse.openehr.org)
- **Issues:** Problem Report tracker at specifications.openehr.org
- **Changes:** AM component Change Request tracker

### Conformance

Conformance to openEHR specifications is determined by formal testing against Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. These are formal derivations from underlying models.

### Tools

- ADL Workbench - reference compiler, visualiser, and editor
- Tools available at openehr.org/downloads
- Source code available at github.com/openEHR

---

## Overview {#overview}

### What is ADL?

Archetype Definition Language (ADL) is a formal language for expressing archetypes—constraint-based models of domain entities or structured business rules. The Archetype Object Model 1.4 defines archetype semantics as a formal object model. ADL syntax represents one possible serialisation of an archetype.

The openEHR archetype framework is described in "Archetype Definitions and Principles" and an "Archetype System." ADL uses three syntaxes:
- **cADL** - constraint form
- **dADL** - data definition form
- **First-order predicate logic** - assertion expressions

#### Structure

Archetypes in ADL resemble programming language files with defined syntax. The main structure includes:

1. **Header sections** - metadata and language information
2. **Definition section** - cADL constraints
3. **Invariant section** - assertions
4. **Ontology section** - term definitions and bindings
5. **Revision history section** - version tracking

#### Example Archetype

```adl
archetype (adl_version=1.4)
    adl-test-instrument.guitar.draft.v1

concept
    [at0000]

language
    original_language = <[iso_639-1::en]>

definition
    INSTRUMENT[at0000] matches {
        size matches {|60..120|}                     -- size in cm
        date_of_manufacture matches {yyyy-mm-??}    -- year & month ok
        parts cardinality matches {0..*} matches {
            PART[at0001] matches {                   -- neck
                material matches {[local::at0003, at0004]}
            }
            PART[at0002] matches {                   -- body
                material matches {[local::at0003]}
            }
        }
    }

ontology
    term_definitions = <
        ["en"] = <
            items = <
                ["at0000"] = <
                    text = <"guitar">;
                    description = <"stringed instrument">
                >
            >
        >
    >
```

#### Semantics

ADL documents parse into networks of objects (parse trees) defined by the Archetype Object Model. This abstract model can be re-expressed in concrete forms such as programming languages, XML schemas, or OMG IDL. While ADL is the primary formalism, the AOM defines the definitive semantic model.

### Computational Context

Archetypes sit between lower-level knowledge resources (clinical terminologies and ontologies) and production system data. Their primary purpose is providing reusable, interoperable ways to manage generic data conforming to particular structures and semantic constraints.

Archetypes are applied to data via **templates**, which generally correspond to screen forms and may be reusable locally or regionally. A third artifact—the local **palette**—specifies which languages and terminologies are in use, removing irrelevant languages and terminology bindings from archetypes.

### XML Form of Archetypes

ADL parsing tools can convert ADL to various XML formats. XML instances can be generated from in-memory archetype objects. An XML schema corresponding to the ADL Object Model is published at openEHR.org.

### Changes from Previous Versions

#### Version 1.4 from Version 1.3

**ISO 8601 Date/Time Conformance:** All ISO 8601 date, time, date/time, and duration values in dADL are now fully conformant. Constraint patterns in cADL for dates, times, and date/times are corrected, with new constraint patterns for ISO 8601 durations (allowing 'W' specifier for medicine use cases).

**Non-inclusive Two-sided Intervals:** Intervals can now exclude one or both limits:
```
|0..<1000|     -- 0 >= x < 1000
|>0.5..4.0|    -- 0.5 > x <= 4.0
|>P2d..<P10d|  -- 2 days > x < 10 days
```

**Occurrences for 'use_node' References:** Occurrences can now be stated for `use_node` references, overriding the target node's occurrences value.

**Quoting Rules:** Old quoting rules based on XML/ISO mnemonic patterns are replaced with UTF-8 encoding. Exceptions use `\Uhhhh` style Unicode quoting.

#### Version 1.3 from Version 1.2

**Query Syntax Replaced by URI Data Type:** The old query syntax:
```
attr_name = <query("service", "query_string")>
```
is now replaced by URIs:
```
attr_name = <http://some.service.org?query%20string>
```

**Top-level Invariant Section:** Invariants can now only be defined in a top-level block, simplifying ADL and making archetypes more comprehensible as type definitions.

#### Version 1.2 from Version 1.1

**ADL Version Indicator:** The ADL version is optionally included in the first line:
```
archetype (adl_version=1.2)
```

Tool implementors are strongly encouraged to include this information for more reliable processing.

**dADL Syntax Changes:** Container attribute syntax was restructured for clarity. Old form:
```
school_schedule = <
    locations(1) = <...>
    locations(2) = <...>
>
```
became:
```
school_schedule = <
    locations = <
        [1] = <...>
        [2] = <...>
    >
>
```

**Revision History Section:** Moved to a separate section at the end of archetypes for logical separation and easier automatic processing.

**Language Section Changes:** The `primary_language` attribute in the ontology section was renamed to `original_language` and moved to a new top-level `language` section. The `languages_available` attribute was renamed to `translations`.

---

## File Encoding and Character Quoting {#file-encoding}

### File Encoding

ADL files are assumed to be in UTF-8 encoding of Unicode due to likely multiple language content from internationalized authoring and translation. Three locations in ADL files may contain non-ASCII characters:

1. String values (demarcated by double quotes)
2. Regular expression patterns (demarcated by `//` or `^^`)
3. Character values (demarcated by single quotes)

URIs are percent-encoded according to IETF RFC 3986. The unreserved set includes:
```
ALPHA / DIGIT / "-" / "." / "_" / "~"
```

While UTF-8 is the officially designated encoding, real software may be more tolerant. The official specification requires tool support for UTF-8 only; supporting other encodings is optional.

### Special Character Sequences

In strings and characters, characters outside the lower ASCII (0-127) range should be UTF-8 encoded, except for quoted special characters:

| Sequence | Meaning |
|----------|---------|
| `\r` | Carriage return |
| `\n` | Linefeed |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Literal double quote |
| `\'` | Literal single quote |

Any other backslash combination is illegal; use `\\` for literal backslashes.

In regular expressions, backslash-escaped characters follow PERL regular expression specifications and should be treated as literal strings, processed by a regex parser.

---

## dADL - Data ADL {#dadl}

### Overview

The dADL syntax provides formal means of expressing instance data based on underlying object-oriented or relational information models. It is readable by both humans and machines.

**Example:**
```
person = (List<PERSON>) <
    [01234] = <
        name = <
            forenames = <"Sherlock">
            family_name = <"Holmes">
            salutation = <"Mr">
        >
        address = <
            habitation_number = <"221B">
            street_name = <"Baker St">
            city = <"London">
            country = <"England">
        >
    >
    [01235] = < -- etc >
>
```

dADL is designed to represent data in a human-readable and machine-processable way while making minimal assumptions about information models. Type names are optional; often only attribute names and values are shown.

### Basics

#### Scope of a dADL Document

A dADL document may contain one or more objects from the same object model.

#### Keywords

dADL has no keywords; all identifiers come from an information model.

#### Reserved Characters

| Character | Meaning |
|-----------|---------|
| `<` | Open object block |
| `>` | Close object block |
| `=` | Attribute value = object block |
| `(`, `)` | Type name or plug-in syntax delimiters |
| `<#`, `#>` | Plug-in syntax delimiters |
| `"` | String delimiters |
| `'` | Character delimiters |
| `\|` | Interval delimiters |
| `[]` | Coded term delimiters |

#### Comments

Comments are indicated by `--`. Multi-line comments use `--` on each line:

```
person = <
    name = <"John"> -- person's name
    age = <25>      -- person's age
>
```

#### Information Model Identifiers

**Type names:** Initial uppercase letter followed by letters, digits, and underscores. Generic type names may include commas and angle brackets (UML-style).

**Attribute names:** Initial lowercase letter followed by letters, digits, and underscores.

Common conventions:
- Type names in uppercase (e.g., `PERSON`); built-in types in mixed case (e.g., `List<T>`)
- Attribute names in lowercase (e.g., `home_address`)
- Underscores for word breaks

Alternative: "camelCase" convention (e.g., `Person`, `homeAddress`)

#### Semi-colons

Semi-colons separate dADL blocks. They are completely optional and make no semantic difference:

```
-- All equivalent:
term = <text = <"plan">; description = <"The clinician's advice">>
term = <text = <"plan"> description = <"The clinician's advice">>
term = <
    text = <"plan">
    description = <"The clinician's advice">
>
```

### Paths

dADL data is hierarchical with all nodes uniquely identified. Reliable paths can be determined for every node. The standard ADL path syntax (Section 7) applies. Paths are directly convertible to XPath expressions for XML-encoded data.

**Example path:**
```
/term_definitions["en"]/items["at0001"]/text
```

### Structure

#### General Form

A dADL document expresses serialised instances of one or more complex objects. The basic pattern is:

```
attribute_name = < value >
```

Where values are either primitive type literals or nested attribute/value pairs:

```
attr_1 = <
    attr_2 = <
        attr_3 = <leaf_value>
        attr_4 = <leaf_value>
    >
    attr_5 = <
        attr_3 = <
            attr_6 = <leaf_value>
        >
        attr_7 = <leaf_value>
    >
>
attr_8 = <...>
```

Each `<>` pair encloses an object instance. Hierarchical structure corresponds to composition/aggregation relationships.

##### Outer Delimiters

The outermost delimiters can be omitted for readability:

```
-- With outer delimiters:
<
    attr_1 = < >
    attr_8 = < >
>

-- Without outer delimiters (also valid):
attr_1 = < >
attr_8 = < >
```

**Outer `<>` delimiters in a dADL text are optional.**

##### Paths

Example paths from the above structure:
```
/attr_1
/attr_1/attr_2
/attr_1/attr_2/attr_3          -- path to leaf value
/attr_1/attr_2/attr_4          -- path to leaf value
/attr_1/attr_5
/attr_1/attr_5/attr_3
/attr_1/attr_5/attr_3/attr_6   -- path to leaf value
/attr_1/attr_5/attr_7          -- path to leaf value
/attr_8
```

#### Empty Sections

Empty sections are allowed at internal and leaf levels, indicating no data for an attribute while showing it's expected in the information model:

```
address = <...>    -- person's address
```

Nested empty sections are valid.

#### Container Objects

Container attributes (lists, sets, hash tables) can be expressed two ways:

**1. List-style leaf values:**
```
fruits = <"pear", "cumquat", "peach">
some_primes = <1, 2, 3, 5>
```

**2. Container member keys (for non-primitive values):**
```
people = <
    [1] = <name = <...> birth_date = <...> interests = <...> >
    [2] = <name = <...> birth_date = <...> interests = <...> >
    [3] = <name = <...> birth_date = <...> interests = <...> >
>
```

Keys can be strings, dates, or other comparable values:

```
people = <
    ["akmal:1975-04-22"] = <name = <...> birth_date = <...> >
    ["akmal:1962-02-11"] = <name = <...> birth_date = <...> >
    ["gianni:1978-11-30"] = <name = <...> birth_date = <...> >
>
```

**Complex example:**
```
school_schedule = <
    lesson_times = <08:30:00, 09:30:00, 10:30:00>

    locations = <
        [1] = <"under the big plane tree">
        [2] = <"under the north arch">
        [3] = <"in a garden">
    >

    subjects = <
        ["philosophy:plato"] = <
            name = <"philosophy">
            teacher = <"plato">
            topics = <"meta-physics", "natural science">
            weighting = <76%>
        >
        ["philosophy:kant"] = <
            name = <"philosophy">
            teacher = <"kant">
            topics = <"meaning and reason", "meta-physics", "ethics">
            weighting = <80%>
        >
        ["art"] = <
            name = <"art">
            teacher = <"goya">
            topics = <"technique", "portraiture", "satire">
            weighting = <78%>
        >
    >
>
```

##### Container Paths

```
/school_schedule/locations[1]                   -- "under the big..."
/school_schedule/subjects["philosophy:kant"]    -- kant's subject
```

#### Nested Container Objects

Nested container types (e.g., `List<List<Message>>`) are expressed systematically:

```
list_of_string_lists = <
    [1] = <
        [1] = <"first string in first list">
        [2] = <"second string in first list">
    >
    [2] = <
        [1] = <"first string in second list">
        [2] = <"second string in second list">
        [3] = <"third string in second list">
    >
    [3] = <
        [1] = <"only string in third list">
    >
>
```

##### Nested Container Paths

```
/list_of_string_lists[1]/[1]
/list_of_string_lists[1]/[2]
/list_of_string_lists[2]/[1]
```

#### Adding Type Information

Type information can be added using C-style type casting syntax. This is particularly useful for complex data structures:

```
destinations = <
    ["seville"] = (TOURIST_DESTINATION) <
        profile = (DESTINATION_PROFILE) <...>
        hotels = <
            ["gran sevilla"] = (HISTORIC_HOTEL) <...>
            ["sofitel"] = (LUXURY_HOTEL) <...>
            ["hotel real"] = (PENSION) <...>
        >
        attractions = <
            ["la corrida"] = (SPORT_VENUE) <...>
            ["Alcazar"] = (HISTORIC_SITE) <...>
        >
    >
>
```

Generic type names follow UML syntax with angle brackets:

```
hotels = (List<HOTEL>) <
    ["gran sevilla"] = (HISTORIC_HOTEL) <>
>
```

Namespace information can be included with dot-separated package names:

```
(org.openehr.rm.ehr.content.ENTRY)
(Core.Abstractions.Relationships.Relationship)
```

**Type Information** can be optionally included on any node immediately before the opening `<` of any block.

#### Associations and Shared Objects

Shared objects are referenced using paths. Associations are expressed via fully qualified paths as attribute values:

```
destinations = <
    ["seville"] = <
        hotels = <
            ["gran sevilla"] = </hotels["gran sevilla"]>
            ["sofitel"] = </hotels["sofitel"]>
            ["hotel real"] = </hotels["hotel real"]>
        >
    >
>

bookings = <
    ["seville:0134"] = <
        customer_id = <"0134">
        period = <...>
        hotel = </hotels["sofitel"]>
    >
>

hotels = <
    ["gran sevilla"] = (HISTORIC_HOTEL) <>
    ["sofitel"] = (LUXURY_HOTEL) <>
    ["hotel real"] = (PENSION) <>
>
```

Data in other dADL documents can be referred to using URI syntax with the internal path included.

**Shared objects** are referenced using paths. External objects use normal URIs with dADL path syntax in the path section.

##### Association Paths

```
/destinations["seville"]/hotels["gran sevilla"]
/destinations["seville"]/hotels["sofitel"]
/destinations["seville"]/hotels["hotel real"]
/bookings["seville:0134"]/customer_id
/bookings["seville:0134"]/period
/bookings["seville:0134"]/hotel
/hotels["sofitel"]
/hotels["hotel real"]
/hotels["gran sevilla"]
```

### Leaf Data - Built-in Types

All dADL data eventually resolves to primitive types: `String`, `Integer`, `Real`, `Double`, `Character`, various date/time types, lists, or intervals. Manifest data values appear immediately inside leaf angle brackets: `some_attribute = <manifest value>`

#### Primitive Types

##### Character Data

Characters in single quotes:
```
'a'
```

Characters outside low ASCII (0-127) must be UTF-8 encoded with allowed backslash-quoted ASCII characters as described in Section 3.

##### String Data

All strings in double quotes:
```
"this is a string"
"this is a much longer string, what one might call a \"phrase\"."
```

Multi-line strings with automatic indentation handling:
```
text = <"And now the STORM-BLAST came, and he
        Was tyrannous and strong :
        He struck with his o'ertaking wings,
        And chased us south along.">
```

Characters outside low ASCII must be UTF-8 encoded.

##### Integer Data

Simple numeric representation:
```
25
300000
29e6
```

Commas or periods for breaking long numbers are not allowed.

##### Real Data

Detected by decimal point:
```
25.0
3.1415926
6.023e23
```

Only periods may separate the decimal part. Commas are reserved for list items.

##### Boolean Data

Case-insensitive values:
```
True
False
```

##### Dates and Times

###### Complete Date/Times

Full and partial dates, times, and durations use ISO 8601 subset. Extended form only (with ':' and '-'). Patterns:

```
yyyy-MM-dd                           -- date
hh:mm:ss[,sss][Z|+/-hhmm]           -- time
yyyy-MM-ddThh:mm:ss[,sss][Z]        -- date/time
```

Where:
- `yyyy` = four-digit year
- `MM` = month in year
- `dd` = day in month
- `hh` = hour (24-hour clock)
- `mm` = minutes
- `ss,sss` = seconds with fractional part
- `Z` = timezone (+/- 4 digits or 'Z' for UTC)

**Duration examples** using ISO 8601 patterns (with 'W' allowed for medical use):
```
P22D4TH15M0S    -- 22 days, 4 hours, 15 minutes
```

###### Examples

```
1919-01-23                  -- birthdate
16:35:04,5                  -- rise time
2001-05-12T07:35:20+1000    -- timestamped email
P22D4TH15M0S                -- period
```

###### Partial Date/Times

ISO 8601 incomplete formats in extended form:

```
yyyy-MM             -- date without days
hh:mm               -- time without seconds
yyyy-MM-ddThh:mm    -- date/time without seconds
yyyy-MM-ddThh       -- date/time without minutes/seconds
```

Alternative form using '?' for missing digits:

```
yyyy-MM-??   -- date with unknown day
yyyy-??-??   -- date with unknown month and day
hh:mm:??     -- time with unknown seconds
hh:??:??     -- time with unknown minutes and seconds
yyyy-MM-ddThh:mm:??           -- date/time unknown seconds
yyyy-MM-ddThh:??:??           -- date/time unknown minutes
yyyy-MM-ddT??:??:??           -- date/time unknown time
yyyy-MM-??T??:??:??           -- date/time unknown day and time
yyyy-??-??T??:??:??           -- date/time unknown month, day, time
```

#### Intervals of Ordered Primitive Types

Uniform syntax for intervals of `Integer`, `Real`, `Date`, `Time`, `Date_time`, or `Duration`:

```
|N..M|         -- N >= x <= M
|N>..M|        -- N > x <= M
|N..<M|        -- N >= x < M
|N>..<M|       -- N > x < M
|<N|           -- x < N
|>N|           -- x > N
|>=N|          -- x >= N
|<=N|          -- x <= N
|N +/-M|       -- interval of N +/- M
```

Allowable values for `N` and `M`:
- Any value in the relevant type's range
- `infinity`
- `-infinity`
- `*` (equivalent to infinity)

**Examples:**
```
|0..5|            -- integer interval
|0.0..1000.0|     -- real interval
|0.0..<1000.0|    -- real 0.0 >= x < 1000.0
|08:02..09:10|    -- time interval
|>= 1939-02-01|   -- open-ended date interval
|5.0 +/-0.5|      -- 4.5 - 5.5
|>=0|             -- >= 0
|0..infinity|     -- 0 - infinity
```

#### Other Built-in Types

##### URIs

Standard URI syntax per IETF RFC 3986:
```
http://archetypes.are.us/home.html
ftp://get.this.file.com#section_5
http://www.mozilla.org/products/firefox/upgrade/?application=thunderbird
```

Special character encoding follows RFC 3986.

##### Coded Terms

Coded terms consist of a terminology identifier and a code:

```
[terminology_id::code]
```

**Examples:**
```
[icd10AM::F60.1]              -- ICD10AM
[snomed-ct::2004950]          -- SNOMED CT
[snomed-ct(3.1)::2004950]     -- SNOMED CT v3.1
```

#### Lists of Built-in Types

Comma-separated values of the same type:

```
"cyan", "magenta", "yellow", "black"    -- colors
1, 1, 2, 3, 5                            -- Fibonacci
08:02, 08:35, 09:10                      -- train times
```

Single-item lists use continuation marker:
```
"en", ...           -- languages
"icd10", ...        -- terminologies
[at0200], ...
```

Whitespace is optional:
```
1,1,2,3   -- identical to: 1, 1, 2,3
```

### Plug-in Syntaxes

dADL allows object values to be expressed in other abstract syntaxes via plug-in parsers. Indicated by syntax type in parentheses with modified delimiters:

```
attr_name = (syntax) <#
    ...
#>
```

**Example** (cADL plug-in):
```
definition = (cadl) <#
    ENTRY[at0000] matches {
        name matches {
            CODED_TEXT matches {
                code matches {
                    CODE_PHRASE matches {[ac0001]}
                }
            }
        }
    }
#>
```

Not all parsers support all plug-in syntaxes.

### Expression of dADL in XML

dADL maps systematically to XML. Type names map to XML 'type' attributes. The mapping is a faithful reflection of object-oriented semantics without concerning itself with visual XML aesthetics.

#### Single Attributes

Single attribute nodes map to tagged nodes of the same name.

#### Container Attributes

Container attributes map to a series of tagged nodes with XML attribute `_id_` set to the dADL key:

**dADL:**
```
subjects = <
    ["philosophy:plato"] = <
        name = <"philosophy">
    >
    ["philosophy:kant"] = <
        name = <"philosophy">
    >
>
```

**XML:**
```xml
<subjects id="philosophy:plato">
    <name>philosophy</name>
</subjects>
<subjects id="philosophy:kant">
    <name>philosophy</name>
</subjects>
```

Path `subjects[@id="philosophy:plato"]/name` navigates to the same element in both dADL and XML.

#### Nested Container Attributes

Nested containers use synthesized element tags and key attributes:

**dADL:**
```
countries = <
    ["spain"] = <
        ["hotels"] = <...>
        ["attractions"] = <...>
    >
    ["egypt"] = <
        ["hotels"] = <...>
        ["attractions"] = <...>
    >
>
```

**XML:**
```xml
<countries key="spain">
    <_items key="hotels">
        ...
    </_items>
    <_items key="attractions">
        ...
    </_items>
</countries>
<countries key="egypt">
    <_items key="hotels">
        ...
    </_items>
    <_items key="attractions">
        ...
    </_items>
</countries>
```

dADL path `countries["spain"]/["hotels"]` transforms to XPath `countries[@key="spain"]/_items[@key="hotels"]`.

#### Type Names

Type names map to XML 'type' attributes:

**dADL:**
```
destinations = <
    ["seville"] = (TOURIST_DESTINATION) <
        profile = (DESTINATION_PROFILE) <>
        hotels = <
            ["gran sevilla"] = (HISTORIC_HOTEL) <>
        >
    >
>
```

**XML:**
```xml
<destinations id="seville" adl:type="TOURIST_DESTINATION">
    <profile adl:type="DESTINATION_PROFILE">
        ...
    </profile>
    <hotels id="gran sevilla" adl:type="HISTORIC_HOTEL">
        ...
    </hotels>
</destinations>
```

### Syntax Specification

#### Grammar

The dADL parser is implemented using lex and yacc specifications. Current implementations are available at the [openEHR adl-tools Github repository](https://github.com/openEHR/adl-tools/tree/Release-1.4/libraries/common_libs/src/structures/syntax/dadl/parser).

**Key production rules:**

```
input:
    attr_vals
    | complex_object_block
    ;

attr_vals:
    attr_val
    | attr_vals attr_val
    | attr_vals ';' attr_val
    ;

attr_val:
    attr_id SYM_EQ object_block
    ;

attr_id:
    V_ATTRIBUTE_IDENTIFIER
    ;

object_block:
    complex_object_block
    | primitive_object_block
    | plugin_object_block
    ;

plugin_object_block:
    V_PLUGIN_SYNTAX_TYPE V_PLUGIN_BLOCK
    ;

complex_object_block:
    single_attr_object_block
    | multiple_attr_object_block
    ;

multiple_attr_object_block:
    untyped_multiple_attr_object_block
    | type_identifier untyped_multiple_attr_object_block
    ;

untyped_multiple_attr_object_block:
    multiple_attr_object_block_head keyed_objects SYM_END_DBLOCK
    ;

multiple_attr_object_block_head:
    SYM_START_DBLOCK
    ;

keyed_objects:
    keyed_object
    | keyed_objects keyed_object
    ;

keyed_object:
    object_key SYM_EQ object_block
    ;

object_key:
    '[' simple_value ']'
    ;

single_attr_object_block:
    untyped_single_attr_object_block
    | type_identifier untyped_single_attr_object_block
    ;

untyped_single_attr_object_block:
    single_attr_object_complex_head SYM_END_DBLOCK
    | single_attr_object_complex_head attr_vals SYM_END_DBLOCK
    ;

single_attr_object_complex_head:
    SYM_START_DBLOCK
    ;

primitive_object_block:
    untyped_primitive_object_block
    | type_identifier untyped_primitive_object_block
    ;

untyped_primitive_object_block:
    SYM_START_DBLOCK primitive_object_value SYM_END_DBLOCK
    ;

primitive_object_value:
    simple_value
    | simple_list_value
    | simple_interval_value
    | term_code
    | term_code_list_value
    ;

simple_value:
    string_value
    | integer_value
    | real_value
    | boolean_value
    | character_value
    | date_value
    | time_value
    | date_time_value
    | duration_value
    | uri_value
    ;

type_identifier:
    '(' V_TYPE_IDENTIFIER ')'
    | '(' V_GENERIC_TYPE_IDENTIFIER ')'
    | V_TYPE_IDENTIFIER
    | V_GENERIC_TYPE_IDENTIFIER
    ;
```

**Interval and list rules follow similar patterns for each primitive type** (integer, real, date, time, date_time, duration).

#### Symbols

Reserved symbols and their meanings:

| Symbol | Meaning |
|--------|---------|
| `SYM_START_DBLOCK` | `<` (start block) |
| `SYM_END_DBLOCK` | `>` (end block) |
| `SYM_EQ` | `=` (equals) |
| `SYM_GT` | `>` (greater than) |
| `SYM_LT` | `<` (less than) |
| `SYM_GE` | `>=` (greater or equal) |
| `SYM_LE` | `<=` (less or equal) |
| `SYM_ELLIPSIS` | `..` (range) |
| `SYM_INTERVAL_DELIM` | `\|` (interval delimiter) |
| `SYM_LIST_CONTINUE` | `...` (list continuation) |
| `SYM_TRUE` | `True` (boolean true) |
| `SYM_FALSE` | `False` (boolean false) |

### Syntax Alternatives

#### Container Attributes

Container attribute values can be expressed using alternative syntax forms where appropriate for specific use cases and tool capabilities.

---

## cADL - Constraint ADL {#cadl}

The cADL syntax provides formal constraint expression over information model structures. (Full cADL specification section content would follow, including constraint definitions, object constraints, primitive type constraints, and cardinality/occurrence specifications.)

---

## Assertions {#assertions}

Assertions are logical expressions used to specify invariants and complex business rules. (Full assertions section content with operators, operands, and syntax would follow.)

---

## ADL Paths {#adl-paths}

ADL paths enable navigation and reference to specific nodes within archetype structures using a syntax similar to XPath. (Full ADL paths section with syntax, examples, and relationship to W3C XPath would follow.)

---

## ADL - Archetype Definition Language {#adl}

The complete ADL syntax combines dADL, cADL, and assertion syntaxes with archetype-specific header and organizational sections. (Full ADL section with header sections, definition section, invariant section, ontology section, and validity rules would follow.)

---

## Customising ADL {#customising}

ADL can be extended with custom syntaxes and domain-specific constraints through defined extension mechanisms. (Full customization section would follow.)

---

## Appendices {#appendices}

### Appendix A: Relationship of ADL to Other Formalisms

ADL shares conceptual similarities with various standardized formalisms:

- **OMG OCL (Object Constraint Language)** - Both provide constraint expression
- **OWL (Web Ontology Language)** - Both express semantic relationships
- **KIF (Knowledge Interchange Format)** - Both support formal knowledge representation
- **XML Schema** - Both constrain data structures

### Appendix B: Extended Meta-data Guide

Extended meta-data allows standardised and custom governance information to be recorded in archetypes. Standardised items and other extensible items are documented for use by developers and governance systems.

### Appendix C: Syntax Specification

Complete EBNF grammar and lexical specifications for all ADL syntaxes are provided, including:
- ADL outer syntax
- cADL syntax
- cADL primitives syntax
- Rules syntax
- ODIN structures
- ODIN value types
- Base lexer

---

## References

- Beale, T. (2000). "Archetypes: Constraint-based Domain Models for Future-proof Information Systems." GEHR Technical Documentation.
- Beale, T. (2002). "Archetypes: Models, Specialization and Deployment." International Conference on Health Informatics.
- Various IETF RFCs (3986, 2781) and ISO 8601 standards.
- openEHR specifications and technical documentation.
- W3C XPath and XML specifications.

---

## License and Copyright

(c) 2003 - 2024 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
[https://creativecommons.org/licenses/by-nd/3.0/](https://creativecommons.org/licenses/by-nd/3.0/)

**Support:**
- Issues: [Problem Reports](https://specifications.openehr.org/components/AM/open_issues)
- Web: [specifications.openEHR.org](https://specifications.openehr.org)

The openEHR Foundation is an independent, non-profit organization facilitating health record sharing through open specifications, clinical models, and platform implementations.
