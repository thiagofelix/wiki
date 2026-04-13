---
title: Object Data Instance Notation (ODIN)
type: entity
sources:
  - raw/lang-odin.md
created: 2026-04-13
updated: 2026-04-13
---

# Object Data Instance Notation (ODIN)

ODIN (Object Data Instance Notation) is a human-readable, machine-processable data serialization syntax developed by openEHR. Previously known as "dADL" (data ADL), it was extracted from the ADL specification and given its own identity. ODIN is part of the LANG component (Release 1.0.0) and holds STABLE status. It serves as the primary serialization format for [[basic-meta-model]] schemas and appears within [[archetype-definition-language]] files.

## Design Principles

ODIN represents instance data based on object-oriented information models. Its core design goals are:

- Human readability and writability (editable in standard text editors)
- Machine processability
- Minimal assumptions about underlying information models
- Support for relational, object-oriented, or mixed model approaches

Each `<>` block corresponds to an object instance. Names before `=` denote attribute names or container keys. Leaf value types are syntactically inferred. Every node is reachable via a path reference, and dynamically bound types can be explicitly indicated.

## Artefact Types

ODIN texts exist in two physical forms: embedded fragments and standalone documents.

### Embedded Fragment

ODIN fragments appear embedded within other formalisms (such as ADL archetype files). They typically omit object identifiers and schema identifiers, which are inferred from surrounding context:

```
attr_1 = <
    attr_12 = <
        attr_13 = <leaf_value>
    >
>
```

### Document Forms

**Implicit Object Document**: Contains only attribute/value blocks with no outer object wrapper. Commonly used for serializing models, configuration files, and BMM schemas.

**Anonymous Object Document**: Contains a single unnamed object wrapped in outer `<>` delimiters enclosing an ODIN fragment.

**Identified Object Document**: Contains multiple serialized objects, each explicitly identified by a key:

```
["id_1"] = <
    attr_1 = <...>
>
["id_2"] = <
    attr_1 = <...>
>
```

Identifiers may use String, Integer, or Date/Time primitive types.

## Content Structure

The fundamental ODIN pattern is:

```
attribute_name = < value >
```

Each attribute name maps to an information model attribute. Values are either primitive literals or nested attribute/value hierarchies terminating in primitive leaves. Sibling attribute nodes must have unique names (validity rule VDATU).

## Data Types

### Primitive Types

| Type | Syntax | Example |
|------|--------|---------|
| String | Double-quoted | `"this is a string"` |
| Character | Single-quoted | `'a'` |
| Integer | Numeric | `25`, `300000`, `29e6` |
| Real | Decimal point | `25.0`, `3.1415926`, `6.023e23` |
| Boolean | Case-insensitive | `True`, `False` |
| Date | ISO 8601 | `1919-01-23` |
| Time | ISO 8601 | `16:35:04,5` |
| Date_time | ISO 8601 | `2001-05-12T07:35:20+1000` |
| Duration | ISO 8601 P-prefix | `P22DT4H15M0S` |
| URI | Standard web syntax | `http://openEHR.org/home` |
| Coded term | `[terminology::code]` | `[snomed_ct::2004950]` |

Strings support multi-line content, UTF-8 encoding, and standard escape sequences (`\r`, `\n`, `\t`, `\\`, `\"`).

### Partial Dates and Times

ODIN supports two partial date/time methods:

1. **ISO 8601 incomplete formats**: `yyyy-MM` (no day), `hh:mm` (no seconds)
2. **ISO 8601 variant with `?`**: `yyyy-MM-??` (unknown day), `hh:mm:??` (unknown seconds)

### Intervals

Intervals of ordered primitives use pipe-delimited syntax:

```
|0..5|            -- two-sided: 0 <= x <= 5
|>0..5|           -- left-open: 0 < x <= 5
|0..<5|           -- right-open: 0 <= x < 5
|<10|             -- one-sided: x < 10
|>=0|             -- one-sided: x >= 0
|5.0 +/-0.5|     -- symmetric: 4.5 to 5.5
```

Works for Integer, Real, Date, Time, Date_time, and Duration types.

### Lists

Primitive values appear as comma-separated lists of identical type:

```
"cyan", "magenta", "yellow", "black"
1, 1, 2, 3, 5
08:02, 08:35, 09:10
```

Single-datum lists use a continuation marker: `"en", ...`

## Container Objects

