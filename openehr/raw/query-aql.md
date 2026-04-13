# Archetype Query Language (AQL)

**Issuer:** openEHR Specification Program
**Release:** QUERY Release-1.1.0
**Status:** STABLE
**Keywords:** query, AQL, archetype, Xpath, openehr

**Source:** https://specifications.openehr.org/releases/QUERY/latest/AQL.html

---

## Table of Contents

1. [Preface](#preface)
2. [Overview](#overview)
3. [AQL Syntax Description](#aql-syntax-description)
4. [Result Structure](#result-structure)
5. [Writing AQL Manually](#writing-aql-manually)
6. [AQL Syntax Specification](#aql-syntax-specification)

---

## Preface

### Purpose

This document describes the syntax of the openEHR Archetype Query Language (AQL), a declarative query language designed for searching and retrieving data from archetype-based repositories.

### Status

This specification is STABLE. The latest development version is available at https://specifications.openehr.org/releases/QUERY/latest/AQL.html.

### Tools

Modeling tools for working with archetypes and templates are listed at https://www.openehr.org/downloads/modellingtools.

### Feedback

- **Forum:** https://discourse.openehr.org/c/specifications/aql
- **Issue Tracker:** https://specifications.openehr.org/components/QUERY/open_issues

---

## Overview

### Existing Query Languages

Traditional database query languages (SQL, XQuery, OQL) depend on specific data schemas and physical representations. They lack portability across systems with different underlying architectures. Modern web-oriented languages (SPARQL, GraphQL) address some issues but remain limited to single-level semantic representation.

### What is AQL?

AQL is a declarative query language for archetype-based repositories. Its design emphasizes:

- **Portability:** Schema-independent queries shareable across systems
- **Multi-level modeling:** Support for hierarchical archetype structures
- **Semantic clarity:** Queries expressed in archetype and reference model terms
- **Fine-grained results:** Retrieval of objects at any granularity level

Key features include:

1. openEHR path syntax for archetype node location
2. CONTAINS operator for hierarchical data relationships
3. ADL-like operator syntax (matches, exists, not)
4. Model-neutral design
5. Parameter support for query reusability
6. Aggregate and string functions
7. Result ordering and pagination

### AQL Example

```sql
SELECT
   o/data[at0001]/.../items[at0004]/value AS systolic,
   o/data[at0001]/.../items[at0005]/value AS diastolic,
   c/context/start_time AS date_time
FROM
   EHR[ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c[openEHR-EHR-COMPOSITION.encounter.v1]
         CONTAINS OBSERVATION o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
   o/data[at0001]/.../items[at0004]/value/value >= 140 OR
   o/data[at0001]/.../items[at0005]/value/value >= 90
ORDER BY c/context/start_time DESC
```

---

## AQL Syntax Description

### Reserved Words and Characters

**Keywords (case-insensitive):**
- SELECT, AS, FROM, CONTAINS, WHERE
- ORDER BY, LIMIT, OFFSET
- DISTINCT, AND, OR, NOT
- EXISTS, LIKE, matches

**Functions:** COUNT, MIN, MAX, SUM, AVG, LENGTH, POSITION, SUBSTRING, CONCAT, CONCAT_WS, ABS, MOD, CEIL, FLOOR, ROUND, CURRENT_DATE, CURRENT_TIME, CURRENT_DATE_TIME, NOW, CURRENT_TIMEZONE, TERMINOLOGY

**Literals:** true, false, NULL

**Special Characters:**
- `"` and `'` -- string delimiters
- `|` -- interval delimiters
- `[]` -- coded terms and predicates
- `{}` -- matches criteria
- `()` -- function calls and grouping
- `$` -- parameter prefix
- `/`, `.` -- path syntax

**Note:** TOP is deprecated in favor of LIMIT with ORDER BY.

### openEHR Path Syntax

openEHR paths reference both archetype nodes and reference model attributes.

#### Archetype Path Examples

| RM Type | Node Name | Archetype ID | Path Syntax | Referenced Type |
|---------|-----------|--------------|-------------|-----------------|
| OBSERVATION | Apgar score | openEHR-EHR-OBSERVATION.apgar.v1 | `/` | OBSERVATION |
| OBSERVATION | Heart rate | openEHR-EHR-OBSERVATION.pulse.v1 | `/data[at0002]/events[at0003]/data[at0001]/items[at0004]` | ELEMENT |
| OBSERVATION | Systolic | openEHR-EHR-OBSERVATION.blood_pressure.v2 | `/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value` | DV_QUANTITY |

#### RM Class Attribute Path Examples

| Attribute | Path Syntax |
|-----------|-------------|
| COMPOSITION.category | `/category` |
| COMPOSITION.context.start_time | `/context/start_time` |
| COMPOSITION.uid.value | `/uid/value` |

### Variables

Variables reference specific openEHR classes in the FROM clause.

**Syntax Rules:**
- Must start with a letter followed by alphanumerics and underscores
- Names are case-insensitive
- Must be unique within a query
- Digits at the start are discouraged
- Cannot clash with reserved words

Variables combine with paths to form identified paths used in SELECT and WHERE clauses.

### Parameters

Parameters enable query reusability by substituting runtime values.

**Syntax:** Parameter names start with `$` followed by letters, digits, or underscores. No spaces allowed; cannot use reserved words.

**Usage Examples:**
```
[ehr_id/value=$ehrUid]
[at0003, $nameValue]
o/data[at0001]/.../items[at0004]/value/value > $systolicCriteria
```

**Resolution:** Parameters are typically resolved at application or EHR system level outside the query engine. Parameter names serve as keys within specific boundaries.

### Predicates

Predicates define filtering criteria using bracket notation.

#### Standard Predicate

Format: `[left-operand operator right-operand]`

Example: `[ehr_id/value='123456']`

Left operand: openEHR path
Right operand: criterion value or parameter
Operators: `>`, `>=`, `=`, `<`, `<=`, `!=`

#### Archetype Predicate

Shortcut format containing only archetype ID:

```
[openEHR-EHR-COMPOSITION.encounter.v1]
```

Used in FROM clauses to scope data source.

#### Node Predicate

Multiple forms available:

**Form 1 -- archetype_node_id only:**
```
[at0002]
// Standard equivalent: [archetype_node_id=at0002]
```

**Form 2 -- archetype_node_id with name/value:**
```
[at0002 and name/value=$nameValue]
[at0002 and name/value='real name value']
// Standard equivalents shown with explicit syntax
```

**Form 3 -- shortcut name/value syntax:**
```
[at0002, $nameValue]
[at0002, 'real name value']
```

**Form 4 -- name term code criterion:**
```
[at0002, at0003]
[at0002, snomed_ct(3.1)::313267000]
[at0003, icd10AM::F60.1|Schizoid personality disorder|]
```

**Form 5 -- advanced general criterion:**
```
[at0002 and value/defining_code/terminology_id/value=$terminologyId]
```

### Identified Paths

An identified path combines variable reference, optional predicate, and/or openEHR path.

**Forms:**

1. Variable + path:
```
o/data[at0001]/.../data[at0003]/items[at0004]/value/value
```

2. Variable + predicate:
```
o[name/value=$nameValue]
```

3. Variable + predicate + path:
```
o[name/value=$nameValue]/data[at0001]/.../data[at0003]/items[at0004]/value/value
```

### Operators

#### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| = | Equal | `name/value = $nameValue` |
| > | Greater than | `items[at0004]/value/value > 140` |
| >= | Greater than or equal | `items[at0004]/value/value >= 140` |
| < | Less than | `items[at0004]/value/value < 160` |
| <= | Less than or equal | `items[at0004]/value/value <= 160` |
| != | Not equal | `template_id/value != ''` |
| LIKE | Pattern matching | `name/value LIKE 'left *'` |
| matches | Advanced matching | `code_string matches {'18919-1', '18961-3'}` |

##### LIKE Operator

Matches strings against simple patterns using wildcards:
- `?` -- matches any single character
- `*` -- matches zero or more characters
- Escape with `\` for literal `?` or `*`

Example:
```sql
WHERE c/context/start_time LIKE '2019-0?-*'
```

##### matches Operator

Supports three right-hand operand forms:

**Form 1 -- cADL list constraint:**
```sql
WHERE o/data[at0002]/.../items[at0018]/name/defining_code/code_string
  matches {'18919-1', '18961-3', '19000-9'}
```

Value list items may be strings, dates/times, integers, or reals. Quotes required for strings and dates/times.

**Form 2 -- URI:**
```sql
WHERE diagnosis/data/items[at0002.1]/value/defining_code
  matches { terminology://snomed-ct/hierarchy?rootConceptId=50043002 }
```

Terminology URI components:
- Scheme: `terminology`
- Authority: service identifier (e.g., SNOMED-CT)
- Path: function name (e.g., hierarchy)
- Query: argument values

**Form 3 -- TERMINOLOGY() function results:**
```sql
WHERE p/data/items[at0002]/value/defining_code/code_string
  matches TERMINOLOGY('expand', 'hl7.org/fhir/4.0',
    'http://snomed.info/sct?fhir_vs=isa/50697003')
```

#### Logical Operators

**AND:** Binary operator representing logical conjunction. Returns true only when both operands evaluate true.

**OR:** Binary operator representing logical disjunction. Returns true when any operand evaluates true.

**NOT:** Unary operator negating Boolean expressions.

Example with NOT in WHERE:
```sql
WHERE NOT (EXISTS c/content[openEHR-EHR-ADMIN_ENTRY.discharge.v1] AND
   e/ehr_status/subject/external_ref/namespace = 'CEC')
```

NOT with CONTAINS exclusion:
```sql
FROM EHR e CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.administrative_encounter.v1]
   NOT CONTAINS ADMIN_ENTRY admission [openEHR-EHR-ADMIN_ENTRY.admission.v1]
```

**EXISTS:** Unary operator checking for data existence at specified path.

Example:
```sql
WHERE NOT EXISTS c/content[openEHR-EHR-ADMIN_ENTRY.discharge.v1]
```

### Functions

AQL provides built-in functions for data manipulation. Function syntax: `function(expression, expression, ...)`

Two types:
- **Single-row functions:** Return one result per data row
- **Aggregate functions:** Return single result from multiple rows

#### Aggregate Functions

| Function | Description |
|----------|-------------|
| COUNT() | Count of rows or values |
| MIN() | Minimum non-null value |
| MAX() | Maximum non-null value |
| SUM() | Sum of non-null values |
| AVG() | Average of non-null values |

**COUNT():** `COUNT([DISTINCT] expression|*)`
- DISTINCT filters duplicate values
- COUNT(*) includes NULL values
- Returns 0 if no matching rows
- Return type: Integer

**MIN():** `MIN(expression)`
- Input types: String, Date, Time, Integer, Real
- Return type matches input type
- Returns NULL if no matching rows

**MAX():** `MAX(expression)`
- Input types: String, Date, Time, Integer, Real
- Return type matches input type
- Returns NULL if no matching rows

**SUM():** `SUM(expression)`
- Input types: Integer, Real
- Return type matches input type
- Returns NULL if no matching rows

**AVG():** `AVG(expression)`
- Input types: Integer, Real
- Return type matches input type
- Returns NULL if no matching rows

Example:
```sql
SELECT
   MAX(o/data[at0001]/.../items[at0004]/value/magnitude) AS maxValue,
   MIN(o/data[at0001]/.../items[at0004]/value/magnitude) AS minValue,
   AVG(o/data[at0001]/.../items[at0004]/value/magnitude) AS meanValue
FROM
   EHR e CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION o [openEHR-EHR-OBSERVATION.blood_pressure.v1]
```

#### String Functions

| Function | Description |
|----------|-------------|
| LENGTH() | Character count |
| CONTAINS() | Substring presence validation |
| POSITION() | First occurrence position |
| SUBSTRING() | Substring extraction |
| CONCAT() | String concatenation |
| CONCAT_WS() | Concatenation with separator |

**LENGTH():** `LENGTH(expression)`
- Argument type: String
- Returns: Integer (character count)

**CONTAINS():** `CONTAINS(expression, substring)`
- Argument types: String, String
- Returns: Boolean

**POSITION():** `POSITION(substring, expression)`
- Returns position of first occurrence (1-indexed)
- Returns 0 if not found
- Argument types: String, String
- Returns: Integer

**SUBSTRING():** `SUBSTRING(expression, position, length)`
- Extracts substring starting at position
- Length argument optional; defaults to end of string
- Position is 1-indexed
- Argument types: String, Integer, Integer
- Returns: String

**CONCAT():** `CONCAT(expr1, expr2, ...)`
- Accepts one or more String arguments
- Returns concatenated String

**CONCAT_WS():** `CONCAT_WS(separator, expr1, expr2, ...)`
- Inserts separator between arguments
- Argument types: String, String, String, ...
- Returns: String

#### Numeric Functions

| Function | Description |
|----------|-------------|
| ABS() | Absolute value |
| MOD() | Remainder |
| CEIL() | Ceiling |
| FLOOR() | Floor |
| ROUND() | Rounding |

**ABS():** `ABS(expression)`
- Argument types: Real, Integer
- Return type matches input

**MOD():** `MOD(x, y)`
- Returns remainder of x divided by y
- Argument types: Real, Integer
- Return type matches input

**CEIL():** `CEIL(expression)`
- Returns Integer >= argument
- Argument types: Real, Integer

**FLOOR():** `FLOOR(expression)`
- Returns Integer <= argument
- Argument types: Real, Integer

**ROUND():** `ROUND(expression, decimal)`
- Rounds to decimal places (default 0)
- Argument types: Real/Integer, Integer
- Returns: Result type matches expression type

#### Date and Time Functions

| Function | Description |
|----------|-------------|
| CURRENT_DATE() | Current date (YYYY-MM-DD) |
| CURRENT_TIME() | Current time (hh:mm:ss) |
| CURRENT_DATE_TIME() / NOW() | Current datetime (ISO 8601) |
| CURRENT_TIMEZONE() | Current timezone (+-hh:mm) |

All accept zero arguments and return String values.

#### TERMINOLOGY Function

Invokes external terminology servers for value set operations.

**Syntax:** `TERMINOLOGY(operation, service_api, params_uri)`

**Arguments (all String):**
- operation: Action to perform
- service_api: Terminology service identifier
- params_uri: RFC 3986 compliant URI

**Common Operations:**
- expand: Retrieve all codes in value set
- validate: Check code belongs to value set
- lookup: Retrieve code information
- map: Translate between value sets
- subsumes: Test subsumption relationship

**Example Service APIs:**
- hl7.org/fhir/4.0
- hl7.org/fhir/3.0
- hl7.org/fhir/1.0
- ots.oceanhealthsystems.com
- bts.better.care

**Usage in WHERE:**

Direct match with results:
```sql
WHERE e/value/defining_code/code_string
  matches TERMINOLOGY('expand', 'hl7.org/fhir/4.0',
    'http://snomed.info/sct?fhir_vs=isa/50697003')
```

Merging explicit codes with results:
```sql
WHERE e/value/defining_code/code_string
  matches {'http://snomed.info/id/442031002',
    TERMINOLOGY('expand', 'hl7.org/fhir/4.0', 'http://snomed.info/sct')}
```

Boolean assertion:
```sql
WHERE TERMINOLOGY('validate', 'hl7.org/fhir/r4',
  'system=http://snomed.info/sct&code=122298005') = true
```

### Expressions

Combinations of literals, operators, variables, predicates, parameters, or functions evaluating to values.

#### Class Expressions

Used in FROM clause for two purposes:
1. Scope data source with RM class constraints
2. Define class variables for reference in other clauses

**Syntax components (1 mandatory, at least 1 optional):**
1. RM class name (mandatory)
2. Variable name (optional)
3. Standard or archetype predicate (optional)

Examples:
```sql
EHR e[ehr_id/value=$ehrUid]
COMPOSITION c[openEHR-EHR-COMPOSITION.report.v1]
```

#### Identified Expression

Specifies matching criteria in WHERE clause.

**Form 1 -- Unary operator:**
```sql
NOT EXISTS path
EXISTS path
```

**Form 2 -- Binary operator:**

Structure:
- Left operand: identified path or function with identified path
- Operator: comparison operator (>, >=, =, <, <=, !=, LIKE, matches)
- Right operand: literal, function, parameter, or identified path

Examples:
```sql
o/data[at0001]/.../items[at0004]/value/value >= 140
c/archetype_details/template_id/value = 'health_encounter'
c/archetype_details/template_id/value = $templateParameter
c/archetype_details/template_id/value LIKE '*encounter*'
o/data[...]/value > o1/data[...]/value
```

### Literals

Fixed values supplied directly in AQL, not derived from identified paths, variables, or aliases.

**Types:**
- Strings: quoted with `'` or `"`
- Numbers: unquoted
- Booleans: unquoted (true/false)
- Dates/times: quoted, ISO 8601 format
- NULL: unquoted keyword

Can be used in SELECT clause as column expressions or WHERE clause as identified expression components.

### Built-in Types

#### Integer Data

Numeric literals without decimal points: `1`, `2`, `365`, `-1`

No comma/period separators; hexadecimal unsupported.

#### Real Data

Decimal literals with decimal point: `3.1415926`, `-1.0`

No comma/period separators.

#### Boolean Data

Case-insensitive literals: `true` or `false`

#### String Data

Single or double-quoted: `'encounter'` or `"encounter"`

Line breaks unsupported.

#### Dates and Times

String literals in ISO 8601 format (quoted).

Formats allowed:
- Basic: `19860101` (interpreted as string)
- Extended: `1986-01-01` (interpreted as date)

Complete or partial values permitted. Extended format recommended.

Datetime example:
```sql
'1986-01-01T12:00:00.000+09:30'
```

Date example:
```sql
'1986-01-01'
```

---

## Query Structure

### Overview

AQL queries must follow this clause order:

1. SELECT (mandatory)
2. FROM (mandatory)
3. WHERE (optional)
4. ORDER BY (optional)
5. LIMIT (optional)

Minimum requirement: SELECT and FROM clauses.

### FROM Clause

Specifies data subset available to remaining clauses.

**Purpose:**
- Defines scope using RM classes and containment
- Filters based on archetype constraints
- Establishes variables for other clauses

**Requirements:**
- Classes must be defined by Reference Model
- Predicates in class expressions provide additional filtering

**Clause order in query:**
1. FROM: Defines data subset
2. WHERE: Filters matched data
3. Class expression predicates: Further filtering
4. SELECT: Final projection of matched data

**Syntax:**

Simple FROM with containment:
```sql
FROM
   EHR e [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.report.v1]
```

#### Containment

Specifies hierarchical relationships between parent and child data items.

**Syntax:** `CONTAINS` operator between class expressions

Example:
```sql
EHR e CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.referral.v1]
```

**Multiple containment constraints using AND/OR:**
```sql
EHR e CONTAINS
   COMPOSITION c [openEHR-EHR-COMPOSITION.referral.v1]
   AND COMPOSITION c1 [openEHR-EHR-COMPOSITION.report.v1]

EHR e CONTAINS
   COMPOSITION c [openEHR-EHR-COMPOSITION.referral.v1]
      CONTAINS (OBSERVATION o [openEHR-EHR-OBSERVATION.laboratory-hba1c.v1]
         OR OBSERVATION o1 [openEHR-EHR-OBSERVATION.laboratory-glucose.v1])
```

**Exclusion constraints using NOT CONTAINS:**
```sql
EHR e CONTAINS
   COMPOSITION c [openEHR-EHR-COMPOSITION.referral.v1]
      NOT CONTAINS OBSERVATION o [openEHR-EHR-OBSERVATION.laboratory_test_result.v1]
```

### WHERE Clause

Applies additional criteria to data items in FROM clause.

**Purpose:** Expresses query criteria not representable in other clauses.

**Syntax:** WHERE keyword followed by one or more identified expressions.

Logical operators AND, OR, NOT and parentheses combine multiple expressions.

Examples:
```sql
WHERE
   c/name/value=$nameValue AND c/archetype_details/template_id/value=$templateId

WHERE
   (c/name/value = $nameValue OR c/archetype_details/template_id/value = $templateId) AND
   o/data[at0001]/.../items[at0004]/value/value >= 140
```

### SELECT Clause

Specifies data to retrieve from query results.

**Syntax:** SELECT keyword, optional DISTINCT, optional TOP (deprecated), one or more column expressions.

Column expression types:
- Identified path: Data at specified path
- Function: Built-in function call result
- Literal value: Fixed value
- Variable name: Full object (returns entire object like COMPOSITION)

Multiple expressions separated by commas.

**Examples:**

Example 1 -- Identified paths with aliases:
```sql
SELECT
   c/name/value AS Name,
   c/context/start_time AS date_time,
   c/composer/name AS Composer
FROM
   EHR e [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c
```

Example 2 -- Full object retrieval:
```sql
SELECT c
FROM
   EHR e [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c
```

Example 3 -- Literals and functions:
```sql
SELECT
   true AS dangerousBP,
   "alert" as indication,
   count(*) as counter
FROM
   EHR [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION [openEHR-EHR-COMPOSITION.encounter.v1]
         CONTAINS OBSERVATION obs [openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
   obs/data[at0001]/.../items[at0004]/value/magnitude >= 160 OR
   obs/data[at0001]/.../items[at0005]/value/magnitude >= 110
```

#### DISTINCT

Modifier filtering duplicate rows from result set.

Rows considered duplicates if all corresponding column values match.

Example:
```sql
SELECT DISTINCT
   c/name/value AS Name,
   c/composer/name AS Composer
FROM
   EHR e [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c
```

#### TOP (Deprecated)

**Status:** Deprecated since Release 1.1.0; use LIMIT with ORDER BY instead.

Will be removed in future major release. Cannot use TOP and LIMIT together.

Syntax: `TOP row_count [BACKWARD|FORWARD]`

#### Name Alias

Renames retrieved data using AS keyword.

Alias must follow AQL variable naming syntax rules.

Example:
```sql
SELECT
   o/data[at0001]/.../items[at0004]/value/magnitude AS systolic
```

### ORDER BY Clause

Sorts returned results.

**Note:** Without ORDER BY, result ordering is undefined per specification.

**Syntax:** ORDER BY keyword followed by one or more sorting expressions.

Sorting expression: identified path, optional sort direction keyword.

Direction keywords:
- DESC / DESCENDING (descending order)
- ASC / ASCENDING (ascending order, default)

Examples:
```sql
ORDER BY c/name/value DESC

ORDER BY c/context/start_time ASC, c/name/value DESC
```

**Behavior:** When leftmost expression values equal between rows, comparison proceeds to next expression. Requires comparable data types.

### LIMIT Clause

Constrains result set with row count and optional offset.

**Syntax:** `LIMIT row_count [OFFSET offset]`

- row_count: Integer >= 1 (maximum rows returned)
- offset: Integer >= 0 (rows to skip, defaults to 0)

**Note:** Deterministic ordering requires ORDER BY clause with LIMIT.

When DISTINCT used, LIMIT applies after duplicate removal.

**Pagination example:**
```sql
SELECT
   c/name/value AS Name,
   c/context/start_time AS date_time,
   c/composer/name AS Composer
FROM
   EHR e [ehr_id/value=$ehrUid]
      CONTAINS COMPOSITION c
ORDER BY c/context/start_time
LIMIT 10 OFFSET 10
```

Returns rows 11-20 when ordered by start_time.

---

## Result Structure

AQL query results are conceptually 2-dimensional tables: `Array<Array<Any>>`, where Any includes all object types, primitive types, or NULL (for missing/unknown data).

Practical implementations typically provide "annotated" result structures including metadata (column descriptors), enabling efficient processing. These annotated results are outside this specification's scope, considered implementation artifacts.

The openEHR Abstract Platform Query Service defines extended result structures for openEHR implementations, available in the openEHR REST Query API as HTTP/JSON mappings.

---

## Writing AQL Manually

### Step 1: The FROM Clause

**Scenario Example:** "Get all abnormal blood pressure values recorded in a health encounter for a specific patient."

**1. EHR Class Expression:**

Determine scope: single EHR or population query.

For single EHR, use parameter for reusability:
```sql
FROM EHR [ehr_id/value=$ehrUid]
```

**2. Archetype Expressions:**

Identify clinical concepts -> corresponding archetypes:
- "blood pressure" -> `openEHR-EHR-OBSERVATION.blood_pressure.v1`
- "health encounter" -> `openEHR-EHR-COMPOSITION.encounter.v1`

Determine variable needs. Variables only needed if referenced by other clauses.

**3. Containment Expression:**

Use openEHR RM to determine hierarchies. Composition is parent of Observation:

```sql
FROM
   EHR [ehr_id/value=$ehrUid]
   CONTAINS COMPOSITION [openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION [openEHR-EHR-OBSERVATION.blood_pressure.v1]
```

### Step 2: The WHERE Clause

**Define criteria:** Abnormal blood pressure = systolic >= 140 OR diastolic >= 90

**Create identified expressions:**

1. Add variable to blood pressure class (needed for path reference):
```sql
OBSERVATION obs [openEHR-EHR-OBSERVATION.blood_pressure.v1]
```

2. Systolic path with operator and value:
```sql
obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/value >= 140
```

3. Diastolic path:
```sql
obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/value >= 90
```

4. Combine with OR:
```sql
WHERE
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/value >= 140 OR
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/value >= 90
```

### Step 3: The SELECT Clause

**Determine return data:** Systolic and diastolic values.

**Build identified paths:** Use variable and paths from WHERE analysis.

**Complete query:**
```sql
SELECT
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude,
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude
FROM
   EHR [ehr_id/value=$ehrUid]
   CONTAINS COMPOSITION [openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION obs [openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= 140 OR
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude >= 90
```

### Step 4: Ordering and Pagination

**Enhanced scenario:** "Get the latest 5 abnormal blood pressure values..."

**Add ordering by datetime:**
```sql
SELECT
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic,
   c/context/start_time AS date_time
FROM
   EHR [ehr_id/value=$ehrUid]
   CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION obs [openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= 140 OR
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude >= 90
ORDER BY
   c/context/start_time DESC
```

**Add LIMIT for pagination:**
```sql
SELECT
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic,
   c/context/start_time AS date_time
FROM
   EHR [ehr_id/value=$ehrUid]
   CONTAINS COMPOSITION c [openEHR-EHR-COMPOSITION.encounter.v1]
      CONTAINS OBSERVATION obs [openEHR-EHR-OBSERVATION.blood_pressure.v1]
WHERE
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude >= 140 OR
   obs/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude >= 90
ORDER BY
   c/context/start_time DESC
LIMIT 5
```

---

## AQL Syntax Specification

The following ANTLR4 grammar formally expresses AQL syntax.

```antlr
//
//  description:  ANTLR4 parser grammar for Archetype Query Language (AQL)
//  authors:      Sebastian Iancu, Code24, Netherlands
//                Teun van Hemert, Nedap, Netherlands
//                Thomas Beale, Ars Semantica UK, openEHR Foundation
//  support:      https://specifications.openehr.org/releases/QUERY/open_issues
//  copyright:    Copyright (c) 2021- openEHR Foundation
//  license:      Creative Commons CC-BY-SA
//

parser grammar AqlParser;

options { tokenVocab=AqlLexer; }

selectQuery
    : selectClause fromClause whereClause? orderByClause? limitClause? SYM_DOUBLE_DASH? EOF
    ;

selectClause
    : SELECT DISTINCT? top? selectExpr (SYM_COMMA selectExpr)*
    ;

fromClause
    : FROM fromExpr
    ;

whereClause
    : WHERE whereExpr
    ;

orderByClause
    : ORDER BY orderByExpr (SYM_COMMA orderByExpr)*
    ;

limitClause
    : LIMIT limit=INTEGER (OFFSET offset=INTEGER)?
    ;

selectExpr
    : columnExpr (AS aliasName=IDENTIFIER)?
    ;

fromExpr
    : containsExpr
    ;

whereExpr
    : identifiedExpr
    | NOT whereExpr
    | whereExpr AND whereExpr
    | whereExpr OR whereExpr
    | SYM_LEFT_PAREN whereExpr SYM_RIGHT_PAREN
    ;

orderByExpr
    : identifiedPath order=(DESCENDING|DESC|ASCENDING|ASC)?
    ;

columnExpr
    : identifiedPath
    | primitive
    | aggregateFunctionCall
    | functionCall
    ;

containsExpr
    : classExprOperand (NOT? CONTAINS containsExpr)?
    | containsExpr AND containsExpr
    | containsExpr OR containsExpr
    | SYM_LEFT_PAREN containsExpr SYM_RIGHT_PAREN
    ;

identifiedExpr
    : EXISTS identifiedPath
    | identifiedPath COMPARISON_OPERATOR terminal
    | functionCall COMPARISON_OPERATOR terminal
    | identifiedPath LIKE likeOperand
    | identifiedPath MATCHES matchesOperand
    | SYM_LEFT_PAREN identifiedExpr SYM_RIGHT_PAREN
    ;

classExprOperand
    : IDENTIFIER variable=IDENTIFIER? pathPredicate?                                       #classExpression
    | VERSION variable=IDENTIFIER? (SYM_LEFT_BRACKET versionPredicate SYM_RIGHT_BRACKET)?  #versionClassExpr
    ;

terminal
    : primitive
    | PARAMETER
    | identifiedPath
    | functionCall
    ;

identifiedPath
    : IDENTIFIER pathPredicate? (SYM_SLASH objectPath)?
    ;

pathPredicate
    : SYM_LEFT_BRACKET (standardPredicate | archetypePredicate | nodePredicate) SYM_RIGHT_BRACKET
    ;

standardPredicate
    : objectPath COMPARISON_OPERATOR pathPredicateOperand
    ;

archetypePredicate
    : ARCHETYPE_HRID
    | PARAMETER
    ;

nodePredicate
    : (ID_CODE | AT_CODE) (SYM_COMMA (STRING | PARAMETER | TERM_CODE | AT_CODE | ID_CODE))?
    | ARCHETYPE_HRID (SYM_COMMA (STRING | PARAMETER | TERM_CODE | AT_CODE | ID_CODE))?
    | PARAMETER
    | objectPath COMPARISON_OPERATOR pathPredicateOperand
    | objectPath MATCHES CONTAINED_REGEX
    | nodePredicate AND nodePredicate
    | nodePredicate OR nodePredicate
    ;

versionPredicate
    : LATEST_VERSION
    | ALL_VERSIONS
    | standardPredicate
    ;

pathPredicateOperand
    : primitive
    | objectPath
    | PARAMETER
    | ID_CODE
    | AT_CODE
    ;

objectPath
    : pathPart (SYM_SLASH pathPart)*
    ;

pathPart
    : IDENTIFIER pathPredicate?
    ;

likeOperand
    : STRING
    | PARAMETER
    ;

matchesOperand
    : SYM_LEFT_CURLY valueListItem (SYM_COMMA valueListItem)* SYM_RIGHT_CURLY
    | terminologyFunction
    | SYM_LEFT_CURLY URI SYM_RIGHT_CURLY
    ;

valueListItem
    : primitive
    | PARAMETER
    | terminologyFunction
    ;

primitive
    : STRING
    | numericPrimitive
    | DATE | TIME | DATETIME
    | BOOLEAN
    | NULL
    ;

numericPrimitive
    : INTEGER
    | REAL
    | SCI_INTEGER
    | SCI_REAL
    | SYM_MINUS numericPrimitive
    ;

functionCall
    : IDENTIFIER SYM_LEFT_PAREN (expression (SYM_COMMA expression)*)? SYM_RIGHT_PAREN
    ;

aggregateFunctionCall
    : aggregateFunction SYM_LEFT_PAREN DISTINCT? aggregateExpr SYM_RIGHT_PAREN
    ;

aggregateFunction
    : COUNT | MIN | MAX | SUM | AVG
    ;

aggregateExpr
    : SYM_MULTIPLY
    | expression
    ;

expression
    : primitive
    | PARAMETER
    | functionCall
    | identifiedPath
    ;

top
    : TOP topCount=(INTEGER) (BACKWARD | FORWARD)?
    ;

terminologyFunction
    : TERMINOLOGY SYM_LEFT_PAREN STRING SYM_COMMA STRING SYM_COMMA STRING SYM_RIGHT_PAREN
    ;
```

---

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/

**Copyright:** (c) 2008 - 2021 The openEHR Foundation
