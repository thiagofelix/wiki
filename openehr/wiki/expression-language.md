---
title: Expression Language (EL)
type: entity
sources:
  - raw/lang-el.md
  - raw/lang-bel.md
created: 2026-04-13
updated: 2026-04-13
---

# Expression Language (EL)

The openEHR Expression Language (EL) is a typed expression language whose meta-model is defined in the `expression` package of the [[basic-meta-model]]. EL provides syntax representation for expressions used in BMM models, archetype rules ([[archetype-object-model]] assertions), [[task-planning]] expressions, [[guideline-definition-language]] versions, and decision language expressions. EL is part of the LANG component and is currently in DEVELOPMENT status.

EL supersedes the earlier Basic Expression Language (BEL), which remains documented below for historical context.

## Design Background

EL combines first-order predicate logic, object-oriented structural concepts, and functional computing. It has similarities with OMG's OCL (Object Constraint Language) and draws on semantics from the Eiffel Language (ECMA-367), but differs in its BMM-based meta-model foundation and syntax designed for developers familiar with modern languages (Java, C#, Python, TypeScript).

### Key Capabilities

- Strong typing and void-safety
- Standard arithmetic, boolean, and relational operators
- Object-oriented qualification using dot notation
- Decision structures (binary choice, condition chains, case tables)
- Functions and agents (lambdas)
- Logical quantifiers (for_all, there_exists)
- Multi-lingual translations for symbolic variables (similar to ADL2)

### Execution Model

Expressions are evaluated by an _evaluator_ against a _data context_, which determines truth values. The data context provides variables that may be read from and written to. Two specification modes exist:

- **Implicit context**: Variables inferred from data binding
- **Explicit context**: EL expressions within a BMM model or context explicitly importing a BMM model

Parsed expressions result in instances of BMM EL meta-types (the `EL_*` classes defined in [[basic-meta-model]]).

## Type System

EL is fully typed. All operators map to operator-aliased functions defined in the BMM as `BMM_ROUTINE` descendants. For example, the `+` operator maps to the `add()` function on `Integer`.

### Primitive Types

| Name | Description |
|------|-------------|
| `Boolean` | Boolean value |
| `Integer` | Signed integer (-2^31 to 2^31-1) |
| `Integer64` | Large integer |
| `Real` | Real value |
| `Double` | Double precision real |
| `Date` | ISO 8601 date |
| `Date_time` | ISO 8601 date/time |
| `Time` | ISO 8601 time |
| `Duration` | ISO 8601 duration |
| `String` | String value |
| `Uri` | IETF RFC 3986 URI |
| `Terminology_code` | Terminology code reference |

Automatic type promotion from `Integer` to `Real` applies to mixed expressions.

### Container Types

| Name | Description |
|------|-------------|
| `Container<T>` | Abstract parent of collection types |
| `List<T>` | Ordered list allowing repeated membership |
| `Set<T>` | Unordered set with unique membership |
| `Map<K:Ordered, V>` | Indexed linear container |

### Interval Type

| Name | Description |
|------|-------------|
| `Interval<T:Ordered>` | Interval of any ordered type |
| `Point_interval<T:Ordered>` | Identical boundary interval |
| `Proper_interval<T:Ordered>` | Different boundary interval |

Complex types are imported from BMM model definitions and become available like foundation types.

## Syntax Style

EL syntax uses snake_case conventions:

- Class names: `Iso8601_date_time`, `Arrayed_list<T>`
- Properties/variables: `employee_group`, `average_pressure()`
- Constants/class functions: `Maximum_speed`

Comments use `--` (end-of-line) or `|` (line comments). Visual dividers use `--------` or `========`.

## Terminal Entities

Terminal entities correspond to the `EL_TERMINAL` meta-type. Three categories exist:

### Literals

Literal values use [[odin]]-compatible syntax for most types, with distinct bracket types for containers:

- `Boolean`: `True`, `False`
- `Integer`: `10`, `-4`, `5e09`
- `Real`: `10.0`, `0.345`, `22.5%`, `6.023e23`
- `Date`: `2004-08-12`
- `String`: `"this is a string"`
- `Uri`: `<https://en.wikipedia.org>`
- `Terminology_code`: `#identifier` or `#snomed_ct::389086002|Hypoxia|`
- `List<T>`: `(val, val, ...)`
- `Set<T>`: `{val, val, ...}`
- `Map<K, V>`: `{ key: val, key: val, ... }`
- `Interval<T>`: `|N..M|`, `|>N..M|`, `|<N|`, etc.

### Variables

Variables are classified as read-only or writable within their declaration scope:

