---
title: Archetype Definition Language (ADL)
type: entity
sources:
  - raw/am-adl2.md
  - raw/am-adl14.md
created: 2026-04-13
updated: 2026-04-13
---

# Archetype Definition Language (ADL)

ADL is the primary syntax for authoring openEHR archetypes and templates. It is the "human-readable" form of archetype definitions. ADL 2 is the current version.

**Release**: AM 2.3.0 (STABLE)

## ADL File Structure

An ADL file has these sections:

```adl
archetype (adl_version=2.0.6; rm_release=1.1.0)
    openEHR-EHR-OBSERVATION.blood_pressure.v2

language
    original_language = <[ISO_639-1::en]>
    translations = <...>

description
    original_author = <...>
    lifecycle_state = <"published">
    details = <
        ["en"] = <
            language = <[ISO_639-1::en]>
            purpose = <"To record arterial blood pressure.">
            use = <"Use for recording all blood pressure measurements.">
            misuse = <"Not for recording venous pressure.">
        >
    >

definition
    OBSERVATION[at0000] matches {    -- Blood pressure
        data matches {
            HISTORY[at0001] matches {
                events cardinality matches {1..*} matches {
                    EVENT[at0006] occurrences matches {0..*} matches {
                        data matches {
                            ITEM_TREE[at0003] matches {
                                items cardinality matches {1..*} matches {
                                    ELEMENT[at0004] matches {  -- Systolic
                                        value matches {
                                            DV_QUANTITY matches {
                                                units matches {"mm[Hg]"}
                                                magnitude matches {|0.0..1000.0|}
                                            }
                                        }
                                    }
                                    ELEMENT[at0005] matches {  -- Diastolic
                                        value matches {
                                            DV_QUANTITY matches {
                                                units matches {"mm[Hg]"}
                                                magnitude matches {|0.0..1000.0|}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

terminology
    term_definitions = <
        ["en"] = <
            ["at0000"] = <text = <"Blood pressure">; description = <"...">>
            ["at0004"] = <text = <"Systolic">; description = <"...">>
            ["at0005"] = <text = <"Diastolic">; description = <"...">>
        >
    >
    term_bindings = <
        ["SNOMED-CT"] = <
            ["at0004"] = <http://snomed.info/id/271649006>
        >
    >
```

## cADL (Constraint ADL)

The `definition` section uses cADL — a constraint syntax for RM objects:

### Object Constraints

```adl
OBSERVATION[at0000] matches {
    -- constrains an OBSERVATION instance
}
```

### Attribute Constraints

```adl
data matches {
    HISTORY[at0001] matches { ... }
}
```

### Existence

Whether an attribute must be present:

```adl
value existence matches {0..1} matches { ... }  -- optional
value existence matches {1..1} matches { ... }  -- mandatory
```

### Cardinality

How many items a container attribute can hold:

```adl
items cardinality matches {0..*; ordered} matches { ... }
items cardinality matches {1..5; unordered; unique} matches { ... }
```

### Occurrences

How many times a constrained node can appear:

```adl
ELEMENT[at0004] occurrences matches {0..1} matches { ... }  -- optional, at most once
ELEMENT[at0005] occurrences matches {1..1} matches { ... }  -- mandatory, exactly once
ELEMENT[at0006] occurrences matches {0..*} matches { ... }  -- optional, unbounded
```

## Primitive Type Constraints

### String
```adl
value matches {"male", "female", "other"}
value matches {/[a-zA-Z]+/}
```

### Integer / Real
```adl
magnitude matches {|0..100|}        -- range
magnitude matches {|>=0|}           -- lower bound
magnitude matches {|0, 5, 10, 15|}  -- enumeration
```

### Date/Time
```adl
value matches {yyyy-mm-dd}
value matches {yyyy-??-XX}  -- year required, month optional, day not allowed
```

### Duration
```adl
value matches {PDTH}        -- days, hours pattern
value matches {|PT0S..PT120S|}  -- 0 to 120 seconds range
```

### Terminology Codes
```adl
value matches {[ac0001]}  -- constraint code referencing a value set
value matches {[at0010, at0011, at0012]}  -- inline code list
```

## Tuple Constraints

Constrain multiple attributes together (co-occurring values):

```adl
value matches {
    DV_QUANTITY[at0020] matches {
        [units, magnitude] matches {
            [{"mm[Hg]"}, {|0.0..1000.0|}],
            [{"kPa"}, {|0.0..133.0|}]
        }
    }
}
```

This ensures that if units is "mm[Hg]" the magnitude range is 0-1000, but if units is "kPa" the range is 0-133.

## Specialisation

A specialised archetype references its parent and only contains differential constraints:

```adl
archetype (adl_version=2.0.6; rm_release=1.1.0)
    openEHR-EHR-OBSERVATION.laboratory_test-blood_gas.v1
specialize
    openEHR-EHR-OBSERVATION.laboratory_test.v1

definition
    OBSERVATION[at0000.1] matches {
        -- only constraints that differ from parent
    }
```

