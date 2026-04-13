# Data Types Information Model

**Issuer**: openEHR Specification Program
**Release**: RM Release-1.1.0
**Status**: STABLE
**Source**: https://specifications.openehr.org/releases/RM/latest/data_types.html
**Licence**: Creative Commons Attribution-NoDerivs 3.0 Unported

---

## Amendment Record

| Issue | Details | Raiser, Implementer | Completed |
|-------|---------|-------------------|-----------|
| RM Release 1.1.0 | 2.2.0 | Multiple | 30 Apr 2020 |
| RM Release 1.0.4 | 2.1.3 | Multiple | 21 Dec 2018 |
| RM Release 1.0.3 | 2.1.2 | Multiple | 15 Nov 2015 |

## Acknowledgements

### Editor
- Thomas Beale, Ars Semantica (UK); openEHR Foundation Management Board

### Contributors
Silje Ljosland Bakke, Pieter Bos, Rong Chen, Matthew Darlinson, Heath Frankel, Peter Gummer, Andrew Goodchild, Grahame Grieve, Sam Heard, Sebastian Iancu, Dipak Kalra, Bostjan Lah, Heather Leslie, David Lloyd, Kristoffer Lundberg, Chunlan Ma, Jan Mewes, Bjørn Næss, Pablo Pazos Gutierrez, Peter Schloeffel, Erik Sundvall, Zar Zar Tun

### Support
University College London (CHIME), Ocean Informatics, Distributed Systems Technology Centre (DSTC)

---

## 1. Preface

### 1.1. Purpose

This specification defines the openEHR Data Types Information Model used across the openEHR Reference Model. Target audiences include standards bodies, academic groups, open source healthcare community, solution vendors, medical informaticians, clinicians, and health data managers.

### 1.2. Related Documents

Prerequisites:
- openEHR Architecture Overview
- openEHR Support Information Model

### 1.3. Status

STABLE. Development version: https://specifications.openehr.org/releases/RM/latest/data_types.html

### 1.4. Feedback

- Forum: https://discourse.openehr.org/c/specifications/rm
- Issues: https://specifications.openehr.org/components/RM/open_issues
- Change history: https://specifications.openehr.org/components/RM/history

### 1.5. Conformance

Conformance testing uses formal Implementation Technology Specifications (ITSs) such as IDL interfaces or XML-schema.

---

## 2. Background

### 2.1. Scope

Defines clinical/scientific data types for openEHR models including EHR, demographic, and terminological models. Types derived from Good Electronic Health Record (GEHR), Synapses project, ISO 13606-1, ISO 13606-3, and HL7v3 Data Types.

### 2.2. Design Criteria

