---
tipo: fonte
titulo: "Projeto de Doutorado Direto: Observadores de aprendizado profundo para a otimização de protocolos de tomografia computadorizada baseada em tarefas"
autores:
  - "Wagner Henrique Marques"
orientador: "Prof. Dr. Paulo Roberto Costa"
instituicao: "Faculdade de Medicina da Universidade de São Paulo (FMUSP)"
ano: 2026
veiculo: "Projeto de Pesquisa FAPESP (Doutorado Direto)"
fonte_bruta: "raw/1408_RASCUNHO_Projeto_DD_FAPESP_Wagner.md"
tags:
  - tomografia-computadorizada
  - deep-learning
  - model-observers
  - task-based-image-quality
  - dosimetria
  - otimizacao-multiobjetivo
  - phantoms-hibridos
---

# Projeto de Doutorado Direto: Observadores de Aprendizado Profundo para a Otimização de Protocolos de TC

## 1. Resumo Executivo
Proposta de pesquisa de Doutorado Direto (FMUSP/FAPESP) visando desenvolver e validar um [[Deep Learning Model Observer|deep-learning-model-observer]] com mecanismo de atenção para estimar a detectabilidade ($d'$) de lesões em [[Tomografia Computadorizada|tomografia-computadorizada]] (TC) reconstruídas com algoritmos não lineares ([[Reconstrução Iterativa|iterative-reconstruction]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-reconstruction]]). O modelo será calibrado contra a resposta perceptual humana obtida via estudos [[Estudo de Observadores 2AFC|2afc-observer-study]] com radiologistas especialistas em três anatomias (tórax, abdome e crânio) usando [[Phantoms Híbridos|phantoms-hibridos]]. A métrica validada será integrada em uma formulação de [[Otimização Multiobjetivo em TC|otimizacao-multiobjetivo-tc]] da tríade Dose ($D$), Tempo Operacional ($T$) e Desempenho ($W$) através da fronteira de Pareto com $\varepsilon$-dominância, avaliando a transferibilidade entre 7 tomógrafos de 4 fabricantes.

## 2. Dados Quantitativos e Metodologia
- **Epidemiologia dosimétrica:** TC responde por ~62% da dose coletiva médica global (~4,3 bilhões de exames/ano) (UNSCEAR 2022). DRLs reduziram 21,8% nos EUA entre 2014 e 2025 (Kanal et al., 2026).
- **Espaço Amostral & Equipamentos:** 7 tomógrafos clínicos de 4 fabricantes; 3 phantoms híbridos antropomórficos/geométricos (tórax, abdome, crânio).
- **Estudo Perceptual:** Mínimo de 20 radiologistas por anatomia (MRMC, poder 0,80 para $\Delta\text{AUC} = 0{,}05$, $\alpha = 0{,}05$).
- **Otimização Multiobjetivo:** Minimização de $D$ ([[Métricas de Dose em TC|ctdivol]] / DLP), Minimização de $T$ ($T_{\text{aquisicao}} + T_{\text{reconstrucao}}$) e Maximização de $W$ ($d'$ / AUC), resolvido via [[Algoritmo Genético NSGA-II|nsga-ii]] e modelos substitutos com Processos Gaussianos.

## 3. Estrutura em Eixos de Pesquisa
- **Eixo 1:** Validação da automação metrológica de [[Noise Power Spectrum|noise-power-spectrum]] (NPS), [[Task Transfer Function|task-transfer-function]] (TTF) e $d'$ clássico ([[NPWE Model Observer|npwe-model-observer]], [[Channelized Hotelling Observer (CHO)|cho-model-observer]], [[Hotelling Observer|hotelling-observer]]) (ICC $\ge 0{,}90$).
- **Eixo 2:** Desenvolvimento do observador baseado em Vision Transformer e calibração via 2AFC.
- **Eixo 3:** Otimização multiobjetivo da tríade $(D, T, -W)$ e caracterização da fronteira de Pareto.
- **Eixo 4:** Transferibilidade inter-fabricantes via validação *leave-one-scanner-out*.

## 4. Conceitos Relacionados
- [[Task Based Image Quality|task-based-image-quality]]
- [[Índice de Detectabilidade|detectability-index]]
- [[Deep Learning Model Observer|deep-learning-model-observer]]
- [[Otimização Multiobjetivo em TC|otimizacao-multiobjetivo-tc]]
- [[Phantoms Híbridos|phantoms-hibridos]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-ct]]