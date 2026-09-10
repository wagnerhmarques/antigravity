---
tipo: conceito
titulo: "Controle Automático de Exposição em Tomografia Computadorizada"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags:
  - "dosimetria"
  - "tcm"
  - "radioprotecao"
fontes_origem:
  - "raw/AAPM Journal  Wiley Online Library.md"
---

## Definição
O **Controle Automático de Exposição (AEC)** e sua implementação específica de modulação de corrente do tubo de raios X ([[Modulação de Corrente de Tubo (TCM)|tube-current-modulation]] - TCM) adaptam dinamicamente a saída de radiação do scanner de acordo com as propriedades radiológicas e geométricas do paciente (através de radiografias de localização e diâmetro equivalente de água $d_w$).

## Métricas de Avaliação (TG233)
- **Adaptação Discreta e Contínua:** Resposta do $mA$ a variações de espessura.
- **Concordância Espacial ($C_{mA}$, $C_{noise}$):** Quantifica o atraso (lag) entre a alteração de atenuação do objeto e a resposta efetiva do sistema.
- **Relação Log-Linear:** Ajustes do tipo $\ln(mA) = \alpha(d_w) + \beta$.

## Ver Também
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Detectabilidade Index|detectabilidade-index]]
