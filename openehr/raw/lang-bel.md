# Basic Expression Language (BEL) Specification

**Document Title:** Basic Expression Language (BEL)

**Issuer:** openEHR Specification Program

**Release:** LANG latest

**Status:** STABLE

**Revision:** [latest_issue]

**Date:** [latest_issue_date]

**Keywords:** openehr, expressions, rules

**Copyright:** © 2016 - 2022 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
(https://creativecommons.org/licenses/by-nd/3.0/)

---

## Table of Contents

- [Amendment Record](#amendment-record)
- [Acknowledgements](#acknowledgements)
- [1. Preface](#1-preface)
- [2. Overview](#2-overview)
- [3. The Basic Expression Language](#3-the-basic-expression-language)
- [4. The Basic Expression Object Model](#4-the-basic-expression-object-model)
- [Appendix A: Syntax Specification](#appendix-a-syntax-specification)
- [References](#references)

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| 1.2.0 | Import old Expression Language as 'Basic Expression Language'; Add `OPERATOR_KIND` enumeration. | SEC | 14 May 2022 |
| 1.1.5 | Retrospectively release interim form of Expression Language. | T Beale, P Bos, D Bosca | 05 Apr 2022 |
| 1.1.0 | Correct UML package nesting and paths; insert `base` parent package; rename `expressions` package to `expression`. | T Beale | 27 Nov 2017 |
| 1.0.1 | Correct type of `OP_DEF_EXISTS._evaluation_agent_` to `FUNCTION<<Any>, Boolean>`. | C Nanjo | 31 May 2016 |
| 1.0.0 | Initial writing. Taken from AOM2 2.0.6. | T Beale, openEHR SEC | 15 Feb 2016 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica; openEHR Foundation Management Board

### Contributors

- Pieter Bos, Senior Engineer, Nedap, Netherlands

---

## 1. Preface

### 1.1. Purpose

This specification defines the openEHR Basic Expression Model and an abstract syntax for the openEHR Basic Expression Language (BEL). The model encodes the semantics of a restricted first-order predicate logic subset suitable for expressing rules, particularly within archetypes.

**Intended Audience:**

- Standards bodies producing health informatics standards
- Academic groups using openEHR
- Solution vendors
- Medical informaticians and clinicians interested in health information

### 1.2. Related Documents

**Prerequisite Documents:**

- The openEHR Architecture Overview

**Related Documents:**

- The Archetype Object Model 2 (AOM2)

### 1.3. Status

This specification was extracted from the AOM2 specification to provide a unified expression and rules model for AOM, GDL, and other specifications. The document is in **STABLE** state.

**Development Note:** The BEL and BEOM have been superseded by the openEHR BMM expression model and a more capable Expression Language (EL). However, BEL remains implemented in the open source Archie project and is used in production systems.

### 1.4. Feedback

- **Forum:** openEHR languages specifications forum
- **Issues:** specifications Problem Report tracker
- **Changes:** LANG component Change Request tracker

### 1.5. Conformance

Conformance to openEHR specifications is determined by formal testing against openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

---

## 2. Overview

### 2.1. Design Background

The openEHR Basic Expression Language derives from restricted first-order predicate logic with added features supporting basic statement types. The design resembles OCL (Object Constraint Language) and Object-Z, but with distinct characteristics:

- Different meta-model foundation
- Syntax designed for developers familiar with mainstream object-oriented and functional languages (Java, C#, Python, TypeScript)

**Semantic Requirements:**

- Arithmetic, boolean, and relational operators
- Functions and quantifier operators
- Operator precedence and parentheses support
- Constants and variable types
- No procedural semantics or full programming language features

### 2.2. Execution Model

BEL text is executed by an _execution engine_. An _evaluator_ processes expressions against a _data context_, which determines truth values. Initially, the data context is assumed to be openEHR templated archetypes within a typical archetype-using component.

### 2.3. General Structure

BEL programs contain _statements_ with typed expressions. Statements may be declarations, assignments, or assertions. Variables employ `$` prefixes (e.g., `$heart_rate`), following shell script convention.

**Variable Types:**

- **Bound variables:** mapped to data context fields
- **Local variables:** declared within the program

Assignment statements associate data context paths with symbolic variables (reading) or reverse the process (writing).

---

## 3. The Basic Expression Language

### 3.1. Overview

This section details the openEHR Basic Expression Language. In various contexts, the syntax provides a foundation for concrete syntaxes supporting specific value-referencing mechanisms and rule types. Key features include variable declarations, assignments, and expressions grounded in first-order predicate logic with arithmetic and relational operators for numeric handling.

**Expression Components:**

- Constants
- Variable references
- Value references
- Functions

### 3.2. Syntax Style

The specification uses 'snake_case' rather than 'CamelCase', consistent with other openEHR specifications, though either convention may be used in applications.

### 3.3. Typing

BEL is fully typed, using the same type system as other openEHR components and the openEHR Foundation Types Specification.

**Type Categories:**

- Primitive types
- Container types: `List<T>`, `Set<T>`, `Hash<K:Ordered,V>`
- Interval type: `Interval<T: Ordered>`

### 3.4. Literals

#### 3.4.1. Primitive Types

| Name | Literal Value | Description |
|------|---------------|-------------|
| `Boolean` | `True`, `False` | Boolean value |
| `Integer` | `10`, `-4`, `1024` | Integer value |
| `Real` | `10.0`, `0.345` | Real value |
| `Date` | `2004-08-12` | ISO8601-format date |
| `Date_time` | `2004-08-12T12:00:59+0100` | ISO8601-format date/time |
| `Time` | `12:00:59` | ISO8601-format time |
| `Duration` | `P39W` | ISO8601-format duration |
| `String` | `"this is a string"` | String |
| `Uri` | `[https://en.wikipedia.org/wiki/Everest]` | URI in RFC3986 format |
| `Terminology_code` | `[snomed_ct::389086002]` or `[snomed_ct::389086002\|Hypoxia\|]` | Terminology code reference |

**Type Promotion:** Automatic promotion from `Integer` to `Real` applies to all integer and real values and expressions.

#### 3.4.2. Container Types

| Name | Literal Value | Description |
|------|---------------|-------------|
| `List<T>` | `[val, val, ...]` | Ordered list; allows repetition |
| `Set<T>` | `{val, val, ...}` | Unordered set; unique membership |
| `Hash<K:Ordered, V>` | `< ["key1"] = <val1> ["key2"] = <val2> ... >` | Keyed indexed container |

**Container Methods:**

```
for_all (test(v: T): Boolean): Boolean
    -- True if test(v) is True for every v

there_exists (test(v: T): Boolean): Boolean
    -- True if test(v) is True for any v
```

#### 3.4.3. Interval Type

| Name | Literal Value | Description |
|------|---------------|-------------|
| `Interval<T>` | Various forms | Interval of ordered primitive |
| Two-sided | `\|N..M\|` | N >= x <= M |
| Two-sided (open left) | `\|>N..M\|` | N > x <= M |
| Two-sided (open right) | `\|N..<M\|` | N >= x < M |
| One-sided (less than) | `\|<N\|` | x < N |
| One-sided (greater than) | `\|>N\|` | x > N |
| One-sided (less-equal) | `\|<=N\|` | x <= N |
| One-sided (greater-equal) | `\|>=N\|` | x >= N |
| Symmetric interval | `\|N +/-M\|` or `\|N+/-M\|` | N +/-M |

### 3.5. Statements

BEL texts consist of declarations, assignments, or assertions.

#### 3.5.1. Declarations

Variables are declared with formal types. Bound variables include data context path assignments. Local variables may include expression-based assignments.

**Examples:**

```
-- local variable, primitive type
$date_of_birth: Date

-- local variable, container type
$heart_rate_history: List<Real>

-- local variable with assignment
$age_in_years: Integer := current_date() - $date_of_birth

-- bound variable
$weight: Quantity := /data[id3]/events[id4]/data[id2]/items[id5]/value
```

#### 3.5.2. Constants

Constants use equality (`=`) operators in declarations with literal values.

**Examples:**

```
Mph_to_kmh_factor: Real = 1.6
Pounds_to_kg: Real = 0.4536
Systolic_normal_range: Interval<Integer> = |105..135|
```

#### 3.5.3. Assignment

Assignment to writable variables uses the `:=` operator. Right-hand sides are value-returning expressions.

**Examples:**

```
$speed_kmh: Real                             -- declaration
$speed_mph: Real := 35.0                     -- assignment in declaration

$speed_kmh := $speed_mph * Mph_to_kmh_factor  -- assignment
```

### 3.6. Bound Variables, Evaluation and Validity

Bound variables differ from local variables in that their availability depends on external entity existence. Unlike local variables (which have default type values), undefined bound variables should generate an 'undefined value' exception.

**Control Strategy:** Use the `exists()` predicate to verify variable availability before dependent logic.

**Examples:**

```
Check_vs_vars: exists $heart_rate and exists $blood_pressure

Smoker_details_recorded: $is_smoker implies exists $smoking_details
```

### 3.7. Expressions

Expressions constitute the language's core, featuring typed operator-based syntax common to programming languages and logics.

**Expression Types:**

- Terminal entities
- Non-terminal entities (operators and functions)

#### 3.7.1. Terminal Entities

Terminal entities include:

- Literals
- Variables
- Variables with sub-paths
- Constants
- Function calls
- Raw paths

**Examples:**

```
-- expression with variable and function call
current_date() - $date_of_birth

-- expression with variable and constant
$speed_mph * Mph_to_kmh_factor
```

**Sub-path Variables:**

Variables bound to paths may reference sub-elements using XPath-like syntax.

**Example:**

```
$event: List<Event> := /data[id2]/events[id3]

Check_field_vals: $event/data[id4]/items[id7]/value/magnitude =
    $event/data[id4]/items[id5]/value/magnitude -
    $event/data[id4]/items[id6]/value/magnitude
```

The construction `$event/data[id4]/items[id7]/value/magnitude` references a data context element whose location combines the path to which `$event` is bound with the subordinate path.

#### 3.7.1.1. Functions

Functions are leaf entities--either built-in or external (user-defined).

**Example:**

```
$date_of_birth: Date
$age: Duration

$age := current_date() - $date_of_birth
```

**Built-in Functions:**

| Name | Textual Rendering | Signature | Meaning |
|------|-------------------|-----------|---------|
| current_date | `current_date()` | :Date | Current date |
| current_time | `current_time()` | :Time | Current time |
| current_date_time | `current_date_time()` | :Date_time | Current date/time |
| current_time_zone | `current_time_zone()` | :Time_zone | Current time zone |
| sum | `sum(x, y, ...)` | <Real, ...>: Real | x + y + ... |
| mean | `mean(x, y, ...)` | <Real, ...>: Real | Average value |
| max | `max(x, y, ...)` | <Real, ...>: Real | Maximum value |
| min | `min(x, y, ...)` | <Real, ...>: Real | Minimum value |

#### 3.7.2. Operators

Expressions include arithmetic, relational, boolean operators, and existential/universal quantifiers.

**Arithmetic Operators (descending precedence):**

| Identifier | Textual | Symbolic | Meaning |
|-----------|---------|----------|---------|
| exp | `^` | `^` | Exponentiation |
| times | `*` | `*` | Multiplication |
| divide | `/` | `/` | Division |
| mod | `%` | `%` | Modulo division |
| plus | `+` | `+` | Addition |
| minus | `-` | `-` | Subtraction |

**Relational Operators (equal precedence):**

| Identifier | Textual | Symbolic | Meaning |
|-----------|---------|----------|---------|
| eq | `=` | `=` | Equality |
| ne | `!=` | | Inequality |
| lt | `<` | `<` | Less than |
| le | `<=` | | Less than or equal |
| gt | `>` | `>` | Greater than |
| ge | `>=` | | Greater than or equal |

**Logical Operators (descending precedence):**

| Identifier | Textual | Symbolic | Meaning |
|-----------|---------|----------|---------|
| not | `not`, `~` | | Negation |
| and | `and` | | Conjunction |
| or | `or` | | Disjunction |
| xor | `xor` | | Exclusive or |
| implies | `implies` | | Material implication |

##### 3.7.2.1. Logical Negation

All Boolean operators take Boolean operands and produce Boolean results. The `not` operator applies as a prefix to all Boolean-returning operators and parenthesized expressions.

##### 3.7.2.2. Precedence and Parentheses

Operator precedence follows the order shown in operator tables. Parentheses override precedence as in standard programming languages.

**Example:**

```
$at_risk := $weight > 120 and ($is_smoker or $is_hypertensive)
```

##### 3.7.2.3. Container Operators

Standard predicate logic quantifiers--`there_exists` and `for_all`--apply to container types.

**`there_exists` Syntax:**

```
there_exists v : container_var | <Boolean expression mentioning v>
```

The `|` symbol reads as "such that."

**`for_all` Syntax:**

```
for_all v : container_var | <Boolean expression mentioning v>
```

The `|` symbol reads as "it holds that."

**Colon Alternative:** The `:` symbol may be replaced with `in`.

---

## 4. The Basic Expression Object Model

### 4.1. Overview

The `beom` package defines the Basic Expression Object Model (BEOM)--a model for 'statements' and 'expressions' usable in various openEHR contexts, including archetypes and GDL guidelines. Parser output takes the form of an expression tree. Other openEHR models may specialize BEOM types for specific purposes.

### 4.2. Core Package

The main `beom.core` package organizes statements into three types:

- `ASSERTION`: Boolean-evaluating expressions
- `VARIABLE_DECLARATION`: Named, typed variables
- `ASSIGNMENT`: Value assignment to variables

A group of statements forms a `STATEMENT_SET`.

#### 4.2.1. Expressions

Expressions are fully evaluable statement values defined by `EXPR_XXX` classes. The Expression meta-model represents evaluation trees where nodes are leaf or operator nodes. Function calls are leaf nodes (black boxes requiring evaluation methods), allowing standard operator semantics to build safely into the main tree.

#### 4.2.2. Other Statement Elements

##### 4.2.2.1. External Query

An `EXTERNAL_QUERY` represents a call to an external service obtaining a value. This treats information items from the computational environment as abstract typed values within expressions.

#### 4.2.3. Class Descriptions

##### 4.2.3.1. STATEMENT_SET Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| statement | List<STATEMENT> | Member statements |
| name | String | Optional rule set name |

| Function | Return | Meaning |
|----------|--------|---------|
| execution_result() | Boolean | AND of all assertion results |

##### 4.2.3.2. STATEMENT Class

**Abstract meta-type** for non-value-returning entities.

##### 4.2.3.3. ASSERTION Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| tag | String | Expression differentiator |
| string_expression | String | String expression form |
| expression | EXPRESSION | Expression tree root |

**Inherits:** STATEMENT

##### 4.2.3.4. VARIABLE_DECLARATION Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| name | String | Variable name |
| type | EXPR_TYPE_DEF | Variable type |

**Inherits:** STATEMENT

##### 4.2.3.5. ASSIGNMENT Class

| Attribute | Type | Meaning |
|-----------|------|---------|
| target | VARIABLE_DECLARATION | Left-hand side variable |
| source | EXPR_VALUE | Right-hand side value |

**Inherits:** STATEMENT

##### 4.2.3.6. EXPR_VALUE Class

**Abstract meta-type** for evaluable statement elements. Type is supplied in descendants or inferred by assignment to typed variables.

| Function | Return | Meaning |
|----------|--------|---------|
| value() | Any | Computed result value |

##### 4.2.3.7. EXTERNAL_QUERY Class

**Inherits:** EXPR_VALUE

| Attribute | Type | Meaning |
|-----------|------|---------|
| context | String | Optional context name (e.g., "patient") |
| query_id | String | External context query identifier |
| query_args | List<String> | Optional query arguments |

##### 4.2.3.8. EXPRESSION Class

**Abstract parent** of all expression meta-types.

**Inherits:** EXPR_VALUE

| Function | Return | Meaning |
|----------|--------|---------|
| type() | EXPR_TYPE_DEF | Primitive node type |

##### 4.2.3.9. EXPR_OPERATOR Class

**Abstract parent** of operator types.

**Inherits:** EXPRESSION

| Attribute | Type | Meaning |
|-----------|------|---------|
| precedence_overridden | Boolean | True if precedence overridden |
| operator | OPERATOR_KIND | Operator definition |
| symbol | String | Actual symbol used |

##### 4.2.3.10. EXPR_UNARY_OPERATOR Class

**Inherits:** EXPR_OPERATOR

| Attribute | Type | Meaning |
|-----------|------|---------|
| operand | EXPRESSION | Operand node |

##### 4.2.3.11. EXPR_BINARY_OPERATOR Class

**Inherits:** EXPR_OPERATOR

| Attribute | Type | Meaning |
|-----------|------|---------|
| left_operand | EXPRESSION | Left operand |
| right_operand | EXPRESSION | Right operand |

##### 4.2.3.12. EXPR_FOR_ALL Class

**Inherits:** EXPR_OPERATOR

| Attribute | Type | Meaning |
|-----------|------|---------|
| condition | ASSERTION | Applied condition |
| operand | EXPR_VALUE_REF | Container reference |

##### 4.2.3.13. EXPR_LEAF Class

**Abstract meta-type** representing manifest constants, path references, constraints, or variable references.

**Inherits:** EXPRESSION

| Attribute | Type | Meaning |
|-----------|------|---------|
| item | Any | Reference item for value computation |

##### 4.2.3.14. EXPR_LITERAL Class

Literal value expression tree leaf item.

**Inherits:** EXPR_LEAF

| Attribute | Type | Meaning |
|-----------|------|---------|
| item | Any | Static constant value |

##### 4.2.3.15. EXPR_VARIABLE_REF Class

Expression tree leaf representing declared variable reference.

**Inherits:** EXPR_LEAF

| Attribute | Type | Meaning |
|-----------|------|---------|
| item | VARIABLE_DECLARATION | Referenced variable |

##### 4.2.3.16. EXPR_FUNCTION_CALL Class

Node representing function calls with zero or more arguments.

**Inherits:** EXPR_LEAF

| Attribute | Type | Meaning |
|-----------|------|---------|
| arguments | List<EXPRESSION> | Function arguments |

### 4.3. Operators

Operators in BEL are represented in the `OPERATOR_KIND` enumeration.

#### 4.3.1. Class Descriptions

##### 4.3.1.1. OPERATOR_KIND Enumeration

| Attribute | Meaning |
|-----------|---------|
| eq | Equality (equals) |
| ne | Inequality (not-equals) |
| lt | Less than |
| le | Less than or equals |
| gt | Greater than |
| ge | Greater than or equals |
| matches | Matches |
| not | Logical negation (not) |
| and | Logical conjunction (and) |
| or | Logical inclusive disjunction (or) |
| xor | Logical exclusive disjunction |
| implies | Logical implication |
| for_all | Universal quantification |
| exists | Existential quantification |
| plus | Arithmetic addition (plus) |
| minus | Arithmetic subtraction (minus) |
| multiply | Arithmetic multiplication (times) |
| divide | Arithmetic division |
| modulo | Arithmetic modulo |
| exponent | Arithmetic exponent (power) |

### 4.4. Typing

The `beom.types` package defines typing via the `EXPR_TYPE_DEF` class and descendants. All types feature `_type_name_` and `_type_anchor_` attributes. The anchor is a variable of the corresponding primitive type from openEHR `base_types` packages (Integer, Real, String, etc.), enabling assignment testing within implementations. A special `TYPE_DEF_OBJECT` enables value references to complex objects.

#### 4.4.1. Class Descriptions

##### 4.4.1.1. EXPR_TYPE_DEF Class

**Abstract ancestor** for types known in the Expression formalism.

| Attribute | Type | Meaning |
|-----------|------|---------|
| type_name | String | Type name in abstract syntax |
| type_anchor | Any | Corresponding openEHR primitive type attribute |

##### 4.4.1.2. TYPE_DEF_BOOLEAN Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Boolean`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Boolean" | String |
| type_anchor | -- | Boolean |

##### 4.4.1.3. TYPE_DEF_INTEGER Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Integer`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Integer" | String |
| type_anchor | -- | Integer |

##### 4.4.1.4. TYPE_DEF_REAL Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Real`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Real" | String |
| type_anchor | -- | Real |

##### 4.4.1.5. TYPE_DEF_DATE Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Date`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Date" | String |
| type_anchor | -- | Iso8601_date |

##### 4.4.1.6. TYPE_DEF_DATE_TIME Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Date_time`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Date_time" | String |
| type_anchor | -- | Iso8601_date_time |

##### 4.4.1.7. TYPE_DEF_TIME Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Time`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Time" | String |
| type_anchor | -- | Iso8601_time |

##### 4.4.1.8. TYPE_DEF_DURATION Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Duration`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Duration" | String |
| type_anchor | -- | Iso8601_duration |

##### 4.4.1.9. TYPE_DEF_STRING Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `String`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "String" | String |
| type_anchor | -- | String |

##### 4.4.1.10. TYPE_DEF_URI Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Uri`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Uri" | String |
| type_anchor | -- | Uri |

##### 4.4.1.11. TYPE_DEF_TERMINOLOGY_CODE Class

**Inherits:** EXPR_TYPE_DEF

Represents the primitive type `Terminology_code`.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Terminology_code" | String |
| type_anchor | -- | Terminology_code |

##### 4.4.1.12. TYPE_DEF_OBJECT_REF Class

**Inherits:** EXPR_TYPE_DEF

Represents the type `Object_ref`, for non-primitive reference targets.

| Attribute | Default | Type |
|-----------|---------|------|
| type_name | "Object_ref" | String |

---

## Appendix A: Syntax Specification

The grammar and lexical specification for standard Expression syntax appears below in ANTLR4 form.

```antlr
//
//  description: Antlr4 grammar for openEHR Rules core syntax.
//  author:      Thomas Beale <thomas.beale@openehr.org>
//  contributors:Pieter Bos <pieter.bos@nedap.com>
//  support:     openEHR Specifications PR tracker
//  copyright:   Copyright (c) 2016- openEHR Foundation
//  license:     Apache 2.0 License

grammar base_expressions;
import cadl2_primitives, odin_values;

//
//  ======================= Top-level _objects ========================
//

statement_block: statement+ ;

// ------------------------- statements ---------------------------
statement: declaration | assignment | assertion;

declaration:
      variable_declaration
    | constant_declaration
    ;

variable_declaration: local_variable ':' type_id ( SYM_ASSIGNMENT expression )? ;

constant_declaration: constant_name ':' type_id  ( SYM_EQ primitive_object )? ;

assignment:
      binding
    | local_assignment
    ;

binding: local_variable SYM_ASSIGNMENT bound_path ;

local_assignment: local_variable SYM_ASSIGNMENT expression ;

assertion: ( ( ALPHA_LC_ID | ALPHA_UC_ID ) ':' )? boolean_expr ;

//
// -------------------------- _expressions --------------------------
//
expression:
      boolean_expr
    | arithmetic_expr
    ;

boolean_expr:
      SYM_NOT boolean_expr
    | boolean_expr SYM_AND boolean_expr
    | boolean_expr SYM_XOR boolean_expr
    | boolean_expr SYM_OR boolean_expr
    | boolean_expr SYM_IMPLIES boolean_expr
    | boolean_leaf equality_binop boolean_leaf
    | boolean_leaf
    ;

boolean_leaf:
      boolean_literal
    | for_all_expr
    | there_exists_expr
    | SYM_EXISTS ( bound_path | sub_path_local_variable )
    | '(' boolean_expr ')'
    | relational_expr
    | equality_expr
    | constraint_expr
    | value_ref
    ;

boolean_literal:
      SYM_TRUE
    | SYM_FALSE
    ;

for_all_expr: SYM_FOR_ALL VARIABLE_ID ( ':' | 'in' ) value_ref '|'? boolean_expr ;

there_exists_expr: SYM_THERE_EXISTS VARIABLE_ID ( ':' | 'in' ) value_ref '|'? boolean_expr ;

constraint_expr: ( arithmetic_expr | value_ref ) SYM_MATCHES  ( '{' c_inline_primitive_object '}' | CONTAINED_REGEXP );

arithmetic_expr:
      <assoc=right> arithmetic_expr '^' arithmetic_expr
    | arithmetic_expr ( '/' | '*' | '%' ) arithmetic_expr
    | arithmetic_expr ( '+' | '-' ) arithmetic_expr
    | arithmetic_leaf
    ;

arithmetic_leaf:
      integer_value
    | real_value
    | date_value
    | date_time_value
    | time_value
    | duration_value
    | value_ref
    | '(' arithmetic_expr ')'
    ;

equality_expr: arithmetic_expr equality_binop arithmetic_expr ;

equality_binop:
      SYM_EQ
    | SYM_NE
    ;

relational_expr: arithmetic_expr relational_binop arithmetic_expr ;

relational_binop:
      SYM_GT
    | SYM_LT
    | SYM_LE
    | SYM_GE
    ;

value_ref:
      function_call
    | bound_path
    | sub_path_local_variable
    | local_variable
    | constant_name
    ;

local_variable: VARIABLE_ID ;

sub_path_local_variable: VARIABLE_WITH_PATH;

bound_path: ADL_PATH ;

constant_name: ALPHA_UC_ID ;

function_call: ALPHA_LC_ID '(' function_args? ')' ;

function_args: expression ( ',' expression )* ;

type_id: ALPHA_UC_ID ( '<' type_id ( ',' type_id )* '>' )? ;
```

---

## References

Hein, J. L. (2002). *Discrete Structures, Logic and Computability* (Second ed.). Jones and Bartlett.

Kilov, H., & Ross, J. (1994). *Information Modelling: an object-oriented approach*. Prentice Hall.

Smith, G. (2000). *The Object Z Specification Language*. Kluwer Academic Publishers.

Sowa, J. F. (2000). *Knowledge Representation: Logical, philosophical and Computational Foundations*. California: Brooks/Cole.

---

**Last Updated:** 2022-12-18 23:43:58 UTC