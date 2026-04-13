# Foundation Types - openEHR BASE Specification

## Document Information

- **Status**: STABLE
- **License**: Creative Commons Attribution-NoDerivs 3.0 Unported
- **Copyright**: The openEHR Foundation
- **Package**: `org.openehr.base.foundation_types`

---

## Table of Contents

- [Amendment Record](#amendment-record)
- [Acknowledgements](#acknowledgements)
- [1. Preface](#preface)
- [2. Overview](#overview)
- [3. Primitive Types](#primitive-types)
- [4. Structure Types](#structure-types)
- [5. Interval](#interval)
- [6. Time Types](#time-types)
- [7. Terminology Package](#terminology-package)
- [8. Functional Meta-types](#functional-meta-types)
- [9. Type Cross-Reference](#type-cross-reference)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| BASE Release 1.2.0 | SPECBASE-34: Allow +14:00 timezone; SPECBASE-25: Improve function definitions, add nominal computation functions | S Iancu, openEHR SEC | 22 Mar 2021, 30 Apr 2020 |
| BASE Release 1.1.0 | SPECRM-72: Add guidance on date/time formatting; SPECBASE-15: Add foundation types to BASE, rename Aggregate to Container; SPECPUB-6: Correct UML package nesting | B Lah, T Beale | 22 Nov 2018, 19 Jul 2018, 27 Nov 2017 |
| 0.7.6 | Re-organise heading structure, remove ISO 11404 references, rename to 'Foundation types' | T Beale | 17 Aug 2017 |
| 0.7.0 | Initial Writing from openEHR RM Release 1.0.3 Support Model | T Beale | 20 May 2016 |

---

## Acknowledgements

### Authors

Developed and maintained by the openEHR Specifications Editorial Committee.

### Contributors

Input from the openEHR and broader health informatics community.

### Trademarks

'openEHR' is a registered trademark of the openEHR Foundation.

---

## Preface

### Purpose

This specification defines the openEHR Foundation Types: "a collection of built-in and library types whose semantics are assumed by all other openEHR specifications."

**Intended audience:**
- Standards bodies producing health informatics standards
- Research groups using openEHR, ISO 13606, archetypes
- Open source healthcare community
- Solution vendors

### Related Documents

- The openEHR Architecture Overview

### Status

STABLE. Development version available at the openEHR specifications portal.

### Previous Versions

#### Interval Types

New types `Point_interval` and `Proper_interval` support specification of point values and proper intervals as substitutable types. Types `Multiplicity_interval` and `Cardinality` added from AOM2 specification.

#### Functional Meta-types

Collection of meta-types representing routines, procedures, and functions added to support functional programming primitives in specifications.

---

## Overview

The `org.openehr.base.foundation_types` package comprises generic low-level types assumed throughout openEHR components. These types establish names, minimal semantics, and implementation mapping points.

Type sources include:
- ISO 8601 (2019) date/time standard
- Major interoperability formalisms (OMG IDL, W3C XML-schema)
- Major typed programming languages (Java, C#, C++)

### Package Structure

The foundation types package contains:

- **primitive_types**: Boolean, Character, Octet, String, Uri, Integer, Integer64, Real, Double
- **structures**: Container, List, Set, Array, Hash
- **time**: ISO 8601-based temporal types
- **interval**: Interval, Point_interval, Proper_interval, Multiplicity_interval, Cardinality
- **terminology**: Terminology_code, Terminology_term
- **functional**: ROUTINE, FUNCTION, PROCEDURE, TUPLE

Two type categories are defined:
- **Built-in types**: Part of language type system (marked with `<<Value_type>>` stereotype)
- **Library types**: Available in standard libraries

### Operators

Operations support operator equivalents via two stereotypes:

- `<<ops>>`: Default operators expressible in normal text (e.g., `'='` for `equal()`)
- `<<sym_ops>>`: Additional symbolic operators for mathematical/logical operations (e.g., `'for_all'` for `for_all()`)

Operators enable function signature-matching from parsed expressions.

### The Any Class

All object-oriented and modern programming environments include an ultimate ancestor type. This specification assumes `Any`, defining minimal equality operations:

- `equal(other: Any): Boolean` -- Reference equality for references, value equality for values
- `is_equal(other: Any): Boolean` -- Value equality; typically redefined in descendants

The `equal()` operation renders as `'='`, while `is_equal()` uses function call syntax.

### openEHR Leaf Types

Leaf types are terminal or endpoint types used as values in other information models. Key leaf types include all primitives, temporal types (Iso8601_date, Iso8601_time, etc.), and terminology types.

### Class Definitions

#### Any Class (Abstract)

Abstract ancestor class for all other classes. Maps to `Any` or `Object` in object-oriented technologies.

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_equal(other: Any): Boolean` (abstract) | Value equality: true if objects considered equal in value |
| `equal(other: Any): Boolean` alias "=", "==" | Reference equality for references, value equality for values |
| `instance_of(a_type: String): Any` | Create new instance of a type |
| `type_of(an_object: Any): String` | Type name of object as string, may include generic parameters |
| `not_equal(other: Ordered): Boolean` alias "!=", "!=" | True if current object not equal to other |

---

## Primitive Types

### Overview

Primitive types assumed by openEHR models are supported directly by most programming languages.

| Type | Description |
|------|-------------|
| `Octet` | 8-bit value |
| `Character` | Member of 8-bit character-set |
| `Boolean` | Logical True/False values |
| `Integer` | 32-bit integers |
| `Integer64` | 64-bit integers |
| `Real` | 32-bit floating point numbers |
| `Double` | 64-bit floating point numbers |
| `String` | Unicode-enabled strings |

### Unicode

"Unicode is supported by the type String" for all Asian, Arabic, and script languages. UTF-8 encoding is assumed in openEHR.

### Class Definitions

#### Boolean Class

Type representing minimal interface of built-in Boolean.

**Inherits:** `Any`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `conjunction(other: Boolean): Boolean` alias "and" | Logical conjunction |
| `semistrict_conjunction(other: Boolean): Boolean` alias "and then", "&&" | Semi-strict conjunction |
| `disjunction(other: Boolean): Boolean` alias "or" | Boolean disjunction |
| `semistrict_disjunction(other: Boolean): Boolean` alias "or else", "\|\|" | Semi-strict disjunction |
| `exclusive_disjunction(other: Boolean): Boolean` alias "xor" | Exclusive or |
| `implication(other: Boolean): Boolean` alias "implies" | Boolean implication (semi-strict) |
| `negation(): Boolean` alias "not", "!" | Boolean negation |

**Invariants:**
- `Involutive_negation`: Double negation returns original value
- `Non_contradiction`: Cannot be both true and false simultaneously
- `Completeness`: Either true or false

#### Ordered Class (Abstract)

Abstract parent of ordered types where `<` operator is defined.

**Inherits:** `Any`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `less_than(other: Ordered): Boolean` alias "<" (abstract) | Returns true if current object < other |
| `less_than_or_equal(other: Ordered): Boolean` alias "<=" | True if current <= other |
| `greater_than(other: Ordered): Boolean` alias ">" | True if current > other |
| `greater_than_or_equal(other: Ordered): Boolean` alias ">=" | True if current >= other |

#### Character Class

Type representing minimal interface of built-in Character.

**Inherits:** `Ordered`

#### Octet Class

Type representing minimal interface of built-in Octet.

**Inherits:** `Ordered`

#### String Class

Type representing minimal interface of built-in String for textual data.

**Inherits:** `Ordered`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_empty(): Boolean` | True if string equals "" |
| `is_integer(): Boolean` | True if string parseable as integer |
| `as_integer(): Integer` | Return integer value from string |
| `append(other: String): String` alias "+" | Concatenate other to string |
| `less_than(other: String): Boolean` alias "<" (effected) | Lexical comparison |
| `contains(other: String): Boolean` | True if string contains other (case-sensitive) |

#### Uri Class

String subtype constrained to RFC 3986 syntax.

**Inherits:** `String`

#### Numeric Class (Abstract)

Abstract parent of numeric types with arithmetic and comparison operators.

**Inherits:** `Any`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `add(other: Numeric): Numeric` alias "+" (abstract) | Sum with other (commutative) |
| `subtract(other: Numeric): Numeric` alias "-" (abstract) | Result of subtracting other |
| `multiply(other: Numeric): Numeric` alias "*" (abstract) | Product by other |
| `divide(other: Numeric): Numeric` alias "/" (abstract) | Divide by other |
| `exponent(other: Numeric): Numeric` alias "^" (abstract) | Exponentiation by other |
| `negative(): Numeric` alias "-" (abstract) | Negative of current value |

#### Ordered_Numeric Class (Abstract)

Abstract notional parent of ordered numeric types with both `less_than()` and arithmetic functions.

**Inherits:** `Ordered`, `Numeric`

#### Integer Class

Type representing minimal interface of 32-bit integers.

**Inherits:** `Ordered_Numeric`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `add(other: Integer): Integer` alias "+" (effected) | Integer addition |
| `subtract(other: Integer): Integer` alias "-" (effected) | Integer subtraction |
| `multiply(other: Integer): Integer` alias "*" (effected) | Integer multiplication |
| `divide(other: Integer): Double` alias "/" (effected) | Integer division |
| `exponent(other: Double): Double` alias "^" (effected) | Integer exponentiation |
| `modulo(mod: Integer): Integer` alias "mod", "\\" | Self modulo other |
| `less_than(other: Integer): Boolean` alias "<" (effected) | True if < other |
| `negative(): Integer` alias "-" (effected) | Negative of current value |
| `is_equal(other: Integer): Boolean` (effected) | Value equality |
| `equal(other: Integer): Boolean` alias "=", "==" (redefined) | Reference/value equality |

#### Integer64 Class

Type representing minimal interface of 64-bit integers.

**Inherits:** `Ordered_Numeric`

**Functions:** Same operations as `Integer` class, returning `Integer64` where appropriate.

#### Real Class

Type for single-precision floating point decimal numbers.

**Inherits:** `Ordered_Numeric`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `floor(): Integer` | Greatest integer <= current value |
| `add(other: Real): Real` alias "+" (effected) | Real addition |
| `subtract(other: Real): Real` alias "-" (effected) | Real subtraction |
| `multiply(other: Real): Real` alias "*" (effected) | Real multiplication |
| `divide(other: Real): Double` alias "/" (effected) | Real division |
| `exponent(other: Double): Double` alias "^" (effected) | Real exponentiation |
| `less_than(other: Real): Boolean` alias "<" (effected) | True if < other |
| `negative(): Real` alias "-" (effected) | Negative of current value |
| `is_equal(other: Real): Boolean` (effected) | Value equality |
| `equal(other: Real): Boolean` alias "=", "==" (redefined) | Reference/value equality |

#### Double Class

Type for double-precision floating point decimal numbers.

**Inherits:** `Ordered_Numeric`

**Functions:** Same operations as `Real` class, returning `Double` where appropriate.

---

## Structure Types

### Overview

Basic data structures assumed standardly available in implementation technologies.

| Type | Description |
|------|-------------|
| `Array<T>` | Physical container indexed by number |
| `List<T>` | Ordered container, non-unique membership |
| `Set<T>` | Unordered container, unique membership |
| `Hash<K:Ordered, V>` | Table of values keyed by ordered type K |

These are minimum structure types assumed by openEHR. Implementation workarounds or equivalences may be needed.

### Class Definitions

#### Container Class (Abstract)

Abstract ancestor of container types with addressable items.

**Inherits:** `Any`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `has(v: T): Boolean` (abstract) | Test for membership of value |
| `count(): Integer` (abstract) | Number of items in container |
| `is_empty(): Boolean` (abstract) | True if container is empty |
| `there_exists(test: Operation): Boolean` | Existential quantifier on container |
| `for_all(test: Operation): Boolean` | Universal quantifier on container |
| `matching(test: Operation): List<T>` | Return List of items matching predicate |
| `select(test: Operation): T` | Return first item matching predicate |

#### List Class

Ordered container that may contain duplicates.

**Inherits:** `Container`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `first(): T` | Return first element |
| `last(): T` | Return last element |

**Invariants:**
- `First_validity`: If not empty, first is not Void
- `Last_validity`: If not empty, last is not Void

#### Set Class

Unordered container that may not contain duplicates.

**Inherits:** `Container`

#### Array Class

Container with assumed contiguous storage.

**Inherits:** `Container`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `item(a_key: Integer): T` alias "[]" | Return item for key |

#### Hash Class

Keyed table of values. V is value type, K is key type.

**Inherits:** `Container`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `has_key(a_key: K): Boolean` | Test for presence of key |
| `item(a_key: K): V` alias "[]" | Return item for key |

---

## Interval

### Overview

Interval structures represent ranges of ordered values. The `Interval<T>` class uses intensional definition (states members by implication from limits rather than enumeration).

To support defining times as either fixed points or intervals, classes `Point_interval<T>` and `Proper_interval<T>` are provided. Either may be attached where `Interval<X>` is defined.

Derived types `Multiplicity_interval` and `Cardinality` represent multiplicity, optionality, and cardinality constraints.

### Class Definitions

#### Interval Class (Abstract)

Interval abstraction with upper and lower limits that may be open or closed.

**Inherits:** `Any`

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| `lower: T` (0..1) | Lower bound |
| `upper: T` (0..1) | Upper bound |
| `lower_unbounded: Boolean` (1..1) | Lower boundary open (= -infinity) |
| `upper_unbounded: Boolean` (1..1) | Upper boundary open (= +infinity) |
| `lower_included: Boolean` (1..1) | Lower boundary value included if not lower_unbounded |
| `upper_included: Boolean` (1..1) | Upper boundary value included if not upper_unbounded |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `has(e: T): Boolean` (abstract) | True if value e contained in interval |
| `intersects(other: Interval): Boolean` (abstract) | True if any overlap with other interval |
| `contains(other: Interval): Boolean` (abstract) | True if current properly contains other |
| `is_equal(other: Any): Boolean` (effected) | True if interval semantically same as other |

**Invariants:**
- `Lower_included_valid`: lower_unbounded implies not lower_included
- `Upper_included_valid`: upper_unbounded implies not upper_included
- `Limits_consistent`: Bounded limits must have lower <= upper
- `Limits_comparable`: Limits must be comparable

#### Point_interval Class

Efficient representation of interval that is a point value. Substitutable for `Interval<T>`.

**Inherits:** `Interval`

**Attributes (Redefined):**

| Signature | Meaning |
|-----------|---------|
| `lower_unbounded: Boolean {default = false}` | Lower boundary closed |
| `upper_unbounded: Boolean {default = false}` | Upper boundary closed |
| `lower_included: Boolean {default = true}` | Lower value included |
| `upper_included: Boolean {default = true}` | Upper value included |

**Invariants:**
- `Inv_point`: lower = upper

#### Proper_interval Class

Represents two-sided or one-sided interval.

**Inherits:** `Interval`

**Invariants:**
- `Inv_not_point`: lower != upper

#### Multiplicity_interval Class

Integer interval representing multiplicity, cardinality, and optionality.

**Inherits:** `Proper_interval`

**Constants:**

| Signature | Meaning |
|-----------|---------|
| `Multiplicity_range_marker: String = ".."` | Marker between limits |
| `Multiplicity_unbounded_marker: char = '*'` | Symbol for unbounded upper limit |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_open(): Boolean` | True if no constraints (0..*) |
| `is_optional(): Boolean` | True if optionality expressed (0..1) |
| `is_mandatory(): Boolean` | True if mandation expressed (1..1) |
| `is_prohibited(): Boolean` | True if set to 0..0 |

#### Cardinality Class

Expresses constraints on cardinality of container attributes including uniqueness and ordering.

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| `interval: Multiplicity_interval` (1..1) | Interval of cardinality |
| `is_ordered: Boolean` (1..1) | True if members ordered |
| `is_unique: Boolean` (1..1) | True if members unique |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_bag(): Boolean` | True if unordered, non-unique (bag) |
| `is_list(): Boolean` | True if ordered, non-unique (list) |
| `is_set(): Boolean` | True if unordered, unique (set) |

---

## Time Types

### Overview

Primitive date/time types in openEHR are based on ISO 8601 (2019) standard, supporting partial dates, times, and complex durations needed in biomedical and clinical domains. Types have String physical representation.

Classes are descendants of native types, adding elements required for ISO 8601.

### Primitive Time Types

ISO 8601-based types define dates and times with String representation and support partial/extended semantics.

**Note on class naming:** Classes named `Iso8601_xxx` clearly identify these in openEHR specifications. Real implementations may use other names.

**Recommendation:** "Extended form of date and time strings be used when writing and displaying data, rather than compact form." Extended dates: `yyyy-mm-dd` (not `yyyymmdd`); extended times: `hh:mm:ss` (not `hhmmss`). Both forms should be supported.

**ISO 8601 semantics NOT included:**
- Expanded dates (>4 digit years, negative years)
- YYYY-WW-DD date method
- Fractional minutes/hours (only fractional seconds supported)
- Interval syntax (handled by ADL)

**openEHR deviations from ISO 8601:**
- Week (W) designator can combine with other designators (common for pregnancy durations)
- Durations support negative sign (e.g., '-P3M' for adjusted age)
- Partial date-times can omit hours, days, months (beyond ISO standard; aligns with HL7v2/v3)
- Time 24:00:00 not allowed (midnight = 00:00:00, aligning with HL7v2/v3)

### Derived Interval / Time Types

Useful types generated from date/time classes and Interval classes for common patterns.

### Computational Functions

Two kinds of computational functions defined on date/time types:

**Definite functions:** Computed per standard numeric rules with exact, invariant values.

**Nominal functions:** Computed per "everyday" calendrical rules where year/month are variable periods. Names follow pattern `xxx_nominal()`.

Example: `Iso8601_date.add()` (definite) treats duration as exact amount using average day/month values. `add_nominal()` uses everyday rules (e.g., "a year from now" means same date next year).

Standard operators (`+`, `-`, etc.) used for definite functions; nominal functions use `++`, `--`, etc.

### Class Definitions

#### Time_Definitions Class

Definitions for date/time classes. Timezone limits set by international dateline location (New Zealand: +12:00, not -12:00).

**Constants:**

| Signature | Meaning |
|-----------|---------|
| `Seconds_in_minute: Integer = 60` | Seconds per minute |
| `Minutes_in_hour: Integer = 60` | Minutes per hour |
| `Hours_in_day: Integer = 24` | Clock hours per day |
| `Average_days_in_month: Real = 30.42` | Conversion factor for durations with months |
| `Max_days_in_month: Integer = 31` | Maximum days in any month |
| `Days_in_year: Integer = 365` | Days in normal year |
| `Average_days_in_year: Real = 365.24` | Conversion factor for durations with years |
| `Days_in_leap_year: Integer = 366` | Days in standard leap year |
| `Days_in_week: Integer = 7` | Days per week |
| `Months_in_year: Integer = 12` | Months per year |
| `Min_timezone_hour: Integer = 12` | Minimum timezone hour per ISO 8601 |
| `Max_timezone_hour: Integer = 14` | Maximum timezone hour per ISO 8601 |
| `Nominal_days_in_month: Real = 30.42` | Nominal month conversion factor |
| `Nominal_days_in_year: Real = 365.24` | Nominal year conversion factor |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `valid_year(y: Integer): Boolean` | True if y >= 0 |
| `valid_month(m: Integer): Boolean` | True if 1 <= m <= 12 |
| `valid_day(y, m, d: Integer): Boolean` | True if 1 <= d <= days_in_month(m,y) |
| `valid_hour(h, m, s: Integer): Boolean` | True if (0 <= h < 24) or (h=24 and m=0 and s=0) |
| `valid_minute(m: Integer): Boolean` | True if 0 <= m < 60 |
| `valid_second(s: Integer): Boolean` | True if 0 <= s < 60 |
| `valid_fractional_second(fs: Double): Boolean` | True if 0.0 <= fs < 1.0 |
| `valid_iso8601_date(s: String): Boolean` | True if valid ISO 8601 date string |
| `valid_iso8601_time(s: String): Boolean` | True if valid ISO 8601 time string |
| `valid_iso8601_date_time(s: String): Boolean` | True if valid ISO 8601 date-time string |
| `valid_iso8601_duration(s: String): Boolean` | True if valid ISO 8601 duration string |

#### Temporal Class (Abstract)

Abstract ancestor of time-related classes.

**Inherits:** `Ordered`

#### Iso8601_type Class (Abstract)

Abstract ancestor of ISO 8601 types defining extended/partial concepts.

**Inherits:** `Temporal`, `Time_Definitions`

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| `value: String` (1..1) | String representation of all descendants |

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_partial(): Boolean` (abstract) | True if trailing values missing |
| `is_extended(): Boolean` (abstract) | True if uses '-' and/or ':' separators |

#### Iso8601_date Class

ISO 8601 date including partial and extended forms.

**Value forms:**
- `YYYY-MM-DD` (extended, preferred)
- `YYYYMMDD` (compact)
- Partial forms: `YYYY-MM`, `YYYY`, `YYYYMM`

**Inherits:** `Iso8601_type`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `year(): Integer` | Extract year as integer |
| `month(): Integer` | Extract month as integer, 0 if not present (pre: not month_unknown) |
| `day(): Integer` | Extract day as integer, 0 if not present (pre: not day_unknown) |
| `timezone(): Iso8601_timezone` | Timezone; may be Void |
| `month_unknown(): Boolean` | True if month unknown (form "YYYY") |
| `day_unknown(): Boolean` | True if day unknown (form "YYYY-MM" or "YYYYMM") |
| `is_partial(): Boolean` (effected) | True if days or more missing |
| `is_extended(): Boolean` (effected) | True if uses '-' separators |
| `as_string(): String` | Return value in extended format |
| `add(a_diff: Iso8601_duration): Iso8601_date` alias "+" | Arithmetic addition of duration |
| `subtract(a_diff: Iso8601_duration): Iso8601_date` alias "-" | Arithmetic subtraction of duration |
| `diff(a_date: Iso8601_date): Iso8601_duration` alias "-" | Difference of two dates |
| `add_nominal(a_diff: Iso8601_duration): Iso8601_date` alias "++" | Nominal duration addition |
| `subtract_nominal(a_diff: Iso8601_duration): Iso8601_date` alias "--" | Nominal duration subtraction |

**Invariants:**
- `Year_valid`: year validated
- `Month_valid`: If not unknown, month validated
- `Day_valid`: If not unknown, day validated for year/month
- `Partial_validity`: If month unknown, day must be unknown

#### Iso8601_time Class

ISO 8601 time including partial and extended forms.

**Value forms:**
- `hh:mm:ss[(,|.)sss][Z|+/-hh[:mm]]` (extended, preferred)
- `hhmmss[(,|.)sss][Z|+/-hh[mm]]` (compact)
- Partial forms: `hh:mm`, `hhmm`, `hh`

**Note:** Time 24:00:00 not allowed (deviation from ISO 8601:2004).

**Inherits:** `Iso8601_type`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `hour(): Integer` | Extract hour as integer |
| `minute(): Integer` | Extract minute as integer, 0 if not present |
| `second(): Integer` | Extract integral seconds, 0 if not present |
| `fractional_second(): Real` | Extract fractional seconds, 0.0 if not present (pre: not second_unknown) |
| `timezone(): Iso8601_timezone` | Timezone; may be Void |
| `minute_unknown(): Boolean` | True if form "hh" |
| `second_unknown(): Boolean` | True if form "hh:mm" or "hhmm" |
| `is_decimal_sign_comma(): Boolean` | True if decimal part uses ',' not '.' |
| `is_partial(): Boolean` (effected) | True if seconds or more missing |
| `is_extended(): Boolean` (effected) | True if uses ':' separators |
| `has_fractional_second(): Boolean` | True if fractional_second significant |
| `as_string(): String` | Return value in extended format |
| `add(a_diff: Iso8601_duration): Iso8601_time` alias "+" | Arithmetic addition of duration |
| `subtract(a_diff: Iso8601_duration): Iso8601_time` alias "-" | Arithmetic subtraction of duration |
| `diff(a_time: Iso8601_time): Iso8601_duration` alias "-" | Difference of two times |

**Invariants:**
- `Hour_valid`: Hour validation per valid_hour()
- `Minute_valid`: If not unknown, minute validated
- `Second_valid`: If not unknown, second validated
- `Fractional_second_valid`: If significant, not second_unknown and valid
- `Partial_validity`: If minute unknown, second must be unknown

#### Iso8601_date_time Class

ISO 8601 date/time including partial and extended forms.

**Value forms:**
- `YYYY-MM-DDThh:mm:ss[(,|.)sss][Z|+/-hh[:mm]]` (extended, preferred)
- `YYYYMMDDThhmmss[(,|.)sss][Z|+/-hh[mm]]` (compact)
- Partial variants with missing hours, days, months

**Deviations from ISO 8601:2004:**
- Partial date-times allow missing date/time parts beyond seconds/minutes
- Time 24:00:00 not allowed

**Inherits:** `Iso8601_type`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `year(): Integer` | Extract year |
| `month(): Integer` | Extract month, 0 if not present (pre: not month_unknown) |
| `day(): Integer` | Extract day, 0 if not present (pre: not day_unknown) |
| `hour(): Integer` | Extract hour, 0 if not present (pre: not hour_unknown) |
| `minute(): Integer` | Extract minute, 0 if not present (pre: not minute_unknown) |
| `second(): Integer` | Extract integral seconds, 0 if not present (pre: not second_unknown) |
| `fractional_second(): Real` | Extract fractional seconds, 0.0 if not present |
| `timezone(): Iso8601_timezone` | Timezone; may be Void |
| `month_unknown(): Boolean` | True if month unknown |
| `day_unknown(): Boolean` | True if day unknown |
| `minute_unknown(): Boolean` | True if minute unknown |
| `second_unknown(): Boolean` | True if second unknown |
| `is_decimal_sign_comma(): Boolean` | True if decimal part uses ',' not '.' |
| `is_partial(): Boolean` (effected) | True if seconds or more missing |
| `is_extended(): Boolean` (effected) | True if uses '-', ':' separators |
| `has_fractional_second(): Boolean` | True if fractional_second significant |
| `as_string(): String` | Return value in extended format |
| `add(a_diff: Iso8601_duration): Iso8601_date_time` alias "+" | Arithmetic addition |
| `subtract(a_diff: Iso8601_duration): Iso8601_date_time` alias "-" | Arithmetic subtraction |
| `diff(a_date_time: Iso8601_date_time): Iso8601_duration` alias "-" | Difference of two date-times |
| `add_nominal(a_diff: Iso8601_duration): Iso8601_date` alias "++" | Nominal duration addition |
| `subtract_nominal(a_diff: Iso8601_duration): Iso8601_date` alias "--" | Nominal duration subtraction |

**Invariants:**
- `Year_valid`: Year validated
- `Month_valid`: Month validated
- `Day_valid`: Day validated for year/month
- `Hour_valid`: Hour validated
- `Minute_valid`: If not unknown, minute validated
- `Second_valid`: If not unknown, second validated
- `Fractional_second_valid`: If significant, not second_unknown and valid
- `Partial_validity_*`: Month, day, hour not unknown; if minute unknown, second must be unknown

#### Iso8601_duration Class

ISO 8601 duration with multiple parts from years to seconds.

**Value form:** `P[nnY][nnM][nnW][nnD][T[nnH][nnM][nnS]]`

**Deviations from ISO 8601:**
- Negative sign supported
- 'W' designator may combine with other designators

**Inherits:** `Iso8601_type`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `is_extended(): Boolean` (effected) | Returns True |
| `is_partial(): Boolean` (effected) | Returns False |
| `years(): Integer` | Number of years (value before 'Y') |
| `months(): Integer` | Number of months (value before 'M' in YMD part) |
| `days(): Integer` | Number of days (value before 'D') |
| `hours(): Integer` | Number of hours (value before 'H' in HMS part) |
| `minutes(): Integer` | Number of minutes (value before 'M' in HMS part) |
| `seconds(): Integer` | Integral seconds (before decimal point) |
| `fractional_seconds(): Real` | Fractional seconds (after decimal point) |
| `weeks(): Integer` | Number of weeks (value before 'W') |
| `is_decimal_sign_comma(): Boolean` | True if decimal uses ',' not '.' |
| `to_seconds(): Real` | Total seconds including fractional, using average values for year/month |
| `as_string(): String` | Return duration value |
| `add(a_val: Iso8601_duration): Iso8601_duration` alias "+" | Duration addition via seconds conversion |
| `subtract(a_val: Iso8601_duration): Iso8601_duration` alias "-" | Duration subtraction via seconds conversion |
| `multiply(a_val: Real): Iso8601_duration` alias "*" | Duration multiplication by number |
| `divide(a_val: Real): Iso8601_duration` alias "/" | Duration division by number |
| `negative(): Iso8601_duration` alias "-" | Negative of current duration |

**Invariants:**
- `Years_valid`: years >= 0
- `Months_valid`: months >= 0
- `Weeks_valid`: weeks >= 0
- `Days_valid`: days >= 0
- `Hours_valid`: hours >= 0
- `Minutes_valid`: minutes >= 0
- `Seconds_valid`: seconds >= 0
- `Fractional_second_valid`: 0.0 <= fractional_second < 1.0

#### Iso8601_timezone Class

ISO 8601 timezone string in format: `Z | +/-hh[mm]`

Where:
- `hh`: "00" - "23" (zero-filled to two digits)
- `mm`: "00" - "59" (zero-filled to two digits)
- `Z`: Literal meaning UTC (equivalent to +0000)

**Inherits:** `Iso8601_type`

**Functions:**

| Signature | Meaning |
|-----------|---------|
| `hour(): Integer` | Extract hour in range 00-14 |
| `minute(): Integer` | Extract minute, usually 0 or 30 |
| `sign(): Integer` | Direction as +1 or -1 |
| `minute_unknown(): Boolean` | True if minute part unknown |
| `is_partial(): Boolean` (effected) | True if minutes missing |
| `is_extended(): Boolean` (effected) | True if uses ':' separator |
| `is_gmt(): Boolean` | True if UTC (+0000) |
| `as_string(): String` | Return value in extended format |

**Invariants:**
- `Min_hour_valid`: If negative, 0 < hour <= 12
- `Max_hour_valid`: If positive, 0 < hour <= 14
- `Minute_valid`: If not unknown, minute validated
- `Sign_valid`: sign = +1 or -1

---

## Terminology Package

### Overview

The `base.foundation_types.terminology` package provides leaf types for representing terminology codes and terms.

An instance of `Terminology_code` references any referenceable entity within a terminology or ontology:
- Single term with rubric(s) and relationships
- Value set (set of terms in tree/structure per relationships)
- Any other referenceable terminological entity

An instance of `Terminology_term` records terminology code and rubric used in operational context, avoiding need for terminology lookup for display.

### Class Definitions

#### Terminology_term Class

Leaf type representing standalone terminology term: term text and code.

**Inherits:** `Any`

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| `concept: Terminology_code` (1..1) | Reference to terminology concept |
| `text: String` (1..1) | Text of term |

#### Terminology_code Class

Primitive type representing standalone reference to terminology concept: terminology identifier, optional version, and code/code string.

**Inherits:** `Any`

**Attributes:**

| Signature | Meaning |
|-----------|---------|
| `terminology_id: String` (1..1) | Archetype environment namespace identifier (e.g., "snomed_ct") |
| `terminology_version: String` (0..1) | Optional version string (date, dotted numeric) |
| `code_string: String` (1..1) | Terminology code or post-coordinated expression |
| `uri: Uri` (0..1) | URI reference for terminology service queries |

---

## Functional Meta-types

### Overview

Meta-types corresponding to functional programming primitives (closures, lambda expressions). Concepts supported in modern programming languages. Types provide formal basis for openEHR specifications defining function-related elements.

Since UML lacks native functional elements, semantics approximated using normal class facilities.

Key abstractions:
- 'Function as a type'
- 'Tuple' enabling argument formalization
- 'Routine' type as function ancestor
- 'Procedure' type for completeness

Tuple type defined as generic meta-type whose descendants may define any number of generic parameters for type lists.

### Class Definitions

#### ROUTINE Class

Type representing function with return type and 0+ arguments as TUPLE.

```
Generic Parameters: ARGS
```

#### FUNCTION Class

Type representing function with return type and 0+ arguments as TUPLE.

**Inherits:** `ROUTINE`

```
Generic Parameters: ARGS, RESULT
```

#### PROCEDURE Class

Type representing procedure with 0+ arguments as TUPLE.

**Inherits:** `ROUTINE`

```
Generic Parameters: ARGS
```

#### TUPLE Class

Parent type of all TUPLE types.

#### TUPLE1 Class

Tuple type for representing single typed argument within Routine signature.

**Inherits:** `TUPLE`

```
Generic Parameters: A
```

#### TUPLE2 Class

Tuple type for representing two typed arguments within Routine signature.

**Inherits:** `TUPLE`

```
Generic Parameters: A, B
```

---

## Type Cross-Reference

Cross-reference of openEHR foundation types to equivalents in common implementation formalisms. Where not listed, specific library may exist or implementation required.

| openEHR Type | Description | XML | Java | C# |
|---|---|---|---|---|
| `Octet` | 8-bit value | - | `Byte` | `Byte` |
| `Character` | 8-bit character-set member | `string` | `Character` | `Char` |
| `Boolean` | True/False values | `boolean` | `Boolean` | `Boolean` |
| `Integer` | 32-bit integers | `decimal` | `Integer` | `Int32` |
| `Integer64` | 64-bit integers | `decimal` | `Long` | `Int64` |
| `Real` | 32-bit real numbers | `float`, `decimal` | `Float` | `Single` |
| `Double` | 64-bit real numbers | `double` | `Double` | `Double` |
| `String` | Unicode strings | `string` | `String` | `String` |
| `Array<T>` | Contiguous array | `sequence` | `Array<T>` | `Array<T>` |
| `List<T>` | Ordered list | `sequence` | `List<T>` | `List<T>` |
| `Set<T>` | Unordered, unique membership | `all` | `Set<T>` | `HashSet<T>` |
| `Hash<K,V>` | Unique-keyed map | (various) | `Map<T>` | `HashTable<T>` |
| `Interval<T:Ordered>` | Interval of ordered types | - | - | - |
| `Date` | Native date type | `date` | `java.util.Date` | `DateTime` |
| `Time` | Native time type | `time` | `java.util.Date` | `DateTime` |
| `Date_time` | Native date/time type | `dateTime` | `java.util.Date` | `DateTime` |
| `Duration` | Native duration type | `duration` | `java.time.Duration` | `TimeSpan` |
| `Iso8601_Date` | ISO 8601 date | `date` | `SimpleDateFormat` / `ISODateTimeFormat` | Formatted string |
| `Iso8601_Time` | ISO 8601 time | `time` | `SimpleDateFormat` / `ISODateTimeFormat` | Formatted string |
| `Iso8601_Date_time` | ISO 8601 date/time | `dateTime` | `SimpleDateFormat` / `ISODateTimeFormat` | Formatted string |
| `Iso8601_Duration` | ISO 8601 duration | `duration` | `SimpleDateFormat` / `ISODateTimeFormat` | Formatted string |
| `Interval<Integer>` | Interval of Integer | - | (various) | - |
| `Interval<Date>` | Interval of Date | - | (various) | - |
| `Interval<Time>` | Interval of Time | - | (various) | - |
| `Interval<DateTime>` | Interval of DateTime | - | (various) | - |

---

**Last updated:** 2021-04-09
**Source:** https://specifications.openehr.org/releases/BASE/latest/foundation_types.html
