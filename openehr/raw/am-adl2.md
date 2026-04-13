# Archetype Definition Language 2 (ADL2)

**Issuer**: openEHR Specification Program
**Release**: AM Release-2.3.0
**Status**: STABLE
**Keywords**: EHR, ADL, AOM, health records, archetypes, constraint language, ISO 13606, openehr

**Source:** https://specifications.openehr.org/releases/AM/latest/ADL2.html

---

## Table of Contents

- [Preface](#preface)
- [Overview](#overview)
- [File Encoding and Character Quoting](#file-encoding-and-character-quoting)
- [cADL - Constraint ADL](#cadl---constraint-adl)
- [ADL Paths](#adl-paths)
- [Default Values](#default-values)
- [ADL - Archetype Definition Language](#adl---archetype-definition-language)
- [Terminology Integration](#terminology-integration)
- [Specialisation](#specialisation)
- [Templates](#templates)

---

## Preface

### Purpose

ADL2 is a language specification for authoring archetypes—formal constraints on clinical data structures. The document serves software developers, domain specialists, and subject matter experts who design clinical data definitions.

### Related Documents

**Prerequisites:**
- openEHR Architecture Overview
- openEHR Archetype Technical Overview

**Related:**
- openEHR Archetype Object Model (AOM2)
- openEHR Operational Template Specification (OPT2)

### Nomenclature

The term "attribute" denotes any stored property in an object model, including primitive attributes and relationships. The term "archetype" encompasses both traditional archetypes and templates, as templates are technically archetypes under ADL/AOM 2.

### Status

This specification is STABLE. Development versions are available at https://specifications.openehr.org/releases/AM/latest/ADL2.html.

### Feedback

- Forum: openEHR ADL forum (discourse.openehr.org)
- Issues: Specifications Problem Report tracker

### Conformance

Conformance is determined by formal testing against openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML-schema.

### Tools

- ADL Workbench (reference compiler, visualizer, editor)
- openEHR tools available at www.openehr.org/downloads
- Source projects at github.com/openEHR

### Changes from Previous Versions

#### dADL (ODIN)

The "dADL" object syntax for description, terminology, and annotation sections has been separated into its own specification: Object Data Instance Notation (ODIN).

#### ADL 2.0 Changes

Key changes include:

- Node identification system replaced at-codes with id-codes
- All nodes now require id-codes
- Specialization rules for node identifiers in child archetypes
- `ontology` section renamed to `terminology`
- Value sets declared in dedicated subsection
- `revision_history` section removed (uses Base Types Resource package)

**Backward Compatibility**: ADL 1.4 archetypes require conversion to ADL 2.x form. The ADL Workbench implements this conversion; ADL 1.4-style paths remain generatable for AQL queries.

#### ADL 1.5 Changes

- Optional `generated` marker in archetype declaration
- Differential representation for specialized archetypes
- Semantics of reference model subtype matching
- Keywords for ordering specialized object nodes
- Negated match operator for value set exclusions
- Inheritance-flattened archetype semantics
- Optional `annotations` section
- `declarations` and `invariants` merged into `rules`
- Language section now mandatory
- `.adls` file extension for differential files

---

## Overview

ADL combines three syntaxes:

1. **cADL** (constraint form): Expresses archetype `definition` section
2. **ODIN** (Object Data Instance Notation): Expresses `language`, `description`, and `terminology` sections
3. **openEHR Expression Language**: For rules and assertions

The top-level archetype structure alternates between constraint definitions and structured data definitions.

### An Example

```
archetype (adl_version=2.0.5; rm_release=1.1.5)
    adl-test-instrument.guitar.v1.0.4

language
    original_language = <[iso_639-1::en]>

definition
    INSTRUMENT[id1] matches {
        size matches {|60..120|}                    -- size in cm
        date_of_manufacture matches {yyyy-mm-??}    -- year & month ok
        parts matches {
            PART[id2] matches {                     -- neck
                material matches {[ac1]}            -- timber or nickel alloy
            }
            PART[id3] matches {                     -- body
                material matches {[at3]}            -- timber
            }
        }
    }

terminology
    term_definitions = <
        ["en"] = <
            ["id1"] = <
                text = <"guitar">;
                description = <"stringed instrument">
            >
            ["id2"] = <
                text = <"neck">;
                description = <"neck of guitar">
            >
            ["id3"] = <
                text = <"body">;
                description = <"body of guitar">
            >
            ["at3"] = <
                text = <"timber">;
                description = <"straight, seasoned timber">
            >
            ["at4"] = <
                text = <"nickel alloy">;
                description = <"frets">
            >
        >
    >

    value_sets = <
        ["ac1"] = <
            id = <"ac1">
            members = <"at3", "at4">
        >
    >
```

---

## File Encoding and Character Quoting

### File Encoding

ADL files are encoded in UTF-8. Three locations allow non-ASCII characters:

- String values (double quotes)
- Regular expression patterns (`//` or `^^`)
- Character values (single quotes)

URIs follow IETF RFC 3986 percent-encoding for characters outside the unreserved set:

```
unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
```

**Fallback for ASCII-only environments**: Use Unicode escape sequences:

- `\uHHHH` for code points U+0000 to U+FFFF (4 hex digits)
- `\uHHHHHHHH` for code points U+10000 to U+10FFFF (8 hex digits, per RFC 2781)

### Special Character Sequences

Allowed escape sequences in strings and characters:

| Sequence | Meaning |
|----------|---------|
| `\r` | Carriage return |
| `\n` | Linefeed |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

In regular expressions, backslash patterns follow PERL syntax (e.g., `\s`, `\d`) and are processed literally by regex engines.

---

## cADL - Constraint ADL

### Overview

cADL uses block-structured syntax for expressing constraints on object-oriented data models. The basic pattern:

```
TYPE[id1] matches {
    attribute matches {
        TYPE[id2] matches { ... }
    }
}
```

Equivalent symbolic notation using mathematical logic symbols:

```
TYPE[id1] ∈ {
    attribute ∈ {
        TYPE[id2] ∈ { ... }
    }
}
```

| Textual | Symbolic | Meaning |
|---------|----------|---------|
| `matches` | `∈` | Set membership |
| `~matches` | `∉` | Not set membership |
| `not` | `∼` | Negation |
| `*` | `∗` | Infinity |

### Basics

#### Keywords

- `matches`, `~matches`, `is_in`, `~is_in`
- `occurrences`, `existence`, `cardinality`
- `ordered`, `unordered`, `unique`
- `use_node`, `allow_archetype`
- `include`, `exclude`
- `before`, `after`

#### Block/Node Structure

cADL alternates between object blocks (introduced by type names in upper case) and attribute blocks (introduced by attribute names in lower case):

```
PERSON[id1] ∈ {                     -- OBJECT block
    name ∈ {                        -- attribute block
        PERSON_NAME[id2] ∈ { ... }  -- OBJECT block
    }
}
```

#### Comments

Comments use `--` leader; multi-line comments repeat `--` on each line.

#### The Underlying Information Model

Identifiers in cADL correspond to entities (types and attributes) from an underlying information model. A cADL archetype constrains only those model parts deemed meaningful; it cannot invalidate model constraints.

Example constraint on a generic model:

```
ELEMENT[id10] matches {          -- diastolic blood pressure
    value matches {
        DV_QUANTITY[id11] matches {
            magnitude matches {|0..1000|}
            property matches {"pressure"}
            units matches {"mm[Hg]"}
        }
    }
}
```

##### Information Model Identifiers

- **Type name**: Starts with uppercase letter, contains letters/digits/underscores. Generic types may include commas, angle brackets, and spaces (per OMG UML 2.x).
- **Attribute name**: Starts with lowercase letter, contains letters/digits/underscores.

Convention in this document: Types shown in ALL_UPPERCASE; attributes in all_lowercase with underscores for word breaks. Other conventions (CamelCase, snake_case) are acceptable per RM convention.

#### Node Identifiers

Node identifiers appear after type names in brackets, e.g., `[id3]`. Root object identifier is `[id1]`, or `[id1.1]`, `[id1.1.1]` in specialized archetypes.

**All object nodes require a node identifier.**

#### The matches Operator

The `matches` (or `is_in`) operator establishes set membership—the allowed values for an entity are specified within braces:

```
aaa matches {/\w*ion[\s\n\t ]/}    -- set of words ending in 'ion'
```

Negative constraint using negated operator:

```
aaa ~matches {5}      -- any value except 5
aaa ~is_in {5}        -- any value except 5
aaa ∉ {5}             -- any value except 5
```

#### Natural Language

cADL is language-independent. Readability comments in archetype text are generated from terminology sections in the locale's language.

---

### Constraints on Complex Types

#### Attribute Constraints

Attributes are single-valued or multiply-valued (container types). Both have `existence`; multiply-valued attributes additionally have `cardinality`.

##### Existence

Existence indicates whether an attribute value is mandatory (1..1) or optional (0..1). Constraints can override reference model defaults:

```
OBSERVATION[id1] matches {
    protocol existence matches {1..1} matches {
        -- details
    }
}
```

Valid existence constraint values: `{0}`, `{0..0}`, `{0..1}`, `{1}`, `{1..1}`.

**An existence constraint appears directly after any attribute identifier.**

#### Single-valued Attributes

Single-valued attributes contain a single object constraint:

```
value matches {
    DV_QUANTITY[id22] matches {
        magnitude matches {|0..55|}
        property matches {"velocity"}
        units matches {"mph"}
    }
}
```

Multiple alternatives (only one matches data):

```
value matches {
    DV_QUANTITY[id22] matches {          -- miles per hour
        magnitude matches {|0..55|}
        property matches {"velocity"}
        units matches {"mph"}
    }
    DV_QUANTITY[id23] matches {          -- km per hour
        magnitude matches {|0..100|}
        property matches {"velocity"}
        units matches {"km/h"}
    }
}
```

**Two or more object constraints under a single-valued attribute are understood as alternatives.**

#### Container Attributes

##### Cardinality

Cardinality constrains the number of members in container types (lists, sets, bags):

```
HISTORY[id2] occurrences ∈ {1} ∈ {
    periodic ∈ {False}
    events cardinality ∈ {*} ∈ {
        EVENT[id3] occurrences ∈ {0..1} ∈ { }    -- 1 min sample
        EVENT[id4] occurrences ∈ {0..1} ∈ { }    -- 2 min sample
        EVENT[id5] occurrences ∈ {0..1} ∈ { }    -- 3 min sample
    }
}
```

Cardinality with ordering semantics:

```
events cardinality ∈ {*; ordered} ∈ { }          -- logical list
events cardinality ∈ {*; unordered; unique} ∈ { } -- logical set
events cardinality ∈ {*; unordered} ∈ { }         -- logical bag
```

Standalone `cardinality` keyword indicates a container attribute without additional constraints:

```
events cardinality ∈ {                -- indicates 'events' is a container
```

Valid cardinality numeric values: `{0}`, `{0..0}`, `{0..n}`, `{m..n}`, `{0..*}`, `{*}`.

Cardinality and existence can co-occur:

```
events existence ∈ {0..1} cardinality ∈ {0..*} ∈ { -- etc -- }
```

**A cardinality constraint must appear after any container attribute name or its existence constraint.**

#### Object Constraints

##### Node Identifiers

Node identifiers `[idN]` after type names identify object nodes. Functions:

- Unambiguously reference nodes within same archetype
- Enable runtime data matching
- Enable specialised archetypes to reference parent nodes
- Enable unique path formation

**Node identifiers are required for every object node.**

Single node identifiers provide semantic meaning by equating codes to descriptions in terminology. Multiple nodes under container attributes require terminology definitions; single nodes under single-valued attributes may be defined but typically aren't necessary.

##### Occurrences

Occurrences constraint indicates how many times instances conforming to a constraint can occur in data. Typically used on container attribute children:

```
events cardinality ∈ {*} ∈ {
    EVENT[id2] occurrences ∈ {1..1} ∈ { }    -- 1 minute sample
    EVENT[id3] occurrences ∈ {0..1} ∈ { }    -- 2 minute sample
    EVENT[id4] occurrences ∈ {0..1} ∈ { }    -- 3 minute sample
}
```

Example restricting specific subtypes:

```
GROUP[id103] ∈ {
    kind ∈ {/tribe|family|club/}
    members cardinality ∈ {*} ∈ {
        PERSON[id104] occurrences ∈ {1} ∈ {
            title ∈ {"head"}
        }
        PERSON[id105] occurrences ∈ {0..*} ∈ {
            title ∈ {"member"}
        }
    }
}
```

Valid occurrences values: `{0}`, `{0..0}`, `{0..1}`, `{1}`, `{1..1}`, `{m..n}`, `{0..*}`, `{*}`, or single integer/infinity.

If no occurrences constraint stated, reference model default applies.

**An occurrences constraint appears directly after object type name within container attributes.**

**Compatibility Rules**: Where cardinality has finite upper bound:
- Child objects with open upper bound occurrences or inferred occurrences are legal
- Sum of child object occurrences lower bounds must be less than cardinality upper bound
- At least one instance of optional/mandatory children must fit within cardinality range

#### "Any" Constraints

Open "any" constraints override existence/cardinality:

```
PERSON[id2] ∈ {
    name existence ∈ {1}
}
```

Unconstrained types:

```
ELEMENT[id4] ∈ {          -- speed limit
    value ∈ {
        DV_QUANTITY[id5]  -- type was 'DATA_VALUE' in RM
    }
}
```

**Deprecated**: ADL 1.4 used `matches {*}` for any constraints. Modern form omits this suffix.

#### Reference Model Type Matching

Type names in cADL may be abstract classes, concrete classes, or generic types (using `<>`, `,`, spaces per UML/language standards). Matching is case-insensitive and whitespace-insensitive.

Data instance conformance matches:
- Same type if concrete
- Any subtype per reference model

Precise specification in AOM2: "Rm_type_name and reference model type matching" section.

##### Narrowed Subtype Constraints

Multiple reference model subtypes under same attribute constrain specific subtypes:

```
counter_party ∈ {
    PARTY[id4] ∈ { ... }           -- general PARTY constraint
    PERSON[id5] ∈ {                -- specific PERSON constraint
        date_of_birth ∈ { ... }
    }
}
```

Under multiply-valued attribute:

```
counter_parties ∈ {
    PERSON[id4] ∈ {
        date_of_birth ∈ { ... }
    }
    ORGANISATION[id5] ∈ {
        date_of_registration ∈ { ... }
    }
    PARTY[id6] ∈ { ... }            -- catch-all for other PARTY subtypes
}
```

##### Remove Specified Subtypes

Exclude specific subtypes using zero occurrences:

```
counter_party ∈ {
    PARTY[id4] ∈ { ... }
    COMPANY[id5] occurrences ∈ {0}
    GROUP[id6] occurrences ∈ {0}
}
```

#### Paths

##### Archetype Path Formation

Identified object nodes enable archetype path formation, referencing nodes unambiguously. Syntax resembles W3C Xpath, convertible to XML.

Paths are extracted from definition sections, constructed from concatenated '/' characters and attribute names with node identifiers as predicates.

Single object under single-valued attribute:

```
manager ∈ {
    PERSON[id104] ∈ {
        title ∈ {"head of finance", "head of engineering"}
    }
}
```

Valid paths:

```
manager[id104]/title
manager/title
```

Multiple sibling nodes require node identifiers for unique referencing:

```
employees ∈ {
    PERSON[id104] ∈ {
        title ∈ {"head"}
    }
    PERSON[id105] matches {
        title ∈ {"member"}
    }
}
```

Unique paths:

```
employees[id104]/title
employees[id105]/title
```

Complex example:

```
HISTORY[id1] occurrences ∈ {1} ∈ {
    periodic ∈ {False}
    events cardinality ∈ {*} ∈ {
        EVENT[id2] occurrences ∈ {0..1} ∈ { }    -- 1 min sample
        EVENT[id3] occurrences ∈ {0..1} ∈ { }    -- 2 min sample
        EVENT[id4] occurrences ∈ {0..1} ∈ { }    -- 3 min sample
    }
}
```

Constructible paths:

```
/
/periodic
/events[id2]
/events[id3]
/events[id4]
```

cADL paths follow ADL path syntax (Section 5), with alternating TYPE/attribute/TYPE/attribute pattern.

**Physical paths** use node identifiers; **logical paths** annotate with code meanings from terminology.

##### External Use of Paths

Paths referencing cADL nodes from outside the containing text require archetype identifier prefix:

```
[openehr-ehr-entry.apgar-result.v]/events[id2]
```

##### Runtime Paths

Runtime data paths match archetype paths except for single-valued attributes (only one instance possible, no ambiguity):

Archetype paths (alternatives):

```
items[id4]/value[id22]
items[id4]/value[id23]
```

Runtime path (single instance):

```
items[id4]/value
```

Query using runtime path matches data regardless of DV_QUANTITY type. Specific queries use full archetype paths or alternative constraints (e.g., `units = "km/h"`).

#### Internal References (Proxy Constraint Objects)

Define constraint structure matching elsewhere-defined structure using proxy object syntax:

```
use_node TYPE[idN] archetype_path
```

Referenced path must not be in proxy object's parent path but may be sibling.

Type in `use_node` reference must match referenced type.

##### Paths and Proxy Objects

Path syntax for proxy references follows archetype path syntax, convertible to W3C Xpath.

#### External References

Reference nodes in other archetypes using archetype identifier and path:

```
ELEMENT[id10] matches {
    value matches {
        use_archetype DV_QUANTITY[id11] /openehr-composition.section.v/items
    }
}
```

##### Paths

External reference paths follow same syntax as internal paths.

#### Archetype Slots

Archetype slots allow plug-in points for other archetypes:

```
items cardinality ∈ {*} ∈ {
    allow_archetype ITEM[id2] matches {
        include archetype_id/pattern/ matches {"openehr-.*"}
        exclude archetype_id/pattern/ matches {"openehr-.*-battery.*"}
    }
}
```

##### Formal Semantics of include and exclude Constraints

Include constraints specify allowed archetypes; exclude constraints remove subset:

```
include constraint_pattern
exclude constraint_pattern
```

##### Slots based on Lexical Archetype Identifiers

Match archetype identifiers using regex patterns:

```
include archetype_id/pattern/ matches {
    "openehr-ehr-.*\.bmi\.v[0-9]+\.[0-9]+"
}
```

##### Slots based on other Constraints

Specialized constraints beyond lexical matching:

```
include matches {
    OBSERVATION[id2] matches {
        data matches {
            HISTORY[id3] matches { ... }
        }
    }
}
```

##### Slot-filling

Slot-filling in templates binds specific archetypes to slots:

```
items[id2] matches {
    use_archetype OBSERVATION[id5] /openehr-ehr-observation.vital_signs.v/data/...
}
```

#### Mixed Structures

Archetypes may contain both objects and primitive constraints:

```
ELEMENT[id1] matches {
    value matches {
        DV_TEXT[id2] matches {
            value matches {/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/}
        }
        DV_QUANTITY[id3] matches { ... }
    }
}
```

### Second-order Constraints

#### Tuple Constraints

Tuple constraints express relationships between multiple attributes:

```
OBSERVATION[id1] matches {
    data matches {
        HISTORY[id2] matches {
            events cardinality ∈ {*} ∈ {
                tuple matches {
                    ["time"] = time;
                    ["magnitude"] = value/magnitude
                }
            }
        }
    }
}
```

##### Paths in Tuple structures

Tuple member paths use ADL path syntax.

#### Group Constraints

Group constraints restrict which combinations of alternatives are valid:

```
value matches {
    DV_QUANTITY[id2] matches { ... }
    DV_COUNT[id3] matches { ... }
    group matches {
        id2,
        id3
    }
}
```

##### Slots and Grouping

Slots may be constrained within groups to bind related archetypes.

### Constraints on Primitive Types

#### General Structure

Primitive type constraints use literal values appropriate to type:

```
ELEMENT[id1] matches {
    value matches {
        5,
        7,
        9
    }
}
```

#### Assumed Values

Default values when data omits value specification:

```
ELEMENT[id1] matches {
    value existence ∈ {0..1} matches {
        5;5           -- constraint; assumed value
    }
}
```

#### Constraints on Boolean

```
periodic matches {
    True,
    False
}
```

#### Constraints on Character

##### List of Characters

```
separator matches {
    ',',
    ';',
    '|'
}
```

##### Regular Expression

```
code matches {
    /[A-Z]{3}/
}
```

#### Constraints on String

##### List of Strings

```
status matches {
    "complete",
    "incomplete",
    "pending"
}
```

##### Regular Expression

```
name matches {
    /[a-zA-Z\s]+/
}
```

#### Constraints on Ordered Types

Ordered types (integers, reals, dates, times, durations) support range constraints:

```
magnitude matches {
    |0..<100|,      -- 0 <= magnitude < 100
    |>=50|          -- magnitude >= 50
}
```

#### Constraints on Integer

##### List of Integers

```
priority matches {
    1,
    2,
    3,
    5
}
```

##### Interval of Integer

```
count matches {
    |0..100|        -- 0 <= count <= 100
}
```

##### More Complex Integer Constraints

Combinations of lists and intervals:

```
value matches {
    5,
    10,
    |20..100|
}
```

Non-inclusive intervals:

```
value matches {
    |0..<1000|      -- 0 <= value < 1000
    |>0..100|       -- 0 < value <= 100
}
```

#### Constraints on Real

```
percentage matches {
    |0.0..100.0|
}
```

#### Constraints on Dates, Times and Durations

##### Date, Time and Date/Time

Pattern constraints using ISO 8601:

```
date_of_birth matches {
    yyyy-mm-dd
}

assessment_date matches {
    yyyy-mm-??,
    yyyy-??-??
}

observation_time matches {
    hh:mm:ss
}

event_datetime matches {
    yyyy-mm-ddThh:mm:ss
}
```

With timezone constraints:

```
timestamp matches {
    yyyy-mm-ddThh:mm:ss±hh:mm,
    yyyy-mm-ddThh:mm:ssZ
}
```

Range constraints:

```
measurement_date matches {
    |>=1990-01-01|,
    |<2020-12-31|
}
```

##### Duration Constraints

ISO 8601 duration patterns:

```
interval matches {
    P1Y,
    P6M,
    P1W,
    P1D,
    PT1H,
    PT30M,
    PT45S
}
```

Negative durations:

```
adjustment matches {
    -P1D,
    P1D
}
```

Complex durations:

```
cumulative matches {
    P1Y6M,
    P2W3D,
    PT1H30M
}
```

Range constraints:

```
delay matches {
    |>=P1D|,
    |<P30D|
}
```

#### Terminology Constraints

##### Formal Terminology Constraint

Constrain to specific terminology codes:

```
reason matches {
    [local::at10, at11, at12]
}
```

##### Soft Terminology Constraint

Allow codes plus specified additions:

```
status matches {
    [local::at10, at11];
    [ac1]       -- value set
}
```

##### Operational Binding Constraints

Bind to external terminology services:

```
finding matches {
    [terminology(snomed-ct)::
        find("*")
        where: ["< 91723000"]  -- is_a Problem
    ]
}
```

#### Constraints on Lists of Primitive Types

```
results matches {
    5,
    7,
    9,
    15,
    42
}
```

#### Constraints on Intervals of Ordered Primitive Types

```
normal_range matches {
    |4.0..6.0|
}
```

#### Constraints on Enumerated Types

```
blood_type matches {
    A,
    B,
    O,
    AB
}
```

### Syntax Validity Rules

Multiple validity rules govern cADL syntax; detailed rules appear in AOM2 specification.

---

## ADL Paths

### Overview

ADL paths reference archetype nodes using syntax similar to W3C Xpath.

#### Relationship with W3C Xpath

ADL paths follow Xpath conventions but are specific to archetype structure.

---

## Default Values

### Syntax

Default values appear in primitive constraints with syntax `constraint;default_value`:

```
value matches {
    5;5
}
```

### Examples

Integer with default:

```
priority matches {
    1,
    2,
    3;2
}
```

Boolean with default:

```
periodic matches {
    True,
    False;False
}
```

String with default:

```
status matches {
    "active",
    "inactive";
    "active"
}
```

---

## ADL - Archetype Definition Language

### Introduction

ADL combines cADL for constraints with ODIN syntax for data. Archetypes define reusable data specifications for clinical systems.

### File-naming Convention

- Standalone archetypes: `.adl`
- Differential (specialized) archetypes: `.adls`

File names follow archetype identifier pattern:

```
domain-entity.concept.version.adl
example: openehr-ehr-observation.blood_pressure.v1.adl
```

### Artefact Content

Archetypes contain sections:

1. Archetype declaration
2. Language section
3. Description section
4. Definition section
5. Rules section (optional)
6. RM Overlay section (optional)
7. Terminology section
8. Annotations section (optional)

### Basics

#### Keywords

ADL-specific keywords:

- `archetype`, `template`
- `language`, `description`, `definition`
- `rules`, `rm_overlay`
- `terminology`, `annotations`
- `specialize`

#### Artefact declaration

Declares archetype type and metadata:

```
archetype (adl_version=2.0.5; rm_release=1.1.5)
    openehr-ehr-observation.blood_pressure.v1.0.0
```

#### Node Identifier Codes

Object node identifiers use id-code format `[idN]`:

- Root object: `[id1]`
- Specialized children: `[id1.1]`, `[id1.1.1]`

#### Local Term Codes

Term codes reference terminology entries, format `[atN]`:

```
["at1"] = <text = <"active">
```

#### Local Value Set Codes

Value set codes reference terminology value sets, format `[acN]`:

```
["ac1"] = <members = <"at1", "at2">>
```

### Archetype Identification Section

#### ADL Version Indicator

Specifies ADL syntax version:

```
archetype (adl_version=2.0.5)
```

#### RM Release Indicator

Specifies reference model version:

```
archetype (rm_release=1.1.5)
```

#### Machine Identifiers

Namespace and identifier uniquely reference archetype:

```
archetype
    namespace = <"openehr">
    [openehr-ehr-observation.blood_pressure.v1.0.0]
```

#### Namespaces

Organize archetypes by domain:

```
namespace = <"openehr">
```

#### Human Readable Archetype Identifier

Composite identifier with semantic components:

```
openehr-ehr-observation.blood_pressure.v1.0.0
```

Structure: `{namespace}-{rm-class}.{concept}.v{major}.{minor}.{patch}`

#### Specialised Archetype Identification

Specializations indicate parent:

```
specialize
    openehr-ehr-observation.blood_pressure.v1
```

#### Version Identifiers

Version in archetype identifier: `v{major}.{minor}.{patch}`

#### Validity

Archetype marked valid/invalid indicating development status:

```
validity = <...>
```

#### Generated Indicator

Optional marker for tool-generated archetypes:

```
generated
```

#### Controlled Indicator

Indicates archetype under version control:

```
controlled
```

### Specialise Section

Declares parent archetype(s):

```
specialise
    openehr-ehr-observation.blood_pressure.v1
```

### Language Section

Declares original language and translations:

```
language
    original_language = <[iso_639-1::en]>
    translations = <
        ["de"] = <
            author = <
                name = <"name">
                organisation = <"org">
            >
            language = <[iso_639-1::de]>
        >
    >
```

### Description Section

Documents archetype purpose, usage, lifecycle:

```
description
    original_author = <
        name = <"name">
        organisation = <"organisation">
        date = <"yyyy-mm-dd">
    >
    details = <
        ["en"] = <
            language = <[iso_639-1::en]>
            purpose = <"...">
            keywords = <"...", "...">
            use = <"...">
            misuse = <"...">
            copyright = <"...">
        >
    >
    lifecycle_state = <"published">
```

### Deprecated Sections

#### Concept Section

Previously declared archetype concept; now implicit from archetype identifier.

### Definition Section

Contains cADL constraint structure:

```
definition
    OBSERVATION[id1] matches {
        data matches {
            HISTORY[id2] matches {
                events cardinality ∈ {*} ∈ {
                    EVENT[id3] occurrences ∈ {0..1} ∈ { }
                }
            }
        }
    }
```

#### Design-time and Run-time paths

Design-time paths include node identifiers for unique reference; runtime paths match single-valued attributes without identifiers.

### Rules Section

Expresses invariants and assertions using openEHR Expression Language:

```
rules
    assertion_name: $value/magnitude > 0
```

#### Assertions

Express constraints on data values:

```
systolic_range: /data/events[id3]/data/items[id4]/value/magnitude >= 0
```

##### Arithmetic Identities

Document mathematical relationships:

```
bmi_calculation: $weight / ($height * $height) = $bmi
```

##### Mathematical Formulae

Express required computations:

```
insulin_dose: $weight * $factor = $dose
```

##### Value-dependent Existence

Conditional requirements:

```
if_married_then_spouse_exists: $marital_status = "married" implies $spouse.exists()
```

#### Computational Statements

Express program-like logic (future capability):

```
for_each_item: ...
```

### RM Overlay Section

Declares reference model attribute modifications:

```
rm_overlay
    rm_visibility = <
        ["/data/items[id4]"] = <
            hide
        >
    >
```

#### RM Visibility

Hide/show reference model attributes; optionally alias names:

```
rm_visibility = <
    ["/protocol"] = <
        visibility = <"hide">
    >
    ["/data/items[id4]/name"] = <
        visibility = <"show">
        alias = <"local_name">
    >
>
```

### Terminology Section

#### Overview

Declares term definitions, value sets, and terminology bindings.

#### Term_definitions Sub-section

Defines node identifiers and term codes:

```
terminology
    term_definitions = <
        ["en"] = <
            ["id1"] = <
                text = <"blood pressure">
                description = <"systolic and diastolic">
            >
            ["at1"] = <
                text = <"systolic">
                description = <"systolic pressure">
            >
        >
    >
```

#### Value_sets Sub-section

Declares terminology value sets:

```
value_sets = <
    ["ac1"] = <
        id = <"ac1">
        members = <"at1", "at2", "at3">
    >
>
```

#### Term_bindings Sub-section

Binds local terms to external terminologies:

```
term_bindings = <
    ["SNOMED-CT"] = <
        items = <
            ["id1"] = <[SNOMED-CT::271649006]>
            ["at1"] = <[SNOMED-CT::163030003]>
        >
    >
>
```

#### Deprecated Terminology Section Features

##### At-codes as identifiers

ADL 1.x used at-codes (`[at10]`, `[at20]`) for node identification. ADL 2 uses id-codes.

##### Terminologies_available sub-section

Previously listed all terminologies; now deprecated. Bindings implicitly indicate available terminologies.

##### Separated definitions and bindings sub-sections

ADL 1.x separated term definitions and bindings; ADL 2 unifies them.

##### Term_definitions Structure

ADL 1.x used different structure; ADL 2 uses language-keyed dictionary.

### Annotations Section

Optional metadata on nodes:

```
annotations
    documentation = <
        ["en"] = <
            ["/data/items[id4]"] = <
                note = <"calibration recommended annually">
            >
        >
    >
```

---

## Terminology Integration

### Requirements

Terminology integration enables:

- Binding local codes to external terminologies
- Constraining values to terminology subsets
- Supporting multiple languages
- Enabling runtime terminology lookups

### Term Constraint Basics

Constraints on terminology-valued attributes use code specifications:

```
status matches {
    [local::at1, at2, at3]
}
```

External terminology binding:

```
status matches {
    [terminology(snomed-ct)::
        find("*")
        where: ["< 91723000"]
    ]
}
```

### From Constraints to Concrete Codes in Data

Archetype constraints define allowable codes; runtime data contains selected codes from constrained set.

---

## Specialisation

### Overview

Specialisation (inheritance) allows archetypes to extend parent archetypes. Specialized archetypes express only differences (differential form) or complete specifications (flat form).

### Specialisation Concepts

#### Differential and Flat Forms

**Differential form** (`.adls` files) contains only changed/new elements:

```
specialize
    openehr-ehr-observation.blood_pressure.v1

definition
    OBSERVATION[id1.1] matches {        -- specialize root
        data matches {
            HISTORY[id2] matches {
                events cardinality ∈ {1..*} ∈ {  -- change cardinality
                    EVENT[id3] occurrences ∈ {1} -- change occurrence
                }
            }
        }
    }
```

**Flat form** (`.adl` files) contains complete specification including inherited nodes.

#### Specialisation Levels

Single-level specialization:

```
openehr-ehr-observation.blood_pressure.v1  (parent)
openehr-ehr-observation.blood_pressure.v1.1  (child)
```

Multi-level specialization:

```
openehr-ehr-observation.blood_pressure.v1     (parent)
openehr-ehr-observation.blood_pressure.v1.1   (child)
openehr-ehr-observation.blood_pressure.v1.1.1 (grandchild)
```

#### Specialisation Paths

Specialization chains create specialization paths. Each level specializes parent.

#### Path Congruence

Paths in specialized archetypes must maintain congruence with parent paths, ensuring child constraints align with parent structure.

#### Redefinition Concepts

Redefinition changes constraints in specialization. Redefinition types:

- **Refinement**: Strengthening constraints (e.g., mandatory to required)
- **Specialization**: Restricting value sets or types
- **Cloning**: Creating multiple distinct variants in single level (under cardinality > 1)

### Examples

#### Redefinition for Refinement

Change occurrence from optional to mandatory:

```
-- parent
OBSERVATION[id1] matches {
    data matches {
        HISTORY[id2] matches {
            events cardinality ∈ {*} ∈ {
                EVENT[id3] occurrences ∈ {0..1}    -- optional
            }
        }
    }
}

-- child (differential)
OBSERVATION[id1.1] matches {
    data matches {
        HISTORY[id2] matches {
            events cardinality ∈ {*} ∈ {
                EVENT[id3.1] occurrences ∈ {1}     -- now mandatory
            }
        }
    }
}
```

#### Redefinition for Specialisation

Narrow value set:

```
-- parent
OBSERVATION[id1] matches {
    value matches {
        [local::at1, at2, at3, at4]
    }
}

-- child (differential)
OBSERVATION[id1.1] matches {
    value matches {
        [local::at1, at2]      -- narrowed set
    }
}
```

##### Specialisation with Cloning

Under container attributes with cardinality > 1, specialization can clone nodes:

```
-- parent
items cardinality ∈ {0..*} ∈ {
    ELEMENT[id2] occurrences ∈ {0..1}
}

-- child (differential) - clone for two variants
items cardinality ∈ {0..*} ∈ {
    ELEMENT[id2.1] occurrences ∈ {0..1}    -- variant 1
    ELEMENT[id2.2] occurrences ∈ {0..1}    -- variant 2
}
```

### Attribute Redefinition

#### Existence Redefinition: Mandation and Exclusion

Mandate optional attribute:

```
-- parent
address existence ∈ {0..1}

-- child (differential)
address existence ∈ {1}        -- now mandatory
```

Exclude attribute (advanced):

```
-- parent
nickname existence ∈ {0..1}

-- child (differential)
nickname existence ∈ {0}       -- exclude entirely
```

#### Multiply-valued (Container) Attributes

##### Cardinality

Constrain container size:

```
-- parent
items cardinality ∈ {*}

-- child (differential)
items cardinality ∈ {1..*}     -- at least one required
```

##### Ordering of Sibling Nodes

Constrain order of sibling object nodes:

```
items cardinality ∈ {*} ∈ {
    ELEMENT[id2] before ELEMENT[id3]
    ELEMENT[id3]
}
```

### Object Redefinition

#### Node Identifiers

##### Adding Nodes

Add new nodes in specialized child:

```
-- child (differential)
items cardinality ∈ {*} ∈ {
    ELEMENT[id4] occurrences ∈ {0..1}      -- new node
}
```

#### Occurrences Redefinition

Change object occurrence constraints:

```
-- parent
items cardinality ∈ {*} ∈ {
    ELEMENT[id2] occurrences ∈ {0..1}
}

-- child (differential)
items cardinality ∈ {*} ∈ {
    ELEMENT[id2.1] occurrences ∈ {1}       -- now required
}
```

##### Mandation

Make optional occurrence mandatory:

```
ELEMENT[id2.1] occurrences ∈ {1}
```

##### Exclusion

Remove optional occurrence:

```
ELEMENT[id2.1] occurrences ∈ {0}
```

#### Single and Multiple Specialisation - When does Cloning Occur?

Cloning occurs when:
- Container cardinality allows multiple children
- Specialization creates multiple variants of same parent node
- Each variant identified by distinct id-code

#### Exhaustive and Non-Exhaustive Redefinition

**Exhaustive redefinition** states all allowed alternatives:

```
-- child (differential)
value matches {
    [local::at1, at2]          -- complete replacement
}
```

**Non-exhaustive** preserves parent alternatives and adds constraints:

```
-- child (differential)
value matches {
    [local::at1, at2];
    [ac1]                      -- adds value set from parent
}
```

#### Reference Model Type Refinement

Narrow RM type to concrete subtype:

```
-- parent
value matches {
    DV_QUANTITY[id5]
}

-- child (differential)
value matches {
    DV_QUANTITY[id5.1] matches {
        property matches {"temperature"}
    }
}
```

#### Internal Reference (Proxy Object) Redefinition

Redefine `use_node` references in specialized archetypes:

```
-- child (differential)
use_node TYPE[idN.1] archetype_path
```

#### External Reference Redefinition

Redefine `use_archetype` references:

```
-- child (differential)
allow_archetype ITEM[id2.1] matches {
    include archetype_id/pattern/ matches {"..."}
}
```

#### Slot Filling and Redefinition

Specialize slot constraints:

```
-- parent
allow_archetype ITEM[id2] matches {
    include archetype_id/pattern/ matches {"openehr-.*"}
}

-- child (differential)
allow_archetype ITEM[id2.1] matches {
    include archetype_id/pattern/ matches {"openehr-.*vital.*"}  -- narrowed
}
```

#### Unconstrained Attributes

Specialization may add constraints to previously unconstrained attributes:

```
-- parent
name

-- child (differential)
name matches {
    /[A-Za-z\s]+/              -- add constraint
}
```

### Primitive Object Redefinition

#### Numeric Primitive Redefinition

Constrain numeric ranges:

```
-- parent
magnitude matches {|0..1000|}

-- child (differential)
magnitude matches {|0..500|}   -- narrowed range
```

#### Terminology Constraint Redefinition

##### Constrain Previously Unconstrained Node

Add terminology constraint:

```
-- parent
status

-- child (differential)
status matches {
    [local::at5, at6]          -- add constraint
}
```

##### Terminology Internal Value Set Redefinition

Modify internal value set members:

```
-- parent
reason matches {[local::at1, at2, at3]}

-- child (differential)
reason matches {[local::at1, at2]}  -- remove at3
```

##### Terminology External Subset Redefinition

Modify external terminology subset:

```
-- parent
finding matches {
    [terminology(snomed-ct)::find("*") where: ["< 91723000"]]
}

-- child (differential)
finding matches {
    [terminology(snomed-ct)::find("*") where: ["< 404684003"]]  -- narrowed
}
```

##### Constraint Strength Redefinition

Change soft to firm constraint:

```
-- parent
status matches {
    [local::at1, at2];
    [ac1]
}

-- child (differential)
status matches {
    [local::at1, at2]          -- remove optional value set
}
```

#### Tuple Redefinition

Redefine tuple constraints in specialization:

```
-- child (differential)
tuple matches {
    ["time"] = time;
    ["measurement"] = value/magnitude
}
```

### Rules

Specialize or add rules in child archetypes:

```
-- child (differential)
rules
    systolic_range: $magnitude > 0  -- additional rule
```

### Languages

Add translations in specialized archetypes:

```
language
    translations = <
        ["fr"] = <
            ...
        >
    >
```

### Description Section

Extend or modify description in specialized archetype:

```
description
    details = <
        ["en"] = <
            purpose = <"...">  -- specialized purpose
        >
    >
```

### Terminology Section

Add/modify terminology definitions in specialized archetype:

```
terminology
    term_definitions = <
        ["en"] = <
            ["id2.1"] = <
                text = <"new node">
            >
        >
    >
```

### Bindings

Add or modify terminology bindings:

```
term_bindings = <
    ["SNOMED-CT"] = <
        items = <
            ["id2.1"] = <[SNOMED-CT::new-code]>
        >
    >
>
```

---

## Templates

### Overview

Templates are archetypes that combine multiple archetypes into complete data specifications. Technically, templates are archetypes that use archetype slots to structure compositions.

### Example

Complete vital signs template:

```
archetype (adl_version=2.0.5)
    openehr-ehr-composition.vital_signs.v1

definition
    COMPOSITION[id1] matches {
        context matches {
            EVENT_CONTEXT[id2] matches {
                start_time matches {yyyy-mm-ddThh:mm:ss}
            }
        }
        content cardinality ∈ {*} ∈ {
            allow_archetype OBSERVATION[id3] matches {
                include archetype_id/pattern/ matches {
                    "openehr-ehr-observation.blood_pressure.*"
                }
            }
            allow_archetype OBSERVATION[id4] matches {
                include archetype_id/pattern/ matches {
                    "openehr-ehr-observation.body_temperature.*"
                }
            }
            allow_archetype OBSERVATION[id5] matches {
                include archetype_id/pattern/ matches {
                    "openehr-ehr-observation.pulse.*"
                }
            }
        }
    }
```

---

## Appendix A: Relationship of ADL to Other Formalisms

### Overview

ADL relates to multiple formal and semi-formal specification languages.

### Constraint Syntaxes

#### OMG OCL (Object Constraint Language)

OCL expresses object model constraints. ADL's cADL syntax parallels OCL but is more domain-oriented and clinically-focused.

### Ontology Formalisms

#### OWL (Web Ontology Language)

OWL expresses semantic ontologies. ADL archetypes define specific constraints rather than general ontologies.

#### KIF (Knowledge Interchange Format)

KIF expresses knowledge in formal logic. ADL's rule section uses similar concepts for clinical logic.

### XML-based Formalisms

#### XML-schema

XML-schema constrains XML documents. ADL provides equivalent capability for clinical information models independent of XML representation.

---

## Appendix B: Syntax Specification

### ADL Outer Syntax

Top-level archetype structure:

```
authored_archetype = archetype_header
                     language_section?
                     description_section?
                     definition_section
                     rules_section?
                     rm_overlay_section?
                     terminology_section?
                     annotations_section?

archetype_header = "archetype"
                   "(" metadata_items ")"
                   archetype_id

metadata_items = metadata_item (";" metadata_item)*

metadata_item = "adl_version" "=" VERSION
              | "rm_release" "=" VERSION
              | "generated"
              | "controlled"

archetype_id = NAMESPACE? archetype_identifier

archetype_identifier = identifier "-" identifier "." identifier ".v" VERSION
```

### cADL Syntax

Object and attribute constraints:

```
c_object = type_identifier node_id? occurrences? c_attribute*

c_attribute = attribute_identifier existence?
              cardinality?
              c_attribute_values

c_attribute_values = "{" c_object+ "}"
                   | "{" c_primitive+ "}"

c_primitive = constraint_value ("," constraint_value)*
            | interval_value ("," interval_value)*
            | pattern_value
            | default_value

node_id = "[" "id" NUMBER "]"

occurrences = "occurrences" "{" interval_value "}"

existence = "existence" "{" interval_value "}"

cardinality = "cardinality" "{" interval_value
              (";" cardinality_option)* "}"

cardinality_option = "ordered" | "unordered" | "unique"
```

### cADL Primitives Syntax

```
constraint_value = STRING | INTEGER | REAL | BOOLEAN | CODE

interval_value = lower_bound ".." upper_bound
               | lower_bound
               | ".." upper_bound

lower_bound = ">" | ">=" | "" (implicit >=)

upper_bound = "<" | "<=" | "" (implicit <=)
            | "*"

pattern_value = "/" regex_pattern "/"
              | "^^" regex_pattern "^^"
              | "yyyy-mm-dd" (date pattern)
              | "hh:mm:ss" (time pattern)
              | "P" duration_pattern (ISO 8601 duration)

default_value = constraint_value ";" constraint_value
```

### Rules Syntax

```
rules_section = "rules" rule_item*

rule_item = rule_name ":" expression

rule_name = identifier

expression = assertion_expr | computation_expr

assertion_expr = path comparison_op value

comparison_op = ">" | ">=" | "<" | "<=" | "=" | "!="
              | "matches" | "~matches"

computation_expr = arithmetic_expr | logical_expr

arithmetic_expr = expression ("+" | "-" | "*" | "/") expression

logical_expr = expression ("and" | "or") expression
             | "not" expression
             | expression "implies" expression
```

### Value types

```
STRING = '"' ([^"\\] | '\' . )* '"'

INTEGER = ["-"] DIGIT+

REAL = ["-"] DIGIT+ "." DIGIT+

BOOLEAN = "True" | "False"

CODE = "[" (("local" "::" ID)
          | ("terminology" "(" ID ")" "::" ID))
       "]"

DURATION = "P" (DIGIT "Y")? (DIGIT "M")? (DIGIT "W")? (DIGIT "D")?
               ("T" (DIGIT "H")? (DIGIT "M")? (DIGIT ("." DIGIT+)? "S")?)?

ARCHETYPE_ID = namespace "-" rm_class "." concept ".v" major "." minor ["." patch]

VERSION = major "." minor ["." patch]
```

### Base Lexer

```
WHITESPACE = [ \t\n\r]+ (ignored except in strings)

COMMENT = "--" [^\n]* (end of line comment)

IDENTIFIER = [a-zA-Z_] [a-zA-Z0-9_]*

UPPER_IDENTIFIER = [A-Z] [a-zA-Z0-9_]*

LOWER_IDENTIFIER = [a-z] [a-zA-Z0-9_]*

NUMBER = [0-9]+

REAL_NUMBER = [0-9]+ "." [0-9]+

SYMBOL = "matches" | "is_in" | "~matches" | "~is_in"
       | "occurrences" | "existence" | "cardinality"
       | "ordered" | "unordered" | "unique"
       | "use_node" | "allow_archetype"
       | "include" | "exclude"
       | "before" | "after"
       | "archetype" | "template"
       | "language" | "description" | "definition"
       | "rules" | "terminology" | "annotations"
       | "specialise" | "rm_overlay"
```

---

## References

**Document Information**

- **Copyright**: © 2003 - 2024 The openEHR Foundation
- **License**: Creative Commons Attribution-NoDerivs 3.0 Unported
- **Web**: specifications.openEHR.org
- **Issues**: Problem Reports tracker
