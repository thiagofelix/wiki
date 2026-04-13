---
title: Archetype Query Language (AQL)
type: entity
sources:
  - raw/query-aql.md
created: 2026-04-13
updated: 2026-04-13
---

# Archetype Query Language (AQL)

AQL is a declarative query language for searching and retrieving data from archetype-based repositories. It is portable across all openEHR implementations because queries reference archetype paths rather than database schemas.

**Release**: QUERY 1.1.0 (STABLE)

## Why AQL?

Traditional query languages (SQL, XQuery) depend on specific data schemas. If two hospitals use different database schemas, the same SQL query won't work on both. AQL solves this by querying against the **archetype model** — which is standardized and shared.

Key advantages:
- **Portable**: Same query works on any openEHR system
- **Semantic**: Queries expressed in clinical terms via archetype paths
- **Fine-grained**: Retrieve data at any granularity (full composition down to individual data points)
- **Multi-level**: Leverages the hierarchical archetype structure

## Syntax Overview

AQL is SQL-like with openEHR-specific extensions:

```sql
SELECT
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value AS diastolic,
    c/context/start_time AS date_time
FROM
    EHR[ehr_id/value=$ehrUid]
        CONTAINS COMPOSITION c[openEHR-EHR-COMPOSITION.encounter.v1]
            CONTAINS OBSERVATION o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= 140
ORDER BY c/context/start_time DESC
LIMIT 10
```

## Clauses

### SELECT

Specifies what data to return. Uses identified paths (variable + archetype path).

```sql
SELECT
    e/ehr_id/value,
    c/uid/value,
    o/data[at0001]/.../items[at0004]/value
```

Supports `DISTINCT` for unique results and aliases with `AS`.

### FROM

Defines the data source using archetype containment. The `CONTAINS` operator expresses hierarchical relationships:

```sql
FROM
    EHR e
        CONTAINS COMPOSITION c[openEHR-EHR-COMPOSITION.encounter.v1]
            CONTAINS OBSERVATION o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
```

This reads: "From EHRs, find Compositions matching the encounter archetype that contain Observations matching the blood pressure archetype."

**Archetype predicates** scope data to specific archetypes:
```sql
c[openEHR-EHR-COMPOSITION.encounter.v1]
```

### WHERE

Filtering conditions using comparison and logical operators:

```sql
WHERE
    o/data[at0001]/.../items[at0004]/value/magnitude >= 140
    AND c/context/start_time > '2024-01-01'
    AND e/ehr_status/subject/external_ref/id/value = '12345'
```

### ORDER BY

Sort results:

```sql
ORDER BY c/context/start_time DESC
```

### LIMIT / OFFSET

Pagination:

```sql
LIMIT 50 OFFSET 100
```

## Path Syntax

AQL uses openEHR paths combining RM attribute paths and archetype node identifiers:

```
o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude
│  │         │              │             │              │     └─ RM attribute
│  │         │              │             │              └─ RM attribute
│  │         │              │             └─ archetype node
│  │         │              └─ archetype node
│  │         └─ archetype node
│  └─ RM attribute
└─ variable
```

- Segments before `[atNNNN]` are RM attributes
- `[atNNNN]` brackets are archetype node identifiers
- Can mix RM and archetype path segments

## Variables

Variables reference RM classes in the FROM clause:

```sql
FROM EHR e
    CONTAINS COMPOSITION c
        CONTAINS OBSERVATION o
-- e, c, o are variables
```

Rules: start with letter, alphanumeric + underscore, case-insensitive, unique per query.

## Parameters

Runtime-substitutable values prefixed with `$`:

```sql
WHERE e/ehr_id/value = $ehrUid
  AND o/.../items[at0004]/value/magnitude > $systolicThreshold
```

Parameters are resolved by the application layer before query execution.

## Predicates

### Standard Predicate
```sql
[ehr_id/value = '12345']
```

### Archetype Predicate
```sql
[openEHR-EHR-OBSERVATION.blood_pressure.v1]
```

### Node Predicate
```sql
[at0004]                           -- by archetype node ID
[at0004 and name/value = 'Systolic']  -- with name constraint
[at0004, 'Systolic']               -- shortcut form
```

## Operators

### Comparison
`=`, `!=`, `>`, `>=`, `<`, `<=`, `LIKE`, `matches`

### LIKE Operator
Pattern matching with wildcards:
- `*` — zero or more characters
- `?` — single character

```sql
WHERE c/context/start_time LIKE '2024-0?-*'
```

### matches Operator
Advanced matching against value lists or terminology queries:

```sql
-- Value list
WHERE o/.../code_string matches {'18919-1', '18961-3', '19000-9'}

-- Terminology URI
WHERE diagnosis/.../defining_code
    matches { terminology://snomed-ct/hierarchy?rootConceptId=50043002 }

-- TERMINOLOGY() function
WHERE p/.../code_string
    matches TERMINOLOGY('expand', 'hl7.org/fhir/4.0',
        'http://snomed.info/sct?fhir_vs=isa/50697003')
```

### Logical
`AND`, `OR`, `NOT`, `EXISTS`, `NOT EXISTS`

```sql
WHERE EXISTS o/data[at0001]/.../items[at0033]
  AND NOT EXISTS o/data[at0001]/.../items[at0034]
```

## Aggregate Functions

`COUNT`, `MIN`, `MAX`, `SUM`, `AVG`

```sql
SELECT
    COUNT(c/uid/value) AS visit_count,
    MAX(o/.../items[at0004]/value/magnitude) AS max_systolic,
    AVG(o/.../items[at0004]/value/magnitude) AS avg_systolic
FROM ...
```

## Other Functions

### String Functions
`LENGTH`, `POSITION`, `SUBSTRING`, `CONCAT`, `CONCAT_WS`

### Numeric Functions
`ABS`, `MOD`, `CEIL`, `FLOOR`, `ROUND`

### Date/Time Functions
`CURRENT_DATE`, `CURRENT_TIME`, `CURRENT_DATE_TIME`, `NOW`, `CURRENT_TIMEZONE`

### Terminology Function
`TERMINOLOGY(operation, service, params)` — integrates external terminology services into queries.

## CONTAINS Operator

The distinctive AQL feature. Expresses hierarchical containment relationships from the RM:

```sql
-- EHR contains Composition contains Observation
EHR CONTAINS COMPOSITION CONTAINS OBSERVATION

-- Boolean logic in containment
COMPOSITION CONTAINS (OBSERVATION OR EVALUATION)

-- NOT CONTAINS
COMPOSITION NOT CONTAINS OBSERVATION[openEHR-EHR-OBSERVATION.lab_test.v1]
```

This is what makes AQL portable — it queries against the logical archetype structure rather than physical storage.
