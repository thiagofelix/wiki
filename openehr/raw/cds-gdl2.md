# Guideline Definition Language v2 (GDL2) Specification

**Status:** STABLE
**Release:** CDS Release-2.0.1
**Issuer:** openEHR Specification Program
**License:** Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Table of Contents

1. [Acknowledgements](#acknowledgements)
2. [Preface](#preface)
3. [Overview](#overview)
4. [Requirements](#requirements)
5. [GDL2 Semantics](#gdl2-semantics)
6. [GDL2 Object Model](#gdl2-object-model)
7. [Syntax Specification](#syntax-specification)
8. [Amendment Record](#amendment-record)

---

## Acknowledgements

### Primary Author

- Rong Chen MD, PhD, Cambio CDS, Sweden

### Contributors

- Thomas Beale, Ars Semantica (UK); openEHR Foundation Management Board

### Support

Funded by Cambio CDS, Sweden

### Trademarks

- 'openEHR' is a trademark of the openEHR Foundation
- 'Java' is a registered trademark of Oracle Corporation
- 'Microsoft' and '.Net' are trademarks of the Microsoft Corporation

---

## 1. Preface

### 1.1. Purpose

This document specifies the design of Guideline Definition Language version 2 (GDL2), a formal language for expressing clinical decision support logic. GDL2 remains agnostic to language, reference terminology, and EHR models while representing a significant evolution from GDL version 1.

### 1.2. Related Documents

Prerequisite reading includes:

- The openEHR Architecture Overview
- openEHR Reference Model specifications
- GDL version 1 specification

### 1.3. Status

This specification is **STABLE**. The development version is available at the openEHR specifications website.

### 1.4. Feedback

- Technical discussion: openEHR technical mailing list
- Issues: Specifications Problem Report tracker
- Change history: CDS component Change Request tracker

### 1.5. A Note on Nomenclature

The terms 'GDL2' and 'GDL' both refer to version 2 of GDL as described in this specification.

### 1.6. Resources

- **GDL-lang site:** Research material and guidelines
- **GitHub repository:** Published GDL guidelines
- **GDL wiki:** Additional documentation

### 1.7. Changes since GDL Version 1

GDL2 introduces:

- Data binding independent of EHR data models (openEHR, ISO 13606, HL7 FHIR)
- Template definitions for output objects with `use_template` statements
- Individual references and item-specific referencing in rules
- Enhanced mathematical function support

Migration guidance available on the gdl-lang site.

---

## 2. Overview

### 2.1. Background

Expressing and sharing computerized clinical decision support across languages and platforms has long presented challenges. Lack of shared clinical information models and flexible terminology support were identified as major barriers. The openEHR information architecture with external terminology provides a foundation for computable guideline development.

### 2.2. Scope

GDL expresses clinical logic as production rules. Discrete rules containing "when-then" statements combine as building blocks for single and complex chained decision-making. Rules drive at-point-of-care decision support and retrospective population analytics.

**Use cases include:**

- Prompts, alerts, and reminders
- Interactive single-screen decision support applications
- Detailed order-sets and care process support
- Algorithm-based calculators
- Personalized care plan generation and updates
- Retrospective compliance checks and outcome measures

### 2.3. An Example: CHA2DS2-VASc Score

GDL guidelines are expressed in either openEHR ODIN or JSON format, representing instances of the GDL2 Object Model. The following ODIN example calculates the CHA2DS2-VASc stroke risk score for atrial fibrillation:

```odin
<
    gdl_version = <"2.0">
    id = <"CHA2DS2-VASc.v1">
    concept = <"gt0001">
    original_language = <[ISO_639-1::en]>
    description = <
        details = <
            ["en"] = <
                copyright = <"Cambio Healthcare Systems">
                keywords = <"Atrial Fibrillation", "Stroke", "CHA2DS2-VASc">
                misuse = <"Do not use in patients without atrial fibrillation diagnosis.">
                purpose = <"Calculates stroke risk in atrial fibrillation patients.">
                use = <"Calculates stroke risk in atrial fibrillation patients.">
            >
        >
        lifecycle_state = <"in_review">
        original_author = <
            ["date"] = <"2016-12-16">
            ["email"] = <"rong.chen@cambio.se">
            ["name"] = <"Rong Chen">
            ["organisation"] = <"Cambio Healthcare Systems">
        >
    >
    definition = <
        pre_conditions = <...>
        data_bindings = <...>
        rules = <...>
    >
    terminology = <
        term_definitions = <...>
        term_bindings = <...>
    >
>
```

#### Data Bindings Example

Data bindings map source data elements to variables:

```odin
data_bindings = <
    ["gt0006"] = <
        model_id = <"openEHR-EHR-EVALUATION.problem-diagnosis.v1">
        type = <"INPUT">
        elements = <
            ["gt0107"] = <
                path = <"/data[at0001]/items[at0002.1]">
            >
        >
    >
>
```

#### Pre-conditions Example

Pre-conditions must be satisfied before rule execution:

```odin
pre_conditions = <"$gt0107|index diagnosis| != null">
```

Additional constraint with predicate:

```odin
predicates = <"/data[at0001]/items[at0002.1] is_a local::gt0105|Atrial fibrillation|">
```

#### Rules Example

Rules contain when-then logic:

```odin
rules = <
    ["gt0018"] = <
        when = <"$gt0108 != null">
        then = <"$gt0014 = 1|local::at0031|Present|">
        priority = (11)
    >
    ["gt0026"] = <
        then = <"$gt0016.magnitude = gt0009.value + $gt0010.value + ...">
        priority = (1)
    >
>
```

#### Terminology Definitions Example

```odin
terminology = <
    term_definitions = <
        ["en"] = <
            ["gt0014"] = <
                text = <"Hypertension">
            >
            ["gt0105"] = <
                text = <"Atrial fibrillation">
            >
        >
    >
    term_bindings = <
        ["ICD10"] = <
            ["gt0105"] = <"ICD10::I48">
        >
    >
>
```

---

## 3. Requirements

### 3.1. Clinical Information Models

- Support for standards-based clinical models (openEHR Archetypes, HL7 FHIR Resources)
- Support for both input and output rule execution
- Common data types underpinning standard clinical models

### 3.2. Natural Language Independence

- Metadata authorable in any natural language
- Rule expressions independent of specific languages
- Rule names independent of specific languages
- Support for multiple language translations without altering logical definitions

### 3.3. Reference Terminology Support

- Bind local terms to single external concepts
- Bind local terms to multiple external concepts
- Bind local terms to externally defined terminology refsets

### 3.4. Identification and Metadata

- Unique rule identification per namespace
- Explicit version information in guideline identifiers
- Sufficient metadata including authorship, purpose, versions, and clinical references

### 3.5. Rule Execution

- Chain execution of multiple guidelines
- Reuse guidelines across different decision support applications and clinical contexts

### 3.6. Complex Output Objects

- Support hierarchical objects as rule execution output
- Alter output structure based on rule execution
- Alter output details based on rule execution
- Support standard and non-standard output formats

### 3.7. Local Variables

- Use local variables for intermediate results
- Use local variables independent of external clinical models

---

## 4. GDL2 Semantics

### 4.1. Rule Structure

GDL2 guidelines structure consists of:

- **Central rules:** "when-then" formal definitions with rule execution filters
- **Rule execution filters:** Pre-conditions and predicates determining rule execution
- **Condition evaluation:** If "when" conditions are satisfied, "then" actions perform
- **Data bindings:** Map gt-codes to nodes in input or output data sets
- **Terminology:** Define gt-codes as terms for human use
- **Templates:** Optional reporting structures for result generation

### 4.2. Execution Model

The execution model shows the relationship between rule execution filters and rule execution. The flow is:

1. Evaluate guideline-level pre-conditions
2. For each data binding, evaluate predicates
3. For applicable rules, evaluate "when" conditions
4. If conditions satisfied, execute "then" actions
5. Apply template rendering if specified

### 4.3. GDL2 Language Elements

#### 4.3.1. Syntax

GDL2 guidelines are machine serializations of the object model, expressed in openEHR ODIN or JSON format. Expressions appear within Assertion and Assignment statements found in:

- `/pre_conditions`
- `data_bindings[id]/predicates`
- `rules[id]/when` statements
- `rules[id]/then` actions
- Guideline `default_actions`

#### 4.3.2. Pre-conditions

Pre-conditions apply guideline-wide and specify applicability conditions. They determine whether a guideline applies to a given patient/subject. Input datasets not satisfying pre-conditions cause the guideline to be considered non-applicable.

**Example:** "Atrial fibrillation must be present"

```
$gt0121 == 1|local::at0051|Present|
```

**Example in JSON:** "No Coeliac disease diagnosis"

```json
"$gt0015|Coeliac disease diagnosis| == null"
```

#### 4.3.3. Rules

Rules follow the pattern: `when Assertion(s) then Statement(s)`. Multiple assertions in the "when" part use AND logic—all must be true for the rule to fire.

**Example: Reporting rule with template**

```json
"gt0007": {
  "id": "gt0007",
  "priority": 1,
  "when": [
    "$gt0025|Type 1 diabetes| == true ||
     $gt0029|Irritable bowel syndrome| == true"
  ],
  "then": [
    "$gt0009|card.summary| = 'tTG serological testing recommended'",
    "use_template($gt2022)"
  ]
}
```

**Example: Calculation rule**

```json
"gt0012": {
  "id": "gt0012",
  "priority": 1,
  "then": [
    "$gt0003|BMI|.unit = 'kg/m2'",
    "$gt0003|BMI|.magnitude = $gt0007.magnitude/($gt0005.magnitude/100)^2"
  ]
}
```

**Example: Complex calculation**

```json
"gt0025": {
  "id": "gt0025",
  "priority": 2,
  "when": ["$gt0026=='female'"],
  "then": [
    "$gt1000|dage|.precision = 15",
    "$gt1001|age_1|.precision = 15",
    "$gt1000|dage|.magnitude = $gt0022|age|.magnitude / 10.0",
    "$gt0030.magnitude = $gt0030.magnitude + $gt0004.value * 0.211937..."
  ]
}
```

#### 4.3.4. Expression Elements

Expression terminal elements are generated during parsing of expressions and statements. Properties such as constant types and variable types are inferred and generated during parsing rather than stated literally.

#### 4.3.5. Local Variables

Local variables identified by gt-codes are defined in the `terminology` section and used within assertions and assignments. They are tracked in `GUIDELINE_DEFINITION.internal_variables` during guideline materialization.

### 4.4. Reporting

Rule "then" actions perform assignments, setting values in output data locations. Templates define how to represent output structures.

**Example template structure:**

```json
"templates": {
  "gt2022": {
    "id": "gt2022",
    "name": "coeliac-disease-alert",
    "model_id": "generic_model",
    "template_id": "generic_model",
    "object": {
      "cards": [
        {
          "summary": "{$gt0009}",
          "detail": "Found risk factor(s):{$gt0020}",
          "indicator": "warning",
          "source": {
            "label": "NICE. Coeliac disease: recognition...",
            "url": "https://www.nice.org.uk/guidance/ng20"
          }
        }
      ]
    }
  }
}
```

At execution, `{}` mentions are substituted with variable values before template processing.

---

## 5. GDL2 Object Model

### 5.1. Package Structure

The GDL2 object model consists of three packages:

1. **Guideline package:** Guideline definitions, rules, data bindings
2. **Expression package:** Expression elements, operators, functions, constants, variables
3. **Terminology package:** Term definitions and terminology bindings

### 5.2. Guideline Package

#### 5.2.1. Overview

The guideline package contains classes for representing discrete guidelines with archetype bindings, rules, and metadata.

#### 5.2.2. Class Definitions

##### GUIDELINE Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String | Guideline identifier (format: `concept_name.v[N[.M.P]]`) |
| `gdl_version` | String | GDL version (format: `N.M[.P]`) |
| `concept` | String | Normative meaning (gt-code) |
| `definition` | GUIDELINE_DEFINITION | Main definition with bindings and rules |
| `terminology` | TERMINOLOGY | Term definitions and translations |

**Inherits from:** AUTHORED_RESOURCE

---

##### GUIDELINE_DEFINITION Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `data_bindings` | Hash<String, DATA_BINDING> | Archetype/template bindings |
| `pre_conditions` | List<ASSERTION> | Applicability conditions |
| `rules` | Hash<String, RULE> | Logic rules indexed by gt-codes |
| `default_actions` | List<ASSIGNMENT> | Always-executed actions |
| `templates` | Hash<String, OUTPUT_TEMPLATE> | Output reporting structures |
| `internal_variables` | List<VARIABLE> | Internally-used variables |

---

##### RULE Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String | Rule's gt-code |
| `when` | List<ASSERTION> | Conditions (INPUT variables only) |
| `then` | List<ASSIGNMENT> | Actions (OUTPUT variables) |
| `priority` | Integer | Execution order (higher first) |

**Logical form:** `when Assertion(s) then Statement(s)`

---

##### DATA_BINDING Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `model_id` | String | Data model identifier (archetype or other) |
| `template_id` | String | Optional template ID |
| `bindings` | Hash<String, ELEMENT> | Variable bindings by gt-code |
| `predicates` | List<ASSERTION> | Constraints before rule execution |
| `type` | String | "INPUT" or "OUTPUT" marker |

---

##### ELEMENT Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String | Element's gt-code |
| `path` | String | Path within archetype |

---

##### OUTPUT_TEMPLATE Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String | Template's gt-code |
| `name` | String | Template name |
| `model_id` | String | Model identifier |
| `template_id` | String | Optional template identifier |
| `object` | String | Output reporting structure |

---

### 5.3. Expressions Package

#### 5.3.1. Overview

The expression package defines elements for constructing expressions within guidelines, including operators, functions, constants, variables, and statements.

#### 5.3.2. Class Definitions

##### EXPRESSION_ITEM Class (abstract)

**Functions:**

| Function | Return | Description |
|----------|--------|-------------|
| `type()` | String | Type name of item (case-insensitive) |

All valued expression elements inherit from this abstract class.

---

##### OPERATOR Class (abstract)

**Inherits from:** EXPRESSION_ITEM

| Attribute | Type | Description |
|-----------|------|-------------|
| `operator` | OPERATOR_KIND | Operator type |

---

##### UNARY_OPERATOR Class

**Inherits from:** OPERATOR

| Attribute | Type | Description |
|-----------|------|-------------|
| `operand` | EXPRESSION_ITEM | Single operand |

---

##### BINARY_OPERATOR Class

**Inherits from:** OPERATOR

| Attribute | Type | Description |
|-----------|------|-------------|
| `left` | EXPRESSION_ITEM | Left operand |
| `right` | EXPRESSION_ITEM | Right operand |

---

##### OPERATOR_KIND Enumeration

| Operator | Symbol | Description |
|----------|--------|-------------|
| ADDITION | `+` | Addition operation |
| SUBTRACTION | `-` | Subtraction operation |
| MULTIPLICATION | `*` | Multiplication operation |
| DIVISION | `/` | Division operation |
| EXPONENT | `^` | Exponent operation |
| AND | `&&` | Logical AND |
| OR | `\|\|` | Logical OR |
| NOT | `!` | Logical negation |
| EQUALITY | `==` | Relational equality |
| INEQUALITY | `!=` | Relational inequality |
| LESS_THAN | `<` | Less than |
| GREATER_THAN | `>` | Greater than |
| LESS_THAN_OR_EQUAL | `<=` | Less than or equal |
| GREATER_THAN_OR_EQUAL | `>=` | Greater than or equal |
| IS_A | `is_a` | Subsumption operator |
| IS_NOT_A | `!is_a` | Negated subsumption |
| FOR_ALL | `∀` | Universal quantifier |

---

##### FUNCTION_CALL Class

**Inherits from:** EXPRESSION_ITEM

| Attribute | Type | Description |
|-----------|------|-------------|
| `items` | List<EXPRESSION_ITEM> | Function arguments |
| `function` | FUNCTION_KIND | Specific function type |

---

##### FUNCTION_KIND Enumeration

| Function | Description |
|----------|-------------|
| `abs` | Absolute value |
| `ceil` | Ceiling (smallest integer >= argument) |
| `exp` | Euler's number e raised to power |
| `floor` | Floor (largest integer <= argument) |
| `log` | Natural logarithm (base e) |
| `log10` | Base 10 logarithm |
| `log1p` | Natural logarithm of (argument + 1) |
| `round` | Nearest long integer |
| `sqrt` | Positive square root |
| `sin` | Trigonometric sine |
| `cos` | Trigonometric cosine |
| `max` | Maximum of N elements |
| `min` | Minimum of N elements |
| `count` | Count of element instances |
| `sum` | Sum of N element values |

---

##### CONSTANT Class (abstract)

**Inherits from:** EXPRESSION_ITEM

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | String | Symbolic name |
| `value` | Any | Constant value |

---

##### STRING_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | String | String value |

---

##### INTEGER_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | Integer | Integer value |

---

##### BOOLEAN_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | Boolean | Boolean value |

---

##### DATE_TIME_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | ISO8601_DATE_TIME | Date/time value |

---

##### CODE_PHRASE_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | CODE_PHRASE | Code phrase value |

---

##### CODED_TEXT_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | DV_CODED_TEXT | Coded text value |

---

##### ORDINAL_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | DV_ORDINAL | Ordinal value |

---

##### QUANTITY_CONSTANT Class

**Inherits from:** CONSTANT

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | DV_QUANTITY | Quantity value |

---

##### VARIABLE Class

**Inherits from:** EXPRESSION_ITEM

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | String | Variable symbolic name |
| `code` | String | Defining gt-code |

---

##### STATEMENT Class (abstract)

Self-standing procedural element representing statements.

---

##### ASSIGNMENT Class

**Inherits from:** STATEMENT

| Attribute | Type | Description |
|-----------|------|-------------|
| `variable` | VARIABLE | Assignment target |
| `expression` | EXPRESSION_ITEM | Assignment source |

---

##### ASSERTION Class

**Inherits from:** STATEMENT

| Attribute | Type | Description |
|-----------|------|-------------|
| `expression` | EXPRESSION_ITEM | Boolean expression |

**Invariant:** `expression.type()` must be "Boolean"

---

### 5.4. Terminology Package

#### 5.4.1. Overview

The terminology package defines semantics for terminology in guidelines, simplified from openEHR AOM2 ARCHETYPE_TERMINOLOGY and ARCHETYPE_TERM classes.

#### 5.4.2. Class Definitions

##### TERMINOLOGY Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `is_differential` | Boolean | Differential or complete w.r.t. parent |
| `original_language` | String | Original language (ISO 639-1 code) |
| `concept_code` | String | Guideline concept gt-code |
| `term_definitions` | Hash<String, Hash<String, TERM>> | Terms by language and code |
| `term_bindings` | Hash<String, TERM_BINDING> | External terminology bindings |

**Functions:**

| Function | Return | Description |
|----------|--------|-------------|
| `specialisation_depth()` | Integer | Specialization depth (0 for unspecialized) |
| `has_language(a_lang)` | Boolean | Language present in terminology |
| `has_terminology(a_terminology_id)` | Boolean | Terminology bindings present |
| `has_term_code(a_code)` | Boolean | Term code defined |
| `term_definition(a_lang, a_code)` | TERM | Term definition for code in language |
| `term_binding(a_terminology, a_code)` | Uri | External binding for code |
| `terminologies_available()` | List<String> | Available terminologies |
| `languages_available()` | List<String> | Available languages |

**Invariants:**

- `original_language` validity
- `concept_code` validity
- `term_bindings` validity
- `parent_archetype` validity

---

##### TERM Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `code` | String | Term code |
| `text` | String | Short display text |
| `description` | String | Full description text |
| `other_items` | Hash<String, String> | Additional items (provenance, etc.) |

---

##### TERM_BINDING Class

| Attribute | Type | Description |
|-----------|------|-------------|
| `bindings` | List<TERM> | External codes (URI or namespace format) |
| `code` | String | Local gt-code |

---

## 6. Syntax Specification

### 6.1. Syntax Details

The GDL syntax is based entirely on openEHR ODIN syntax with JSON equivalents, driven by the guideline object model. Expressions in Assertion and Assignment statements follow a grammar implemented using javaCC specifications. The full Java GDL parser source code is available in the GitHub repository.

**Supported syntax formats:**

- **ODIN:** openEHR Object Data Instance Notation
- **JSON:** JavaScript Object Notation

**Expression syntax supports:**

- Arithmetic operators: `+`, `-`, `*`, `/`, `^`
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `&&`, `||`, `!`
- Special operators: `is_a`, `!is_a`
- Mathematical functions: `abs()`, `sqrt()`, `log()`, `sin()`, `cos()`, etc.
- Aggregate functions: `sum()`, `count()`, `min()`, `max()`

---

## 7. Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| CDS Release 2.0.1 | Current stable release | - | - |
| **CDS Release 2.0.0** | - | - | - |
| 2.0.0 | SPECCDS-2: Add GDL and GDL2 specs to CDS release | SEC | 20 May 2019 |
| - | Initial Writing | R Chen, T Beale | 12 Apr 2019 |

**Last updated:** 2024-07-31 09:56:12 UTC

---

## Copyright and License

© 2018 - 2024 The openEHR Foundation

The openEHR Foundation is an independent, non-profit organization facilitating health record sharing through open specifications, clinical models, and platform implementations.

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/
