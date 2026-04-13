# Expression Language (EL) Specification

**Issuer:** openEHR Specification Program
**Release:** LANG latest
**Status:** DEVELOPMENT
**Date:** 2022-05-10
**Keywords:** openehr, expressions, rules

---

## Table of Contents

1. [Expression Language (EL)](#expression-language-el)
2. [Amendment Record](#amendment-record)
3. [Acknowledgements](#acknowledgements)
4. [Preface](#preface)
5. [Overview](#overview)
6. [EL Basics](#el-basics)
7. [Terminal Entities](#terminal-entities)
8. [Complex Expressions](#complex-expressions)
9. [Syntax Specification](#syntax-specification)
10. [References](#references)

---

## Expression Language (EL)

**Copyright:** © 2020 - 2022 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/

**Support:**
- Issues: [Problem Reports](https://specifications.openehr.org/components/LANG/open_issues)
- Web: [specifications.openEHR.org](https://specifications.openehr.org)

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| **LANG Release 1.0.0** | | | |
| 2.0.0 | Add Expression Language specification | T Beale | 10 May 2020 |
| | Add Container selectors | T Beale | 10 May 2020 |
| | Update based on BMM expression package | T Beale | 03 Mar 2020 |
| | Initial writing; added external model use; added `defined()` and `check()` predicates | T Beale | 19 Sep 2018 |

---

## Acknowledgements

### Primary Author

- Thomas Beale, Ars Semantica; openEHR Foundation Management Board

### Contributors

- Pieter Bos, Senior Engineer, Nedap, Netherlands
- Borut Fabjan, Program Manager, Better, Slovenia
- Matija Kejzar, Senior Engineer, Better, Slovenia
- Bostjan Lah, Architect, Better, Slovenia

### Supporters

- openEHR Foundation Industry and Organisation Partners
- Ars Semantica, UK
- Better, Slovenia (formerly Marand)

---

## Preface

### 1.1. Purpose

This specification defines an abstract openEHR Expression Language (EL) that provides syntax representation for expressions whose meta-model is defined in the `expression` package of the openEHR Basic Meta-Model (BMM). The language may be used within BMM models, archetype rules, Task Planning expressions, newer GDL versions, and decision language expressions.

**Intended audience includes:**
- Standards bodies producing health informatics standards
- Academic groups using openEHR
- Solution vendors

### 1.2. Related Documents

**Prerequisite documents:**
- The openEHR Architecture Overview
- The openEHR Basic Meta-Model (BMM)

**Related documents:**
- Archetype Object Model 2 (AOM2), Assertions section
- Task Planning specification
- Guideline Definition Language (GDL)

### 1.3. Status

This specification is in DEVELOPMENT state. The expression language described here represents a more powerful evolution of the original Basic Expression Language (BEL), based on the openEHR BMM expression model rather than the BEL meta-model.

Known omissions are marked with "TBD" (To Be Determined) paragraphs throughout the document.

### 1.4. Feedback

Feedback may be provided on the [openEHR languages specifications forum](https://discourse.openehr.org/c/specifications/bmm-el).

Issues may be raised on the [specifications Problem Report tracker](https://specifications.openehr.org/components/LANG/open_issues).

### 1.5. Conformance

Conformance is determined by formal testing against relevant openEHR Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. ITS conformance indicates model conformance.

---

## Overview

### 2.1. Requirements

The language supports standard arithmetic, boolean, and relational operators, functions, logical quantifiers, operator precedence, constant values, and variables. Multi-lingual translations for symbolic variables are supported similarly to the openEHR Archetype Definition Language (ADL2).

### 2.2. Design Background

EL combines first-order predicate logic, object-oriented structural concepts, and functional computing. It has similarities with OMG's OCL (Object Constraint Language) and draws on semantics from the Eiffel Language (ECMA-367).

**Key distinctions:**
- Different meta-model based on BMM `expression`
- Syntax designed for developers familiar with modern languages (Java, C#, Python, TypeScript)

**Key features:**
- Strong typing and void-safety
- Standard operators including logical, arithmetic, and relational operators
- Object-oriented qualification using dot notation
- Decision structures (binary choice, condition chains, case tables)
- Functions and agents (lambdas)

### 2.3. Execution Model

Expressions are evaluated by an _evaluator_ against a _data context_, which determines truth values. The data context provides variables that may be read from and written to.

**Two specification modes:**

1. **Implicit context:** Variables are inferred from data binding
2. **Explicit context:** EL expressions appear within a BMM model or context explicitly importing a BMM model

In both cases, parsed expressions result in instances of BMM EL meta-types.

---

## EL Basics

### 3.1. Syntax Style

EL syntax is inspired by TypeScript, Kotlin, and Java, adapted for readability by both IT and non-IT professionals.

**Lexical conventions use snake_case:**
- _Class names_: `Iso8601_date_time`, `Arrayed_list<T>`
- _Properties and variables_: `employee_group`, `average_pressure()`
- _Constants and class functions_: `Maximum_speed`

Upper and lower case distinctions are stylistic only.

**TBD:** Equivalence specification between snake_case and CamelCase, or tool-level switch.

### 3.2. Commenting

Two comment styles are supported:

- **End-of-line comments:** Leader pattern `--`
- **Line comments:** Bar character `|`

Visual dividing lines use multiple hyphens (`--------`) or equals signs (`========`).

**Example:**
```
|
| patient fit to undertake regime
|
patient_fit:
    Result := not
        (platelets.in_range ([very_low]) or  -- platelets can't be too low
         neutrophils.in_range ([very_low]))
```

### 3.3. Typing

EL is fully typed. "All operators are assumed to be implemented by and to map to functions defined on types" (BMM specification). For example, the `+` operator maps to the `add()` function on `Integer`.

Operators map to operator-aliased functions defined in the BMM as `BMM_ROUTINE` descendants. Implementations may optimize by using built-in native types for primitive operations rather than always dispatching via BMM.

### 3.4. EL Foundation Types

#### 3.4.1. Primitive Types

| Name | Description |
|------|-------------|
| `Boolean` | Boolean value |
| `Integer` | Integer value |
| `Integer64` | Large integer value |
| `Real` | Real value |
| `Double` | Large real value |
| `Date` | ISO 8601-format date |
| `Date_time` | ISO 8601-format date/time |
| `Time` | ISO 8601-format time |
| `Duration` | ISO 8601-format duration |
| `String` | String |
| `Uri` | Uri in IETF RFC 3986 format |
| `Terminology_code` | Terminology code reference |

Automatic type promotion from `Integer` to `Real` applies to mixed integer/real expressions.

#### 3.4.2. Container Types

| Name | Description |
|------|-------------|
| `Container<T>` | Abstract parent of List, Set, and Map types |
| `List<T>` | Linear list allowing order and repeated membership |
| `Set<T>` | Set with no order and unique membership |
| `Map<K:Ordered, V>` | Indexed linear container |

#### 3.4.3. Interval Type

| Name | Description |
|------|-------------|
| `Interval<T:Ordered>` | Interval of any ordered type |
| `Point_interval<T:Ordered>` | Closed intervals with identical boundaries |
| `Proper_interval<T:Ordered>` | Intervals with different boundaries |

Automatic type promotion from `Interval<Integer>` to `Interval<Real>` is supported.

#### 3.4.4. Complex Types

Complex types are imported from formal model definitions expressed in openEHR BMM format or formal equivalents. These become available within EL just as foundation types do.

---

## Terminal Entities

Terminal entities correspond to the `EL_TERMINAL` meta-type and descendants. Three categories exist:

- _Instance references_: Direct references to literals, constants, variables, or function calls
- _Predicates_: Logical conditions on instance references
- _Agents_: Delayed routine call objects

### 4.1. Literals

Literal values correspond to openEHR Foundation and Based types, expressed in openEHR ODIN syntax (except for List, Set, and Map types distinguished by specific bracket types).

| Type | Literal Values | Description |
|------|----------------|-------------|
| `Boolean` | `True`, `False` | |
| `Integer` | `10`, `-4`, `5e09` | Signed integers from -2^31 to 2^31-1, E-notation supported |
| `Real` | `10.0`, `0.345`, `22.5%`, `6.023e23` | Signed reals, percentages, and E-notation supported |
| `Double` | `10.0`, `0.345`, `22.5%`, `6.023e23` | Double precision reals |
| `Date` | `2004-08-12` | ISO 8601 format |
| `Date_time` | `2004-08-12T12:00:59+0100` | ISO 8601 format |
| `Time` | `12:00:59` | ISO 8601 format |
| `Duration` | `P2Y8M` | ISO 8601 format |
| `String` | `"this is a string"` | |
| `Uri` | `<https://en.wikipedia.org>` | IETF RFC 3986 format |
| `Terminology_code` | `#identifier` or `#snomed_ct::389086002\|Hypoxia\|` | Local or openEHR format |
| `Array<T>` | `[val, val, ...]` | Tuple-like structure |
| `List<T>` | `(val, val, ...)` | Linear collection |
| `Set<T>` | `{val, val, ...}` | Unique membership set |
| `Map<K, V>` | `{ key: val, key: val, ... }` | Keyed collection |
| `Object` | `{ prop: val, prop: val, ... }` | Property-based object |
| `Interval<T>` | `\|N..M\|`, `\|>N..M\|`, `\|N..<M\|`, etc. | Various interval formats |
| `Tuple` | `[a, b, c]` | Mixed-type sequence |

**TBD:** Consider eliminating `Array` and reserving `[]` for tuples exclusively.

### 4.2. Variables

Symbolic variables are valid within their declaration scope and classified as read-only or writable.

- **Read-only variables** (`EL_READONLY_VARIABLE`): Routine parameters and `Self`
- **Writable variables** (`EL_WRITABLE_VARIABLE`): Locally declared variables and `Result`

#### 4.2.1. Self

A pre-defined read-only reference to the current object is available via `Self`. Unlike some languages, `Self` is not needed to qualify properties or functions, and is generally used only as a function argument.

#### 4.2.2. Result

In any function, `Result` is automatically declared to the return type. This writable variable contains the value returned when the function completes.

### 4.3. Type References

Types may be directly referenced using syntax `{TypeName}`, creating an anonymous read-only instance variable. This enables access to static features and constants without creating instances:

```
{TypeName}.constant_name
{TypeName}.static_function()
```

### 4.4. Feature References

#### 4.4.1. Qualified Referencing

Any feature may appear alone or qualified by scoping entities using dot notation:

```
person1.name
employees[1].name.first_name
blood_pressure.history.events[3].data.data.systolic
agent obstetric_risks.basic_risk
```

#### 4.4.2. Constants

Constants are capitalized labels representing values of any type:

```
Mph_to_kmh_factor = 1.6
Safe_glucose_limits.has (3.5)
```

#### 4.4.3. Property References

Properties are valid within their declaring class and may be used in any routine definition or assertion:

```
diabetic_status
blood_glucose_level
```

#### 4.4.4. Function Calls

Functions are called using typical programming language syntax. Simple functions without arguments may be called with or without parentheses:

```
age
age()
tnm_major_number (tnm_t)
tnm_major_number ("Tis")
```

Function calls may include arguments of other function calls, agents, tuples, operator expressions, and instance references.

#### 4.4.5. Built-in Functions

No built-in functions exist per se; all utility functions come from imported models. The openEHR Base Types provide common functions such as:

```
{Env}.current_date                                -- obtain today's date
blood_glucose_list: List<Real>
{Statistical_evaluator}.max (blood_glucose_list)  -- compute maximum
{Locale}.language                                 -- primary language
```

#### 4.4.6. Container Item Access

Container members are accessed via normal function calls or the `[]` operator:

| Operator | Function | Meaning |
|----------|----------|---------|
| `[i]` | `Array<T>.item(i: Integer): T` | i-th element (1-based) |
| `[i]` | `List<T>.item(i: Integer): T` | i-th element (1-based) |
| `[k]` | `Map<K,V>.item(k: K): V` | Element at key k |

**TBD:** Generic mechanism for mapping operators to member functions requires model-supplied configuration.

#### 4.4.7. Matching Objects

Objects are matched using `[]` syntax with agent arguments of signature `<[T], Boolean>`:

```
class Book {
    title: String;
    pub_date: Date;
    country: Terminology_code;
}

book_list, old_spanish_books: List<Book>

old_spanish_books := book_list [(b:Book) {b.title.contains("Quixote")}]
```

A shorter form assumes the variable:

```
old_spanish_books := book_list [title.contains("Quixote") OR pub_date < P1650Y AND country = #iso639::es]
```

Chaining selectors enables XPath-like expressions:

```
book_list [title.contains("Quixote")][1].pub_date.year
```

The return type is nullable. This requires a `match()` function on container types.

**TBD:** Generic mechanism for mapping operators to member functions.

### 4.5. Predicates

EL predicates express tests on runtime object structures.

#### 4.5.1. Attached() Predicate

The `attached()` predicate tests whether a reference is attached to a value (equivalent to null/None testing in other languages):

```
not attached (test_result) or else test_result.data.events[1].data.value > 6.5
```

### 4.6. Agents

Delayed routine calls use the `agent` keyword. Agents may be created with full or partial argument lists, with `?` symbols representing unfilled arguments:

```
|
| define a naive obstetric risk function
|
obstetric_risk (age: Duration[1]; previous_pregnancies: Integer[1]): Coded_term[1]

|
| generate an agent with signature <[Duration, Integer], Coded_term>
|
agent obstetric_risk

|
| generate an agent with signature <[Integer], Coded_term>
| (age of 38 years is supplied)
|
agent obstetric_risk ('P38Y', ?)
```

Agents may also be created with all arguments supplied for later execution:

```
agent obstetric_risk ('P38Y', 2)  -- generates agent of signature <[],Coded_term>
```

Procedure agents are created similarly, with evaluation type `<[args]>` (no return type).

---

## Complex Expressions

### 5.1. Equality Operator

The `=` operator maps to the function `equal()` on type `Any`. For primitive value types, semantics are value comparison; for other types, reference comparison is used.

For value comparison of non-primitive types, use `Any.is_equal()`, which may be redefined in subtypes.

### 5.2. Primitive Operators

Primitive operators are infix or prefix function syntax on primitive types. For example, `-` (minus) on `Numeric` implements subtraction.

#### 5.2.1. Arithmetic Operators

| Operator | Function | Meaning | Precedence |
|----------|----------|---------|-----------|
| `^` | `exponent()` | Exponentiation | 1 (highest) |
| `*` | `multiply()` | Multiplication | 2 |
| `/` | `divide()` | Division | 2 |
| `%` | `modulus()` | Modulo division | 2 |
| `+` | `add()` | Addition | 3 |
| `-` | `subtract()` | Subtraction | 3 |

#### 5.2.2. Relational Operators

| Operator | Function | Meaning |
|----------|----------|---------|
| `=` | `equal()` | Value equality |
| `!=` | `not_equal()` | Inequality |
| `<` | `less_than()` | Less than |
| `<=` | `less_than_or_equal()` | Less than or equal |
| `>` | `greater_than()` | Greater than |
| `>=` | `greater_than_or_equal()` | Greater than or equal |

#### 5.2.3. Logical Operators

| Operator | Function | Meaning | Precedence |
|----------|----------|---------|-----------|
| `NOT`, `~` | `not()` | Negation | 1 (highest) |
| `AND` | `conjunction()` | Logical AND | 2 |
| `OR` | `disjunction()` | Logical OR | 3 |
| `XOR` | `exclusive_disjunction()` | Exclusive OR | 3 |
| `IMPLIES` | `implication()` | Material implication | 4 |

**Usage examples:**
```
systolic_bp > 140 AND (is_smoker OR is_hypertensive)
```

#### 5.2.4. Additional Operators

**String operators:**
| Operator | Function | Meaning |
|----------|----------|---------|
| `+` | `append()` | String concatenation |

**Date operators:**
| Operator | Function | Meaning |
|----------|----------|---------|
| `+` | `add(d: Duration)` | Add precise duration to date |
| `++` | `add_nominal(d: Duration)` | Add nominal duration to date |
| `-` | `subtract(d: Duration)` | Subtract precise duration |
| `--` | `subtract_nominal(d: Duration)` | Subtract nominal duration |
| `-` | `diff(d: Date)` | Difference of two dates |

**Date_time operators:**
| Operator | Function | Meaning |
|----------|----------|---------|
| `+` | `add(d: Duration)` | Add precise duration |
| `++` | `add_nominal(d: Duration)` | Add nominal duration |
| `-` | `subtract(d: Duration)` | Subtract precise duration |
| `--` | `subtract_nominal(d: Duration)` | Subtract nominal duration |
| `-` | `diff(d: Date_time)` | Difference of two date/times |

**Time operators:**
| Operator | Function | Meaning |
|----------|----------|---------|
| `+` | `add(d: Duration)` | Add duration to time |
| `-` | `subtract(d: Duration)` | Subtract duration from time |
| `-` | `diff(d: Time)` | Difference of two times |

**Duration operators:**
| Operator | Function | Meaning |
|----------|----------|---------|
| `+` | `add(d: Duration)` | Add duration to duration |
| `-` | `subtract(d: Duration)` | Subtract duration from duration |

#### 5.2.5. Logical Negation

The `not` operator applies as a prefix to all Boolean-returning operators and parenthesized Boolean expressions.

#### 5.2.6. Precedence and Parentheses

Operator precedence follows the order shown in operator tables. Parentheses override precedence:

```
systolic_bp > 140 AND (is_smoker OR is_hypertensive)
```

### 5.3. Higher-order Operators

#### 5.3.1. Quantification Operators

**Universal quantification (for_all):**

Textual syntax:
```
for_all v in container_var | <Boolean expression mentioning v>
```

Functional equivalent:
```
list_of_reals: List<Real>

|
| returns true if all values in list exceed 140.0
|
list_of_reals.for_all (
    agent (v: Real): Boolean {
        v > 140.0
    }
)
```

**Existential quantification (there_exists):**

Textual syntax:
```
there_exists v in container_var | <Boolean expression mentioning v>
```

Functional equivalent:
```
list_of_reals: List<Real>

|
| returns true if list contains at least one value greater than 140.0
|
list_of_reals.there_exists (
    agent (v: Real): Boolean {
        v > 140.0
    }
)
```

### 5.4. Decision Tables

Decision tables express multi-branch constructs returning single expressions. Two flavours exist: condition chains (if/then/else) and case tables (case statements). Both are purely functional--branches contain expressions only, not statements.

#### 5.4.1. Condition Chain (if/then)

Standard form:
```
choice in
    <condition_1>:  <expression_1>,
    <condition_2>:  <expression_2>,
    ...
    <condition_N>:  <expression_N>,
    *:              <else expression>
;
```

The `*` character represents a catch-all else branch.

**Realistic example:**
```
molecular_subtype: Terminology_term
    Result := choice in
        =========================================================
        er_positive and
        her2_negative and
        not ki67.in_range ([high]):    #luminal_A,
        ---------------------------------------------------------
        er_positive and
        her2_negative and
        ki67.in_range ([high]):        #luminal_B_HER2_negative,
        ---------------------------------------------------------
        er_positive and
        her2_positive:                 #luminal_B_HER2_positive,
        ---------------------------------------------------------
        er_negative and
        pr_negative and
        her2_positive and
        ki67.in_range ([high]):        #HER2,
        ---------------------------------------------------------
        er_negative and
        pr_negative and
        her2_negative and
        ki67.in_range ([high]):        #triple_negative,
        ---------------------------------------------------------
        *:                             #none
        =========================================================
    ;
```

**Compact form (binary choice):**

For single conditions, use C-style ternary syntax:
```
calculate_score: Integer
    Result := expr1 ? 2 : 0
```

**Arithmetic computation example:**
```
ipi_raw_score: Integer
    Result := Result.add (
        =============================================
        age > 60                             ? 1 : 0,
        staging matches {#stage_III, #stage_IV}    ? 1 : 0,
        ldh.in_range (#normal)               ? 1 : 0,
        ecog > 1                             ? 1 : 0,
        extranodal_sites > 1                 ? 1 : 0
        =============================================
    )
    ;
```

#### 5.4.2. Case Table

Case table syntax tests a single expression against multiple value ranges:

```
gfr_range: Real

risk_assessment: Real
    Result := case gfr_range in
        =================
        |>20|:      1,
        |10 - 20|:  0.75,
        |<10|:      0.5
        =================
    ;
```

Each branch condition takes the form `Expr matches Constri` where `Expr` is identical across branches.

#### 5.4.3. Nested Case Table

Case tables may be nested to create complex decision logic:

```
post_bureau_risk_category: Terminology_term
    Result := case existing_customer in
        ========================================
        True:   case
                appl_risk_score
                in
                --------------------------------
                |<=120|:     case
                            credit_score
                            in
                            --------------------
                            |<590|:      #HIGH,
                            |590..610|:  #MEDIUM,
                            |>610|:      #LOW
                            --------------------
                            ;,
                |>120|:     case
                            credit_score
                            in
                            --------------------
                            |<600|:      #HIGH,
                            |600..625|:  #MEDIUM,
                            |>625|:      #LOW
                            --------------------
                            ;
                --------------------------------
                ;,
        False:  case
                appl_risk_score
                in
                --------------------------------
                |<=100|:     case
                            credit_score
                            in
                            --------------------
                            |<580|:      #HIGH,
                            |580..600|:  #MEDIUM,
                            |>600|:      #LOW
                            --------------------
                            ;,
                |>100|:     case
                            credit_score
                            in
                            --------------------
                            |<590|:      #HIGH,
                            |590..615|:  #MEDIUM,
                            |>615|:      #LOW
                            --------------------
                            ;
                --------------------------------
                ;
        ========================================
        ;
    ;
```

---

## Syntax Specification

ANTLR4 grammar files are available in the [openEHR Antlr4 Git repository](https://github.com/openEHR/openEHR-antlr4/tree/master/combined/src/main/antlr).

### Parser Grammar

```antlr
// ========================== EL Statements ==========================

statementBlock: statement+ EOF ;

statement: declaration | assignment | assertion ;

declaration:
      variableDeclaration
    | constantDeclaration
    ;

variableDeclaration: instantiableRef ':' typeId ( SYM_ASSIGNMENT expression )? ;

constantDeclaration: constantId ':' typeId ( SYM_EQ expression )? ;

assignment: valueGenerator SYM_ASSIGNMENT expression ;

assertion: ( ( LC_ID | UC_ID ) ':' )? SYM_ASSERT booleanExpr ;

// ========================== EL Expressions ==========================

expression:
      terminal
    | operatorExpression
    | tuple
    ;

operatorExpression:
      booleanExpr
    | arithmeticExpr
    ;

// ------------------- Boolean-returning operator expressions --------------------

booleanExpr:
      SYM_NOT booleanExpr
    | booleanExpr SYM_AND booleanExpr
    | booleanExpr SYM_XOR booleanExpr
    | booleanExpr SYM_OR booleanExpr
    | booleanExpr SYM_IMPLIES booleanExpr
    | booleanExpr ( SYM_IFF | SYM_EQ ) booleanExpr
    | booleanLeaf
    ;

booleanLeaf:
      booleanValue
    | forAllExpr
    | thereExistsExpr
    | arithmeticConstraintExpr
    | generalConstraintExpr
    | '(' booleanExpr ')'
    | SYM_DEFINED '(' valueGenerator ')'
    | arithmeticComparisonExpr
    | objectComparisonExpr
    | valueGenerator
    ;

forAllExpr: SYM_FOR_ALL localVariableId ':' valueGenerator '|' booleanExpr ;

thereExistsExpr: SYM_THERE_EXISTS localVariableId ':' valueGenerator '|' booleanExpr ;

arithmeticConstraintExpr: arithmeticLeaf SYM_MATCHES '{' cInlineOrderedObject '}' ;

generalConstraintExpr: simpleTerminal SYM_MATCHES '{' cObjectMatcher '}' ;

// --------------------------- Arithmetic operator expressions --------------------------

arithmeticComparisonExpr: arithmeticExpr comparisonBinop arithmeticExpr ;

comparisonBinop:
      SYM_EQ
    | SYM_NE
    | SYM_GT
    | SYM_LT
    | SYM_LE
    | SYM_GE
    ;

arithmeticExpr:
      <assoc=right> arithmeticExpr '^' arithmeticExpr
    | arithmeticExpr ( '/' | SYM_ASTERISK | '%' ) arithmeticExpr
    | arithmeticExpr ( '+' | '-' ) arithmeticExpr
    | arithmeticLeaf
    ;

arithmeticLeaf:
      arithmeticValue
    | '(' arithmeticExpr ')'
    | valueGenerator
    | simpleCaseTable
    ;

arithmeticValue:
      integerValue
    | realValue
    | dateValue
    | dateTimeValue
    | timeValue
    | durationValue
    ;

// -------------------- Equality operator expressions for other types ------------------------

objectComparisonExpr: simpleTerminal equalityBinop simpleTerminal ;

equalityBinop:
    SYM_EQ
  | SYM_NE
  ;

// ========================== Tuples ============================

tuple: '[' expression ( ',' expression )+ ']';

// ========================== Value-generating Expressions ==========================

terminal:
      simpleTerminal
    | decisionTable
    ;

simpleTerminal:
      primitiveObject
    | valueGenerator
    ;

valueGenerator:
      bareRef
    | scopedFeatureRef
    | typeRef
    ;

bareRef:
      boundVariableId
    | staticRef
    | localRef
    | functionCall
    ;

staticRef:
      SYM_SELF
    | constantId
    ;

localRef:
      SYM_RESULT
    | localVariableId
    ;

scopedFeatureRef: scoper featureRef ;

scoper: ( typeRef '.' )? ( bareRef '.' )* ;

typeRef: '{' typeId '}' ;

typeId: UC_ID ( '<' typeId ( ',' typeId )* '>' )? ;

featureRef:
      functionCall
    | instantiableRef
    ;

instantiableRef:
      boundVariableId
    | localVariableId
    | constantId
    ;

boundVariableId: BOUND_VARIABLE_ID ;

localVariableId: LC_ID ;

constantId: UC_ID ;

functionCall: LC_ID '(' exprList? ')' ';'? ;

exprList: expression ( ',' expression )* ;

// ========================== Decision Tables ============================

decisionTable:
      binaryChoice
    | caseTable
    | conditionTable
    ;

caseTable:
      simpleCaseTable
    | generalCaseTable
    ;

conditionTable: SYM_CHOICE SYM_IN ( conditionBranch ',' )+ ( conditionBranch | conditionDefaultBranch ) ';' ;

conditionBranch: booleanExpr ':' expression ;

conditionDefaultBranch: SYM_ASTERISK ':' expression ;

binaryChoice:  booleanExpr '?' simpleTerminal ':' simpleTerminal ;

generalCaseTable: SYM_CASE expression SYM_IN ( generalCaseBranch ',' )+ ( generalCaseBranch | generalCaseDefaultBranch ) ';' ;

generalCaseBranch: primitiveObject ':' expression ;

generalCaseDefaultBranch: SYM_ASTERISK ':' expression ;

simpleCaseTable: SYM_CASE simpleTerminal SYM_IN ( simpleCaseBranch ',' )+ ( simpleCaseBranch | simpleCaseDefaultBranch ) ';' ;

simpleCaseBranch: primitiveObject ':' simpleTerminal ;

simpleCaseDefaultBranch: SYM_ASTERISK ':' simpleTerminal ;
```

### Lexer Grammar

```antlr
lexer grammar ElLexer;
import AdlPathLexer, Cadl2Lexer, GeneralLexer;

channels {
    COMMENT
}

// ============== Lines and Comments ==============

CMT_LINE : '--' .*? EOL -> channel(COMMENT) ;
TABLE_CMT_LINE : '===' '='* EOL -> channel(COMMENT) ;
EOL      : '\r'? '\n'   -> channel(HIDDEN) ;
WS       : [ \t\r]+     -> channel(HIDDEN) ;

// ============== Keywords ==============

SYM_DEFINED : 'defined' ;
SYM_SELF    : 'Self' ;
SYM_IN      : 'in' ;
SYM_CHOICE  : 'choice' ;
SYM_CASE    : 'case' ;
SYM_RESULT  : 'Result' ;

// ============== Symbols ==============

SYM_ASSIGNMENT: ':=' ;
SYM_COLON : ':' ;
SYM_INTERROGATION: '?' ;
SYM_NE : '/=' | '!=' ;
SYM_EQ : '=' ;
SYM_GT : '>' ;
SYM_LT : '<' ;
SYM_LE : '<=' ;
SYM_GE : '>=' ;

SYM_PLUS    : '+' ;
SYM_MINUS   : '-' ;
SYM_SLASH   : '/' ;
SYM_PERCENT : '%' ;
SYM_CARET   : '^' ;
SYM_DOT     : '.' ;

SYM_DOUBLE_MINUS: '--' ;
SYM_DOUBLE_PLUS: '++' ;

SYM_THEN     : 'then' | 'THEN' ;
SYM_AND      : 'and' | 'AND' ;
SYM_OR       : 'or' | 'OR' ;
SYM_XOR      : 'xor' | 'XOR' ;
SYM_NOT      : 'not' | 'NOT' | '!' | '~' ;
SYM_IMPLIES  : 'implies' ;
SYM_FOR_ALL  : 'for_all' ;
SYM_THERE_EXISTS: 'there_exists' ;
SYM_MATCHES  : 'matches' | 'is_in' ;
SYM_ASSERT   : 'assert' ;

SYM_EXISTS   : 'exists' ;

BOUND_VARIABLE_ID: '$' LC_ID ;

LOCAL_TERM_CODE_REF: '[' ALPHANUM_US_CHAR+ ']' ;
```

---

## References

1. Hein, J. L. (2002). _Discrete Structures, Logic and Computability_ (Second Edition). Jones and Bartlett.

2. Kilov, H., & Ross, J. (1994). _Information Modelling: An Object-Oriented Approach_. Prentice Hall.

3. Sowa, J. F. (2000). _Knowledge Representation: Logical, Philosophical and Computational Foundations_. California: Brooks/Cole.

---

**Last Updated:** 2022-05-10 13:51:02 +0100