- **Read-only** (`EL_READONLY_VARIABLE`): Routine parameters and `Self` (reference to current object)
- **Writable** (`EL_WRITABLE_VARIABLE`): Locally declared variables and `Result` (automatic return value in functions)

### Type References

Types may be directly referenced using `{TypeName}` syntax for accessing static features:

```
{Env}.current_date
{Statistical_evaluator}.max(blood_glucose_list)
{Locale}.language
```

### Feature References

Features use dot-qualified notation:

```
person1.name
employees[1].name.first_name
blood_pressure.history.events[3].data.data.systolic
```

Function calls use standard syntax. Parentheses are optional for zero-argument functions.

### Container Item Access

```
list[i]       -- i-th element (1-based)
map[key]      -- element at key
```

### Matching Objects

Objects are matched using agent-based selectors in `[]`:

```
old_spanish_books := book_list [title.contains("Quixote")]
book_list [title.contains("Quixote")][1].pub_date.year  -- XPath-like chaining
```

### Predicates

- **attached()**: Tests whether a reference is non-null
- **defined()**: Tests whether a variable is defined

```
not attached(test_result) or else test_result.data.events[1].data.value > 6.5
```

### Agents

Delayed routine calls use the `agent` keyword with optional partial argument lists (`?` for unfilled arguments):

```
agent obstetric_risk              -- full agent: <[Duration, Integer], Coded_term>
agent obstetric_risk('P38Y', ?)   -- partial: <[Integer], Coded_term>
agent obstetric_risk('P38Y', 2)   -- closed: <[], Coded_term>
```

## Operators

### Arithmetic Operators

| Operator | Function | Precedence |
|----------|----------|-----------|
| `^` | `exponent()` | 1 (highest) |
| `*` | `multiply()` | 2 |
| `/` | `divide()` | 2 |
| `%` | `modulus()` | 2 |
| `+` | `add()` | 3 |
| `-` | `subtract()` | 3 |

### Relational Operators

| Operator | Function |
|----------|----------|
| `=` | `equal()` (value equality for primitives, reference for others) |
| `!=` | `not_equal()` |
| `<` | `less_than()` |
| `<=` | `less_than_or_equal()` |
| `>` | `greater_than()` |
| `>=` | `greater_than_or_equal()` |

### Logical Operators

| Operator | Function | Precedence |
|----------|----------|-----------|
| `NOT` / `~` | `not()` | 1 (highest) |
| `AND` | `conjunction()` | 2 |
| `OR` | `disjunction()` | 3 |
| `XOR` | `exclusive_disjunction()` | 3 |
| `IMPLIES` | `implication()` | 4 |

### Date/Time Operators

Date, Date_time, Time, and Duration types support:

- `+` / `-`: Add/subtract precise durations
- `++` / `--`: Add/subtract nominal durations (e.g., calendar months)
- `-` (binary): Difference between two date/time values

### String Operators

`+` maps to `append()` for string concatenation.

## Decision Structures

### Condition Chain (choice in)

Multi-branch if/then/else returning an expression:

```
molecular_subtype: Terminology_term
    Result := choice in
        er_positive and her2_negative and
        not ki67.in_range([high]):    #luminal_A,
        er_positive and her2_negative and
        ki67.in_range([high]):        #luminal_B_HER2_negative,
        *:                            #none
    ;
```

The `*` character represents the else (catch-all) branch.

### Binary Choice

C-style ternary syntax for single conditions:

```
Result := expr1 ? 2 : 0
```

Can be composed for additive scoring:

```
ipi_raw_score: Integer
    Result := Result.add(
        age > 60               ? 1 : 0,
        staging matches {#stage_III, #stage_IV} ? 1 : 0,
        ldh.in_range(#normal)  ? 1 : 0
    )
```

### Case Table

Tests a single expression against multiple value ranges:

```
risk_assessment: Real
    Result := case gfr_range in
        |>20|:      1,
        |10 - 20|:  0.75,
        |<10|:      0.5
    ;
```

Case tables may be nested to create complex decision logic (e.g., credit risk scoring with multiple dimensions).

## Higher-Order Features

### Universal Quantification (for_all)

```
for_all v in container_var | <Boolean expression mentioning v>

-- Functional form:
list_of_reals.for_all(
    agent (v: Real): Boolean { v > 140.0 }
)
```

### Existential Quantification (there_exists)

```
there_exists v in container_var | <Boolean expression mentioning v>

-- Functional form:
list_of_reals.there_exists(
    agent (v: Real): Boolean { v > 140.0 }
)
```

## Syntax Specification

EL has a formal ANTLR4 grammar available in the openEHR Antlr4 Git repository. The grammar defines:

