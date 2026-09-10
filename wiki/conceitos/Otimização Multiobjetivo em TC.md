---
tipo: conceito
titulo: "Otimização Multiobjetivo em Tomografia Computadorizada"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags:
  - otimizacao
  - pareto
  - radioprotecao
  - gestao-operacional
fontes_origem:
  - "[[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]]"
---

# Otimização Multiobjetivo em Tomografia Computadorizada

## 1. Formulação do Problema
A seleção ótima de protocolos em TC é modelada formalmente pela minimização e maximização simultânea do vetor tripartite:

$$
\min_{\mathbf{p} \in \Omega} \Big( D(\mathbf{p}), \, T(\mathbf{p}), \, -W(\mathbf{p}) \Big)
$$

Onde:
- $\mathbf{p}$: Vetor de parâmetros de aquisição e reconstrução (kVp, mA/mAs, pitch, espessura de corte, kernel, algoritmo);
- $D$: Métrica de dose de radiação ([[Métricas de Dose em TC|ctdivol]], DLP);
- $T$: Tempo operacional total ($T_{\text{aquisicao}} + T_{\text{reconstrucao}}$);
- $W$: Desempenho na tarefa diagnóstica ([[Índice de Detectabilidade|detectability-index]] $d'$ ou AUC).

## 2. Fronteira de Pareto e Incerteza Experimental
Como os objetivos são conflitantes, o resultado é um conjunto de soluções não dominadas (Fronteira de Pareto). Para considerar a incerteza experimental, aplica-se o conceito de **$\varepsilon$-dominância**, onde uma solução só domina outra se o ganho exceder o limiar de incerteza estatística das medições.

## 3. Métodos Numéricos
- Algoritmo genético elitista [[Algoritmo Genético NSGA-II|nsga-ii]];
- Modelos substitutos baseados em Processos Gaussianos (Kriging) para interpolação do espaço contínuo de protocolos.