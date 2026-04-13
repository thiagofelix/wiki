---
title: Cascata de Impostos de Importação Brasil
type: conceito
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/regulatory.md
  - raw/providers.md
tags:
  - tributação
  - regulatória
  - conformidade
---

# Cascata de Impostos de Importação Brasil

## Visão Geral

Cada importação comercial para o Brasil enfrenta uma pilha cascata de impostos federais e estaduais. O total de carga tributária efetiva normalmente varia de **40% a mais de 100%** do valor CIF, dependendo da categoria de produto e estado de entrada.

## Sequência Tributária

| Ordem | Imposto | Autoridade | Base | Taxa Típica |
|-------|-----|-----------|------|-------------|
| 1 | **II** (Imposto de Importação) | Federal | Valor CIF | 0–35% |
| 2 | **IPI** (Imposto sobre Produtos Industrializados) | Federal | CIF + II | 0–30% |
| 3 | **AFRMM** (sobretaxa marítima) | Federal | Valor do frete marítimo | 25% |
| 4 | **PIS-Importação** | Federal | Valor CIF | 2,1% |
| 5 | **COFINS-Importação** | Federal | Valor CIF | 9,65% |
| 6 | **Taxa SISCOMEX** | Federal | Por declaração | R$185 + R$29,50/item |
| 7 | **ICMS** | Estadual | CIF + II + IPI + PIS + COFINS + despesas ("por dentro") | 17–25% |

## Regras Fiscais-Chave

### II — Imposto de Importação
- Taxa determinada por código NCM; má classificação carrega penalidade 50%
- China recebe tarifas MFN padrão (sem acordo preferencial)
- Intervalo: 0% (matérias-primas) a 35% (bens de consumo); eletrônicos normalmente 10–20%

### IPI
- Taxa por tabela TIPI; inversamente proporcional à "essencialidade" do produto
- Será reduzido a zero para maioria dos produtos até 2027 sob reforma tributária (exceção categorias Zona Franca Manaus)

### PIS/COFINS-Importação
- Combinado: 11,75% (2,1% PIS + 9,65% COFINS)
- Decisão STF (Tema 69): ICMS excluído da base PIS/COFINS

### ICMS
- 27 estruturas estaduais diferentes; taxa depende do estado de desembaraço aduaneiro
- Taxas-chave: São Paulo 18%, Rio de Janeiro 20%, Minas Gerais 19%
- Calculado "por dentro" (incluído em própria base), tornando taxa efetiva superior
- Fórmula: `Base ICMS = (CIF + II + IPI + PIS + COFINS + Despesas) / (1 − taxa ICMS)`

## Exemplo Elaborado: Eletrônicos para São Paulo

FOB $10.000 + frete $500 + seguro $100 → CIF = $10.600 × R$5,20 = **R$55.120**

| Etapa | Valor (R$) |
|------|-------------|
| II (14%) | 7.717 |
| IPI (10%) | 6.284 |
| PIS (2,1%) | 1.158 |
| COFINS (9,65%) | 5.319 |
| ICMS (18%) | ~16.902 |
| **Total Impostos** | **~37.380** |
| **Taxa Efetiva sobre CIF** | **~67,8%** |

## Mecanismo de Pagamento

Todos os impostos federais pagos via DARF antes de desembaraço aduaneiro. ICMS pago ao tesouro estadual.

## Otimização Fiscal Santa Catarina

Redução ICMS via regime **TTD** (Tratamento Tributário Diferenciado) de SC em portos Itajaí, Navegantes, São Francisco do Sul e Itapoá é vantagem competitiva de facto alavancada por muitas trading companies e importadoras.

## Mudanças Próximas

Veja [reforma-tributaria.md](reforma-tributaria.md) — CBS + IBS substituirão PIS/COFINS e ICMS entre 2026–2033.

## Páginas Relacionadas

- [receita-federal.md](receita-federal.md) — Receita Federal do Brasil
- [ncm-classification.md](ncm-classification.md) — Classificação de produtos
- [remessa-conforme.md](remessa-conforme.md) — Regras impostos e-commerce
- [comparacao-modalidades-importacao.md](comparacao-modalidades-importacao.md) — Conta e ordem vs. encomenda