- **Statements**: `declaration`, `assignment`, `assertion`
- **Expressions**: `booleanExpr`, `arithmeticExpr`, tuples
- **Decision tables**: `conditionTable`, `caseTable`, `binaryChoice`
- **Value generators**: `bareRef`, `scopedFeatureRef`, `typeRef`, `functionCall`

The lexer imports from `AdlPathLexer`, `Cadl2Lexer`, and `GeneralLexer`.

## Usage Contexts

EL is designed for use in:

- **[[archetype-object-model]] assertions**: Rules sections in AOM2 archetypes
- **[[task-planning]] expressions**: Conditions and computations in clinical workflow plans
- **[[guideline-definition-language]]**: Newer GDL versions for clinical decision support
- **BMM model annotations**: Design-by-contract invariants and pre/post-conditions

---

## Basic Expression Language (BEL) -- Historical Predecessor

The Basic Expression Language (BEL) was the original openEHR expression formalism, extracted from the AOM2 specification to provide a unified expression and rules model for AOM, GDL, and other specifications. BEL holds STABLE status but has been superseded by EL. It remains implemented in the open-source Archie project and is used in production systems.

### Key Differences from EL

| Aspect | BEL | EL |
|--------|-----|-----|
| **Meta-model** | Own Basic Expression Object Model (BEOM) | BMM expression package (`EL_*` classes) |
| **Variable syntax** | `$` prefix (e.g., `$heart_rate`) | No prefix; scoped declarations |
| **Data binding** | Bound variables with archetype paths (e.g., `$weight := /data[id3]/...`) | Implicit or explicit BMM context |
| **Built-in functions** | `current_date()`, `sum()`, `mean()`, `max()`, `min()` | No built-ins; all functions from imported BMM models |
| **Decision structures** | None | Condition chains, case tables, binary choice |
| **Agents/lambdas** | Not supported | Full agent support with partial application |
| **Sub-path variables** | `$event/data[id4]/items[id7]/value` | Dot-qualified references |
| **Status** | STABLE | DEVELOPMENT |

### BEL Design

BEL derives from restricted first-order predicate logic with basic statement types. It uses `$`-prefixed variables following shell script convention. Variable types include:

- **Bound variables**: Mapped to data context fields via archetype paths
- **Local variables**: Declared within the program

BEL is fully typed, using the openEHR Foundation Types. It supports declarations, assignments, and assertions.

### BEL Operators

BEL supports the same arithmetic, relational, and logical operators as EL. Container operators include `there_exists` and `for_all` with `|` separator ("such that" / "it holds that") or `in` keyword.

The `exists` predicate tests bound variable availability -- important because bound variables depend on external entity existence and may be undefined at runtime.

### Basic Expression Object Model (BEOM)

The BEOM defines the parse tree structure with three statement types:

- **ASSERTION**: Boolean-evaluating expression with tag
- **VARIABLE_DECLARATION**: Named, typed variable
- **ASSIGNMENT**: Value assignment to a variable

Expressions form trees of `EXPRESSION` nodes:

- **EXPR_LITERAL**: Manifest constant leaf
- **EXPR_VARIABLE_REF**: Declared variable reference
- **EXPR_FUNCTION_CALL**: Function call with arguments
- **EXPR_UNARY_OPERATOR** / **EXPR_BINARY_OPERATOR**: Operator nodes
- **EXPR_FOR_ALL**: Universal quantification
- **EXTERNAL_QUERY**: Call to external service for data values

The `OPERATOR_KIND` enumeration defines all supported operators (eq, ne, lt, le, gt, ge, matches, not, and, or, xor, implies, for_all, exists, plus, minus, multiply, divide, modulo, exponent).

Typing uses `EXPR_TYPE_DEF` descendants: `TYPE_DEF_BOOLEAN`, `TYPE_DEF_INTEGER`, `TYPE_DEF_REAL`, `TYPE_DEF_DATE`, `TYPE_DEF_DATE_TIME`, `TYPE_DEF_TIME`, `TYPE_DEF_DURATION`, `TYPE_DEF_STRING`, `TYPE_DEF_URI`, `TYPE_DEF_TERMINOLOGY_CODE`, and `TYPE_DEF_OBJECT_REF`.

### Why BEL was Superseded

BEL's BEOM was a standalone meta-model separate from the BMM. EL unifies expression handling by using the BMM expression package directly, enabling:

- Richer type system with full BMM type awareness
- Decision structures (condition chains, case tables) absent from BEL
- Agent/lambda support for functional programming patterns
- No built-in functions -- all functions come from BMM models, making the language extensible
- Integration with BMM design-by-contract features (invariants, pre/post-conditions)
