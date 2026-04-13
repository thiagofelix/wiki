---
title: NF-e — Nota Fiscal Eletrônica para Importações
type: conceito
created: 2026-04-12
updated: 2026-04-12
sources:
  - raw/regulatory.md
tags:
  - conformidade
  - tributação
  - documentação
---

# NF-e — Nota Fiscal Eletrônica para Importações

## Requisito

Emitir uma NF-e no desembaraço aduaneiro é **obrigatório** para todos os importadores comerciais por **Protocolo ICMS 85/2010**. Deve ser emitida antes da mercadoria deixar a unidade alfandegária.

## Quem Emite

O **importador de registro** sempre, independentemente de modalidade:
- **Importação direta**: Uma NF-e para mercadorias entrando em estoque
- **[Conta e ordem](comparacao-modalidades-importacao.md)**: Trading emite NF-e de entrada (CFOP 3.949) + NF-e de transferência para cliente (5.949/6.949)
- **[Encomenda](comparacao-modalidades-importacao.md)**: Trading emite NF-e de entrada + NF-e de venda para encomendante

## Campos Obrigatórios

| Campo | Conteúdo |
|-------|---------|
| CFOP | 3.101 (industrialização), 3.102 (revenda), 3.127 (uso), 3.949 (conta e ordem) |
| NCM | Código Mercosul de 8 dígitos |
| Valor Aduaneiro | Valor CIF |
| Número DI/DUIMP | Referência obrigatória |
| Impostos | II, IPI, PIS, COFINS, ICMS — valores e alíquotas |
| Fornecedor | Nome e país do exportador estrangeiro |

NF-e emitida em **BRL** à taxa SISCOMEX na data de registro da DI.

## Documentos de Suporte

1. Extrato DI/DUIMP
2. Comprovante de Importação (CI)
3. Recibo de pagamento ICMS
4. Bill of Lading / AWB
5. Fatura comercial
6. Packing list

## DANFE

O DANFE impresso deve acompanhar a mercadoria da porto/aeroporto até as instalações do importador. **Sem ele, a mercadoria não pode ser transportada domesticamente.**

## Páginas Relacionadas

- [cascata-tributária.md](cascata-tributária.md) — Estrutura tributária
- [comparacao-modalidades-importacao.md](comparacao-modalidades-importacao.md) — Modalidades
- [armadilhas-conformidade.md](armadilhas-conformidade.md) — Multas por erros em NF-e
