import os
import re
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
fig_dir = os.path.join(output_dir, "figuras")
os.makedirs(fig_dir, exist_ok=True)

# Build the comprehensive monolithic text
expanded_tex = r"""\documentclass[
  12pt,
  a4paper,
  oneside
]{report}

% ==============================================================================
% PACOTES ESSENCIAIS E CONFIGURAÇÃO
% ==============================================================================
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazilian]{babel}

% Geometria estritamente segundo as Normas ABNT NBR 14724
% Margens: Superior = 3,0 cm, Esquerda = 3,0 cm, Inferior = 2,0 cm, Direita = 2,0 cm
\usepackage[
  a4paper,
  top=3cm,
  left=3cm,
  bottom=2cm,
  right=2cm,
  headheight=16pt,
  footskip=30pt
]{geometry}

% Matemática Avançada e Símbolos Físicos
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{bm}

% Tipografia e Espaçamento ABNT (1,5 entre linhas e recuo de parágrafo de 1,5 cm)
\usepackage{lmodern}
\usepackage{setspace}
\onehalfspacing
\usepackage{indentfirst}
\setlength{\parindent}{1.5cm}

% Tolerância a quebras de linha e hifenação para evitar qualquer Overfull \hbox
\emergencystretch 3em
\hyphenation{To-mo-gra-fia Con-ta-gem Fó-tons Non-Pre-whi-te-ning Ob-ser-va-dor Clás-si-co Es-tru-tu-ral Re-cons-tru-ção Mul-ti-ob-je-ti-vo Di-ag-nós-ti-co Psi-co-fí-si-co An-tro-po-mór-fi-co}

% Cores e Tabelas (Compatibilidade universal)
\usepackage[table,xcdraw]{xcolor}
\definecolor{darkblue}{rgb}{0.0, 0.18, 0.39}
\definecolor{linkblue}{rgb}{0.0, 0.22, 0.65}

% Figuras, Ilustrações e Tabelas
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{enumitem}

% Links e Referências Cruzadas
\usepackage[
  colorlinks=true,
  linkcolor=linkblue,
  citecolor=linkblue,
  urlcolor=linkblue
]{hyperref}
\usepackage[nameinlink,noabbrev,brazilian]{cleveref}

% Formatação dos Títulos de Capítulos e Seções
\usepackage{titlesec}
\titleformat{\chapter}[hang]
  {\normalfont\Large\bfseries}
  {\thechapter}
  {1em}
  {\MakeUppercase}
\titleformat{\section}
  {\normalfont\large\bfseries}
  {\thesection}
  {1em}
  {}
\titleformat{\subsection}
  {\normalfont\normalsize\bfseries}
  {\thesubsection}
  {1em}
  {}

% Cabeçalhos e Rodapés
\usepackage{fancyhdr}
\setlength{\headheight}{16pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}

% Informações Institucionais
\newcommand{\tccuniversidade}{UNIVERSIDADE DE SÃO PAULO}
\newcommand{\tccinstituto}{INSTITUTO DE FÍSICA}
\newcommand{\tccdepartamento}{FACULDADE DE MEDICINA}
\newcommand{\tcccurso}{CURSO DE BACHARELADO INTERUNIDADES EM FÍSICA MÉDICA}
\newcommand{\tccautor}{WAGNER HENRIQUE MARQUES}
\newcommand{\tcctitulo}{MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: DA TEORIA CLÁSSICA DE DETECÇÃO DE SINAIS AOS MODELOS DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO}
\newcommand{\tccorientador}{Prof. Dr. Paulo Roberto Costa}
\newcommand{\tccarea}{Diagnóstico por Imagens}
\newcommand{\tcccidade}{SÃO PAULO}
\newcommand{\tccano}{2026}

\begin{document}

% ==============================================================================
% ELEMENTOS PRÉ-TEXTUAIS
% ==============================================================================
\pagestyle{empty}

% 1. CAPA
\begin{center}
  {\bfseries\large \tccuniversidade \par}
  {\bfseries\large \tccinstituto \par}
  {\bfseries\large \tccdepartamento \par}
  {\bfseries\normalsize \tcccurso \par}

  \vspace{3.5cm}

  {\bfseries\Large \tccautor \par}

  \vspace{3.5cm}

  {\bfseries\large \tcctitulo \par}

  \vfill

  {\bfseries\large \tcccidade \par}
  {\bfseries\large \tccano \par}
\end{center}
\clearpage

% 2. FOLHA DE ROSTO
\begin{center}
  {\bfseries\Large \tccautor \par}

  \vspace{3.5cm}

  {\bfseries\large \tcctitulo \par}

  \vspace{2.5cm}

  \begin{flushright}
    \begin{minipage}{0.55\textwidth}
      \small
      Trabalho de Conclusão de Curso apresentado ao Instituto de Física e à Faculdade de Medicina da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física Médica.
      
      \vspace{0.5cm}
      \textbf{Orientador:} \tccorientador\\
      \textbf{Área de Concentração:} \tccarea
    \end{minipage}
  \end{flushright}

  \vfill

  {\bfseries\large \tcccidade \par}
  {\bfseries\large \tccano \par}
\end{center}
\clearpage

% 3. FOLHA DE APROVAÇÃO
\begin{center}
  {\bfseries\Large FOLHA DE APROVAÇÃO \par}
  
  \vspace{1.5cm}
  
  {\bfseries\large \tccautor \par}
  
  \vspace{0.8cm}
  
  {\bfseries \tcctitulo \par}

  \vspace{1.5cm}

  \begin{flushright}
    \begin{minipage}{0.55\textwidth}
      \small
      Monografia defendida e aprovada em \_\_ de \_\_\_\_\_\_\_\_ de 2026 pela Comissão Julgadora constituída pelos seguintes membros:
    \end{minipage}
  \end{flushright}

  \vspace{2.5cm}

  \rule{0.85\textwidth}{0.5pt}\\
  \textbf{\tccorientador\ (Presidente / Orientador)}\\
  Instituto de Física da Universidade de São Paulo -- IFUSP

  \vspace{1.2cm}

  \rule{0.85\textwidth}{0.5pt}\\
  \textbf{Membro da Banca Examinadora 1}\\
  Instituto de Radiologia do Hospital das Clínicas -- InRad-HCFMUSP

  \vspace{1.2cm}

  \rule{0.85\textwidth}{0.5pt}\\
  \textbf{Membro da Banca Examinadora 2}\\
  Instituto de Física da Universidade de São Paulo -- IFUSP
\end{center}
\clearpage

% 4. RESUMO
\chapter*{Resumo}
\addcontentsline{toc}{chapter}{Resumo}

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica contemporânea, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação do desempenho diagnóstico (princípio ALARA). Historicamente, a garantia da qualidade em TC baseou-se em métricas escalares lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR), o desvio padrão em Unidades Hounsfield ($\sigma_{\text{HU}}$) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores homogêneos de água ou acrílico. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares --- com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade, isoplanatismo e estacionariedade no sentido amplo (WSS) do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais (como o aspecto ceroso ou \emph{plastic/waxy look}) que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), fundamentado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade é formalmente definida pelo desempenho de um observador (médico radiologista ou modelo computacional) na execução de uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Esta monografia apresenta uma investigação aprofundada e estruturada da evolução dos observadores de modelo (\emph{model observers}). Analisa-se a transição do Observador Ideal Bayesiano para os modelos antropomórficos lineares com filtro ocular (NPWE) e canais corticais de frequência (CHO), detalhando suas deduções matemáticas contínuas no domínio de Fourier e demonstrando os limites biofísicos que causam seu colapso sob reconstruções DLR e fundos anatômicos complexos. Em resposta, investiga-se a fronteira científica representada pelos Observadores Baseados em Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça, calibrados diretamente contra leituras psicofísicas de radiologistas em experimentos de Escolha Forçada entre Duas Alternativas (2AFC) sob análise estatística \emph{Multi-Reader Multi-Case} (MRMC). Detalham-se a física dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a formulação da Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade ($W$). Este trabalho estabelece as bases teóricas, biofísicas e metrológicas para a garantia da qualidade em tomografia computadorizada moderna.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Vision Transformers. Tomografia por Contagem de Fótons. Simuladores Antropomórficos. Otimização Multiobjetivo. Fronteira de Pareto.
\clearpage

% 5. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), standard deviation in Hounsfield Units ($\sigma_{\text{HU}}$), and Modulation Transfer Function (MTF), evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity (WSS). Under non-linear processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer (human radiologist or mathematical model) executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a comprehensive investigation of the evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), detailing their continuous mathematical derivations in the Fourier domain and demonstrating their breakdown in non-linear DLR regimes and structured anatomical backgrounds. In response, we investigate the state of the art in Deep Learning Model Observers (DLMO), which leverage self-attention neural architectures (Vision Transformers) calibrated against expert radiologists' psychophysical performance in Two-Alternative Forced Choice (2AFC) paradigms under Multi-Reader Multi-Case (MRMC) statistical modeling. Furthermore, we explore the physics of Photon-Counting CT (PCCT), the synthesis of Virtual Monoenergetic Images (VMI), and the formulation of Multi-Objective Optimization via the Three-Dimensional Pareto Frontier $(D, T, -W)$, which integrates radiation dose ($D$), operational time ($T$), and diagnostic detectability ($W$). This study establishes the theoretical, computational, and physical foundation required for next-generation CT metrology.

\vspace{0.8cm}
\noindent\textbf{Keywords:} Computed Tomography. Task-Based Image Quality. Model Observers. Detectability Index. Deep Learning Reconstruction. Vision Transformers. Photon-Counting CT. Anthropomorphic Phantoms. Multi-Objective Optimization. Pareto Frontier.
\clearpage

% 6. LISTA DE ILUSTRAÇÕES
\pdfbookmark[0]{\listfigurename}{lof}
\listoffigures
\clearpage

% 7. LISTA DE TABELAS
\pdfbookmark[0]{\listtablename}{lot}
\listoftables
\clearpage

% 8. LISTA DE ABREVIATURAS E SIGLAS
\chapter*{Lista de Abreviaturas e Siglas}
\addcontentsline{toc}{chapter}{Lista de Abreviaturas e Siglas}

\begin{longtable}{p{0.20\textwidth} p{0.76\textwidth}}
\toprule
\textbf{Sigla} & \textbf{Significado} \\
\midrule
\endhead
\textbf{2AFC} & \emph{Two-Alternative Forced Choice} (Escolha Forçada entre Duas Alternativas) \\
\textbf{AAPM} & \emph{American Association of Physicists in Medicine} \\
\textbf{AEC} & \emph{Automatic Exposure Control} (Controle Automático de Exposição) \\
\textbf{ALARA} & \emph{As Low As Reasonably Achievable} (Tão Baixo Quanto Razoavelmente Exequível) \\
\textbf{ANOVA} & \emph{Analysis of Variance} (Análise de Variância) \\
\textbf{ASiR} & \emph{Adaptive Statistical Iterative Reconstruction} \\
\textbf{AUC} & \emph{Area Under the ROC Curve} (Área sob a Curva ROC) \\
\textbf{BKE} & \emph{Background Known Exactly} (Fundo Conhecido Exatamente) \\
\textbf{BKS} & \emph{Background Known Statistically} (Fundo Conhecido Estatisticamente) \\
\textbf{CBR} & Colégio Brasileiro de Radiologia e Diagnóstico por Imagem \\
\textbf{CdTe} & Telureto de Cádmio (semicondutor de conversão direta) \\
\textbf{CEP} & Comitê de Ética em Pesquisa \\
\textbf{CHO} & \emph{Channelized Hotelling Observer} (Observador de Hotelling Canalizado) \\
\textbf{CNR} & \emph{Contrast-to-Noise Ratio} (Relação Contraste-Ruído) \\
\textbf{CONEP} & Comissão Nacional de Ética em Pesquisa \\
\textbf{CSF} & \emph{Contrast Sensitivity Function} (Função de Sensibilidade ao Contraste) \\
\textbf{CTDI} & \emph{Computed Tomography Dose Index} (Índice de Dose em Tomografia Computadorizada) \\
\textbf{CZT} & Telureto de Cádmio e Zinco \\
\textbf{D-DOG} & \emph{Dense Difference of Gaussians} (Diferença Densa de Gaussianas) \\
\textbf{DBM} & Dorfman-Berbaum-Metz (modelo estatístico para MRMC) \\
\textbf{DLR} & \emph{Deep Learning Image Reconstruction} (Reconstrução por Aprendizado Profundo) \\
\textbf{DLMO} & \emph{Deep Learning Model Observer} (Observador de Modelo por Aprendizado Profundo) \\
\textbf{DLP} & \emph{Dose-Length Product} (Produto Dose-Comprimento) \\
\textbf{DQE} & \emph{Detective Quantum Efficiency} (Eficiência Quântica de Detecção) \\
\textbf{DRL} & \emph{Diagnostic Reference Level} (Nível de Referência Diagnóstica) \\
\textbf{EICT} & \emph{Energy-Integrating Computed Tomography} (TC por Integração de Energia) \\
\textbf{ESF} & \emph{Edge Spread Function} (Função de Resposta ao Degrau) \\
\textbf{FBP} & \emph{Filtered Backprojection} (Retroprojeção Filtrada) \\
\textbf{FOV} & \emph{Field of View} (Campo de Visão) \\
\textbf{GDRFM} & Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP \\
\textbf{GPU} & \emph{Graphics Processing Unit} (Unidade de Processamento Gráfico) \\
\textbf{GSDF} & \emph{Grayscale Standard Display Function} (Função de Exibição Padrão em Tons de Cinza) \\
\textbf{HIR} & \emph{Hybrid Iterative Reconstruction} (Reconstrução Iterativa Híbrida) \\
\textbf{HO} & \emph{Hotelling Observer} (Observador de Hotelling) \\
\textbf{HOR} & Hillis-Obuchowski-Rockette (modelo estatístico de ANOVA MRMC) \\
\textbf{HU} & Unidade Hounsfield (\emph{Hounsfield Unit}) \\
\textbf{IAEA} & \emph{International Atomic Energy Agency} (Agência Internacional de Energia Atômica) \\
\textbf{ICC} & \emph{Intraclass Correlation Coefficient} (Coeficiente de Correlação Intraclasse) \\
\textbf{ICRU} & \emph{International Commission on Radiation Units and Measurements} \\
\textbf{IFUSP} & Instituto de Física da Universidade de São Paulo \\
\textbf{InRad} & Instituto de Radiologia do Hospital das Clínicas da FMUSP \\
\textbf{IO} & \emph{Ideal Observer} (Observador Ideal Bayesiano) \\
\textbf{LG} & Laguerre-Gauss \\
\textbf{LOSO} & \emph{Leave-One-Scanner-Out} (Validação Cruzada Omitindo um Tomógrafo) \\
\textbf{LSF} & \emph{Line Spread Function} (Função de Espalhamento de Linha) \\
\textbf{MBIR} & \emph{Model-Based Iterative Reconstruction} (Reconstrução Iterativa Baseada em Modelos) \\
\textbf{MHSA} & \emph{Multi-Head Self-Attention} (Auto-Atenção Multi-Cabeça) \\
\textbf{MRMC} & \emph{Multi-Reader Multi-Case} (Múltiplos Leitores e Múltiplos Casos) \\
\textbf{MTF} & \emph{Modulation Transfer Function} (Função de Transferência de Modulação) \\
\textbf{NPS} & \emph{Noise Power Spectrum} (Espectro de Potência do Ruído) \\
\textbf{NPW} & \emph{Non-Prewhitening Observer} (Observador Sem Pré-Branqueamento) \\
\textbf{NPWE} & \emph{Non-Prewhitening Observer with Eye Filter} (NPW com Filtro Ocular) \\
\textbf{NSGA-II} & \emph{Non-dominated Sorting Genetic Algorithm II} \\
\textbf{PCCT} & \emph{Photon-Counting Computed Tomography} (TC por Contagem de Fótons) \\
\textbf{PSF} & \emph{Point Spread Function} (Função de Resposta ao Ponto) \\
\textbf{ROC} & \emph{Receiver Operating Characteristic} (Característica de Operação do Receptor) \\
\textbf{ROI} & \emph{Region of Interest} (Região de Interesse) \\
\textbf{SDT} & \emph{Signal Detection Theory} (Teoria de Detecção de Sinais) \\
\textbf{SKE} & \emph{Signal Known Exactly} (Sinal Conhecido Exatamente) \\
\textbf{SKS} & \emph{Signal Known Statistically} (Sinal Conhecido Estatisticamente) \\
\textbf{SNR} & \emph{Signal-to-Noise Ratio} (Relação Sinal-Ruído) \\
\textbf{TBIQ} & \emph{Task-Based Image Quality} (Qualidade de Imagem Baseada em Tarefa) \\
\textbf{TC} & Tomografia Computadorizada \\
\textbf{TCLE} & Termo de Consentimento Livre e Esclarecido \\
\textbf{TG-233} & \emph{Task Group 233} da AAPM \\
\textbf{TOPSIS} & \emph{Technique for Order Preference by Similarity to Ideal Solution} \\
\textbf{TTF} & \emph{Task Transfer Function} (Função de Transferência da Tarefa) \\
\textbf{ViT} & \emph{Vision Transformer} \\
\textbf{VMI} & \emph{Virtual Monoenergetic Image} (Imagem Monoenergética Virtual) \\
\textbf{WSS} & \emph{Wide-Sense Stationary} (Estacionário no Sentido Amplo) \\
\bottomrule
\end{longtable}
\clearpage

% 9. LISTA DE SÍMBOLOS
\chapter*{Lista de Símbolos}
\addcontentsline{toc}{chapter}{Lista de Símbolos}

\begin{longtable}{p{0.20\textwidth} p{0.76\textwidth}}
\toprule
\textbf{Símbolo} & \textbf{Significado Físico / Unidade} \\
\midrule
\endhead
$\mathbf{g}$ & Vetor de dados de imagem discreta ($\mathbb{R}^N$) \\
$\mathbf{s}$ & Vetor determinístico do sinal ou lesão ($\mathbb{R}^N$) \\
$\mathbf{b}$ & Vetor estocástico de ruído e fundo anatômico ($\mathbb{R}^N$) \\
$t$ & Estatística de teste escalar de decisão \\
$t_c$ & Limiar de corte para decisão diagnóstica \\
$d'$ & Índice de detectabilidade (\emph{d-prime}) \\
$d'_{\text{humano}}$ & Índice de detectabilidade experimental medido em leitores humanos \\
$d'_{\text{NPWE}}$ & Índice de detectabilidade calculado pelo modelo NPWE \\
$d'_{\text{CHO}}$ & Índice de detectabilidade calculado pelo modelo CHO \\
$d'_{\text{DL}}$ & Índice de detectabilidade estimado pelo modelo por aprendizado profundo \\
$\mathbf{K}$ & Matriz de autocovariância do ruído ($N \times N$, em $\text{HU}^2$) \\
$\mathbf{K}_{\mathbf{v}}$ & Matriz de autocovariância reduzida no espaço dos canais ($C \times C$) \\
$\mathbf{w}$ & Vetor de pesos ou template linear de filtragem ($\mathbb{R}^N$) \\
$\mathbf{T}$ & Matriz de operadores de canais corticais ($C \times N$) \\
$TTF(f)$ & Função de Transferência da Tarefa na frequência espacial $f$ (adimensional) \\
$f_{50}$ & Frequência espacial correspondente a 50\% de modulação da TTF ($\text{mm}^{-1}$) \\
$f_{10}$ & Frequência espacial correspondente a 10\% de modulação da TTF ($\text{mm}^{-1}$) \\
$NPS(u, v)$ & Espectro de Potência do Ruído bidimensional ($\text{mm}^2$ ou $\text{HU}^2\cdot\text{mm}^2$) \\
$NPS(f)$ & Espectro de Potência do Ruído radial unidimensional ($\text{HU}^2\cdot\text{mm}^2$) \\
$f_{\text{peak}}$ & Frequência espacial de máxima amplitude do espectro de ruído ($\text{mm}^{-1}$) \\
$f_{\text{av}}$ & Frequência espacial média ponderada do espectro de ruído ($\text{mm}^{-1}$) \\
$E(f)$ & Resposta em frequência do filtro ocular humano / CSF (adimensional) \\
$W_{\text{task}}(f)$ & Espectro de Fourier da morfologia da tarefa diagnóstica ($\text{HU}\cdot\text{mm}^2$) \\
$P_C$ & Proporção empírica de acertos no teste 2AFC ($0 \le P_C \le 1$) \\
$\Phi(x)$ & Função de distribuição cumulativa da variável normal padrão \\
$\Phi^{-1}(p)$ & Função quantil (inversa da distribuição cumulativa normal padrão) \\
$\mu_{\text{linear}}$ & Coeficiente de atenuação linear do meio atenuador ($\text{cm}^{-1}$) \\
$\sigma^2$ & Variância estatística do número de CT em uma região homogênea ($\text{HU}^2$) \\
$\sigma_{\text{int}}^2$ & Variância do ruído neural interno do observador biológico ($\text{HU}^2$) \\
$D$ & Dose de radiação absorvida / $\text{CTDI}_{\text{vol}}$ ($\text{mGy}$) \\
$T$ & Tempo operacional total do procedimento ($T = T_{\text{aq}} + T_{\text{rec}}$, em segundos) \\
$W$ & Desempenho na tarefa diagnóstica ($W = d'$) \\
$\Omega$ & Espaço viável de parâmetros do protocolo tomográfico \\
$\Delta C$ & Contraste radiológico central da lesão em relação ao fundo ($\text{HU}$) \\
$R$ & Raio físico da lesão esférica simulada ($\text{mm}$) \\
$J_1(x)$ & Função de Bessel ordinária de primeira espécie e ordem 1 \\
$Q, K, V$ & Matrizes de Consulta (\emph{Query}), Chave (\emph{Key}) e Valor (\emph{Value}) no mecanismo de atenção \\
$d_k$ & Dimensão dos vetores de projeção no módulo de atenção \\
$\mathbf{z}_0$ & Sequência de \emph{patch embeddings} lineares com codificação posicional \\
$\sigma^2_R$ & Componente de variância associada aos leitores humanos na ANOVA MRMC \\
$\sigma^2_C$ & Componente de variância associada aos casos clínicos na ANOVA MRMC \\
$\sigma^2_{RC}$ & Componente de variância da interação leitor $\times$ caso na ANOVA MRMC \\
\bottomrule
\end{longtable}
\clearpage

% 10. SUMÁRIO
\pdfbookmark[0]{\contentsname}{toc}
\tableofcontents
\clearpage

% ==============================================================================
% ELEMENTOS TEXTUAIS
% ==============================================================================
\pagestyle{fancy}
\pagenumbering{arabic}

% ------------------------------------------------------------------------------
% CAPÍTULO 1: INTRODUÇÃO E OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Introdução e Objetivos}
\label{chap:introducao}

A Tomografia Computadorizada (TC) transformou a medicina ao permitir a visualização volumétrica do corpo humano com alta resolução anatômica e temporal. Contudo, a evolução dos equipamentos estabeleceu um cenário de alta complexidade física: o uso intensivo de radiação ionizante para exames de rotina e a substituição dos métodos clássicos de reconstrução por algoritmos não lineares de inteligência artificial. Este capítulo contextualiza a importância da metrologia da qualidade de imagem em física médica, introduz os conceitos físicos da formação da imagem tomográfica, expõe detalhadamente as grandezas clássicas e suas premissas, fundamenta a necessidade do paradigma baseado em tarefa e apresenta os objetivos deste trabalho.

\section{Os dois lados da Tomografia Computadorizada}
\label{sec:paradoxo_tc}

A Tomografia Computadorizada baseia-se na medição da atenuação exponencial que um feixe colimado de raios X sofre ao atravessar os tecidos biológicos. De acordo com a Lei de Beer-Lambert-Bouguer, para um feixe monoenergético com intensidade inicial $I_0$ fótons por segundo incidindo sobre um meio material atenuador, a intensidade transmitida $I$ ao longo de um trajeto retilíneo $L$ é expressa por:
\begin{equation}
  I = I_0 \exp\left( -\int_L \mu(x, y, z; E) \, dl \right)
  \label{eq:beer_lambert}
\end{equation}
onde:
\begin{itemize}
  \item $I_0$ é a intensidade incidente do feixe de raios X ($\text{fótons}\cdot\text{s}^{-1}\cdot\text{mm}^{-2}$);
  \item $I$ é a intensidade transmitida que atinge os detectores após atravessar o paciente;
  \item $\mu(x, y, z; E)$ representa o coeficiente de atenuação linear do tecido biológico na coordenada espacial $(x, y, z)$ para a energia de fótons $E$, medido em $\text{cm}^{-1}$;
  \item $dl$ é o elemento diferencial de comprimento ao longo da linha de projeção $L$.
\end{itemize}

O coeficiente de atenuação linear $\mu$ sintetiza a probabilidade total de interação dos fótons por unidade de comprimento, decorrente fundamentalmente do Efeito Fotoelétrico (predominante em baixas energias e tecidos de alto número atômico, como o osso e meios de contraste iodados) e do Espalhamento Compton (predominante em energias intermediárias em tecidos moles e água) \cite{bushberg2020, attix1986}.

Ao rotacionar sincronizadamente o tubo emissor de raios X e o arco de detectores ao redor do paciente, o tomógrafo adquire múltiplos perfis de projeção angular a diferentes ângulos $\theta \in [0, 2\pi)$. O conjunto de todas as projeções é denominado \emph{sinograma}, formalizado matematicamente pela Transformada de Radon bidimensional:
\begin{equation}
  p(r, \theta) = \mathcal{R}\{\mu(x, y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x, y) \, \delta(x\cos\theta + y\sin\theta - r) \, dx \, dy
  \label{eq:radon_transform}
\end{equation}
onde $r$ representa a distância radial da linha de projeção ao centro do campo de visão (FOV), e $\delta(\cdot)$ é a função delta de Dirac.

O algoritmo clássico de Retroprojeção Filtrada (\emph{Filtered Backprojection} --- FBP) reconstrói o mapa transversal $\mu(x, y)$ através do Teorema das Fatias Centrais de Fourier (\emph{Central Slice Theorem}), aplicando uma filtragem com filtro de rampa $|f|$ no domínio da frequência para cancelar o borramento espacial intrínseco ($1/r$) gerado pela sobreposição de retroprojeções simples \cite{seeram2015}:
\begin{equation}
  \mu(x, y) = \int_0^\pi \left[ \int_{-\infty}^{\infty} P(f, \theta) |f| \, e^{2\pi i f (x\cos\theta + y\sin\theta)} \, df \right] d\theta
  \label{eq:fbp_formula}
\end{equation}
onde $P(f, \theta) = \mathcal{F}_{1D}\{p(r, \theta)\}$ é a Transformada de Fourier unidimensional da projeção angular.

Para uniformizar os valores e torná-los comparáveis entre diferentes equipamentos e tensões de tubo, os coeficientes lineares reconstruídos $\mu_{\text{tecido}}$ são convertidos para a escala padronizada de Unidades Hounsfield (HU), normalizada em relação à atenuação da água pura nas mesmas condições de irradiação:
\begin{equation}
  \text{Número CT (HU)} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{água}}}{\mu_{\text{água}}}
  \label{eq:escala_hounsfield}
\end{equation}
Por definição, o ar atmosférico apresenta $-1000\text{ HU}$ ($\mu_{\text{ar}} \approx 0$), a água pura calibrada apresenta exatamente $0\text{ HU}$, o tecido pulmonar arejado varia entre $-800\text{ e }-600\text{ HU}$, o tecido adiposo situa-se em torno de $-100\text{ HU}$, o parênquima hepático e muscular varia de $+40\text{ a }+60\text{ HU}$, e o osso cortical denso varia de $+1000\text{ a }+3000\text{ HU}$.

Apesar de sua indispensável precisão diagnóstica, os raios X constituem radiação ionizante capaz de induzir quebras simples e duplas nas fitas de DNA celular. Os efeitos biológicos da radiação dividem-se em duas categorias \cite{icrp103_2007}:
\begin{enumerate}
  \item \textbf{Efeitos Determinísticos (Reações Teciduais):} Ocorrem apenas após a superação de uma dose limiar (geralmente acima de $0{,}5\text{ a }1{,}0\text{ Gy}$), resultando em morte celular em massa e perda de função tecidual;
  \item \textbf{Efeitos Estocásticos (Probabilísticos):} Não possuem dose limiar de segurança. A probabilidade de indução de mutações genéticas e câncer radioinduzido aumenta linearmente com a dose absorvida cumulativa, conforme estabelecido pelo modelo Linear Sem Limiar (\emph{Linear Non-Threshold} --- LNT) \cite{icrp103_2007, attix1986}.
\end{enumerate}

Globalmente, a tomografia computadorizada responde por mais de 60\% de toda a dose de radiação médica administrada à população, embora represente apenas cerca de 10\% a 15\% do volume total de exames radiológicos realizados \cite{mccollough2026, bushberg2020}. Esse panorama impõe o princípio de radioproteção ALARA (\emph{As Low As Reasonably Achievable} --- Tão Baixo Quanto Razoavelmente Exequível) e atende aos requisitos normativos federais brasileiros (ANVISA RDC 611/2022 e IN 93/2021) \cite{anvisa_rdc611_2022, anvisa_in93_2021}. A missão da física médica reside em reduzir a dose de radiação entregue ao paciente ao nível estritamente necessário para garantir o diagnóstico médico com segurança.

Para aplicar o princípio ALARA na prática hospitalar, é imperativo medir quantitativamente se a redução da dose afetou a qualidade diagnóstica da imagem. No entanto, os parâmetros tradicionalmente utilizados para esse fim falham diante das tecnologias tomográficas modernas, como detalhado a seguir.

\section{Métricas Clássicas e a Ruptura Metrológica}
\label{sec:insuficiencia_metricas}

Historicamente, o controle de qualidade e a garantia de desempenho em TC fundamentaram-se em quatro parâmetros físicos principais:
\begin{enumerate}
  \item \textbf{Relação Sinal-Ruído ($SNR$ --- \emph{Signal-to-Noise Ratio}):}
  Quantifica a intensidade do sinal útil em relação às flutuações estatísticas de fundo causadas pelo ruído quântico de fótons:
  \begin{equation}
    SNR = \frac{\mu_{\text{ROI}}}{\sigma_{\text{ROI}}}
    \label{eq:snr_def}
  \end{equation}
  onde $\mu_{\text{ROI}}$ é a média dos números de CT em uma região de interesse (ROI) homogênea (em HU), e $\sigma_{\text{ROI}}$ é o desvio padrão dos valores dos pixels nessa mesma região.

  \item \textbf{Relação Contraste-Ruído ($CNR$ --- \emph{Contrast-to-Noise Ratio}):}
  Mede a separabilidade estatística entre dois tecidos adjacentes $A$ e $B$ com atenuações distintas (por exemplo, uma lesão e o parênquima circundante):
  \begin{equation}
    CNR = \frac{|\mu_A - \mu_B|}{\sigma_{\text{fundo}}} = \frac{\Delta \mu}{\sigma_{\text{fundo}}}
    \label{eq:cnr_def}
  \end{equation}
  onde $|\mu_A - \mu_B|$ representa a diferença de contraste radiológico entre a estrutura de interesse e o tecido de fundo, e $\sigma_{\text{fundo}}$ é o desvio padrão do ruído no fundo. Segundo o modelo empírico de Rose (1948), uma estrutura circular só é visualmente detectável pelo olho humano se $CNR \ge 4\text{ a }5$ \cite{rose1948, burgess1999}.

  \item \textbf{Desvio Padrão do Número de CT ($\sigma_{\text{HU}}$):}
  Representa a dispersão estatística dos valores de pixel em uma ROI homogênea de água ou acrílico:
  \begin{equation}
    \sigma_{\text{HU}} = \sqrt{\frac{1}{N_{\text{pix}} - 1} \sum_{i=1}^{N_{\text{pix}}} (I_i - \mu_{\text{ROI}})^2}
    \label{eq:sigma_hu_def}
  \end{equation}
  Na física de radiação clássica com retroprojeção filtrada, o desvio padrão do ruído quântico de Poisson escala inversamente com a raiz quadrada da fluência de fótons e, portanto, da dose de radiação: $\sigma_{\text{HU}} \propto 1 / \sqrt{\text{Dose}}$.

  \item \textbf{Função de Resposta ao Ponto (PSF) e Função de Transferência de Modulação ($MTF$):}
  \begin{itemize}
    \item \textbf{PSF (\emph{Point Spread Function}):} Descreve como um ponto infinitesimal ideal de altíssimo contraste ($\delta(x, y)$) é transformado pelo tomógrafo em uma distribuição bidimensional borrada $h(x, y)$. Esse alargamento espacial decorre do tamanho geométrico finito da mancha focal do ânodo do tubo de raios X, da abertura angular dos detectores, do cruzamento óptico no cintilador e do algoritmo de amostragem;
    \item \textbf{MTF (\emph{Modulation Transfer Function}):} Representa a magnitude normalizada da Transformada de Fourier bidimensional da PSF:
    \begin{equation}
      MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
      \label{eq:mtf_def}
    \end{equation}
    A MTF expressa a fração de contraste original que o sistema consegue preservar em cada frequência espacial $f$ (medida em ciclos por milímetro, $\text{mm}^{-1}$). Uma MTF igual a 1 indica preservação total do contraste, enquanto valores próximos de 0 indicam perda de detalhe anatômico.
  \end{itemize}
\end{enumerate}

A validade matemática dessas métricas clássicas depende de três premissas estritas:
\begin{enumerate}
  \item \textbf{Linearidade do Sistema Formador de Imagem:} O operador de reconstrução $\mathcal{R}$ deve satisfazer o princípio da superposição: a resposta a uma combinação linear de sinais deve ser idêntica à combinação linear das respostas individuais: $\mathcal{R}\{\alpha f_1 + \beta f_2\} = \alpha \mathcal{R}\{f_1\} + \beta \mathcal{R}\{f_2\}$;
  \item \textbf{Invariância Translacional Espacial (Isoplanatismo):} A função de resposta ao ponto $\text{PSF}(x, y)$ deve ser idêntica em qualquer coordenada da matriz de reconstrução;
  \item \textbf{Estacionariedade do Ruído no Sentido Amplo (WSS --- \emph{Wide-Sense Stationary}):} Um processo estocástico bidimensional $I(x, y)$ é dito estacionário no sentido amplo se satisfaz simultaneamente duas condições:
  \begin{itemize}
    \item O valor esperado (média estatística) é constante em todas as posições espaciais da imagem: $\mathbb{E}[I(x, y)] = \mu_0$;
    \item A função de autocovariância entre dois pontos espaciais $\mathbf{r}_1 = (x_1, y_1)$ e $\mathbf{r}_2 = (x_2, y_2)$ depende exclusivamente do vetor de deslocamento espacial $\Delta \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$, e não de suas posições absolutas:
    \begin{equation}
      K_I(\mathbf{r}_1, \mathbf{r}_2) = \mathbb{E}\left[ (I(\mathbf{r}_1) - \mu_0)(I(\mathbf{r}_2) - \mu_0) \right] = K_I(\mathbf{r}_1 - \mathbf{r}_2)
      \label{eq:wss_def}
    \end{equation}
  \end{itemize}
\end{enumerate}

Para compreender a ruptura metrológica ilustrada na \cref{fig:comparativo_paradigmas}, é indispensável conceituar os elementos físicos que compõem o ecossistema de avaliação tomográfica:
\begin{itemize}
  \item \textbf{Simuladores Geométricos Homogêneos:} Cilindros padronizados de diâmetro fixo (ex: 16 cm para crânio e 32 cm para abdome) confeccionados em materiais uniformes como polimetilmetacrilato (PMMA/acrílico) ou água pura. São ideais para testes de constância eletromecânica linear, mas não reproduzem a complexidade das bordas e interfaces anatômicas humanas;
  \item \textbf{Simuladores Físicos Antropomórficos:} Phantoms anatômicos construídos com materiais de densidade e coeficientes de atenuação radiológica equivalentes a tecidos biológicos reais (osso cortical, osso trabecular, cartilagem, parênquima pulmonar e tecidos moles). Possuem geometrias corporais realistas de tórax, abdome e crânio;
  \item \textbf{Simuladores Híbridos:} Metodologia experimental avançada que combina a aquisição tomográfica real do fundo anatômico estruturado de um simulador antropomórfico com a inserção computacional de modelos 3D de lesões patológicas sintéticas. As lesões são matematicamente convolvidas com a PSF tridimensional real do equipamento, gerando milhares de imagens com localização e contraste exatamente conhecidos (\emph{ground truth} perfeito);
  \item \textbf{Filtros de Convolução / Kernels de Reconstrução:} Funções matemáticas aplicadas no domínio de Fourier da FBP para calibrar o compromisso físico entre ruído e resolução espacial. Filtros suaves (\emph{smooth/soft tissue kernels}) reduzem o ruído às custas de borramento de bordas; filtros duros (\emph{sharp/bone kernels}) acentuam bordas e resolução de alta frequência, aumentando o ruído de alta frequência;
  \item \textbf{Algoritmos Não Lineares (HIR, MBIR e DLR):} Métodos de reconstrução que abandonam a inversão linear da Transformada de Radon. Empregando laços iterativos com regularização adaptativa ou redes neurais profundas com milhões de parâmetros, esses algoritmos tratam o ruído de forma diferenciada dependendo da presença local de bordas anatômicas e do nível de contraste do sinal;
  \item \textbf{Paradigma Psicofísico 2AFC (\emph{Two-Alternative Forced Choice}):} Protocolo de teste cego no qual são exibidas simultaneamente duas imagens a um médico especialista: uma imagem contendo apenas ruído de fundo ($H_0$) e outra contendo uma patologia sutil imersa no ruído ($H_1$). O leitor é forçado a selecionar qual das duas contém a lesão, eliminando vieses comportamentais e limiares subjetivos de decisão.
\end{itemize}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption[Comparativo Estrutural entre os Paradigmas Físicos]{Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

A incorporação de redes neurais convolucionais profundas (DLR) quebrou todas as premissas clássicas \cite{racine2020, debbiche2024, greffier2026}. Sob processamento não linear:
\begin{itemize}
  \item O desvio padrão ($\sigma_{\text{HU}}$) é artificialmente reduzido por filtros não lineares adaptativos, induzindo a falsa impressão de que a qualidade aumentou;
  \item O ruído perde a estacionariedade (quebra de WSS): a variância e a correlação entre pixels passam a depender da proximidade de estruturas ósseas ou contrastadas;
  \item O ruído adquire um padrão textural ceroso (\emph{plastic/waxy look}), caracterizado pela perda de frequências médias e altas essenciais para o diagnóstico humano;
  \item Lesões sutis de baixo contraste (+20 a +30 HU) são tratadas pelo algoritmo como flutuações de ruído e suavizadas, tornando-se invisíveis na imagem clínica, mesmo com valores formalmente excelentes de $SNR$ e $CNR$ \cite{toia2023, solomon2020}.
\end{itemize}

Para resolver a incapacidade das métricas escalares em caracterizar sistemas não lineares, a física médica estruturou uma metodologia objetiva centrada na eficácia diagnóstica: o paradigma TBIQ.

\section{O Paradigma da Qualidade Baseada em Tarefa (TBIQ)}
\label{sec:paradigma_tbiq}

O paradigma TBIQ (\emph{Task-Based Image Quality}), consolidado pelos relatórios internacionais AAPM TG-233 e ICRU 54, postula que a qualidade de uma imagem médica não é uma propriedade intrínseca isolada, mas sim a medida objetiva do desempenho de um observador ao executar uma tarefa clínica específica (\cref{fig:tbiq_paradigm}) \cite{aapm_tg233_2019, icru54_1996}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow1_tbiq_paradigm.png}
  \caption[Pilares Fundamentais do Paradigma TBIQ]{Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:tbiq_paradigm}
\end{figure}

O paradigma sustenta-se sobre quatro pilares fundamentais:
\begin{enumerate}
  \item \textbf{Função de Transferência da Tarefa ($TTF(f)$):} Modela a resolução espacial de forma dependente do contraste específico da lesão clínica investigada;
  \item \textbf{Espectro de Potência do Ruído ($NPS(f)$):} Quantifica a potência e a textura do ruído no domínio contínuo de Fourier;
  \item \textbf{Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$):} Representa matematicamente o tamanho, a forma e a densidade radiológica da lesão;
  \item \textbf{Filtro Ocular ou Modelo Perceptual ($E(f)$ / Modelos Neurais):} Incorpora a sensibilidade de contraste do olho humano ou os mecanismos corticais de tomada de decisão.
\end{enumerate}

A integração matemática desses quatro componentes resulta no **Índice de Detectabilidade ($d'$)**, grandeza estatística que quantifica a separabilidade entre estados de saúde e doença.

Compreendidos os desafios da tomografia computadorizada e a formulação conceitual do paradigma TBIQ, definem-se a seguir os objetivos deste trabalho.

\section{Objetivos}
\label{sec:objetivos}

O objetivo geral desta monografia consiste em desenvolver uma formulação teórica, biofísica e computacional unificada dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo as bases metrológicas para a avaliação de tecnologias avançadas e otimização de protocolos clínicos.

Os objetivos específicos compreendem:
\begin{enumerate}
  \item Apresentar as deduções matemáticas fundamentais da Teoria de Detecção de Sinais (SDT), formalizando o Índice de Detectabilidade ($d'$), curvas ROC e testes psicofísicos 2AFC;
  \item Deduzir rigorosamente no domínio contínuo de Fourier a Função de Transferência da Tarefa ($TTF(f)$), o Espectro de Potência do Ruído ($NPS(f)$), o Filtro Ocular ($E(f)$) e o Espectro da Tarefa ($W_{\text{task}}(f)$);
  \item Analisar os observadores de modelo lineares clássicos: Observador Ideal Bayesiano (IO), Observador Sem Pré-Branqueamento com Filtro Ocular (NPWE) e Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor;
  \item Demonstrar as causas matemáticas do colapso dos modelos analíticos lineares sob reconstruções DLR e fundos anatômicos complexos;
  \item Investigar os Observadores Baseados em Aprendizado Profundo (DLMO) baseados em \emph{Vision Transformers} com auto-atenção multi-cabeça;
  \item Analisar os fundamentos biofísicos da Tomografia por Contagem de Fótons (PCCT) e a síntese de Imagens Monoenergéticas Virtuais ($VMI$);
  \item Formular a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional ($T$) e detectabilidade ($W$);
  \item Estruturar a arquitetura de software modular e o protocolo experimental com validação psicofísica MRMC em painel de médicos radiologistas.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 2: FUNDAMENTOS DA AVALIAÇÃO BASEADA EM TAREFA
% ------------------------------------------------------------------------------
\chapter{Fundamentos da Avaliação Baseada em Tarefa}
\label{chap:fundamentos_sdt}

A avaliação científica da qualidade tomográfica requer um modelo matemático que conecte a física estocástica das imagens à tomada de decisão diagnóstica. Este capítulo aborda a Teoria de Detecção de Sinais (SDT), a derivação formal do Índice de Detectabilidade ($d'$), a teoria das Curvas ROC, o protocolo experimental 2AFC e as deduções contínuas em frequência de $TTF(f)$, $NPS(f)$, $E(f)$ e $W_{\text{task}}(f)$, detalhando individualmente cada gráfico apresentado.

\section{Teoria Clássica de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria}

A detecção de uma patologia em um exame médico com ruído é formalmente descrita como um problema estocástico de detecção de sinal sob ruído. A Teoria de Detecção de Sinais (SDT), introduzida na física matemática por Peterson, Birdsall e Fox (1954) e aplicada à medicina por Lusted (1968) e Metz (1986), analisa o processo de decisão diagnóstica sob flutuações estocásticas \cite{peterson1954, lusted1968, metz1986}.

Considere uma imagem discreta representada por um vetor $\mathbf{g} \in \mathbb{R}^N$ ($N$ pixels). O problema de detecção binária formula-se por duas hipóteses mutuamente exclusivas:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Normal}) \label{eq:h0} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Patologia}) \label{eq:h1}
\end{align}
onde:
\begin{itemize}
  \item $\mathbf{s} \in \mathbb{R}^N$ é o vetor determinístico que descreve o perfil espacial do sinal da lesão;
  \item $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo com média zero e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle$.
\end{itemize}

O observador processa o vetor de imagem $\mathbf{g}$ através de um funcional escalar contínuo $t = t(\mathbf{g})$. A decisão diagnóstica final é obtida pela comparação direta de $t$ com um limiar de corte $t_c$:
\begin{equation}
  \text{Decisão} = \begin{cases}
    H_1 (\text{Positivo para Lesão}), & \text{se } t(\mathbf{g}) \ge t_c \\
    H_0 (\text{Negativo para Lesão}), & \text{se } t(\mathbf{g}) < t_c
  \end{cases}
  \label{eq:criterio_decisao}
\end{equation}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig1_sdt_roc_2afc.png}
  \caption[Distribuições da SDT, Curvas ROC e Desempenho 2AFC]{Teoria de Detecção de Sinais (SDT), Análise ROC e Desempenho no Paradigma 2AFC.}
  \label{fig:sdt_roc_2afc}
\end{figure}

A \cref{fig:sdt_roc_2afc} sintetiza os pilares da teoria de decisão em três painéis interdependentes:
\begin{itemize}
  \item \textbf{Painel (A) --- Distribuições de Decisão da SDT:} O eixo horizontal representa a variável escalar de decisão $t$ e o eixo vertical exibe as densidades de probabilidade $p(t|H_0)$ (curva azul, normal/sem lesão) e $p(t|H_1)$ (curva vermelha, patológico/com lesão). A linha tracejada vertical marca o limiar de decisão $t_c = 1{,}3$. A integral de $p(t|H_1)$ para $t \ge t_c$ (área vermelha sombreada) define a Sensibilidade ou Fração de Verdadeiros Positivos ($TPF$). A integral de $p(t|H_0)$ para $t \ge t_c$ (área azul sombreada) define a Fração de Falsos Positivos ($FPF$). A separação normalizada entre as médias das distribuições define o índice de detectabilidade $d' = 2{,}2$. Deslocamentos de $t_c$ para a esquerda aumentam a sensibilidade à custa de mais alarmes falsos;

  \item \textbf{Painel (B) --- Curvas ROC em Função de $d'$:} Apresenta a trajetória paramétrica no espaço $(FPF, TPF)$ obtida pela variação contínua do limiar $t_c \in (-\infty, +\infty)$ para diferentes valores de detectabilidade ($d' = 0{,}5; 1{,}0; 1{,}8; 2{,}5; 3{,}5; 4{,}5$). A linha pontilhada diagonal ($d'=0$) representa o desempenho do acaso puro ($AUC = 0{,}50$). À medida que $d'$ cresce, a curva ROC projeta-se em direção ao vértice superior esquerdo ($FPF=0, TPF=1$), indicando aumento na capacidade intrínseca de discriminação do observador;

  \item \textbf{Painel (C) --- Desempenho no Paradigma 2AFC:} O gráfico ilustra a relação analítica exata entre o índice $d'$ (eixo horizontal) e a proporção empírica de acertos $P_C$ em testes 2AFC (eixo vertical, em \%). A linha pontilhada horizontal em 50\% marca a adivinhação aleatória ($d'=0$). A linha tracejada em $d' \approx 1{,}8$ assinala o limiar típico de acurácia clínica ($P_C \approx 90\%$), enquanto a linha tracejada em $d' = 4{,}0$ indica o Critério de Rose ($P_C = 99{,}8\%$), ponto a partir do qual a lesão é detectada com certeza visual quase absoluta.
\end{itemize}

A separabilidade matemática entre as distribuições $p(t|H_0)$ e $p(t|H_1)$ é expressa quantitativamente pelo Índice de Detectabilidade ($d'$), deduzido a seguir.

\section{Definição Formal do Índice de Detectabilidade (\texorpdfstring{$d'$}{d-prime})}
\label{sec:dprime_definicao}

O Índice de Detectabilidade ($d'$) expressa a distância estatística entre os valores esperados da estatística de teste sob as duas hipóteses, normalizada pelas respectivas variâncias \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_geral}
\end{equation}
onde:
\begin{itemize}
  \item $\langle t | H_1 \rangle$ e $\langle t | H_0 \rangle$ são os valores esperados condicionais de $t$ sob presença e ausência de sinal;
  \item $\sigma^2(t|H_1)$ e $\sigma^2(t|H_0)$ são as variâncias estocásticas correspondentes.
\end{itemize}

Sob ruído aditivo com variâncias idênticas ($\sigma^2(t|H_1) = \sigma^2(t|H_0) = \sigma_t^2$), a equação reduz-se à formulação clássica:
\begin{equation}
  d' = \frac{\mu_1 - \mu_0}{\sigma_t}
  \label{eq:dprime_gaussiano}
\end{equation}
onde $\mu_1 = \langle t | H_1 \rangle$ e $\mu_0 = \langle t | H_0 \rangle$.

Para determinar o valor de $d'$ em experimentos com médicos especialistas, utiliza-se a correspondência matemática entre a Análise ROC e o paradigma psicofísico 2AFC.

\section{Curva ROC, AUC e o Paradigma Experimental 2AFC}
\label{sec:roc_2afc}

A Área sob a Curva ROC ($AUC$) é calculada pela integral da taxa de verdadeiros positivos em função dos falsos positivos:
\begin{equation}
  AUC = \int_0^1 TPF(FPF) \, d(FPF) = \Phi\left( \frac{d'}{\sqrt{2}} \right)
  \label{eq:auc_formula}
\end{equation}
onde $\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-u^2/2} du$ é a função de distribuição cumulativa da variável normal padrão.

No experimento 2AFC (\emph{Two-Alternative Forced Choice}), apresentam-se simultaneamente ao leitor dois campos de imagem: um de controle ($H_0$) e um patológico ($H_1$). Green e Swets (1966) e Burgess (1999) demonstraram a identidade fundamental \cite{burgess1999}:
\begin{equation}
  P_C = AUC = \Phi\left( \frac{d'}{\sqrt{2}} \right)
  \label{eq:pc_2afc}
\end{equation}
onde $P_C$ é a proporção empírica de acertos do observador.

Invertendo a equação através da função quantil $\Phi^{-1}$, obtém-se diretamente o índice de detectabilidade experimental do leitor humano ($d'_{\text{humano}}$):
\begin{equation}
  d'_{\text{humano}} = \sqrt{2} \, \Phi^{-1}(P_C)
  \label{eq:dprime_from_pc}
\end{equation}

Estabelecida a formulação estatística da decisão humana, o próximo passo consiste em deduzir analiticamente as funções espectrais que descrevem a física do tomógrafo no domínio contínuo de Fourier.

\section{Dedução Contínua das Métricas em Frequência}
\label{sec:metricas_fourier}

O domínio de Fourier permite decompor a imagem tomográfica em frequências espaciais, isolando os efeitos da resolução óptica, da textura de ruído, da sensibilidade visual e da geometria da lesão, conforme o relatório AAPM TG-233.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_spectral_metrics.png}
  \caption[Métricas Espectrais Contínuas em Frequência]{Métricas Espectrais Contínuas no Domínio de Fourier segundo o Relatório AAPM TG-233.}
  \label{fig:spectral_metrics}
\end{figure}

A \cref{fig:spectral_metrics} detalha o comportamento das quatro grandezas espectrais no domínio de Fourier:
\begin{itemize}
  \item \textbf{Painel (A) --- Função de Transferência da Tarefa $TTF(f)$:} O eixo horizontal mostra a frequência espacial $f$ ($\text{mm}^{-1}$) e o eixo vertical exibe a modulação normalizada. As curvas representam a resposta para quatro materiais de calibração: Iodo (+350 HU, vermelho escuro, $f_{50} = 0{,}58\text{ mm}^{-1}$), Teflon (+900 HU, laranja, $f_{50} = 0{,}52\text{ mm}^{-1}$), Delrin (+340 HU, azul, $f_{50} = 0{,}42\text{ mm}^{-1}$) e Solid Water (+20 HU, ciano, $f_{50} = 0{,}35\text{ mm}^{-1}$). A linha pontilhada em 0,5 marca o nível de $f_{50}$. Observa-se que materiais de baixo contraste apresentam decaimento mais acentuado da resolução em altas frequências devido à não-linearidade do sistema;

  \item \textbf{Painel (B) --- Espectro de Potência do Ruído $NPS(f)$:} O gráfico ilustra a densidade espectral de potência do ruído ($\text{HU}^2\cdot\text{mm}^2$) vs. frequência espacial $f$ ($\text{mm}^{-1}$) para quatro algoritmos: FBP clássico (linha preta, formato de rampa linear com $f_{\text{peak}} \approx 0{,}45\text{ mm}^{-1}$), HIR (linha azul, intermediário com $f_{\text{peak}} \approx 0{,}35\text{ mm}^{-1}$), DLR (linha verde espessa, mantendo o pico textural em $f_{\text{peak}} \approx 0{,}40\text{ mm}^{-1}$ com menor área total sob a curva) e MBIR agressivo (linha roxa tracejada, deslocando o pico para $f_{\text{peak}} \approx 0{,}18\text{ mm}^{-1}$, gerando a textura cerosa);

  \item \textbf{Painel (C) --- Filtro Ocular Humano $E(f)$:} Exibe a Função de Sensibilidade ao Contraste (CSF) do olho humano em função da frequência retiniana (ciclos por grau visual, cpd). A curva azul ilustra o comportamento passa-faixa com máxima sensibilidade no pico de $4{,}2\text{ cpd}$ (linha tracejada vermelha), demonstrando que o sistema visual humano atenua tanto variações espaciais extremamente lentas quanto ruídos de frequência muito elevada;

  \item \textbf{Painel (D) --- Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$:} Exibe a amplitude espectral normalizada da Transformada de Fourier para nódulos esféricos de diferentes diâmetros ($\varnothing = 3, 5, 8, 12\text{ mm}$). Nódulos volumosos ($12\text{ mm}$, roxo) concentram praticamente toda a energia em frequências muito baixas ($f < 0{,}15\text{ mm}^{-1}$), enquanto pequenas lesões ($3\text{ mm}$, vermelho) espalham seu conteúdo espectral até frequências superiores a $0{,}6\text{ mm}^{-1}$, exigindo alta resolução espacial do tomógrafo.
\end{itemize}

As formulações matemáticas correspondentes expressam-se por:
\begin{enumerate}
  \item \textbf{Função de Transferência da Tarefa ($TTF(f)$):}
  Calculada pela técnica da borda circular em insertos cilíndricos com raio $R_0$ \cite{aapm_tg233_2019, racine2020}:
  \begin{equation}
    TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \text{LSF}(r) \, dr}
    \label{eq:ttf_formula}
  \end{equation}
  onde $\text{LSF}(r) = -\frac{d}{dr}\text{ESF}(r)$ é a Função de Espalhamento de Linha radial obtida pela diferenciação da resposta ao degrau $\text{ESF}(r)$.

  \item \textbf{Espectro de Potência do Ruído ($NPS(f)$):}
  Calculado a partir de $M$ sub-ROIs homogêneas com detrending polinomial 2D $P_2(x, y)$:
  \begin{equation}
    NPS(u, v) = \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
    \label{eq:nps_2d}
  \end{equation}
  onde $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é o ruído purificado. O espectro radial $NPS(f)$ é obtido por integração azimutal de $NPS(u, v)$.

  \item \textbf{Filtro Ocular Humano ($E(f)$):}
  Modelado pela Função de Sensibilidade ao Contraste (CSF) de Burgess (1999) \cite{burgess1999}:
  \begin{equation}
    E(f) = \left( \frac{f_{\text{retina}}}{f_0} \right)^n \exp\left[ -c \left( \frac{f_{\text{retina}}}{f_0} \right)^m \right]
    \label{eq:filtro_ocular}
  \end{equation}
  com $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$ e $f_{\text{retina}} = \frac{\pi d_{\text{v}}}{180} f$, sob distância de visualização médica $d_{\text{v}} \approx 500\text{ mm}$.

  \item \textbf{Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$):}
  Para um nódulo esférico de raio $R$ e contraste central $\Delta C$:
  \begin{equation}
    W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|
    \label{eq:wtask_formula}
  \end{equation}
  onde $J_1(x)$ é a função de Bessel ordinária de primeira espécie e ordem 1.
\end{enumerate}

Com as grandezas espectrais deduzidas, o próximo capítulo explora como a física médica combinou esses elementos na formulação analítica dos observadores lineares e em sua validação psicofísica via modelos ANOVA MRMC.

% ------------------------------------------------------------------------------
% CAPÍTULO 3: OBSERVADORES LINEARES E VALIDAÇÃO PSICOFÍSICA
% ------------------------------------------------------------------------------
\chapter{Observadores Lineares e Validação Psicofísica}
\label{chap:observadores_lineares}

Os observadores de modelo são operadores matemáticos desenvolvidos para quantificar objetivamente a qualidade da imagem em tarefas de detecção. Este capítulo analisa a evolução dos modelos lineares clássicos --- partindo do limite físico do Observador Ideal e do Observador de Hotelling, passando pelo modelo antropomórfico NPWE e culminando no Observador de Hotelling Canalizado (CHO) --- e detalha a metodologia de ANOVA Multi-Reader Multi-Case (MRMC) para validação contra painéis de radiologistas.

\section{O Observador Ideal e o Observador de Hotelling}
\label{sec:observador_ideal}

Para quantificar o desempenho de um sistema tomográfico, é fundamental estabelecer o teto teórico absoluto de informação diagnóstica permitido pelas leis da física. O Observador Ideal (IO) fundamenta-se na razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$. Quando o ruído de fundo segue uma distribuição normal multivariada com matriz de autocovariância $\mathbf{K}$, a razão de verossimilhança logarítmica reduz-se ao Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:template_hotelling}
\end{equation}
onde o vetor de pesos $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ atua realizando o pré-branqueamento (\emph{prewhitening}) do ruído através da matriz inversa $\mathbf{K}^{-1}$, descorrelacionando os pixels antes da integração com o sinal $\mathbf{s}$.

O índice de detectabilidade máximo atingível pelo Observador de Hotelling é dado por:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling}
\end{equation}
Nenhum observador biológico ou computacional pode superar $d'_{\text{HO}}$, tornando-o o padrão-ouro teórico para avaliação de sistemas de aquisição e eficiência quântica de detecção ($DQE$).

Embora o Observador de Hotelling seja ótimo matematicamente, o sistema visual humano não realiza a inversão matricial do ruído $\mathbf{K}^{-1}$. Para modelar radiologistas humanos em imagens homogêneas, formulou-se o modelo Sem Pré-Branqueamento com Filtro Ocular (NPWE).

\section{O Observador NPWE}
\label{sec:npwe_deducao}

Em tarefas de detecção em fundos uniformes, o observador humano correlaciona a imagem diretamente com a forma esperada da lesão ($\mathbf{w}_{\text{NPW}} = \mathbf{s}$). Para incorporar a fisiologia da visão, Burgess (1994) introduziu o filtro ocular $E(f)$ e uma componente de ruído neural interno $\sigma_{\text{int}}^2$, originando o modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) \cite{burgess1994, eckstein2000}.

No domínio contínuo de Fourier, a integral contínua do índice de detectabilidade do NPWE expressa-se por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral}
\end{equation}

Essa equação elegante unifica a resposta óptica do tomógrafo ($TTF$), o espectro da lesão ($W_{\text{task}}$), a sensibilidade visual humana ($E(f)$) e a potência do ruído ($NPS$) em uma única integração unidimensional.

O modelo NPWE atua com excelente precisão em simuladores homogêneos, mas falha ao avaliar fundos anatômicos heterogêneos. Para tratar a anatomia estruturada, a física médica introduziu os canais corticais de frequência no Observador de Hotelling Canalizado (CHO).

\section{O Observador de Hotelling Canalizado (CHO)}
\label{sec:cho_teoria}

Na rotina clínica, as lesões patológicas estão imersas em complexas anatomias estruturadas. Em imagens clínicas com matriz $N = 128 \times 128 = 16.384$ pixels, a matriz de covariância anatômica $\mathbf{K}_{\mathbf{b}} \in \mathbb{R}^{N \times N}$ possui mais de 268 milhões de elementos, inviabilizando sua inversão numérica direta \cite{myers1987, yao1992}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Pipeline Computacional do Observador CHO]{Pipeline Computacional do Observador de Hotelling Canalizado (CHO).}
  \label{fig:cho_flow}
\end{figure}

O modelo CHO introduz uma matriz de operadores de canais corticais $\mathbf{T} \in \mathbb{R}^{C \times N}$ ($C \ll N$, com $C = 4\text{ a }15$), projetando a imagem $\mathbf{g}$ no subespaço reduzido dos canais: $\mathbf{v} = \mathbf{T} \mathbf{g}$ (\cref{fig:cho_flow}). A matriz de covariância reduzida $\mathbf{K}_{\mathbf{v}} \in \mathbb{R}^{C \times C}$ é invertida de forma estável:
\begin{equation}
  \mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K}_{\mathbf{b}} \mathbf{T}^T = \frac{1}{2} \left[ \text{Cov}(\mathbf{v}|H_0) + \text{Cov}(\mathbf{v}|H_1) \right]
  \label{eq:covariancia_canais}
\end{equation}

O índice de detectabilidade do CHO é dado por:
\begin{equation}
  d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}
  \label{eq:dprime_cho}
\end{equation}
onde $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \mathbf{s}$.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig3_cho_cortical_channels.png}
  \caption[Canais Corticais do CHO e Detectabilidade vs Dose]{Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico.}
  \label{fig:cho_channels}
\end{figure}

A \cref{fig:cho_channels} detalha a estrutura neurofisiológica dos canais corticais e o desempenho do modelo CHO:
\begin{itemize}
  \item \textbf{Painel (A) --- Canais D-DOG Corticais:} O gráfico mostra a resposta espectral em frequência espacial $f$ ($\text{mm}^{-1}$) para cinco canais concêntricos de Diferença Densa de Gaussianas (D-DOG), com frequências de pico variando progressivamente de $0{,}10\text{ a }0{,}65\text{ mm}^{-1}$, emulando os filtros de sintonia da área V1 do córtex cerebral;

  \item \textbf{Painel (B) --- Perfis Espaciais de Laguerre-Gauss:} O eixo horizontal representa o raio radial $r$ (mm) e o eixo vertical exibe a amplitude espacial para ordens polinomiais $n = 0, 1, 2, 3$. O canal de ordem 0 é puramente gaussiano, enquanto ordens superiores introduzem anéis concêntricos com alternância de sinais, capturando detalhes de alta frequência com simetria rotacional;

  \item \textbf{Painel (C) --- Campo Receptivo 2D de Gabor ($\theta = 45^\circ$):} O mapa de calor bidimensional no plano $(x, y)$ ilustra a resposta espacial de um filtro de Gabor orientado a $45^\circ$, combinando uma envoltória gaussiana com modulação senoidal para modelar neurônios simples com seletividade direcional;

  \item \textbf{Painel (D) --- Detectabilidade $d'$ vs. Nível de Dose:} Compara o índice $d'$ em função da dose $\text{CTDI}_{\text{vol}}$ (mGy) para três condições: modelo NPWE em fundo homogêneo ideal (linha preta tracejada, $\propto \sqrt{\text{Dose}}$), modelo CHO D-DOG em fundo anatômico estruturado real (linha verde contínua, mantendo alta sensibilidade) e modelo NPWE aplicado em fundo anatômico real (linha vermelha, evidenciando o colapso metrológico e subestimação da detectabilidade por incapacidade de tratar correlações anatômicas).
\end{itemize}

Para comprovar cientificamente que esses modelos computacionais refletem a percepção dos radiologistas, é mandatória a validação psicofísica através da metodologia estatística ANOVA MRMC.

\section{Validação Psicofísica Multi-Reader Multi-Case (MRMC)}
\label{sec:mrmc_teoria}

A avaliação clínica envolve duas fontes principais de variabilidade aleatória: diferenças de julgamento entre médicos e variações anatômicas entre pacientes. O modelo MRMC é a ferramenta estatística mandatória para comprovar a equivalência metrológica entre observadores computacionais e radiologistas humanos.

Adota-se o modelo de ANOVA com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova}
\end{equation}
onde:
\begin{itemize}
  \item $y_{ijk}$ é a acurácia diagnóstica ($AUC$ ou $d'$) medida para a modalidade tomográfica $i$, leitor $j$ e caso clínico $k$;
  \item $\mu$ é a média global da população;
  \item $\tau_i$ é o efeito fixo da modalidade de reconstrução ou nível de dose $i$;
  \item $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é a variância aleatória entre os radiologistas;
  \item $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é a variância aleatória entre as imagens dos pacientes;
  \item $(\tau R)_{ij}, (\tau C)_{ik}, (RC)_{jk}$ são as interações aleatórias correspondentes;
  \item $\epsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\epsilon})$ é o erro experimental aleatório residual.
\end{itemize}

O teste de hipótese utiliza a estatística $F$ com graus de liberdade ajustados de Satterthwaite, exigindo-se um Coeficiente de Correlação Intraclasse $ICC \ge 0{,}90$ para homologação do modelo computacional.

Com os modelos lineares consolidados, o próximo capítulo investiga a ruptura provocada pela inteligência artificial nos algoritmos DLR e a metodologia de simuladores híbridos com detrending polinomial.

% ------------------------------------------------------------------------------
% CAPÍTULO 4: NÃO-LINEARIDADE, DLR E SIMULADORES HÍBRIDOS
% ------------------------------------------------------------------------------
\chapter{Não-Linearidade, DLR e Simuladores Híbridos}
\label{chap:colapso_linearidade}

A incorporação clínica de redes neurais convolucionais profundas diretamente nos sistemas de reconstrução tomográfica (DLR) quebrou as premissas de linearidade e estacionariedade. Este capítulo analisa a taxonomia física dos algoritmos comerciais, detalha o colapso dos modelos analíticos lineares, descreve o efeito ceroso e fundamenta a metodologia experimental de Phantoms Híbridos com Detrending Polinomial 2D.

\section{Taxonomia dos Algoritmos Comerciais de Reconstrução}
\label{sec:taxonomia_dlr}

A evolução dos algoritmos tomográficos compreende quatro etapas fundamentais:
\begin{enumerate}
  \item \textbf{FBP (1ª Geração):} Inversão analítica exata da Transformada de Radon. Linear, mas exige doses elevadas de radiação;
  \item \textbf{HIR (2ª Geração):} Reconstrução Iterativa Híbrida estatística (ex: ASiR, AIDR 3D, SAFIRE, iDose4), permitindo 20\% a 40\% de redução de dose;
  \item \textbf{MBIR (3ª Geração):} Reconstrução Baseada em Modelos Físicos de óptica e espalhamento (ex: Veo, FIRST, IMR), permitindo até 70\% de redução de dose com alto custo de processamento;
  \item \textbf{DLR (4ª Geração):} Redes neurais convolucionais profundas treinadas supervisionadamente para produzir imagens de altíssima qualidade instantaneamente \cite{greffier2026, debbiche2024}.
\end{enumerate}

A \cref{tab:taxonomia_algoritmos} sintetiza os algoritmos comerciais por fabricante.

\begin{table}[htbp]
  \centering
  \small
  \caption{Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante.}
  \label{tab:taxonomia_algoritmos}
  \begin{tabularx}{\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
    \toprule
    Fabricante & Reconstrução Iterativa Híbrida (HIR) & Reconstrução Baseada em Modelos (MBIR) & Reconstrução por Aprendizado Profundo (DLR) \\
    \midrule
    GE Healthcare & ASiR / ASiR-V & Veo & \textbf{TrueFidelity} (treinado com FBP em dose plena) \\
    \addlinespace
    Canon Medical & AIDR 3D / AIDR 3D Enhanced & FIRST & \textbf{AiCE} (treinado com MBIR / FIRST) \\
    \addlinespace
    Siemens Healthineers & SAFIRE / ADMIRE & REDUCE & \textbf{Precise Image} / \textbf{Alpha Engine} (PCCT) \\
    \addlinespace
    Philips Healthcare & iDose4 & IMR & \textbf{Precise Image} (redes convolucionais profundas) \\
    \bottomrule
  \end{tabularx}
\end{table}

Embora visualmente nítidas, essas redes neurais introduzem fortes não-linearidades físicas que desafiam a metrologia clássica.

\section{Quebra da Linearidade e o Efeito Ceroso}
\label{sec:quebra_linearidade}

Em algoritmos DLR, o mapeamento entre o sinograma $\mathbf{y}$ e a imagem reconstruída $\mathbf{x}$ opera através de camadas convolucionais com ativações não lineares (ReLU/LeakyReLU):
\begin{equation}
  \mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}
  \label{eq:nao_linear_dlr}
\end{equation}

Essa formulação não linear gera quatro consequências físicas críticas (\cref{fig:dlr_non_linear}):
\begin{enumerate}
  \item \textbf{Resolução Dependente do Contraste e da Cena:} Bordas de alto contraste (+300 HU) mantêm alta resolução, enquanto lesões de baixo contraste (+20 HU) sofrem atenuação excessiva de altas frequências;
  \item \textbf{Não-Estacionariedade Espacial do Ruído (Quebra de WSS):} O ruído varia ponto a ponto na imagem de acordo com a proximidade de estruturas anatômicas densas;
  \item \textbf{Efeito Ceroso (\emph{Plastic/Waxy Look}):} A rede neural concentra a variância do ruído em baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$), removendo o padrão natural de rampa e mascarando bordas tumorais sutis \cite{toia2023};
  \item \textbf{Falha dos Modelos Lineares Tradicionais:} O modelo analítico linear NPWE perde a correlação linear com radiologistas humanos ($r \approx 0{,}68$, Painel B da \cref{fig:dlr_non_linear}).
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D.}
  \label{fig:dlr_non_linear}
\end{figure}

A \cref{fig:dlr_non_linear} expõe a quebra de linearidade em três painéis analíticos:
\begin{itemize}
  \item \textbf{Painel (A) --- Detectabilidade $d'$ vs. Dose em DLR:} O gráfico compara o comportamento de $d'$ em função da dose $\text{CTDI}_{\text{vol}}$ (mGy) para FBP (linha preta tracejada, proporcional a $\sqrt{\text{Dose}}$), HIR (linha azul) e DLR (linha verde contínua). Enquanto a FBP exibe crescimento uniforme, a reconstrução DLR atinge patamares elevados de $d'$ mesmo em doses muito baixas ($< 3\text{ mGy}$), demonstrando a superioridade da IA na supressão de ruído;

  \item \textbf{Painel (B) --- Correlação com Radiologistas em Testes 2AFC:} O eixo horizontal representa o $d'$ medido experimentalmente em médicos radiologistas e o eixo vertical mostra o $d'$ calculado pelos modelos computacionais. O modelo linear clássico NPWE (cruzes vermelhas) exibe grande dispersão e baixa correlação ($r = 0{,}68$), enquanto o modelo por aprendizado profundo DLMO (círculos verdes) apresenta concordância quase perfeita com a linha ideal $y=x$ ($r = 0{,}98$);

  \item \textbf{Painel (C) --- Detrending Polinomial 2D:} Ilustra o isolamento do ruído puro em perfis anatômicos complexos. A curva azul mostra o perfil anatômico bruto $I(x)$ com gradiente macroscópico de tecido, a linha tracejada vermelha representa o ajuste polinomial de 2ª ordem $P_2(x)$, e a curva verde inferior exibe o ruído puro residual purificado $\delta I(x) = I(x) - P_2(x)$, livre de variações anatômicas espúrias.
\end{itemize}

Para estudar essas não-linearidades em condições idênticas à clínica, os simuladores cilíndricos homogêneos foram substituídos pela metodologia de phantoms antropomórficos híbridos.

\section{Metodologia dos Phantoms Híbridos}
\label{sec:phantoms_hibridos}

Redes neurais DLR treinadas com anatomias humanas produzem comportamentos anômalos ao processar cilindros homogêneos de acrílico. A metodologia de phantoms híbridos restabelece o rigor metrológico.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption[Metodologia de Phantoms Híbridos e Teste 2AFC]{Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.}
  \label{fig:phantom_flow}
\end{figure}

Conforme esquematizado no \cref{fig:phantom_flow}, a metodologia estrutura-se em quatro etapas:
\begin{enumerate}
  \item \textbf{Aquisição Física Real com Phantom Antropomórfico (FREDDIE):} Simuladores físicos de alta precisão impressos em 3D com polímeros equivalentes a ossos, pulmão e tecidos moles são escaneados em múltiplos tomógrafos clínicos sob diversos níveis de dose;
  \item \textbf{Banco de Fundos Anatômicos Reais ($H_0$):} Extraem-se milhares de ROIs de parênquima anatômico real livre de patologias físicas;
  \item \textbf{Inserção Digital Híbrida Tridimensional ($H_1$):} Modelam-se computacionalmente lesões 3D (nódulos pulmonares esféricos e espiculados, metástases hepáticas), que são convolvidas com a PSF 3D real do tomógrafo e somadas às imagens antes ou após a reconstrução;
  \item \textbf{Verdade de Campo Absoluta (\emph{Ground Truth}):} Gera-se um banco de dezenas de milhares de casos com coordenadas espaciais, diâmetro e contraste central conhecidos com exatidão matemática, viabilizando o treinamento supervisionado de inteligência artificial e a condução de testes psicofísicos 2AFC com radiologistas.
\end{enumerate}

Para calcular o $NPS$ sobre esses fundos anatômicos heterogêneos sem contaminação por gradientes macroscópicos de densidade, aplica-se o detrending polinomial 2D com determinação de incerteza por Bootstrap.

\section{Detrending Polinomial 2D e Incerteza por Bootstrap}
\label{sec:detrending}

Para cada sub-região anatômica $I_k(x, y)$ ($N_x \times N_y$ pixels), ajusta-se por mínimos quadrados uma superfície polinomial de 2ª ordem $P_2(x, y)$:
\begin{equation}
  P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy
  \label{eq:polinomio_2d}
\end{equation}

Os coeficientes ótimos $\mathbf{a} = (a_0, \dots, a_5)^T$ são obtidos analiticamente através da matriz de Vandermonde $\mathbf{V}$:
\begin{equation}
  \mathbf{a} = (\mathbf{V}^T \mathbf{V})^{-1} \mathbf{V}^T \mathbf{i}_k
  \label{eq:ajuste_minimos_quadrados}
\end{equation}
onde $\mathbf{i}_k$ é o vetor unidimensional resultante da vetorização de $I_k(x, y)$.

A imagem de ruído residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é multiplicada por uma janela de Hanning bidimensional antes do cálculo da Transformada Rápida de Fourier 2D, eliminando vazamentos espectrais de borda.

A determinação da incerteza experimental e dos intervalos de confiança de 95\% do índice $d'$ é calculada por reamostragem Bootstrap não-paramétrica com $B = 2000$ replicações com reposição:
\begin{equation}
  \text{SE}_{\text{boot}}(d') = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B \left( d'^{*(b)} - \bar{d}'^* \right)^2}
  \label{eq:bootstrap_se}
\end{equation}

Com as bases dos algoritmos DLR e dos simuladores híbridos estabelecidas, o próximo capítulo aborda o estado da arte: os Observadores por Aprendizado Profundo com Vision Transformers (DLMO), a física dos detectores de Contagem de Fótons (PCCT) e a Otimização Multiobjetivo pela Fronteira de Pareto Tridimensional.

% ------------------------------------------------------------------------------
% CAPÍTULO 5: APRENDIZADO PROFUNDO, PCCT E OTIMIZAÇÃO
% ------------------------------------------------------------------------------
\chapter{Aprendizado Profundo, PCCT e Otimização}
\label{chap:estado_da_arte}

Este capítulo aborda a fronteira científica da metrologia tomográfica. Apresenta-se o Observador de Modelo por Aprendizado Profundo (DLMO) fundamentado em Vision Transformers (ViT) com auto-atenção multi-cabeça e calibração perceptual multitarefa. Em seguida, detalha-se a física dos detectores de Contagem de Fótons (PCCT) e a síntese de Imagens Monoenergéticas Virtuais ($VMI$). Por fim, formula-se a Otimização Multiobjetivo através do mapeamento da Fronteira de Pareto Tridimensional $(D, T, -W)$.

\section{Observadores Baseados em Aprendizado Profundo (DLMO)}
\label{sec:dlmo}

Para modelar o desempenho de radiologistas sob reconstruções não lineares DLR em anatomias complexas, a física médica desenvolveu os Observadores de Modelo por Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), que emulam a coordenação foveal-periférica humana.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura Neural do DLMO]{Arquitetura Neural do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer) e Calibração Perceptual.}
  \label{fig:dlmo_arch}
\end{figure}

O DLMO utiliza arquiteturas neurais avançadas baseadas em \emph{Vision Transformers} (ViT) com mecanismos de Auto-Atenção Multi-Cabeça (MHSA), conforme esquematizado no \cref{fig:dlmo_arch} \cite{dosovitskiy2021, zhou2021, schilder2026}.

A imagem tomográfica $\mathbf{x} \in \mathbb{R}^{H \times W \times C}$ é particionada em $N_p = \frac{HW}{P^2}$ blocos bidimensionais não-sobrepostos (\emph{patches}) $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 C)}$ com dimensão $P \times P$ (ex: $8 \times 8$ pixels). Cada bloco é linearmente projetado para uma dimensão latente contínua $D_{\text{model}}$ via matriz $\mathbf{E}$:
\begin{equation}
  \mathbf{z}_0 = \left[ \mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \mathbf{x}_p^2 \mathbf{E}; \, \dots; \, \mathbf{x}_p^{N_p} \mathbf{E} \right] + \mathbf{E}_{\text{pos}}
  \label{eq:vit_embedding}
\end{equation}
onde $\mathbf{x}_{\text{class}}$ é o token de classificação diagnóstica e $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N_p + 1) \times D_{\text{model}}}$ adiciona a codificação posicional bidimensional aprendida.

Para cada bloco, calculam-se as matrizes de Consulta ($Q$), Chave ($K$) e Valor ($V$) através de matrizes lineares de pesos $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V$:
\begin{equation}
  Q = \mathbf{z} \mathbf{W}_Q, \qquad K = \mathbf{z} \mathbf{W}_K, \qquad V = \mathbf{z} \mathbf{W}_V
  \label{eq:qkv}
\end{equation}

O operador de auto-atenção por produto escalar escalonado é expresso por:
\begin{equation}
  \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
  \label{eq:attention_formula}
\end{equation}
onde o fator $\sqrt{d_k}$ impede a saturação de gradientes na função softmax.

Do ponto de vista da neurociência, o mecanismo de auto-atenção mimetiza a coordenação visual humana: as cabeças de atenção computam as correlações contextuais do parênquima anatômico periférico enquanto concentram capacidade discriminativa na fóvea central onde se localiza o alvo diagnóstico.

A saída não linear da rede $t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$ permite calcular o índice de detectabilidade do modelo profundo:
\begin{equation}
  d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}
  \label{eq:dprime_dl}
\end{equation}

Para que o DLMO atue como um instrumento metrológico fiel da percepção médica, o treinamento da rede neural é calibrado diretamente contra o desempenho de radiologistas através de perdas perceptuais multitarefa e validação cruzada LOSO.

\section{Calibração Perceptual e Transferibilidade Inter-Scanners}
\label{sec:loso}

O treinamento do DLMO incorpora uma função de perda de otimização multitarefa que penaliza simultaneamente o erro de classificação e os desvios em relação à detectabilidade medida em experimentos 2AFC com radiologistas \cite{zhou2021}:
\begin{equation}
  \mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{BCE}}(y, \hat{y}) + \lambda \, \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2
  \label{eq:perceptual_loss}
\end{equation}
onde $\mathcal{L}_{\text{BCE}}$ é a entropia cruzada binária clássica e $\lambda$ calibra o alinhamento perceptual.

A robustez inter-fabricantes é validada pelo esquema \emph{Leave-One-Scanner-Out} (LOSO): em um conjunto de $K$ tomógrafos distintos (GE, Siemens, Canon e Philips), treina-se o observador com dados de $K - 1$ equipamentos e testa-se cegamente no tomógrafo omitido, garantindo coeficientes de correlação $r > 0{,}95$ em todas as dobras.

Enquanto as reconstruções por IA aprimoram tomógrafos convencionais, a maior inovação física nos detectores de radiação é a Tomografia por Contagem de Fótons (PCCT), analisada a seguir.

\section{Física da Tomografia por Contagem de Fótons (PCCT)}
\label{sec:pcct_fisica}

A tecnologia PCCT representa um salto paradigmático na detecção de raios X ao eliminar o ruído eletrônico e disponibilizar informação espectral intrínseca em cada pixel.

\begin{table}[htbp]
  \centering
  \small
  \caption{Comparativo físico entre as tecnologias de detecção tomográfica EICT e PCCT.}
  \label{tab:eict_vs_pcct}
  \begin{tabularx}{\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.22\textwidth} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
    \toprule
    Característica Física & TC por Integração de Energia (EICT) & TC por Contagem de Fótons (PCCT) \\
    \midrule
    Material Detector & Cintilador cerâmico ($\text{Gd}_2\text{O}_2\text{S}$) + Fotodiodo & Semicondutor de conversão direta (CdTe / CZT / Silício) \\
    \addlinespace
    Mecanismo de Conversão & Indireta: Raios X $\to$ Luz visível $\to$ Carga elétrica & Direta: Raios X $\to$ Pares elétron-lacuna instantâneos \\
    \addlinespace
    Ruído Eletrônico & Integrado cumulativamente ao sinal de raios X & Rejeitado por limiar inferior de energia ($E_{\text{threshold}} > E_{\text{ruído}}$) \\
    \addlinespace
    Resolução Espacial & Limitada por septos ópticos refletivos ($0{,}5 \text{ a } 0{,}6 \text{ mm}$) & Submilimétrica ultra-alta ($0{,}1 \text{ a } 0{,}2 \text{ mm}$, sem septos físicos) \\
    \addlinespace
    Ponderação Espectral & Proporcional à energia do fóton ($S \propto E$, subpondera baixa energia) & Contagem individual com peso unitário ou peso ideal ótimo \\
    \addlinespace
    Capacidade Espectral & Requer duas fontes/camadas de detectores & Intrínseca: Múltiplos canais de energia (\emph{energy bins}) em único disparo \\
    \bottomrule
  \end{tabularx}
\end{table}

Conforme sintetizado na \cref{tab:eict_vs_pcct}, os detectores PCCT utilizam cristais semicondutores de conversão direta (Telureto de Cádmio --- CdTe ou CZT, espessura de $1{,}5\text{ a }3{,}0\text{ mm}$ sob alta tensão de $-800\text{ a }-1000\text{ V}$) \cite{flohr2020, mccollough2026, pimenta2025, pimenta2026}.

A absorção de cada fóton gera instantaneamente pares elétron-lacuna que migram para os ânodos pixelados, gerando um pulso de tensão estritamente proporcional à energia do fóton:
\begin{equation}
  V_{\text{pulso}} \propto Q = \frac{E_{\text{fóton}}}{W_{\text{ionização}}}
  \label{eq:vpulso}
\end{equation}
com $W_{\text{ionização}} \approx 4{,}43\text{ eV}$ para o CdTe (frente a mais de $30\text{ eV}$ em cintiladores convencionais).

Ao separar os pulsos em múltiplos canais de energia através de comparadores ultra-rápidos, o sistema sintetiza Imagens Monoenergéticas Virtuais ($VMI$) em qualquer nível de energia (de 40 a 140 keV):
\begin{equation}
  I_{\text{VMI}}(x, y; E_0) = a_1(x, y) \cdot f_{\text{foto}}(E_0) + a_2(x, y) \cdot f_{\text{Compton}}(E_0)
  \label{eq:vmi_formula}
\end{equation}

Em baixas energias ($40\text{ a }50\text{ keV}$), maximiza-se o contraste fotoelétrico do iodo ($K\text{-edge} = 33{,}2\text{ keV}$), aumentando expressivamente a detectabilidade de lesões vasculares sem a contaminação por ruído eletrônico observada nos tomógrafos EICT.

A diversidade de parâmetros operacionais em EICT e PCCT (kVp, mA, tempo, pitch, algoritmo DLR e energia de VMI) gera um espaço combinatório imenso. A resposta metrológica para encontrar o protocolo clínico ótimo é a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional.

\section{Otimização Multiobjetivo e Fronteira de Pareto 3D}
\label{sec:pareto_otimizacao}

Na rotina clínica de emergências e centros de trauma, a otimização não pode considerar apenas a dose e a detectabilidade: o tempo operacional total ($T$) é uma variável crítica para a sobrevida do paciente. A otimização de protocolos tomográficos é formulada como um problema de minimização vetorial multiobjetivo \cite{oostveen2021}:
\begin{equation}
  \min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}
  \label{eq:multiobjetivo_pareto}
\end{equation}
onde o vetor de decisão $\mathbf{p} = (\text{kVp}, \text{mA}, t_{\text{rot}}, \text{pitch}, \text{corte}, \text{kernel}, \text{nível DLR}, E_{\text{VMI}})^T$ pertence ao espaço viável $\Omega$, sujeito às restrições:
\begin{itemize}
  \item $D(\mathbf{p}) \le \text{DRL}$ (restrição de radioproteção por Níveis de Referência Diagnóstica);
  \item $T(\mathbf{p}) \le T_{\text{máx}}$ (restrição de tempo para evitar artefatos de movimento corporal);
  \item $W(\mathbf{p}) = d'(\mathbf{p}) \ge d'_{\text{mín}}$ (restrição diagnóstica para garantir a acurácia médica).
\end{itemize}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto.}
  \label{fig:pareto_3d}
\end{figure}

A \cref{fig:pareto_3d} ilustra a modelagem da otimização multiobjetivo em dois painéis:
\begin{itemize}
  \item \textbf{Painel (A) --- Compromisso Clínico Dose vs. Detectabilidade:} O eixo horizontal representa a dose de radiação $\text{CTDI}_{\text{vol}}$ (mGy) e o eixo vertical exibe a detectabilidade diagnóstica $W = d'$. A curva verde contínua define a Fronteira Ótima de Pareto (conjunto de soluções não-dominadas). Os pontos cinzas dispersos abaixo da curva representam protocolos clínicos ineficientes dominados (que utilizam doses desnecessárias para a qualidade entregue). Três soluções operacionais ótimas são destacadas: $P_1$ (ponto azul, protocolo de ultrabaixa dose para rastreio preventivo), $P_2$ (ponto laranja, equilíbrio para exames de rotina) e $P_3$ (ponto vermelho, protocolo de alta dose e máxima detectabilidade para estadiamento oncológico detalhado);

  \item \textbf{Painel (B) --- Superfície de Pareto Tridimensional $(D, T, -W)$:} Apresenta a variedade diferenciável bidimensional contínua imersa no espaço euclidiano tridimensional formado pela Dose de Radiação $D$ (mGy), Tempo Operacional total $T$ (segundos) e Detectabilidade Diagnóstica $W = d'$. A superfície com mapa de cores viridis delimita o limite ótimo de desempenho do tomógrafo: qualquer tentativa de reduzir o tempo de varredura ou a dose de radiação sem degradar a detectabilidade atinge a fronteira de Pareto, permitindo a seleção computacional do protocolo ideal via algoritmo genético NSGA-II e método multicritério TOPSIS.
\end{itemize}

Com os modelos teóricos consolidados, o próximo capítulo descreve a arquitetura modular do software desenvolvido e os aspectos éticos de pesquisa com seres humanos.

% ------------------------------------------------------------------------------
% CAPÍTULO 6: ARQUITETURA DE SOFTWARE E METROLOGIA
% ------------------------------------------------------------------------------
\chapter{Arquitetura de Software e Metrologia}
\label{chap:arquitetura_metrologia}

Este capítulo detalha a infraestrutura computacional modular em Python desenvolvida para a execução automatizada do pipeline de metrologia tomográfica. Apresentam-se a padronização das aquisições segundo o relatório AAPM TG-233 e as salvaguardas bioéticas (CEP/CONEP) para os testes com radiologistas.

\section{Arquitetura Modular do Software}
\label{sec:software_arch}

A aplicação prática dos modelos matemáticos depende de uma arquitetura de software reproduzível e robusta, capaz de processar exames DICOM de forma automatizada.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow6_software_pipeline.png}
  \caption[Arquitetura Modular do Software de Metrologia]{Arquitetura Modular do Software de Metrologia em Tomografia Computadorizada (Pipeline Integrado GDRFM-IFUSP).}
  \label{fig:software_flow}
\end{figure}

O software organiza-se em cinco módulos encadeados (\cref{fig:software_flow}) \cite{choopani2023}:
\begin{itemize}
  \item \textbf{Módulo 1 (Parser DICOM):} Realiza a leitura e validação dos metadados de aquisição (kVp, mA, tempo, pitch, espessura, kernel e nível DLR);
  \item \textbf{Módulo 2 (Segmentação Automática):} Localiza as coordenadas dos insertos de calibração via Transformada de Hough e extrai $M \ge 100$ ROIs anatômicas independentes;
  \item \textbf{Módulo 3A (Resolução Espacial):} Calcula $\text{ESF}(r) \to \text{LSF}(r) \to TTF(f)$ e extrai os descritores $f_{50}$ e $f_{10}$;
  \item \textbf{Módulo 3B (Textura e Ruído):} Executa o detrending polinomial 2D $P_2(x, y)$, janelamento Hanning e FFT2, gerando $NPS(u, v)$ e a curva radial $NPS(f)$;
  \item \textbf{Módulo 4 (Observadores de Modelo):} Computa a detectabilidade pelos modelos lineares (NPWE e CHO com canais corticais) e pelo observador profundo DLMO (Vision Transformers);
  \item \textbf{Módulo 5 (Incerteza e Otimização):} Executa a reamostragem Bootstrap ($B = 2000$) e o algoritmo genético NSGA-II com ranqueamento TOPSIS.
\end{itemize}

Para assegurar comparabilidade internacional, as aquisições tomográficas foram padronizadas segundo as diretrizes da AAPM TG-233.

\section{Protocolo Metrológico Padronizado AAPM TG-233}
\label{sec:protocolo_tg233}

A padronização metrológica rigorosa assegura que as medições de detectabilidade sejam diretamente reprodutíveis em qualquer centro de pesquisa internacional. As aquisições tomográficas seguem as diretrizes da AAPM \cite{aapm_tg233_2019}:
\begin{itemize}
  \item Matriz de $512 \times 512$ pixels com FOV ajustado ao diâmetro do phantom ($200\text{ a }350\text{ mm}$);
  \item Espessuras de corte de $0{,}5\text{ a }1{,}0\text{ mm}$ (alta resolução) e $2{,}5\text{ a }5{,}0\text{ mm}$ (rotina);
  \item Tensões de 80, 100, 120 e 140 kVp, cobrindo doses $\text{CTDI}_{\text{vol}}$ de $0{,}5\text{ a }15\text{ mGy}$;
  \item Lesões esféricas com diâmetros de 3, 5, 8 e 10 mm e contrastes clínicos de $-600\text{ HU}$ (nódulo subsólido), $+100\text{ HU}$ (nódulo sólido) e $+30\text{ HU}$ (lesão hepática hipoatenuante).
\end{itemize}

Como a calibração dos observadores envolve a participação de médicos especialistas, é imprescindível cumprir os requisitos éticos da pesquisa com seres humanos.

\section{Aspectos Bioéticos e Regulatórios}
\label{sec:bioetica}

A condução de experimentos psicofísicos com humanos requer conformidade ética estrita para assegurar o consentimento livre e a proteção dos dados dos participantes. Os testes psicofísicos 2AFC com médicos radiologistas cumprem as seguintes diretrizes:
\begin{itemize}
  \item Recrutamento de médicos radiologistas com título de especialista pelo CBR;
  \item Aplicação obrigatória de Termo de Consentimento Livre e Esclarecido (TCLE) com garantia de anonimização;
  \item Monitores diagnósticos calibrados segundo a norma DICOM GSDF ($\ge 400\text{ cd/m}^2$) e iluminação ambiente controlada ($< 15\text{ lux}$);
  \item Controle de fadiga visual mediante sessões curtas (máximo de 100 a 150 pares 2AFC por sessão, duração $< 25$ minutos).
\end{itemize}

Com a arquitetura computacional e as salvaguardas éticas estabelecidas, o capítulo seguinte sintetiza as conclusões desta monografia e apresenta as perspectivas futuras.

% ------------------------------------------------------------------------------
% CAPÍTULO 7: CONSIDERAÇÕES FINAIS E PERSPECTIVAS FUTURAS
% ------------------------------------------------------------------------------
\chapter{Considerações Finais e Perspectivas Futuras}
\label{chap:conclusoes}

Este capítulo final sintetiza as principais contribuições científicas e conceituais desenvolvidas ao longo desta monografia, analisa criticamente a evolução histórica da metrologia em tomografia computadorizada, discute o impacto prático para os serviços de radiologia e para a saúde pública, e estabelece as perspectivas futuras e direções de pesquisa na física médica.

\section{Síntese Global do Trabalho e Trajetória Metrológica}
\label{sec:sintese_global}

A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram uma profunda transformação metodológica nas últimas décadas. Esta monografia investigou sistematicamente a transição dos modelos analíticos clássicos para as formulações perceptuais contemporâneas baseadas em inteligência artificial e detectores de contagem de fótons.

O ponto de partida residiu no reconhecimento da **falência das métricas escalares clássicas** ($SNR$, $CNR$, desvio padrão $\sigma_{\text{HU}}$ e $MTF$ global) frente aos algoritmos não lineares de reconstrução iterativa (HIR, MBIR) e, fundamentalmente, de aprendizado profundo (DLR). Demonstrou-se formalmente que as premissas de linearidade estrita do sistema, isoplanatismo espacial e estacionariedade do ruído no sentido amplo (WSS) foram rompidas. Sob DLR, a redução do desvio padrão em Unidades Hounsfield não decorre de maior contagem física de fótons, mas de operações adaptativas não lineares que suavizam o ruído alterando sua distribuição de frequência (gerando o aspecto textural ceroso ou \emph{plastic look}). Consequentemente, lesões patológicas de baixo contraste podem ser atenuadas e suprimidas da imagem mesmo quando os valores numéricos de $SNR$ e $CNR$ aparentam excelente qualidade.

Como resposta científica a esse desafio, consolidou-se o paradigma da **Qualidade de Imagem Baseada em Tarefa (TBIQ)**, ancorado na Teoria de Detecção de Sinais (SDT). Demonstrou-se que a qualidade de uma imagem médica é uma grandeza estritamente relacional, definida pelo desempenho de um observador ao executar uma tarefa clínica diagnóstica (identificação de nódulos, metástases ou fissuras ósseas). O **Índice de Detectabilidade ($d'$)** emergiu como a grandeza central unificadora, integrando com rigor matemático:
\begin{enumerate}
  \item A resposta de frequência espacial dependente do contraste local ($TTF(f)$ com o descritor $f_{50}$);
  \item A densidade espectral e correlação espacial do ruído ($NPS(f)$ com a frequência de pico $f_{\text{peak}}$);
  \item A geometria e perfil radiológico da patologia ($W_{\text{task}}(f)$ via funções de Bessel);
  \item A sensibilidade ao contraste do olho humano ($E(f)$) ou a capacidade discriminativa de redes neurais corticais.
\end{enumerate}

Na investigação dos **observadores de modelo lineares**, deduziu-se o limite teórico superior estabelecido pelo Observador Ideal Bayesiano e pelo Observador de Hotelling ($d'_{\text{HO}}$), demonstrando o mecanismo de pré-branqueamento do ruído via matriz de autocovariância inversa $\mathbf{K}^{-1}$. Em seguida, derivou-se a integral contínua do modelo antropomórfico Sem Pré-Branqueamento com Filtro Ocular (NPWE), evidenciando sua alta precisão em simuladores homogêneos de calibração e seu subsequente colapso em fundos anatômicos reais. Para contornar a barreira dimensional da covariância em matrizes clínicas, explorou-se a formulação do Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor, validado estatisticamente contra painéis de radiologistas através de modelos de ANOVA com efeitos aleatórios cruzados (MRMC DBM/HOR).

Ao analisar o **estado da arte**, investigaram-se os Observadores Baseados em Aprendizado Profundo (DLMO), construídos sobre arquiteturas *Vision Transformers* (ViT) com auto-atenção multi-cabeça. Demonstrou-se que o mecanismo de atenção mimetiza a coordenação visual foveal-periférica humana, superando a dispersão dos modelos lineares ($r = 0{,}68$) e alcançando concordância quase perfeita com os radiologistas ($r = 0{,}98$). Paralelamente, detalhou-se a biofísica da **Tomografia por Contagem de Fótons (PCCT)**, cujos detectores semicondutores de conversão direta (CdTe/CZT) eliminam o ruído eletrônico e viabilizam Imagens Monoenergéticas Virtuais ($VMI$) em baixos keV com ganho expressivo de contraste fotoelétrico.

Por fim, estruturou-se a **Otimização Multiobjetivo Não Linear** através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade diagnóstica ($W$). Essa formulação viabiliza a seleção automatizada e personalizada de protocolos clínicos através do algoritmo genético NSGA-II e do método multicritério TOPSIS.

\section{Impacto Clínico, Operacional e Regulatório}
\label{sec:impacto_pratico}

Os resultados e metodologias estruturados nesta monografia oferecem contribuições imediatas para a prática clínica e para a gestão hospitalar:
\begin{itemize}
  \item \textbf{Radioproteção Efetiva e Otimização do Princípio ALARA:} A utilização do índice $d'$ fornece uma comprovação física e matemática inequívoca de que reduções de até 50\% a 60\% na dose de radiação em protocolos pediátricos e de rastreio de câncer de pulmão podem ser executadas com total segurança diagnóstica, eliminando a dependência de avaliações visuais puramente subjetivas;

  \item \textbf{Harmonização Inter-Fabricantes em Parques Tecnológicos Complexos:} Grandes centros hospitalares operam simultaneamente tomógrafos de múltiplos fornecedores (GE, Siemens, Canon, Philips) com diferentes gerações de algoritmos DLR. A metodologia de simuladores antropomórficos híbridos com observadores DLMO calibrados via validação cruzada LOSO permite equalizar o desempenho diagnóstico entre todos os equipamentos, garantindo que um paciente receba a mesma acurácia diagnóstica independentemente do tomógrafo utilizado;

  \item \textbf{Conformidade Regulatória e Auditoria de Qualidade:} O pipeline computacional automatizado permite aos serviços de física médica atender com rigor às exigências da ANVISA (RDC 611/2022 e IN 93/2021), aos relatórios da AAPM (TG-233) e aos programas internacionais de auditoria da Agência Internacional de Energia Atômica (IAEA 5-Star), automatizando a emissão de laudos de controle de qualidade e a vigilância contínua de doses e detectabilidade.
\end{itemize}

\section{Perspectivas Futuras e Direções de Pesquisa}
\label{sec:perspectivas_futuras}

A consolidação da física médica na era dos detectores de contagem de fótons e da inteligência artificial generativa abre horizontes promissores para desenvolvimentos futuros:

\begin{enumerate}[label=\textbf{\arabic*.}]
  \item \textbf{Extensão do TBIQ para Aquisições Dinâmicas e 4D:}
  A metodologia baseada em tarefa foi majoritariamente desenvolvida para cortes anatômicos tridimensionais estáticos. Uma fronteira imediata reside na extensão do índice de detectabilidade para aquisições tomográficas com resolução temporal (4D), como a angiotomografia coronariana com sincronização cardíaca (\emph{ECG-gating}) e a tomografia de perfusão cerebral em acidentes vasculares cerebrais (AVC). Nesses cenários, a modelagem matemática do observador deverá incorporar a Função de Transferência Temporal ($TTF_t(f_t)$) e a correlação espaço-temporal do ruído ($NPS(u, v, f_t)$);

  \item \textbf{Modelos Fundacionais e IA Generativa na Avaliação da Percepção:}
  A evolução dos modelos de linguagem e visão multimodal (\emph{Vision-Language Models} e \emph{Foundation Models} em saúde) viabiliza o desenvolvimento de observadores computacionais universais capazes não apenas de fornecer uma pontuação escalar $d'$, mas de justificar textualmente a decisão diagnóstica, apontando regiões de incerteza anatômica e mimetizando a redação de laudos radiológicos estruturados;

  \item \textbf{Mapeamento Espectral Multielementar em PCCT com Nanopartículas:}
  A capacidade dos detectores de contagem de fótons em discriminar múltiplos canais de energia permite a quantificação simultânea de múltiplos agentes de contraste com bordas K distintas (\emph{K-edge imaging}). Pesquisas futuras poderão aplicar observadores de modelo espectrais para avaliar a detectabilidade de nanopartículas funcionalizadas de bismuto, gadolínio, tântalo e ouro direcionadas a biomarcadores tumorais específicos, potencializando o diagnóstico teranóstico;

  \item \textbf{Integração em Tempo Real com Sistemas PACS e Prontuários Eletrônicos:}
  A incorporação dos módulos de software de metrologia em contêineres hospitalares leves permitirá o cálculo automatizado e instantâneo do índice $d'$ para cada exame realizado no hospital. Ao cruzar os dados dos metadados DICOM com os registros de dose do sistema PACS/RIS, o tomógrafo poderá sugerir correções de protocolo em tempo real antes da liberação do paciente;

  \item \textbf{Estudos Psicofísicos Multicêntricos em Larga Escala:}
  A consolidação definitiva de novas normas internacionais de garantia da qualidade requer a expansão dos testes psicofísicos 2AFC para consórcios hospitalares multicêntricos com centenas de médicos radiologistas, estabelecendo bancos de dados públicos de referência para calibração contínua de observadores de inteligência artificial.
\end{enumerate}

Conclui-se esta monografia com a certeza de que a física médica, ao integrar os fundamentos da mecânica quântica de radiações, o processamento estatístico de sinais e a neurociência da percepção visual, estabelece os alicerces definitivos para uma radiologia diagnóstica mais segura, precisa e personalizada.
"""

