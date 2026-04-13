# Object Data Instance Notation (ODIN)

**Status:** STABLE
**Release:** LANG Release-1.0.0
**Revision:** Latest Issue
**Date:** Latest Issue Date
**Keywords:** data, notation, JSON, syntax

---

## Document Information

**Issuer:** openEHR Specification Program

**Copyright:** © 2003 - 2021 The openEHR Foundation

**License:** Creative Commons Attribution-NoDerivs 3.0 Unported
https://creativecommons.org/licenses/by-nd/3.0/

**Support:**
- Issues: Problem Reports
- Web: specifications.openEHR.org

---

## Table of Contents

1. [Preface](#preface)
2. [Overview](#overview)
3. [Basics](#basics)
4. [ODIN Artefacts](#odin-artefacts)
5. [Content](#content)
6. [References](#references)
7. [Leaf Data](#leaf-data)
8. [Path Syntax](#path-syntax)
9. [Plug-in Syntaxes](#plug-in-syntaxes)
10. [Appendix A: Relationship with Other Syntaxes](#appendix-a)
11. [Appendix B: Syntax Specification](#appendix-b)

---

## Amendment Record

| Issue | Details | Raiser | Completed |
|-------|---------|--------|-----------|
| **LANG Release 1.0.0** | 1.5.2 | SPECLANG-7: Move IDON spec to LANG component | openEHR SEC | 11 Nov 2018 |
| | 1.5.1 | SPECLANG-3, SPECLANG-4, SPECLANG-5: Grammar updates for ranges, keys, ISO 8601 variant | K Allen, T Beale, S Garde | 29 Aug 2018 |
| | 1.5.0 | SPECLANG-6: Correct minor comment errors in section 7 | C Nanjo | 08 Apr 2016 |
| **BASE Release 1.0.3** | 1.5.1 | Separate from ADL spec and rename to ODIN | T Beale | 15 Apr 2013 |
| | 1.5.0 | Add fractional seconds to dADL grammar | T Beale | 15 Aug 2012 |
| **Release 1.0.2** | 1.4.1 | SPEC-268: Correct missing parentheses in dADL type identifiers | R Chen | 12 Dec 2008 |
| **Release 1.0.1** | 1.4.0 | SPEC-213, SPEC-216: Include 'T' in date/time values; ISO 8601 Duration | T Beale, S Heard | 13 Mar 2007 |
| **Release 1.0** | 1.3.0 | SPEC-143: Add partial date/time values to dADL syntax | S Heard | 18 Jun 2005 |
| | | SPEC-149: Add URIs to dADL and remove query() syntax | T Beale | |
| **Release 0.95** | 1.2 | SPEC-110: Added explanatory material; domain type support; rewrote sections | T Beale | 15 Nov 2004 |
| **Release 0.9** | 0.9.9 | SPEC-75: Added dADL object model | T Beale | 28 Dec 2003 |

---

## Acknowledgements

### Primary Author

**Thomas Beale** - Ars Semantica; openEHR Foundation Management Board (previously Ocean Informatics UK)

### Contributors

- Kurt W. Allen, Applicadia Inc, Minnesota, USA
- Rong Chen, MD, PhD, Cambio Healthcare Systems, Sweden
- Sam Heard, MD, DRCOG, MRCGP, FRACGP, Director at Ocean Informatics, Australia
- Claude Nanjo, MA African Studies, M Public Health, Cognitive Medical Systems Inc., California, USA

### Supporters

- University College London - Centre for Health Informatics and Multi-professional Education (CHIME)
- Ocean Informatics

Special acknowledgment to David Ingram, Emeritus Professor of Health Informatics at UCL.

### Trademarks

- 'openEHR' is a trademark of the openEHR Foundation
- 'Java' is a registered trademark of Oracle Corporation
- 'Microsoft' and '.Net' are trademarks of the Microsoft Corporation

---

## Preface

### Purpose

This specification describes the Object Data Instance Notation (ODIN) syntax, previously known as 'dADL' from openEHR ADL specifications. It targets software developers, technically-oriented domain specialists, and subject matter experts. ODIN functions as both human-readable and computer-processible data representation syntax, supporting standard text editor editing.

### Nomenclature

Throughout this document, "attribute" denotes any stored property of a type in an object model, including primitive attributes and relationships such as associations or aggregations. When XML is mentioned, XML 'attributes' are explicitly designated.

### Status

This specification maintains STABLE status. Development versions are available at:
https://specifications.openehr.org/releases/LANG/Release-1.0.0/odin.html

### Feedback

Community feedback may be submitted via the openEHR languages specifications forum:
https://discourse.openehr.org/c/specifications/bmm-el

Issues can be raised on the specifications Problem Report tracker:
https://specifications.openehr.org/components/LANG/open_issues

Historical change records are available at:
https://specifications.openehr.org/components/LANG/history

### Conformance

Data or software artifact conformance to openEHR specifications is determined through formal testing against relevant Implementation Technology Specifications (ITSs), such as IDL interfaces or XML schemas. Since ITSs derive formally from underlying models, ITS conformance indicates model conformance.

---

## Overview

ODIN provides formal syntax for expressing instance data based on object-oriented or relational information models. The notation is readable by both humans and machines. Consider this example:

```
person = (List<PERSON>) <
    [01234] = <
        name = <
            forenames = <"Sherlock">
            family_name = <"Holmes">
            salutation = <"Mr">
        >
        address = <
            habitation_number = <"221B">
            street_name = <"Baker St">
            city = <"London">
            country = <"England">
        >
    >
    [01235] = < -- etc >
>
```

The design principle emphasizes representing data as both machine-processible and human-readable while making minimal assumptions about underlying information models. Type names remain optional; attribute names and values typically appear explicitly. The notation accommodates relational, object-oriented, or mixed model approaches.

ODIN exhibits several advantageous characteristics:

- Each `<>` block corresponds to an object instance
- Names before '=' denote attribute names or container keys
- Leaf value types are syntactically inferred
- Paths navigate the tree structure by concatenating attribute names and container keys
- Every node is reachable via path reference
- Dynamically bound types are explicitly indicated
- Shared objects may be referenced by path

---

## Basics

### File Encoding

ODIN files utilize UTF-8 Unicode encoding to accommodate characters from any language, enabling multi-language usage including software translation files.

Files encoded in Latin-1 (ISO-8859-1) or ISO-8859 variants may function acceptably under certain conditions:

- Content contains only ASCII (unicode code-points 0-127)
- Operating system performs automatic UTF-8 conversion
- Tools support multiple encoding variants

For non-UTF-8 environments, ASCII encoding of unicode characters outside code-point 127 should employ `\u` escaped UTF-16:

- `\uHHHH` - 4 hex digits for unicode code-points U+0000 through U+FFFF
- `\uHHHHHHHH` - 8 hex digits for code-points U+10000 through U+10FFFF (per IETF RFC 2781)

While native UTF-8 is the officially designated encoding and recommended approach, tools may optionally support alternative encodings. UTF-8 support remains the minimum requirement for ODIN-compliant processors.

**URI Handling:** All URI characters outside the 'unreserved set' per IETF RFC 3986 require percent-encoding. The unreserved set comprises:

```
ALPHA | DIGIT | '-' | '.' | '_' | '~'
```

### Special Character Sequences

String and character data may employ the following quoted forms:

- `\r` - carriage return
- `\n` - linefeed
- `\t` - tab
- `\\` - backslash
- `\"` - literal double quote within String values
- `\'` - literal single quote within Character values

Any other backslash combination is illegal. Literal backslashes must use `\\` exclusively.

Multi-line strings and paragraphs commonly require only `\\` and `\"`. Parsers should support the complete list to accommodate author preferences and text editor variations.

### Keywords

ODIN contains no reserved keywords; all identifiers derive from information models.

### Reserved Characters

The following characters have specific meanings in ODIN:

- `<` - open object block
- `>` - close object block
- `=` - indicate attribute value assignment
- `(`, `)` - type name or plug-in syntax delimiters
- `<#` - open plug-in syntax block
- `#>` - close plug-in syntax block

Within `<>` delimiters, additional characters indicate primitive values:

- `"` - delimit string values
- `'` - delimit single character values
- `|` - delimit intervals
- `[]` - delimit coded terms

### Comments

Comments use the `--` indicator. Multi-line comments repeat `--` on each continuing line.

Example:
```
name = <"John"> -- person's given name
-- This is a multi-line comment
-- extending across multiple lines
```

### Information Model Identifiers

Two identifier categories exist: **type names** and **attribute names**.

**Type names** begin with uppercase letters followed by alphanumeric characters and underscores. Generic type names additionally permit commas and angle brackets, maintaining UML syntactical correctness.

**Attribute names** begin with lowercase letters followed by alphanumeric characters and underscores.

Common naming conventions include:

1. **Uppercase convention:**
   - Type names in uppercase: `PERSON`, `ADDRESS`
   - Built-in types in mixed case: `Integer`, `String`, `List<T>`
   - Attribute names in lowercase: `home_address`, `date_of_birth`

2. **Camelcase convention:**
   - Type names: `Person`, `Address`
   - Attribute names: `homeAddress`, `dateOfBirth`

Underscores represent word breaks. Convention selection should reflect the underlying information model's conventions.

### Semi-colons

Semi-colons separate ODIN blocks on single lines but carry no semantic significance:

```
term = <text = <"plan">; description = <"The clinician's advice">>
```

is equivalent to:

```
term = <
    text = <"plan">
    description = <"The clinician's advice">
>
```

Semi-colons remain entirely optional.

---

## ODIN Artefacts

ODIN texts exist in two physical forms: embedded fragments and documents. Both follow the general structure:

```
odin_text = (schema_identifier)? main_text
schema_identifier = '@' schema '=' URI
```

The optional schema identifier indicates the schema version on which the ODIN text is based. When schema is known a priori or inferrable from context, omission is appropriate.

### Embedded Fragment

ODIN fragments appear embedded within other formalisms and typically omit object identifiers and schema identifiers, inferred from surrounding context:

```
--
-- ODIN Embedded Fragment
--
attr_1 = <
    attr_12 = <
        attr_13 = <leaf_value>
    >
>
attr_2 = <
    attr_22 = <leaf_value>
>
```

### Document

ODIN documents represent standalone artefacts containing serialised objects in various forms.

#### Implicit Object Document

Documents containing only embedded fragments represent "implicit" object documents, where contents consist of various object property values. This degenerate form of anonymous object documents is commonly used for serialising models, configuration files, and schemas. Filenames and content typically identify the artefact sufficiently.

#### Anonymous Object Document

Anonymous object documents contain one object per document, identified by no identifier, consisting of outer `<>` delimiters enclosing an ODIN embedded fragment:

```
--
-- ODIN Anonymous Object Document
--
<
    attr_1 = <
        attr_12 = <
            attr_13 = <leaf_value>
        >
    >
    attr_2 = <
        attr_22 = <leaf_value>
    >
>
```

#### Identified Object Document

Identified object documents represent multiple serialised objects, each explicitly identified:

```
--
-- ODIN Identified Object Document
--
["id_1"] = <
    attr_1 = <
        attr_12 = <
            attr_13 = <leaf_value>
        >
    >
>

["id_2"] = <
    attr_1 = <
        attr_12 = <
            attr_13 = <leaf_value>
        >
    >
>

["id_N"] = <
    attr_1 = <
        attr_12 = <
            attr_13 = <leaf_value>
        >
    >
>
```

Identifiers may employ String, Integer, or Date/Time primitive types. Strings are most common:

```
["aaa"] = <...>
["bbb"] = <...>
["ccc"] = <...>
```

These documents typically represent serialised in-memory instance networks or object dumps.

---

## Content

### General Structure

ODIN object instances (implied, anonymous, or identified) consist of attribute names and object values hierarchically organized. The fundamental pattern:

```
object = attribute_name '=' '<' value '>'
```

Each attribute name represents an information model attribute. Each "value" is either a primitive type literal value or further nested attributes and values, terminating in primitive leaf nodes. Sibling attribute nodes must be uniquely named.

Example structure:

```
attr_1 = <
    attr_2 = <
        attr_3 = <leaf_value>
        attr_4 = <leaf_value>
    >
    attr_5 = <
        attr_3 = <
            attr_6 = <leaf_value>
        >
        attr_7 = <leaf_value>
    >
>
attr_8 = <...>
```

Each `<>` pair encloses a type instance. The hierarchy represents composition and aggregation relationships (part-of connections). Associations between instances are representable through references.

**Validity Rule:**

**VDATU:** Sibling attributes within an object node must possess unique names, consistent with class definitions in information models.

### Paths

ODIN structures generate extractable paths corresponding to tree structure:

```
/attr_1
/attr_1/attr_2
/attr_1/attr_2/attr_3           -- path to leaf value
/attr_1/attr_2/attr_4           -- path to leaf value
/attr_1/attr_5
/attr_1/attr_5/attr_3
/attr_1/attr_5/attr_3/attr_6    -- path to leaf value
/attr_1/attr_5/attr_7           -- path to leaf value
/attr_8
```

Path syntax maps trivially to W3C Xpath and Xquery paths (detailed in [Path Syntax](#path-syntax)).

### Void Objects

Void objects (attributes with no value) are permitted but ignored by parsers. Output is legal but not recommended:

```
address = <...>    -- person's address
```

### Container Objects

Container type attributes (`List<Type>`, `Set<Type>`, `Hash<KeyType, ValueType>`) support two expression approaches.

**Leaf values** use manifest list syntax:

```
fruits = <"pear", "cumquat", "peach">
some_primes = <1, 2, 3, 5>
```

**Non-primitive container values** employ container member keys--array-style syntax without explicit attribute names. Primitive comparable values serve as keys rather than exclusively integers:

```
people = <
    [1] = <name = <...> birth_date = <...> interests = <...> >
    [2] = <name = <...> birth_date = <...> interests = <...> >
    [3] = <name = <...> birth_date = <...> interests = <...> >
>
```

String and date keys are also supported:

```
people = <
    ["akmal:1975-04-22"] = <name = <...> birth_date = <...> interests = <...> >
    ["akmal:1962-02-11"] = <name = <...> birth_date = <...> interests = <...> >
    ["gianni:1978-11-30"] = <name = <...> birth_date = <...> interests = <...> >
>
```

Key values follow primitive type syntax. Complex data becomes readable:

```
school_schedule = <
    lesson_times = <08:30:00, 09:30:00, 10:30:00>

    locations = <
        [1] = <"under the big plane tree">
        [2] = <"under the north arch">
        [3] = <"in a garden">
    >

    subjects = <
        ["philosophy:plato"] = <
            name = <"philosophy">
            teacher = <"plato">
            topics = <"meta-physics", "natural science">
            weighting = <76%>
        >
        ["philosophy:kant"] = <
            name = <"philosophy">
            teacher = <"kant">
            topics = <"meaning and reason", "meta-physics", "ethics">
            weighting = <80%>
        >
        ["art"] = <
            name = <"art">
            teacher = <"goya">
            topics = <"technique", "portraiture", "satire">
            weighting = <78%>
        >
    >
>
```

This structure corresponds to the type specification:

```
class SCHEDULE
    lesson_times: List<Time>
    locations: List<String>
    subjects: List<SUBJECT>
end

class SUBJECT
    name: String
    teacher: String
    topics: List<String>
    weighting: Real
end
```

**Validity Rule:**

**VDOBU:** Sibling objects within container attributes must possess unique identifiers.

Container paths include bracketed keys:

```
/school_schedule/locations[1]
/school_schedule/subjects["philosophy:kant"]
```

### Nested Container Objects

Nested container types (`List<List<Message>>`, `Hash<List<Integer>, String>`) follow straightforward syntax extension:

```
list_of_string_lists = <
    [1] = <
        [1] = <"first string in first list">
        [2] = <"second string in first list">
    >
    [2] = <
        [1] = <"first string in second list">
        [2] = <"second string in second list">
        [3] = <"third string in second list">
    >
    [3] = <
        [1] = <"only string in third list">
    >
>
```

Paths become:

```
/list_of_string_lists[1]/[1]
/list_of_string_lists[1]/[2]
/list_of_string_lists[2]/[1]
```

### Adding Type Information

Simple, regular structures benefit from minimal model information. Complex data (aircraft design databases, health records) often requires explicit type information, particularly when sub-objects employ subtypes of statically declared model types (dynamic binding).

Type information is indicated using C-language casting operator syntax--type names in parentheses after '=' signs:

```
destinations = <
    ["seville"] = (TOURIST_DESTINATION) <
        profile = (DESTINATION_PROFILE) <...>
        hotels = <
            ["gran sevilla"] = (HISTORIC_HOTEL) <...>
            ["sofitel"] = (LUXURY_HOTEL) <...>
            ["hotel real"] = (PENSION) <...>
        >
        attractions = <
            ["la corrida"] = (SPORT_VENUE) <...>
            ["Alcazar"] = (HISTORIC_SITE) <...>
        >
    >
>
```

Generic template types use standard UML angle bracket syntax:

```
hotels = (List<HOTEL>) <
    ["gran sevilla"] = (HISTORIC_HOTEL) <...>
>
```

Namespaced type names prepend package names separated by periods:

```
org.openehr.rm.ehr.content.ENTRY
Core.Abstractions.Relationships.Relationship
```

---

## References

### Associations and Shared Objects

Reliable paths enable representation of single business objects (aggregation/composition hierarchies) and associations between objects, including shared object references.

#### Within An Object

Hotel objects may be shared by association:

```
destinations = <
    ["seville"] = <
        hotels = <
            ["gran sevilla"] = </hotels["gran sevilla"]>
            ["sofitel"] = </hotels["sofitel"]>
            ["hotel real"] = </hotels["hotel real"]>
        >
    >
>

bookings = <
    ["seville:0134"] = <
        customer_id = <"0134">
        period = <...>
        hotel = </hotels["sofitel"]>
    >
>

hotels = <
    ["gran sevilla"] = (HISTORIC_HOTEL) <...>
    ["sofitel"] = (LUXURY_HOTEL) <...>
    ["hotel real"] = (PENSION) <...>
>
```

Associations employ fully qualified paths as attribute data. Type declarations occur in relevant object declarations; type declarations may precede path references when association types are ancestor types.

#### Across Objects

Identified object documents with cross-object references include object identifiers in reference paths:

```
["travel_db_0293822"] = <
    destinations = <
        ["seville"] = <
            hotels = <
                ["gran sevilla"] = <["tourism_db_13"]/hotels["gran sevilla"]>
                ["sofitel"] = <["tourism_db_13"]/hotels["sofitel"]>
                ["hotel real"] = <["tourism_db_13"]/hotels["hotel real"]>
            >
        >
    >

    bookings = <
        ["seville:0134"] = <
            customer_id = <"0134">
            period = <...>
            hotel = <["tourism_db_13"]/hotels["sofitel"]>
        >
    >
>

["tourism_db_13"] = <
    hotels = <
        ["gran sevilla"] = (HISTORIC_HOTEL) <...>
        ["sofitel"] = (LUXURY_HOTEL) <...>
        ["hotel real"] = (PENSION) <...>
    >
>
```

#### Across ODIN Documents

Other ODIN documents are referenced via URIs containing reference paths:

```
external_reference = </uri/to/document/path/to/node>
```

---

## Leaf Data

ODIN data ultimately resolves to primitive type instances: `String`, `Integer`, `Real`, `Double`, `Character`, date/time types, lists, intervals, and specialized types. Manifest values appear directly within leaf angle brackets:

```
some_attribute = <manifest_value>
```

### Primitive Types

#### Character Data

Characters appear in single quotes:

```
'a'
```

Characters outside ASCII (0-127) must be UTF-8 encoded with supported backslash escapes per [File Encoding](#file-encoding) section.

#### String Data

Strings enclose in double quotes:

```
"this is a string"
```

ISO/IEC 10646 code encoding:

```
"this is a much longer string, what one might call a &quot;phrase&quot;."
```

Multi-line strings include returns naturally:

```
text = <"And now the STORM-BLAST came, and he
        Was tyrannous and strong :
        He struck with his o'ertaking wings,
        And chased us south along.">
```

Strings accommodate nearly any formalism content. Characters outside ASCII (0-127) require UTF-8 encoding or supported escapes.

#### Integer Data

Integers are represented as numbers:

```
25
300000
29e6
```

Commas or periods for long number formatting are disallowed due to list item comma usage conflicts.

#### Real Data

Real numbers employ decimal point notation:

```
25.0
3.1415926
6.023e23
```

Periods only separate decimal portions; European comma usage conflicts with list comma separation.

#### Boolean Data

Boolean values employ case-insensitive indicators:

```
True
False
```

#### Dates and Times

##### Complete Date/Times

Full dates, times, and durations employ ISO 8601 subset syntax. Extended form only (':' and '-' required). Single year numbers and hour-only times are unsupported as ambiguous. See [Partial Date/Times](#partial-datetimes) for partial forms.

Durations employ 'P'-prefixed strings with period designators:
- 'Y' - years
- 'M' - months
- 'W' - weeks
- 'D' - days
- 'H' - hours
- 'M' - minutes
- 'S' - seconds

Literal 'T' separates YMWD from HMS components:

```
1919-01-23                 -- birthdate of Django Reinhardt
16:35:04,5                 -- rise of Venus in Sydney on 24 Jul 2003
2001-05-12T07:35:20+1000   -- timestamp on an email received from Australia
P22DT4H15M0S               -- period of 22 days, 4 hours, 15 minutes
```

##### Partial Date/Times

Two partial date/time expression methods exist:

1. **ISO 8601 incomplete formats** (extended form with '-' and ':' separators):

```
yyyy-MM            -- date with no days
hh:mm              -- time with no seconds
yyyy-MM-ddThh:mm   -- date/time with no seconds
yyyy-MM-ddThh      -- date/time, no minutes or seconds
```

2. **ISO 8601 variant with '?' character** substitution for missing digits:

Partial dates:
```
yyyy-MM-??         -- date with unknown day in month
yyyy-??-??         -- date with unknown month and day
```

Partial times:
```
hh:mm:??           -- time with unknown seconds
hh:??:??           -- time with unknown minutes and seconds
```

Partial date/times:
```
yyyy-MM-ddThh:mm:??     -- date/time with unknown seconds
yyyy-MM-ddThh:??:??     -- date/time with unknown minutes and seconds
```

### Intervals of Ordered Primitive Types

Intervals of ordered primitive types (Integer, Real, Date, Time, Date_time, Duration) employ uniform syntax:

```
|N..M|        -- two-sided range N >= x <= M
|>N..M|       -- two-sided range N > x <= M
|N..<M|       -- two-sided range N <= x < M
|>N..<M|      -- two-sided range N > x < M
|<N|          -- one-sided range x < N
|>N|          -- one-sided range x > N
|>=N|         -- one-sided range x >= N
|<=N|         -- one-sided range x <= N
|N +/-M|      -- interval of N +/-M
|N+/-M|       -- interval of N +/-M
```

Examples:

```
|0..5|              -- integer interval
|0.0..1000.0|       -- real interval
|0.0..<1000.0|      -- real interval 0.0 <= x < 1000.0
|08:02..09:10|      -- interval of time
|>=1939-02-01|      -- open-ended interval of dates
|5.0 +/-0.5|        -- 4.5 +/-5.5
|5.0 +/-0.5|        -- 4.5 +/-5.5
|>=0|               -- >= 0
```

### Other Built-in Types

#### URIs

URIs follow standard web syntax per IETF RFC3986:

```
http://openEHR.org/home
ftp://get.this.file.com?file=cats.doc#section_5
http://www.mozilla.org/products/firefox/upgrade/?application=thunderbird
```

Special character encoding follows IETF RFC 3986 per [File Encoding](#file-encoding).

#### Coded Terms

Coded terms employ structure: terminology identifier plus code. String representation:

```
[terminology_id::code]
```

where `terminology_id` is alphanumeric with optional parenthetical version, and `code` is a string.

Clinical examples:

```
[icd10AM::F60.1]            -- from ICD10AM
[snomed_ct::2004950]        -- from snomed-ct
[snomed_ct(3.1)::2004950]   -- from snomed-ct v 3.1
```

### Lists of Built-in Types

Primitive type data appear singly or as comma-separated lists of identical type:

```
"cyan", "magenta", "yellow", "black"    -- printer's colours
1, 1, 2, 3, 5                           -- first 5 fibonacci numbers
08:02, 08:35, 09:10                     -- set of train times
```

Single-datum lists employ comma and continuation marker:

```
"en", ...       -- languages
"icd10", ...    -- terminologies
[at0200], ...
```

Whitespace is optional:

```
1,1,2,3
```

is identical to:

```
1, 1, 2, 3
```

---

## Path Syntax

### Semantics

ODIN path syntax format:

```
path            = ['/'] path_segment { '/' path_segment }
path_segment    = attr_name [ '[' object_id ']' ]
```

ODIN paths consist of segments separated by slashes ('/'), each segment being an attribute name with optional object identifier predicate in brackets ('[]').

Paths are **absolute** (commencing with initial '/') or **relative**.

Typical ODIN path example:

```
/term_definitions["en"]/items["at0001"]/text
```

### Relationship with W3C Xpath

ODIN path syntax represents a semantic Xpath subset with syntactic shortcuts reducing common-case verbosity. Xpath differentiates "children" from "attributes" due to XML element/attribute distinction. ODIN, employing pure object formalism, shows no such distinction--all subparts reference as Xpath children. The `child::` abbreviated syntax key is unnecessary.

ODIN assumes no attribute/children distinction, assuming `node_id` attribute. Legal expressions:

```
items[1]            -- first member of 'items'
items["systolic"]   -- member with meaning 'systolic'
items["at0001"]     -- member with node id 'at0001'
```

Xpath equivalents:

```
items[1]
items[@key = 'systolic']
items[@archetype_node_id = 'at0001']
```

---

## Plug-in Syntaxes

ODIN enables expressing any object structure. Certain requirements necessitate expressing structure parts in abstract syntax rather than literal serialised object form. Plug-in syntaxes allow value expression (between `<>` delimiters) in alternative syntaxes.

Plug-in syntax indication employs syntax type in parentheses before the block. For plug-in sections, `<>` delimiters modify to `<# #>` for parser design convenience and human readability:

```
attr_name = (syntax) <#
...
#>
```

cADL plug-in example in archetype (itself an ODIN document):

```
definition = (cadl) <#
    ENTRY[at0000] matches { -- blood pressure measurement
        name matches { -- any synonym of BP
            CODED_TEXT matches {
                code matches {
                    CODE_PHRASE matches {[ac0001]}
                }
            }
        }
    }
#>
```

Many plug-in syntaxes may future usage; ODIN parser support is not guaranteed. Parsing employs plug-in parsers--obtaining alternative syntax parsers integrated into existing framework.

---

## Appendix A: Relationship with Other Syntaxes

### XML

Common questioning addresses ODIN necessity given XML's existence. This reveals widespread XML misconception--that textual readability implies human-target design. XML is machine-processing-oriented, with textuality guaranteeing interoperability rather than readability. Realistic XML examples (XML-schema instances, OWL-RDF ontologies) typically lack human readability. ODIN designs for human writing and reading while remaining machine-processible; it functions as abstract syntax for object-oriented data.

ODIN differs from XML by:

- Providing comprehensive primitive data types including numeric and date/time intervals and all-primitive-type lists
- Adhering to object-oriented semantics, particularly container types, where XML schema languages generally fall short
- Avoiding XML's confusing 'attributes' and 'elements' distinction for object properties
- Requiring approximately half XML's equivalent space

ODIN documents convert straightforwardly to XML.

#### Expression of ODIN in XML

ODIN maps relatively easily to XML instance. XML developers frequently develop different object-oriented data mappings due to XML's systematic object-oriented semantics absence. List and set containers (`employees: List<Person>`) often map to invented tags like 'employee'. This mapping design faithfully reflects object-oriented data semantics, avoiding visual XML aesthetics considerations. Xpath expressions remain identical for ODIN and XML, aligning with underlying object model expectations.

Main mapping elements:

##### Single Attributes

Single attribute nodes map to similarly-named tagged nodes.

##### Container Attributes

Container attribute nodes map to same-named tagged node series, each with XML 'id' attribute set to ODIN key:

ODIN:
```
subjects = <
    ["philosophy:plato"] = <
        name = <"philosophy">
    >
    ["philosophy:kant"] = <
        name = <"philosophy">
    >
>
```

XML:
```xml
<subjects id="philosophy:plato">
    <name>philosophy</name>
</subjects>
<subjects id="philosophy:kant">
    <name>philosophy</name>
</subjects>
```

Path `subjects[@id='philosophy:plato']/name` navigates identically in ODIN and XML.

##### Nested Container Attributes

Nested container attribute nodes map to same-named tagged node series, each with 'id' attribute set to ODIN key. For `countries:Hash<Hash<Hotel,String>,String>` signature:

ODIN:
```
countries = <
    ["spain"] = <
        ["hotels"] = <...>
        ["attractions"] = <...>
    >
    ["egypt"] = <
        ["hotels"] = <...>
        ["attractions"] = <...>
    >
>
```

XML (employing synthesised `_items` tag and `key` attribute):
```xml
<countries key="spain">
    <_items key="hotels">
        ...
    </_items>
    <_items key="attractions">
        ...
    </_items>
</countries>

<countries key="egypt">
    <_items key="hotels">
        ...
    </_items>
    <_items key="attractions">
        ...
    </_items>
</countries>
```

ODIN path `countries["spain"]/["hotels"]` transforms to Xpath `countries[@key="spain"]/_items[@key="hotels"]`.

##### Type Names

Type names map to XML 'type' attributes:

ODIN:
```
destinations = <
    ["seville"] = (TOURIST_DESTINATION) <
        profile = (DESTINATION_PROFILE) <...>
        hotels = <
            ["gran sevilla"] = (HISTORIC_HOTEL) <...>
        >
    >
>
```

XML:
```xml
<destinations id="seville" rm:type="TOURIST_DESTINATION">
    <profile rm:type="DESTINATION_PROFILE">
        ...
    </profile>
    <hotels id="gran sevilla" rm:type="HISTORIC_HOTEL">
        ...
    </hotels>
</destinations>
```

### JSON

JavaScript Object Notation (JSON) designs for JavaScript data object representation in language-independent manner, primarily web and JavaScript use. Contemporary usage increasingly applies to complex data representation, including REST web services.

#### Leaf Types

ODIN possesses more primitive types than JSON, including date/time and Interval types.

Date/time types typically map to/from Strings containing ISO 8601 syntax dates/times.

Interval is a built-in ODIN type requiring explicit JSON structure expansion, using the recommended model:

```
class Interval <T: Ordered> {
    T lower
    T upper
    Boolean lower_included
    Boolean upper_included
}
```

#### Typing

ODIN supports optional type markers unavailable in JSON. Conversion situations require explicit structure conversion.

---

## Appendix B: Syntax Specification

### ODIN Grammar (ANTLR4)

```antlr
grammar odin;
import odin_values;

odin_text :
      attr_vals
    | object_value_block
    | keyed_object+
    | included_other_language
    ;

attr_vals : ( attr_val ';'? )+ ;

attr_val : attribute_id '=' object_block ;

object_block :
      object_value_block
    | object_reference_block
    ;

object_value_block : ( '(' type_id ')' )? '<' ( primitive_object | attr_vals? | keyed_object* ) '>' | EMBEDDED_URI;

keyed_object : '[' primitive_value ']' '=' object_block ;

included_other_language: INCLUDED_LANGUAGE_FRAGMENT;

primitive_object :
      primitive_value
    | primitive_list_value
    | primitive_interval_value
    ;

primitive_value :
      string_value
    | integer_value
    | real_value
    | boolean_value
    | character_value
    | term_code_value
    | date_value
    | time_value
    | date_time_value
    | duration_value
    ;

primitive_list_value :  primitive_value ( ( ',' primitive_value )+ | ',' SYM_LIST_CONTINUE ) ;

primitive_interval_value :
      integer_interval_value
    | real_interval_value
    | date_interval_value
    | time_interval_value
    | date_time_interval_value
    | duration_interval_value
    ;

object_reference_block : '<' odin_path_list '>' ;

odin_path_list     : odin_path ( ( ',' odin_path )+ | SYM_LIST_CONTINUE )? ;
odin_path          : '/' | ADL_PATH ;
```

### ODIN Values Grammar (ANTLR4)

```antlr
grammar odin_values;
import base_patterns;

string_value : STRING ;
string_list_value : string_value ( ( ',' string_value )+ | ',' SYM_LIST_CONTINUE ) ;

integer_value : ( '+' | '-' )? INTEGER ;
integer_list_value : integer_value ( ( ',' integer_value )+ | ',' SYM_LIST_CONTINUE ) ;
integer_interval_value :
      '|' SYM_GT? integer_value SYM_INTERVAL_SEP SYM_LT? integer_value '|'
    | '|' relop? integer_value '|'
    ;
integer_interval_list_value : integer_interval_value ( ( ',' integer_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

real_value : ( '+' | '-' )? REAL ;
real_list_value : real_value ( ( ',' real_value )+ | ',' SYM_LIST_CONTINUE ) ;
real_interval_value :
      '|' SYM_GT? real_value SYM_INTERVAL_SEP SYM_LT? real_value '|'
    | '|' relop? real_value '|'
    ;
real_interval_list_value : real_interval_value ( ( ',' real_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

boolean_value : SYM_TRUE | SYM_FALSE ;
boolean_list_value : boolean_value ( ( ',' boolean_value )+ | ',' SYM_LIST_CONTINUE ) ;

character_value : CHARACTER ;
character_list_value : character_value ( ( ',' character_value )+ | ',' SYM_LIST_CONTINUE ) ;

date_value : ISO8601_DATE ;
date_list_value : date_value ( ( ',' date_value )+ | ',' SYM_LIST_CONTINUE ) ;
date_interval_value :
      '|' SYM_GT? date_value SYM_INTERVAL_SEP SYM_LT? date_value '|'
    | '|' relop? date_value '|'
    ;
date_interval_list_value : date_interval_value ( ( ',' date_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

time_value : ISO8601_TIME ;
time_list_value : time_value ( ( ',' time_value )+ | ',' SYM_LIST_CONTINUE ) ;
time_interval_value :
      '|' SYM_GT? time_value SYM_INTERVAL_SEP SYM_LT? time_value '|'
    | '|' relop? time_value '|'
    ;
time_interval_list_value : time_interval_value ( ( ',' time_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

date_time_value : ISO8601_DATE_TIME ;
date_time_list_value : date_time_value ( ( ',' date_time_value )+ | ',' SYM_LIST_CONTINUE ) ;
date_time_interval_value :
      '|' SYM_GT? date_time_value SYM_INTERVAL_SEP SYM_LT? date_time_value '|'
    | '|' relop? date_time_value '|'
    ;
date_time_interval_list_value : date_time_interval_value ( ( ',' date_time_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

duration_value : ISO8601_DURATION ;
duration_list_value : duration_value ( ( ',' duration_value )+ | ',' SYM_LIST_CONTINUE ) ;
duration_interval_value :
      '|' SYM_GT? duration_value SYM_INTERVAL_SEP SYM_LT? duration_value '|'
    | '|' relop? duration_value '|'
    ;
duration_interval_list_value : duration_interval_value ( ( ',' duration_interval_value )+ | ',' SYM_LIST_CONTINUE ) ;

term_code_value : TERM_CODE_REF ;
term_code_list_value : term_code_value ( ( ',' term_code_value )+ | ',' SYM_LIST_CONTINUE ) ;

relop : SYM_GT | SYM_LT | SYM_LE | SYM_GE ;

SYM_LIST_CONTINUE: '...' ;
SYM_INTERVAL_SEP: '..' ;
```

### Base Patterns Grammar (ANTLR4)

```antlr
grammar base_patterns;
import base_lexer;

type_id      : ALPHA_UC_ID ( '<' type_id ( ',' type_id )* '>' )? ;
attribute_id : ALPHA_LC_ID ;
identifier   : ALPHA_UC_ID | ALPHA_LC_ID ;

archetype_ref : ARCHETYPE_HRID | ARCHETYPE_REF ;
```

---

## Last Updated

27 July 2020, 10:30:22 +0100