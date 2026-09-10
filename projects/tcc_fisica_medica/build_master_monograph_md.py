import os

target_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md"

content = r"""---
tipo: tcc-monografia
titulo: "Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo"
autor: "Wagner H. M."
orientador: "Prof. Dr. Paulo Roberto Costa"
instituicao: "Instituto de Física da Universidade de São Paulo (IFUSP)"
departamento: "Departamento de Física Nuclear - GDRFM"
data: 2026-09-01
versao: "4.0-master-completo"
tags:
  - tcc
  - abnt
  - fisica-medica
  - tomografia-computadorizada
  - task-based-image-quality
  - model-observers
  - deep-learning
  - vision-transformers
  - photon-counting-ct
  - anova-mrmc
  - otimizacao-multiobjetivo
  - psicofisica
---

<center>
<h3>UNIVERSIDADE DE SÃO PAULO</h3>
<h3>INSTITUTO DE FÍSICA</h3>
<h3>DEPARTAMENTO DE FÍSICA NUCLEAR</h3>
<h4>CURSO DE BACHARELADO EM FÍSICA COM HABILITAÇÃO EM FÍSICA MÉDICA</h4>

<br><br><br>

<h1>WAGNER H. M.</h1>

<br><br><br><br>

<h2>MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: DA TEORIA CLÁSSICA DE DETECÇÃO DE SINAIS AOS MODELOS DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO</h2>
</center>

<br><br><br><br><br><br>

<center>
<h3>SÃO PAULO</h3>
<h3>2026</h3>
</center>

<div style="page-break-after: always;"></div>

---

<center>
<h1>WAGNER H. M.</h1>

<br><br><br>

<h2>MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: DA TEORIA CLÁSSICA DE DETECÇÃO DE SINAIS AOS MODELOS DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO</h2>
</center>

<br><br>

<div style="margin-left: 45%; text-align: justify; font-size: 0.9em; line-height: 1.3;">
Monografia de Conclusão de Curso apresentada ao Instituto de Física da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física com Habilitação em Física Médica.
<br><br>
<b>Orientador:</b> Prof. Dr. Paulo Roberto Costa
<br>
<b>Área de Concentração:</b> Física Médica e Radiológica
</div>

<br><br><br><br>

<center>
<h3>SÃO PAULO</h3>
<h3>2026</h3>
</center>

<div style="page-break-after: always;"></div>

---

<center>
<h2>FOLHA DE APROVAÇÃO</h2>
<br>
<h3>WAGNER H. M.</h3>
<br>
<b>Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo</b>
</center>

<br>

<div style="margin-left: 45%; text-align: justify; font-size: 0.9em; line-height: 1.3;">
Monografia de Conclusão de Curso defendida e aprovada em _____ de ________________ de 2026 pela banca examinadora constituída pelos seguintes membros:
</div>

<br><br><br>

<center>
____________________________________________________<br>
<b>Prof. Dr. Paulo Roberto Costa (Orientador / Presidente)</b><br>
Instituto de Física da Universidade de São Paulo – IFUSP
<br><br><br>
____________________________________________________<br>
<b>Membro da Banca Examinadora 1</b><br>
Instituto de Radiologia do Hospital das Clínicas – InRad-HCFMUSP
<br><br><br>
____________________________________________________<br>
<b>Membro da Banca Examinadora 2</b><br>
Instituto de Física da Universidade de São Paulo – IFUSP
</center>

<div style="page-break-after: always;"></div>

---

## RESUMO

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica moderna, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação do desempenho diagnóstico (princípio ALARA). Historicamente, a metrologia e a garantia da qualidade em TC apoiaram-se em grandezas físicas escalares e lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores geométricos homogêneos. No entanto, a incorporação clínica de algoritmos avançados não lineares — com destaque para as reconstruções iterativas estatísticas e, fundamentalmente, as reconstruções baseadas em aprendizado profundo (*Deep Learning Image Reconstruction* - DLR) — quebrou as premissas de linearidade e invariância translacional do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo, dependente da dose, do contraste e da geometria local da cena, induzindo alterações texturais perceptuais (como a textura cerosa ou *plastic/waxy look*) que não são capturadas pelas métricas clássicas. Para superar essa limitação, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality* - TBIQ), ancorado na Teoria de Detecção de Sinais (*Signal Detection Theory* - SDT), no qual a qualidade da imagem é formalmente definida pelo desempenho de um observador (humano ou computacional) na execução de uma tarefa diagnóstica clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Este trabalho apresenta uma investigação exaustiva e estruturada da evolução dos observadores de modelo (*model observers*). Analisa-se a transição histórica do Observador Ideal Bayesiano para os modelos lineares antropomórficos com filtro ocular (NPWE) e canais corticais de frequência (CHO), demonstrando suas deduções matemáticas contínuas no domínio de Fourier e evidenciando os limites biofísicos que causam seu colapso sob reconstruções DLR e fundos anatômicos complexos. Em resposta, investiga-se a fronteira científica representada pelos Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO), baseados em arquiteturas *Vision Transformers* (ViT) com mecanismos de auto-atenção multi-cabeça, calibrados diretamente contra leituras psicofísicas de radiologistas em experimentos de Escolha Forçada entre Duas Alternativas (2AFC) sob análise estatística *Multi-Reader Multi-Case* (MRMC). Detalham-se a física dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a formulação da Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, que integra dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade ($W$). Esta monografia consolida as bases teóricas, biofísicas e metrológicas que sustentam a pesquisa de Doutorado Direto do autor no IFUSP.

**Palavras-chave:** Tomografia Computadorizada. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Vision Transformers. Tomografia por Contagem de Fótons. ANOVA MRMC. Simuladores Antropomórficos. Otimização Multiobjetivo. Fronteira de Pareto.

<div style="page-break-after: always;"></div>

---

## ABSTRACT

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), and Modulation Transfer Function (MTF), evaluated on homogeneous geometric phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms—including iterative reconstructions and Deep Learning Image Reconstruction (DLR)—has broken the foundational assumptions of system linearity and shift-invariance. Under non-linear processing, image noise becomes spatially non-stationary, dose-dependent, and scene-dependent, introducing perceptual texture alterations (such as the "plastic" or "waxy" appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer (human radiologist or mathematical model) executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a comprehensive investigation of the evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), detailing their continuous mathematical derivations in the Fourier domain and demonstrating their breakdown in non-linear DLR regimes and structured anatomical backgrounds. In response, we investigate the state of the art in Deep Learning Model Observers (DLMO), which leverage self-attention neural architectures (Vision Transformers) calibrated against expert radiologists' psychophysical performance in Two-Alternative Forced Choice (2AFC) paradigms under Multi-Reader Multi-Case (MRMC) statistical modeling. Furthermore, we explore the physics of Photon-Counting CT (PCCT), the synthesis of Virtual Monoenergetic Images (VMI), and the formulation of Multi-Objective Optimization via the Three-Dimensional Pareto Frontier $(D, T, -W)$, which integrates radiation dose ($D$), operational time ($T$), and diagnostic detectability ($W$). This study establishes the theoretical, computational, and physical foundation required for next-generation CT metrology, directly supporting the author's Direct Doctorate research at IFUSP.

**Keywords:** Computed Tomography. Task-Based Image Quality. Model Observers. Detectability Index. Deep Learning Reconstruction. Vision Transformers. Photon-Counting CT. ANOVA MRMC. Anthropomorphic Phantoms. Multi-Objective Optimization. Pareto Frontier.

<div style="page-break-after: always;"></div>

---

## LISTA DE ILUSTRAÇÕES

- **Figura 1** – Fundamentos da Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC
- **Figura 2** – Métricas Espectrais de Resolução ($TTF$), Ruído ($NPS$), Filtro Ocular ($E$) e Espectro da Tarefa ($W_{\text{task}}$)
- **Figura 3** – Modelagem de Canais Corticais (Gabor, Laguerre-Gauss, D-DOG) e Desempenho do Observador CHO
- **Figura 4** – Impacto da Não-Linearidade em DLR, Colapso de Modelos Analíticos Lineares e Metodologia de *Detrending*
- **Figura 5** – Fronteira de Pareto Tridimensional $(D, T, -W)$ para Otimização Multiobjetivo de Protocolos de TC
- **Fluxograma 1** – Pilares Fundamentais da Avaliação Baseada em Tarefa (TBIQ)
- **Fluxograma 2** – Decomposição em Canais Corticais e Decisão no Channelized Hotelling Observer (CHO)
- **Fluxograma 3** – Metodologia Experimental com *Phantoms* Híbridos e Plataforma Psicofísica 2AFC
- **Fluxograma 4** – Arquitetura Neural do Observador DLMO com Mecanismos de Auto-Atenção
- **Fluxograma 5** – Arquitetura Modular do Pipeline Computacional de Metrologia em TC
- **Quadro 1** – Comparativo Estrutural: Paradigma Tradicional *versus* Paradigma Baseado em Tarefa

<div style="page-break-after: always;"></div>

---

## LISTA DE TABELAS E QUADROS

- **Tabela 1** – Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante (FBP, HIR, MBIR e DLR)
- **Tabela 2** – Comparativo físico das tecnologias de detecção em TC: Detectores Integradores de Energia (EICT) *versus* Contagem de Fótons (PCCT)
- **Quadro 1** – Comparativo Estrutural entre o Paradigma Físico Clássico (Linear/Escalar) e o Paradigma Contemporâneo Baseado em Tarefa (TBIQ)

<div style="page-break-after: always;"></div>

---

## LISTA DE ABREVIATURAS E SIGLAS

| Sigla | Significado |
| :--- | :--- |
| **2AFC** | *Two-Alternative Forced Choice* (Escolha Forçada entre Duas Alternativas) |
| **AAPM** | *American Association of Physicists in Medicine* |
| **AEC** | *Automatic Exposure Control* (Controle Automático de Exposição) |
| **ALARA** | *As Low As Reasonably Achievable* (Tão Baixo Quanto Razoavelmente Exequível) |
| **ANOVA** | *Analysis of Variance* (Análise de Variância) |
| **ASiR** | *Adaptive Statistical Iterative Reconstruction* |
| **AUC** | *Area Under the ROC Curve* (Área sob a Curva ROC) |
| **BKE** | *Background Known Exactly* (Fundo Conhecido Exatamente) |
| **BKS** | *Background Known Statistically* (Fundo Conhecido Estatisticamente) |
| **CBR** | Colégio Brasileiro de Radiologia e Diagnóstico por Imagem |
| **CdTe** | Telureto de Cádmio (semicondutor de conversão direta) |
| **CEP** | Comitê de Ética em Pesquisa |
| **CHO** | *Channelized Hotelling Observer* (Observador de Hotelling Canalizado) |
| **CNR** | *Contrast-to-Noise Ratio* (Relação Contraste-Ruído) |
| **CONEP** | Comissão Nacional de Ética em Pesquisa |
| **CSF** | *Contrast Sensitivity Function* (Função de Sensibilidade ao Contraste) |
| **CTDI** | *Computed Tomography Dose Index* (Índice de Dose em Tomografia Computadorizada) |
| **CZT** | Telureto de Cádmio e Zinco |
| **D-DOG** | *Dense Difference of Gaussians* (Diferença Densa de Gaussianas) |
| **DBM** | Dorfman-Berbaum-Metz (modelo estatístico para MRMC) |
| **DLR** | *Deep Learning Image Reconstruction* (Reconstrução por Aprendizado Profundo) |
| **DLMO** | *Deep Learning Model Observer* (Observador de Modelo por Aprendizado Profundo) |
| **DLP** | *Dose-Length Product* (Produto Dose-Comprimento) |
| **DQE** | *Detective Quantum Efficiency* (Eficiência Quântica de Detecção) |
| **DRL** | *Diagnostic Reference Level* (Nível de Referência Diagnóstica) |
| **EICT** | *Energy-Integrating Computed Tomography* (TC por Integração de Energia) |
| **ESF** | *Edge Spread Function* (Função de Resposta ao Degrau) |
| **FBP** | *Filtered Backprojection* (Retroprojeção Filtrada) |
| **FOV** | *Field of View* (Campo de Visão) |
| **GDRFM** | Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP |
| **GPU** | *Graphics Processing Unit* (Unidade de Processamento Gráfico) |
| **GSDF** | *Grayscale Standard Display Function* (Função de Exibição Padrão em Tons de Cinza) |
| **HIR** | *Hybrid Iterative Reconstruction* (Reconstrução Iterativa Híbrida) |
| **HO** | *Hotelling Observer* (Observador de Hotelling) |
| **HOR** | Hillis-Obuchowski-Rockette (modelo estatístico de ANOVA MRMC) |
| **HU** | Unidade Hounsfield (*Hounsfield Unit*) |
| **IAEA** | *International Atomic Energy Agency* (Agência Internacional de Energia Atômica) |
| **ICC** | *Intraclass Correlation Coefficient* (Coeficiente de Correlação Intraclasse) |
| **ICRU** | *International Commission on Radiation Units and Measurements* |
| **IFUSP** | Instituto de Física da Universidade de São Paulo |
| **InRad** | Instituto de Radiologia do Hospital das Clínicas da FMUSP |
| **IO** | *Ideal Observer* (Observador Ideal Bayesiano) |
| **LG** | Laguerre-Gauss |
| **LOSO** | *Leave-One-Scanner-Out* (Validação Cruzada Omitindo um Tomógrafo) |
| **LSF** | *Line Spread Function* (Função de Espalhamento de Linha) |
| **MBIR** | *Model-Based Iterative Reconstruction* (Reconstrução Iterativa Baseada em Modelos) |
| **MHSA** | *Multi-Head Self-Attention* (Auto-Atenção Multi-Cabeça) |
| **MRMC** | *Multi-Reader Multi-Case* (Múltiplos Leitores e Múltiplos Casos) |
| **MTF** | *Modulation Transfer Function* (Função de Transferência de Modulação) |
| **NPS** | *Noise Power Spectrum* (Espectro de Potência do Ruído) |
| **NPW** | *Non-Prewhitening Observer* (Observador Sem Pré-Branqueamento) |
| **NPWE** | *Non-Prewhitening Observer with Eye Filter* (NPW com Filtro Ocular) |
| **NSGA-II** | *Non-dominated Sorting Genetic Algorithm II* |
| **OR** | Obuchowski-Rockette |
| **PACS** | *Picture Archiving and Communication System* |
| **PCCT** | *Photon-Counting Computed Tomography* (TC por Contagem de Fótons) |
| **PSF** | *Point Spread Function* (Função de Resposta ao Ponto) |
| **ROC** | *Receiver Operating Characteristic* (Característica de Operação do Receptor) |
| **ROI** | *Region of Interest* (Região de Interesse) |
| **SDT** | *Signal Detection Theory* (Teoria de Detecção de Sinais) |
| **SKE** | *Signal Known Exactly* (Sinal Conhecido Exatamente) |
| **SKS** | *Signal Known Statistically* (Sinal Conhecido Estatisticamente) |
| **SNR** | *Signal-to-Noise Ratio* (Relação Sinal-Ruído) |
| **TBIQ** | *Task-Based Image Quality* (Qualidade de Imagem Baseada em Tarefa) |
| **TC** | Tomografia Computadorizada |
| **TCLE** | Termo de Consentimento Livre e Esclarecido |
| **TG-233** | *Task Group 233* da AAPM |
| **TOPSIS** | *Technique for Order Preference by Similarity to Ideal Solution* |
| **TTF** | *Task Transfer Function* (Função de Transferência da Tarefa) |
| **ViT** | *Vision Transformer* |
| **VMI** | *Virtual Monoenergetic Image* (Imagem Monoenergética Virtual) |
| **WSS** | *Wide-Sense Stationary* (Estacionário no Sentido Amplo) |

<div style="page-break-after: always;"></div>

---

## LISTA DE SÍMBOLOS

| Símbolo | Significado Físico / Unidade |
| :--- | :--- |
| $\mathbf{g}$ | Vetor de dados de imagem discreta ($\mathbb{R}^N$) |
| $\mathbf{s}$ | Vetor determinístico do sinal ou lesão ($\mathbb{R}^N$) |
| $\mathbf{b}$ | Vetor estocástico de ruído e fundo anatômico ($\mathbb{R}^N$) |
| $t$ | Estatística de teste escalar de decisão |
| $t_c$ | Limiar de corte para decisão diagnóstica |
| $d'$ | Índice de detectabilidade (*d-prime*) |
| $d'_{\text{humano}}$ | Índice de detectabilidade experimental medido em leitores humanos |
| $d'_{\text{NPWE}}$ | Índice de detectabilidade calculado pelo modelo NPWE |
| $d'_{\text{CHO}}$ | Índice de detectabilidade calculado pelo modelo CHO |
| $d'_{\text{DL}}$ | Índice de detectabilidade estimado pelo modelo por aprendizado profundo |
| $\mathbf{K}$ | Matriz de autocovariância do ruído ($N \times N$, em $\text{HU}^2$) |
| $\mathbf{K}_{\mathbf{v}}$ | Matriz de autocovariância reduzida no espaço dos canais ($C \times C$) |
| $\mathbf{w}$ | Vetor de pesos ou template linear de filtragem ($\mathbb{R}^N$) |
| $\mathbf{T}$ | Matriz de operadores de canais corticais ($C \times N$) |
| $TTF(f)$ | Função de Transferência da Tarefa na frequência espacial $f$ (adimensional) |
| $f_{50}$ | Frequência espacial correspondente a 50% de modulação da TTF ($\text{mm}^{-1}$) |
| $f_{10}$ | Frequência espacial correspondente a 10% de modulação da TTF ($\text{mm}^{-1}$) |
| $NPS(u, v)$ | Espectro de Potência do Ruído bidimensional ($\text{mm}^2$ ou $\text{HU}^2\cdot\text{mm}^2$) |
| $NPS(f)$ | Espectro de Potência do Ruído radial unidimensional ($\text{HU}^2\cdot\text{mm}^2$) |
| $f_{\text{peak}}$ | Frequência espacial de máxima amplitude do espectro de ruído ($\text{mm}^{-1}$) |
| $f_{\text{av}}$ | Frequência espacial média ponderada do espectro de ruído ($\text{mm}^{-1}$) |
| $E(f)$ | Resposta em frequência do filtro ocular humano / CSF (adimensional) |
| $W_{\text{task}}(f)$ | Espectro de Fourier da morfologia da tarefa diagnóstica ($\text{HU}\cdot\text{mm}^2$) |
| $P_C$ | Proporção empírica de acertos no teste 2AFC ($0 \le P_C \le 1$) |
| $\Phi(x)$ | Função de distribuição cumulativa da variável normal padrão |
| $\Phi^{-1}(p)$ | Função quantil (inversa da distribuição cumulativa normal padrão) |
| $\sigma^2$ | Variância estatística do número de CT em uma região homogênea ($\text{HU}^2$) |
| $\sigma_{\text{int}}^2$ | Variância do ruído neural interno do observador biológico ($\text{HU}^2$) |
| $D$ | Dose de radiação absorvida / $\text{CTDI}_{\text{vol}}$ ($\text{mGy}$) |
| $T$ | Tempo operacional total do procedimento ($T = T_{\text{aq}} + T_{\text{rec}}$, em segundos) |
| $W$ | Desempenho na tarefa diagnóstica ($W = d'$) |
| $\Omega$ | Espaço viável de parâmetros do protocolo tomográfico |
| $\Delta C$ | Contraste radiológico central da lesão em relação ao fundo ($\text{HU}$) |
| $R$ | Raio físico da lesão esférica simulada ($\text{mm}$) |
| $J_1(x)$ | Função de Bessel ordinária de primeira espécie e ordem 1 |
| $Q, K, V$ | Matrizes de Consulta (*Query*), Chave (*Key*) e Valor (*Value*) no mecanismo de auto-atenção |
| $d_k$ | Dimensão dos vetores de projeção no módulo de atenção |
| $\mathbf{z}_0$ | Sequência de *patch embeddings* lineares com codificação posicional |
| $\sigma^2_R$ | Componente de variância associada aos leitores humanos na ANOVA MRMC |
| $\sigma^2_C$ | Componente de variância associada aos casos clínicos na ANOVA MRMC |
| $\sigma^2_{RC}$ | Componente de variância da interação leitor $\times$ caso na ANOVA MRMC |

<div style="page-break-after: always;"></div>

---

# SUMÁRIO

1. [1 INTRODUÇÃO](#1-introdução)
   - 1.1 [O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico](#11-o-dilema-fundamental-da-tomografia-computadorizada-dose-versus-desempenho-clínico)
   - 1.2 [Limitações Estruturais das Métricas Físicas Globais Tradicionais](#12-limitações-estruturais-das-métricas-físicas-globais-tradicionais)
   - 1.3 [A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa](#13-a-mudança-de-paradigma-qualidade-de-imagem-baseada-em-tarefa)
   - 1.4 [Objetivos](#14-objetivos)
     - 1.4.1 [Objetivo Geral](#141-objetivo-geral)
     - 1.4.2 [Objetivos Específicos](#142-objetivos-específicos)
   - 1.5 [Estrutura da Monografia](#15-estrutura-da-monografia)
2. [2 FUNDAMENTOS TEÓRICOS DA QUALIDADE BASEADA EM TAREFA](#2-fundamentos-teóricos-da-qualidade-baseada-em-tarefa)
   - 2.1 [Teoria de Detecção de Sinais e Tomada de Decisão Estatística](#21-teoria-de-detecção-de-sinais-e-tomada-de-decisão-estatística)
   - 2.2 [O Índice de Detectabilidade no Domínio Espacial](#22-o-índice-de-detectabilidade-no-domínio-espacial)
   - 2.3 [Transição para o Domínio das Frequências via Teorema de Wiener-Khinchin](#23-transição-para-o-domínio-das-frequências-via-teorema-de-wiener-khinchin)
     - 2.3.1 [Função de Transferência da Tarefa e Resolução Dependente de Contraste](#231-função-de-transferência-da-tarefa-e-resolução-dependente-de-contraste)
     - 2.3.2 [Espectro de Potência do Ruído e Textura Espacial](#232-espectro-de-potência-do-ruído-e-textura-espacial)
     - 2.3.3 [Filtro Ocular e Modelagem Biofísica da Visão Humana](#233-filtro-ocular-e-modelagem-biofísica-da-visão-humana)
     - 2.3.4 [Espectro da Tarefa Diagnóstica e o Critério de Rose](#234-espectro-da-tarefa-diagnóstica-e-o-critério-de-rose)
   - 2.4 [Paradigmas de Detecção e a Dedução Matemática do Experimento 2AFC](#24-paradigmas-de-detecção-e-a-dedução-matemática-do-experimento-2afc)
3. [3 A EVOLUÇÃO DOS OBSERVADORES DE MODELO LINEARES E VALIDAÇÃO PSICOFÍSICA MRMC](#3-a-evolução-dos-observadores-de-modelo-lineares-e-validação-psicofísica-mrmc)
   - 3.1 [O Observador Ideal Bayesiano e o Limite Superior Termodinâmico](#31-o-observador-ideal-bayesiano-e-o-limite-superior-termodinâmico)
   - 3.2 [O Observador NPW e a Dedução Contínua do Modelo NPWE](#32-o-observador-npw-e-a-dedução-contínua-do-modelo-npwe)
   - 3.3 [O Desafio dos Fundos Estruturados: Hotelling Observer e Channelized Hotelling Observer](#33-o-desafio-dos-fundos-estruturados-hotelling-observer-e-channelized-hotelling-observer)
     - 3.3.1 [Formulação Algébrica do Observador de Hotelling](#331-formulação-algébrica-do-observador-de-hotelling)
     - 3.3.2 [Modelagem dos Canais Corticais: Gabor, Laguerre-Gauss e D-DOG](#332-modelagem-dos-canais-corticais-gabor-laguerre-gauss-e-d-dog)
   - 3.4 [Validação Psicofísica e Decomposição Formal da Variância na ANOVA MRMC](#34-validação-psicofísica-e-decomposição-formal-da-variância-na-anova-mrmc)
     - 3.4.1 [Modelo Linear Misto de Efeitos Aleatórios](#341-modelo-linear-misto-de-efeitos-aleatórios)
     - 3.4.2 [Graus de Liberdade Ajustados de Satterthwaite e Teste de Hipóteses](#342-graus-de-liberdade-ajustados-de-satterthwaite-e-teste-de-hipóteses)
4. [4 O COLAPSO DA LINEARIDADE, ALGORITMOS DLR E SIMULADORES HÍBRIDOS](#4-o-colapso-da-linearidade-algoritmos-dlr-e-simuladores-híbridos)
   - 4.1 [Taxonomia e Comparativo Físico dos Algoritmos de Reconstrução](#41-taxonomia-e-comparativo-físico-dos-algoritmos-de-reconstrução)
     - 4.1.1 [Filosofia GE Healthcare: TrueFidelity e Mapeamento Direto de FBP](#411-filosofia-ge-healthcare-truefidelity-e-mapeamento-direto-de-fbp)
     - 4.1.2 [Filosofia Canon Medical: AiCE e Treinamento Ancorado em MBIR](#412-filosofia-canon-medical-aice-e-treinamento-ancorado-em-mbir)
     - 4.1.3 [Filosofia Siemens Healthineers: Precise Image e Alpha Engine](#413-filosofia-siemens-healthineers-precise-image-e-alpha-engine)
     - 4.1.4 [Filosofia Philips Healthcare: Precise Image em Espaço Híbrido](#414-filosofia-philips-healthcare-precise-image-em-espaço-híbrido)
   - 4.2 [A Quebra da Linearidade, Não-Estacionariedade e o Efeito Ceroso](#42-a-quebra-da-linearidade-não-estacionariedade-e-o-efeito-ceroso)
   - 4.3 [A Transição dos Simuladores: De Cilindros Homogêneos a Phantoms Antropomórficos Híbridos](#43-a-transição-dos-simuladores-de-cilindros-homogêneos-a-phantoms-antropomórficos-híbridos)
   - 4.4 [Tratamento de Ruído em Anatomias Complexas: Detrending Polinomial 2D e Incerteza Bootstrap](#44-tratamento-de-ruído-em-anatomias-complexas-detrending-polinomial-2d-e-incerteza-bootstrap)
5. [5 O ESTADO DA ARTE: OBSERVADORES POR APRENDIZADO PROFUNDO, PCCT E OTIMIZAÇÃO MULTIOBJETIVO](#5-o-estado-da-arte-observadores-por-aprendizado-profundo-pcct-e-otimização-multiobjetivo)
   - 5.1 [Observadores Baseados em Aprendizado Profundo e Auto-Atenção](#51-observadores-baseados-em-aprendizado-profundo-e-auto-atenção)
     - 5.1.1 [Arquitetura Vision Transformer: Projeção Linear e Patch Embeddings](#511-arquitetura-vision-transformer-projeção-linear-e-patch-embeddings)
     - 5.1.2 [Mecanismo de Auto-Atenção Multi-Cabeça e Conexão Neurofisiológica](#512-mecanismo-de-auto-atenção-multi-cabeça-e-conexão-neurofisiológica)
   - 5.2 [Calibração Perceptual com Radiologistas e Transferibilidade Leave-One-Scanner-Out](#52-calibração-perceptual-com-radiologistas-e-transferibilidade-leave-one-scanner-out)
   - 5.3 [Física da Tomografia Computadorizada por Contagem de Fótons](#53-física-da-tomografia-computadorizada-por-contagem-de-fótons)
     - 5.3.1 [Detectores Semicondutores de Conversão Direta: CdTe versus Silício](#531-detectores-semicondutores-de-conversão-direta-cdte-versus-silício)
     - 5.3.2 [Fenômenos Estocásticos: Charge Sharing e Pulse Pile-Up](#532-fenômenos-estocásticos-charge-sharing-e-pulse-pile-up)
     - 5.3.3 [Compartimentalização de Energia e Imagens Monoenergéticas Virtuais](#533-compartimentalização-de-energia-e-imagens-monoenergéticas-virtuais)
   - 5.4 [Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional](#54-otimização-multiobjetivo-em-tc-a-fronteira-de-pareto-tridimensional)
6. [6 ARQUITETURA COMPUTACIONAL, METROLOGIA EXPERIMENTAL E ASPECTOS ÉTICOS](#6-arquitetura-computacional-metrologia-experimental-e-aspectos-éticos)
   - 6.1 [Arquitetura de Software do Pipeline Integrado de Metrologia](#61-arquitetura-de-software-do-pipeline-integrado-de-metrologia)
   - 6.2 [Protocolo Metrológico Padronizado segundo o Relatório AAPM TG-233](#62-protocolo-metrológico-padronizado-segundo-o-relatório-aapm-tg-233)
   - 6.3 [Aspectos Bioéticos, Regulatórios e Desenho Experimental com Seres Humanos](#63-aspectos-bioéticos-regulatórios-e-desenho-experimental-com-seres-humanos)
7. [7 CONSIDERAÇÕES FINAIS E PERSPECTIVAS](#7-considerações-finais-e-perspectivas)
   - 7.1 [Síntese da Trajetória Biofísica e Metrológica](#71-síntese-da-trajetória-biofísica-e-metrológica)
   - 7.2 [Impacto Clínico, Operacional e Normativo](#72-impacto-clínico-operacional-e-normativo)
   - 7.3 [Articulação com a Pesquisa de Doutorado Direto (FAPESP 2026–2030)](#73-articulação-com-a-pesquisa-de-doutorado-direto-fapesp-20262030)
8. [REFERÊNCIAS](#referências)

<div style="page-break-after: always;"></div>

---

# 1 INTRODUÇÃO

## 1.1 O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico

A Tomografia Computadorizada (TC) revolucionou a medicina diagnóstica desde a sua introdução clínica na década de 1970 por Godfrey Hounsfield. Ao permitir a reconstrução tridimensional de secções transversais do corpo humano com elevada diferenciação de densidades de tecidos moles e resolução espacial submilimétrica, a TC consolidou-se como a modalidade de escolha para o estadiamento oncológico, o planejamento cirúrgico e radioterápico, a avaliação de traumas agudos e o rastreamento precoce de doenças pulmonares e vasculares (MCCOLLOUGH et al., 2026; SEERAM, 2015; BUSHBERG et al., 2020).

Contudo, o princípio físico basilar da formação da imagem tomográfica reside na atenuação exponencial de feixes de raios X transmitidos através do paciente (ATTIX, 1986). A absorção e o espalhamento dessa radiação ionizante no tecido biológico provocam ionizações atômicas e quebras de ligações moleculares em estruturas de DNA celular, associando-se a riscos estocásticos de carcinogênese a longo prazo (ICRP, 2007). Consequentemente, embora represente apenas de 10% a 15% do total de procedimentos radiológicos executados mundialmente, a TC responde por aproximadamente 65% a 70% de toda a dose coletiva de radiação ionizante de origem médica absorvida pela população humana (IAEA, 2026; MCCOLLOUGH et al., 2026).

Essa assimetria impõe a aplicação rigorosa do princípio fundamental da radioproteção: o princípio ALARA (*As Low As Reasonably Achievable*) (ICRP, 2007; ANVISA, 2021; ANVISA, 2022). De acordo com essa diretriz, os protocolos tomográficos devem ser continuamente otimizados para operar na menor dose de radiação compatível com o objetivo diagnóstico desejado.

Para compreender a dificuldade física dessa otimização, é necessário analisar como os fótons de raios X se comportam estatisticamente. A detecção de fótons é um processo estocástico regido pela distribuição de Poisson (KNOLL, 2010). Em termos intuitivos, quanto menor o número de fótons emitidos pelo tubo de raios X, maiores são as flutuações estatísticas percentuais registradas pelos detectores. No domínio da imagem reconstruída, essa incerteza manifesta-se visualmente sob a forma de ruído quântico.

A relação matemática fundamental entre o desvio padrão do ruído ($\sigma_{\text{ruído}}$), o número de fótons detectados ($N_{\text{fótons}}$) e o índice de dose volumétrico ($\text{CTDI}_{\text{vol}}$) é expressa por:

$$\sigma_{\text{ruído}} \propto \frac{1}{\sqrt{N_{\text{fótons}}}} \propto \frac{1}{\sqrt{\text{CTDI}_{\text{vol}}}}$$

Em termos práticos, se um físico médico tentar reduzir a dose de radiação pela metade sem alterar a tecnologia do tomógrafo ou o algoritmo de reconstrução, o nível de ruído da imagem aumentará automaticamente em um fator de $\sqrt{2} \approx 1{,}41$ (ou seja, cerca de 41% de acréscimo de ruído). Esse ruído adicional sobrepõe-se às estruturas anatômicas sutis, reduzindo a capacidade do radiologista de identificar lesões de baixo contraste, como metástases hepáticas incipientes ou pequenos nódulos pulmonares em vidro fosco.

## 1.2 Limitações Estruturais das Métricas Físicas Globais Tradicionais

Durante quatro décadas, o controle de qualidade e a avaliação de desempenho de tomógrafos hospitalares apoiaram-se em grandezas físicas escalares derivadas da teoria de sistemas lineares e invariantes no espaço (BARRETT; MYERS, 2004):

a) Desvio padrão do número CT ($\sigma_{\text{HU}}$), mensurado no centro de um simulador geométrico homogêneo de água;
b) Relação Sinal-Ruído (SNR) e Relação Contraste-Ruído (CNR), calculadas classicamente pela diferença de médias entre o alvo e o fundo dividida pelo desvio padrão:

$$CNR = \frac{|\overline{\mu}_{\text{alvo}} - \overline{\mu}_{\text{fundo}}|}{\sigma_{\text{fundo}}}$$

c) Função de Transferência de Modulação (MTF), obtida a partir da resposta ao impulso de fios finos metálicos ou micro-esferas de alta densidade suspensas em meio uniforme.

Embora essas métricas fossem adequadas para caracterizar o algoritmo analítico clássico da Retroprojeção Filtrada (FBP) — que atua de forma estritamente linear e produz ruído gaussiano espacialmente estacionário —, elas falham de maneira substancial na avaliação dos tomógrafos modernos (SAMEI et al., 2019).

Essa falha decorre do fato de que os equipamentos contemporâneos utilizam algoritmos não lineares, como as reconstruções iterativas e as redes neurais profundas. A CNR convencional possui limitações conceituais severas:

Primeiramente, a CNR avalia apenas a dispersão pontual dos valores em pixels isolados, sendo completamente cega para a textura espacial do ruído. Duas imagens podem apresentar exatamente o mesmo valor numérico de $\sigma_{\text{fundo}}$ e a mesma diferença de contraste, mas uma conter ruído fino e granular enquanto a outra apresenta manchas borradas de baixa frequência. Para a percepção do olho humano, a facilidade de encontrar uma lesão em cada uma dessas imagens é completamente distinta.

Em segundo lugar, a aplicação de filtros matemáticos de suavização espacial reduz o desvio padrão do fundo, inflando artificialmente o valor da CNR, ao mesmo tempo em que apaga bordas anatômicas e diminui a nitidez de detalhes diagnósticos finos.

Por fim, a CNR não incorpora nenhuma propriedade fisiológica do sistema visual humano, tratando a tomada de decisão médica como se fosse uma simples subtração aritmética de intensidades.

## 1.3 A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa

Diante dessas inconsistências, órgãos normativos internacionais, como o relatório AAPM TG-233 (SAMEI et al., 2019) e o ICRU Report 54 (1996), formalizaram a transição para o paradigma da Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality* - TBIQ).

No escopo da TBIQ, a qualidade da imagem deixa de ser tratada como um atributo físico isolado e passa a ser definida como a eficácia estatística com que um observador específico consegue responder a uma pergunta clínica sobre a imagem (BARRETT; MYERS, 2004).

O Quadro 1 sumariza as diferenças estruturais fundamentais entre os dois paradigmas.

![Quadro 1: Comparativo Estrutural entre o Paradigma Físico Clássico (Linear/Escalar) e o Paradigma Contemporâneo Baseado em Tarefa (TBIQ).](assets/flow2_comparativo_paradigmas.png)

<center><em><b>Quadro 1:</b> Comparativo Estrutural: Paradigma Tradicional versus Paradigma Baseado em Tarefa.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

O pilar quantitativo da TBIQ é o Índice de Detectabilidade ($d'$), que integra de forma coerente as grandezas físicas do sistema tomográfico com as propriedades da visão humana, conforme esquematizado no Fluxograma 1.

![Fluxograma 1: Pilares Fundamentais da Avaliação de Qualidade de Imagem Baseada em Tarefa (TBIQ), articulando Resolução ($TTF$), Ruído ($NPS$) e Fisiologia Visual ($E(f)$) no Índice de Detectabilidade ($d'$).](assets/flow1_tbiq_paradigm.png)

<center><em><b>Fluxograma 1:</b> Pilares Fundamentais da Avaliação Baseada em Tarefa (TBIQ).</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

## 1.4 Objetivos

### 1.4.1 Objetivo Geral
Estruturar, deduzir matematicamente e analisar criticamente a evolução dos modelos perceptivos e computacionais de avaliação de qualidade de imagem baseada em tarefas em Tomografia Computadorizada, partindo das formulações lineares clássicas até os observadores de aprendizado profundo contemporâneos e sua aplicação na otimização multiobjetivo de protocolos clínicos.

### 1.4.2 Objetivos Específicos
a) Formalizar as deduções matemáticas da Teoria de Detecção de Sinais nos domínios espacial e de frequências, demonstrando a diagonalização da matriz de covariância via Teorema de Wiener-Khinchin;
b) Analisar a trajetória dos observadores lineares (IO, NPW, NPWE, HO e CHO), explicitando as aproximações do córtex visual e os métodos psicofísicos de validação humana (2AFC e ANOVA MRMC com decomposição formal de variâncias);
c) Investigar o colapso da linearidade em sistemas DLR, demonstrando o surgimento da não-estacionariedade e detalhando comparativamente as quatro filosofias comerciais de reconstrução profunda (GE, Canon, Siemens e Philips);
d) Examinar a fronteira científica dos Observadores Baseados em Aprendizado Profundo (DLMO), deduzindo os mecanismos de auto-atenção multi-cabeça nos *Vision Transformers* e sua correspondência com a visão foveal humana;
e) Investigar os fundamentos biofísicos da Tomografia por Contagem de Fótons (PCCT), cristais semicondutores CdTe/Silício, *charge sharing*, *pulse pile-up* e a síntese de Imagens Monoenergéticas Virtuais ($VMI$);
f) Formular o problema de Otimização Multiobjetivo em TC através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose ($D$), tempo operacional ($T$) e detectabilidade ($W$).

## 1.5 Estrutura da Monografia

Esta monografia está organizada em sete capítulos principais: o Capítulo 2 estabelece os fundamentos teóricos da SDT e a dedução das métricas de Fourier; o Capítulo 3 aborda a era dos observadores lineares e a validação psicofísica MRMC; o Capítulo 4 analisa a quebra da linearidade pelas reconstruções modernas, comparando os algoritmos comerciais DLR e o uso de simuladores antropomórficos; o Capítulo 5 discute os observadores de aprendizado profundo (ViT), a física da PCCT e a otimização multiobjetivo; o Capítulo 6 detalha a arquitetura computacional, a metrologia experimental e os aspectos bioéticos; e o Capítulo 7 sintetiza as conclusões e os direcionamentos futuros da pesquisa.

<div style="page-break-after: always;"></div>

---

# 2 FUNDAMENTOS TEÓRICOS DA QUALIDADE BASEADA EM TAREFA

## 2.1 Teoria de Detecção de Sinais e Tomada de Decisão Estatística

A Teoria de Detecção de Sinais (SDT), originada na engenharia de telecomunicações e adaptada para a física médica, fornece a estrutura matemática para modelar o processo de diagnóstico médico sob condições de incerteza estocástica (PETERSON et al., 1954; LUSTED, 1968; METZ, 1986; BARRETT; MYERS, 2004).

Em termos clínicos, quando um radiologista avalia uma região anatômica em um exame de tomografia, ele se depara com duas situações mutuamente exclusivas: ou o paciente não apresenta lesão naquele ponto (hipótese nula, $H_0$), ou existe uma lesão de contraste e morfologia definidos sobreposta às estruturas normais (hipótese alternativa, $H_1$).

Matematicamente, representamos a imagem digital através de um vetor de dados $\mathbf{g} \in \mathbb{R}^N$, formado por $N = N_x \times N_y$ pixels ordenados sequencialmente. O teste de hipóteses binário é formalizado por:

$$\begin{cases}
H_0 : \mathbf{g} = \mathbf{b} & \text{(Sinal Ausente: Apenas Ruído e Fundo Anatômico)} \\
H_1 : \mathbf{g} = \mathbf{b} + \mathbf{s} & \text{(Sinal Presente: Lesão } \mathbf{s} \text{ Sobreposta ao Fundo } \mathbf{b}\text{)}
\end{cases}$$

Um observador (seja um especialista humano ou um modelo computacional) avalia a imagem aplicando um operador matemático $t(\mathbf{g}): \mathbb{R}^N \to \mathbb{R}$, que condensa todas as informações visuais em um único valor numérico escalar $t$, denominado estatística de teste.

A decisão diagnóstica é tomada comparando $t$ com um valor limiar de corte $t_c$:
- Se $t \ge t_c$, o observador conclui que a lesão está presente ($H_1$);
- Se $t < t_c$, o observador declara que a imagem é normal ($H_0$).

Como a imagem contém ruído estocástico, a estatística $t$ comporta-se como uma variável aleatória, gerando duas curvas de densidade de probabilidade: $p(t|H_0)$ e $p(t|H_1)$, conforme ilustrado no Painel A da Figura 1.

![Figura 1: Fundamentos da Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC. (A) Distribuições condicionais de probabilidade $p(t|H_0)$ e $p(t|H_1)$, ilustrando o limiar de decisão $t_c$, a taxa de verdadeiros positivos (TPF) e falsos positivos (FPF), e a separação $d'$. (B) Família de curvas ROC para diferentes índices de detectabilidade ($d' = 0{,}5$ a $4{,}5$). (C) Relação psicofísica formal $P_C = \Phi(d'/\sqrt{2})$ no paradigma 2AFC, destacando o limiar clínico e o critério de Rose.](assets/fig1_sdt_roc_2afc.png)

<center><em><b>Figura 1:</b> Fundamentos da Teoria de Detecção de Sinais (SDT), Curvas ROC e Psicofísica 2AFC.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

A variação do limiar $t_c$ permite construir a curva Característica de Operação do Receptor (curva ROC), cujas ordenadas representam a Fração de Verdadeiros Positivos (TPF ou Sensibilidade) e as abscissas indicam a Fração de Falsos Positivos (FPF ou $1 - \text{Especificidade}$):

$$\text{TPF}(t_c) = \int_{t_c}^{\infty} p(t|H_1) \, dt, \qquad \text{FPF}(t_c) = \int_{t_c}^{\infty} p(t|H_0) \, dt$$

A integral sob a curva ROC define a métrica global de acurácia, denominada Área sob a Curva ROC (AUC), que varia de $0{,}5$ (desempenho equivalente ao acaso puro) até $1{,}0$ (discriminação perfeita sem erros).

## 2.2 O Índice de Detectabilidade no Domínio Espacial

Quando as distribuições condicionais $p(t|H_0)$ e $p(t|H_1)$ são gaussianas com variâncias semelhantes, a separação estatística entre elas é sintetizada pelo Índice de Detectabilidade ($d'$):

$$d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}$$

Para a classe dos observadores lineares, a estatística $t$ é obtida pelo produto interno entre a imagem $\mathbf{g}$ e um vetor de template (filtro linear) $\mathbf{w} \in \mathbb{R}^N$:

$$t = \mathbf{w}^T \mathbf{g} = \sum_{i=1}^N w_i g_i$$

Substituindo essa relação linear na definição de $d'$:
- O valor esperado sob $H_0$ é $\langle t | H_0 \rangle = \mathbf{w}^T \langle \mathbf{b} \rangle$;
- O valor esperado sob $H_1$ é $\langle t | H_1 \rangle = \mathbf{w}^T \langle \mathbf{b} \rangle + \mathbf{w}^T \mathbf{s}$;
- A diferença entre as médias das hipóteses é dada por $\Delta \langle t \rangle = \mathbf{w}^T \mathbf{s}$;
- A variância do teste para ruído de matriz de covariância $\mathbf{K} = \langle (\mathbf{b} - \langle \mathbf{b} \rangle)(\mathbf{b} - \langle \mathbf{b} \rangle)^T \rangle$ é $\sigma^2(t) = \mathbf{w}^T \mathbf{K} \mathbf{w}$.

Assim, obtém-se a formulação geral do índice de detectabilidade linear no domínio espacial:

$$d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}$$

Em termos intuitivos, o numerador ($\mathbf{w}^T \mathbf{s}$) quantifica quanta energia útil do sinal o filtro $\mathbf{w}$ consegue capturar, enquanto o denominador ($\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}$) mede a quantidade de ruído indesejado que atravessa esse mesmo filtro. O valor de $d'$ representa, portanto, a relação sinal-ruído efetiva do observador na tarefa.

## 2.3 Transição para o Domínio das Frequências via Teorema de Wiener-Khinchin

A manipulação da matriz de covariância $\mathbf{K}$ no domínio espacial torna-se computacionalmente inviável para imagens de alta resolução (onde $N \approx 262.144$ pixels).

Entretanto, se o ruído de fundo for estacionário no sentido amplo (WSS), a autocorrelação entre dois pontos espaciais depende exclusivamente da distância relativa entre eles. Matematicamente, isso transforma a matriz de covariância em uma matriz circulante.

Pelo Teorema de Wiener-Khinchin, a Transformada de Fourier bidimensional da função de autocorrelação espacial é exatamente igual à densidade espectral de potência do ruído, denominada Espectro de Potência do Ruído ($NPS(u, v)$) (BARRETT; MYERS, 2004; WAGNER et al., 1979). Essa propriedade permite transpor o cálculo de $d'$ para integrais contínuas no domínio das frequências espaciais.

A Figura 2 ilustra as quatro grandezas espectrais que compõem o cálculo da detectabilidade.

![Figura 2: Métricas Espectrais de Qualidade de Imagem Baseada em Tarefas. (A) Função de Transferência da Tarefa $TTF(f)$ para insertos de diferentes contrastes e materiais, evidenciando a dependência não linear e o ponto de modulação de 50% ($f_{50}$). (B) Espectro de Potência do Ruído $NPS(f)$ comparando FBP (rampa de alta frequência), HIR, DLR e MBIR com deslocamento de $f_{\text{peak}}$ ("plastic look"). (C) Filtro Ocular Humano $E(f)$ (Função de Sensibilidade ao Contraste). (D) Espectro de Potência da Tarefa Diagnóstica $W_{\text{task}}(f)$ para lesões nodulares esféricas de diferentes diâmetros ($\varnothing = 3, 5, 8, 12\text{ mm}$).](assets/fig2_spectral_metrics.png)

<center><em><b>Figura 2:</b> Métricas Espectrais de Resolução ($TTF$), Ruído ($NPS$), Filtro Ocular ($E$) e Espectro da Tarefa ($W_{\text{task}}$).</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

### 2.3.1 Função de Transferência da Tarefa e Resolução Dependente de Contraste
A Função de Transferência da Tarefa ($TTF(f)$) quantifica a resolução espacial do tomógrafo para um contraste radiológico e nível de dose específicos (SAMEI et al., 2019). Ela é obtida experimentalmente através da técnica da borda circular em insertos cilíndricos de calibração (Painel A da Figura 2).

O cálculo segue três etapas analíticas:
1. Obtenção do perfil radial de atenuação em torno do centro geométrico do inserto, gerando a Função de Resposta ao Degrau Radial ($\text{ESF}(r)$);
2. Diferenciação numérica radial para obter a Função de Espalhamento de Linha ($\text{LSF}(r) = \frac{d}{dr}\text{ESF}(r)$);
3. Cálculo da Transformada de Fourier 1D normalizada na frequência zero:

$$TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) e^{-i 2\pi f r} \, dr \right|}{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, dr \right|}$$

A frequência $f_{50}$ representa o ponto no qual a transferência de contraste decai para 50% do valor máximo, servindo como índice de nitidez do protocolo.

### 2.3.2 Espectro de Potência do Ruído e Textura Espacial
O Espectro de Potência do Ruído 2D ($NPS(u, v)$) quantifica como a energia do ruído estocástico se distribui pelas frequências espaciais da imagem:

$$NPS(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \left\langle \left| \mathcal{F}_{2D} \left\{ I(x, y) - \overline{I}(x, y) \right\} \right|^2 \right\rangle$$

onde $\overline{I}(x, y)$ é a superfície de fundo removida por *detrending*.

Para caracterizar a textura visual do ruído, calcula-se a frequência de pico ($f_{\text{peak}}$) e a frequência média ponderada ($f_{\text{av}}$):

$$f_{\text{av}} = \frac{\int_{0}^{\infty} f \cdot NPS(f) \, df}{\int_{0}^{\infty} NPS(f) \, df}$$

Conforme demonstrado no Painel B da Figura 2, algoritmos analíticos (FBP) apresentam picos em frequências mais elevadas (textura granular fina), enquanto métodos iterativos agressivos deslocam o pico para frequências baixas, provocando perda de textura estocástica natural (*plastic look*).

### 2.3.3 Filtro Ocular e Modelagem Biofísica da Visão Humana
O olho humano não responde de forma uniforme a todas as frequências espaciais. A Função de Sensibilidade ao Contraste do sistema visual atua como um filtro passa-faixa, modelado matematicamente pelo Filtro Ocular $E(f)$ (BURGESS, 1994; SAMEI et al., 2019):

$$E(f) = \left( \frac{f}{f_0} \right)^n \exp\left[ -c \left( \frac{f}{f_0} \right)^m \right]$$

com parâmetros $f_0 = 0{,}8 \text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$ e $c = 2{,}2$.

A frequência angular na retina ($f_{\text{retina}}$, em ciclos por grau) relaciona-se com a frequência espacial física na imagem ($f_{\text{imagem}}$, em $\text{mm}^{-1}$) para uma distância de visualização de $500 \text{ mm}$ através da expressão:

$$f_{\text{retina}} (\text{ciclos/grau}) \approx 8{,}727 \cdot f_{\text{imagem}} (\text{mm}^{-1})$$

O Painel C da Figura 2 evidencia que o olho humano possui máxima sensibilidade a variações de contraste na faixa de 3 a 5 ciclos/grau ($\approx 0{,}45 \text{ mm}^{-1}$ no plano do monitor diagnóstico), atenuando tanto variações muito suaves quanto detalhes ultrafinos.

Adicionalmente, a fisiologia da visão introduz um ruído interno neural ($\sigma_{\text{int}}^2$), de modo que a detectabilidade humana real relaciona-se com o modelo computacional por:

$$d'_{\text{humano}} = \frac{d'_{\text{NPWE}}}{\sqrt{1 + \left(\frac{\sigma_{\text{int}}}{\sigma_{\text{ext}}}\right)^2}}$$

### 2.3.4 Espectro da Tarefa Diagnóstica e o Critério de Rose
Para uma lesão circular homogênea de raio $R$ e contraste central $\Delta C$, o espectro da tarefa diagnóstica no domínio de Fourier é descrito por uma função de Bessel ordinária de primeira espécie $J_1$:

$$W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|$$

O Painel D da Figura 2 mostra que lesões maiores concentram sua energia em frequências espaciais baixas, enquanto lesões puntiformes dispersam sua informação em frequências médias e altas.

O Critério clássico de Rose (1948) postulava que um sinal só é detectado pelo ser humano se a relação de contraste-ruído ponderada pela área for superior a 5 ($k \ge 5$). Na formulação contemporânea da TBIQ, esse limiar corresponde a $d' \ge 4{,}0 \text{ a } 5{,}0$ para detecção quase certa ($P_C \ge 99\%$), enquanto $d' \approx 1{,}5 \text{ a } 2{,}0$ estabelece o limite de visibilidade clínica aceitável.

## 2.4 Paradigmas de Detecção e a Dedução Matemática do Experimento 2AFC

O padrão-ouro experimental para medir a percepção humana em física médica é o experimento de Escolha Forçada entre Duas Alternativas (2AFC) (BURGESS, 2011; ECKSTEIN et al., 2000).

No teste 2AFC, apresentam-se ao leitor dois campos de imagem idênticos: um contendo apenas ruído ($H_0$) e outro contendo a lesão inserida sobre o ruído ($H_1$). O observador avalia as duas imagens e calcula suas respectivas variáveis de decisão: $t_0 = t(\mathbf{g}|H_0)$ e $t_1 = t(\mathbf{g}|H_1)$. O observador acerta a escolha se $t_1 > t_0$.

Considerando que $t_0 \sim \mathcal{N}(\mu_0, \sigma^2)$ e $t_1 \sim \mathcal{N}(\mu_1, \sigma^2)$ são variáveis normais independentes, definimos a variável de diferença $\Delta t = t_1 - t_0$.

As propriedades estatísticas dessa variável combinada são:
- Média da diferença: $\mu_{\Delta t} = \mu_1 - \mu_0$;
- Variância da diferença: $\sigma_{\Delta t}^2 = \sigma^2(t_1) + \sigma^2(t_0) = 2\sigma^2$;
- Desvio padrão da diferença: $\sigma_{\Delta t} = \sqrt{2}\sigma$.

A proporção de acertos esperada ($P_C$) é a probabilidade de que $\Delta t > 0$:

$$P_C = P(\Delta t > 0) = P\left( \frac{\Delta t - \mu_{\Delta t}}{\sigma_{\Delta t}} > \frac{-(\mu_1 - \mu_0)}{\sqrt{2}\sigma} \right) = \Phi\left( \frac{\mu_1 - \mu_0}{\sqrt{2}\sigma} \right)$$

Como $d' = \frac{\mu_1 - \mu_0}{\sigma}$, estabelece-se a relação fundamental da psicofísica 2AFC:

$$P_C = \Phi\left( \frac{d'}{\sqrt{2}} \right)$$

Invertendo a equação através da função cumulativa normal inversa $\Phi^{-1}$:

$$d'_{\text{humano}} = \sqrt{2} \cdot \Phi^{-1}(P_C)$$

Essa dedução demonstra a origem física do fator $\sqrt{2}$, permitindo converter a porcentagem de acertos de médicos radiologistas em um índice escalar de detectabilidade $d'$ diretamente comparável aos modelos matemáticos.

<div style="page-break-after: always;"></div>

---

# 3 A EVOLUÇÃO DOS OBSERVADORES DE MODELO LINEARES E VALIDAÇÃO PSICOFÍSICA MRMC

## 3.1 O Observador Ideal Bayesiano e o Limite Superior Termodinâmico

O Observador Ideal (IO) representa o tomador de decisão estatístico ótimo que utiliza todas as informações físicas do feixe de radiação e do detector para maximizar a área sob a curva ROC ($AUC$), de acordo com o Lema de Neyman-Pearson (BARRETT; MYERS, 2004).

A estatística de teste do Observador Ideal para ruído gaussiano com matriz de covariância $\mathbf{K}$ e sinal determinístico $\mathbf{s}$ é obtida pelo logaritmo da razão de verossimilhança:

$$t_{\text{IO}}(\mathbf{g}) = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}$$

O índice de detectabilidade do Observador Ideal é expresso pela distância de Mahalanobis:

$$d'_{\text{IO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}} = \left[ \iint \frac{\left| W_{\text{task}}(u, v) \cdot TTF(u, v) \right|^2}{NPS(u, v)} \, du \, dv \right]^{1/2}$$

O Observador Ideal executa uma operação de pré-branqueamento (*prewhitening* $\mathbf{K}^{-1/2}$), descorrelacionando completamente a estrutura de ruído antes de aplicar o filtro casado. Embora o IO estabeleça o limite físico máximo de informação contida na radiação, ele superestima grosseiramente a percepção de observadores humanos, servindo apenas como referência física teórica superior.

## 3.2 O Observador NPW e a Dedução Contínua do Modelo NPWE

Para aproximar os modelos matemáticos das limitações biológicas, desenvolveu-se o modelo sem pré-branqueamento (*Non-Prewhitening* - NPW), cuja premissa é que o olho humano não inverte matrizes de ruído, atuando como um filtro casado simples $\mathbf{w}_{\text{NPW}} = \mathbf{s}$ (BURGESS, 1994).

A incorporação do filtro ocular $E(f)$ deu origem ao modelo NPWE (*Non-Prewhitening with Eye Filter*), que foi adotado pelo relatório internacional AAPM TG-233 como referência normativa para a avaliação de tomógrafos clínicos (SAMEI et al., 2019).

Aplicando a diagonalização do Teorema de Wiener-Khinchin, a detectabilidade do modelo NPWE em coordenadas contínuas bidimensionais é descrita por:

$$d'_{\text{NPWE}} = \frac{\iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \, du \, dv}{\left\{ \iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^4 \cdot NPS(u, v) \, du \, dv \right\}^{1/2}}$$

Para sistemas com simetria rotacional no plano de corte axial, a integral é simplificada para a coordenada radial $f$:

$$d'_{\text{NPWE}} = \frac{\int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^2 \cdot 2\pi f \, df}{\left\{ \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^4 \cdot NPS(f) \cdot 2\pi f \, df \right\}^{1/2}}$$

O modelo NPWE apresenta excelente correlação com leitores humanos em fundos homogêneos. No entanto, ele falha sistematicamente quando aplicado a fundos anatômicos complexos, pois não possui mecanismos para tratar o ruído estrutural.

## 3.3 O Desafio dos Fundos Estruturados: Hotelling Observer e Channelized Hotelling Observer

### 3.3.1 Formulação Algébrica do Observador de Hotelling
Quando uma lesão está localizada sobre tecidos anatômicos reais (como o parênquima pulmonar ou o trabeculado ósseo), o fundo introduz uma componente adicional de ruído estrutural. A matriz de covariância total é dada por $\mathbf{K}_{\text{total}} = \mathbf{K}_{\text{ruído}} + \mathbf{K}_{\text{anatômico}}$ (BARRETT; MYERS, 2004).

O Observador de Hotelling (HO) aplica a análise discriminante linear de Fisher para maximizar a separabilidade de classes sob fundos variáveis:

$$\mathbf{w}_{\text{HO}} = \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle \implies d'_{\text{HO}} = \sqrt{\langle \mathbf{s} \rangle^T \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle}$$

### 3.3.2 Modelagem dos Canais Corticais: Gabor, Laguerre-Gauss e D-DOG
Para simular o processamento de imagens realizado pelos neurônios do córtex visual primário (área V1) e contornar o custo computacional da inversão da matriz $\mathbf{K}_{\text{total}}$, Barrett et al. (1993), Yao & Barrett (1992) e Myers & Barrett (1987) introduziram o Observador de Hotelling Canalizado (*Channelized Hotelling Observer* - CHO).

O CHO aplica uma matriz de canais corticais $\mathbf{T} \in \mathbb{R}^{C \times N}$ (onde $C \ll N$, tipicamente $C \in [4, 10]$ canais), reduzindo o vetor de imagem $\mathbf{g}$ a um vetor canalizado de baixa dimensionalidade $\mathbf{v} \in \mathbb{R}^C$:

$$\mathbf{v} = \mathbf{T} \mathbf{g}$$

O fluxo completo de processamento do modelo CHO está ilustrado no Fluxograma 2.

![Fluxograma 2: Fluxo de Redução de Dimensionalidade por Canais Corticais e Decisão no Channelized Hotelling Observer (CHO).](assets/flow3_cho_pipeline.png)

<center><em><b>Fluxograma 2:</b> Decomposição Cortical e Processamento de Decisão no CHO.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

A matriz de covariância no espaço dos canais $\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K}_{\text{total}} \mathbf{T}^T \in \mathbb{R}^{C \times C}$ é facilmente invertida, fornecendo o índice de detectabilidade do CHO:

$$d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}$$

A Figura 3 apresenta os três principais modelos de canais corticais utilizados na literatura.

![Figura 3: Modelagem de Canais Corticais no Channelized Hotelling Observer (CHO). (A) Resposta em frequência dos canais passa-faixa Dense Difference of Gaussians (D-DOG) com espaçamento de meia oitava. (B) Perfis espaciais dos canais Laguerre-Gauss radiais ($LG_0$ a $LG_3$). (C) Mapa de sensibilidade bidimensional de um canal de Gabor orientado a $\theta = 45^\circ$. (D) Comportamento da detectabilidade $d'$ do modelo CHO em ruído anatômico estruturado comparado ao colapso do modelo NPWE não-canalizado.](assets/fig3_cho_cortical_channels.png)

<center><em><b>Figura 3:</b> Modelagem dos Canais Corticais (Gabor, Laguerre-Gauss, D-DOG) e desempenho do observador CHO.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

As formulações matemáticas dos canais corticais são:
1. **Canais D-DOG (*Dense Difference of Gaussians*):** Filtros passa-faixa concêntricos com espaçamento de meia oitava ($\alpha = 1{,}4$) e razão $a = 1{,}6$:
   $$D\text{-}DOG_j(f) = \exp\left[ -\frac{f^2}{2\sigma_j^2} \right] - \exp\left[ -\frac{f^2}{2(a \sigma_j)^2} \right]$$
2. **Canais Laguerre-Gauss (LG):** Funções ortogonais com simetria circular ponderadas por Polinômios de Laguerre $L_n$:
   $$LG_n(r; a_u) = \frac{\sqrt{2}}{a_u} \exp\left( -\frac{\pi r^2}{a_u^2} \right) L_n\left( \frac{2\pi r^2}{a_u^2} \right)$$
3. **Canais de Gabor:** Funções sinusoidais moduladas por envelope gaussiano com orientação espacial $\theta$ e frequência foveal $f_c$ (ABBEY; BARRETT, 2001).

## 3.4 Validação Psicofísica e Decomposição Formal da Variância na ANOVA MRMC

### 3.4.1 Modelo Linear Misto de Efeitos Aleatórios
Para certificar a confiabilidade metrológica de um observador computacional, é imperativo comparar seus resultados com o desempenho de médicos radiologistas reais em estudos psicofísicos 2AFC sob análise estatística *Multi-Reader Multi-Case* (MRMC) (DORFMAN et al., 1992; OBUCHOWSKI; ROCKETTE, 1995; HILLIS et al., 2011; RACINE et al., 2021).

O paradigma MRMC isola a variabilidade inerente aos leitores humanos da variabilidade amostral dos pacientes (casos clínicos). O modelo linear misto de Dorfman-Berbaum-Metz (DBM) e Obuchowski-Rockette-Hillis (ORH) decompõe a acurácia observada $Y_{ijk}$ (para a modalidade $i$, leitor $j$ e caso $k$) em:

$$Y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}$$

onde:
- $\mu$ é a média global de acurácia;
- $\tau_i$ é o efeito fixo da modalidade tomográfica $i$;
- $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é o efeito aleatório do leitor $j$;
- $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é o efeito aleatório do caso clínico $k$;
- $(\tau R)_{ij} \sim \mathcal{N}(0, \sigma^2_{\tau R})$ é a interação modalidade $\times$ leitor;
- $(\tau C)_{ik} \sim \mathcal{N}(0, \sigma^2_{\tau C})$ é a interação modalidade $\times$ caso;
- $(RC)_{jk} \sim \mathcal{N}(0, \sigma^2_{RC})$ é a interação leitor $\times$ caso;
- $\epsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\epsilon})$ é o erro residual aleatório.

### 3.4.2 Graus de Liberdade Ajustados de Satterthwaite e Teste de Hipóteses
A estatística de teste $F$ para a hipótese de equivalência entre o modelo computacional e os leitores humanos ($H_0: \tau_{\text{modelo}} = \tau_{\text{humano}}$) utiliza a aproximação de Satterthwaite para os graus de liberdade efetivos do denominador ($df_{\text{den}}$):

$$F = \frac{MS(\tau)}{MS(\tau R) + MS(\tau C) - MS(\tau RC)} \sim F(df_{\text{num}}, df_{\text{den}})$$

Exige-se que o Coeficiente de Correlação Intraclasse ($ICC$) atinja $ICC \ge 0{,}90$ com intervalo de confiança de 95% para que o modelo computacional seja aceito como substituto metrológico confiável da avaliação humana.

<div style="page-break-after: always;"></div>

---

# 4 O COLAPSO DA LINEARIDADE, ALGORITMOS DLR E SIMULADORES HÍBRIDOS

## 4.1 Taxonomia e Comparativo Físico dos Algoritmos de Reconstrução

A evolução algorítmica da tomografia computadorizada compreende quatro gerações principais de processamento numérico de sinogramas:

A Tabela 1 detalha os algoritmos comerciais implementados pelos quatro principais fabricantes globais de tomógrafos.

| Fabricante | Reconstrução Iterativa Híbrida (HIR) | Reconstrução Iterativa Baseada em Modelos (MBIR) | Reconstrução por Aprendizado Profundo (DLR) |
| :--- | :--- | :--- | :--- |
| **GE Healthcare** | ASiR / ASiR-V | Veo | **TrueFidelity** (treinado com FBP de dose plena) |
| **Canon Medical** | AIDR 3D / AIDR 3D Enhanced | FIRST | **AiCE** (*Advanced intelligent Clear-IQ Engine*) |
| **Siemens Healthineers** | SAFIRE / ADMIRE | REDUCE | **Precise Image** / **Alpha Engine** (PCCT) |
| **Philips Healthcare** | iDose4 | IMR (*Iterative Model Reconstruction*) | **Precise Image** (redes convolucionais profundas) |

<center><small><b>Tabela 1:</b> Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante.<br>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

### 4.1.1 Filosofia GE Healthcare: TrueFidelity e Mapeamento Direto de FBP
A rede neural profunda do TrueFidelity (GE Healthcare) foi concebida sob uma filosofia de preservação textural estrita. Seu treinamento supervisionado utilizou como alvo (*ground truth*) imagens reconstruídas por FBP adquiridas em dose plena (alta contagem de fótons). Dessa forma, a rede aprende a remover o ruído quântico de exames de baixa dose sem alterar o formato de rampa do $NPS(f)$, preservando a granularidade visual clássica apreciada por radiologistas experientes.

### 4.1.2 Filosofia Canon Medical: AiCE e Treinamento Ancorado em MBIR
O algoritmo AiCE (*Advanced intelligent Clear-IQ Engine*, Canon Medical) adota como alvo de treinamento imagens reconstruídas por MBIR de altíssima qualidade (algoritmo FIRST). Como o MBIR modela a óptica real do feixe e a física do ponto focal, a rede aprende a recuperar frequências espaciais elevadas em bordas ($TTF$ elevada) e atua com forte supressão de ruído em tecidos moles, exigindo calibração criteriosa para evitar a suavização excessiva de microestruturas.

### 4.1.3 Filosofia Siemens Healthineers: Precise Image e Alpha Engine
A Siemens Healthineers desenvolveu redes neurais que atuam de forma combinada no domínio de projeções brutas e no espaço da imagem. Em sistemas PCCT, o algoritmo *Alpha Engine* processa múltiplos sinogramas espectrais simultaneamente, aplicando regularização adaptativa de gradientes que mantém a resolução espacial mesmo em níveis ultrabaixos de dose ($\text{CTDI}_{\text{vol}} < 1{,}0\text{ mGy}$).

### 4.1.4 Filosofia Philips Healthcare: Precise Image em Espaço Híbrido
O sistema Precise Image da Philips utiliza redes convolucionais profundas em múltiplas escalas com camadas residuais, processando dados iterativamente entre o espaço de sinogramas e o domínio espacial para eliminar artefatos de feixe endurecido e espalhamento com baixo custo computacional.

## 4.2 A Quebra da Linearidade, Não-Estacionariedade e o Efeito Ceroso

Em sistemas tomográficos que utilizam reconstruções por aprendizado profundo (DLR) e MBIR, a relação matemática entre as projeções brutas $\mathbf{y}$ e a imagem final $\mathbf{x}$ é estritamente não linear (GREFFIER et al., 2026; DEBBICHE et al., 2024):

$$\mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}$$

Essa não-linearidade acarreta fenômenos físicos complexos, evidenciados na Figura 4:

![Figura 4: Não-Linearidade em Algoritmos DLR, Falha dos Modelos Lineares e Metodologia de Detrending. (A) Detectabilidade $d'$ em função do nível de dose $\text{CTDI}_{\text{vol}}$ para FBP, HIR e DLR. (B) Dispersão e quebra de correlação linear do modelo NPWE ($r = 0{,}68$) versus a alta correlação do modelo DLMO ancorado na percepção de radiologistas ($r = 0{,}98$). (C) Processo de Detrending Polinomial 2D: remoção do gradiente anatômico macroscópico $P_2(x, y)$ para isolamento do ruído quântico puro $\delta I(x, y)$.](assets/fig4_dlr_non_linearity_detrending.png)

<center><em><b>Figura 4:</b> Impacto da não-linearidade em DLR, colapso de modelos analíticos lineares e metodologia de detrending em fundos anatômicos.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

1. **Dependência do Contraste e da Cena:** A resolução espacial da imagem deixa de ser constante, variando dinamicamente de acordo com o contraste do objeto e o nível de ruído local;
2. **Não-Estacionariedade Espacial:** O ruído da imagem não possui propriedades estatísticas homogêneas. Em torno de bordas de alto contraste, o algoritmo preserva frequências espaciais elevadas, enquanto em regiões homogêneas de tecidos moles atua com agressiva remoção de ruído;
3. **Efeito Ceroso (*Plastic/Waxy Look*):** A excessiva concentração de energia do ruído em frequências baixas gera uma textura artificialmente lisa, que mascara lesões sutis de baixo contraste e reduz a sensibilidade de radiologistas (TOIA et al., 2023; GREFFIER et al., 2026);
4. **Colapso dos Modelos Lineares Tradicionais:** O modelo analítico linear NPWE falha em prever a acurácia diagnóstica real sob reconstruções DLR, apresentando dispersão acentuada e baixa correlação ($r \approx 0{,}68$, Painel B da Figura 4).

## 4.3 A Transição dos Simuladores: De Cilindros Homogêneos a Phantoms Antropomórficos Híbridos

Simuladores físicos homogêneos de acrílico ou água (como o *phantom* Catphan®) foram desenvolvidos para a calibração de sistemas FBP lineares. Quando submetidos a algoritmos DLR (que foram treinados predominantemente com anatomias humanas reais), esses simuladores produzem padrões atípicos fora da distribuição de treinamento, invalidando as medições metrológicas (SOLOMON et al., 2020; RACINE et al., 2020).

Para restabelecer o rigor da avaliação física, a física médica adotou a metodologia dos *Phantoms* Antropomórficos Híbridos (Fluxograma 3).

![Fluxograma 3: Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.](assets/flow4_phantom_hibrido_2afc.png)

<center><em><b>Fluxograma 3:</b> Metodologia de Phantoms Híbridos e Validação Psicofísica 2AFC.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

Essa abordagem utiliza simuladores físicos de alta fidelidade tecidual (como o *phantom* FREDDIE) confeccionados por impressão 3D multimaterial para aquisição de fundos anatômicos reais ($H_0$), sobre os quais são inseridos computacionalmente modelos tridimensionais de lesões convolvidas com a PSF tridimensional do tomógrafo ($H_1$). Isso possibilita a geração de milhares de imagens com verdade de campo exata para treinamento de redes e testes psicofísicos humanos.

## 4.4 Tratamento de Ruído em Anatomias Complexas: Detrending Polinomial 2D e Incerteza Bootstrap

Para calcular o espectro de ruído ($NPS$) no parênquima pulmonar ou no abdome de um *phantom* antropomórfico, é necessário remover as variações anatômicas macroscópicas de densidade através da técnica de *Detrending* Polinomial 2D (Painel C da Figura 4):

Para cada sub-região de interesse $I_k(x, y)$, ajusta-se uma superfície polinomial bidimensional de 2ª ordem $P_2(x, y)$ por mínimos quadrados:

$$P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy$$

A matriz de ruído puro residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é então submetida a janelamento de Hanning 2D para cálculo do $NPS$ sem vazamento espectral.

Para estimar o erro padrão e os intervalos de confiança de 95% do índice $d'$ sem impor premissas gaussianas arbitrárias, aplica-se a técnica estatística de reamostragem Bootstrap não-paramétrica com $B = 2000$ replicações com reposição.

<div style="page-break-after: always;"></div>

---

# 5 O ESTADO DA ARTE: OBSERVADORES POR APRENDIZADO PROFUNDO, PCCT E OTIMIZAÇÃO MULTIOBJETIVO

## 5.1 Observadores Baseados em Aprendizado Profundo e Auto-Atenção

Para superar a quebra de linearidade dos algoritmos DLR, a física médica desenvolveu os Observadores de Modelo Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO) (ZHOU et al., 2021; SCHILDER et al., 2026).

Em vez de assumir templates lineares fixos, o DLMO emprega redes neurais profundas com arquitetura *Vision Transformer* (ViT) dotadas de mecanismos de Auto-Atenção Multi-Cabeça (MHSA), conforme esquematizado no Fluxograma 4.

![Fluxograma 4: Arquitetura Neural do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer) e Calibração Perceptual.](assets/flow5_dlmo_architecture.png)

<center><em><b>Fluxograma 4:</b> Arquitetura do Observador DLMO com Mecanismos de Auto-Atenção.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

### 5.1.1 Arquitetura Vision Transformer: Projeção Linear e Patch Embeddings
A imagem tomográfica $\mathbf{x} \in \mathbb{R}^{H \times W \times C}$ é dividida em uma sequência de $N_p = \frac{HW}{P^2}$ blocos bidimensionais não-sobrepostos (*patches*) $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 C)}$, onde $P \times P$ é a dimensão espacial de cada bloco. Cada bloco é projetado linearmente para um espaço latente de dimensão $D_{\text{model}}$ através de uma matriz treinável $\mathbf{E}$:

$$\mathbf{z}_0 = \left[ \mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \mathbf{x}_p^2 \mathbf{E}; \, \dots; \, \mathbf{x}_p^{N_p} \mathbf{E} \right] + \mathbf{E}_{\text{pos}}$$

onde $\mathbf{x}_{\text{class}}$ é o token especial de decisão e $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N_p + 1) \times D_{\text{model}}}$ codifica as coordenadas espaciais 2D absolutas.

### 5.1.2 Mecanismo de Auto-Atenção Multi-Cabeça e Conexão Neurofisiológica
A auto-atenção permite à rede computacional aprender correlações espaciais globais e locais simultaneamente. Para cada bloco, calculam-se as projeções de Consulta ($Q$), Chave ($K$) e Valor ($V$):

$$Q = \mathbf{z} \mathbf{W}_Q, \qquad K = \mathbf{z} \mathbf{W}_K, \qquad V = \mathbf{z} \mathbf{W}_V$$

A equação de auto-atenção escalonada por produto escalar é expressa por:

$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V$$

onde o fator $\sqrt{d_k}$ evita a saturação dos gradientes na função softmax.

Do ponto de vista neurofisiológico, essa formulação matemática mimetiza a interação foveal-periférica dos radiologistas: a matriz de atenção pondera áreas anatômicas distantes para inferir o contexto anatômico de fundo enquanto focaliza recursos computacionais na detecção foveal da lesão central.

A estatística de teste não linear $t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$ permite calcular o índice de detectabilidade não linear:

$$d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}$$

## 5.2 Calibração Perceptual com Radiologistas e Transferibilidade Leave-One-Scanner-Out

Para que o modelo DLMO funcione como um instrumento metrológico clinicamente representativo, ele não deve ser treinado apenas como um classificador matemático puro, mas sim calibrado através de uma função de perda perceptual multitarefa ancorada em leituras humanas:

$$\mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{classificação}}(y, \hat{y}) + \lambda \, \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2$$

onde $\mathcal{L}_{\text{classificação}}$ garante a acurácia na separação de classes e o segundo termo penaliza desvios em relação à detectabilidade medida no painel de radiologistas em testes 2AFC.

A capacidade de generalização do modelo é testada pelo método *Leave-One-Scanner-Out* (LOSO), onde a rede é treinada com dados de $K - 1$ tomógrafos e testada cegamente no tomógrafo restante, garantindo robustez inter-institucional.

## 5.3 Física da Tomografia Computadorizada por Contagem de Fótons

A Tomografia Computadorizada por Contagem de Fótons (*Photon-Counting CT* - PCCT) representa o salto tecnológico mais expressivo da tomografia na última década (MCCOLLOUGH et al., 2026; PIMENTA; COSTA, 2025; PIMENTA, 2026).

A Tabela 2 sintetiza as diferenças fundamentais entre a tecnologia clássica (EICT) e os detectores de contagem de fótons (PCCT).

| Característica Física | TC por Integração de Energia (EICT) | TC por Contagem de Fótons (PCCT) |
| :--- | :--- | :--- |
| **Material Detector** | Cintilador cerâmico ($\text{Gd}_2\text{O}_2\text{S}$) + Fotodiodo | Semicondutor de conversão direta (CdTe / CZT / Silício) |
| **Mecanismo de Conversão** | Indireta: Raios X $\to$ Luz visível $\to$ Carga elétrica | Direta: Raios X $\to$ Pares elétron-lacuna instantâneos |
| **Ruído Eletrônico** | Integrado cumulativamente ao sinal de raios X | Rejeitado por limiar inferior de energia ($E_{\text{threshold}} > E_{\text{ruído}}$) |
| **Resolução Espacial** | Limitada por septos ópticos refletivos ($0{,}5 \text{ a } 0{,}6 \text{ mm}$) | Submilimétrica ultra-alta ($0{,}1 \text{ a } 0{,}2 \text{ mm}$, sem septos físicos) |
| **Ponderação Espectral** | Proporcional à energia do fóton ($S \propto E$, subpondera baixa energia) | Contagem individual com peso unitário ou peso ideal ótimo |
| **Capacidade Espectral** | Requer duas fontes/camadas de detectores | Intrínseca: Múltiplos canais de energia (*energy bins*) em único disparo |

<center><small><b>Tabela 2:</b> Comparativo físico entre as tecnologias de detecção tomográfica EICT e PCCT.<br>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

### 5.3.1 Detectores Semicondutores de Conversão Direta: CdTe versus Silício
Enquanto os detectores tradicionais EICT dependem da conversão de raios X em luz visível dentro de cristais cintiladores cerâmicos (processo que induz espalhamento óptico e exige septos refletores entre pixels), os detectores PCCT utilizam cristais semicondutores espessos (de 1,5 a 3,0 mm de Telureto de Cádmio - CdTe, CZT ou Silício polarizados sob alta tensão de -800 V a -1000 V). A absorção fotoelétrica de cada fóton incidente gera imediatamente uma nuvem de pares elétron-lacuna que migra em nanossegundos em direção aos ânodos pixelados, produzindo um pulso elétrico cuja amplitude de corrente é estritamente proporcional à energia do fóton:

$$V_{\text{pulso}} \propto Q = \frac{E_{\text{fóton}}}{W_{\text{ionização}}}$$

onde $W_{\text{ionização}} \approx 4{,}43 \text{ eV}$ para o CdTe (comparado aos $30 \text{ eV}$ necessários para gerar um elétron em cintiladores convencionais).

### 5.3.2 Fenômenos Estocásticos: Charge Sharing e Pulse Pile-Up
Apesar de sua eficiência, dois fenômenos estocásticos complexos desafiam a modelagem metrológica em PCCT:
1. **Compartilhamento de Carga (*Charge Sharing*):** Quando um fóton de raios X interage próximo à borda entre dois micropixels, a nuvem de elétrons em expansão divide-se entre ânodos adjacentes, gerando múltiplos pulsos de menor amplitude (*charge splitting*). Sistemas avançados compensam esse efeito através de circuitos de adição de carga em tempo real (*Charge-Sharing Correction*);
2. **Empilhamento de Pulsos (*Pulse Pile-Up*):** Em altas taxas de exposição tomográfica ($> 10^7 \text{ fótons}/(\text{mm}^2\cdot\text{s})$), múltiplos fótons atingem o mesmo pixel antes que o circuito integrador retorne à linha de base, causando contagens subestimadas e distorções espectrais na altura do pulso.

### 5.3.3 Compartimentalização de Energia e Imagens Monoenergéticas Virtuais
A discriminação eletrônica dos pulsos em múltiplos comparadores com limiares de energia programáveis ($E_1, E_2, E_3, E_4$) permite a decomposição das projeções tomográficas na base de materiais fundamentais (efeito fotoelétrico e espalhamento Compton), viabilizando a síntese de Imagens Monoenergéticas Virtuais ($VMI$) em qualquer energia nominal desejada (de 40 a 140 keV):

$$I_{\text{VMI}}(x, y; E_0) = a_1(x, y) \cdot f_{\text{foto}}(E_0) + a_2(x, y) \cdot f_{\text{Compton}}(E_0)$$

Em baixas energias nominais ($40 \text{ a } 50 \text{ keV}$), maximiza-se a absorção fotoelétrica do iodo ($K\text{-edge} = 33{,}2 \text{ keV}$), elevando substancialmente a $TTF$ de pequenas lesões vasculares e neoplásicas. Como a PCCT rejeita totalmente o ruído eletrônico, é possível sintetizar imagens de 40 keV sem a explosão de ruído estocástico que inviabilizava essa técnica nos tomógrafos EICT convencionais.

## 5.4 Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional

A otimização tradicional de protocolos limitava-se a buscar o equilíbrio entre dose e qualidade de imagem. Contudo, em ambientes hospitalares de alta rotatividade (prontos-socorros e centros de trauma), o tempo operacional total ($T = T_{\text{aq}} + T_{\text{rec}}$) é uma variável determinante (OOSTVEEN et al., 2021).

A física médica moderna modela esse cenário como um problema de Otimização Multiobjetivo Não Linear:

$$\min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}$$

sujeito às restrições clínicas formais:
- $D(\mathbf{p}) \le \text{DRL}$ (restrição de dose de radioproteção);
- $T(\mathbf{p}) \le T_{\text{máx}}$ (restrição operacional de tempo em emergência);
- $W(\mathbf{p}) = d'(\mathbf{p}) \ge d'_{\text{mín}}$ (restrição diagnóstica de detectabilidade).

A Figura 5 apresenta o mapeamento da Fronteira de Pareto nos domínios bidimensional e tridimensional.

![Figura 5: Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto. (A) Trade-off bidimensional entre Dose e Detectabilidade, ilustrando soluções ótimas na fronteira e protocolos dominados ineficientes. (B) Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando Dose de Radiação ($D$), Tempo Operacional total ($T$) e Detectabilidade Diagnóstica ($W = d'$).](assets/fig5_dlmo_pareto_3d.png)

<center><em><b>Figura 5:</b> Fronteira de Pareto Tridimensional $(D, T, -W)$ para Otimização Multiobjetivo de Protocolos de TC.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

O mapeamento dessa superfície de soluções não-dominadas é realizado através do Algoritmo Genético NSGA-II acoplado ao método de tomada de decisão multicritério TOPSIS, permitindo escolher o protocolo ótimo para cada perfil institucional (pediátrico de ultrabaixa dose, emergência ultrarrápida ou oncologia de alta resolução).

<div style="page-break-after: always;"></div>

---

# 6 ARQUITETURA COMPUTACIONAL, METROLOGIA EXPERIMENTAL E ASPECTOS ÉTICOS

## 6.1 Arquitetura de Software do Pipeline Integrado de Metrologia

A infraestrutura computacional deste trabalho foi concebida de forma modular em linguagem Python (utilizando NumPy, SciPy, PyDICOM e PyTorch), integrada aos pipelines do grupo GDRFM-IFUSP, conforme detalhado no Fluxograma 5.

![Fluxograma 5: Arquitetura Modular do Software de Metrologia em Tomografia Computadorizada (Pipeline Integrado GDRFM-IFUSP).](assets/flow6_software_pipeline.png)

<center><em><b>Fluxograma 5:</b> Arquitetura Modular do Pipeline Computacional de Metrologia em TC.</em><br><small>Fonte: Elaborado pelo autor (2026).</small></center>

<br>

O software é composto por cinco módulos encadeados:
- **Módulo 1:** Parser DICOM e validação de metadados de aquisição;
- **Módulo 2:** Segmentação automática dos insertos de calibração e amostragem de mosaicos com $M \ge 100$ ROIs independentes;
- **Módulo 3A:** Cálculo da resolução espacial da tarefa ($ESF \to LSF \to TTF \to f_{50}$);
- **Módulo 3B:** *Detrending* polinomial 2D e cálculo do espectro de ruído ($NPS(u, v)$ e $NPS(f)$);
- **Módulo 4:** Cálculo da detectabilidade via observadores lineares (NPWE e CHO) e modelos por aprendizado profundo (DLMO);
- **Módulo 5:** Análise de incerteza por Bootstrap e otimização da Fronteira de Pareto 3D via algoritmo NSGA-II e método TOPSIS.

## 6.2 Protocolo Metrológico Padronizado segundo o Relatório AAPM TG-233

As aquisições tomográficas para calibração seguem as diretrizes internacionais da AAPM (SAMEI et al., 2019):
- Matriz de imagem de $512 \times 512$ pixels com FOV ajustado ao diâmetro do simulador ($200 \text{ a } 350 \text{ mm}$);
- Espessuras de corte de $0{,}5 \text{ a } 1{,}0 \text{ mm}$ para alta resolução e $2{,}5 \text{ a } 5{,}0 \text{ mm}$ para rotina clínica;
- Tensões de tubo de 80, 100, 120 e 140 kVp, cobrindo doses de $\text{CTDI}_{\text{vol}}$ de $0{,}5 \text{ mGy}$ a $15 \text{ mGy}$;
- Modelagem de lesões esféricas padronizadas com diâmetros de 3, 5, 8 e 10 mm e contrastes clínicos de $-600 \text{ HU}$ (nódulo subsólido pulmonar), $+100 \text{ HU}$ (nódulo sólido hiperatenuante) e $+30 \text{ HU}$ (lesão hepática de baixo contraste).

## 6.3 Aspectos Bioéticos, Regulatórios e Desenho Experimental com Seres Humanos

A condução dos testes psicofísicos 2AFC com médicos radiologistas para obtenção dos dados de calibração exige aprovação formal em Comitê de Ética em Pesquisa (CEP/CONEP):
- Recrutamento de no mínimo 20 médicos radiologistas com título de especialista pelo CBR para cada anatomia clínica avaliada ($\ge 60$ leitores no total para tórax, abdome e crânio);
- Aplicação obrigatória de Termo de Consentimento Livre e Esclarecido (TCLE) com garantia de anonimização dos dados de desempenho individual;
- Monitores diagnósticos com luminância calibrada segundo o padrão DICOM GSDF ($\ge 400 \text{ cd/m}^2$) e iluminação ambiente controlada ($< 15 \text{ lux}$);
- Mitigação de fadiga visual através de sessões curtas com no máximo 100 a 150 pares de imagens 2AFC por sessão (duração inferior a 25 minutos).

<div style="page-break-after: always;"></div>

---

# 7 CONSIDERAÇÕES FINAIS E PERSPECTIVAS

## 7.1 Síntese da Trajetória Biofísica e Metrológica

A trajetória da avaliação da qualidade de imagem em tomografia computadorizada reflete a constante superação de abstrações matemáticas lineares simplificadas em direção à modelagem da complexidade biofísica:

1. **A Fase Linear Analítica (1950–1990):** Partiu da teoria de detecção de sinais e do Observador Ideal Bayesiano, introduzindo filtros oculares (NPWE) para simular as limitações fisiológicas humanas em fundos uniformes;
2. **A Modelagem Cortical (1990–2015):** Desenvolveu o Observador de Hotelling Canalizado (CHO), utilizando canais de frequência inspirados na arquitetura do córtex visual primário para superar o ruído estrutural de fundos anatômicos;
3. **A Ruptura da Linearidade (2015–2026):** A introdução clínica de algoritmos de reconstrução por aprendizado profundo (DLR) quebrou as premissas de invariância espacial e estacionariedade, expondo os limites dos modelos analíticos tradicionais;
4. **O Paradigma da Inteligência Artificial Perceptual e Otimização Multiobjetivo (2026+):** A emergência dos observadores computacionais por aprendizado profundo com mecanismos de auto-atenção (DLMO), calibrados diretamente contra a percepção de radiologistas e integrados a espaços de decisão tridimensionais $(D, T, -W)$.

## 7.2 Impacto Clínico, Operacional e Normativo

A consolidação dessas ferramentas computacionais produz impacto prático imediato:
- **Segurança Radiológica Personalizada:** Comprova cientificamente que reduções expressivas de dose preservam a detectabilidade diagnóstica de lesões clínicas sutis;
- **Auditoria e Comissionamento Hospitalar:** Fornece rotinas automatizadas para que serviços de física médica realizem auditorias em conformidade com o relatório AAPM TG-233 e com o sistema internacional IAEA 5-Star;
- **Harmonização de Parques Tecnológicos:** Permite equalizar o desempenho diagnóstico entre tomógrafos de diferentes fabricantes e gerações tecnológicas.

## 7.3 Articulação com a Pesquisa de Doutorado Direto (FAPESP 2026–2030)

Esta monografia de conclusão de curso cumpre o papel fundamental de consolidar o embasamento teórico, biofísico, matemático e computacional que sustenta o projeto de pesquisa de Doutorado Direto do autor (FAPESP 2026–2030) no Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP:

O trabalho articula-se com os avanços em PCCT da Dra. Elsa Pimenta (Doutorado 2026) e com o pipeline de automação linear no tórax de Davi Amaral (Mestrado FAPESP), estabelecendo as seguintes metas para a tese de doutorado:
a) Treinamento e validação experimental do observador DLMO baseado em *Vision Transformers*;
b) Execução do estudo psicofísico nacional 2AFC com mais de 60 radiologistas especialistas sob modelagem ANOVA MRMC;
c) Validação cruzada de transferibilidade inter-scanners (*leave-one-scanner-out*) em sete tomógrafos de quatro fabricantes distintos no InRad-HCFMUSP e Radboudumc;
d) Mapeamento experimental completo da Fronteira de Pareto Tridimensional $(D, T, -W)$ para os principais protocolos tomográficos de crânio, tórax e abdome em sistemas EICT e PCCT.

Conclui-se, assim, este trabalho acadêmico com a convicção de que a física médica brasileira continua contribuindo para a vanguarda científica internacional, unindo o rigor analítico da física à missão de preservar vidas humanas.

<div style="page-break-after: always;"></div>

---

# REFERÊNCIAS

ABBEY, C. K.; BARRETT, H. H. Human- and model-observer performance in ramp-spectrum noise with regularization. **Journal of the Optical Society of America A**, v. 18, n. 3, p. 473-488, 2001.

AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). **Instrução Normativa nº 93, de 27 de maio de 2021**: Estabelece os requisitos sanitários para a garantia da qualidade e da segurança em sistemas de tomografia computadorizada médica. Brasília: ANVISA, 2021.

AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). **Resolução da Diretoria Colegiada - RDC nº 611, de 9 de março de 2022**: Estabelece os requisitos sanitários para a organização e o funcionamento de serviços de radiologia diagnóstica ou intervencionista. Brasília: ANVISA, 2022.

AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). **Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233**. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., Medical Physics, v. 46, n. 11, p. e735-e756, 2019).

ATTIX, F. H. **Introduction to Radiological Physics and Radiation Dosimetry**. New York: John Wiley & Sons, 1986. 607 p.

BARRETT, H. H.; MYERS, K. J. **Foundations of Image Science**. Hoboken: John Wiley & Sons, 2004. 1540 p.

BARRETT, H. H.; YAO, J.; ROLAND, P. X.; MYERS, K. J. Model observers for assessment of image quality. **Physics in Medicine & Biology**, v. 38, n. 2, p. 277-295, 1993.

BURGESS, A. E. Statistically defined backgrounds: performance of a modified nonprewhitening observer model. **Journal of the Optical Society of America A**, v. 11, n. 4, p. 1237-1242, 1994.

BURGESS, A. E. The Rose model, revisited. **Journal of the Optical Society of America A**, v. 16, n. 3, p. 633-646, 1999.

BURGESS, A. E. Visual perception studies and observer models in medical imaging. **Seminars in Nuclear Medicine**, v. 41, n. 6, p. 419-436, 2011.

BUSHBERG, J. T.; SEIBERT, J. A.; LEIDHOLDT, E. M.; BOONE, J. M. **The Essential Physics of Medical Imaging**. 4. ed. Philadelphia: Lippincott Williams & Wilkins, 2020. 1048 p.

CHOOPANI, R. et al. Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. **Physics in Medicine & Biology**, v. 68, n. 14, p. 145002, 2023.

DEBBICHE, I. et al. Task-based image quality assessment of deep learning image reconstruction in abdominal CT: a multi-reader phantom study. **European Radiology**, v. 34, n. 5, p. 3120-3132, 2024.

DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E. Receiver operating characteristic rating analysis: generalization to the population of readers and patients with the jackknife method. **Investigative Radiology**, v. 27, n. 9, p. 723-731, 1992.

DOSOVITSKIY, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: **International Conference on Learning Representations (ICLR)**, 2021. p. 1-21.

ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P. Role of knowledge in human visual search for signals in noise. **Journal of the Optical Society of America A**, v. 17, n. 11, p. 2064-2076, 2000.

FLOHR, T. et al. Photon-counting CT review. **Physica Medica**, v. 79, p. 126-136, 2020.

GREFFIER, J. et al. Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. **Diagnostic and Interventional Imaging**, v. 107, n. 1, p. 1016-1025, 2026.

GREFFIER, J. et al. Comparison of iterative and deep learning reconstruction algorithms in low-dose abdominal CT: a task-based image quality study on a phantom. **European Radiology**, v. 33, p. 7890-7901, 2023.

HILLIS, S. L.; OBUCHOWSKI, N. A.; BERBAUM, K. S. Multi-reader multi-case ROC analysis: an updated review of methods and software. **Academic Radiology**, v. 18, n. 7, p. 842-856, 2011.

INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA). Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. **European Journal of Radiology**, v. 184, p. 113133, 2026.

INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION (ICRP). **The 2007 Recommendations of the International Commission on Radiological Protection**. ICRP Publication 103. Annals of the ICRP, v. 37, n. 2-4, p. 1-332, 2007.

INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). **Medical Imaging - The Assessment of Image Quality**. ICRU Report 54. Bethesda, MD: ICRU, 1996.

KNOLL, G. F. **Radiation Detection and Measurement**. 4. ed. Hoboken: John Wiley & Sons, 2010. 860 p.

LUSTED, L. B. **Introduction to Medical Decision Making**. Springfield, IL: Charles C Thomas, 1968.

MCCOLLOUGH, C. H. et al. Radiation dose in computed tomography: technological advances and clinical optimization over two decades. **Radiology**, v. 318, n. 2, p. e251200, 2026.

METZ, C. E. ROC methodology in radiologic imaging. **Investigative Radiology**, v. 21, n. 9, p. 720-733, 1986.

MYERS, K. J.; BARRETT, H. H. Addition of a channel mechanism to the ideal-observer model. **Journal of the Optical Society of America A**, v. 4, n. 12, p. 2447-2457, 1987.

OBUCHOWSKI, N. A.; ROCKETTE, H. E. Hypothesis testing of diagnostic accuracy for multiple readers and multiple tests: an ANOVA approach with dependent observations. **Communications in Statistics - Simulation and Computation**, v. 24, n. 2, p. 285-308, 1995.

OOSTVEEN, L. J. et al. Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. **European Radiology**, v. 31, p. 7412-7421, 2021.

PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. **Transactions of the IRE Professional Group on Information Theory**, v. 4, n. 4, p. 171-212, 1954.

PIMENTA, E. F.; COSTA, P. R. Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. **Medical Physics**, v. 52, n. 4, p. 2150-2165, 2025.

PIMENTA, E. F. **Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax**. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.

RACINE, D. et al. Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. **Physics in Medicine & Biology**, v. 65, n. 18, p. 185011, 2020.

RACINE, D. et al. Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. **Medical Physics**, v. 48, n. 6, p. 2890-2901, 2021.

ROSE, A. The sensitivity performance of the human eye on an absolute scale. **Journal of the Optical Society of America**, v. 38, n. 2, p. 196-208, 1948.

SAMEI, E. et al. Assessment of image quality in CT: from physical measurements to task-based performance. **Medical Physics**, v. 46, n. 11, p. e735-e756, 2019.

SCHILDER, C. M. et al. Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. **La Rivista del Nuovo Cimento**, v. 49, n. 3, p. 145-210, 2026.

SEERAM, E. **Computed Tomography: Physical Principles, Clinical Applications, and Quality Control**. 4. ed. St. Louis: Elsevier Health Sciences, 2015. 560 p.

SOLOMON, J. et al. Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. **Medical Physics**, v. 47, n. 8, p. 3412-3425, 2020.

TOIA, G. V. et al. Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. **European Radiology**, v. 33, p. 4310-4322, 2023.

WAGNER, R. F.; BROWN, D. G.; METZ, C. E. Application of information theory to the assessment of computed tomography. **Medical Physics**, v. 6, n. 2, p. 83-94, 1979.

YAO, J.; BARRETT, H. H. Predicting human performance by a channelized Hotelling observer model. In: **SPIE Medical Imaging: Image Perception**, v. 1654, p. 268-278, 1992.

ZHOU, W. et al. Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. **IEEE Transactions on Medical Imaging**, v. 40, n. 9, p. 2350-2362, 2021.
"""

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Master Monograph written successfully to {target_path}")
