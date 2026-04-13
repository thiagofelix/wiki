# Regulatory and Compliance Framework: Importing Goods from China to Brazil

*Research compiled: June 2025. Sources include Receita Federal, ANVISA, INMETRO, Senado Federal, Banco Central do Brasil, and trade law practitioners.*

---

## Table of Contents

1. [Receita Federal — Import Taxes and Duties](#1-receita-federal--import-taxes-and-duties)
2. [ANVISA — Health, Cosmetics, and Food Products](#2-anvisa--health-cosmetics-and-food-products)
3. [INMETRO — Certification for Electronics, Toys, and Regulated Products](#3-inmetro--certification-for-electronics-toys-and-regulated-products)
4. [SISCOMEX — The Integrated Foreign Trade System](#4-siscomex--the-integrated-foreign-trade-system)
5. [Radar/SISCOMEX Habilitação — Import Authorization](#5-radarsiscomex-habilitação--import-authorization)
6. [Remessa Conforme Program — Cross-Border E-commerce](#6-remessa-conforme-program--cross-border-e-commerce)
7. [KYC/AML Requirements — Trade Intermediaries](#7-kycaml-requirements--trade-intermediaries)
8. [Câmbio — Foreign Exchange for Import Payments](#8-câmbio--foreign-exchange-for-import-payments)
9. [NF-e — Nota Fiscal Eletrônica for Imports](#9-nf-e--nota-fiscal-eletrônica-for-imports)
10. [Compliance Pitfalls, Penalties, and Risks](#10-compliance-pitfalls-penalties-and-risks)
11. [Importação por Conta e Ordem vs. Por Encomenda](#11-importação-por-conta-e-ordem-vs-por-encomenda)
12. [Recent Regulatory Changes (2024–2026)](#12-recent-regulatory-changes-20242026)

---

## 1. Receita Federal — Import Taxes and Duties

### Overview

Every commercial import into Brazil is subject to a cascading stack of federal and state taxes administered by the Receita Federal (RFB). The total effective tax burden on imported goods typically ranges from **40% to over 100%** of the CIF (Cost, Insurance, and Freight) value, depending on the product category and state of entry.

### The Tax Cascade

Taxes are computed in a specific sequence, with each successive tax building on the base that includes previously calculated taxes:

| Order | Tax | Authority | Base of Calculation | Typical Rate |
|-------|-----|-----------|---------------------|--------------|
| 1 | II (Imposto de Importação) | Federal | CIF value (valor aduaneiro) | 0–35% |
| 2 | IPI (Imposto sobre Produtos Industrializados) | Federal | CIF + II | 0–30% |
| 3 | AFRMM (maritime surcharge) | Federal | Ocean freight value | 25% (maritime only) |
| 4 | PIS-Importação | Federal | CIF value (standard) | 2.1% |
| 5 | COFINS-Importação | Federal | CIF value (standard) | 9.65% |
| 6 | SISCOMEX fee | Federal | Per declaration | R$185 + R$29.50/item |
| 7 | ICMS | State | CIF + II + IPI + PIS + COFINS + expenses ("por dentro") | 17–25% (varies by state) |

**Source:** [NOVATRADE Brazil Import Duties Guide](https://novatradebrasil.com/en/import-duties-taxes-brazil/), [Receita Federal](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/remessas-postal-e-expressa/preciso-pagar-impostos-nas-compras-internacionais/quanto-pagarei-de-imposto), [U.S. International Trade Administration](https://www.trade.gov/country-commercial-guides/brazil-import-tariffs)

### Detailed Tax Rules

#### II — Imposto de Importação
- Collected before customs clearance via DARF (Federal Tax Collection Document)
- Rate determined by the product's NCM (Nomenclatura Comum do Mercosul) code — misclassification carries penalties up to 50% of tax due
- Brazil applies zero reduced tariffs for most Mercosur partners; China receives standard MFN rates with no preferential agreement
- Range: 0% (raw materials, some inputs) to 35% (consumer goods); electronics typically 10–20%

#### IPI — Imposto sobre Produtos Industrializados
- Rate defined by the TIPI table (Tabela de Incidência do IPI)
- Range: 0–30%, inversely proportional to product "essentiality"
- Importers on the Lucro Real regime can claim IPI credits when the product is resold
- **Reform note:** IPI will be reduced to zero for most products by 2027 under the tax reform, except Manaus Free Zone-protected categories

#### PIS/COFINS-Importação
- Standard rates: 2.1% (PIS) + 9.65% (COFINS) = 11.75% combined
- Base: valor aduaneiro (for most products)
- Exceptions and differentiated rates apply to beverages (NCM chapters 21–22), tobacco (chapter 24), and certain other categories with per-unit or per-liter calculations
- Lucro Real entities can credit PIS/COFINS paid on imports against future obligations
- **STF ruling (Tema 69):** ICMS is excluded from the PIS/COFINS base — a significant taxpayer victory

#### ICMS — Imposto sobre Circulação de Mercadorias e Serviços
- State-level tax with 27 different legislative frameworks — rate depends on the **state of customs clearance**, not destination
- Key state rates: São Paulo 18%, Rio de Janeiro 20%, Minas Gerais 19%
- Calculated "por dentro" (the tax is included in its own base), making the effective rate higher than the nominal rate
  - Formula: `ICMS Base = (CIF + II + IPI + PIS + COFINS + Despesas) / (1 − ICMS rate)`
  - `ICMS = ICMS Base × ICMS rate`
- **Reform note:** ICMS will be gradually replaced by IBS (Imposto sobre Bens e Serviços) between 2029–2033

### Worked Example (Electronics to São Paulo)
Assume: FOB $10,000, freight $500, insurance $100 → CIF = $10,600 × R$5.20 = **R$55,120**

| Step | Calculation | Amount (R$) |
|------|-------------|-------------|
| II (14%) | R$55,120 × 14% | 7,717 |
| IPI (10%) | (R$55,120 + R$7,717) × 10% | 6,284 |
| PIS (2.1%) | R$55,120 × 2.1% | 1,158 |
| COFINS (9.65%) | R$55,120 × 9.65% | 5,319 |
| ICMS base (18%) | (55,120+7,717+6,284+1,158+5,319+~1,500) / (1−0.18) | ~93,900 |
| ICMS | R$93,900 × 18% | ~16,902 |
| **Total Tax** | | **~37,380** |
| **Effective Rate on CIF** | | **~67.8%** |

### Payment Mechanism
All federal taxes must be paid via DARF before customs release (desembaraço aduaneiro). ICMS is paid to the state treasury.

---

## 2. ANVISA — Health, Cosmetics, and Food Products

### Scope
ANVISA (Agência Nacional de Vigilância Sanitária) regulates imports of:
- Pharmaceuticals and drugs
- Medical devices and in vitro diagnostics
- Cosmetics, perfumes, and personal hygiene products
- Food and beverages
- Tobacco
- Chemicals and pesticides
- Cannabis-derived products (new category, 2024)

The governing regulation is **RDC nº 81/2008** (Technical Regulation for Imported Goods for Health Surveillance purposes), updated by Comunicado Importação nº 036/2024 effective August 1, 2024.

### Company-Level Requirements

Any Brazilian entity importing ANVISA-regulated products must have:

1. **Active CNPJ** with import/distribution activity registered
2. **AFE (Autorização de Funcionamento de Empresa)** from ANVISA for the relevant activity (valid 2 years, renewable) — *exception: food importers only need a municipal Alvará de Funcionamento*
3. **Responsável Técnico (RT)** — a licensed pharmacist or chemist who is legally responsible for product compliance
4. **RADAR/SISCOMEX habilitação** for import operations
5. **Product registration or notification** (product-by-product, not a blanket authorization)

**Source:** [Wilson Sons step-by-step guide](https://wilsonsons.com.br/pt-br/blog/importacao-de-produtos-regulados-pela-anvisa-passo-a-passo/), [Babi Tonhela cosmetics guide](https://babitonhela.com/blog/importar-cosmeticos-china/)

### Product Regulatory Pathways

#### Cosmetics (RDC 752/2022)
| Category | Pathway | Typical Timeline | Examples |
|----------|---------|------------------|---------|
| Grau 1 (low risk) | Notificação | 3–6 months | shampoo, lipstick, eyeshadow, nail polish |
| Grau 2 (higher risk) | Registro (full analysis) | 12+ months | hair dyes, retinoids, sunscreens SPF>30 |

**What is NOT a cosmetic (no ANVISA needed):** Makeup brushes, sponges, beauty blenders, hair clips, organizers — classified as utensils/accessories. These follow general import rules (INMETRO for electrical items, general safety standards).

#### Food Products
- Require Licença de Importação (LI) via SISCOMEX
- Municipal Alvará de Funcionamento (no AFE needed for most foods)
- Labeling must be in Portuguese; foreign-language labels require approved translation

#### Pharmaceuticals / Medical Devices
- Full product registration (Registro) required before import
- Import License (LI) per shipment required
- Foreign manufacturers often need GMP (Good Manufacturing Practices) certificates
- Clinical trial materials: governed by Law 14.874/2024 and RDC 208/2018, with 2–4 week ANVISA review windows

### Import Process (Step-by-Step)

1. Register LI (Licença de Importação) in SISCOMEX Importação
2. Create dossier in Visão Integrada (Portal Único Siscomex)
3. Attach Petição Primária using the specific subject code for importation
4. Attach required documents: LI extract, commercial invoice (original signed), Bill of Lading, DUIMP, and DDR (Declaração do Detentor do Registro) if importer ≠ registration holder
5. Link dossier to a single LI
6. Wait minimum 30 minutes for system processing (Visão Integrada ↔ PEI/Solicita)
7. Access ANVISA mailbox via Solicita system → "Concluir Peticionamento"
8. Complete electronic petition form; generate and pay GRU (Guia de Recolhimento Único)
9. Await banking confirmation → receive Comprovante de Protocolização

**Key challenge:** Municipal alvará is issued by each municipality (5,500+ municipalities in Brazil), creating significant local variation in requirements and timelines.

### 2024 Regulatory Update
**Comunicado Importação nº 036/2024** (effective August 1, 2024) introduced new administrative treatments by product category:
- New NCM codes with specific highlights for better categorization
- Revised treatments for: Alimentos, Cosméticos/perfumes/higiene, Dispositivos médicos, Medicamentos, Substâncias controladas, Cannabis products
- Importers can now select specific subcategories for finished products vs. inputs

**Source:** [Logcomex ANVISA 2024 update](https://insights.logcomex.com/noticias/industria-farmaceutica-n/novas-regras-importacao-anvisa/)

---

## 3. INMETRO — Certification for Electronics, Toys, and Regulated Products

### What is INMETRO?
INMETRO (Instituto Nacional de Metrologia, Qualidade e Tecnologia) is Brazil's national metrology and certification body. It designates which products require mandatory conformity assessment before entering the Brazilian market.

### Mandatory Certification Categories (from China)

| Product Category | Key Regulation | Notes |
|-----------------|----------------|-------|
| Toys (for under-14s) | Portaria INMETRO 302/2021 | Mandatory since Jan 1, 2022; age labeling required |
| Home appliances (refrigerators, TVs, etc.) | Varies by product | All household appliances |
| Electrical accessories (plugs, sockets, switches) | Specific portarias | Annual re-certification |
| Electronic ballasts / inductive ballasts | Specific portarias | Lighting products |
| Automotive parts (tires, brakes, glass) | Specific portarias | Safety-critical components |
| PPE (helmets, gloves) | NR standards | Occupational safety |
| Construction materials (cement, rebar) | ABNT NBR standards | Structural safety |

**Wireless/Bluetooth devices** (including toys with Bluetooth, Wi-Fi, drones under 250g, remote-controlled vehicles) additionally require **ANATEL homologação** — a separate certification from the telecom regulator.

**Source:** [INMETRO official FAQ](http://www.inmetro.gov.br/qualidade/iaac/certifique-seu-produto.asp), [NOVATRADE INMETRO guide](https://novatradebrasil.com/en/navigating-inmetro-and-anatel-regulations-for-product-importation-in-brazil/), [BRICS Certificações](https://www.brics-ocp.com.br/certificacao-de-produtos/brinquedos/)

### The Certification Process

1. **Identify the applicable Regulamento Técnico da Qualidade (RTQ)** for the product's NCM code — check via the Portal SISCOMEX or NCM consultation tool
2. **Engage an OCP (Organismo de Certificação de Produto)** — INMETRO-accredited body; the importer selects the OCP, which conducts testing and issues the certificate
3. **Submit documentation:** company registration (CNPJ/contrato social), product technical specification
4. **Laboratory testing:** physical, electrical, mechanical, toxicological tests (for toys: non-toxicity, flammability, small parts, age labeling)
5. **Factory audit** (in some cases, especially for ongoing compliance monitoring; auditor may travel to China)
6. **Certificate issuance** by OCP → **Registration in INMETRO system**
7. **INMETRO Conformity Seal** applied to packaging — mandatory for all certified products

**Timeline:** 3–6 months average; technical/electrical products can take longer.

**Cost variables:** OCP selection (competitive; negotiated directly with OCP), laboratory fees, potential factory audit travel.

### Operational Requirements
- Certification is **per importer + per product model** — not transferable between companies
- Annual maintenance via sample inspection and factory audits (1–2 times/year depending on category)
- INMETRO Seal must appear on product packaging; Portuguese labeling mandatory (user manuals, safety warnings)
- INMETRO certification is a **prerequisite for the Licença de Importação (LI)** — without it, LI cannot be granted

### Impact on Business Model
For a business acting as an import intermediary (conta e ordem or encomenda), the certification must be held by either the **importer of record** or the **client** (adquirente). Misunderstanding this can block the LI for the entire shipment.

---

## 4. SISCOMEX — The Integrated Foreign Trade System

### What is SISCOMEX?
SISCOMEX (Sistema Integrado de Comércio Exterior) was established by Decree 660 of September 25, 1992, as Brazil's unified electronic platform for all import/export operations. It transformed a paper-based, multi-agency process into a single electronic flow.

**Administered by three core entities:**
- Receita Federal do Brasil (RFB) — customs, tax, and fiscal control
- Secretaria de Comércio Exterior (SECEX/MDIC) — trade policy and administrative licensing
- Banco Central do Brasil (BACEN) — financial and forex aspects

**Source:** [Receita Federal SISCOMEX page](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/importacao-e-exportacao/sistema-integrado-de-comercio-exterior-siscomex), [Gett Tecnologia SISCOMEX overview](https://gett.com.br/como-funciona-o-siscomex-e-qual-a-sua-importancia-no-comercio-exterior/)

### Key Functions

| Function | Description |
|----------|-------------|
| Declaração de Importação (DI) / DUIMP | Electronic import declaration (DI being phased out; DUIMP replacing it) |
| Licença de Importação (LI) | Import license for controlled products |
| LPCO | Licenses, Permits, Certificates, and Other Documents (new module in Portal Único) |
| Risk parametrization | Assigns import channels: Green (auto-release), Yellow (document check), Red (physical + document check), Grey (value investigation) |
| Anuentes integration | Connects to ANVISA, MAPA, IBAMA, Army, and other regulatory bodies |
| Exchange control | Links to Banco Central for forex settlement data |

### Who Must Use SISCOMEX?
All commercial importers must use SISCOMEX. This includes:
- Importers (directly or via customs broker/despachante aduaneiro)
- Exporters
- Cargo agents and freight forwarders (transportadores)
- Warehouse operators at bonded zones
- Customs brokers (despachantes aduaneiros)

A customs broker (despachante aduaneiro) must be engaged for the actual filing of declarations; companies cannot file declarations themselves without specific accreditation.

### Transition to Portal Único / DUIMP
The legacy SISCOMEX LI/DI system is being phased out. The **DUIMP (Declaração Única de Importação)** on the Portal Único de Comércio Exterior is the replacement. This transition is covered in detail in [Section 12 — Recent Regulatory Changes](#12-recent-regulatory-changes-20242026).

---

## 5. Radar/SISCOMEX Habilitação — Import Authorization

### What is RADAR?
RADAR (Registro e Rastreamento da Atuação dos Intervenientes Aduaneiros) is the authorization granted by the Receita Federal that allows a legal entity or individual to operate in SISCOMEX. Without RADAR, a company cannot register import declarations, regardless of its CNPJ or business activity.

**RADAR is a prerequisite for all commercial imports.** No exceptions.

**Source:** [Conexos RADAR guide](https://conexoscloud.com.br/radar-siscomex-como-habilitacao/), [WM Trading RADAR overview](https://www.wmtrading.com.br/blog/radar-siscomex/)

### RADAR Modalities

| Modality | Import Limit (per semester) | Export Limit | Target Profile |
|----------|----------------------------|--------------|----------------|
| **Expressa** | Up to USD 50,000 | Unlimited | Public companies (SA de capital aberto), SOEs, MEIs; automatic online approval |
| **Limitada I** | Up to USD 50,000 | Unlimited | Small/new companies starting international operations |
| **Limitada II** | Up to USD 150,000 | Unlimited | Medium-sized companies with demonstrated capacity |
| **Ilimitada** | Unlimited | Unlimited | Companies with proven financial capacity and import experience |
| **Pessoa Física** | Limited to IR declaration values | Unlimited | Individuals importing for personal use |

**Key operational note:** When the semester limit is reached on a Limitada modality, the system blocks further registrations until a "Revisão de Estimativa" (limit review/upgrade request) is processed.

### Habilitação Process

**For Expressa:**
- Online application via Portal SISCOMEX
- Automatic deferral (no human review)

**For Limitada and Ilimitada:**
1. Analyze eligibility and gather documentation
2. Collect required documents (varies by modality):
   - Contrato social / corporate acts
   - Financial statements demonstrating economic capacity (Portaria COANA 72/2020 / IN RFB 1984/2020)
   - Tax compliance certificates (Certidões Negativas)
   - Bank statements
   - DTE (Domicílio Tributário Eletrônico) — mandatory for habilitação
3. Formalize request online (Portal SISCOMEX)
4. Schedule appointment at Receita Federal regional office (Limitada/Ilimitada only)
5. Present physical documents; obtain protocol number
6. RFB auditor review; typical approval: **up to 10 business days** if documentation is complete

### RADAR for Import Intermediaries (Conta e Ordem)
In **importação por conta e ordem** operations, **both the importer (trading) and the adquirente (client)** must be RADAR-habilitados. The client's RADAR must specifically be configured to allow conta e ordem operations. This is a common compliance gap.

---

## 6. Remessa Conforme Program — Cross-Border E-commerce

### Program Overview
**Programa Remessa Conforme (PRC)** was created by the Receita Federal to regulate cross-border e-commerce. It is a voluntary compliance certification for international e-commerce platforms that commit to:
- Accurate, pre-arrival declaration of shipment data (value, contents, CPF of buyer) to Receita Federal
- Upfront collection and remittance of import taxes at point of sale
- Working with licensed carriers/logistics operators

**Source:** [Receita Federal PRC official page](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/remessas-postal-e-expressa/programa-remessa-conforme-o-que-e-como-funciona), [SERPRO PRC award article](https://www.serpro.gov.br/menu/noticias/noticias-2025/remessa-conforme-premiacao-internacional)

### Current Certified Platforms (Major)
AliExpress, Shein, Shopee, Temu, Amazon Brasil, Mercado Livre. Combined, these represent the vast majority of international small-parcel volume entering Brazil.

### Tax Rules (Effective August 1, 2024)

The prior isenção (exemption) for purchases under USD 50 was **eliminated**. Current rules:

| Buyer scenario | Purchase value | Import Tax (II) rate | Discount |
|----------------|---------------|---------------------|----------|
| Site **certified** in PRC | Up to USD 50 | **20%** | None |
| Site **certified** in PRC | USD 50.01–3,000 | **60%** | USD 20 off the tax bill |
| Site **NOT certified** in PRC | Any value | **60%** | None |

In addition, **ICMS applies in all cases:**
- Most states: 17% (base rate)
- Since April 1, 2025: some states raised to 20%

**How taxes are collected:** For PRC-certified platforms, taxes are collected at checkout. The platform remits to Correios/express carriers, who forward to Receita Federal. Packages receive "green channel" treatment with faster customs processing.

**Legal basis:** Medida Provisória 1.236/2024 and Portaria MF 1.086 (published July 2024); IN RFB 1.737 (Portaria COANA 130/23 for display requirements).

### Platform Requirements to Join PRC
1. Present complete documentation to Receita Federal
2. Sign compliance commitment
3. Ensure logistics partners are licensed and familiar with PRC operations
4. Send pre-arrival data electronically (before physical arrival in Brazil)
5. Display clearly on each product page: origin (imported), total price breakdown (product + international freight + insurance + II + ICMS + other charges)
6. Operate with full tax transparency; errors/omissions → sanctions up to program exclusion

### Significance for a Trade Business
Any business building a platform or marketplace connecting Brazilian buyers with Chinese sellers must understand whether it qualifies/needs to qualify for PRC. **Operating without PRC certification while facilitating cross-border micro-shipments means customers pay 60% II (instead of 20%) and face slower customs processing.** PRC certification is now effectively a competitive requirement.

The Receita Federal can conduct **5-year retroactive review (revisão aduaneira)** of prior shipments that were not properly taxed — a significant liability for platforms that facilitated non-compliant imports.

---

## 7. KYC/AML Requirements — Trade Intermediaries

### Legal Framework

Brazil's AML/CFT framework is anchored by:
- **Lei 9.613/1998** (Anti-Money Laundering Law) — establishes COAF and defines reporting entities
- **Lei 12.683/2012** — expanded scope to non-financial entities (real estate, art, luxury goods, trade intermediaries)
- **Banco Central Circular 3.978/2020** — requires risk-based approach for financial institutions
- **CMN Resolution 29/2017** and **Resolution 25/2019** — updated KYC/CDD requirements

**Source:** [Sanctions.io Brazil AML guide](https://www.sanctions.io/blog/aml-compliance-guidelines-brazil), [AML Watcher Brazil](https://amlwatcher.com/our-coverage/brazil/), [Arctic Intelligence Brazil](https://arctic-intelligence.com/countries/compliance-brazil)

### Who is a Regulated Entity in Foreign Trade Context?
While financial institutions bear the heaviest AML burden, import intermediaries (trading companies, customs brokers, logistics operators) face compliance obligations under the expanded framework. **COAF regulates entities not supervised by another specific authority.**

Key obligations for trade intermediaries:

| Obligation | Detail |
|------------|--------|
| **Customer Identification (KYC)** | Verify identity of clients (corporate and individual), including beneficial owners |
| **Customer Due Diligence (CDD)** | Understand the purpose and nature of the business relationship |
| **Enhanced Due Diligence (EDD)** | Required for high-risk clients: PEPs (Politically Exposed Persons), entities in sanctioned regions, unusual transaction patterns |
| **Transaction Monitoring** | Implement systems to detect suspicious patterns |
| **Suspicious Activity Reporting (SAR)** | Report to COAF within 24 hours of identifying suspicious transactions |
| **Large Transaction Reporting** | Transactions ≥ R$10,000 for certain account types; R$100,000 for foreign accounts |
| **Record Keeping** | Maintain customer identification, transaction records, and due diligence documentation for minimum 5 years |
| **PEP Screening** | Screen all customers against PEP lists and international sanctions lists |

### Specific Risks in China-Brazil Trade
- **Subfaturamento (undervaluation):** A common evasion technique in China-Brazil trade. When an intermediary facilitates shipments with declared values lower than actual transaction values, it may be complicit in tax evasion and AML violations
- **Shell company exporters:** Chinese suppliers operating through opaque corporate structures require enhanced due diligence
- **Cash-heavy operations:** Any cross-border arrangement involving undocumented cash flows is a red flag
- **Sanctions risk:** Chinese entities on U.S. or EU sanctions lists can create compliance exposure

### Practical Compliance Program for a Trade Intermediary

1. **Internal policies and procedures:** Document KYC standards, risk appetite, escalation paths
2. **Client onboarding:** CNPJ verification, corporate structure mapping, beneficial ownership identification
3. **Ongoing monitoring:** Flag unusual order values, rapid changes in purchase volumes, inconsistent product/value combinations
4. **Supplier KYC:** Verify Chinese supplier legitimacy via Alibaba/Made-in-China trade histories, certifications, factory audits
5. **AML officer:** Designate a responsible compliance officer
6. **Training:** Regular staff training on recognizing suspicious patterns
7. **COAF registration:** Register with COAF if not supervised by another authority

---

## 8. Câmbio — Foreign Exchange for Import Payments

### Governing Law
The **Nova Lei Cambial (Lei 14.286/2021)** entered into force on December 31, 2022, modernizing Brazil's foreign exchange framework — replacing a patchwork of over 40 instruments, some dating to the 1930s. The Banco Central do Brasil implemented this via **Resoluções BCB 277–282 (December 31, 2022)**.

**Source:** [Pinheiro Neto legal analysis](https://www.pinheironeto.com.br/conhecimento-juridico/artigo/nova-lei-cambial-e-dos-capitais-internacionais-entra-em-vigor-e-autoridades-monetarias-publicam-a-sua-regulamentacao), [Business2Gether nova lei cambial overview](https://business2gether.com/novo-marco-cambial/), [Laws of Brazil summary](https://lawsofbrazil.com/brazil-has-a-new-foreign-exchange-law/)

### Key Rules for Importers

#### Payment Timing
- Import payments may be made **up to 360 days before** the expected shipment date (antecipação de pagamento)
- Standard commercial terms: payment within 360 days of customs clearance
- **Imports financed over 360 days** with value ≥ USD 500,000 must be registered with the Banco Central
- **Imports financed over 180 days** with value ≥ USD 500,000 require Banco Central information reporting

#### Exchange Contracting
- No fixed-format contract required (eliminated by Lei 14.286/2021)
- Exchange operations must still contain minimum required data and be registered in Banco Central systems
- **Operations ≤ USD 50,000:** Settlement data can be reported to BCB by the 5th of the following month
- **Operations > USD 50,000:** Same-day reporting to BCB required
- The **enquadramento cambial (forex classification code)** is now the importer's responsibility (previously the bank's)

#### Authorized Channels for Payment
- Any bank or financial institution authorized by BCB to operate in the forex market
- **Payment institutions (IPs)** are now authorized for electronic forex operations up to specific limits
- International credit cards: usable for imports up to USD 50,000 equivalent

#### Currency Flexibility
- Import payments can be made in **any currency**, not just the currency of the Import Declaration
- Parity between currencies must reflect international market rates
- Imports can be paid in **Brazilian Reais** to a non-resident account maintained in Brazil (for the legitimate foreign creditor)

#### Forex Compliance (Compliance Cambial)
Best practices required by **Lei 14.286/2021** and BCB Circular 3.978/2020:
- Correct classification of forex operation nature (nature code selection)
- Supporting documentation: contracts, commercial invoices, payment receipts, SISCOMEX registration
- 10-year document retention for all forex transactions
- AML/CFT controls (the law explicitly requires authorized forex dealers to maintain AML/CFT programs)

#### Stablecoins and Crypto (November 2025 Update)
**BCB Resoluções 519, 520, 521 (November 2025)** brought foreign-currency-referenced stablecoins and virtual asset international transfers within the BCB's regulatory perimeter. Stablecoin-based import payments are now subject to the same forex reporting and AML rules as bank transfers.

**Source:** [Instituto Aduaneiro (IPDA) analysis](https://institutoaduaneiro.com.br/contratos-de-cambio-novas-tecnologias-e-a-comprovacao-de-pagamento-no-comercio-exterior/)

---

## 9. NF-e — Nota Fiscal Eletrônica for Imports

### Legal Requirement
Emitting a Nota Fiscal Eletrônica (NF-e) upon customs clearance of imported goods is **mandatory** for all commercial importers, regardless of their tax regime, per **Protocolo ICMS 85/2010** (effective December 1, 2010). The NF-e must be emitted before the goods are removed from the customs facility (recinto alfandegado).

**Source:** [GSF Soluções NF-e import guide](https://gsfsolucoes.com.br/nota-fiscal-eletronica-produtos-importados/), [Fazcomex NF import guide](https://www.fazcomex.com.br/importacao/nota-fiscal-de-importacao/)

### Who Issues the NF-e
The **importer of record** is always responsible for issuing the NF-e, regardless of the import modality:
- Direct import: the importing company issues one NF-e for the goods entering its stock
- Conta e ordem: the trading company (importer) issues the NF-e of entry; then issues a second NF-e to the adquirente (client) representing the transfer of goods
- Por encomenda: the trading company issues the NF-e to itself (as owner) and then an NF-e of sale to the encomendante

### Required Data Fields

| Field | Content |
|-------|---------|
| **Tipo de Operação** | Import (entry) |
| **CFOP** | 3.101 (purchase for industrialization), 3.102 (purchase for resale), 3.127 (purchase for use/consumption), 3.949 (conta e ordem entry) |
| **NCM** | Product's 8-digit Mercosur code |
| **Valor Aduaneiro** | CIF value (FOB + freight + insurance) |
| **Número da DI / DUIMP** | Mandatory reference to the customs declaration |
| **Impostos** | II, IPI, PIS, COFINS, ICMS values and rates explicitly stated |
| **Fornecedor** | Name and country of the foreign exporter |
| **CST (Código de Situação Tributária)** | Origin code and tax treatment applied |
| **DANFE** | Physical auxiliary document that must accompany the cargo during domestic transport |

### Valuation
The NF-e is always issued **in Brazilian Reais (R$)**, converted at the SISCOMEX exchange rate on the date of the Import Declaration registration. All amounts must match the DI/DUIMP.

### Mandatory Supporting Documents for NF-e Issuance
1. DI or DUIMP extract from SISCOMEX
2. Comprovante de Importação (CI) — issued after customs release
3. ICMS payment receipt or ICMS exemption certificate
4. Bill of Lading (BL) or AWB
5. Commercial Invoice (fatura comercial / invoice)
6. Packing List
7. Tax payment worksheets (espelho da NF)

### DANFE
The DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) is the printed representation of the NF-e that must accompany all goods from the port/airport to the importer's premises. Without it, goods cannot be transported domestically.

---

## 10. Compliance Pitfalls, Penalties, and Risks

### Most Common Compliance Failures

| Failure | Regulatory Risk | Consequence |
|---------|----------------|-------------|
| Incorrect NCM classification | Tax underpayment + fine | 50% of II due; forced reclassification; re-export possible |
| Undervaluation (subvaloração) | Tax fraud investigation | 100% fine on value difference + criminal liability (2–5 years prison) |
| Invoice undervaluation (subfaturamento) | Criminal charge (Lei 8.137/90, Art. 1) | 100% fine + imprisonment 2–5 years for administrators |
| INMETRO-required product without certification | Goods seized and destroyed | Cargo detention, destruction, import prohibition |
| ANVISA-regulated product without AFE/notification | Sanitary infraction | Goods seized, fines, operator liability |
| LI (Licença de Importação) obtained after embarque | Procedural violation | 30% fine on valor aduaneiro (minimum R$500) |
| NF-e not issued or issued with errors | State tax violation | R$10,000–R$20,000 per declaration (2026 UPF rules) |
| RADAR expired or wrong modality | Import halt | Unable to register DI/DUIMP until resolved |
| Non-payment of forex within required timeframe | BCB fine | Fine calculated on the value of the delayed payment |
| Incorrect enquadramento cambial | BCB/RFB violation | Administrative fine + potential money laundering suspicion |

**Source:** [Receita Federal penalty framework](https://turbocargo.com.br/noticias/consultoria/receita-federal-atualiza-quadro-de-multas-na-importacao), [DB Fazolo on subfaturamento crime](https://dbfadvocacia.com/subfaturamento-na-importacao-consequencias-penais/), [Legale on subvaloração](https://legale.com.br/blog/subvaloracao-x-subfaturamento-o-crime-tributario-e-a-defesa/)

### 2026 Penalty Update — New Fine for Inaccurate Declarations
Under **Lei Complementar 214/2025 (Art. 341-G, XIX)**, inaccurate or incomplete information in import declarations carries:
- **Standard fine:** 100 UPF = **R$20,000** per declaration (2026 UPF = R$200)
- **Minimum (floor):** 50 UPF = R$10,000
- **Maximum (ceiling):** 1% of the declared transaction value
- **Recidivism:** +50% if same infraction recurs within 3 years (same CNPJ base, including subsidiaries)
- **Note:** NCM classification errors alone do not trigger automatic fines if product description is sufficient for fiscal analysis

### Customs Inspection Channels
SISCOMEX automatically assigns every import declaration to a risk channel:
- **Verde (Green):** Automated release — no physical inspection
- **Amarelo (Yellow):** Document review only
- **Vermelho (Red):** Physical inspection + document review
- **Cinza (Grey):** Value investigation — most serious; used when subfaturamento suspected

Importers repeatedly flagged for errors or discrepancies will be systematically channeled to Red/Grey.

### Special Risks in China-Brazil Trade
1. **Chinese New Year / national holidays:** Plan inventory to avoid shipments that arrive during port congestion
2. **Port backlogs:** Armazenagem (port storage) fees accumulate rapidly and can exceed the value of small shipments
3. **Supplier certification claims:** Chinese suppliers frequently claim product certifications they do not actually hold — always verify INMETRO/ANATEL certificates independently via official portals before import
4. **Mislabeled products:** ANVISA and INMETRO may reject goods where Portuguese labeling is absent or incorrect, even if product is otherwise compliant
5. **"Gray channel" scrutiny on Chinese imports:** Goods from China receive elevated scrutiny due to historical undervaluation patterns; robust pricing documentation (purchase contracts, price lists, supplier invoices showing actual market prices) is essential

---

## 11. Importação por Conta e Ordem vs. Por Encomenda

### Legal Framework
Both modalities are governed by **IN RFB 1.861/2018** (as amended by IN 1.937/2020 and IN 2.101/2022) and **Portaria COANA 25/2019** (which governs the registration and information-sharing requirements in SISCOMEX for these operations). They were originally introduced by **Medida Provisória 2.158-35/2001**.

**Source:** [IN RFB 1.861 full text](https://www.garciaemoreno.com.br/legislacao/18628/in_rfb_no_1.861_requisitos_nas_opera_c_ies_de_importa_c_eo_por_conta_e_ordem_de_terceiros_e_por_encomenda.html), [Importe Melhor detailed comparison](https://importemelhor.com.br/importacao-por-conta-e-ordem-vs-importacao-por-encomenda/), [Paulicon Contábil analysis](https://paulicon.com.br/2024/02/06/a-importacao-por-encomenda-e-seus-efeitos/)

### Side-by-Side Comparison

| Dimension | Importação por Conta e Ordem | Importação por Encomenda |
|-----------|------------------------------|--------------------------|
| **Legal nature** | Service contract: trading provides customs clearance service | Commercial transaction: trading buys abroad, then sells domestically |
| **Who owns the goods** | Adquirente (client) owns goods from purchase moment abroad | Importadora (trading) owns goods until sale to encomendante |
| **Who pays the supplier** | Adquirente (client) — or trading on client's behalf | Trading, using **its own financial resources** |
| **Who is the taxpayer (sujeito passivo)** | Adquirente is the taxpayer for II, IPI, PIS/COFINS | Importadora is the taxpayer for all import duties |
| **RADAR requirements** | BOTH importer AND adquirente must be RADAR-habilitados | Only the importadora needs RADAR |
| **DI/DUIMP identification** | Adquirente's CNPJ must be identified in the declaration | Only importadora appears |
| **PIS/COFINS concentrated rates** | Adquirente collects at concentrated rate on onward sale | Importadora collects at concentrated rate on sale to encomendante |
| **PIS/COFINS credit** | Adquirente claims import credit | Importadora claims import credit |
| **Financial risk** | Lower for trading (doesn't use own funds) | Higher for trading (capital tied up until resale) |
| **Governing contract** | Service contract (mandatory, must be filed) | Purchase + resale contract |
| **IPI on transfer** | IPI applies on exit from importer to adquirente (importer is equated to industrial) | IPI applies on sale to encomendante |
| **Key NF-e flow** | Entry NF (CFOP 3.949 to importer) + exit NF (CFOP 5.949/6.949 to adquirente) | Entry NF + sale NF to encomendante |
| **Liability if misclassified** | Substantial: wrong characterization = tax audit, back-taxes, fines | Same; determines who owes what taxes |

### Why the Distinction Matters
**Misclassifying the operation** (e.g., calling a conta e ordem operation an encomenda, or vice versa) is one of the most frequently audited areas in Brazilian import compliance. The Receita Federal uses the DI/DUIMP data, the money trail (who paid the foreign supplier), and contractual terms to determine the real nature of the transaction.

**Practical signal:** If the **client's money** flows to pay the Chinese supplier (directly or via the trading), it's conta e ordem. If the **trading's own capital** is used, it's encomenda.

### Which Modality for an Import Intermediary Startup?

**Conta e Ordem** is generally preferred when:
- The business acts as a service provider/platform with thin capital
- Clients already have RADAR and want to maintain ownership and fiscal credit
- Regulatory burden concentration on the client is acceptable

**Encomenda** is preferred when:
- The trading maintains stock and sells domestically
- The trading wants to control the full commercial relationship
- The client does not have or want RADAR habilitação

---

## 12. Recent Regulatory Changes (2024–2026)

### A. DUIMP / Portal Único Migration (2024–2025)

The most significant operational change in recent years is the mandatory migration from the old SISCOMEX LI/DI system to the **DUIMP (Declaração Única de Importação)** on the **Portal Único de Comércio Exterior**.

**Timeline:**
- **October 2024:** DUIMP becomes mandatory for maritime imports without licensing under special regimes (RECOF, etc.) — gradual start
- **First half 2025:** Maritime imports under drawback, admissão temporária, RECOF, Repetro; air cargo imports begin migration; anuentes ANVISA, MAPA, Army migrate to LPCO module
- **December 2025:** Target: 100% of all imports on DUIMP; DI system fully decommissioned

**Source:** [Siscomex official migration schedule](https://www.gov.br/siscomex/pt-br/comunicados/cronograma-migracao-das-importacoes-para-o-portal-unico-primeiro-semestre-de-2025), [Fazcomex migration update](https://www.fazcomex.com.br/npi/migracao-das-importacoes-para-o-portal-Unico-cronograma-primeiro-semestre-de-2025/)

**What changes with DUIMP:**
- **Módulo Catálogo de Produtos:** Importers must pre-register all products with detailed attributes (composition, dimensions, certifications, images) before importing — data is reused across declarations
- **Single-window "Canal Único":** All government agencies parametrize their channel assignments (green/yellow/red) through one integrated system — greater transparency, potentially faster release
- **Integration with LPCO:** Licenses, permits, certificates from ANVISA/MAPA/Army/Exército are managed in the same portal
- **DI legacy:** The old DI format simply cannot accommodate the tax reform (CBS/IBS data fields), making the DUIMP transition legally mandated by 2026

### B. Tax Reform — CBS and IBS (2024–2033 Transition)

**Emenda Constitucional 132/2023** and **Lei Complementar 214/2025** enacted Brazil's most significant tax reform in decades. For imports:

| Existing Tax | Replacement | Timeline |
|-------------|-------------|----------|
| PIS + COFINS (federal) | CBS (Contribuição sobre Bens e Serviços) | Testing 2026; operational transition 2027+ |
| ICMS (state) + ISS (municipal) | IBS (Imposto sobre Bens e Serviços) | Gradual 2029–2033 |
| IPI | Reduced to zero for most products by 2027; remains for Manaus FTZ exclusives | |

**Combined CBS + IBS rate** expected near **28%** (reference rates defined under PLP 68/2024), replacing the current cascading stack.

**Key principles of new system:**
- **Non-cumulative (IVA logic):** Credits can be taken for IBS/CBS paid on imports and used to offset taxes on output sales
- **Destination principle:** Tax flows to the state/municipality where the buyer is located (not where customs clearance happens) — a major shift from current ICMS rules
- **Art. 63, LC 214/2025:** IBS and CBS apply to ALL imports, regardless of importer type, without exception for non-economic entities

**Cash flow warning:** Even with non-cumulative credit, **CBS and IBS on imports are paid at customs clearance** — credit is recovered later through the tax apportionment mechanism. This creates working capital pressure for importers.

**Source:** [Blog Mainô reforma tributária imports](https://blog.maino.com.br/reforma-tributaria-nas-importacoes/), [SimTax IBS CBS imports](https://simtax.com.br/ibs-cbs-na-importacao/)

### C. Remessa Conforme — August 2024 Tax Change

Effective **August 1, 2024** (Medida Provisória 1.236/2024 + Portaria MF 1.086):
- Eliminated the prior zero-II treatment for purchases ≤ USD 50 from PRC-certified platforms
- Instituted the 20% II rate for ≤ USD 50 on certified platforms
- Maintained 60% II for non-certified platforms and values > USD 50 (with USD 20 discount for certified platforms)
- Added ICMS on all international small parcel purchases (some states at 17%, others 20% since April 2025)

### D. ANVISA Administrative Treatment Update (August 2024)

Comunicado Importação nº 036/2024 restructured NCM classification and administrative treatment codes for ANVISA-regulated products. New treatments effective August 1, 2024 across: pharmaceuticals, medical devices, cosmetics, food, controlled substances, and cannabis products.

### E. New Foreign Trade Legal Framework (PL 4.423/2024)

Approved by the Brazilian Senate in December 2025 and sent to the Câmara dos Deputados:
- Replaces Decreto-Lei 37/1966 (the 60-year-old foundation of Brazilian customs law)
- Mandates Portal Único use for all import/export data exchange
- Requires government to make all trade rules available in Portuguese AND English
- Authorizes AI-based risk management for customs enforcement
- Creates a structured channel for denuncias (tips/complaints) about illicit imports
- Establishes binding pre-rulings (solução antecipada vinculante) — importers can request formal advance determination of how their goods will be classified/treated

### F. BCB Crypto/Stablecoin Forex (November 2025)

Resoluções BCB 519, 520, and 521 (November 2025) brought crypto and stablecoin-based international payments within the BCB's formal regulatory perimeter, with the same AML/CFT and reporting obligations as bank transfers. This affects any fintech or platform seeking to use stablecoins for import payment settlement.

### G. New Import Declaration Fine Structure (LC 214/2025)

The new fine for inaccurate import declarations (Art. 341-G, XIX of LC 214/2025) replaces the prior Art. 711 framework:
- R$20,000 standard fine per declaration (100 UPF at 2026 rates)
- R$10,000 floor; 1% of transaction value ceiling
- 50% surcharge for recidivism within 3 years

---

## Summary: Regulatory Burden Matrix

| Business Activity | Key Regulators | Primary Compliance Items |
|-------------------|---------------|--------------------------|
| Commercial importer of any goods | Receita Federal | RADAR habilitação, DUIMP/DI filing, tax payments, NF-e issuance |
| Importing health/cosmetics/food | ANVISA + Receita Federal | AFE, RT, product notification/registration, LI per shipment |
| Importing electronics/toys/appliances | INMETRO + ANATEL + Receita Federal | Mandatory certification (3–6 months), ANATEL for wireless |
| Cross-border e-commerce platform | Receita Federal (PRC) + State tax authorities | PRC certification, real-time data transmission, upfront tax collection |
| Import intermediary (trading) | Receita Federal, BCB, COAF | IN 1.861/2018 compliance, dual RADAR (for conta e ordem), AML program, forex compliance |
| Any entity making forex payments | BCB, Receita Federal | Nova Lei Cambial (Lei 14.286/2021), BCB classification codes, 10-year document retention |

---

## Key Contacts and Official Resources

| Entity | Portal | Key Function |
|--------|--------|--------------|
| Receita Federal | gov.br/receitafederal | DUIMP, RADAR, tax rules, penalties |
| ANVISA | gov.br/anvisa | AFE, product registration, LI for health products |
| INMETRO | inmetro.gov.br | Mandatory product certification programs |
| Portal Único SISCOMEX | gov.br/siscomex | DUIMP filing, LPCO, anuentes integration |
| Banco Central | bcb.gov.br | Forex regulations, BCB resolutions |
| COAF | gov.br/coaf | AML reporting, STR submission |
| SECEX/MDIC | gov.br/mdic | Trade policy, antidumping, tariff ex-tarifário |

---

*This document reflects regulations and guidance as of mid-2025 through early 2026. The tax reform (IBS/CBS), DUIMP migration, and Remessa Conforme rules are in active evolution — monitoring of Receita Federal and BCB publications is essential for ongoing compliance.*