Node IDs in specialisations use dot notation: `at0000.1` specialises `at0000`.

## Archetype Slots

Define insertion points for other archetypes:

```adl
allow_archetype OBSERVATION[at0050] occurrences matches {0..*} matches {
    include
        archetype_id/value matches {/openEHR-EHR-OBSERVATION\.blood_pressure.*/}
        archetype_id/value matches {/openEHR-EHR-OBSERVATION\.heart_rate.*/}
    exclude
        archetype_id/value matches {/.*/}
}
```

## Terminology Section

### Term Definitions

Map archetype node IDs to human-readable names per language:

```adl
term_definitions = <
    ["en"] = <
        ["at0000"] = <text = <"Blood pressure">; description = <"Measurement of arterial blood pressure.">>
    >
    ["pt"] = <
        ["at0000"] = <text = <"Pressão arterial">; description = <"...">>
    >
>
```

### Term Bindings

Map node IDs to external terminology codes:

```adl
term_bindings = <
    ["SNOMED-CT"] = <
        ["at0004"] = <http://snomed.info/id/271649006>  -- Systolic blood pressure
    >
    ["LOINC"] = <
        ["at0004"] = <http://loinc.org/id/8480-6>
    >
>
```

### Constraint Bindings

Map constraint codes to terminology value sets:

```adl
constraint_bindings = <
    ["SNOMED-CT"] = <
        ["ac0001"] = <terminology://snomed-ct/query?subset=blood_pressure_positions>
    >
>
```

## Template Syntax

Templates in ADL 2 are syntactically archetypes with `template` keyword:

```adl
template (adl_version=2.0.6; rm_release=1.1.0)
    openEHR-EHR-COMPOSITION.encounter-vitals.v1
specialize
    openEHR-EHR-COMPOSITION.encounter.v1

definition
    COMPOSITION[at0000] matches {
        content matches {
            use_archetype OBSERVATION[at0001, openEHR-EHR-OBSERVATION.blood_pressure.v2]
            use_archetype OBSERVATION[at0002, openEHR-EHR-OBSERVATION.heart_rate.v2]
        }
    }
```

## ADL 1.4 (Legacy)

ADL 1.4 is the earlier version of the Archetype Definition Language, still widely used in production systems. While ADL 2 is the current specification, many deployed archetypes, tools, and repositories continue to use ADL 1.4 syntax.

### dADL Syntax

ADL 1.4 uses **dADL** (Data ADL) for the language, description, and ontology sections -- a data instance notation that later evolved into [[odin|ODIN]]. dADL expresses object data using angle-bracket delimiters:

```adl
original_language = <[iso_639-1::en]>
term_definitions = <
    ["en"] = <
        items = <
            ["at0000"] = <
                text = <"blood pressure">;
                description = <"measurement of arterial blood pressure">
            >
        >
    >
>
```

### Key Differences from ADL 2

| Feature | ADL 1.4 | ADL 2 |
|---------|---------|-------|
| **Header** | `archetype (adl_version=1.4)` with separate `concept` section | `archetype (adl_version=2.0.6; rm_release=1.1.0)` |
| **Tuple constraints** | Not supported -- unit/magnitude pairs constrained separately | Supported via `[units, magnitude] matches { ... }` syntax |
| **Slot syntax** | `include`/`exclude` with assertion expressions | Same structure, but with refined matching semantics |
| **Specialisation encoding** | Encoded via hyphens in the `concept_id` segment of the archetype ID (e.g., `problem-diagnosis`) | Uses explicit `specialize` keyword; ID structure is independent |
| **Terminology section** | Named `ontology`; uses `ARCHETYPE_ONTOLOGY` class | Named `terminology`; uses `ARCHETYPE_TERMINOLOGY` class |
| **Node ID format** | `at0000` codes with dot-based specialisation depth (e.g., `at0001.1`) | Same at-codes but with refined id-code semantics |

### Archetype Identification in ADL 1.4

ADL 1.4 archetype IDs follow the pattern `{rm_publisher}-{rm_closure}-{rm_class}.{concept_id}.v{version}`. Specialisation is encoded by appending hyphenated segments to the concept_id (e.g., `openEHR-EHR-EVALUATION.problem.v1` specialises to `openEHR-EHR-EVALUATION.problem-diagnosis.v1`). See [[archetype-identification]] for the full identification scheme across both versions.

### Production Usage

ADL 1.4 remains the dominant format in production openEHR deployments. The REST API Definition service supports both ADL 1.4 and ADL 2 template uploads (at `/definition/template/adl1.4` and `/definition/template/adl2` respectively). Most clinical archetypes in the openEHR Clinical Knowledge Manager (CKM) are authored in ADL 1.4 format.