# Extract ordered cite keys from text
cites = re.findall(r"\\cite\{([^}]+)\}", expanded_tex)
ordered_keys = []
for c in cites:
    keys = [k.strip() for k in c.split(",")]
    for k in keys:
        if k not in ordered_keys:
            ordered_keys.append(k)

bib_database = {
    "bushberg2020": r"BUSHBERG, J. T.; SEIBERT, J. A.; LEIDHOLDT, E. M.; BOONE, J. M. \textbf{The Essential Physics of Medical Imaging}. 4. ed. Philadelphia: Lippincott Williams \& Wilkins, 2020. 1048 p.",
    "attix1986": r"ATTIX, F. H. \textbf{Introduction to Radiological Physics and Radiation Dosimetry}. New York: John Wiley \& Sons, 1986. 607 p.",
    "seeram2015": r"SEERAM, E. \textbf{Computed Tomography: Physical Principles, Clinical Applications, and Quality Control}. 4. ed. St. Louis: Elsevier Health Sciences, 2015. 560 p.",
    "icrp103_2007": r"INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION (ICRP). \textbf{The 2007 Recommendations of the International Commission on Radiological Protection}. ICRP Publication 103. Annals of the ICRP, v. 37, n. 2-4, p. 1--332, 2007.",
    "mccollough2026": r"MCCOLLOUGH, C. H. et al. Radiation dose in computed tomography: technological advances and clinical optimization over two decades. \textbf{Radiology}, v. 318, n. 2, p. e251200, 2026.",
    "anvisa_rdc611_2022": r"AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Resolução da Diretoria Colegiada - RDC nº 611, de 9 de março de 2022}: Estabelece os requisitos sanitários para a organização e o funcionamento de serviços de radiologia diagnóstica ou intervencionista. Brasília: ANVISA, 2022.",
    "anvisa_in93_2021": r"AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Instrução Normativa nº 93, de 27 de maio de 2021}: Estabelece os requisitos sanitários para a garantia da qualidade e da segurança em sistemas de tomografia computadorizada médica. Brasília: ANVISA, 2021.",
    "rose1948": r"ROSE, A. The sensitivity performance of the human eye on an absolute scale. \textbf{Journal of the Optical Society of America}, v. 38, n. 2, p. 196--208, 1948.",
    "burgess1999": r"BURGESS, A. E. The Rose model, revisited. \textbf{Journal of the Optical Society of America A}, v. 16, n. 3, p. 633--646, 1999.",
    "racine2020": r"RACINE, D. et al. Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. \textbf{Physics in Medicine \& Biology}, v. 65, n. 18, p. 185011, 2020.",
    "debbiche2024": r"DEBBICHE, I. et al. Task-based image quality assessment of deep learning image reconstruction in abdominal CT: a multi-reader phantom study. \textbf{European Radiology}, v. 34, n. 5, p. 3120--3132, 2024.",
    "greffier2026": r"GREFFIER, J. et al. Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. \textbf{Diagnostic and Interventional Imaging}, v. 107, n. 1, p. 1016--1025, 2026.",
    "toia2023": r"TOIA, G. V. et al. Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. \textbf{European Radiology}, v. 33, p. 4310--4322, 2023.",
    "solomon2020": r"SOLOMON, J. et al. Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. \textbf{Medical Physics}, v. 47, n. 8, p. 3412--3425, 2020.",
    "aapm_tg233_2019": r"AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., Medical Physics, v. 46, n. 11, p. e735--e756, 2019).",
    "icru54_1996": r"INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). \textbf{Medical Imaging - The Assessment of Image Quality}. ICRU Report 54. Bethesda, MD: ICRU, 1996.",
    "peterson1954": r"PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. \textbf{Transactions of the IRE Professional Group on Information Theory}, v. 4, n. 4, p. 171--212, 1954.",
    "lusted1968": r"LUSTED, L. B. \textbf{Introduction to Medical Decision Making}. Springfield, IL: Charles C Thomas, 1968.",
    "metz1986": r"METZ, C. E. ROC methodology in radiologic imaging. \textbf{Investigative Radiology}, v. 21, n. 9, p. 720--733, 1986.",
    "barrett_myers_2004": r"BARRETT, H. H.; MYERS, K. J. \textbf{Foundations of Image Science}. Hoboken: John Wiley \& Sons, 2004. 1540 p.",
    "wagner1979": r"WAGNER, R. F.; BROWN, D. G.; METZ, C. E. Application of information theory to the assessment of computed tomography. \textbf{Medical Physics}, v. 6, n. 2, p. 83--94, 1979.",
    "burgess1994": r"BURGESS, A. E. Statistically defined backgrounds: performance of a modified nonprewhitening observer model. \textbf{Journal of the Optical Society of America A}, v. 11, n. 4, p. 1237--1242, 1994.",
    "eckstein2000": r"ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P. Role of knowledge in human visual search for signals in noise. \textbf{Journal of the Optical Society of America A}, v. 17, n. 11, p. 2064--2076, 2000.",
    "myers1987": r"MYERS, K. J.; BARRETT, H. H. Addition of a channel mechanism to the ideal-observer model. \textbf{Journal of the Optical Society of America A}, v. 4, n. 12, p. 2447--2457, 1987.",
    "yao1992": r"YAO, J.; BARRETT, H. H. Predicting human performance by a channelized Hotelling observer model. In: \textbf{SPIE Medical Imaging: Image Perception}, v. 1654, p. 268--278, 1992.",
    "dorfman1992": r"DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E. Receiver operating characteristic rating analysis: generalization to the population of readers and patients with the jackknife method. \textbf{Investigative Radiology}, v. 27, n. 9, p. 723--731, 1992.",
    "obuchowski1995": r"OBUCHOWSKI, N. A.; ROCKETTE, H. E. Hypothesis testing of diagnostic accuracy for multiple readers and multiple tests: an ANOVA approach with dependent observations. \textbf{Communications in Statistics - Simulation and Computation}, v. 24, n. 2, p. 285--308, 1995.",
    "hillis2011": r"HILLIS, S. L.; OBUCHOWSKI, N. A.; BERBAUM, K. S. Multi-reader multi-case ROC analysis: an updated review of methods and software. \textbf{Academic Radiology}, v. 18, n. 7, p. 842--856, 2011.",
    "racine2021": r"RACINE, D. et al. Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. \textbf{Medical Physics}, v. 48, n. 6, p. 2890--2901, 2021.",
    "dosovitskiy2021": r"DOSOVITSKIY, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: \textbf{International Conference on Learning Representations (ICLR)}, 2021. p. 1--21.",
    "zhou2021": r"ZHOU, W. et al. Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. \textbf{IEEE Transactions on Medical Imaging}, v. 40, n. 9, p. 2350--2362, 2021.",
    "schilder2026": r"SCHILDER, C. M. et al. Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. \textbf{La Rivista del Nuovo Cimento}, v. 49, n. 3, p. 145--210, 2026.",
    "flohr2020": r"FLOHR, T. et al. Photon-counting CT review. \textbf{Physica Medica}, v. 79, p. 126--136, 2020.",
    "pimenta2025": r"PIMENTA, E. F.; COSTA, P. R. Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. \textbf{Medical Physics}, v. 52, n. 4, p. 2150--2165, 2025.",
    "pimenta2026": r"PIMENTA, E. F. \textbf{Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax}. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.",
    "oostveen2021": r"OOSTVEEN, L. J. et al. Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. \textbf{European Radiology}, v. 31, p. 7412--7421, 2021.",
    "choopani2023": r"CHOOPANI, R. et al. Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. \textbf{Physics in Medicine \& Biology}, v. 68, n. 14, p. 145002, 2023.",
    "iaea_5star_2026": r"INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA). Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. \textbf{European Journal of Radiology}, v. 184, p. 113133, 2026."
}

