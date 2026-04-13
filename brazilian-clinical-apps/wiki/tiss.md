---
title: TISS — Troca de Informação em Saúde Suplementar
type: concept
sources:
  - raw/market-landscape-research.md
created: 2026-04-12
updated: 2026-04-12
---

TISS (Troca de Informações na Saúde Suplementar) is the **mandatory electronic data exchange standard** for health plan beneficiary care data in Brazil's supplementary health sector. Every clinical software that interfaces with private health insurers must be TISS-compliant. Non-compliance prevents electronic claims submission to the 668 ANS-registered insurers covering ~51 million Brazilians.

**Established by:** ANS (Agência Nacional de Saúde Suplementar)  
**Governing resolution:** RN nº 501 (and subsequent updates)  
**Current version:** March 2024 ([ANS — Padrão TISS Março/2024](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/marco-2024))

---

## What TISS Is

TISS standardizes the electronic exchange of beneficiary care data among three parties:
1. **Operadoras** (health insurers)
2. **Prestadores** (healthcare providers — clinics, hospitals, physicians)
3. **ANS** (the regulator)

The key rule: insurers cannot request paper copies of information already transmitted electronically via TISS with a valid ICP-Brasil digital certificate ([TISS Organizational Component](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/PadroTISS_ComponenteOrganizacional_202401.pdf)).

**Interoperability mandate:** TISS must be interoperable with SUS systems (SIH, SIA, SIM, SINASC) and ANS registration systems ([TISS Organizational Component](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/PadroTISS_ComponenteOrganizacional_202401.pdf)).

---

## Five Components of TISS

| # | Component | Description | Current Version |
|---|---|---|---|
| **1** | **Organizational** | Operational rules for who must comply and how | 202403 |
| **2** | **Content & Structure** | XML-based data architecture for electronic messages (guias) | 202211 |
| **3** | **Concepts Representation** | TUSS terminology for clinical codes and procedures | 202403 |
| **4** | **Security & Privacy** | Encryption and confidentiality requirements | 202305 |
| **5** | **Communication** | XML messaging formats and electronic protocols | 04.01.00 and 01.04.01 |

([ANS TISS March 2024](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss/marco-2024))

---

## Covered Transactions

TISS standardizes electronic exchanges for:
- **Authorization requests** — guias de consultas, exames, internações, terapias
- **Billing/invoicing** — providers submitting claims to insurers
- **Reimbursement claims** — beneficiaries seeking direct reimbursement
- **Monitoring data** — insurers reporting to ANS

---

## TUSS — Terminologia Unificada da Saúde Suplementar

TUSS is the **standardized procedure code and nomenclature system** that constitutes Component 3 (Concepts Representation) of TISS. It defines the codes used in all TISS electronic messages.

**Full name:** Terminologia Unificada da Saúde Suplementar  
**Created by:** ANS + AMB (Associação Médica Brasileira) + COPISS (Comitê de Padronização das Informações em Saúde Suplementar)  
**Based on:** CBHPM 6th Edition (Classificação Brasileira Hierarquizada de Procedimentos Médicos)

([ANS — TUSS](https://www.ans.gov.br/a-ans/sala-de-noticias-ans/operadoras-e-servicos-de-saude/2010-rol-de-procedimentos-e-terminologia-unificada-da-saude-suplementar))

### TUSS vs TISS

| | TISS | TUSS |
|---|---|---|
| **Role** | The electronic interchange standard (the "pipe") | The terminology/codes used within that pipe (the "language") |
| **Layer** | Protocol and format | Vocabulary/codeset |
| **Analogy** | EDI messaging standard | ICD-10 / procedure codes |

([Mais Laudo](https://maislaudo.com.br/blog/tabela-tuss/))

### Five TUSS Categories

1. Medical procedures and other assistive services
2. Daily rates and service fees (diárias e taxas)
3. Materials and medications
4. Orthotics, prosthetics, and special materials (OPME)
5. Items not in CBHPM but recognized by ANS

([Mais Laudo](https://maislaudo.com.br/blog/tabela-tuss/))

### TUSS Governance

- ANS maintains and updates TUSS; COPISS proposes additions and reviews codes.
- For unlisted procedures, an insurer can create a temporary proprietary code until COPISS approves inclusion.

([Mais Laudo](https://maislaudo.com.br/blog/tabela-tuss/))

---

## ANS Requirements for Clinical Software Vendors

Beyond TISS itself, ANS imposes several obligations on stakeholders:

| Obligation | Description | Reference |
|---|---|---|
| **TISS compliance** | All electronic data exchanges between providers and insurers must use TISS (XML guias) | RN 501 |
| **DIOPS reporting** | Insurers submit quarterly/annual financial data via DIOPS-DOCS (XML). Relevant for insurer-facing software | RN 527 ([Blendus Blog](https://blendus.com.br/blog/normas-ans-para-operadoras-de-saude/)) |
| **Corporate portal** | Each insurer must maintain an internet-facing portal for TISS data exchange | RN 501 |
| **Coordenador TISS** | Each insurer must designate a TISS Coordinator — a technical professional responsible for compliance | [ANS](https://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar) |
| **IDSS performance index** | ANS scores insurers on Índice de Desempenho da Saúde Suplementar; affects regulatory eligibility | [BVS](https://bvsms.saude.gov.br/bvs/saudelegis/ans/2025/res_0630_07_04_2025.html) |
| **APS Certification** | Optional primary care certification (RN 572/2023); requires specific software capabilities | RN 572/2023 |
| **Rol de Procedimentos** | Mandatory minimum coverage list; billing modules must map against Rol codes | ANS |

---

## Why TISS Matters for Clinical Software Vendors

1. **Mandatory for private-payer revenue cycle.** Any clinic or hospital billing a health insurer must use TISS-formatted XML guias. Software that does not implement TISS cannot process private insurance billing electronically.

2. **Digital certificate requirement.** Valid ICP-Brasil digital certificates are required for TISS transmissions, creating a dependency on [[sus-integration]] PKI infrastructure.

3. **Compliance as competitive differentiation.** TISS compliance is complex to implement and maintain (versioned XML schemas, regular ANS updates). Vendors with robust TISS teams create switching costs.

4. **Integration with Rol de Procedimentos.** Billing modules must map against the ANS mandatory minimum coverage list, requiring ongoing maintenance as the Rol is updated.

5. **LGPD intersection.** TISS billing data sent to insurers generally does not require separate patient consent; however, detailed clinical data in reports may require consent under [[lgpd-health-data]].

---

## Platforms with TISS Integration

TISS compliance is table-stakes for any platform serving the supplementary market. Platforms in this wiki that implement TISS include: [[iclinic]], [[feegow]], [[amplimed]], [[clinica-nas-nuvens]], [[prontmed]], [[shosp]], [[ninsaude]], [[mv-sistemas]], [[pixeon]], among others.

---

## See Also

- [[lgpd-health-data]] — Data protection requirements intersecting with TISS transmissions
- [[sus-integration]] — ICP-Brasil certificates also required for RNDS/SUS
- [[market-overview]] — Market context for private insurer coverage
- [[sbis-certification]] — Software certification standard that validates security Component 4
- [[anvisa-samd]] — ANVISA regulation relevant to software with clinical decision functions
