---
tipo: fonte
titulo: "Resumo do AAPM Task Group 233: Avaliação de Desempenho em Tomografia Computadorizada"
data_criacao: 2026-08-23
data_atualizacao: 2026-08-23
tags: [aapm, tg-233\, dosimetria, qualidade-de-imagem, reconstrucao-iterativa, aec]
fontes_origem: ["raw/Performance evaluation of computed tomography systems Summary of AAPM Task Group 233.md"]
---

# Resumo do AAPM Task Group 233: Avaliação de Desempenho em Tomografia Computadorizada

## Visão Geral
O relatório do **AAPM Task Group 233** (Samei et al., 2019) estabelece diretrizes atualizadas para a avaliação de desempenho de sistemas de Tomografia Computadorizada (TC). O documento responde às limitações dos métodos tradicionais baseados em especificações ideais (sistemas lineares e invariantes no espaço), que se tornaram obsoletos com a introdução de algoritmos de **reconstrução iterativa (IR)** e sistemas dinâmicos de **[[Controle Automático de Exposição em TC|controle-automatico-de-exposicao-ct]] (AEC)**.

## Métodos e Pilares Avaliados
O TG-233 fundamenta a avaliação em métricas orientadas à tarefa (*task-based performance*)\, divididas em quatro pilares principais:

1. **Caracterização do Ruído:** Avaliação não apenas da magnitude (desvio padrão), mas da textura e espectro frequencial através do [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]].
2. **Resolução Espacial Sistemática:** Substituição da MTF tradicional pela [[Task Transfer Function|ttf-task-transfer-function]], que acomoda o comportamento não-linear das reconstruções iterativas variando conforme o contraste do objeto.
3. **Desempenho Baseado em Tarefa:** Uso do [[Índice de Detectabilidade|indice-de-detectabilidade]] ($d'$) e estimabilidade para correlacionar parâmetros físicos com a capacidade de detecção clínica de lesões.
4. **Desempenho do AEC:** Avaliação da modulação do tubo de raios X (mA) em relação à atenuação do paciente, garantindo reprodutibilidade e eficácia dosimetria/qualidade.

## Impacto Prático
As recomendações padronizam phantoms e algoritmos de análise para que físicos médicos possam realizar benchmarking objetivo e comparativo entre diferentes fabricantes e tecnologias de tomografia computadorizada.