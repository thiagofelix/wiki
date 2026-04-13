---
title: Data Types
type: entity
sources:
  - raw/rm-data-types.md
created: 2026-04-13
updated: 2026-04-13
---

# Data Types Information Model

The openEHR data types are clinically-aware types designed for health information. All types use the `DV_` prefix and inherit from `DATA_VALUE`.

**Release**: RM 1.1.0 (STABLE)

## Design Criteria

1. **Clarity of expression** — clearly convey clinical domain semantics
2. **Ease of implementation** — compatible with OO languages (Java, C#, Python, etc.)
3. **Interoperability** — compatible with ISO 13606, HL7v3 data types

## Package Structure

| Package | Key Types | Purpose |
|---------|-----------|---------|
| `basic` | DV_BOOLEAN, DV_STATE, DV_IDENTIFIER | Booleans, state machines, real-world entity IDs |
| `text` | DV_TEXT, DV_CODED_TEXT, CODE_PHRASE | Plain and coded text, terminology integration |
| `quantity` | DV_QUANTITY, DV_COUNT, DV_PROPORTION, DV_ORDINAL | Measurable values |
| `date_time` | DV_DATE, DV_TIME, DV_DATE_TIME, DV_DURATION | Temporal values |
| `encapsulated` | DV_MULTIMEDIA, DV_PARSABLE | Binary/complex data |
| `uri` | DV_URI, DV_EHR_URI | Resource locators |

## Basic Package

### DV_BOOLEAN
True boolean data (yes/no). Not for enumerations — male/female should be coded, not boolean.

### DV_STATE
State values obeying archetype-defined state machines (e.g., medication order lifecycle). Contains a DV_CODED_TEXT value and `is_terminal` flag.

### DV_IDENTIFIER
Real-world entity identifiers (driver's license, SSN, passport, prescription ID). Fields:
- `id` (mandatory) — the identifier value
- `issuer` — authority issuing the ID type
- `assigner` — organization creating the ID
- `type` — kind of identifier

**Not** for infrastructure identifiers (use OBJECT_ID/OBJECT_REF instead).

## Text Package

### DV_TEXT
Any textual value. Attributes:
- `value` — the text string
- `formatting` — optional format indicator
- `hyperlink` — optional DV_URI
- `mappings` — optional term mappings

### DV_CODED_TEXT
Text with a bound terminology code. Inherits from DV_TEXT, adds:
- `defining_code` — CODE_PHRASE linking to a terminology

Use DV_CODED_TEXT when text must be coded. Use DV_TEXT where either coded or free text is acceptable.

### CODE_PHRASE
A terminology code reference:
- `terminology_id` — which terminology (e.g., "SNOMED-CT", "local", "openehr")
- `code_string` — the code or expression within that terminology

### TERM_MAPPING
Maps a DV_CODED_TEXT to equivalent codes in other terminologies:
- `match` — equivalence: `=` (equivalent), `>` (broader), `<` (narrower), `?` (unknown)
- `target` — CODE_PHRASE in the target terminology
- `purpose` — why the mapping exists

## Quantity Package

### DV_QUANTITY
The primary measurable data type:
- `magnitude` — numeric value (Real)
- `units` — UCUM unit string (e.g., "mm[Hg]", "kg", "mg/dL")
- `precision` — number of decimal places (-1 = unlimited)
- `magnitude_status` — qualifier: `=`, `<`, `>`, `<=`, `>=`, `~` (approximate)
- `normal_range` — reference range (DV_INTERVAL)
- `other_reference_ranges` — additional ranges (e.g., therapeutic, critical)

### DV_COUNT
Countable quantities (integer magnitude, no units).

### DV_PROPORTION
Ratios: numerator/denominator with proportion kind:
- `pk_ratio` (0): unitary ratio (e.g., 1:128)
- `pk_unitary` (1): unitary proportion (e.g., mL/mL)
- `pk_percent` (2): percentage
- `pk_fraction` (3): integer fraction (e.g., 1/2)
- `pk_integer_fraction` (4): integer fraction with integer result

### DV_ORDINAL
Ordinal values pairing integers with coded terms. Used for scales like pain scores, Glasgow Coma Scale, Apgar scores:
- `value` — integer ordinal value
- `symbol` — DV_CODED_TEXT label

### DV_QUANTIFIED (abstract)
Abstract parent of all quantifiable types. Adds `magnitude_status` for qualifying measurements as approximate, greater-than, etc.

## Date/Time Package

| Type | Format Example | Description |
|------|---------------|-------------|
| DV_DATE | 2024-03-15 | Calendar date (partial dates allowed: 2024-03, 2024) |
| DV_TIME | 14:30:00.000+01:00 | Time of day (partial allowed) |
| DV_DATE_TIME | 2024-03-15T14:30:00Z | Combined date+time |
| DV_DURATION | P1Y2M3DT4H5M6S | ISO 8601 duration |

All support partial values where components are unknown.

## Encapsulated Package

### DV_MULTIMEDIA
Binary multimedia content:
- `media_type` — MIME type (e.g., "image/jpeg", "application/pdf")
- `data` — binary content (inline)
- `uri` — external reference (alternative to inline data)
- `size` — content size in bytes

### DV_PARSABLE
Parsable text content (formulas, rules, markup):
- `value` — the parsable string
- `formalism` — name of the formalism (e.g., "GLIF", "proforma", "markdown")

## URI Package

### DV_URI
Any URI reference.

### DV_EHR_URI
openEHR-specific URI for referencing EHR data:
```
ehr://system_id/ehr_id/path/to/data
```

## Reference Ranges

DV_ORDERED types (DV_QUANTITY, DV_COUNT, DV_DATE_TIME, etc.) support:
- `normal_range` — the normal reference range as DV_INTERVAL
- `other_reference_ranges` — named ranges (therapeutic, critical, panic)
- `normal_status` — coded normal/abnormal/high/low status