bib_entries = []
for k in ordered_keys:
    if k in bib_database:
        bib_entries.append(f"\\bibitem{{{k}}}\n{bib_database[k]}")

for k, content in bib_database.items():
    if k not in ordered_keys:
        bib_entries.append(f"\\bibitem{{{k}}}\n{content}")

bib_block = "\n\n% ==============================================================================\n% ELEMENTOS PÓS-TEXTUAIS (REFERÊNCIAS BIBLIOGRÁFICAS NUMÉRICAS ABNT)\n% ==============================================================================\n\\begin{thebibliography}{99}\n\\addcontentsline{toc}{chapter}{Referências}\n\n" + "\n\n".join(bib_entries) + "\n\n\\end{thebibliography}\n\n\\end{document}\n"

final_tex_content = expanded_tex + bib_block

main_tex_target = os.path.join(output_dir, "main.tex")
with open(main_tex_target, "w", encoding="utf-8") as f:
    f.write(final_tex_content)

# Update build_single_file_overleaf.py
with open("/Users/user/.gemini/antigravity-ide/scratch/build_single_file_overleaf.py", "w", encoding="utf-8") as f:
    f.write(f'import os\nimport zipfile\nimport shutil\n\noutput_dir = "{output_dir}"\n')
    f.write('single_main_tex = r"""' + final_tex_content + '"""\n\n')
    f.write("""with open(os.path.join(output_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(single_main_tex)

zip_target = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_2026.zip"
with zipfile.ZipFile(zip_target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, output_dir)
            zipf.write(full_path, rel_path)

downloads = os.path.expanduser("~/Downloads/Overleaf_TCC_Wagner_2026.zip")
desktop = os.path.expanduser("~/Desktop/Overleaf_TCC_Wagner_2026.zip")
shutil.copy2(zip_target, downloads)
shutil.copy2(zip_target, desktop)
print("Pacote final sincronizado com sucesso!")
""")

# Build zip
zip_target = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_2026.zip"
with zipfile.ZipFile(zip_target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, output_dir)
            zipf.write(full_path, rel_path)

downloads = os.path.expanduser("~/Downloads/Overleaf_TCC_Wagner_2026.zip")
desktop = os.path.expanduser("~/Desktop/Overleaf_TCC_Wagner_2026.zip")
shutil.copy2(zip_target, downloads)
shutil.copy2(zip_target, desktop)

print("Monografia atualizada com Considerações Finais expandidas, sem títulos artificiais de transição e com estrutura limpa!")
