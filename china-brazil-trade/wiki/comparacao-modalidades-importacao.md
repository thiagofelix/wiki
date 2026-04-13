---
title: "Comparação: Modalidades de Importação (Conta e Ordem vs. Encomenda)"
type: comparação
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/regulatory.md
tags:
  - regulatória
  - conformidade
  - trading-company
---

# Comparação: Importação por Conta e Ordem vs. Por Encomenda

Ambas as modalidades são regidas por **IN RFB 1.861/2018** (alterada por IN 1.937/2020 e IN 2.101/2022).

## Lado a Lado

| Dimensão | Conta e Ordem | Encomenda |
|-----------|--------------|-----------|
| **Natureza legal** | Contrato de serviço: trading fornece serviço aduaneiro | Comercial: trading compra exterior, revende domesticamente |
| **Propriedade de bens** | **Adquirente (cliente)** é dono desde momento da compra | **Trading** é dona até venda para encomendante |
| **Quem paga fornecedor** | Adquirente (ou trading em nome do cliente) | Trading, usando **seus próprios recursos financeiros** |
| **Contribuinte (sujeito passivo)** | Adquirente para II, IPI, PIS/COFINS | Trading para todos os impostos de importação |
| **Requisitos RADAR** | **Ambos** importador E adquirente devem ter RADAR | Apenas trading precisa RADAR |
| **Identificação DI/DUIMP** | CNPJ do adquirente identificado na declaração | Apenas trading aparece |
| **Crédito PIS/COFINS** | Adquirente reivindica crédito de importação | Trading reivindica crédito de importação |
| **Risco financeiro para trading** | Menor (não usa próprios fundos) | Maior (capital vinculado até revenda) |
| **Tipo de contrato** | Contrato de serviço (arquivo obrigatório) | Contrato de compra + revenda |
| **Fluxo NF-e** | NF entrada (CFOP 3.949) + saída NF (5.949/6.949 cliente) | NF entrada + NF venda encomendante |

## Quando Usar Cada Uma

### Conta e Ordem é preferida quando:
- Negócio funciona como **provedor de serviço/plataforma** com capital reduzido
- Clientes já têm RADAR e querem propriedade de crédito fiscal
- Carga regulatória em cliente é aceitável

### Encomenda é preferida quando:
- Trading mantém **estoque e vende domesticamente**
- Trading quer controlar relacionamento comercial completo
- Cliente **não tem ou quer** habilitação RADAR

## Nota Crítica de Conformidade

**Má classificação da operação** é uma das áreas mais frequentemente auditadas. Receita Federal usa dados DI/DUIMP, fluxo monetário (quem pagou fornecedor), e termos contratuais para determinar natureza real.

**Sinal prático**: Se **dinheiro do cliente** flui para pagar fornecedor chinês → conta e ordem. Se **capital próprio da trading** → encomenda.

## Há também uma terceira modalidade:

**Importação por Conta Própria** — trading importa por própria conta e revende para empresas brasileiras. O modelo mais simples mas exige compromisso de capital pleno.

## Páginas Relacionadas

- [radar-siscomex.md](radar-siscomex.md) — Requisitos RADAR
- [cascata-tributária.md](cascata-tributária.md) — Estrutura tributária
- [armadilhas-conformidade.md](armadilhas-conformidade.md) — Penalidades por má classificação
