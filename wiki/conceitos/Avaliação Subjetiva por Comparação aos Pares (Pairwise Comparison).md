---
tipo: conceito
titulo: "Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags:
  - psicofisica
  - qualidade-de-imagem
  - metodologia-cientifica
  - estatistica
fontes_origem:
  - "[[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]"
---

# Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)

## 1. Limitações Críticas da Escala Likert Tradicional
A avaliação de qualidade de imagem diagnóstica em radiologia tem sido dominada pelo uso de escalas ordinais de Likert (típicas de 1 a 5 pontos). No entanto, estudos metodológicos revelam deficiências estruturais desse modelo:
1. **Viés de Tendência Central (*Central Tendency Bias*):** Observadores humanos tendem a evitar atribuir as notas extremas (1 e 5) por receio de que surjam casos ainda piores ou melhores ao longo do teste. Isso concentra a grande maioria dos escores nos valores 3 e 4, suprimindo o poder discriminativo.
2. **Calibração Interna Flutuante:** Critérios de pontuação variam entre diferentes leitores (variabilidade interobservador) e no mesmo leitor em momentos distintos (variabilidade intraobservador).
3. **Ineficácia de Treinamento Prévio:** Fornecer imagens de referência ou treinamento pré-teste não elimina as discrepâncias de escala ordinal.

---

## 2. Princípio da Comparação aos Pares e Algoritmo de Ford-Johnson
O método de **Pairwise Comparison (PC)** apoia-se na lei psicofísica do julgamento comparativo de Thurstone: a mente humana é substancialmente mais precisa ao comparar dois estímulos simultâneos e emitir uma escolha forçada ("Qual imagem possui melhor qualidade diagnóstica?") do que ao quantificar uma pontuação absoluta isolada.

### Otimização Computacional: Algoritmo de Ford-Johnson
Para ordenar $N=50$ exames tomográficos, uma abordagem de força bruta exigiria todas as combinações possíveis:

$$
C(N, 2) = \frac{N(N-1)}{2} = \frac{50 \times 49}{2} = 1225 \text{ comparacoes}
$$

Para viabilizar a rotina de radiologistas, integra-se o **algoritmo de ordenação por merge/inserção de Ford-Johnson**, que assume a transitividade relacional ($A > B \land B > C \implies A > C$). Isso reduz as avaliações necessárias para aproximadamente **220 comparações dinâmicas por leitor** (uma redução de >80% no esforço de avaliação).

```
[Apresentação Dinâmica Par A vs. B] ─── Escolha do Radiologista ───► [Árvore de Decisão Ford-Johnson]
                                                                                 │
                                                                                 ▼
[Ranking Contínuo e Ordenado de Qualidade] ◄─── Conclusão em ~220 pares ────────┘
```

---

## 3. Ganhos de Reprodutibilidade e Validação Estatística

Conforme demonstrado na tese de [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]], a substituição da escala Likert pela comparação pareada gerou expressivos ganhos no Coeficiente de Correlação Intraclasse (ICC):

| Dataset Avaliado | ICC Interobservador (Likert) | ICC Interobservador (Pairwise Comparison) | Ganho de Confiabilidade |
| :--- | :--- | :--- | :--- |
| **Alta Variação de Qualidade** | $0,665$ ($95\%\text{ CI } 0,396-0,814$) | **$0,785$** ($95\%\text{ CI } 0,676-0,867$) | $+18,0\%$ no ICC |
| **Baixa Variação de Qualidade** (Sutil) | $0,276$ ($95\%\text{ CI } 0,034-0,500$) | **$0,562$** ($95\%\text{ CI } 0,337-0,729$) | **$+103,6\%$ no ICC** |

O método revelou-se especialmente superior para detectar variações sutis de qualidade geradas por alterações incrementais de dose ou filtros de reconstrução iterativa, servindo como *gold standard* para validação de algoritmos de inteligência artificial.

---

## Referências Cruzadas
- [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]