Container-typed attributes (`List<Type>`, `Set<Type>`, `Hash<K, V>`) use bracketed keys for non-primitive members:

```
people = <
    [1] = <name = <...> birth_date = <...>>
    [2] = <name = <...> birth_date = <...>>
>
```

Keys may be integers, strings, or dates:

```
subjects = <
    ["philosophy:plato"] = <
        name = <"philosophy">
        teacher = <"plato">
        topics = <"meta-physics", "natural science">
    >
>
```

Nested containers (`List<List<T>>`) follow the same pattern with additional bracketed levels:

```
list_of_string_lists = <
    [1] = <
        [1] = <"first string in first list">
        [2] = <"second string in first list">
    >
>
```

Sibling objects within containers must have unique identifiers (validity rule VDOBU).

## Type Markers

When subtype polymorphism or explicit typing is needed, type markers appear in parentheses after the `=` sign, using C-style cast syntax:

```
destinations = <
    ["seville"] = (TOURIST_DESTINATION) <
        profile = (DESTINATION_PROFILE) <...>
        hotels = <
            ["gran sevilla"] = (HISTORIC_HOTEL) <...>
            ["sofitel"] = (LUXURY_HOTEL) <...>
        >
    >
>
```

Generic types use angle brackets: `(List<HOTEL>) <...>`. Namespaced type names use period-separated package paths: `org.openehr.rm.ehr.content.ENTRY`.

## Paths

ODIN structures generate extractable paths by concatenating attribute names and container keys:

```
/attr_1/attr_2/attr_3           -- path to leaf
/school_schedule/locations[1]   -- container element by index
/school_schedule/subjects["philosophy:kant"]  -- by string key
/list_of_lists[1]/[2]           -- nested container path
```

Path syntax is a semantic subset of W3C XPath with syntactic shortcuts. ODIN assumes no XML attribute/children distinction -- all subparts reference as XPath children.

## Shared Object References

ODIN supports associations between objects through path references:

```
bookings = <
    ["seville:0134"] = <
        hotel = </hotels["sofitel"]>  -- reference by path
    >
>
hotels = <
    ["sofitel"] = (LUXURY_HOTEL) <...>
>
```

Cross-object references include object identifiers in paths. Cross-document references use URIs.

## Plug-in Syntaxes

ODIN allows expressing value blocks in alternative syntaxes using a named plug-in syntax type with modified delimiters `<# #>`:

```
definition = (cadl) <#
    ENTRY[at0000] matches {
        name matches { ... }
    }
#>
```

This mechanism enables embedding cADL (constraint ADL) within archetype files that are themselves ODIN documents.

## Comparison with Other Formats

### vs. XML

ODIN differs from XML in several key ways:

- **Comprehensive primitive types**: Numeric intervals, date/time intervals, all-primitive-type lists are built in
- **Pure object semantics**: No confusing attribute/element distinction for object properties
- **Container type support**: Proper `List<T>`, `Set<T>`, `Hash<K,V>` semantics
- **Space efficiency**: Approximately half the size of equivalent XML
- **Human readability**: Designed for human writing and reading, not just machine processing

ODIN documents convert straightforwardly to XML. In the XML mapping, container attributes become repeated elements with `id` attributes, and ODIN type markers map to XML `type` attributes.

### vs. JSON

JSON has fewer primitive types than ODIN -- lacking date/time types and intervals. Date/time values typically map to ISO 8601 strings. ODIN's optional type markers have no JSON equivalent and require structural conversion.

## File Encoding

ODIN files use UTF-8 Unicode encoding. Non-ASCII characters outside code-point 127 may use `\uHHHH` (4-hex-digit) or `\uHHHHHHHH` (8-hex-digit) escaped UTF-16. ODIN has no reserved keywords; all identifiers derive from information models.

Comments use the `--` indicator (double dash). Semi-colons are optional separators for single-line blocks.

## Use in BMM and ADL

ODIN is the default serialization format for [[basic-meta-model]] schemas. BMM `.bmm` files are ODIN serializations of `P_BMM_*` class instances, containing schema headers, inclusion declarations, package definitions, and class definitions with typed property blocks.

In [[archetype-definition-language]] files, ODIN sections encode the `language`, `description`, `terminology`, and `annotations` sections. The `definition` section uses cADL via the plug-in syntax mechanism. ODIN is also used in the [[base-component]] for configuration and resource description serialization.
