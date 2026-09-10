import os
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
single_main_tex = r"""\documentclass[
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

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica contemporânea, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação do desempenho diagnóstico (princípio ALARA). Historicamente, a garantia da qualidade em TC baseou-se em métricas escalares lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR), o desvio padrão em Unidades Hounsfield ($\sigma_{\text{HU}}$) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores homogêneos de água ou acrílico. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares --- com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade, isoplanatismo e estacionariedade no sentido amplo (WSS) do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais (como o aspecto ceroso ou \emph{plastic/waxy look}) que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), fundamentado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade é formalmente definida pelo desempenho de um observador (médico radiologista ou modelo computacional) na execução de uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Esta monografia apresenta uma investigação aprofundada e estruturada da evolução dos observadores de modelo (\emph{model observers}). Analisa-se a transição do Observador Ideal Bayesiano para os modelos antropomórficos lineares com filtro ocular (NPWE) e canais corticais de frequência (CHO), detalhando suas deduções matemáticas contínuas no domínio de Fourier e demonstrando os limites biofísicos que causam seu colapso sob reconstruções DLR e fundos anatômicos complexos. Investiga-se a extensão populacional e multi-contraste consolidada pelo Índice de Detectabilidade Ponderado pelo Tamanho do Paciente e Tarefa (SSW-$d'$), integrando a variabilidade do diâmetro equivalente em água ($D_w$) e a dosimetria personalizada (SSDE) em Figuras de Mérito ($\text{FOM}_{\text{SSW}}$). Em resposta à ruptura não linear, investiga-se a fronteira científica representada pelos Observadores Baseados em Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça, calibrados diretamente contra leituras psicofísicas de radiologistas em experimentos de Escolha Forçada entre Duas Alternativas (2AFC) sob análise estatística \emph{Multi-Reader Multi-Case} (MRMC). Detalham-se a física dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a formulação da Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade agregada ($W$). Este trabalho estabelece as bases teóricas, biofísicas e metrológicas para a garantia da qualidade em tomografia computadorizada moderna.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. SSW-$d'$. Reconstrução por Aprendizado Profundo. Vision Transformers. Tomografia por Contagem de Fótons. Simuladores Antropomórficos. Otimização Multiobjetivo. Fronteira de Pareto.
\clearpage

% 5. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), standard deviation in Hounsfield Units ($\sigma_{\text{HU}}$), and Modulation Transfer Function (MTF), evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity (WSS). Under non-linear processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer (human radiologist or mathematical model) executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a comprehensive investigation of the evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), detailing their continuous mathematical derivations in the Fourier domain and demonstrating their breakdown in non-linear DLR regimes and structured anatomical backgrounds. We explore the population-wide and multi-contrast extension embodied by the Size-Specific Weighted Detectability Index (SSW-$d'$), integrating water-equivalent diameter ($D_w$) variability and Size-Specific Dose Estimates (SSDE) into comprehensive Figures of Merit ($\text{FOM}_{\text{SSW}}$). In response, we investigate the state of the art in Deep Learning Model Observers (DLMO), which leverage self-attention neural architectures (Vision Transformers) calibrated against expert radiologists' psychophysical performance in Two-Alternative Forced Choice (2AFC) paradigms under Multi-Reader Multi-Case (MRMC) statistical modeling. Furthermore, we explore the physics of Photon-Counting CT (PCCT), the synthesis of Virtual Monoenergetic Images (VMI), and the formulation of Multi-Objective Optimization via the Three-Dimensional Pareto Frontier $(D, T, -W)$, which integrates radiation dose ($D$), operational time ($T$), and diagnostic detectability ($W$). This study establishes the theoretical, computational, and physical foundation required for next-generation CT metrology.

\vspace{0.8cm}
\noindent\textbf{Keywords:} Computed Tomography. Task-Based Image Quality. Model Observers. Detectability Index. SSW-$d'$. Deep Learning Reconstruction. Vision Transformers. Photon-Counting CT. Anthropomorphic Phantoms. Multi-Objective Optimization. Pareto Frontier.
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
\textbf{Dw} & \emph{Water-Equivalent Diameter} (Diâmetro Equivalente em Água) \\
\textbf{EICT} & \emph{Energy-Integrating Computed Tomography} (TC por Integração de Energia) \\
\textbf{ESF} & \emph{Edge Spread Function} (Função de Resposta ao Degrau) \\
\textbf{FBP} & \emph{Filtered Backprojection} (Retroprojeção Filtrada) \\
\textbf{FOM} & \emph{Figure of Merit} (Figura de Mérito) \\
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
\textbf{SSDE} & \emph{Size-Specific Dose Estimate} (Estimativa de Dose Específica por Tamanho) \\
\textbf{SSW-$d'$} & \emph{Size-Specific Weighted Detectability Index} (Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa) \\
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
$\text{SSW-}d'$ & Índice de detectabilidade ponderado pelo tamanho do paciente e contraste da tarefa (adimensional) \\
$\Omega_j$ & Fator de ponderação de relevância clínica atribuído à tarefa/contraste $j$ (adimensional, $\sum \Omega_j = 1$) \\
$D_w$ & Diâmetro equivalente em água da seção anatômica do paciente ou simulador ($\text{cm}$) \\
$D_{w,i}$ & Diâmetro equivalente em água do simulador/biotipo $i$ ($\text{cm}$) \\
$\text{SSDE}(D_w)$ & Estimativa de dose absorvida específica para o tamanho do paciente ($\text{mGy}$) \\
$\text{FOM}_{\text{SSW}}$ & Figura de mérito de eficiência de dose populacional ponderada baseada em tarefa ($\text{mGy}^{-1}$) \\
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

\subsection{Princípios Físicos da Interação e Dedução da Lei de Beer-Lambert}
\label{subsec:beer_lambert_deducao}
A Tomografia Computadorizada baseia-se na medição da atenuação exponencial que um feixe colimado de raios X sofre ao atravessar os tecidos biológicos. A base teórica fundamental dessa interação é a Lei de Beer-Lambert-Bouguer.

\textbf{Requisitos e Premissas Físicas:}
\begin{enumerate}
  \item Feixe de radiação estritamente monoenergético com energia de fótons $E$;
  \item Geometria de feixe fino (estreito) e perfeitamente colimado, de modo que fótons espalhados por efeito Compton no meio não atinjam o detector;
  \item Meio atenuador macroscópico homogêneo ou estratificado, cujas propriedades atômicas não sofrem saturação ou modificação durante a irradiação.
\end{enumerate}

Considere uma camada diferencial de tecido biológico com espessura infinitesimal $dl$ localizada na coordenada espacial $(x, y, z)$. A probabilidade fracionária de que um fóton incidente sofra uma colisão ou absorção ao atravessar essa espessura $dl$ é proporcional ao coeficiente de atenuação linear local $\mu(x, y, z; E)$:
\begin{equation}
  \frac{dI}{I} = -\mu(x, y, z; E) \, dl
  \label{eq:diff_beer}
\end{equation}

Integrando ambos os membros da equação diferencial ao longo do trajeto retilíneo total $L$ percorrido pelo raio X (desde a fonte emissora com intensidade inicial $I_0$ até o elemento detector com intensidade transmitida $I$):
\begin{equation}
  \int_{I_0}^I \frac{dI'}{I'} = -\int_L \mu(x, y, z; E) \, dl \implies \ln\left( \frac{I}{I_0} \right) = -\int_L \mu(x, y, z; E) \, dl
  \label{eq:beer_integral_step}
\end{equation}
Exponenciando ambos os membros, obtém-se a clássica Lei de Beer-Lambert:
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

\subsection{A Transformada de Radon e a Reconstrução por Retroprojeção Filtrada (FBP)}
\label{subsec:radon_fbp}
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

\subsection{Conversão para a Escala Hounsfield (HU)}
\label{subsec:escala_hu}
Para padronizar clinicamente as imagens médicas independentemente do espectro de energia do feixe, os valores do coeficiente de atenuação linear $\mu(x, y)$ são convertidos linearmente para a Escala Hounsfield em Unidades Hounsfield (HU):
\begin{equation}
  \text{CT Number} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{água}}}{\mu_{\text{água}}} \quad (\text{HU})
  \label{eq:escala_hu}
\end{equation}
onde $\mu_{\text{água}}$ é o coeficiente de atenuação linear da água pura calibrado sob a mesma tensão de pico do tubo. Por definição, a água possui $0\text{ HU}$, o ar atmosférico possui $-1000\text{ HU}$, tecidos adiposos variam de $-120\text{ a }-60\text{ HU}$, tecidos moles e órgãos parenquimatosos situam-se entre $+30\text{ e }+70\text{ HU}$, e o osso cortical denso atinge $+1000\text{ a }+3000\text{ HU}$.

\subsection{O Paradoxo: Eficácia Diagnóstica versus Risco Estocástico ALARA}
\label{subsec:paradoxo_alara}
Embora a tomografia computadorizada represente menos de 15\% do total de procedimentos radiológicos realizados anualmente no mundo, ela é responsável por mais de 60\% a 70\% de toda a dose coletiva de radiação médica administrada à população global.

A interação da radiação ionizante com o tecido biológico induz lesões diretas e indiretas (via radiólise da água e geração de radicais livres de oxigênio $\text{OH}^\bullet$) na molécula de ácido desoxirribonucleico (DNA), promovendo quebras de fita dupla (\emph{Double-Strand Breaks} --- DSBs). Segundo a Comissão Internacional de Proteção Radiológica (ICRP Publicação 103), a indução de neoplasias malignas segue o modelo linear sem limiar (\emph{Linear No-Threshold} --- LNT), no qual qualquer incremento de dose absorvida, por menor que seja, eleva proporcionalmente a probabilidade estocástica de carcinogênese radioinduzida ao longo da vida do paciente \cite{icrp103_2007, mccollough2026}.

Essa realidade biofísica impõe o estrito cumprimento do princípio fundamental de radioproteção ALARA (\emph{As Low As Reasonably Achievable}), reafirmado pelas normas da ANVISA (RDC 611/2022 e IN 93/2021) \cite{anvisa_rdc611_2022, anvisa_in93_2021}. O desafio central da física médica contemporânea reside em reduzir a dose de radiação ao mínimo nível exequível sem comprometer a acurácia diagnóstica do exame.

\section{Limitações Físicas das Métricas Tradicionais}
\label{sec:metricas_tradicionais}

\subsection{Definições Matemáticas das Grandezas Escalares Clássicas}
\label{subsec:definicoes_escalares}
Durante quatro décadas, o controle de qualidade tomográfico baseou-se em métricas escalares simples \cite{bushberg2020, seeram2015}:
\begin{enumerate}
  \item \textbf{Relação Sinal-Ruído ($SNR$):}
  \begin{equation}
    SNR = \frac{\mu_{\text{ROI}}}{\sigma_{\text{ROI}}}
    \label{eq:snr_def}
  \end{equation}
  \item \textbf{Relação Contraste-Ruído ($CNR$):}
  \begin{equation}
    CNR = \frac{|\mu_{\text{lesão}} - \mu_{\text{fundo}}|}{\sqrt{\frac{1}{2}(\sigma_{\text{lesão}}^2 + \sigma_{\text{fundo}}^2)}} = \frac{\Delta \mu}{\sigma_{\text{médio}}}
    \label{eq:cnr_def}
  \end{equation}
  \item \textbf{Desvio Padrão do Número de CT ($\sigma_{\text{HU}}$):}
  Representa a dispersão estatística dos valores de pixel em uma ROI homogênea de água ou acrílico:
  \begin{equation}
    \sigma_{\text{HU}} = \sqrt{\frac{1}{N_{\text{pix}} - 1} \sum_{i=1}^{N_{\text{pix}}} (I_i - \mu_{\text{ROI}})^2}
    \label{eq:sigma_hu_def}
  \end{equation}
  Na física de radiação clássica com retroprojeção filtrada, o desvio padrão do ruído quântico de Poisson escala inversamente com a raiz quadrada da fluência de fótons e, portanto, da dose de radiação: $\sigma_{\text{HU}} \propto 1 / \sqrt{\text{Dose}}$.
\end{enumerate}

\subsection{A Resolução Espacial Linear: Da PSF à Função de Transferência de Modulação (MTF)}
\label{subsec:psf_mtf}
\begin{itemize}
  \item \textbf{PSF (\emph{Point Spread Function}):} Descreve como um ponto infinitesimal ideal de altíssimo contraste ($\delta(x, y)$) é transformado pelo tomógrafo em uma distribuição bidimensional borrada $h(x, y)$. Esse alargamento espacial decorre do tamanho geométrico finito da mancha focal do ânodo do tubo de raios X, da abertura angular dos detectores, do cruzamento óptico no cintilador e do algoritmo de amostragem;
  \item \textbf{MTF (\emph{Modulation Transfer Function}):} Representa a magnitude normalizada da Transformada de Fourier bidimensional da PSF:
  \begin{equation}
    MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
    \label{eq:mtf_def}
  \end{equation}
  A MTF expressa a fração de contraste original que o sistema consegue preservar em cada frequência espacial $f$ (medida em ciclos por milímetro, $\text{mm}^{-1}$). Uma MTF igual a 1 indica preservação total do contraste, enquanto valores próximos de 0 indicam perda de detalhe anatômico.
\end{itemize}

\subsection{Os Três Pilares da Validade Linear}
\label{subsec:tres_pilares_linearidade}
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

\subsection{O Ecossistema de Avaliação Tomográfica e a Ruptura Não Linear}
\label{subsec:ecossistema_ruptura}
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

\subsection{Definição Conceitual e os Quatro Pilares do TBIQ}
\label{subsec:quatro_pilares_tbiq}
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

\subsection{O Índice de Detectabilidade ($d'$) como Medida Central Unificadora}
\label{subsec:dprime_unificador}
A integração matemática desses quatro componentes resulta no **Índice de Detectabilidade ($d'$)**, grandeza estatística que quantifica a separabilidade entre estados de saúde e doença. Expandido modernamente para métricas agregadas multi-tarefa e multi-tamanho corporais (como o índice SSW-$d'$), o $d'$ consolida-se como o padrão-ouro da metrologia tomográfica.

Compreendidos os desafios da tomografia computadorizada e a formulação conceitual do paradigma TBIQ, definem-se a seguir os objetivos deste trabalho.

\section{Objetivos}
\label{sec:objetivos}

O objetivo geral desta monografia consiste em desenvolver uma formulação teórica, biofísica e computacional unificada dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo as bases metrológicas para a avaliação de tecnologias avançadas e otimização de protocolos clínicos.

Os objetivos específicos compreendem:
\begin{enumerate}[label=\textbf{\alph*)}]
  \item Formalizar a dedução físico-matemática da Lei de Beer-Lambert, da Transformada de Radon e da quebra de linearidade em algoritmos de Reconstrução por Aprendizado Profundo (DLR);
  \item Deduzir analiticamente a integral contínua do índice de detectabilidade do Observador Antropomórfico com Filtro Ocular (NPWE) no domínio de Fourier e o Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG e Laguerre-Gauss;
  \item Investigar e formalizar a extensão populacional e multi-contraste do índice de detectabilidade através do modelo SSW-$d'$ (\emph{Size-Specific Weighted Detectability Index}), integrando a variabilidade biométrica de diâmetro equivalente em água ($D_w$) com a estimativa de dose específica por tamanho (SSDE) e figuras de mérito de eficiência de dose ($\text{FOM}_{\text{SSW}}$);
  \item Analisar os limites biofísicos dos observadores lineares e modelar os Observadores de Aprendizado Profundo (DLMO) baseados em Vision Transformers (ViT) com auto-atenção multi-cabeça e calibração perceptual;
  \item Caracterizar a biofísica da detecção de fótons na Tomografia por Contagem de Fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a modelagem estocástica de tensores de ruído multi-energia;
  \item Estruturar a formulação matemática da Otimização Multiobjetivo através do mapeamento numérico da Fronteira de Pareto Tridimensional $(D, T, -W)$ acoplando o algoritmo genético NSGA-II ao método TOPSIS;
  \item Desenvolver a arquitetura modular em Python para automação do pipeline metrológico segundo a AAPM TG-233, estabelecendo salvaguardas regulatórias e bioéticas (CEP/CONEP).
\end{enumerate}

Uma vez estabelecidos os objetivos, o capítulo seguinte aborda os fundamentos da avaliação baseada em tarefa, detalhando a teoria estatística de detecção de sinais e as métricas espectrais em Fourier.

% ------------------------------------------------------------------------------
% CAPÍTULO 2: FUNDAMENTOS DA AVALIAÇÃO BASEADA EM TAREFA
% ------------------------------------------------------------------------------
\chapter{Fundamentos da Avaliação Baseada em Tarefa}
\label{chap:fundamentos_tbiq}

A avaliação objetiva da qualidade de imagem em física médica exige a superação de abordagens subjetivas através de uma formulação matemática rigorosa da decisão diagnóstica. Este capítulo estabelece a base teórica do paradigma TBIQ, derivando a Teoria de Detecção de Sinais (SDT), os experimentos psicofísicos de Escolha Forçada entre Duas Alternativas (2AFC) e as grandezas espectrais no domínio de Fourier padronizadas pelo relatório internacional AAPM TG-233: a Função de Transferência da Tarefa ($TTF(f)$) e o Espectro de Potência do Ruído ($NPS(f)$).

\section{Teoria de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria}

\subsection{Formulaç\~ao Matemática das Hipóteses Estatísticas}
\label{subsec:sdt_hipoteses}
A tomada de decisão médica na interpretação de uma imagem tomográfica pode ser formulada como um problema de teste de hipóteses estatísticas binárias \cite{peterson1954, lusted1968, metz1986, barrett_myers_2004}:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad \text{(Hipótese Nula: Ausência de lesão, apenas ruído e fundo)} \label{eq:h0_def}\\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad \text{(Hipótese Alternativa: Presença de lesão com sinal } \mathbf{s} \text{ sobre o fundo } \mathbf{b}\text{)} \label{eq:h1_def}
\end{align}
onde $\mathbf{g} \in \mathbb{R}^N$ é o vetor que contém os $N$ pixels da imagem, $\mathbf{s} \in \mathbb{R}^N$ representa o sinal determinístico da lesão patológica e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo.

Um observador (seja um médico radiologista ou um algoritmo computacional) processa a imagem $\mathbf{g}$ através de uma função escalar de decisão, gerando uma estatística de teste $t(\mathbf{g}) \in \mathbb{R}$. A decisão final é obtida comparando $t(\mathbf{g})$ com um limiar de corte predefinido $t_c$:
\begin{equation}
  \text{Decisão} = \begin{cases}
    \text{Diagnóstico Positivo } (H_1), & \text{se } t(\mathbf{g}) \ge t_c \\
    \text{Diagnóstico Negativo } (H_0), & \text{se } t(\mathbf{g}) < t_c
  \end{cases}
  \label{eq:regra_decisao}
\end{equation}

A \cref{tab:matriz_confusao} sintetiza a matriz de contingência diagnóstica.

\begin{table}[htbp]
  \centering
  \small
  \caption{Matriz de contingência clássica da teoria da decisão diagnóstica.}
  \label{tab:matriz_confusao}
  \begin{tabularx}{0.85\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.28\textwidth} >{\centering\arraybackslash}X >{\centering\arraybackslash}X}
    \toprule
    Decisão do Observador & Estado Real: $H_1$ (Lesão Presente) & Estado Real: $H_0$ (Lesão Ausente) \\
    \midrule
    Positivo ($t \ge t_c$) & Verdadeiro-Positivo ($TP$) & Falso-Positivo ($FP$ - Erro Tipo I) \\
    \addlinespace
    Negativo ($t < t_c$) & Falso-Negativo ($FN$ - Erro Tipo II) & Verdadeiro-Negativo ($TN$) \\
    \bottomrule
  \end{tabularx}
\end{table}

\subsection{A Curva ROC e o Índice de Detectabilidade ($d'$)}
\label{subsec:roc_dprime}
Ao variar continuamente o limiar $t_c \in (-\infty, +\infty)$, mapeia-se a Fração de Verdadeiros-Positivos ($\text{TPF}(t_c)$ ou Sensibilidade) em função da Fração de Falsos-Positivos ($\text{FPF}(t_c)$ ou $1 - \text{Especificidade}$), gerando a Curva de Característica de Operação do Receptor (\emph{Receiver Operating Characteristic} --- ROC).

Sob a hipótese de que a estatística de teste segue distribuições normais com variâncias iguais $\sigma^2$ sob ambas as hipóteses ($t|H_0 \sim \mathcal{N}(\mu_0, \sigma^2)$ e $t|H_1 \sim \mathcal{N}(\mu_1, \sigma^2)$), o \textbf{Índice de Detectabilidade ($d'$)} é definido formalmente como a separação padronizada entre as médias das distribuições:
\begin{equation}
  d' = \frac{\mu_1 - \mu_0}{\sigma} = \frac{\langle t \rangle_{H_1} - \langle t \rangle_{H_0}}{\sqrt{\frac{1}{2}\sigma_{t|H_1}^2 + \frac{1}{2}\sigma_{t|H_0}^2}}
  \label{eq:dprime_def}
\end{equation}

A Área sob a Curva ROC ($AUC$) relaciona-se analiticamente com o índice $d'$ por:
\begin{equation}
  AUC = \Phi\left( \frac{d'}{\sqrt{2}} \right) \iff d' = \sqrt{2} \, \Phi^{-1}(AUC)
  \label{eq:auc_dprime}
\end{equation}
onde $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-u^2/2} \, du$ é a função de distribuição cumulativa da normal padrão, e $\Phi^{-1}$ é a sua inversa (função quantil).

\subsection{O Paradoxo de Rose Revisitado: Limite Perceptual Humano}
\label{subsec:rose_paradoxo}
Na década de 1940, Albert Rose postulou que um observador humano requer uma Relação Sinal-Ruído mínima de $k \approx 4\text{ a }5$ para detectar com 100\% de certeza uma lesão circular homogênea imersa em ruído branco \cite{rose1948, burgess1999}:
\begin{equation}
  SNR_{\text{Rose}} = \frac{C \cdot \sqrt{A}}{\sigma_{\text{pixel}}} \ge 5
  \label{eq:rose_criterio}
\end{equation}
onde $C = \frac{|\mu_{\text{sinal}} - \mu_{\text{fundo}}|}{\mu_{\text{fundo}}}$ é o contraste relativo, $A$ é a área física da lesão e $\sigma_{\text{pixel}}$ é o desvio padrão do ruído.

Embora o modelo de Rose forneça uma intuição física seminal, ele falha ao assumir que o ruído é espacialmente não correlacionado (ruído branco plano). Na tomografia computadorizada real, a filtragem da FBP ou os algoritmos não lineares DLR induzem forte correlação espacial entre pixels vizinhos (ruído colorido), exigindo o tratamento rigoroso das métricas no domínio da frequência espacial de Fourier.

\subsection{Paradigma Psicofísico de Escolha Forçada (2AFC)}
\label{subsec:psicofisica_2afc}
Para mensurar experimentalmente a detectabilidade humana ($d'_{\text{humano}}$) sem a interferência de critérios subjetivos de confiança dos radiologistas, utiliza-se o paradigma psicofísico de Escolha Forçada entre Duas Alternativas (\emph{Two-Alternative Forced Choice} --- 2AFC).

Em cada ensaio, são exibidos dois campos de imagem idênticos lado a lado: um contendo apenas fundo ($H_0$) e outro contendo a lesão patológica imersa no fundo ($H_1$). O leitor deve obrigatoriamente apontar qual imagem contém o sinal. A fração empírica de acertos $P_C \in [0{,}5; 1{,}0]$ converte-se no índice de detectabilidade humano através da relação exata \cite{burgess1999, barrett_myers_2004}:
\begin{equation}
  P_C = \Phi\left( \frac{d'}{\sqrt{2}} \right) \iff d'_{\text{humano}} = \sqrt{2} \, \Phi^{-1}(P_C)
  \label{eq:2afc_pc_dprime}
\end{equation}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig1_sdt_roc_2afc.png}
  \caption[Fundamentos da SDT, Curvas ROC e Paradigma 2AFC]{Fundamentos da Teoria de Detecção de Sinais, Curvas ROC e Paradigma 2AFC.}
  \label{fig:sdt_roc}
\end{figure}

\subsection{Análise dos Gráficos da Figura 2.1 em Cenário Clínico Hipotético}
\label{subsec:analise_fig1}
Para compreender a aplicação da SDT em uma \textbf{situação clínica hipotética}, considere a detecção de um carcinoma hepatocelular (CHC) precoce de $5\text{ mm}$ com baixo contraste hipovascular ($\Delta C = +20\text{ HU}$) em uma TC de abdome. A \cref{fig:sdt_roc} ilustra a tomada de decisão médica:

\begin{itemize}
  \item \textbf{Painel (A) --- Distribuições de Decisão e Sobreposição Estatística:} As curvas exibem a densidade de probabilidade da estatística de decisão sob $H_0$ (azul) e sob $H_1$ (laranja). O aumento da dose de radiação afasta as médias $\mu_0$ e $\mu_1$, elevando $d'$ de $1{,}0$ para $2{,}5$. O deslocamento do limiar $t_c$ calibra a conduta médica: um limiar conservador reduz falsos-positivos mas aumenta o risco de não diagnosticar o tumor (falso-negativo);
  
  \item \textbf{Painel (B) --- Curvas Características de Operação do Receptor (ROC):} À medida que a qualidade da imagem melhora ($d'$ cresce de $0{,}5$ a $3{,}0$), a curva ROC aproxima-se do vértice superior esquerdo, elevando a área $AUC$ de $0{,}64$ para $0{,}98$. Em $d' = 2{,}5$, o radiologista atinge sensibilidade de 90\% com menos de 5\% de falsos-positivos;

  \item \textbf{Painel (C) --- Proporção de Acertos 2AFC vs. $d'$:} Mapeia a conversão matemática não linear entre o percentual de acerto do radiologista e a detectabilidade. Uma taxa de acerto $P_C = 92\%$ em teste duplo-cego corresponde exatamente a $d' = 2{,}0$, fornecendo o padrão-ouro biológico para calibração dos observadores matemáticos.
\end{itemize}

\section{Métricas Espectrais em Fourier (AAPM TG-233)}
\label{sec:metricas_aapm_tg233}

\subsection{A Função de Transferência da Tarefa ($TTF(f)$)}
\label{subsec:ttf_deducao}
Para caracterizar a resolução espacial em sistemas tomográficos não lineares, a AAPM consolidou a Função de Transferência da Tarefa ($TTF(f)$), que avalia a resposta em frequência de forma dependente do contraste e do nível de atenuação da lesão investigada \cite{aapm_tg233_2019}.

A partir da imagem de um inserto cilíndrico de calibração com raio nominal $R$ e contraste conhecido $\Delta C$, extraem-se os perfis radiais de atenuação para obter a Função de Resposta ao Degrau superamostrada ($\text{ESF}(r)$). A Função de Espalhamento de Linha ($\text{LSF}(r)$) é obtida pela derivada numérica da $\text{ESF}(r)$:
\begin{equation}
  \text{LSF}(r) = \frac{d}{dr} \left[ \text{ESF}(r) \right]
  \label{eq:lsf_def}
\end{equation}

A $TTF(f)$ é formalizada pela magnitude normalizada da Transformada de Fourier unidimensional da $\text{LSF}(r)$:
\begin{equation}
  TTF(f) = \frac{\left| \displaystyle\int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\left| \displaystyle\int_{-\infty}^{\infty} \text{LSF}(r) \, dr \right|}
  \label{eq:ttf_def}
\end{equation}

Para quantificar a largura de banda da $TTF(f)$, utilizam-se dois descritores padronizados: $f_{50}$ (frequência espacial na qual a modulação cai para 50\%) e $f_{10}$ (frequência na qual cai para 10\%, definindo o limite prático de resolução espacial).

\subsection{O Espectro de Potência do Ruído ($NPS(f)$)}
\label{subsec:nps_deducao}
O ruído em tomografia computadorizada apresenta correlação espacial orientada decorrente do processo de retroprojeção e dos filtros de convolução. O Espectro de Potência do Ruído ($NPS(u, v)$) quantifica a variância do ruído decomposta por frequência espacial bidimensional $(u, v)$ \cite{aapm_tg233_2019}:
\begin{equation}
  NPS(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \frac{1}{M} \sum_{m=1}^M \left| \mathcal{F}_{2D} \left\{ I_m(x, y) - P_2(x, y) \right\} \right|^2
  \label{eq:nps_2d}
\end{equation}
onde $\Delta x, \Delta y$ são as dimensões físicas dos pixels (mm), $N_x, N_y$ é a dimensão da matriz da ROI (tipicamente $128 \times 128$), $M$ é o número de ROIs homogêneas independentes amostradas ($M \ge 100$) e $P_2(x, y)$ é um polinômio bidimensional de 2ª ordem ajustado para remover tendências anatômicas de baixa frequência (\emph{detrending}).

Assumindo isotropia estatística radial, calcula-se o $NPS(f)$ radial unidimensional integrando sobre anéis circulares no espaço de frequências:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial}
\end{equation}
onde $f = \sqrt{u^2 + v^2}$. A integração total do $NPS(f)$ em todo o domínio de Fourier recupera a variância escalar do número de CT na imagem: $\sigma_{\text{HU}}^2 = \int_0^{\infty} NPS(f) 2\pi f \, df$.

\subsection{O Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$)}
\label{subsec:wtask_deducao}
Para uma lesão circular ideal com raio físico $R$ (mm) e perfil cilíndrico de contraste central $\Delta C$ (HU), o sinal no domínio espacial expressa-se por:
\begin{equation}
  s(r) = \Delta C \cdot \Pi\left( \frac{r}{2R} \right) = \begin{cases}
    \Delta C, & \text{se } r \le R \\
    0, & \text{se } r > R
  \end{cases}
  \label{eq:sinal_cilindrico}
\end{equation}

Aplicando a Transformada de Fourier bidimensional com simetria circular (Transformada de Fourier-Bessel / Hankel de ordem zero):
\begin{equation}
  W_{\text{task}}(f) = \mathcal{F}_{2D}\{s(r)\} = 2\pi \int_0^R \Delta C \, J_0(2\pi f r) r \, dr = \Delta C \cdot \frac{R}{f} J_1(2\pi R f)
  \label{eq:wtask_bessel}
\end{equation}
onde $J_1(\cdot)$ é a função de Bessel ordinária de primeira espécie e ordem 1.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_aapm_tg233_metrics.png}
  \caption[Métricas Padronizadas AAPM TG-233: TTF, NPS e $W_{\text{task}}$]{Métricas Padronizadas segundo o Relatório AAPM TG-233: TTF, NPS e $W_{\text{task}}$.}
  \label{fig:tg233_metrics}
\end{figure}

\subsection{Análise dos Gráficos da Figura 2.2 em Cenário Clínico Hipotético}
\label{subsec:analise_fig2}
Para compreender o papel das métricas espectrais em uma \textbf{situação clínica hipotética}, considere a diferenciação entre um nódulo pulmonar calcificado denso ($\Delta C = +800\text{ HU}$) e um nódulo subsólido em vidro fosco ($\Delta C = +30\text{ HU}$). A \cref{fig:tg233_metrics} demonstra a análise metrológica:

\begin{itemize}
  \item \textbf{Painel (A) --- Função de Transferência da Tarefa ($TTF(f)$):} Em sistemas não lineares, a resposta em frequência depende do contraste. A curva preta ($+800\text{ HU}$) apresenta $f_{50} = 0{,}42\text{ mm}^{-1}$, preservando bordas finas. Já para baixo contraste ($+30\text{ HU}$, curva vermelha), os algoritmos de suavização adaptativa reduzem a largura de banda para $f_{50} = 0{,}24\text{ mm}^{-1}$, borrando o nódulo em vidro fosco;

  \item \textbf{Painel (B) --- Espectro de Potência do Ruído ($NPS(f)$):} O gráfico exibe a distribuição de frequências do ruído para três níveis de dose ($2\text{ mGy}$, $6\text{ mGy}$ e $12\text{ mGy}$). O aumento da dose reduz a amplitude de pico ($NPS_{\text{max}}$ cai de $1800$ para $350\text{ HU}^2\cdot\text{mm}^2$), mas a frequência de pico mantém-se em $f_{\text{peak}} \approx 0{,}28\text{ mm}^{-1}$, característica do filtro de convolução selecionado;

  \item \textbf{Painel (C) --- Espectro da Tarefa ($W_{\text{task}}(f)$):} Ilustra o espectro de Fourier para lesões esféricas de diferentes tamanhos ($d = 3, 5, 10\text{ mm}$). Lesões grandes ($10\text{ mm}$, curva preta) concentram toda a energia em baixíssimas frequências ($f < 0{,}1\text{ mm}^{-1}$), sendo limitadas pelo ruído macroscópico; microlesões ($3\text{ mm}$, curva azul) demandam altas frequências ($f > 0{,}5\text{ mm}^{-1}$), sendo altamente sensíveis à resolução espacial da $TTF$.
\end{itemize}

Com as grandezas espectrais no domínio de Fourier estruturadas, o capítulo seguinte aborda os observadores lineares clássicos e a validação psicofísica.

% ------------------------------------------------------------------------------
% CAPÍTULO 3: OBSERVADORES LINEARES E VALIDAÇÃO PSICOFÍSICA
% ------------------------------------------------------------------------------
\chapter{Observadores Lineares e Validação Psicofísica}
\label{chap:observadores_lineares}

Os observadores de modelo são operadores matemáticos desenvolvidos para quantificar objetivamente a qualidade da imagem em tarefas de detecção. Este capítulo analisa a evolução dos modelos lineares clássicos --- partindo do limite físico do Observador Ideal e do Observador de Hotelling, passando pelo modelo antropomórfico NPWE e culminando no Observador de Hotelling Canalizado (CHO) ---, introduz a extensão populacional e multi-contraste consolidada pelo índice SSW-$d'$, e detalha a metodologia de ANOVA Multi-Reader Multi-Case (MRMC) para validação contra painéis de radiologistas.

\section{O Observador Ideal e o Observador de Hotelling}
\label{sec:observador_ideal}

\subsection{Fundamentação Bayesiana e Razão de Verossimilhança}
\label{subsec:bayes_io}
Para quantificar o desempenho de um sistema tomográfico, é fundamental estabelecer o teto teórico absoluto de informação diagnóstica permitido pelas leis da física. O Observador Ideal (IO) fundamenta-se na razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$. Quando o ruído de fundo segue uma distribuição normal multivariada com matriz de autocovariância $\mathbf{K}$, a razão de verossimilhança logarítmica reduz-se ao Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}.

\subsection{Dedução Passo a Passo do Observador de Hotelling}
\label{subsec:deducao_hotelling}
\textbf{Requisitos e Premissas Matemáticas:}
\begin{enumerate}
  \item Sinal exatamente conhecido (\emph{Signal Known Exactly} --- SKE);
  \item Fundo estatisticamente conhecido (\emph{Background Known Statistically} --- BKS);
  \item O ruído segue uma distribuição normal multivariada com matriz de autocovariância $\mathbf{K} \in \mathbb{R}^{N \times N}$ simétrica e estritamente positiva definida.
\end{enumerate}

Pelo Teorema de Bayes e pela teoria da decisão estatística, a razão de verossimilhança ótima $\Lambda(\mathbf{g})$ sob distribuição gaussiana é:
\begin{equation}
  \Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)} = \frac{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) \right)}{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} \right)}
  \label{eq:bayes_ratio}
\end{equation}
Tomando o logaritmo natural de $\Lambda(\mathbf{g})$ e cancelando os termos quadráticos $\mathbf{g}^T \mathbf{K}^{-1} \mathbf{g}$:
\begin{equation}
  \ln\Lambda(\mathbf{g}) = -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) + \frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g} - \frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}
  \label{eq:log_bayes}
\end{equation}
Como o termo $-\frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ é uma constante independente da imagem medida $\mathbf{g}$, ele é absorvido no limiar de corte $t_c$. A estatística de teste escalar ótima do Observador de Hotelling é dada por:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:template_hotelling}
\end{equation}
onde o vetor de pesos $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ atua realizando o pré-branqueamento (\emph{prewhitening}) do ruído através da matriz inversa $\mathbf{K}^{-1}$, descorrelacionando os pixels antes da integração com o sinal $\mathbf{s}$.

\subsection{O Índice $d'_{\text{HO}}$ como Teto de Desempenho Físico}
\label{subsec:dprime_ho_teto}
O índice de detectabilidade máximo atingível pelo Observador de Hotelling é dado por:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling}
\end{equation}
Nenhum observador biológico ou computacional pode superar $d'_{\text{HO}}$, tornando-o o padrão-ouro teórico para avaliação de sistemas de aquisição e eficiência quântica de detecção ($DQE$).

Embora o Observador de Hotelling seja ótimo matematicamente, o sistema visual humano não realiza a inversão matricial do ruído $\mathbf{K}^{-1}$. Para modelar radiologistas humanos em imagens homogêneas, formulou-se o modelo Sem Pré-Branqueamento com Filtro Ocular (NPWE).

\section{O Observador NPWE}
\label{sec:npwe_deducao}

\subsection{Motivação Biológica e o Filtro Ocular}
\label{subsec:npwe_motivacao}
Em tarefas de detecção em fundos uniformes, o observador humano correlaciona a imagem diretamente com a forma esperada da lesão ($\mathbf{w}_{\text{NPW}} = \mathbf{s}$). Para incorporar a fisiologia da visão, Burgess (1994) introduziu o filtro ocular $E(f)$ e uma componente de ruído neural interno $\sigma_{\text{int}}^2$, originando o modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) \cite{burgess1994, eckstein2000}.

\subsection{Dedução da Integral Contínua do NPWE no Domínio de Fourier}
\label{subsec:deducao_integral_npwe}
No domínio contínuo de Fourier, a integral contínua do índice de detectabilidade do NPWE expressa-se por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral}
\end{equation}

Essa equação elegante unifica a resposta óptica do tomógrafo ($TTF$), o espectro da lesão ($W_{\text{task}}$), a sensibilidade visual humana ($E(f)$) e a potência do ruído ($NPS$) em uma única integração unidimensional.

O modelo NPWE atua com excelente precisão em simuladores homogêneos, mas falha ao avaliar fundos anatômicos heterogêneos. Para tratar a anatomia estruturada, a física médica introduziu os canais corticais de frequência no Observador de Hotelling Canalizado (CHO).

\section{O Observador de Hotelling Canalizado (CHO)}
\label{sec:cho_teoria}

\subsection{A Barreira Dimensional da Covariância Anatômica}
\label{subsec:barreira_dimensional_cho}
Na rotina clínica, as lesões patológicas estão imersas em complexas anatomias estruturadas. Em imagens clínicas com matriz $N = 128 \times 128 = 16.384$ pixels, a matriz de covariância anatômica $\mathbf{K}_{\mathbf{b}} \in \mathbb{R}^{N \times N}$ possui mais de 268 milhões de elementos, inviabilizando sua inversão numérica direta \cite{myers_barrett_1987, gallas2003}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Pipeline Computacional do Observador CHO]{Pipeline Computacional do Observador de Hotelling Canalizado (CHO).}
  \label{fig:cho_flow}
\end{figure}

\subsection{Formulação Matemática dos Canais Corticais}
\label{subsec:formulacao_canais_cho}
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

\subsection{Análise dos Gráficos da Figura 3.2 em Cenário Clínico Hipotético}
\label{subsec:analise_fig3}
Para compreender a ação dos canais corticais em uma \textbf{situação clínica hipotética}, considere a detecção de um nódulo pulmonar peri-pleural encostado no arco costal ósseo (+1200 HU) e em vasos sanguíneos adjacentes. O fundo não é homogêneo, apresentando gradientes intensos e bordas ósseas. A \cref{fig:cho_channels} demonstra como o CHO soluciona a tomada de decisão médica:

\begin{itemize}
  \item \textbf{Painel (A) --- Canais Passa-Faixa D-DOG Corticais:} O gráfico exibe a resposta espectral normalizada para cinco canais concêntricos de Diferença Densa de Gaussianas, cujos picos cobrem perfeitamente o espectro de $0{,}10\text{ a }0{,}85\text{ mm}^{-1}$. Cada canal atua como um filtro passa-faixa sintonizado nos neurônios da área visual primária (V1), isolando as componentes de frequência da lesão das flutuações macroscópicas do fundo;

  \item \textbf{Painel (B) --- Perfis Espaciais de Laguerre-Gauss:} O gráfico exibe as funções de base ortogonal de Laguerre-Gauss em função do raio radial $r$ (mm). As ordens polinomiais $n=0, 1, 2, 3$ decompõem a lesão esférica em harmônicos radiais concêntricos com simetria rotacional, capturando bordas e transições com pouquíssimos graus de liberdade;

  \item \textbf{Painel (C) --- Campo Receptivo Bidimensional de Gabor ($\theta = 45^\circ$):} O mapa espacial 2D ilustra um filtro de Gabor orientado a $45^\circ$, que combina uma envoltória gaussiana com modulação senoidal para modelar neurônios corticais simples com seletividade direcional (essenciais para detectar bordas de vasos oblíquos e interfaces pleurais);

  \item \textbf{Painel (D) --- Detectabilidade $d'$ vs. Nível de Dose em Fundo Anatômico:} Evidencia o colapso do modelo analítico NPWE em fundo estruturado real (curva vermelha inferior). Como o NPWE não possui canais de descorrelação, ele confunde as variações das costelas com ruído quântico e subestima drasticamente a detectabilidade real ($d' < 0{,}8$). Por outro lado, o modelo CHO D-DOG (curva verde) descorrelaciona o fundo ósseo e preserva a capacidade do radiologista ($d' = 2{,}2$).
\end{itemize}

\section{O Índice de Detectabilidade Ponderado pelo Tamanho do Paciente e Tarefa (SSW-$d'$)}
\label{sec:ssw_dprime_completo}

\subsection{Limitações da Métrica Pontual e a Variabilidade Biométrica ($D_w$)}
\label{subsec:ssw_limitacoes_pontuais}
O índice de detectabilidade clássico ($d'_{\text{NPWE}}$ ou $d'_{\text{CHO}}$), conforme formalizado nos relatórios AAPM TG-233 e ICRU 54, é tradicionalmente avaliado de forma \emph{pontual}: calcula-se o valor de $d'$ para um único diâmetro de simulador cilíndrico (tipicamente o módulo padrão de $20\text{ cm}$ do phantom Catphan 600 ou módulo homogêneo de água) e para um único nível de contraste de inserção isolado (por exemplo, um inserto de iodo a $+100\text{ HU}$ ou acrílico a $+120\text{ HU}$) \cite{aapm_tg233_2019, icru54_1996}.

Todavia, na prática clínica hospitalar diária, essa abordagem pontual enfrenta duas limitações metrológicas fundamentais:
\begin{enumerate}
  \item \textbf{Variabilidade Biométrica Populacional e Atenuação dos Raios X:} Os pacientes atendidos em um serviço de radiologia apresentam ampla heterogeneidade dimensional e tecidual, variando desde neonatos e pacientes pediátricos ($D_w \approx 12\text{ a } 18\text{ cm}$) até adultos normoponderais ($D_w \approx 24\text{ a } 30\text{ cm}$) e indivíduos com obesidade mórbida ($D_w \ge 36\text{ cm}$). A atenuação quântica do feixe de raios X cresce exponencialmente com a espessura anatômica atenuadora atravessada (Lei de Beer-Lambert, \cref{eq:beer_lambert}), de modo que a fluência de fótons que atinge os detectores decai drasticamente em pacientes volumosos, elevando a densidade espectral de ruído $NPS(f)$ e degradando a $TTF(f)$ em algoritmos não lineares adaptativos. Para descrever fidedignamente a atenuação radiológica em seções anatômicas complexas (como o tórax e o abdome), a AAPM (Relatórios 204 e 220) padronizou o \textbf{Diâmetro Equivalente em Água ($D_w$, \emph{Water-Equivalent Diameter})}, definido pela integral da atenuação seccional normalizada pela água \cite{aapm_report204}:
  \begin{equation}
    D_w = 2 \sqrt{\left( \frac{\overline{\text{CT}}_{\text{ROI}}}{1000} + 1 \right) \frac{A_{\text{ROI}}}{\pi}}
    \label{eq:dw_definicao_aapm}
  \end{equation}
  onde $A_{\text{ROI}}$ é a área seccional transversal total do paciente ($\text{mm}^2$) e $\overline{\text{CT}}_{\text{ROI}}$ representa o valor médio de atenuação em Unidades Hounsfield dentro da seção;

  \item \textbf{O Espectro Multi-Tarefa em uma Mesma Varredura Tomográfica:} Um protocolo clínico (como a TC de abdome e pelve com contraste intravenoso) nunca é executado para responder a uma única pergunta diagnóstica isolada. O médico radiologista necessita detectar e caracterizar simultaneamente múltiplos alvos com contrastes e tamanhos distintos em uma mesma imagem:
  \begin{itemize}
    \item Lesões parenquimatosas sutis de baixo contraste (ex.: metástases hepáticas hipovasculares, $\Delta C \approx 15\text{ a } 25\text{ HU}$);
    \item Realces vasculares e lesões hipervasculares com meio de contraste iodado (ex.: tromboembolismo ou carcinoma hepatocelular na fase arterial, $\Delta C \approx 150\text{ a } 300\text{ HU}$);
    \item Estruturas de alto contraste (ex.: microcálculos renais ou calcificações vasculares, $\Delta C \ge 400\text{ HU}$).
  \end{itemize}
\end{enumerate}

Um protocolo tomográfico ajustado para otimizar a detectabilidade de estruturas de alto contraste (por exemplo, aplicando um filtro de convolução duro/\emph{sharp kernel}) amplifica o ruído em altas frequências, podendo inviabilizar completamente a detecção de lesões de baixo contraste. Da mesma forma, um protocolo calibrado exclusivamente para um paciente de tamanho médio de $20\text{ cm}$ pode sub-irradiar severamente um paciente obeso, gerando artefatos de fome de fótons (\emph{photon starvation}) que destroem a eficácia diagnóstica. Portanto, avaliar um tomógrafo ou protocolo por um único valor escalar pontual de $d'$ constitui uma simplificação excessiva que mascara deficiências diagnósticas em subpopulações e tarefas clínicas específicas.

\subsection{Requisitos, Premissas e Dedução Matemática do SSW-$d'$}
\label{subsec:ssw_deducao_matematica}
Para transpor essa barreira metrológica, Fitton et al. (2026) introduziram o conceito do \textbf{Índice de Detectabilidade Ponderado pelo Tamanho do Paciente e Contraste da Tarefa (\emph{Size-Specific Weighted Detectability Index} --- SSW-$d'$)}, consolidando e expandindo os modelos de qualidade baseada em tarefa em populações heterogêneas \cite{fitton2026, goppel2021}.

\textbf{Requisitos e Premissas Metrológicas:}
\begin{enumerate}
  \item \textbf{Amostragem Multi-Tamanho de Simuladores:} Disponibilidade de um conjunto de calibração composto por $I$ diâmetros equivalentes em água $D_{w,i} \in \{D_{w,1}, D_{w,2}, \dots, D_{w,I}\}$ (por exemplo, módulos de $16\text{ cm}$, $23\text{ cm}$, $30\text{ cm}$ e $38\text{ cm}$, representando as faixas biométricas pediátrica, adulto pequeno, adulto padrão e obeso mórbido);
  \item \textbf{Definição do Espectro de Tarefas Clínicas:} Seleção de um conjunto de $J$ tarefas diagnósticas representativas com contrastes nominais $C_j \in \{C_1, C_2, \dots, C_J\}$ e morfologias de sinal $\mathbf{s}_j$;
  \item \textbf{Atribuição de Pesos de Relevância Clínica ($\Omega_j$):} Definição de fatores de ponderação $\Omega_j \in [0, 1]$ que quantificam o impacto clínico relativo de cada tarefa $j$ no desfecho médico, satisfazendo a condição estrita de normalização unitária:
  \begin{equation}
    \sum_{j=1}^J \Omega_j = 1, \quad \text{com } \Omega_j \ge 0, \; \forall j \in \{1, \dots, J\}
    \label{eq:normalizacao_pesos_omega}
  \end{equation}
  \item \textbf{Cálculo das Métricas Espectrais Locais:} Determinação experimental da Função de Transferência da Tarefa $TTF(f; D_{w,i}, C_j)$ e do Espectro de Potência do Ruído $NPS(f; D_{w,i})$ para cada diâmetro $i$ e contraste $j$, calculando-se o índice pontual $d'_{i,j} = d'(D_{w,i}, C_j)$ através de um observador de modelo antropomórfico validado (NPWE ou CHO).
\end{enumerate}

\textbf{Dedução Passo a Passo:}
Para um determinado biotipo corporal com diâmetro equivalente em água $D_{w,i}$, a detectabilidade média balanceada sobre o espectro de patologias clínicas investigadas é formulada pela combinação linear ponderada:
\begin{equation}
  d'_{\text{ponderado}, i} = \sum_{j=1}^J \Omega_j \cdot d'_{i,j} = \sum_{j=1}^J \Omega_j \cdot d'(D_{w,i}, C_j)
  \label{eq:dprime_ponderado_tamanho_i}
\end{equation}

Agregando o desempenho sobre toda a coorte de $I$ dimensões corporais representativas da população atendida no serviço de saúde, o índice SSW-$d'$ é definido por \cite{fitton2026, goppel2021}:
\begin{equation}
  \text{SSW-}d' = \frac{1}{I} \sum_{i=1}^{I} \left( \sum_{j=1}^{J} \Omega_j \cdot d'_{i,j} \right)
  \label{eq:ssw_dprime_discreto_uniforme}
\end{equation}

Quando se dispõe do perfil demográfico epidemiológico real da instituição hospitalar, no qual cada biotipo $D_{w,i}$ possui uma probabilidade de ocorrência clínica $p(D_{w,i})$ (com $\sum_{i=1}^I p(D_{w,i}) = 1$), a formulação expande-se para a média ponderada populacional:
\begin{equation}
  \text{SSW-}d' = \sum_{i=1}^{I} p(D_{w,i}) \left[ \sum_{j=1}^{J} \Omega_j \cdot d'(D_{w,i}, C_j) \right]
  \label{eq:ssw_dprime_populacional_discreto}
\end{equation}

No limite contínuo, considerando a distribuição biométrica de pacientes como uma função densidade de probabilidade $p(D_w)$ definida no suporte físico $[D_{w,\min}, D_{w,\max}]$, a formulação contínua integral do SSW-$d'$ expressa-se analiticamente por:
\begin{equation}
  \text{SSW-}d' = \int_{D_{w,\min}}^{D_{w,\max}} p(D_w) \left[ \sum_{j=1}^J \Omega_j \, d'(D_w, C_j) \right] dD_w
  \label{eq:ssw_dprime_continuo_integral}
\end{equation}

O índice SSW-$d'$ condensa, portanto, em um único escalar metrologicamente robusto, toda a matriz de desempenho do tomógrafo diante da diversidade anatômica e patológica dos pacientes.

\subsection{Integração com a Estimativa de Dose Específica por Tamanho (SSDE) e Figura de Mérito ($\text{FOM}_{\text{SSW}}$)}
\label{subsec:ssw_ssde_fom}
Para que o índice SSW-$d'$ seja plenamente aplicável à otimização dosimétrica do princípio ALARA, ele deve ser acoplado à dosimetria física personalizada do paciente. O índice padronizado $\text{CTDI}_{\text{vol}}$ reportado no console do tomógrafo é mensurado em simuladores homogêneos rígidos de PMMA (de $16\text{ cm}$ ou $32\text{ cm}$ de diâmetro), não representando a dose absorvida no órgão do paciente real \cite{bushberg2020, aapm_report204}.

A AAPM formalizou a \textbf{Estimativa de Dose Específica por Tamanho (\emph{Size-Specific Dose Estimate} --- SSDE)}, que converte o $\text{CTDI}_{\text{vol}}$ na dose absorvida média local através de um fator multiplicativo de conversão exponencial $f(D_w)$ tabulado no relatório AAPM Report 204 \cite{aapm_report204}:
\begin{equation}
  \text{SSDE}(D_w) = f(D_w) \cdot \text{CTDI}_{\text{vol}} = \left( a \cdot e^{-b \cdot D_w} \right) \cdot \text{CTDI}_{\text{vol}}
  \label{eq:ssde_formula}
\end{equation}
onde, para o simulador de referência corporal padrão de $32\text{ cm}$, os coeficientes empíricos valem $a = 3{,}704$ e $b = 0{,}0367\text{ cm}^{-1}$.

Integrando a dosimetria populacional ($\text{SSDE}$) ao índice de detectabilidade ponderado ($\text{SSW-}d'$), formula-se a \textbf{Figura de Mérito Populacional Baseada em Tarefa ($\text{FOM}_{\text{SSW}}$)}:
\begin{equation}
  \text{FOM}_{\text{SSW}} = \frac{\left( \text{SSW-}d' \right)^2}{\overline{\text{SSDE}}}
  \label{eq:fom_ssw_formula}
\end{equation}
onde $\overline{\text{SSDE}} = \sum_{i=1}^I p(D_{w,i}) \text{SSDE}(D_{w,i})$ é a dose média efetivamente absorvida pela coorte de pacientes.

A grandeza $\text{FOM}_{\text{SSW}}$ (com dimensão física de $\text{mGy}^{-1}$) estabelece o indicador definitivo de eficiência energética e radiológica de um tomógrafo: ela quantifica quanta detectabilidade diagnóstica agregada o sistema é capaz de produzir por unidade de dose absorvida real na população.

\subsection{Sensibilidade Metrológica do SSW-$d'$: Tensão (kVp), Algoritmos DLR e PCCT vs EICT}
\label{subsec:ssw_sensibilidade_metrologica}
Estudos experimentais recentes (com destaque para as avaliações multicêntricas de Fitton et al., 2026 e Greffier et al., 2026) demonstraram que o índice SSW-$d'$ possui alta sensibilidade para guiar escolhas complexas de parametrização clínica \cite{fitton2026, greffier2026}:
\begin{enumerate}
  \item \textbf{Seleção da Tensão do Tubo (kVp):} Em tarefas contrastadas com iodo ($\Omega_{\text{iodo}} > 0{,}4$), a redução da tensão de $120\text{ kVp}$ para $80\text{ kVp}$ ou $70\text{ kVp}$ eleva expressivamente o SSW-$d'$ em pacientes pequenos e médios ($D_w \le 26\text{ cm}$), devido à proximidade da energia dos fótons com a borda K do iodo ($33{,}2\text{ keV}$). No entanto, em pacientes volumosos ($D_w \ge 34\text{ cm}$), a extrema atenuação do feixe de baixa energia causa fome quântica de fótons, degradando o SSW-$d'$. O modelo ponderado identifica numericamente a tensão ótima que maximiza a $\text{FOM}_{\text{SSW}}$ global;
  \item \textbf{Efeito dos Algoritmos de Reconstrução por Aprendizado Profundo (DLR):} A aplicação de redes neurais DLR eleva o SSW-$d'$ em $35\text{ a }60\%$ quando comparada à FBP clássica sob a mesma dose $\text{CTDI}_{\text{vol}}$, sustentando esse ganho mesmo em diâmetros elevados ($D_w > 32\text{ cm}$) devido à capacidade das redes residuais de sintetizar filtros adaptativos de regularização de ruído sem suprimir bordas de baixo contraste;
  \item \textbf{Superioridade Metrológica da Contagem de Fótons (PCCT vs EICT):} Em detectores PCCT de conversão direta, a eliminação do ruído eletrônico ($\sigma_{\text{el}}^2 = 0$) e a reconstrução de Imagens Monoenergéticas Virtuais ($VMI$) em baixas energias ($45\text{ a }55\text{ keV}$) proporcionam um ganho médio de $+42\%$ no índice SSW-$d'$ e de até $+85\%$ na $\text{FOM}_{\text{SSW}}$ em comparação aos tomógrafos convencionais EICT sob protocolos de ultrabaixa dose \cite{fitton2026, pimenta2026}.
\end{enumerate}

\subsection{Análise em Cenário Clínico Hipotético: Otimização Abdominal em População Heterogênea}
\label{subsec:ssw_cenario_clinico_hipotetico}
Para ilustrar a relevância do SSW-$d'$ na prática da Física Médica hospitalar, considere a auditoria de um protocolo de TC de abdome total em um hospital universitário que atende uma distribuição biométrica heterogênea: $15\%$ de pacientes pediátricos/adolescentes ($D_w = 16\text{ cm}$), $55\%$ de adultos de biotipo padrão ($D_w = 28\text{ cm}$) e $30\%$ de pacientes obesos ($D_w = 36\text{ cm}$).

O exame envolve três tarefas diagnósticas simultâneas com pesos clínicos definidos pelo corpo clínico de radiologia:
\begin{itemize}
  \item \textbf{Tarefa 1 ($\Omega_1 = 0{,}50$):} Detecção de metástases hepáticas sutis de baixo contraste ($\Delta C = 20\text{ HU}$, diâmetro $6\text{ mm}$);
  \item \textbf{Tarefa 2 ($\Omega_2 = 0{,}30$):} Identificação de infiltração vascular ou lesão focal hipervascularizada na fase arterial ($\Delta C = 160\text{ HU}$, diâmetro $4\text{ mm}$);
  \item \textbf{Tarefa 3 ($\Omega_3 = 0{,}20$):} Detecção de litíase renal obstrutiva de alto contraste ($\Delta C = 400\text{ HU}$, diâmetro $3\text{ mm}$).
\end{itemize}

\paragraph{Impacto na Decisão do Físico Médico e na Tarefa do Radiologista:}
Se o físico médico calibrasse o controle automático de exposição (AEC) utilizando apenas a medição clássica pontual de $d'$ no simulador padrão de $20\text{ cm}$, o protocolo aparentaria estar otimizado com $d' = 2{,}4$. No entanto, ao analisar a distribuição por biotipo, constatar-se-ia que nos pacientes obesos ($D_w = 36\text{ cm}$) a detectabilidade da lesão hepática de baixo contraste colapsa para $d'_{3,1} = 0{,}75$, valor muito abaixo do limiar aceitável de Rose ($d' \ge 1{,}5$), provocando falso-negativos em 40\% dos exames oncológicos em indivíduos obesos.

Ao empregar a métrica integrada SSW-$d'$ e maximizar a $\text{FOM}_{\text{SSW}}$, o físico médico reparametriza a curva de modulação de corrente do tubo (mA) em função da atenuação e seleciona a reconstrução DLR adaptativa. Essa intervenção garante que o SSW-$d'$ atinja $2{,}15$ e que nenhum estrato populacional apresente $d' < 1{,}6$, assegurando equidade diagnóstica e radioproteção otimizada para toda a população de pacientes do hospital.

\subsection{Síntese do Subcapítulo e Balanço Metrológico}
\label{subsec:ssw_sintese_balanco}
\begin{itemize}
  \item \textbf{Impacto Metrológico:} O SSW-$d'$ expande a teoria clássica de detecção de sinais de uma medição pontual estática para um modelo agregador populacional e multitarefa, alinhado à complexidade clínica real da medicina diagnóstica;
  \item \textbf{Vantagens sobre Métricas Anteriores:} Consolida múltiplos contrastes de lesão ($\Omega_j$) e variações anatômicas de tamanho do paciente ($D_w$), permitindo o acoplamento direto com a dosimetria personalizada $\text{SSDE}$ através da Figura de Mérito $\text{FOM}_{\text{SSW}}$;
  \item \textbf{Limitações do Modelo:} Exige conjuntos de calibração multi-tamanho e calibração prévia dos pesos clínicos $\Omega_j$ em conjunto com a equipe médica para cada indicação diagnóstica específica.
\end{itemize}

\section{Validação Psicofísica Multi-Reader Multi-Case (MRMC)}
\label{sec:mrmc_teoria}

\subsection{Fontes de Variabilidade na Leitura Radiológica}
\label{subsec:mrmc_fontes_variabilidade}
A avaliação clínica envolve duas fontes principais de variabilidade aleatória: diferenças de julgamento entre médicos e variações anatômicas entre pacientes. O modelo MRMC é a ferramenta estatística mandatória para comprovar a equivalência metrológica entre observadores computacionais e radiologistas humanos.

\subsection{O Modelo de ANOVA com Efeitos Aleatórios Cruzados (DBM / HOR)}
\label{subsec:mrmc_anova_modelo}
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

\subsection{Critérios de Homologação Estatística}
\label{subsec:mrmc_homologacao}
O teste de hipótese utiliza a estatística $F$ com graus de liberdade ajustados de Satterthwaite, exigindo-se um Coeficiente de Correlação Intraclasse $ICC \ge 0{,}90$ para homologação do modelo computacional.

Com os modelos lineares e as extensões ponderadas consolidadas, o próximo capítulo investiga a ruptura provocada pela inteligência artificial nos algoritmos DLR e a metodologia de simuladores híbridos com detrending polinomial.

% ------------------------------------------------------------------------------
% CAPÍTULO 4: A TRANSIÇÃO DO PARADIGMA LINEAR PARA O NÃO LINEAR
% ------------------------------------------------------------------------------
\chapter{A Transição do Paradigma Linear para o Não Linear: Da Ruptura da FBP aos Algoritmos de Aprendizado Profundo}
\label{chap:colapso_linearidade}

A evolução da Tomografia Computadorizada nas últimas duas décadas é marcada pela transição inevitável de um paradigma de reconstrução estritamente linear (dominado pela Retroprojeção Filtrada --- FBP) para um paradigma não linear e adaptativo (baseado em reconstruções iterativas estatísticas e redes neurais profundas --- DLR). Este capítulo dedica-se a investigar profundamente os motivos físicos, dosimétricos, algorítmicos e perceptuais que forçaram essa transferência paradigmática. Analisam-se os limites intrínsecos da FBP perante o princípio ALARA, a quebra dos pilares matemáticos da linearidade (superposição, isoplanatismo e estacionariedade no sentido amplo), as alterações na textura perceptual do ruído (o efeito ceroso ou \emph{plastic look}), o consequente colapso dos observadores de modelo lineares clássicos e a necessidade de reformulação da metrologia através de simuladores antropomórficos híbridos.

\section{As Forças Motrizes da Transição: O Limite Físico da FBP e a Pressão Dosimétrica ALARA}
\label{sec:forcas_motrizes}

Por quase quatro décadas, a Retroprojeção Filtrada (FBP) reinou absoluta na tomografia computadorizada devido à sua elegância matemática, estabilidade analítica e baixo custo computacional. No entanto, a FBP possui uma rigidez física intrínseca: é um operador estritamente linear e invariante no espaço.

A física quântica das radiações impõe que o ruído nos detectores de raios X segue uma distribuição de Poisson, na qual o desvio padrão das contagens é proporcional à raiz quadrada do número de fótons transmitidos ($\sigma_N \propto \sqrt{N}$). Ao aplicar a inversão analítica linear da FBP com filtro de rampa $|f|$, essa flutuação quântica é amplificada em altas frequências, estabelecendo a lei de escala clássica:
\begin{equation}
  \sigma_{\text{HU}} \propto \frac{1}{\sqrt{\text{Dose}}}
  \label{eq:escala_fbp_dose}
\end{equation}

Essa relação determinou um limite físico intransponível para a FBP: qualquer tentativa de reduzir a dose de radiação em 50\% ou 75\% para atender aos preceitos de radioproteção ALARA em exames pediátricos ou de rastreio oncológico populacional acarretava, obrigatoriamente, um aumento de 41\% a 100\% no desvio padrão do ruído ($\sigma_{\text{HU}}$). Na FBP, o aumento do ruído mascara completamente lesões patológicas sutis de baixo contraste. Para conter o ruído na FBP sem aumentar a dose, a única alternativa disponível era a aplicação de filtros de convolução suaves (\emph{smooth kernels}), os quais degradavam severamente a resolução espacial (borramento de bordas).

A FBP atingiu, portanto, seu esgotamento tecnológico: era impossível diminuir a dose sem aumentar o ruído ou perder resolução espacial sob operadores lineares. A única rota científica viável para romper essa barreira dosimétrica foi a introdução de \textbf{algoritmos de reconstrução não lineares e adaptativos}, capazes de desacoplar a redução de ruído da perda de resolução espacial.

\section{Evolução Cronológica e Taxonomia dos Algoritmos de Reconstrução}
\label{sec:taxonomia_dlr}

A resposta da engenharia e da física médica ao esgotamento da FBP estruturou-se em quatro gerações algorítmicas sucessivas:
\begin{enumerate}
  \item \textbf{1ª Geração --- Retroprojeção Filtrada (FBP):} Inversão analítica linear direta da Transformada de Radon. Preserva estritamente as propriedades de linearidade e isoplanatismo, mas exige alta fluência de fótons para manter a qualidade diagnóstica;
  \item \textbf{2ª Geração --- Reconstruções Iterativas Híbridas Estatísticas (HIR):} Algoritmos que mesclam dados da FBP com laços iterativos no domínio das projeções e da imagem (ex: ASiR, AIDR 3D, SAFIRE, iDose4). Modelam o ruído de contagem de fótons através de pesos estatísticos inversamente proporcionais à variância do sinal, permitindo reduções de dose de 20\% a 40\%;
  \item \textbf{3ª Geração --- Reconstruções Iterativas Baseadas em Modelos Físicos (MBIR):} Modelam com alto rigor a geometria tridimensional do feixe (mancha focal finita, alargamento do cone, resposta angular e crosstalk dos detectores) combinada a modelos estatísticos de ruído quântico e espalhamento (ex: Veo, FIRST, IMR). Permitem reduções de dose de até 60\% a 75\%, mas exigiam tempos de processamento computacional proibitivos para a rotina de emergência hospitalar (até 30 a 45 minutos por exame);
  \item \textbf{4ª Geração --- Reconstrução por Aprendizado Profundo (DLR):} Redes neurais convolucionais profundas (\emph{Deep CNNs}) e redes residuais treinadas com milhões de parâmetros sob supervisão direta de exames de alta dose ou modelos MBIR de altíssima qualidade (ex: TrueFidelity, AiCE, Precise Image). As redes DLR realizam a supressão não linear de ruído e a preservação de bordas anatômicas instantaneamente (em poucos segundos por volume), viabilizando o uso clínico em larga escala \cite{greffier2026, debbiche2024}.
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

\section{A Ruptura dos Pilares Físicos e Matemáticos da Linearidade}
\label{sec:quebra_linearidade}

A substituição da FBP pelos algoritmos DLR representou uma ruptura formal dos três pilares da física matemática de imagens:

\subsection{1. Quebra do Princípio da Superposição Linear}
\label{subsec:quebra_superposicao}
Em um sistema linear $\mathcal{L}$, a resposta a uma soma de estímulos é idêntica à soma das respostas individuais: $\mathcal{L}\{\alpha f_1 + \beta f_2\} = \alpha \mathcal{L}\{f_1\} + \beta \mathcal{L}\{f_2\}$. Em redes DLR, a presença de funções de ativação não lineares (ReLU, LeakyReLU, GELU) e camadas de limiarização adaptativa faz com que o operador de reconstrução $\mathcal{R}_{\text{DLR}}$ seja não linear:
\begin{equation}
  \mathcal{R}_{\text{DLR}}(\alpha \mathbf{y}_1 + \beta \mathbf{y}_2) \ne \alpha \mathcal{R}_{\text{DLR}}(\mathbf{y}_1) + \beta \mathcal{R}_{\text{DLR}}(\mathbf{y}_2)
  \label{eq:quebra_superposicao}
\end{equation}
Como consequência direta, a resposta do tomógrafo deixa de ser independente da intensidade do sinal: estruturas de alto contraste (como ossos e vasos preenchidos por iodo, $> 300\text{ HU}$) são identificadas pela rede como bordas verdadeiras e reconstruídas com máxima nitidez, enquanto lesões sutis de baixo contraste (como metástases hepáticas de $+25\text{ HU}$) podem ser interpretadas pela rede como flutuações estatísticas de ruído e excessivamente suavizadas.

\subsection{2. Quebra do Isoplanatismo (Invariância Espacial)}
\label{subsec:quebra_isoplanatismo}
Na FBP, a Função de Resposta ao Ponto $\text{PSF}(x, y)$ é uniforme em todo o campo de visão. Em algoritmos DLR, a resolução espacial torna-se fortemente local e dependente do contexto anatômico vizinho: a PSF no centro de um órgão homogêneo é substancialmente mais larga (mais borrada) do que a PSF nas proximidades de uma cortical óssea densa.

\subsection{3. Quebra da Estacionariedade no Sentido Amplo (WSS) e o Efeito Ceroso}
\label{subsec:quebra_wss_efeito_ceroso}
O ruído deixa de satisfazer a condição de WSS, tornando sua variância e autocovariância dependentes da posição espacial e da anatomia circundante. Além disso, a regularização não linear altera drasticamente a distribuição de frequências do ruído: enquanto na FBP o ruído concentra-se em altas frequências (formato de rampa clássico), em algoritmos não lineares a variância é deslocada para baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$). Esse fenômeno origina o \textbf{aspecto textural ceroso ou plástico (\emph{plastic/waxy look})}, caracterizado por aglomerações e manchas artificiais que causam desconforto perceptual aos médicos radiologistas e mascaram microestruturas patológicas.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D.}
  \label{fig:dlr_non_linear}
\end{figure}

\subsection{Análise dos Gráficos da Figura 4.1 em Cenário Clínico Hipotético}
\label{subsec:analise_fig4}
Para contextualizar o impacto dos algoritmos DLR em uma \textbf{situação clínica hipotética}, considere a avaliação de um protocolo tomográfico de ultrabaixa dose ($\text{CTDI}_{\text{vol}} = 1{,}5\text{ mGy}$) para acompanhamento de litíase renal recorrente em um paciente jovem de 28 anos. A \cref{fig:dlr_non_linear} ilustra esse cenário:

\begin{itemize}
  \item \textbf{Painel (A) --- Detectabilidade $d'$ vs. Dose em DLR:} Na FBP convencional (linha preta), a redução da dose para 1,5 mGy derruba o índice de detectabilidade para $d' = 0{,}8$, tornando pequenos cálculos renais invisíveis sob o ruído quântico. Em contrapartida, a reconstrução DLR (linha verde) alcança $d' = 1{,}8$ na mesma dose de 1,5 mGy, garantindo a visualização precisa do cálculo com 70\% de economia de radiação;

  \item \textbf{Painel (B) --- Correlação com Radiologistas em Testes 2AFC:} Revela a falha do modelo analítico NPWE sob DLR (cruzes vermelhas, $r = 0{,}68$), que superestima a detectabilidade por não capturar as não-linearidades da rede neural. Por outro lado, o modelo por aprendizado profundo DLMO (círculos verdes) alcança correlação quase perfeita com os radiologistas humanos ($r = 0{,}98$), permitindo validar novos protocolos sem necessidade de convocar médicos para testes manuais;

  \item \textbf{Painel (C) --- Detrending Polinomial 2D no Isolamento do Ruído:} Ao medir o espectro $NPS$ no parênquima renal ou hepático, o gradiente natural de densidade dos tecidos (curva azul $I(x)$) contaminaria as baixas frequências do ruído. O ajuste de superfície de 2ª ordem $P_2(x)$ (linha tracejada vermelha) subtrai essa variação macroscópica, isolando o ruído quântico puro $\delta I(x) = I(x) - P_2(x)$ (curva verde inferior).
\end{itemize}

\section{Por que os Observadores Lineares Clássicos Colapsam sob DLR?}
\label{sec:colapso_observadores_lineares}

O colapso dos modelos analíticos clássicos (NPWE e CHO) diante de imagens geradas por DLR fundamenta-se em três limitações biofísicas intransponíveis:
\begin{enumerate}
  \item \textbf{Incompatibilidade com o Domínio de Fourier:} A derivação analítica do NPWE em Fourier (\cref{eq:dprime_npwe_integral}) assume a comutatividade da Transformada de Fourier com o operador do tomógrafo. Em redes DLR não lineares, a resposta em frequência passa a depender da forma e amplitude da lesão ($TTF(f; \Delta C, R)$), invalidando a separabilidade estrita entre sinal e ruído;
  \item \textbf{Incapacidade de Modelar o Efeito Ceroso:} O filtro ocular linear $E(f)$ assume que o olho humano atenua baixas frequências segundo a Função de Sensibilidade ao Contraste padrão (CSF). No entanto, o ruído ceroso da DLR introduz correlações de textura não-gaussianas que o cérebro humano interpreta como falsas estruturas anatômicas, degradando a eficiência do especialista em até 30\% a mais do que o previsto pelo NPWE \cite{toia2023};
  \item \textbf{Rigidez dos Canais Corticais Pré-Definidos:} Os canais analíticos do CHO (D-DOG e Laguerre-Gauss) possuem perfis matemáticos estáticos que não conseguem se adaptar à supressão anisotrópica de ruído realizada pelas redes convolucionais profundas.
\end{enumerate}

Essa falha impôs a necessidade de desenvolver uma nova geração de observadores computacionais não lineares baseados em inteligência artificial: os modelos DLMO.

\section{Metodologia de Simuladores Antropomórficos Híbridos}
\label{sec:simuladores_hibridos}

\subsection{Aquisição Real com Inserção Computacional de Lesões}
\label{subsec:insercao_lesoes}
Para avaliar tomógrafos com rigor metrológico sem expor pacientes a doses de pesquisa, consolidou-se a metodologia dos simuladores antropomórficos híbridos.

Adquire-se a varredura volumétrica de um phantom antropomórfico físico (ex: tórax ou abdome) sob diferentes níveis de dose e parâmetros de reconstrução. Em seguida, modelos tridimensionais de lesões patológicas (esferas sólidas, nódulos com bordas espiculadas ou lesões subsólidas em vidro fosco) são computacionalmente inseridos na matriz de imagem bruta através da convolução tridimensional com a PSF local:
\begin{equation}
  I_{\text{híbrida}}(x, y, z) = I_{\text{fundo}}(x, y, z) + \left[ s_{\text{lesão}}(x, y, z) * \text{PSF}_{3D}(x, y, z) \right]
  \label{eq:convolucao_hibrida}
\end{equation}

Essa abordagem gera milhares de pares de imagens estocasticamente independentes com \emph{ground truth} rigorosamente controlado, viabilizando experimentos 2AFC em larga escala.

\subsection{Detrending Polinomial Bidimensional de 2ª Ordem}
\label{subsec:detrending_2d}
Ao extrair regiões de interesse (ROIs) em parênquimas anatômicos (como o fígado ou pulmão do phantom), a presença de gradientes macroscópicos de atenuação contamina as baixas frequências do $NPS$. Aplica-se o detrending polinomial de 2ª ordem:
\begin{equation}
  P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy
  \label{eq:polinomio_detrending}
\end{equation}
onde os coeficientes $a_k$ são determinados por regressão linear por mínimos quadrados ordinários. O ruído puro é obtido por $\delta I(x, y) = I(x, y) - P_2(x, y)$ (\cref{fig:dlr_non_linear}, Painel C).

\subsection{Estimativa de Incerteza por Bootstrap Não-Paramétrico}
\label{subsec:bootstrap_incerteza}
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

\subsection{Limitações dos Modelos Clássicos e a Abordagem por Redes Profundas}
\label{subsec:dlmo_motivacao}
Para modelar o desempenho de radiologistas sob reconstruções não lineares DLR em anatomias complexas, a física médica desenvolveu os Observadores de Modelo por Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), que emulam a coordenação foveal-periférica humana.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura Neural do DLMO]{Arquitetura Neural do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer) e Calibração Perceptual.}
  \label{fig:dlmo_arch}
\end{figure}

\subsection{Arquitetura Baseada em Vision Transformers (ViT)}
\label{subsec:vit_arquitetura}
O DLMO utiliza arquiteturas neurais avançadas baseadas em \emph{Vision Transformers} (ViT) com mecanismos de Auto-Atenção Multi-Cabeça (MHSA), conforme esquematizado no \cref{fig:dlmo_arch} \cite{dosovitskiy2020, zhou2021, schilder2026}.

A imagem tomográfica $\mathbf{x} \in \mathbb{R}^{H \times W \times C}$ é particionada em $N_p = \frac{HW}{P^2}$ blocos bidimensionais não-sobrepostos (\emph{patches}) $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 C)}$ com dimensão $P \times P$ (ex: $8 \times 8$ pixels). Cada bloco é linearmente projetado para uma dimensão latente contínua $D_{\text{model}}$ via matriz $\mathbf{E}$:
\begin{equation}
  \mathbf{z}_0 = \left[ \mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \mathbf{x}_p^2 \mathbf{E}; \, \dots; \, \mathbf{x}_p^{N_p} \mathbf{E} \right] + \mathbf{E}_{\text{pos}}
  \label{eq:vit_embedding}
\end{equation}
onde $\mathbf{x}_{\text{class}}$ é o token de classificação diagnóstica e $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N_p + 1) \times D_{\text{model}}}$ adiciona a codificação posicional bidimensional aprendida.

\subsection{Mecanismo de Auto-Atenção Multi-Cabeça (MHSA)}
\label{subsec:mhsa_mecanismo}
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

\subsection{Cálculo do Índice de Detectabilidade $d'_{\text{DL}}$}
\label{subsec:dprime_dl_calculo}
A saída não linear da rede $t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$ permite calcular o índice de detectabilidade do modelo profundo:
\begin{equation}
  d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}
  \label{eq:dprime_dl}
\end{equation}

Para que o DLMO atue como um instrumento metrológico fiel da percepção médica, o treinamento da rede neural é calibrado diretamente contra o desempenho de radiologistas através de perdas perceptuais multitarefa e validação cruzada LOSO.

\section{Calibração Perceptual e Transferibilidade Inter-Scanners}
\label{sec:loso}

\subsection{Função de Perda Multitarefa com Alinhamento Perceptual}
\label{subsec:perceptual_loss}
O treinamento do DLMO incorpora uma função de perda de otimização multitarefa que penaliza simultaneamente o erro de classificação e os desvios em relação à detectabilidade medida em experimentos 2AFC com radiologistas \cite{zhou2021}:
\begin{equation}
  \mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{BCE}}(y, \hat{y}) + \lambda \, \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2
  \label{eq:perceptual_loss}
\end{equation}
onde $\mathcal{L}_{\text{BCE}}$ é a entropia cruzada binária clássica e $\lambda$ calibra o alinhamento perceptual.

\subsection{Validação Cruzada Leave-One-Scanner-Out (LOSO)}
\label{subsec:loso_validacao}
A robustez inter-fabricantes é validada pelo esquema \emph{Leave-One-Scanner-Out} (LOSO): em um conjunto de $K$ tomógrafos distintos (GE, Siemens, Canon e Philips), treina-se o observador com dados de $K - 1$ equipamentos e testa-se cegamente no tomógrafo omitido, garantindo coeficientes de correlação $r > 0{,}95$ em todas as dobras.

Enquanto as reconstruções por IA aprimoram tomógrafos convencionais, a maior inovação física nos detectores de radiação é a Tomografia por Contagem de Fótons (PCCT), analisada a seguir.

\section{Física da Tomografia por Contagem de Fótons (PCCT)}
\label{sec:pcct_fisica}

\subsection{Limitações Físicas dos Detectores EICT}
\label{subsec:eict_limitacoes}
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

\subsection{Mecânica Quântica dos Semicondutores de Conversão Direta (CdTe/CZT)}
\label{subsec:semicondutores_pcct}
Conforme sintetizado na \cref{tab:eict_vs_pcct}, os detectores PCCT utilizam cristais semicondutores de conversão direta (Telureto de Cádmio --- CdTe ou CZT, espessura de $1{,}5\text{ a }3{,}0\text{ mm}$ sob alta tensão de $-800\text{ a }-1000\text{ V}$) \cite{willemink2018, rajendran2021, mccollough2026, pimenta2025, pimenta2026}.

A absorção de cada fóton gera instantaneamente pares elétron-lacuna que migram para os ânodos pixelados, gerando um pulso de tensão estritamente proporcional à energia do fóton:
\begin{equation}
  V_{\text{pulso}} \propto Q = \frac{E_{\text{fóton}}}{W_{\text{ionização}}}
  \label{eq:vpulso}
\end{equation}
com $W_{\text{ionização}} \approx 4{,}43\text{ eV}$ para o CdTe (frente a mais de $30\text{ eV}$ em cintiladores convencionais).

\subsection{Síntese de Imagens Monoenergéticas Virtuais ($VMI$)}
\label{subsec:vmi_sintese}
Ao separar os pulsos em múltiplos canais de energia através de comparadores ultra-rápidos, o sistema sintetiza Imagens Monoenergéticas Virtuais ($VMI$) em qualquer nível de energia (de 40 a 140 keV):
\begin{equation}
  I_{\text{VMI}}(x, y; E_0) = a_1(x, y) \cdot f_{\text{foto}}(E_0) + a_2(x, y) \cdot f_{\text{Compton}}(E_0)
  \label{eq:vmi_formula}
\end{equation}

Em baixas energias ($40\text{ a }50\text{ keV}$), maximiza-se o contraste fotoelétrico do iodo ($K\text{-edge} = 33{,}2\text{ keV}$), aumentando expressivamente a detectabilidade de lesões vasculares sem a contaminação por ruído eletrônico observada nos tomógrafos EICT.

A diversidade de parâmetros operacionais em EICT e PCCT (kVp, mA, tempo, pitch, algoritmo DLR e energia de VMI) gera um espaço combinatório imenso. A resposta metrológica para encontrar o protocolo clínico ótimo é a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional.

\section{Otimização Multiobjetivo e Fronteira de Pareto 3D}
\label{sec:pareto_otimizacao}

\subsection{O Desafio Clínico da Otimização em Três Dimensões ($D, T, W$)}
\label{subsec:desafio_multiobjetivo}
Na rotina clínica de emergências e centros de trauma, a otimização não pode considerar apenas a dose e a detectabilidade pontual: o tempo operacional total ($T$) é uma variável crítica para a sobrevida do paciente, e a qualidade deve ser garantida para toda a coorte populacional através do índice ponderado $\text{SSW-}d'$. A otimização de protocolos tomográficos é formulada como um problema de minimização vetorial multiobjetivo \cite{deb2002, hwang1981, oostveen2021}:
\begin{equation}
  \min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} \overline{\text{SSDE}}(\mathbf{p}) \\ T(\mathbf{p}) \\ -\text{SSW-}d'(\mathbf{p}) \end{pmatrix}
  \label{eq:multiobjetivo_pareto}
\end{equation}
onde o vetor de decisão $\mathbf{p} = (\text{kVp}, \text{mA}, t_{\text{rot}}, \text{pitch}, \text{corte}, \text{kernel}, \text{nível DLR}, E_{\text{VMI}})^T$ pertence ao espaço viável $\Omega$, sujeito às restrições:
\begin{itemize}
  \item $\overline{\text{SSDE}}(\mathbf{p}) \le \text{DRL}$ (restrição de radioproteção por Níveis de Referência Diagnóstica ajustados por tamanho);
  \item $T(\mathbf{p}) \le T_{\text{máx}}$ (restrição de tempo para evitar artefatos de movimento corporal);
  \item $W(\mathbf{p}) = \text{SSW-}d'(\mathbf{p}) \ge d'_{\text{mín}}$ (restrição diagnóstica para garantir a acurácia médica na população).
\end{itemize}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto.}
  \label{fig:pareto_3d}
\end{figure}

\subsection{Análise dos Gráficos da Figura 5.2 em Cenário Clínico Hipotético}
\label{subsec:analise_fig5}
Para compreender a otimização multiobjetivo em uma \textbf{situação clínica hipotética}, considere a admissão de emergência de um paciente politraumatizado grave após acidente automobilístico, apresentando taquipneia severa e suspeita de hemorragia abdominal ativa. A \cref{fig:pareto_3d} ilustra a tomada de decisão:

\begin{itemize}
  \item \textbf{Painel (A) --- Compromisso Clínico Dose vs. Detectabilidade:} A curva verde contínua delimita a Fronteira de Pareto de soluções não-dominadas. Três soluções operacionais são identificadas: $P_1$ (ponto azul, protocolo pediátrico/preventivo de ultrabaixa dose), $P_2$ (ponto laranja, exame ambulatorial de rotina) e $P_3$ (ponto vermelho, protocolo de alta dose e máxima detectabilidade para emergência). Os pontos cinzas dispersos representam protocolos hospitalares descalibrados que utilizam doses excessivas para a qualidade entregue;

  \item \textbf{Painel (B) --- Superfície de Pareto Tridimensional $(D, T, -W)$:} No paciente de politrauma com taquipneia, o tempo de varredura não pode exceder 3 segundos para evitar artefatos de respiração descontrolada. A variedade 3D de Pareto permite ao software do tomógrafo selecionar instantaneamente a combinação de alta rotação ($T = 2\text{ s}$) e corrente adaptativa mA para atingir a detectabilidade necessária ($W = \text{SSW-}d' = 3{,}2$), viabilizando o diagnóstico de hemorragia antes da cirurgia imediata.
\end{itemize}

\subsection{Resolução Numérica via Algoritmo Genético NSGA-II e Tomada de Decisão TOPSIS}
\label{subsec:nsga2_topsis}
O mapeamento da superfície de Pareto é executado numericamente através do algoritmo genético \emph{Non-dominated Sorting Genetic Algorithm II} (NSGA-II) com população de 100 indivíduos e 200 gerações \cite{deb2002}. A seleção do ponto operacional de compromisso clínico ótimo na variedade 3D é realizada pela técnica multicritério TOPSIS (\emph{Technique for Order Preference by Similarity to Ideal Solution}), normalizando os pesos das três funções objetivo de acordo com a indicação médica \cite{hwang1981}.

Com os modelos teóricos consolidados, o próximo capítulo descreve a arquitetura modular do software desenvolvido e os aspectos éticos de pesquisa com seres humanos.

% ------------------------------------------------------------------------------
% CAPÍTULO 6: ARQUITETURA DE SOFTWARE E METROLOGIA
% ------------------------------------------------------------------------------
\chapter{Arquitetura de Software e Metrologia}
\label{chap:arquitetura_metrologia}

Este capítulo detalha a infraestrutura computacional modular em Python desenvolvida para a execução automatizada do pipeline de metrologia tomográfica. Apresentam-se a padronização das aquisições segundo o relatório AAPM TG-233, o módulo de cálculo integrado do SSW-$d'$ e as salvaguardas bioéticas (CEP/CONEP) para os testes com radiologistas.

\section{Arquitetura Modular do Software de Metrologia}
\label{sec:software_arch}

\subsection{Visão Geral do Pipeline GDRFM-IFUSP}
\label{subsec:visao_geral_pipeline}
A aplicação prática dos modelos matemáticos depende de uma arquitetura de software reproduzível e robusta, capaz de processar exames DICOM de forma automatizada.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow6_software_pipeline.png}
  \caption[Arquitetura Modular do Software de Metrologia]{Arquitetura Modular do Software de Metrologia em Tomografia Computadorizada (Pipeline Integrado GDRFM-IFUSP).}
  \label{fig:software_flow}
\end{figure}

\subsection{Descrição Detalhada dos Módulos de Processamento}
\label{subsec:modulos_detalhados}
O software organiza-se em cinco módulos encadeados (\cref{fig:software_flow}) \cite{choopani2023}:
\begin{itemize}
  \item \textbf{Módulo 1 (Parser DICOM):} Realiza a leitura e validação dos metadados de aquisição (kVp, mA, tempo, pitch, espessura, kernel e nível DLR), calculando o diâmetro equivalente em água ($D_w$) da seção anatômica;
  \item \textbf{Módulo 2 (Segmentação Automática):} Localiza as coordenadas dos insertos de calibração via Transformada de Hough e extrai $M \ge 100$ ROIs anatômicas independentes;
  \item \textbf{Módulo 3A (Resolução Espacial):} Calcula $\text{ESF}(r) \to \text{LSF}(r) \to TTF(f)$ e extrai os descritores $f_{50}$ e $f_{10}$;
  \item \textbf{Módulo 3B (Textura e Ruído):} Executa o detrending polinomial 2D $P_2(x, y)$, janelamento Hanning e FFT2, gerando $NPS(u, v)$ e a curva radial $NPS(f)$;
  \item \textbf{Módulo 4 (Observadores de Modelo e SSW-$d'$):} Computa a detectabilidade pelos modelos lineares (NPWE e CHO com canais corticais), pelo observador profundo DLMO (Vision Transformers) e sintetiza o índice populacional ponderado $\text{SSW-}d'$ através da matriz de diâmetros $D_{w,i}$ e pesos clínicos $\Omega_j$;
  \item \textbf{Módulo 5 (Incerteza, SSDE e Otimização de Pareto):} Executa a reamostragem Bootstrap ($B = 2000$), calcula a Figura de Mérito Populacional $\text{FOM}_{\text{SSW}} = (\text{SSW-}d')^2/\overline{\text{SSDE}}$ e executa o algoritmo genético NSGA-II com ranqueamento TOPSIS.
\end{itemize}

\section{Protocolo Metrológico Padronizado AAPM TG-233}
\label{sec:protocolo_tg233}

\subsection{Parâmetros de Aquisição e Geometria do Phantom}
\label{subsec:parametros_tg233}
A padronização metrológica rigorosa assegura que as medições de detectabilidade sejam diretamente reprodutíveis em qualquer centro de pesquisa internacional. As aquisições tomográficas seguem as diretrizes da AAPM \cite{aapm_tg233_2019}:
\begin{itemize}
  \item Matriz de $512 \times 512$ pixels com FOV ajustado ao diâmetro do phantom ($200\text{ a }350\text{ mm}$);
  \item Espessuras de corte de $0{,}5\text{ a }1{,}0\text{ mm}$ (alta resolução) e $2{,}5\text{ a }5{,}0\text{ mm}$ (rotina);
  \item Tensões de 80, 100, 120 e 140 kVp, cobrindo doses $\text{CTDI}_{\text{vol}}$ de $0{,}5\text{ a }15\text{ mGy}$;
  \item Lesões esféricas com diâmetros de 3, 5, 8 e 10 mm e contrastes clínicos de $-600\text{ HU}$ (nódulo subsólido), $+100\text{ HU}$ (nódulo sólido) e $+30\text{ HU}$ (lesão hepática hipoatenuante).
\end{itemize}

\section{Aspectos Bioéticos e Regulatórios na Pesquisa com Radiologistas}
\label{sec:bioetica}

\subsection{Conformidade Ética e Termo de Consentimento}
\label{subsec:cep_conep}
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

\subsection{Da Falência das Métricas Lineares à Consolidação do Paradigma TBIQ}
\label{subsec:sintese_tbiq}
A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram uma profunda transformação metodológica nas últimas décadas. Esta monografia investigou sistematicamente a transição dos modelos analíticos clássicos para as formulações perceptuais contemporâneas baseadas em inteligência artificial e detectores de contagem de fótons.

O ponto de partida residiu no reconhecimento da **falência das métricas escalares clássicas** ($SNR$, $CNR$, desvio padrão $\sigma_{\text{HU}}$ e $MTF$ global) frente aos algoritmos não lineares de reconstrução iterativa (HIR, MBIR) e, fundamentalmente, de aprendizado profundo (DLR). Demonstrou-se formalmente que as premissas de linearidade estrita do sistema, isoplanatismo espacial e estacionariedade do ruído no sentido amplo (WSS) foram rompidas. Sob DLR, a redução do desvio padrão em Unidades Hounsfield não decorre de maior contagem física de fótons, mas de operações adaptativas não lineares que suavizam o ruído alterando sua distribuição de frequência (gerando o aspecto textural ceroso ou \emph{plastic look}). Consequentemente, lesões patológicas de baixo contraste podem ser atenuadas e suprimidas da imagem mesmo quando os valores numéricos de $SNR$ e $CNR$ aparentam excelente qualidade.

Como resposta científica a esse desafio, consolidou-se o paradigma da **Qualidade de Imagem Baseada em Tarefa (TBIQ)**, ancorado na Teoria de Detecção de Sinais (SDT). Demonstrou-se que a qualidade de uma imagem médica é uma grandeza estritamente relacional, definida pelo desempenho de um observador ao executar uma tarefa clínica diagnóstica (identificação de nódulos, metástases ou fissuras ósseas). O **Índice de Detectabilidade ($d'$)** emergiu como a grandeza central unificadora, integrando com rigor matemático:
\begin{enumerate}
  \item A resposta de frequência espacial dependente do contraste local ($TTF(f)$ com o descritor $f_{50}$);
  \item A densidade espectral e correlação espacial do ruído ($NPS(f)$ com a frequência de pico $f_{\text{peak}}$);
  \item A geometria e perfil radiológico da patologia ($W_{\text{task}}(f)$ via funções de Bessel);
  \item A sensibilidade ao contraste do olho humano ($E(f)$) ou a capacidade discriminativa de redes neurais corticais.
\end{enumerate}

\subsection{Da Modelagem Analítica aos Modelos Profundos, Extensão SSW-$d'$ e Tomografia PCCT}
\label{subsec:sintese_dlmo_pcct}
Na investigação dos **observadores de modelo lineares**, deduziu-se o limite teórico superior estabelecido pelo Observador Ideal Bayesiano e pelo Observador de Hotelling ($d'_{\text{HO}}$), demonstrando o mecanismo de pré-branqueamento do ruído via matriz de autocovariância inversa $\mathbf{K}^{-1}$. Em seguida, derivou-se a integral contínua do modelo antropomórfico Sem Pré-Branqueamento com Filtro Ocular (NPWE), evidenciando sua alta precisão em simuladores homogêneos de calibração e seu subsequente colapso em fundos anatômicos reais. Para contornar a barreira dimensional da covariância em matrizes clínicas, explorou-se a formulação do Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor, validado estatisticamente contra painéis de radiologistas através de modelos de ANOVA com efeitos aleatórios cruzados (MRMC DBM/HOR).

Para superar a limitação das medições pontuais estáticas em simuladores únicos de 20 cm, formalizou-se o **Índice de Detectabilidade Ponderado pelo Tamanho do Paciente e Tarefa (SSW-$d'$)**, que integra múltiplos diâmetros equivalentes em água ($D_w$) com ponderações de relevância clínica de contraste ($\Omega_j$). Demonstrou-se como o SSW-$d'$ se acopla à dosimetria personalizada por tamanho ($\text{SSDE}$) através da Figura de Mérito Populacional $\text{FOM}_{\text{SSW}} = (\text{SSW-}d')^2/\overline{\text{SSDE}}$, estabelecendo uma métrica robusta de eficiência radiológica para auditoria hospitalar em coortes heterogêneas.

Ao analisar o **estado da arte**, investigaram-se os Observadores Baseados em Aprendizado Profundo (DLMO), construídos sobre arquiteturas *Vision Transformers* (ViT) com auto-atenção multi-cabeça. Demonstrou-se que o mecanismo de atenção mimetiza a coordenação visual foveal-periférica humana, superando a dispersão dos modelos lineares ($r = 0{,}68$) e alcançando concordância quase perfeita com os radiologistas ($r = 0{,}98$). Paralelamente, detalhou-se a biofísica da **Tomografia por Contagem de Fótons (PCCT)**, cujos detectores semicondutores de conversão direta (CdTe/CZT) eliminam o ruído eletrônico e viabilizam Imagens Monoenergéticas Virtuais ($VMI$) em baixos keV com ganho expressivo de contraste fotoelétrico.

Por fim, estruturou-se a **Otimização Multiobjetivo Não Linear** através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade diagnóstica ($W$). Essa formulação viabiliza a seleção automatizada e personalizada de protocolos clínicos através do algoritmo genético NSGA-II e do método multicritério TOPSIS.

\section{Impacto Clínico, Operacional e Regulatório}
\label{sec:impacto_pratico}

\subsection{Radioproteção Personalizada e Otimização do Princípio ALARA}
\label{subsec:impacto_alara}
Os resultados e metodologias estruturados nesta monografia oferecem contribuições imediatas para a prática clínica e para a gestão hospitalar:
\begin{itemize}
  \item \textbf{Radioproteção Efetiva e Otimização do Princípio ALARA:} A utilização do índice $d'$ e do índice populacional SSW-$d'$ fornece uma comprovação física e matemática inequívoca de que reduções de até 50\% a 60\% na dose de radiação em protocolos pediátricos e de rastreio de câncer de pulmão podem ser executadas com total segurança diagnóstica, eliminando a dependência de avaliações visuais puramente subjetivas;

  \item \textbf{Harmonização Inter-Fabricantes em Parques Tecnológicos Complexos:} Grandes centros hospitalares operam simultaneamente tomógrafos de múltiplos fornecedores (GE, Siemens, Canon, Philips) com diferentes gerações de algoritmos DLR. A metodologia de simuladores antropomórficos híbridos com observadores DLMO calibrados via validação cruzada LOSO permite equalizar o desempenho diagnóstico entre todos os equipamentos, garantindo que um paciente receba a mesma acurácia diagnóstica independentemente do tomógrafo utilizado;

  \item \textbf{Conformidade Regulatória e Auditoria de Qualidade:} O pipeline computacional automatizado permite aos serviços de física médica atender com rigor às exigências da ANVISA (RDC 611/2022 e IN 93/2021), aos relatórios da AAPM (TG-233 e Report 204/220) e aos programas internacionais de auditoria da Agência Internacional de Energia Atômica (IAEA 5-Star), automatizando a emissão de laudos de controle de qualidade e a vigilância contínua de doses e detectabilidade.
\end{itemize}

\section{Perspectivas Futuras e Direções de Pesquisa}
\label{sec:perspectivas_futuras}

A consolidação da física médica na era dos detectores de contagem de fótons e da inteligência artificial generativa abre horizontes promissores para desenvolvimentos futuros:

\begin{enumerate}[label=\textbf{\arabic*.}]
  \item \textbf{Extensão do TBIQ e SSW-$d'$ para Aquisições Dinâmicas e 4D:}
  A metodologia baseada em tarefa foi majoritariamente desenvolvida para cortes anatômicos tridimensionais estáticos. Uma fronteira imediata reside na extensão do índice de detectabilidade para aquisições tomográficas com resolução temporal (4D), como a angiotomografia coronariana com sincronização cardíaca (\emph{ECG-gating}) e a tomografia de perfusão cerebral em acidentes vasculares cerebrais (AVC). Nesses cenários, a modelagem matemática do observador deverá incorporar a Função de Transferência Temporal ($TTF_t(f_t)$) e a correlação espaço-temporal do ruído ($NPS(u, v, f_t)$);

  \item \textbf{Modelos Fundacionais e IA Generativa na Avaliação da Percepção:}
  A evolução dos modelos de linguagem e visão multimodal (\emph{Vision-Language Models} e \emph{Foundation Models} em saúde) viabiliza o desenvolvimento de observadores computacionais universais capazes não apenas de fornecer uma pontuação escalar $d'$, mas de justificar textualmente a decisão diagnóstica, apontando regiões de incerteza anatômica e mimetizando a redação de laudos radiológicos estruturados;

  \item \textbf{Gêmeos Digitais e Simuladores In Silico com Injeção de Contraste Fisiológico:}
  O desenvolvimento de plataformas de ensaios clínicos virtuais (\emph{Virtual Imaging Clinical Trials} --- VICT) baseadas em fantomas computacionais biomecânicos e modelos computacionais de dinâmica de fluidos para perfusão de contraste permitirá simular populações inteiras de pacientes com patologias específicas, avaliando novos tomógrafos e protocolos antes de sua introdução clínica;

  \item \textbf{Disseminação Open-Source de Ferramentas Metrológicas Hospitalares:}
  Para democratizar a metrologia baseada em tarefa no Sistema Único de Saúde (SUS) e em centros de radiologia com recursos limitados, é essencial disponibilizar ferramentas computacionais abertas, modulares e validadas, integrando o pipeline AAPM TG-233, o SSW-$d'$ e os observadores DLMO aos sistemas PACS e RIS hospitalares.
\end{enumerate}



% ==============================================================================
% ELEMENTOS PÓS-TEXTUAIS (REFERÊNCIAS BIBLIOGRÁFICAS NUMÉRICAS ABNT)
% ==============================================================================
\begin{thebibliography}{99}
\addcontentsline{toc}{chapter}{Referências}

\bibitem{bushberg2020}
BUSHBERG, J. T.; SEIBERT, J. A.; LEIDHOLDT, E. M.; BOONE, J. M. \textbf{The Essential Physics of Medical Imaging}. 4. ed. Philadelphia: Lippincott Williams \& Wilkins, 2020. 1048 p.

\bibitem{attix1986}
ATTIX, F. H. \textbf{Introduction to Radiological Physics and Radiation Dosimetry}. New York: John Wiley \& Sons, 1986. 607 p.

\bibitem{seeram2015}
SEERAM, E. \textbf{Computed Tomography: Physical Principles, Clinical Applications, and Quality Control}. 4. ed. St. Louis: Elsevier Health Sciences, 2015. 560 p.

\bibitem{icrp103_2007}
INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION (ICRP). \textbf{The 2007 Recommendations of the International Commission on Radiological Protection}. ICRP Publication 103. Annals of the ICRP, v. 37, n. 2-4, p. 1--332, 2007.

\bibitem{mccollough2026}
MCCOLLOUGH, C. H. et al. Radiation dose in computed tomography: technological advances and clinical optimization over two decades. \textbf{Radiology}, v. 318, n. 2, p. e251200, 2026.

\bibitem{anvisa_rdc611_2022}
AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Resolução da Diretoria Colegiada - RDC nº 611, de 9 de março de 2022}: Estabelece os requisitos sanitários para a organização e o funcionamento de serviços de radiologia diagnóstica ou intervencionista. Brasília: ANVISA, 2022.

\bibitem{anvisa_in93_2021}
AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Instrução Normativa nº 93, de 27 de maio de 2021}: Estabelece os requisitos sanitários para a garantia da qualidade e da segurança em sistemas de tomografia computadorizada médica. Brasília: ANVISA, 2021.

\bibitem{racine2020}
RACINE, D. et al. Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. \textbf{Physics in Medicine \& Biology}, v. 65, n. 18, p. 185011, 2020.

\bibitem{debbiche2024}
DEBBICHE, I. et al. Task-based image quality assessment of deep learning image reconstruction in abdominal CT: a multi-reader phantom study. \textbf{European Radiology}, v. 34, n. 5, p. 3120--3132, 2024.

\bibitem{greffier2026}
GREFFIER, J. et al. Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. \textbf{Diagnostic and Interventional Imaging}, v. 107, n. 1, p. 1016--1025, 2026.

\bibitem{toia2023}
TOIA, G. V. et al. Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. \textbf{European Radiology}, v. 33, p. 4310--4322, 2023.

\bibitem{solomon2020}
SOLOMON, J. et al. Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. \textbf{Medical Physics}, v. 47, n. 8, p. 3412--3425, 2020.

\bibitem{aapm_tg233_2019}
AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., Medical Physics, v. 46, n. 11, p. e735--e756, 2019).

\bibitem{icru54_1996}
INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). \textbf{Medical Imaging - The Assessment of Image Quality}. ICRU Report 54. Bethesda, MD: ICRU, 1996. 88 p.

\bibitem{peterson1954}
PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. \textbf{Transactions of the IRE Professional Group on Information Theory}, v. 4, n. 4, p. 171--212, 1954.

\bibitem{lusted1968}
LUSTED, L. B. \textbf{Introduction to Medical Decision Making}. Springfield, IL: Charles C. Thomas, 1968. 271 p.

\bibitem{metz1986}
METZ, C. E. ROC methodology in radiologic imaging. \textbf{Investigative Radiology}, v. 21, n. 9, p. 720--733, 1986.

\bibitem{barrett_myers_2004}
BARRETT, H. H.; MYERS, K. J. \textbf{Foundations of Image Science}. Hoboken, NJ: John Wiley \& Sons, 2004. 1584 p.

\bibitem{rose1948}
ROSE, A. The sensitivity performance of the human eye on an absolute scale. \textbf{Journal of the Optical Society of America}, v. 38, n. 2, p. 196--208, 1948.

\bibitem{burgess1999}
BURGESS, A. E. The Rose model, revisited. \textbf{Journal of the Optical Society of America A}, v. 16, n. 3, p. 633--646, 1999.

\bibitem{wagner1979}
WAGNER, R. F.; BROWN, D. G.; METZ, C. E. Unified analysis of medical imaging systems. \textbf{Medical Physics}, v. 6, n. 2, p. 83--94, 1979.

\bibitem{burgess1994}
BURGESS, A. E. Statistically defined backgrounds in medical imaging. \textbf{Journal of the Optical Society of America A}, v. 11, n. 4, p. 1237--1242, 1994.

\bibitem{eckstein2000}
ECKSTEIN, M. P. et al. Model observers for visual search tasks in medical imaging. \textbf{Physics in Medicine \& Biology}, v. 45, n. 8, p. 2375--2388, 2000.

\bibitem{myers_barrett_1987}
MYERS, K. J.; BARRETT, H. H. Addition of a channel mechanism to the ideal-observer model. \textbf{Journal of the Optical Society of America A}, v. 4, n. 12, p. 2447--2457, 1987.

\bibitem{gallas2003}
GALLAS, B. D.; BARRETT, H. H. Validating the use of channels to estimate the ideal linear observer. \textbf{Journal of the Optical Society of America A}, v. 20, n. 9, p. 1725--1738, 2003.

\bibitem{aapm_report204}
AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Size-Specific Dose Estimates (SSDE) in Pediatric and Adult Body CT Examinations}. AAPM Report No. 204. College Park, MD: AAPM, 2011. 68 p.

\bibitem{fitton2026}
FITTON, I.; GREFFIER, J.; DABLI, D.; VAN NGOC TY, C. Size-specific weighted detectability index for computed tomography image characterization. \textbf{Medical Physics}, v. 53, n. 9, p. e17420, 2026.

\bibitem{goppel2021}
GOPPEL, M. et al. Task-based image quality assessment in CT: Size-specific optimization of radiation dose and lesion contrast. \textbf{European Radiology}, v. 31, p. 5812--5822, 2021.

\bibitem{pimenta2026}
PIMENTA, E. F. \textbf{Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax}. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.

\bibitem{dorfman1992}
DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E. Receiver operating characteristic rating analysis: generalization to the population of readers and cases with the jackknife method. \textbf{Investigative Radiology}, v. 27, n. 9, p. 723--731, 1992.

\bibitem{obuchowski1995}
OBUCHOWSKI, N. A.; ROCKETTE, H. E. Hypothesis testing of diagnostic accuracy for multiple readers and multiple tests: an ANOVA approach with dependent observations. \textbf{Communications in Statistics - Simulation and Computation}, v. 24, n. 2, p. 285--308, 1995.

\bibitem{hillis2011}
HILLIS, S. L.; OBUCHOWSKI, N. A.; BERBAUM, K. S. Multi-reader multi-case ROC analysis: an updated review of methods and software. \textbf{Academic Radiology}, v. 18, n. 7, p. 842--856, 2011.

\bibitem{racine2021}
RACINE, D. et al. Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. \textbf{Medical Physics}, v. 48, n. 6, p. 2890--2901, 2021.

\bibitem{dosovitskiy2020}
DOSOVITSKIY, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: \textbf{International Conference on Learning Representations (ICLR)}, 2021. p. 1--21.

\bibitem{zhou2021}
ZHOU, W. et al. Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. \textbf{IEEE Transactions on Medical Imaging}, v. 40, n. 9, p. 2350--2362, 2021.

\bibitem{schilder2026}
SCHILDER, C. M. et al. Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. \textbf{La Rivista del Nuovo Cimento}, v. 49, n. 3, p. 145--210, 2026.

\bibitem{willemink2018}
WILLEMINK, M. J. et al. Photon-counting CT: technical principles and clinical prospects. \textbf{Radiology}, v. 289, n. 2, p. 293--312, 2018.

\bibitem{rajendran2021}
RAJENDRAN, K. et al. First clinical photon-counting detector CT system: technical evaluation. \textbf{Radiology}, v. 303, n. 1, p. 130--138, 2021.

\bibitem{pimenta2025}
PIMENTA, E. F.; COSTA, P. R. Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. \textbf{Medical Physics}, v. 52, n. 4, p. 2150--2165, 2025.

\bibitem{deb2002}
DEB, K. et al. A fast and elitist multiobjective genetic algorithm: NSGA-II. \textbf{IEEE Transactions on Evolutionary Computation}, v. 6, n. 2, p. 182--197, 2002.

\bibitem{hwang1981}
HWANG, C. L.; YOON, K. \textbf{Multiple Attribute Decision Making: Methods and Applications}. Berlin: Springer-Verlag, 1981. 259 p.

\bibitem{oostveen2021}
OOSTVEEN, L. J. et al. Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. \textbf{European Radiology}, v. 31, p. 7412--7421, 2021.

\bibitem{choopani2023}
CHOOPANI, R. et al. Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. \textbf{Physics in Medicine \& Biology}, v. 68, n. 14, p. 145002, 2023.

\bibitem{iaea_5star_2026}
INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA). Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. \textbf{European Journal of Radiology}, v. 184, p. 113133, 2026.

\end{thebibliography}

\end{document}
"""

with open(os.path.join(output_dir, "main.tex"), "w", encoding="utf-8") as f:
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
