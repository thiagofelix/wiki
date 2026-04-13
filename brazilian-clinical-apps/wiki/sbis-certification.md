---
title: SBIS/CFM Certification for EHR Systems
type: concept
sources:
  - raw/market-landscape-research.md
created: 2026-04-12
updated: 2026-04-12
---

SBIS/CFM certification is the primary voluntary conformity assessment program for Electronic Health Record (EHR) software in Brazil. Run jointly by **SBIS (Sociedade Brasileira de Informática em Saúde)** and the **CFM (Conselho Federal de Medicina)**, it evaluates whether clinical software meets security, functionality, and legal requirements for handling patient health records in Brazil.

---

## What It Is

The certification was established through a collaboration between SBIS and CFM to operationalize CFM resolutions mandating that electronic health records meet defined levels of security and functional quality. It is a market-recognized signal that a platform is technically and legally fit for clinical use in Brazil.

SBIS evaluations are explicitly recognized by ANPD (the LGPD enforcement authority) and health sector regulators as a method to validate software security for health data, making certification a practical [[lgpd-health-data]] compliance instrument ([Portal Telemedicina](https://portaltelemedicina.com.br/lgpd-na-saude-como-garantir-a-seguranca-de-dados-dos-pacientes)).

---

## Certification Levels

The program defines two levels of guarantee — **NGS1** and **NGS2** — corresponding to increasing security and functional requirements.

### NGS1 — Nível de Garantia de Segurança 1

The baseline certification level. Covers:
- Basic access control and user authentication
- Audit trail for data access and modifications
- Basic data backup and recovery
- Minimum functional requirements for electronic records

NGS1 is sufficient for administrative clinical management software with limited clinical risk exposure.

### NGS2 — Nível de Garantia de Segurança 2

The higher certification level. Required for:
- Platforms supporting **telemedicine** under CFM Resolution 2.314/2022
- Platforms issuing **digital prescriptions** via ICP-Brasil
- Systems connected to **RNDS** (Rede Nacional de Dados em Saúde)

NGS2 adds:
- **ICP-Brasil digital signature** support (Type A1/A3 certificates)
- Stricter access controls and authentication
- Enhanced audit trails with non-repudiation
- Interoperability requirements
- Stronger cryptographic requirements for data at rest and in transit

CFM Resolution 2.314/2022 explicitly requires telemedicine platforms to support NGS2 or an equivalent legally accepted standard ([CMS Law](https://cms.law/en/int/expert-guides/cms-expert-guide-to-digital-health-apps-and-telemedicine/brazil)).

---

## Why Certification Matters

### Regulatory Compliance
- **CFM 2.314/2022** requires NGS2-equivalent security for telemedicine SRES (electronic health record systems).
- **LGPD compliance:** SBIS certification is recognized as evidence of appropriate technical security measures for sensitive health data.
- **ANVISA SaMD:** While not directly required for [[anvisa-samd]] registration, certification demonstrates conformity with clinical safety and security requirements.

### Commercial and Procurement Value
- Hospital and clinic procurement teams often require or strongly prefer certified systems.
- Public sector SUS procurement processes increasingly reference SBIS certification criteria.
- Certification differentiates established vendors from newer entrants in a fragmented market.

### Switching Cost Creation
Maintaining certification requires ongoing conformity — updates to clinical workflows, security patches, and documentation — creating operational stickiness for certified platforms.

---

## Platforms with SBIS/CFM Certification

Platforms in this wiki that have pursued or hold SBIS/CFM certification include larger EHR vendors in the hospital and outpatient markets. Notable certified or certification-pursuing platforms include:

- [[mv-sistemas]] — Hospital EHR (SOUL MV); certification standard for enterprise deployments
- [[pixeon]] — Diagnostic imaging and hospital systems; SBIS compliance for PACS/RIS/LIS
- [[iclinic]] — Outpatient SaaS; NGS1/NGS2 compliance pursued post-Afya acquisition
- [[feegow]] — Clinic management SaaS; SBIS compliance documentation
- [[amplimed]] — Clinic management; compliance documentation
- [[ninsaude]] — Outpatient EHR; actively promotes SBIS-aligned security

Smaller platforms — [[prontmed]], [[shosp]], [[easy-health]], [[hidoctor]], [[medicina-direta]], [[prodoctor]], [[consultorio-live]], [[simdoctor]], [[conclinica]] — have varying levels of formal SBIS certification; independent verification is recommended.

> Note: The SBIS maintains an updated public registry of certified products at sbis.org.br. Always verify current certification status directly, as certifications are periodically renewed.

---

## Certification and ANS / TISS

SBIS certification indirectly supports [[tiss]] compliance by validating that the security and interoperability components of clinical software meet the Component 4 (Security & Privacy) requirements of the TISS standard. Insurers and hospital groups may require certified platforms as a condition of TISS-based electronic interchange agreements.

---

## ICP-Brasil Integration

NGS2 certification requires support for **ICP-Brasil** digital certificates. ICP-Brasil (Infraestrutura de Chaves Públicas Brasileira) is the Brazilian PKI standard. Clinical software seeking NGS2 must integrate with ICP-Brasil Type A1 (software certificate) or A3 (hardware token) certificates for:
- Physician digital signatures on prescriptions and reports
- Electronic health record authentication and non-repudiation
- RNDS data submissions (see [[sus-integration]])

---

## Summary

| | NGS1 | NGS2 |
|---|---|---|
| **Use case** | Administrative / basic clinical management | Telemedicine, digital prescriptions, RNDS integration |
| **ICP-Brasil** | Not required | Required |
| **Audit trail** | Basic | Enhanced with non-repudiation |
| **CFM 2.314/2022** | Insufficient for telemedicine SRES | Required (or equivalent) |
| **LGPD evidence** | Provides baseline evidence | Stronger evidence for sensitive health data processing |

---

## See Also

- [[lgpd-health-data]] — SBIS certification as recognized LGPD compliance evidence
- [[telemedicine-regulation]] — CFM 2.314/2022 requires NGS2 for telemedicine SRES
- [[sus-integration]] — ICP-Brasil certificates required for RNDS integration
- [[tiss]] — Security Component 4 of TISS aligns with SBIS requirements
- [[anvisa-samd]] — Complementary regulatory framework for clinical software
- [[market-overview]] — Market context for EHR platform competition
