---
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
  }
  section.lead h1 {
    font-size: 2.2em;
    color: #1b4332;
  }
  section.lead h2 {
    color: #40916c;
    font-weight: 400;
  }
  h1 { color: #1b4332; }
  h2 { color: #40916c; }
  h3 { color: #2d6a4f; }
  table { font-size: 0.8em; }
  blockquote { border-left: 4px solid #40916c; padding-left: 16px; color: #555; }
  strong { color: #1b4332; }
  .columns { display: flex; gap: 2em; }
  .col { flex: 1; }
  code { background: #f0f7f4; color: #1b4332; }
---

<!-- _class: lead -->

# Modalidades de Importação no Brasil

## Conta e Ordem · Encomenda · Conta Própria

*Guia prático para trading companies e importadores*
*Abril 2026*

---

# As 3 Modalidades

Reguladas pela **IN RFB 1.861/2018** (alterada por IN 1.937/2020 e IN 2.101/2022)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   1. CONTA E ORDEM        Serviço aduaneiro                 │
│      Trading = prestador de serviço                          │
│      Cliente = dono da mercadoria                            │
│                                                              │
│   2. ENCOMENDA             Compra + revenda                  │
│      Trading = dona da mercadoria até revenda                │
│      Cliente = encomendante                                  │
│                                                              │
│   3. CONTA PRÓPRIA         Importação direta                 │
│      Trading importa e revende livremente                    │
│      Modelo mais simples, maior capital necessário           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

# Conta e Ordem — Visão Geral

### Trading como **prestadora de serviço**

```
 Fornecedor      Trading         Cliente
  (China)      (importador)    (adquirente)
     │               │               │
     │◄──────────────│  Contrato de  │
     │   Pagamento   │   serviço     │
     │   (em nome    │◄──────────────│
     │   do cliente) │               │
     │               │               │
     │──── Mercadoria ────►│         │
     │               │  NF saída ───►│
     │               │  (5.949/6.949)│
```

- **Propriedade**: do **cliente** desde a compra no exterior
- **Quem paga o fornecedor**: o cliente (ou trading em nome dele)
- **Contrato**: de prestação de serviço (arquivo obrigatório)
- **CNPJ na DI/DUIMP**: aparece o CNPJ do adquirente

---

# Encomenda — Visão Geral

### Trading como **compradora e revendedora**

```
 Fornecedor      Trading         Cliente
  (China)      (importador)   (encomendante)
     │               │               │
     │◄──────────────│               │
     │  Pagamento    │               │
     │  (capital     │               │
     │   próprio)    │               │
     │               │               │
     │──── Mercadoria ────►│         │
     │               │  NF venda ───►│
     │               │  (revenda)    │
```

- **Propriedade**: da **trading** até a revenda doméstica
- **Quem paga o fornecedor**: a trading, com **recursos próprios**
- **Contrato**: de compra e revenda
- **CNPJ na DI/DUIMP**: apenas a trading

---

# Comparação Lado a Lado

| Dimensão | Conta e Ordem | Encomenda |
|----------|--------------|-----------|
| **Natureza legal** | Serviço aduaneiro | Compra + revenda |
| **Propriedade dos bens** | **Cliente** (adquirente) | **Trading** até revenda |
| **Quem paga fornecedor** | Cliente (ou trading em nome) | Trading (capital próprio) |
| **Sujeito passivo (impostos)** | Adquirente | Trading |
| **Requisitos RADAR** | **Ambos** (trading + cliente) | Apenas trading |
| **Identificação na DI** | CNPJ do adquirente | Apenas trading |
| **Crédito PIS/COFINS** | Adquirente reivindica | Trading reivindica |
| **Risco financeiro trading** | Menor | Maior (capital vinculado) |
| **Fluxo NF-e** | Entrada 3.949 + Saída 5.949/6.949 | Entrada + NF de venda |

---

# Quando Usar Cada Uma?

<div class="columns">
<div class="col">

### Conta e Ordem

- Trading funciona como **plataforma/serviço** com capital reduzido
- Cliente já tem **RADAR habilitado**
- Cliente quer **propriedade dos créditos fiscais** (PIS/COFINS)
- Carga regulatória no cliente é aceitável
- Trading quer **menor risco financeiro**

</div>
<div class="col">

### Encomenda

- Trading mantém **estoque próprio** e revende domesticamente
- Trading quer **controlar o relacionamento comercial** completo
- Cliente **não tem ou não quer** habilitação RADAR
- Trading tem **capital disponível** para financiar a operação
- Maior autonomia na precificação

</div>
</div>

---

# Conta Própria — A Terceira Via

### O modelo mais simples, mas mais intensivo em capital

| Aspecto | Detalhe |
|---------|---------|
| **Como funciona** | Trading importa por iniciativa própria e revende livremente |
| **Propriedade** | Trading é dona em todo o ciclo |
| **Capital** | Compromisso pleno — financia toda a operação |
| **RADAR** | Apenas trading |
| **Vantagem** | Simplicidade operacional · sem contrato prévio com cliente |
| **Desvantagem** | Risco de estoque · capital intensivo |

> Ideal para trading companies que trabalham com **produtos de giro rápido** e têm capacidade financeira para bancar o estoque.

---

# RADAR: Quem Precisa do Quê?

| Modalidade | Trading | Cliente |
|-----------|---------|---------|
| **Conta e Ordem** | RADAR obrigatório | **RADAR obrigatório** (configurado p/ conta e ordem) |
| **Encomenda** | RADAR obrigatório | Não precisa |
| **Conta Própria** | RADAR obrigatório | Não precisa |

### Modalidades RADAR

| Tipo | Limite semestral | Perfil |
|------|-----------------|--------|
| Expressa | USD 50.000 | MEIs, empresas públicas |
| Limitada I | USD 50.000 | Empresas pequenas/novas |
| Limitada II | USD 150.000 | Empresas médias |
| Ilimitada | Sem limite | Capacidade financeira comprovada |

> **Lacuna comum**: Cliente sem RADAR operando por conta e ordem → infração.

---

# Impacto Tributário por Modalidade

### Cascata de impostos (40% a 100%+ sobre CIF)

| Imposto | Base | Taxa típica | Conta e Ordem | Encomenda |
|---------|------|-------------|---------------|-----------|
| **II** | CIF | 0–35% | Adquirente paga | Trading paga |
| **IPI** | CIF + II | 0–30% | Adquirente paga | Trading paga |
| **PIS** | CIF | 2,1% | Adquirente paga | Trading paga |
| **COFINS** | CIF | 9,65% | Adquirente paga | Trading paga |
| **ICMS** | Cascata "por dentro" | 17–25% | Adquirente paga | Trading paga |

> Na **conta e ordem**, o adquirente é o sujeito passivo e reivindica créditos.
> Na **encomenda**, a trading assume toda a carga tributária e repassa no preço de venda.

---

# Exemplo Prático: Eletrônicos (CIF R$ 55.120)

| Etapa | Valor (R$) |
|-------|-----------|
| II (14%) | 7.717 |
| IPI (10%) | 6.284 |
| PIS (2,1%) | 1.158 |
| COFINS (9,65%) | 5.319 |
| ICMS (18% — SP) | ~16.902 |
| **Total Impostos** | **~37.380** |
| **Taxa efetiva sobre CIF** | **~67,8%** |

> Este custo é pago pelo **adquirente** (conta e ordem) ou pela **trading** (encomenda).
> Na encomenda, a trading embute na margem de revenda.

---

# Fluxo de Notas Fiscais

<div class="columns">
<div class="col">

### Conta e Ordem

1. **NF Entrada** (CFOP 3.949)
   Trading registra entrada da mercadoria importada

2. **NF Saída** (CFOP 5.949 / 6.949)
   Trading remete ao adquirente
   *(transferência, não venda)*

</div>
<div class="col">

### Encomenda

1. **NF Entrada**
   Trading registra entrada como mercadoria própria

2. **NF Venda**
   Trading vende ao encomendante
   *(operação comercial com margem)*

</div>
</div>

> **Atenção**: CFOP incorreto é um dos erros mais auditados pela Receita Federal.

---

<!-- _class: lead -->

# ⚠️ Conformidade

## A Receita Federal está de olho

---

# O Teste da Receita Federal

### Como a RFB determina a natureza real da operação:

```
  ┌──────────────────────────────────────────────┐
  │  QUEM PAGOU O FORNECEDOR?                    │
  │                                               │
  │  Dinheiro do CLIENTE → Conta e Ordem          │
  │  Capital da TRADING  → Encomenda              │
  └──────────────────────────────────────────────┘
```

**A Receita cruza:**
- Dados da DI/DUIMP
- Fluxo monetário (quem pagou o fornecedor chinês)
- Termos contratuais arquivados
- Notas fiscais emitidas

> **Má classificação da modalidade** é uma das áreas **mais frequentemente auditadas**.

---

# Penalidades por Não Conformidade

| Infração | Consequência |
|----------|-------------|
| **Má classificação da modalidade** | Requalificação + multa + glosa de créditos |
| **NCM incorreta** | Multa de **50%** sobre II devido |
| **Subvaloração / subfaturamento** | Multa de **100%** + 2–5 anos de prisão |
| **RADAR expirado / modalidade errada** | Importação **paralisada** |
| **LI obtida após embarque** | Multa de **30%** sobre valor aduaneiro |
| **Erros NF-e** | R$ 10.000–20.000 por declaração |
| **Reincidência (3 anos)** | **+50%** sobre a multa |

### Canais de fiscalização aduaneira

| Canal | O que acontece |
|-------|---------------|
| **Verde** | Liberação automática |
| **Amarelo** | Revisão documental |
| **Vermelho** | Inspeção física + documental |
| **Cinza** | Investigação de valor — o mais grave |

---

# Riscos Específicos China → Brasil

1. **Certificações falsas**: Fornecedores chineses frequentemente alegam INMETRO/ANATEL que **não possuem** — sempre verifique nos portais oficiais

2. **Subfaturamento**: Importações da China recebem **escrutínio elevado** (canal Cinza) por padrões históricos — documentação de preço robusta é essencial

3. **Rotulagem incorreta**: ANVISA/INMETRO rejeitam e **destroem** mercadorias sem rotulagem em português

4. **Congestionamento portuário**: Ano Novo Chinês e feriados causam atrasos — armazenagem em Santos acumula rápido

5. **Câmbio fora do prazo**: Multa do BCB sobre valor de pagamento atrasado + suspeita de lavagem

---

# Otimização: TTD de Santa Catarina

### Vantagem competitiva de muitas trading companies

| Aspecto | Detalhe |
|---------|---------|
| **O que é** | Tratamento Tributário Diferenciado para ICMS |
| **Portos elegíveis** | Itajaí, Navegantes, São Francisco do Sul, Itapoá |
| **Benefício** | Redução significativa do ICMS na importação |
| **Quem usa** | Maioria das trading companies especializadas |

> Combinado com a escolha correta de modalidade, o TTD/SC pode reduzir **substancialmente** a carga tributária total.

---

# Mudanças no Horizonte

### Reforma Tributária (LC 214/2025) — Transição 2026–2033

| Atual | Futuro |
|-------|--------|
| PIS + COFINS (federal) | **CBS** (Contribuição sobre Bens e Serviços) |
| ICMS (estadual) | **IBS** (Imposto sobre Bens e Serviços) |
| 27 legislações ICMS | Alíquota unificada nacional |

### Portal Único / DUIMP

| Atual | Futuro |
|-------|--------|
| DI (Declaração de Importação) | **DUIMP** (Declaração Única) |
| Múltiplos sistemas | Portal Único integrado |
| Licenças separadas | LPCO centralizado |

> Meta: 100% migração para DUIMP até dez/2025.

---

<!-- _class: lead -->

# Resumo Decisório

---

# Qual Modalidade Escolher?

```
                    ┌─────────────────────────┐
                    │  Você quer manter        │
                    │  estoque próprio?        │
                    └──────────┬──────────────┘
                         │
                    SIM  │        NÃO
                    ▼    │         ▼
              ┌──────────┴──┐  ┌──────────────────┐
              │ CONTA       │  │ Cliente tem RADAR? │
              │ PRÓPRIA     │  └────────┬──────────┘
              └─────────────┘      │          │
                              SIM  │     NÃO  │
                              ▼    │          ▼
                        ┌──────────┴──┐  ┌────────────┐
                        │ CONTA E     │  │ ENCOMENDA   │
                        │ ORDEM       │  │             │
                        └─────────────┘  └─────────────┘
```

> **Regra de ouro**: Se o dinheiro do cliente paga o fornecedor → **conta e ordem**.
> Se o capital da trading paga → **encomenda**. Não misture.

---

<!-- _class: lead -->

# Obrigado!

*Apresentação gerada a partir do wiki de pesquisa*
*Baseado em IN RFB 1.861/2018 e legislação vigente*
*Dados atualizados até abril de 2026*