Three primary concerns drive design:
1. **Clarity of expression** - clearly convey clinical domain semantics
2. **Ease of implementation** - compatibility with object-oriented languages (IDL, C++, Java, C#, Eiffel, Delphi, Python)
3. **Interoperability** - compatibility with other standards

All types use `DV_` prefix to avoid clashes with language built-ins. Models avoid multiple inheritance (except for substitutability). Generic classes clarify structure. XML-schema implementation feasible. Relational database mapping straightforward.

### 2.3. Prior Work

Reviewed GEHR, HL7v3, ISO 13606-1, and OMG Corbamed type systems. Special attention to HL7v3 data types (see Appendix A for detailed comparison).

---

## 3. Introduction

### 3.1. Overview

Types suitable for scientific, clinical, and related information structures. Built on primitive types: `Integer`, `Real`, `Boolean`, `Character`, `Octet`, `String`, `List<T>`, `Set<T>`, `Array<T>` (defined in openEHR Support Information Model).

All `DV_` types inherit from `DATA_VALUE` class. Two uses in reference models:
1. Data values via `DATA_VALUE` class (e.g., `ELEMENT._value_`)
2. Attribute types in other classes (dates, coded terms)

### 3.2. Package Structure

Data types organized in packages:
- Basic Package
- Text Package
- Quantity Package
- Date Time Package
- Time_specification Package
- Encapsulated Package
- Uri Package

---

## 4. Basic Package

### 4.1. Overview

`data_types.basic` package contains types for bistate values, state machine states, and real-world entity identifiers.

#### 4.1.1. Requirements

##### 4.1.1.1. Bi-state Values

Boolean or bi-state data types inheriting from `DATA_VALUE`, enabling use as `ELEMENT._value_`.

##### 4.1.1.2. State Machine States

Type for state values in state machines (e.g., medication order lifecycle). Enables archetyping via state machine definitions rather than integer constraints.

##### 4.1.1.3. Real-world Entity Identification

Real-world entity (RWE) identifiers (driver's license, social security number, passport, prescription ID) are not guaranteed unique despite design intent. Treated as entity attributes, not reliable identifiers. Examples:

- Driver's licence ID
- Social security number
- Passport number
- Prescription ID

RWE identifiers continue identifying entities regardless of attribute changes. If two RWE IDs equal, they refer to same RWE.

#### 4.1.2. Design

`DV_IDENTIFIER` records three components:

1. **Identifier** (mandatory) - given to item of interest
2. **Issuing authority** (optional) - e.g., federal health department
3. **Assigner** (optional) - organization creating identified item

Additionally records identifier type (e.g., "driver's licence"). All fields are text rather than coded (no definitive vocabularies). Recommended sources: HL7v2 Table 0203.

Only `identifier` field mandatory. Strongly recommend populating `type` and `issuer`. Often `issuer` and `assigner` identical; separate fields allow central issuer distributing identifier blocks to assigning organizations.

---

## 4.2. Class Descriptions

### 4.2.1. DATA_VALUE Class

**Class**: `DATA_VALUE (abstract)`

**Description**: Abstract parent of all `DV_` data value types. Common ancestor in openEHR models.

**Inherit**: `OPENEHR_DEFINITIONS`

### 4.2.2. DV_BOOLEAN Class

**Class**: `DV_BOOLEAN`

**Description**: Items with truly boolean data (true/false, yes/no answers). Critical to devise meanings carefully ensuring only true/false results.

**Misuse**: Not replacement for enumerated types (male/female). Such values should be coded; enumerations often exceed two values.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: Boolean` | Boolean value of this item |

### 4.2.3. DV_STATE Class

**Class**: `DV_STATE`

**Description**: Represents state values obeying defined state machines (instruction/care process states). Expressed as String with archetype-defined state machines driving values. Powerful method capturing stateful processes in simple data.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: DV_CODED_TEXT` | State name from archetype-defined state/event table |
| 1..1 | `is_terminal: Boolean` | Indicates if terminal state (aborted, completed) |

### 4.2.4. DV_IDENTIFIER Class

**Class**: `DV_IDENTIFIER`

**Description**: Represents identifiers of real-world entities. Typical examples: driver's license, social security number, veterans affairs number, prescription ID, order ID.

Represents any identifier issued by authority/agency for real things.

**Misuse**: Not for infrastructure-generated information entity identifiers; use `OBJECT_ID` and `OBJECT_REF` types instead.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `issuer: String` | Optional authority issuing identifier type |
| 0..1 | `assigner: String` | Optional organization assigning ID |
| 1..1 | `id: String` | Identifier value, often structured per issuer rules |
| 0..1 | `type: String` | Optional type (prescription, SSN). Controlled vocabulary future possibility |

**Invariants**:

- `Id_valid`: `not id.is_empty`

---

## 5. Text Package

### 5.1. Overview

`rm.data_types.text` package contains types for textual values: plain text, coded terms, narrative text.

#### 5.1.1. Requirements

Two overriding principles for text:

1. "Clinicians able to record exactly what they want to say...whether very general
   or very specific...appropriate coded terms available" (with facility for later coding)
2. Assumes terminology service providing "complete interface to terminology"

Terminology ID types:

- `"local"` - origin in archetype; archetype contains codes/local translation
- `"[authority]"` - e.g., "openehr", "centc251", "hl7"
- `"[authority]:[Domain value set]"` - e.g., "openehr:event math function"
- `"SNOMED-CT"`, `"ICD10AM"` - universally known authoritative sources

##### 5.1.1.1. Narrative Text

Uses include:
- Coded reference model attributes
- Subjective/imprecise patient responses
- Narrative statements (visual observations)
- Prose tracts (findings, conclusions, prognoses)
- Values when codes/terminology unavailable

May have associated code phrases (mappings); may mix coded items within paragraph.

##### 5.1.1.2. Terminological Entities

Terminology use ensures:
- Meaning interoperability (avoid "cold" ambiguity)
- Standardized textual renderings (vs. informal shorthand)
- Unambiguous problem/medication/diagnosis naming
- Standard naming (Physical examination headings)
- Finite value sets (Blood Group = A|B|AB|O)
- Classification for statistical studies

Basic interoperability requirement: record both rubric and code/code-phrase, retaining originally intended text for receivers lacking terminologies.

Terminology services handle validated coordination of terms. Post-coordinations carry code expressions interpretable by terminology. Difference: pre-coordinated terms single code; post-coordinated terms code phrase/expression.

##### 5.1.1.3. Integration Scenarios

Common requirements:

1. Represent user-chosen term AND preferred term (when different)
2. Capture mapped term code AND preferred term/expression text

##### 5.1.1.4. Text Formatting

Modern systems support visual formatting. Clinicians expect paragraphs, bolding, bullet lists. Coded term text typically unformatted strings. No guarantee newlines/bolding won't appear in future rich text rubrics.

Clinicians need freedom maximizing clarity via formatting.

#### 5.1.2. Design

Atomic text items: `DV_TEXT` or `DV_CODED_TEXT`. Use `DV_TEXT` where coded/non-coded text allowed. Use `DV_CODED_TEXT` where text must be coded.

`DV_TEXT` captures text (`_value_` attribute) with optional formatting/hyperlinking.

`DV_CODED_TEXT` captures:
- Code from terminology service (`_defining_code_`, `CODE_PHRASE` type)
- Text rubric (`_value_` attribute from `DV_TEXT`)

`CODE_PHRASE._code_string_` records term code/expression retrievable from terminology service.

`DV_CODED_TEXT` captures actual user-chosen term (preferred term/synonym, or post-coordination expression). Use if final textual value exactly matches terminology service term text. User modifications require mapping to `DV_TEXT` instead.

**Deprecated**: `DV_PARAGRAPH` represented larger prose via `DV_TEXT` lists. Now represented as plain text with newlines or markdown.

#### 5.1.3. Qualification

Qualification narrows meaning through post-coordinating additional terms. Example: "acute bronchitis" qualifies "bronchitis"; all instances of latter also instances of former.

#### 5.1.4. Meaning Modification

Modifiers change meaning so modified term no longer refers to unmodified term instances.

##### 5.1.4.1. Mode-changing Terms

Words like "risk of", "fear of", "history of" change 'mode' (present to past/potential). Modified terms shouldn't match root term queries (coronary disease query shouldn't match "family history of coronary disease").

##### 5.1.4.2. Context Sensitivity

Meaning changes by context:

- Blood sugar level post-75gm loading differs from fasting
- Pulmonary artery systolic BP differs from systemic
- "Total hip replacement" in planned procedure context
- "Meningitis" in differential diagnosis context

##### 5.1.4.3. Negation

Special mode change type. Historically serious design challenge—negation modifiers only sensible with certain terms.

##### 5.1.4.4. Representation of Meaning-Modifying Terms

Rather than explicit features in `DV_CODED_TEXT`, general principle: higher-level archetyped structures (e.g., `ENTRY`) are minimal indivisible information units. Full meaning requires considering all node names from root to relevant leaf.

Example: "family history of coronary disease" represented as `ENTRY` named "subject family history" including further structure; coded term "coronary disease" appears in this structure. Actual structure completely defined by archetypes.

Same approach for context-dependent terms: "planned procedures" or "differential diagnosis" root nodes; contained terms' meaning understood including root.

Negations best handled by archetype design. Terminologies may provide terms like "No known allergies," but medicolegal requirements may demand recording "no known allergies to penicillin" (specific negation). Generic negation modifier approach creates problems: "no liver" combinations produce non-sensical/difficult interpretations.

Negation handling principle: most naive use cases are ambiguous. Requires detail for EHR usefulness. Archetypes preclude clinician negating terms typically. If needed, handle via negative/quantitative answer: "allergies: NONE" with "allergies" `DV_CODED_TEXT`, "NONE" `DV_CODED_TEXT` or `DV_TEXT`. No explicit openEHR negation model.

#### 5.1.5. Mappings

Circumstances require mapping text/coded text to alternative terminology terms. Theoretically shouldn't occur (relationships belong in knowledge base/terminology service). Practically, real-world activities breach information/knowledge boundary; explicit mapping concept included with "purpose" and "match" indicators.

##### 5.1.5.1. Classification (Broader Terms)

Text items map to coded classifiers for research/reporting/decision support. Example: GP writes "Ross River infection" (tropical Australia) using ICD9 lacking term; maps to ICD9 classifier "arbovirus infection NOS."

Utility: enables powerful decision support inferences; handles unavailable terminology classification; available to terminology-lacking users.

Classifying mappings: add term to mappings list with match='>' (broader). Match values from ISO 2788/5964: '>' (broader), '<' (narrower), '=' (equivalent).

##### 5.1.5.2. Equivalent / Synonymous Terms

Pathology labs historically code locally, sometimes supplying nearest equivalent (e.g., LOINC) enabling receiver standard processing.

"Equivalence" means same meaning, different vocabulary.

Equivalent term instances: laboratory local terminology with recognized terminology equivalents; specialist vocabulary translation across jurisdictions; plain text mapping to equivalent coded terms via natural language processing.

Match attribute = '=' (synonym).

##### 5.1.5.3. More Specific Mappings (Narrower Terms)

Occasional need mapping to narrower meaning terms. Example: clinician records syndrome "croup"/"influenza" (terminology lacks these general terms, has specific "viral laryngo-tracheitis"/"influenza type A"). Clinician should record intended meaning (plain text); mapping to precise term possible.

Narrower term mappings: match = '<'.

##### 5.1.5.4. The Unified Medical Language System (UMLS)

UMLS reference terms potentially supplied with coded terms via UMLS Concept Unique Identifier (CUI). UMLS (National Library of Medicine) cross-references terms across ICDx, SNOMED CT, READ.

Proper UMLS use: terms passed to UMLS interface; CUI + rubric received. Mapping approach could also map UMLS CUIs to existing EHR text/terms; construct `DV_CODED_TEXT` per UMLS "term" (code=CUI, rubric=CUI text rendering). Same approach for future thesauri.

##### 5.1.5.5. Legacy Mapping Scenarios

Legacy data conversion (only codes available, e.g., ICD/ICPC):

- Create `DV_TEXT` value="(not available)"
- Add mapping: `purpose`="legacy conversion", `match`="=", `target`=`CODE_PHRASE` with available legacy code
- Expresses legacy system recorded code directly; conversion treats code as mapping

#### 5.1.6. Language Translations

Natural language typically known from enclosing Entry/context. Where different (German sentence in English diagnosis) or no context, `DV_TEXT._language_` indicates text language.

#### 5.1.7. Formatting and Hyperlinking

Formatted text represented via `DV_TEXT`/`DV_CODED_TEXT` instances.

**Prior to RM Release 1.0.4**: `DV_PARAGRAPH` represented larger text tracts with newlines/formatting subsections (each `DV_TEXT`/`DV_CODED_TEXT`).

**Warning**: `DV_PARAGRAPH` now deprecated; use `DV_TEXT`/`DV_CODED_TEXT`. For legacy, `DV_PARAGRAPH` remains legal, basic support required.

**Warning**: Previously assumed `_value_` contained no newlines. Since RM Release 1.0.4, newlines permitted.

Text processing pipeline: readable text with markings → rendering (HTML, PDF) → display tool. Historical approaches (nroff, troff, Latex, XML) disadvantageous: poor human readability, rendering-engine-specific. Modern trend: markdown (readable raw form, industry-standard conversion).

**Deprecated**: Prior RM Release 1.0.4, `DV_TEXT._formatting_` contained CSS font strings. Now deprecated (legacy systems allowed).

Current approach: `_formatting_` attribute values:

- `Void` - no formatting marks (newlines allowed); safe straight-through display
- `"markdown"` - markdown format, strongly recommend CommonMark; render via HTML conversion or straight-through if unavoidable
- `"plain"` - plain text, possibly newlines, unformatted (Void equivalent); enables clear unformatted requirement
- `"plain_no_newlines"` - plain text, no newlines, simple atom
- (legacy - deprecated) - CSS string form `"name:value; name:value…"` e.g. `"font-weight : bold; font-family : Arial; font-size : 12pt;"`

`DV_TEXT._hyperlink_` (type `DV_URI`) specifies web link for whole text. Like formatting, modern markdown in `_value_` more flexible (multiple links).

**Deprecated**: Starting RM Release 1.0.4, `_hyperlink_` deprecated for markdown links in `_value_` (CommonMark: `[text](uri)`).

Not all CommonMark features allowed in markdown `_value_`:

- No HTML blocks
- No raw HTML
- No images (include via `DV_MULTIMEDIA`)

##### 5.1.7.1. Usage in DV_TEXT Instances

| Requirement | `_value_` | `_formatting_` | Legacy |
|------------|----------|----------------|---------
| Plain text atom (no formatting, no newlines) | plain text string | `Void` or `"plain_no_newlines"` | same |
| Plain text atom with hyperlink (no formatting, no newlines) | text `[text](uri)` or CommonMark link | `"markdown"` | `_value_`=plain text; `_hyperlink_`=URI |
| Plain text paragraphs (no other formatting) | plain text with newlines | `Void` or `"plain"` | `DV_PARAGRAPH` containing plain legacy text atom `DV_TEXT`s |
| Formatted text with paragraphs, bolding, italics, lists, links | CommonMark text string | `"markdown"` | `DV_PARAGRAPH` containing legacy `DV_TEXT`s (CSS formatting/`_hyperlink_`) |

##### 5.1.7.2. Usage in DV_CODED_TEXT Instances

| Requirement | `_value_` | `_formatting_` | Legacy |
|------------|----------|----------------|---------
| Plain text of coded term | plain text string | `Void` | same |
| Plain text of coded term with hyperlink | text `[text](uri)` or CommonMark link | `"markdown"` | `_value_`=plain text; `_hyperlink_`=URI |
| Plain coded term text, containing newlines | plain formatted text | `Void` or `"plain"` | N/A |

### 5.2. Class Descriptions

#### 5.2.1. DV_TEXT Class

**Class**: `DV_TEXT`

**Description**: Text item containing legal characters arranged as words, sentences, etc. (single `DV_TEXT` may exceed one word). Visual formatting/hyperlinks via markdown.

`_formatting_` field effects:
- `_formatting_ = "plain"` - plain text, may contain newlines
- `_formatting_ = "plain_no_newlines"` - plain text, no newlines
- `_formatting_ = "markdown"` - markdown format; CommonMark strongly recommended

`DV_TEXT` coded via mappings.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | Displayable rendition regardless of structure. For `DV_CODED_TEXT`, terminology service rubric. |
| 0..1 | `hyperlink: DV_URI` | DEPRECATED: deprecated field; use markdown link/text in `_value_`, `"markdown"` in `_formatting_`. Prior RM Release 1.0.4: optional web link behind text/coded term. |
| 0..1 | `formatting: String` | If set, one of: `"plain"` (plain text, possibly newlines, unformatted); `"plain_no_newlines"` (no newlines/formatting); `"markdown"` (markdown format, CommonMark recommended). DEPRECATED: CSS string `"name:value; name:value…"` e.g. `"font-weight : bold;..."` |
| 0..1 | `mappings: List<TERM_MAPPING>` | Terms from other terminologies matching this, typically where originator (pathology lab) uses local terminology supplying well-known equivalents (LOINC). |
| 0..1 | `language: CODE_PHRASE` | Optional localized language indicator. Coded from openEHR languages code set. Used when text object different language from enclosing `ENTRY`, or outside enclosing structure indicating language. |
| 0..1 | `encoding: CODE_PHRASE` | Character encoding scheme name. Coded from openEHR character sets code set. Unicode default with UTF-8 assumed encoding. Allows variation assumptions. |

**Invariants**:

- `Language_valid`: `language /= Void implies code_set (Code_set_id_languages).has_code (language)`
- `Encoding_valid`: `encoding /= Void implies code_set (Code_set_id_character_sets).has_code (encoding)`
- `Mappings_valid`: `mappings /= void implies not mappings.is_empty`
- `Formatting_valid`: `formatting /= void implies not formatting.is_empty`

#### 5.2.2. TERM_MAPPING Class

**Class**: `TERM_MAPPING`

**Description**: Coded term mapped to `DV_TEXT` with relative match. Plain/coded text items mapped to alternative terminology terms for computer processing. Only instances of `DV_CODED_TEXT` used for mappings.

Used for classification terms (e.g., ICD classifiers to SNOMED terms) or equivalent mappings across nursing vocabularies.

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `match: char` | Relative match of target term: `'>'` broader (arbovirus infection→viral infection); `'='` equivalent; `'<'` narrower (diabetes→diabetes mellitus); `'?'` unknown. From ISO 2788/5964. |
| 0..1 | `purpose: DV_CODED_TEXT` | Mapping purpose: 'automated data mining', 'billing', 'interoperability'. |
| 1..1 | `target: CODE_PHRASE` | Target term of mapping. |

**Functions**:

| Signature | Meaning |
|-----------|---------|
| `narrower (): Boolean` Post: `match = '<' implies Result` | Mapping to narrower term |
| `broader (): Boolean` Post: `match = '>' implies Result` | Mapping to broader term |
| `equivalent (): Boolean` | Mapping to equivalent term |
| `unknown (): Boolean` Post: `match = '?' implies Result` | Mapping kind unknown |
| `is_valid_match_code (c: char[1]): Boolean` Post: `Result := c = '>' or c = '=' or c = '<' or c = '?'` | True if match valid |

**Invariants**:

- `Purpose_valid`: `purpose /= Void implies terminology (Terminology_id_openehr).has_code_for_group_id (Group_id_term_mapping_purpose, purpose.defining_code)`
- `Match_valid`: `is_valid_match_code (match)`

#### 5.2.3. CODE_PHRASE Class

**Class**: `CODE_PHRASE`

**Description**: Fully coordinated term from terminology service (not particular terminology).

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `terminology_id: TERMINOLOGY_ID` | Issuing authority identifier for extracted code_string/elements. |
| 1..1 | `code_string: String` | Terminology service key identifying concept/coordination. Likely parsable inside service; syntax assumptions invalid outside. |
| 0..1 | `preferred_term: String` | Optional preferred term corresponding to code/expression in `_code_string_`. Typical integration scenario use carrying both non-preferred actual term and preferred term. |

**Invariants**:

- `Code_string_valid`: `not code_string.is_empty`

#### 5.2.4. DV_CODED_TEXT Class

**Class**: `DV_CODED_TEXT`

**Description**: Text item whose value must be controlled terminology rubric; `_defining_code_` key in `_code_string_`. Combination: `CODE_PHRASE` (code) + term rubric from terminology service in authoring language.

`DV_CODED_TEXT` subtype `DV_TEXT` enables `DV_TEXT` use meaning text optionally coded.

**Misuse**: Not for term code attached to plain text fragment; use `DV_TEXT` + `TERM_MAPPING` to `CODE_PHRASE`.

**Inherit**: `DV_TEXT`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `defining_code: CODE_PHRASE` | Term whose `_value_` textual rendering (rubric). |

#### 5.2.5. DV_PARAGRAPH Class

**Class**: `DV_PARAGRAPH`

**Description**: DEPRECATED: use markdown formatted `DV_TEXT`.

**Original definition**: Logical composite text value from `DV_TEXT` series (plain text, optionally coded, simple formatting), forming larger prose paragraph.

Standard construction method for longer text in summaries, reports.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `items: List<DV_TEXT>` | Paragraph items, each text item (may have own formatting/hyperlinks). |

**Invariants**:

- `Items_valid`: `not items.is_empty`

---

## 6. Quantity Package

### 6.1. Overview

`data_types.quantity` package. (Dates/Times in next section.)

#### 6.1.1. Requirements

##### 6.1.1.1. Scores and Scales

Medicine commonly uses relative magnitude symbols without exact values, typically classifying patients into groups informing decisions. Known as "scores" or "scales." Examples:

- Pain: 'mild', 'medium', 'severe'
- Reflex response: "-", "+/-", "+", "++", "+++", "++++"
- Global scales: Apgar Score, Glasgow Coma Scale (GCS), Barthel Index

Some cases prevent precise quantification (subjective experience/informal judgment); understood as ordered (++ arithmetically greater than +).

Symbolic haemolysed blood values (urinalysis) with approximate ranges, not usable like true quantities:

- "neg", "trace" (10 cells/μl)
- "small" (<25 cells/μl)
- "moderate" (<80 cells/μl)
- "large" (>200 cells/μl)

Second requirement: many cases need numeric values associated with symbols for ordered comparison and longitudinal result comparison (pain, protein). Most scores/scales limit Integer values; some use Real numbers interspersed (Borg CR 10 scale perceived exertion). Both cases: values may negative, zero, positive.

##### 6.1.1.2. Countable Things

Dimensionless countable quantities common in medicine:

- Number of doses: 2
- Number previous pregnancies: 1
- Number tablets: 3

Always integral. Convertible to reals for statistics (average pregnancies per couple).

Some countable entities (tablets) divisible into major fractions (typically halves, occasionally quarters).

##### 6.1.1.3. Dimensioned Quantities

Most common quantity type: measured, dimensioned. Involves aspects:

- Magnitude (real number value)
- Physical property measured (appropriate units)
- Precision concept (decimal places recorded)
- Accuracy concept (known/assumed measurement error via instrumentation/human judgment)

Examples:

- Systolic BP: 110 mmHg
- Height: 178 cm
- Asthma attack rate: 7 /week
- Weight loss: 2.5 kg

##### 6.1.1.4. Ratios and Proportions

Common quantitative type in science/medicine, used situations:

- 1:128 (titer)
- Na:K concentration ratio (unitary denominator)
- Albumin:creatinine ratio
- % e.g., red cell distribution width (RDW)

Generally real number values, despite many integer-appearing examples. Proportions with unitary denominator and % (denominator=100) common.

##### 6.1.1.5. Formulations

Concept superficially similar to proportions/ratios: material formulations, solid in liquid:

- 250 mg / 500 ml (solute/solvent)

Single solute/solvent appears ratio-like; general form any substances mixed, usually per particular procedure. Not candidates direct quantity modelling; constructed via archetyping higher-level structure, each leaf containing required Quantity.

##### 6.1.1.6. Quantity Ranges

Ubiquitous in science/medicine, definable for any measured phenomenon:

- Healthy weight range: 48kg - 60kg
- Normal urinalysis pregnancy protein range: "nil" - "trace"

##### 6.1.1.7. Reference Ranges

Quantity range attached to measured value, common laboratory results. Typical form indicates 'normal' range. Examples:

- Normal serum Na: 135 - 145 mmol/L
- Desirable total cholesterol: < 5.5 mmol/L (technically 2.0-5.5, not usually quoted thus as low cholesterol not problem)

Drug administration ranges typical 'therapeutic' range. Example: Carbamazepine (anticonvulsant) 20-40 μMol/L. Multiple ranges sometimes: Salicylate therapeutic 1.0-2.5 mmol/L, toxic >3.6 mmol/L.

Multiple range instances:

- Drug administration recommendations per patient state. Cyclosporin (immunosuppressant) therapeutic range time post-transplant dependent: kidney <6 months 250-350 μg/L, >6 months 100-200 μg/L.
- Blood IgG/IgA/IgM normal ranges vary significantly by age months post-birth.
- Progesterone/pituitary hormones different phases menstrual cycle/menopause. 4-5 possible ranges per result; only one applies per patient—exact phase possibly unknown, ranges associated with value, no 'normal' range.

Critical question: "which range information relevant to actual recorded patient data?" Theory: only applicable patient-situation range used (per sex, age, smoking, athlete status, organ transplanted, etc.). Usually single "normal" or "therapeutic"/"critical" pair. Practical factors complicate: data sometimes supplied with some/all applicable ranges, even though only some possibly apply—particularly labs lacking patient data. Labs rarely providing all potentially applicable ranges. Patient-relevant range typically recorded separately, determining applicable range at report-generation time.

Reference ranges often need description/interpretation; simple numeric alone insufficient. For instance, a potassium result 5.5 mmol/L with normal range 3.5-5.0 mmol/L is "abnormally high"; clinician must potentially consider result significance depending on kidney function, medications, etc. Reference range reporting frequently includes normal/abnormal status (normal, low, high, critically high, etc.), sometimes additional interpretation text.

##### 6.1.1.8. Normal Range and Status in Laboratory data

Status represents interpretation: normal, low, high, critical, etc. Status normally computed from value vs. reference range, but sometimes directly reported.

#### 6.1.2. Design

##### 6.1.2.1. Basic Semantics

Ordered types hierarchy:

- `DV_ORDERED` - abstract base for ordered values
  - `DV_ORDINAL` - symbolic relative magnitude (scores, scales)
  - `DV_SCALE` - real ordinal values
  - `DV_QUANTIFIED` - ordered numeric values
    - `DV_AMOUNT` - real number magnitudes
      - `DV_QUANTITY` - dimensioned quantities
      - `DV_COUNT` - countable integer things
      - `DV_PROPORTION` - ratios/proportions

##### 6.1.2.2. Accuracy and Uncertainty

`DV_QUANTIFIED` includes `accuracy` attribute representing measurement uncertainty. Values:

- `Void` - accuracy unknown/irrelevant
- Non-negative Real - assumed symmetric percent/absolute accuracy
- Special values: -1.0 (unknown), -2.0 (no quantification for metric)

##### 6.1.2.3. Quantity Ranges

`DV_INTERVAL<T>` represents bounded/unbounded ranges for any ordered type.

##### 6.1.2.4. Proportions

`DV_PROPORTION` represents ratios via numerator, denominator, optionally type specification.

##### 6.1.2.5. Normal and Reference Ranges

`REFERENCE_RANGE<T>` pairs range with optional meaning. `DV_ORDERED` includes optional `normal_range` attribute.

##### 6.1.2.6. Recording Time

`DV_QUANTITY` optionally records magnitude accuracy as magnitude state.

### 6.2. Class Descriptions

#### 6.2.1. DV_ORDERED Class

**Class**: `DV_ORDERED (abstract)`

**Description**: Abstract parent for ordered data types. Properties defined here apply across all ordered types.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `normal_range: REFERENCE_RANGE<T>` | Optional normal range. |
| 0..1 | `normal_status: CODE_PHRASE` | Coded normal status from openEHR Normal status code set. |
| 0..1 | `other_reference_ranges: List<REFERENCE_RANGE<T>>` | Additional reference ranges. |

**Functions**:

| Signature | Meaning |
|-----------|---------|
| `is_normal (): Boolean` | Value within normal range |
| `is_simple (): Boolean` | Normal ranges simple (normal vs. abnormal) |

#### 6.2.2. DV_INTERVAL Class

**Class**: `DV_INTERVAL<T: DV_ORDERED>`

**Description**: Interval (range) of ordered values.

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `lower: T` | Lower boundary; Void if unbounded |
| 0..1 | `upper: T` | Upper boundary; Void if unbounded |
| 1..1 | `lower_included: Boolean` | Inclusive lower boundary |
| 1..1 | `upper_included: Boolean` | Inclusive upper boundary |

**Functions**:

| Signature | Meaning |
|-----------|---------|
| `lower_unbounded (): Boolean` | Lower boundary unbounded |
| `upper_unbounded (): Boolean` | Upper boundary unbounded |
| `has (value: T): Boolean` | Value within interval |

#### 6.2.3. REFERENCE_RANGE Class

**Class**: `REFERENCE_RANGE<T: DV_ORDERED>`

**Description**: Range definition with optional meaning.

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `meaning: DV_TEXT` | Optional range meaning ('normal', 'therapeutic', 'critical', etc.) |
| 1..1 | `range: DV_INTERVAL<T>` | Actual range. |

#### 6.2.4. DV_ORDINAL Class

**Class**: `DV_ORDINAL`

**Description**: Ordered value of symbolic items without precise magnitude, suitable for scores/scales. Records value as paired integer with symbol.

**Inherit**: `DV_ORDERED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: Integer` | Numeric value enabling ordering/comparison. |
| 1..1 | `symbol: DV_CODED_TEXT` | Coded term representing value. |

#### 6.2.5. DV_SCALE Class

**Class**: `DV_SCALE`

**Description**: Real ordinal values for ordinal measurements involving real numbers. Examples: pain scale (0.0-10.0), preference scale (0.0-1.0).

**Inherit**: `DV_ORDERED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: Real` | Real-valued ordinal measurement. |

#### 6.2.6. DV_QUANTIFIED Class

**Class**: `DV_QUANTIFIED (abstract)`

**Description**: Abstract parent for numeric quantities (count, quantity, proportion).

**Inherit**: `DV_ORDERED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `magnitude_status: String` | Status of magnitude: Void (complete), "=" (approximately equal), "<" (less than), ">" (greater than), "<=" (less than or equal), ">=" (greater than or equal). |
| 0..1 | `accuracy: Real` | Measurement uncertainty. Void (unknown/irrelevant), non-negative Real (symmetric ±percent/absolute), -1.0 (unknown), -2.0 (not quantified). |

#### 6.2.7. DV_AMOUNT Class

**Class**: `DV_AMOUNT (abstract)`

**Description**: Abstract parent for real number magnitude quantities.

**Inherit**: `DV_QUANTIFIED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `magnitude: Real` | Quantity value. |

#### 6.2.8. DV_QUANTITY Class

**Class**: `DV_QUANTITY`

**Description**: Dimensioned quantity (magnitude + units). Represents measured/derived values (temperature, height, lab results).

**Inherit**: `DV_AMOUNT`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `precision: Integer` | Decimal places. Negative values indicate left-decimal precision. |
| 1..1 | `units: String` | Units String per openEHR units syntax. |
| 0..1 | `units_system: String` | Optional units system identifier (ISO 80000, UCUM, etc.). |
| 0..1 | `units_display_name: String` | Optional display name for units (human-readable form). |

#### 6.2.9. DV_COUNT Class

**Class**: `DV_COUNT`

**Description**: Countable quantity (integral number). Examples: doses, pregnancies, tablets.

**Inherit**: `DV_AMOUNT`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `magnitude: Integer` | Count value. |

#### 6.2.10. DV_PROPORTION Class

**Class**: `DV_PROPORTION`

**Description**: Ratio/proportion (numerator, denominator, optional type).

**Inherit**: `DV_QUANTIFIED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `numerator: Real` | Numerator value. |
| 1..1 | `denominator: Real` | Denominator value (non-zero). |
| 0..1 | `type: Integer` | Proportion type (0=unitary, 1=percent, 2=ratio, 3=fraction, 4=quotient). Constrained by `PROPORTION_KIND`. |
| 1..1 | `precision: Integer` | Decimal places. |

**Invariants**:

- `Denominator_not_zero`: `denominator /= 0.0`

#### 6.2.11. PROPORTION_KIND Class

**Class**: `PROPORTION_KIND`

**Description**: Type enumeration for proportions.

Values:
- `0` - unitary (0.0-1.0)
- `1` - percent (0.0-100.0)
- `2` - ratio (unspecified range)
- `3` - fraction (unspecified range)
- `4` - quotient (unspecified range)

#### 6.2.12. DV_ABSOLUTE_QUANTITY Class

**Class**: `DV_ABSOLUTE_QUANTITY (abstract)`

**Description**: Abstract parent for absolute quantities (opposed to relative).

**Inherit**: `DV_AMOUNT`

### 6.3. Syntaxes

#### 6.3.1. Units Syntax

Units represented as strings. Format examples:

- Simple: `"mg"`, `"mmol/L"`, `"cm"`, `"°C"`
- Complex: `"kg.m2/s2"`, `"mL/(8.h)"` (per 8 hours)

Based on UCUM (Unified Code for Units of Measure) specification, allowing standard unit representation and conversion.

---

## 7. Date Time Package

### 7.1. Overview

`data_types.date_time` package for temporal values.

#### 7.1.1. Requirements

##### 7.1.1.1. Standard Date/Times

Standard requirements for date/time recording:

- Date (year, month, day)
- Time (hour, minute, second, fractional second)
- Date-time (date + time)
- Duration (temporal interval)

ISO 8601 standard provides specification.

##### 7.1.1.2. Partial Date/Times

Real-world situations involve incomplete dates/times:

- "born in 1995" (year only)
- "seen Tuesday at 14:00" (time only)
- "first diagnosis sometime in 2015" (year only)

Partial dates/times representable via same classes as complete, with Void fields.

#### 7.1.2. Design

##### 7.1.2.1. General Approach

Values represented as ISO 8601 strings internally. Classes provide structured access. All temporal types inherit `DV_TEMPORAL`.

##### 7.1.2.2. Partial Date/Times

Partial temporal values represented with Void fields (month/day for partial date, hour/minute for partial time).

##### 7.1.2.3. Calendars

Gregorian calendar assumed. Timezone support via ISO 8601.

##### 7.1.2.4. Representation

Values stored/transmitted as ISO 8601 strings. Extended format (with hyphens/colons) recommended for readability.

### 7.2. Class Descriptions

#### 7.2.1. DV_TEMPORAL Class

**Class**: `DV_TEMPORAL (abstract)`

**Description**: Abstract parent for temporal values (date, time, date-time, duration).

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | ISO 8601 string representation. |

#### 7.2.2. DV_DATE Class

**Class**: `DV_DATE`

**Description**: Date value (year, month, day). Partial dates permitted (month/day Void).

**Inherit**: `DV_TEMPORAL`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | ISO 8601 date string (YYYY-MM-DD format); partial dates allowed (YYYY-MM, YYYY). |

#### 7.2.3. DV_TIME Class

**Class**: `DV_TIME`

**Description**: Time value (hour, minute, second, fractional second, timezone). Partial times permitted.

**Inherit**: `DV_TEMPORAL`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | ISO 8601 time string (hh:mm:ss[.fff][Z±hh:mm] format); partial times allowed. |

#### 7.2.4. DV_DATE_TIME Class

**Class**: `DV_DATE_TIME`

**Description**: Date-time value combining date + time with timezone.

**Inherit**: `DV_TEMPORAL`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | ISO 8601 date-time string (YYYY-MM-DDThh:mm:ss[.fff][Z±hh:mm] format). |

#### 7.2.5. DV_DURATION Class

**Class**: `DV_DURATION`

**Description**: Duration (temporal interval). Represented as ISO 8601 duration string.

**Inherit**: `DV_TEMPORAL`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | ISO 8601 duration string (P[n]Y[n]M[n]DT[n]H[n]M[n]S format); negative durations prefix "-". |

---

## 8. Time_specification Package

### 8.1. Overview

`data_types.time_specification` package for recurring/planned temporal specifications (medication schedules, recurring appointments).

#### 8.1.1. Requirements

Temporal specifications for recurring/cyclical events. Examples:

- "every 6 hours" (medication)
- "every Tuesday and Friday" (recurring appointment)
- "daily at 18:00" (blood test monitoring)
- "between meals" (medication timing)

Represented as phase-linked, event-linked periodic, or general specifications.

#### 8.1.2. Design

Three specification types:

1. **Phase-linked** - linked to menstrual cycle phase, meal timing, etc.
2. **Event-linked periodic** - recurring relative events
3. **General** - complex arbitrary specifications (free text or machine-readable)

### 8.2. Class Descriptions

#### 8.2.1. DV_TIME_SPECIFICATION Class

**Class**: `DV_TIME_SPECIFICATION (abstract)`

**Description**: Abstract parent for temporal specifications.

**Inherit**: `DATA_VALUE`

#### 8.2.2. DV_PERIODIC_TIME_SPECIFICATION Class

**Class**: `DV_PERIODIC_TIME_SPECIFICATION`

**Description**: Recurring temporal specification (fixed interval or event-linked).

**Inherit**: `DV_TIME_SPECIFICATION`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `period: DV_DURATION` | Fixed interval period. |
| 0..1 | `frequency: Integer` | Frequency per period (e.g., 2 times per day). |

#### 8.2.3. DV_GENERAL_TIME_SPECIFICATION Class

**Class**: `DV_GENERAL_TIME_SPECIFICATION`

**Description**: General temporal specification via description or expression.

**Inherit**: `DV_TIME_SPECIFICATION`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: DV_PARSABLE` | Specification as parsable string (free text or formal expression). |

### 8.3. Syntaxes

#### 8.3.1. Phase-linked Time Specification Syntax

Temporal specifications linked to phases:

- `"with meals"` - linked to meal times
- `"before menstruation"` - menstrual cycle phase

Represented as coded terms or free text.

#### 8.3.2. Event-linked Periodic Time Specification Syntax

Recurring relative to events:

- `"every 6 hours"` - fixed interval
- `"3 times daily"` - frequency per day
- `"every alternate morning"` - periodic relative events

#### 8.3.3. General Time Specification Syntax

Complex specifications:

- Free text: `"every Tuesday and Friday at 14:00"`
- Formal: cron-like syntax or proprietary expressions

---

## 9. Encapsulated Package

### 9.1. Overview

`data_types.encapsulated` package for encapsulated (non-decomposed) data: binary multimedia, parsable text.

#### 9.1.1. Requirements

Encapsulated data allows inclusion of:

- Multimedia (images, audio, video)
- Structured/formatted documents (PDF, Office formats)
- Parsable text (XML, JSON, custom formats)

Requirements:

- Reference/direct inclusion support
- Multiple encoding/compression variants
- Integrity checking capability

#### 9.1.2. Design

Base class `DV_ENCAPSULATED` for all encapsulated types:

- `DV_MULTIMEDIA` - images, audio, video with media type specification
- `DV_PARSABLE` - structured text with format specification

#### 9.1.3. Examples

Examples: JPEG image, PNG graphic, MP3 audio, PDF document, XML structured data, JSON configuration.

### 9.2. Class Descriptions

#### 9.2.1. DV_ENCAPSULATED Class

**Class**: `DV_ENCAPSULATED (abstract)`

**Description**: Abstract parent for encapsulated data values.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 0..1 | `language: CODE_PHRASE` | Language of content (if text-based). |
| 0..1 | `charset: CODE_PHRASE` | Character set (if text-based). Coded from openEHR character sets. |
| 0..1 | `alternate_text: DV_TEXT` | Alternate plain text representation. |

#### 9.2.2. DV_MULTIMEDIA Class

**Class**: `DV_MULTIMEDIA`

**Description**: Encapsulated multimedia (image, audio, video, document).

**Inherit**: `DV_ENCAPSULATED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `media_type: CODE_PHRASE` | MIME type (image/jpeg, audio/mpeg, etc.). |
| 0..1 | `compression_algorithm: CODE_PHRASE` | Optional compression (zip, gzip, deflate). |
| 1..1 | `data: Array<Octet>` | Binary data. |
| 0..1 | `uri: DV_URI` | Optional URI reference. |
| 0..1 | `integrity_check_algorithm: CODE_PHRASE` | Optional integrity algorithm (MD5, SHA256). |
| 0..1 | `integrity_check: Array<Octet>` | Optional integrity check value. |

#### 9.2.3. DV_PARSABLE Class

**Class**: `DV_PARSABLE`

**Description**: Structured parsable text (XML, JSON, custom formats).

**Inherit**: `DV_ENCAPSULATED`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | Parsable content. |
| 1..1 | `format: String` | Format specification (xml, json, etc.). |

---

## 10. Uri Package

### 10.1. Overview

`data_types.uri` package for Uniform Resource Identifiers.

#### 10.1.1. Requirements

URIs identify resources:

- Web links (http://, https://)
- Email addresses (mailto:)
- EHR references (ehr://)
- Internal identifiers

#### 10.1.2. Design

Base `DV_URI` for general URIs; `DV_EHR_URI` for EHR-specific references.

### 10.2. Definitions

- **URI** - identifier conforming RFC 3986
- **EHR URI** - openEHR-specific scheme (ehr://) referencing EHR entries

### 10.3. Class Descriptions

#### 10.3.1. DV_URI Class

**Class**: `DV_URI`

**Description**: Uniform Resource Identifier reference.

**Inherit**: `DATA_VALUE`

**Attributes**:

| Cardinality | Signature | Meaning |
|-------------|-----------|---------|
| 1..1 | `value: String` | URI string per RFC 3986. |

#### 10.3.2. DV_EHR_URI Class

**Class**: `DV_EHR_URI`

**Description**: EHR-specific URI reference using ehr:// scheme.

**Inherit**: `DV_URI`

**Syntax**: `ehr://server/ehr_id/path[?query]`

Example: `ehr://ethic.acme.com/ehr_id/composition/medications`

### 10.4. Syntaxes

#### 10.4.1. DV_EHR_URI Syntax

Format: `ehr://[authority]/ehr_id/path[?query]`

Components:
- **authority** - optional server identifier
- **ehr_id** - EHR identifier
- **path** - XPath expression (Composition/Element/Cluster paths)
- **query** - optional query string

---

## 11. Implementation Strategies

### 11.1. Overview

Guidance for implementation in various technologies.

### 11.2. Quantities and Ordered_numeric

Implementations should support:

- Proper ordering/comparison operations
- Accuracy/precision handling
- Reference range evaluation
- Magnitude status values

### 11.3. Unicode

All text types assume Unicode (UTF-8 default). Legacy character sets representable via `DV_TEXT.encoding` specification.

### 11.4. Dates and Times

ISO 8601 standard representation. Extended format (hyphens/colons) recommended for readability:

- **Date**: YYYY-MM-DD (partial: YYYY-MM, YYYY)
- **Time**: hh:mm:ss[.fff][Z±hh:mm]
- **Date-Time**: YYYY-MM-DDThh:mm:ss[.fff][Z±hh:mm]
- **Duration**: P[n]Y[n]M[n]DT[n]H[n]M[n]S (negative: -P...)

---

## Appendix A: Comparison with HL7v3 Types

### A.1. Scope

Detailed comparison between openEHR and HL7v3 data types, design approaches, and differences.

### A.2. Design Differences

#### A.2.1. Naming

HL7v3 uses single letter prefixes (ST, II, CO); openEHR uses "DV_" prefix ensuring clarity and avoiding language built-in clashes.

#### A.2.2. Identification

HL7v3 `II` combines identifier/assigner; openEHR separates into distinct RWE identifier vs. IE identifier concepts via `DV_IDENTIFIER` and `OBJECT_REF`.

#### A.2.3. Archetyping

openEHR designed with archetyping in mind (e.g., `DV_STATE` for state machines); HL7v3 generally not archetype-aware.

#### A.2.4. Treatment of Inbuilt Types

openEHR distinguishes assumed primitive types from `DV_` clinical types. HL7v3 less consistent in distinction.

#### A.2.5. Use of Null Markers

HL7v3 includes null flavors; openEHR uses optional attributes (Void) and `magnitude_status`.

#### A.2.6. Terminology Approach

openEHR assumes complete terminology service interface; HL7v3 includes inline terminology mechanisms. openEHR supports flexible mapping via `TERM_MAPPING`.

#### A.2.7. Date/Time Approach

openEHR supports partial dates/times via Void fields; HL7v3 uses explicit flavors. Both use ISO 8601 basis.

#### A.2.8. Time Specification Types

openEHR provides `DV_TIME_SPECIFICATION` hierarchy; HL7v3 uses `SXCM_TS` and related types.

#### A.2.9. Type Conversions

Both support conversions between related types, but openEHR emphasizes semantic clarity in operations.

---

## References

- **GeHR_Aus2001**: Beale & Heard (2000). Good Electronic Health Record (GEHR). Australian EHR specifications.
- **Synapses_Req_A**: Kalra (1996). Synapses project healthcare data requirements.
- **ISO 13606-1**: Electronic health record communication - Part 1: Reference model
- **ISO 13606-3**: Electronic health record communication - Part 3: Distribution rules
- **HL7v3 Data Types**: Health Level Seven Version 3 Data Types
- **ISO 2788**: Guide to establishment and development of monolingual thesauri
- **ISO 5964**: Guide to establishment and development of multilingual thesauri
- **ISO 80000**: Quantities and units
- **RFC 3986**: Uniform Resource Identifier (URI): Generic syntax
- **UCUM**: Unified Code for Units of Measure
- **SNOMED CT**: Systematized Nomenclature of Medicine Clinical Terms
- **ICD**: International Statistical Classification of Diseases
- **LOINC**: Logical Observation Identifiers Names and Codes
- **CommonMark**: A strongly defined, highly compatible specification of Markdown
- **OpenEHR Standard**: openEHR Foundation specifications