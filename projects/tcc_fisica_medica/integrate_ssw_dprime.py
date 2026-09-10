# -*- coding: utf-8 -*-
import os
import zipfile
import subprocess

# Full text based 100% on the user's provided LaTeX text, enriched seamlessly with the SSW-d' additions.

latex_code = r'''\documentclass[
  12pt,
  a4paper,
  oneside
]{report}

\pdfsuppresswarningpagegroup=1

% ==============================================================================
% PACOTES ESSENCIAIS E CONFIGURAÇÃO TIPOGRÁFICA ABNT
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

% Matemática Avançada, Símbolos Físicos e Fontes
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{bm}
\usepackage{mathrsfs}

% Tipografia e Espaçamento ABNT (1,5 entre linhas e recuo de parágrafo de 1,5 cm)
\usepackage{lmodern}
\usepackage{setspace}
\onehalfspacing
\usepackage{indentfirst}
\setlength{\parindent}{1.5cm}

% Tolerância a quebras de linha e hifenação para evitar qualquer Overfull \hbox
\emergencystretch 3em
\hyphenation{To-mo-gra-fia Con-ta-gem Fó-tons Non-Pre-whi-te-ning Ob-ser-va-dor Clás-si-co Es-tru-tu-ral Re-cons-tru-ção Mul-ti-ob-je-ti-vo Di-ag-nós-ti-co Psi-co-fí-si-co An-tro-po-mór-fi-co Me-to-do-lo-gia Re-sul-ta-dos Dis-cus-são Bio-mé-di-ca Con-ti-nui-da-de De-tec-ta-bi-li-da-de He-te-ro-ge-nei-da-de Es-ta-cio-na-rie-da-de}

% Cores e Tabelas
\usepackage[table,xcdraw]{xcolor}
\definecolor{darkblue}{rgb}{0.0, 0.18, 0.39}
\definecolor{linkblue}{rgb}{0.0, 0.22, 0.65}

% Figuras, Ilustrações e Tabelas
\usepackage{graphicx}
\graphicspath{{figuras/}{./}}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{ragged2e}
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

% Macro para Inclusão Robusta de Figuras
\newcommand{\incluirfigura}[3][width=0.95\textwidth]{%
  \includegraphics[#1]{#2}%
}

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
\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries\itshape}
  {\thesubsubsection}
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
\newcommand{\tcctitulo}{MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: UMA REVISÃO SISTEMÁTICA E MODELAGEM TEÓRICO-METROLÓGICA DA TEORIA DE DETECÇÃO DE SINAIS AO APRENDIZADO PROFUNDO}
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

  \vspace{3.0cm}

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
      \small\raggedright
      Trabalho de Conclusão de Curso (Monografia de Revisão Bibliográfica Sistemática e Modelagem Teórico-Metrológica) apresentado ao Instituto de Física e à Faculdade de Medicina da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física Médica.
      
      \vspace{0.5cm}
      Orientador: \tccorientador\\
      Área de Concentração: \tccarea
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
      \small\raggedright
      Monografia defendida e aprovada em \_\_ de \_\_\_\_\_\_\_\_ de 2026 pela Comissão Julgadora constituída pelos seguintes membros:
    \end{minipage}
  \end{flushright}

  \vspace{2.5cm}

  \rule{0.85\textwidth}{0.5pt}\\
  \tccorientador\ (Presidente / Orientador)\\
  Instituto de Física da Universidade de São Paulo -- IFUSP

  \vspace{1.2cm}

  \rule{0.85\textwidth}{0.5pt}\\
  Membro da Banca Examinadora 1\\
  Instituto de Radiologia do Hospital das Clínicas -- InRad-HCFMUSP

  \vspace{1.2cm}

  \rule{0.85\textwidth}{0.5pt}\\
  Membro da Banca Examinadora 2\\
  Instituto de Física da Universidade de São Paulo -- IFUSP
\end{center}
\clearpage

% 4. DEDICATÓRIA E AGRADECIMENTOS
\chapter*{Dedicatória}
\addcontentsline{toc}{chapter}{Dedicatória}
\vspace*{\fill}
\begin{flushright}
  \textit{DEPOIS EU PENSO.}
\end{flushright}
\clearpage

\chapter*{Agradecimentos}
\addcontentsline{toc}{chapter}{Agradecimentos}

Ao meu orientador, Prof. Dr. Paulo Roberto Costa, pela dedicação pedagógica e incentivo contínuo ao longo de todo a minha passagem pelo curso.

Aos docentes, pesquisadores e funcionários do Instituto de Física (IFUSP) e da Faculdade de Medicina (FMUSP) da Universidade de São Paulo, pela sólida formação interdisciplinar oferecida ao longo da graduação.

Aos colegas de curso, amigos e pesquisadores do Grupo de Dosimetria das Radiações e Física Médica (GDRFM) e do Centro de Investigação Translacional de Oncologia Experimental, pelo companheirismo e frutíferas trocas científicas.

À Universidade de São Paulo, pelo patrimônio acadêmico e compromisso inegociável com a ciência pública, gratuita e de excelência.
\clearpage

% 5. EPÍGRAFE
\chapter*{Epígrafe}
\addcontentsline{toc}{chapter}{Epígrafe}
\vspace*{\fill}
\begin{flushright}
  \textit{``An image is not good in itself; it is only good for a purpose.''}\\
  \vspace{0.3cm}
  --- Harrison H. Barrett \& Kyle J. Myers (\emph{Foundations of Image Science})
\end{flushright}
\clearpage

% 6. RESUMO
\chapter*{Resumo}
\addcontentsline{toc}{chapter}{Resumo}

A Tomografia Computadorizada desempenha um papel indispensável na medicina diagnóstica contemporânea, operando sob o compromisso físico entre a minimização da dose de radiação ionizante e a preservação da eficiência diagnóstica, princípio fundamental de otimização radiológica. Historicamente, a garantia da qualidade em tomografia baseou-se em grandezas escalares lineares, como a Relação Sinal-Ruído, a Relação Contraste-Ruído, o desvio padrão em Unidades Hounsfield e a Função de Transferência de Modulação, avaliadas em simuladores cilíndricos homogêneos. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares, com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo, rompeu com as premissas de linearidade, isoplanatismo espacial e estacionariedade no sentido amplo do sistema formador de imagens. Sob processamentos não lineares adaptativos, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais, comumente referidas como aspecto ceroso ou plastificado, que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa, fundamentado na Teoria de Detecção de Sinais, no qual a qualidade é formalmente definida pelo desempenho de um observador ao executar uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade. Esta monografia constitui uma revisão bibliográfica sistemática e modelagem teórico-metrológica da evolução dos observadores de modelo e das métricas baseadas em tarefa. A busca bibliográfica foi estruturada segundo o protocolo PRISMA 2020 em seis bases científicas internacionais, identificando 1.206 registros brutos, que após triagem rigorosa e aplicação de critérios de elegibilidade resultaram em um corpus analítico de 38 publicações fundamentais. Apresentam-se as deduções matemáticas partindo do Observador Ideal Bayesiano e de Hotelling, passando pelos modelos antropomórficos lineares com filtro ocular e canais corticais, o Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa (SSW-$d'$) acoplado à Estimativa de Dose Específica por Tamanho (SSDE), até as fronteiras contemporâneas em redes neurais profundas e Tomografia por Contagem de Fótons. Para fundamentar pedagogicamente as deduções, o trabalho incorpora modelagens numéricas sintéticas controladas codificadas originalmente pelo autor em Python, complementando cada dedução com discussões analíticas aprofundadas com exemplos sobre cenários clínicos reais, como o rastreamento de nódulos pulmonares sutis, metástases hepáticas hipoatenuantes, isquemia cerebral hiperaguda e angiotomografia coronariana.

\vspace{0.8cm}
\noindent Palavras-chave: Tomografia Computadorizada. Revisão Bibliográfica Sistemática. Protocolo PRISMA 2020. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Índice Ponderado por Tamanho (SSW-$d'$). Dose Específica por Tamanho (SSDE). Reconstrução por Aprendizado Profundo. Simulação Numérica em Python. Tomografia por Contagem de Fótons. Relatório AAPM TG-233.
\clearpage

% 7. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy, following the fundamental optimization principle of radiation protection. Historically, image quality assurance in computed tomography relied on linear scalar metrics, such as Signal-to-Noise Ratio, Contrast-to-Noise Ratio, standard deviation in Hounsfield Units, and Modulation Transfer Function, evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms, including iterative reconstructions and Deep Learning Image Reconstruction, has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity. Under non-linear adaptive processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations, commonly referred to as plastic or waxy look, that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality paradigm, grounded in Signal Detection Theory, where image quality is rigorously defined by the performance of an observer executing a specific clinical task, quantified by the Detectability Index. This monograph provides a systematic literature review and theoretical-metrological synthesis of the evolution of model observers and task-based metrics. The literature search was structured according to the PRISMA 2020 protocol across six international scientific databases, identifying 1,206 raw records, which after rigorous screening and eligibility criteria yielded an analytical corpus of 38 fundamental publications. We present complete step-by-step mathematical derivations transitioning from the Bayesian Ideal Observer and Hotelling Observer to anthropomorphic linear models incorporating eye filters and cortical frequency channels, the Size-Specific Weighted Detectability Index (SSW-$d'$) coupled with Size-Specific Dose Estimates (SSDE), up to recent frontiers involving deep learning architectures and Photon-Counting Computed Tomography physics. To pedagogically support the theoretical deductions, this work incorporates controlled synthetic numerical simulations coded from scratch by the author in Python, complementing each mathematical derivation with comprehensive analytical discussions focused on real-world clinical tasks, such as subtle ground-glass lung nodule detection, hypoattenuating liver metastases, hyperacute stroke ischemia, and coronary CT angiography.

\vspace{0.8cm}
\noindent Keywords: Computed Tomography. Systematic Literature Review. PRISMA 2020 Statement. Task-Based Image Quality. Model Observers. Detectability Index. Size-Specific Weighted Detectability (SSW-$d'$). Size-Specific Dose Estimates (SSDE). Deep Learning Reconstruction. Numerical Simulation in Python. Photon-Counting CT. AAPM TG-233 Report.
\clearpage

% 8. LISTA DE ILUSTRAÇÕES
\chapter*{Lista de Ilustrações}
\addcontentsline{toc}{chapter}{Lista de Ilustrações}
\begin{itemize}[leftmargin=*,label={}]
  \item Figura 1.1 -- Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 16
  \item Figura 1.2 -- Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 19
  \item Figura 3.1 -- Diagrama Conceitual das Etapas de Formulação Metodológica da Pesquisa \dotfill 26
  \item Figura 4.1 -- Fluxograma PRISMA 2020 de Identificação, Triagem, Elegibilidade e Inclusão dos Estudos da Revisão Sistemática \dotfill 30
  \item Figura 4.2 -- Modelagem Numérica Sintética da Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Desempenho Psicofísico 2AFC \dotfill 34
  \item Figura 4.3 -- Modelagem Numérica Sintética das Quatro Funções Espectrais no Domínio de Fourier segundo o Relatório AAPM TG-233 \dotfill 41
  \item Figura 4.4 -- Modelagem Numérica Sintética dos Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico \dotfill 50
  \item Figura 4.5 -- Diagrama do Fluxo de Decisão do Observador de Hotelling Canalizado (CHO) \dotfill 52
  \item Figura 4.6 -- Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D \dotfill 57
  \item Figura 4.7 -- Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC \dotfill 61
  \item Figura 4.8 -- Arquitetura de Redes Neurais para Observadores de Modelo por Aprendizado Profundo (DLMO / Vision Transformers) \dotfill 65
  \item Figura 4.9 -- Modelagem Numérica Sintética da Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -d')$ \dotfill 71
  \item Figura 4.10 -- Estrutura Conceitual do Pipeline Metrológico em Tomografia Computadorizada segundo o Relatório AAPM TG-233 \dotfill 75
\end{itemize}
\clearpage

% 9. LISTA DE TABELAS
\chapter*{Lista de Tabelas}
\addcontentsline{toc}{chapter}{Lista de Tabelas}
\begin{itemize}[leftmargin=*,label={}]
  \item Tabela 3.1 -- Estratégia de Busca Booleana Estruturada por Eixo Temático e Termos MeSH/DeCS \dotfill 23
  \item Tabela 3.2 -- Critérios de Elegibilidade, Inclusão e Exclusão para o Levantamento Bibliográfico \dotfill 25
  \item Tabela 3.3 -- Parâmetros Matemáticos das Modelagens Numéricas Sintéticas em Python \dotfill 28
  \item Tabela 4.1 -- Resumo Comparativo das Classes de Observadores de Modelo em Física Médica \dotfill 54
  \item Tabela 4.2 -- Simulação Paramétrica do Índice SSW-$d'$ e da Figura de Mérito ($\text{FOM}_{\text{SSW}}$) em Coorte Clínica Abdominal \dotfill 62
  \item Tabela 4.3 -- Síntese das Tecnologias de Detectores em Tomografia Computadorizada (EID vs PCCT) Extraída do Corpus da Revisão \dotfill 69
\end{itemize}
\clearpage

% 10. LISTA DE ABREVIATURAS E SIGLAS
\chapter*{Lista de Abreviaturas e Siglas}
\addcontentsline{toc}{chapter}{Lista de Abreviaturas e Siglas}

\begin{longtable}{p{0.18\textwidth}p{0.78\textwidth}}
  2AFC   & \emph{Two-Alternative Forced Choice} (Escolha Forçada entre Duas Alternativas) \\
  AAPM   & \emph{American Association of Physicists in Medicine} \\
  AEC    & \emph{Automatic Exposure Control} (Controle Automático de Exposição) \\
  ALARA  & \emph{As Low As Reasonably Achievable} \\
  ANVISA & Agência Nacional de Vigilância Sanitária \\
  ATCM   & \emph{Automatic Tube Current Modulation} (Modulação Automática de Corrente do Tubo) \\
  AUC    & \emph{Area Under the ROC Curve} (Área sob a Curva ROC) \\
  BKS    & \emph{Background Known Statistically} (Fundo Estatisticamente Conhecido) \\
  CdTe   & Telureto de Cádmio (\emph{Cadmium Telluride}) \\
  CHO    & \emph{Channelized Hotelling Observer} (Observador de Hotelling Canalizado) \\
  CNR    & \emph{Contrast-to-Noise Ratio} (Relação Contraste-Ruído) \\
  CTDI   & \emph{Computed Tomography Dose Index} (Índice de Dose em Tomografia) \\
  CZT    & Telureto de Cádmio e Zinco (\emph{Cadmium Zinc Telluride}) \\
  D-DOG  & \emph{Dense Difference of Gaussians} (Diferença Densa de Gaussianas) \\
  DLR    & \emph{Deep Learning Image Reconstruction} (Reconstrução por Aprendizado Profundo) \\
  DLMO   & \emph{Deep Learning Model Observer} (Observador por Aprendizado Profundo) \\
  DLP    & \emph{Dose-Length Product} (Produto Dose-Comprimento) \\
  DQE    & \emph{Detective Quantum Efficiency} (Eficiência Quântica de Detecção) \\
  $D_w$  & \emph{Water-Equivalent Diameter} (Diâmetro Equivalente em Água) \\
  EID    & \emph{Energy-Integrating Detector} (Detector de Integração de Energia) \\
  ESF    & \emph{Edge Spread Function} (Função de Espalhamento de Borda / Resposta ao Degrau) \\
  FBP    & \emph{Filtered Backprojection} (Retroprojeção Filtrada) \\
  FOM    & \emph{Figure of Merit} (Figura de Mérito de Eficiência Dosimétrica) \\
  FOV    & \emph{Field of View} (Campo de Visão de Reconstrução) \\
  HIR    & \emph{Hybrid Iterative Reconstruction} (Reconstrução Iterativa Híbrida) \\
  HO     & \emph{Hotelling Observer} (Observador de Hotelling) \\
  HU     & \emph{Hounsfield Unit} (Unidade Hounsfield) \\
  ICRP   & \emph{International Commission on Radiological Protection} \\
  ICRU   & \emph{International Commission on Radiation Units and Measurements} \\
  IO     & \emph{Ideal Observer} (Observador Ideal Bayesiano) \\
  LSF    & \emph{Line Spread Function} (Função de Espalhamento de Linha) \\
  MBIR   & \emph{Model-Based Iterative Reconstruction} (Reconstrução Iterativa Baseada em Modelo) \\
  MRMC   & \emph{Multi-Reader Multi-Case} (Múltiplos Leitores e Múltiplos Casos) \\
  MTF    & \emph{Modulation Transfer Function} (Função de Transferência de Modulação) \\
  NPS    & \emph{Noise Power Spectrum} (Espectro de Potência do Ruído) \\
  NPWE   & \emph{Non-Prewhitening Observer with Eye Filter} (Observador NPW com Filtro Ocular) \\
  NSGA-II& \emph{Non-dominated Sorting Genetic Algorithm II} \\
  PCCT   & \emph{Photon-Counting Computed Tomography} (Tomografia por Contagem de Fótons) \\
  PMMA   & Polimetilmetacrilato (Acrílico) \\
  PRISMA & \emph{Preferred Reporting Items for Systematic Reviews and Meta-Analyses} \\
  PSF    & \emph{Point Spread Function} (Função de Espalhamento de Ponto) \\
  ROC    & \emph{Receiver Operating Characteristic} (Característica de Operação do Receptor) \\
  ROI    & \emph{Region of Interest} (Região de Interesse) \\
  SDT    & \emph{Signal Detection Theory} (Teoria de Detecção de Sinais) \\
  SKE    & \emph{Signal Known Exactly} (Sinal Exatamente Conhecido) \\
  SNR    & \emph{Signal-to-Noise Ratio} (Relação Sinal-Ruído) \\
  SSDE   & \emph{Size-Specific Dose Estimate} (Estimativa de Dose Específica por Tamanho, AAPM 204) \\
  SSW-$d'$ & \emph{Size-Specific Weighted Detectability Index} (Índice de Detectabilidade Ponderado por Tamanho e Tarefa) \\
  TBIQ   & \emph{Task-Based Image Quality} (Qualidade de Imagem Baseada em Tarefa) \\
  TOPSIS & \emph{Technique for Order Preference by Similarity to Ideal Solution} \\
  TTF    & \emph{Task-Based Transfer Function} (Função de Transferência da Tarefa) \\
  ViT    & \emph{Vision Transformer} \\
  VMI    & \emph{Virtual Monoenergetic Image} (Imagem Monoenergética Virtual) \\
  WSS    & \emph{Wide-Sense Stationary} (Estacionariedade no Sentido Amplo)
\end{longtable}
\clearpage

% 11. SUMÁRIO
\tableofcontents
\clearpage

% ==============================================================================
% ELEMENTOS TEXTUAIS
% ==============================================================================
\pagestyle{fancy}
\pagenumbering{arabic}
\setcounter{page}{1}

% ------------------------------------------------------------------------------
% CAPÍTULO 1: INTRODUÇÃO
% ------------------------------------------------------------------------------
\chapter{Introdução}
\label{chap:introducao}

A Tomografia Computadorizada (TC) consolidou-se como um dos pilares mais revolucionários e transformadores da medicina diagnóstica moderna, otimizando o diagnóstico clínico desde a sua concepção teórica e implementação prática por Godfrey N. Hounsfield e Allan M. Cormack na década de 1970 \cite{bushberg2020, attix1986, seeram2015}. Ao converter projeções radiográficas angulares de atenuação de raios X em matrizes tridimensionais de coeficientes de atenuação linear seccionais, a tomografia viabilizou a visualização anatômica de órgãos internos com resolução espacial milimétrica e diferenciação tecidual adequada.

\section{Fundamentos da Aquisição Tomográfica}
\label{sec:panorama_fisico_tc}

A formação da imagem tomográfica tem como fundamento a atenuação exponencial de um feixe polienergético de raios X ao atravessar a matéria biológica. A atenuação macroscópica ao longo de uma trajetória retilínea $L$ é governada pela Lei de Beer-Lambert generalizada:
\begin{equation}
  I = \int_0^{E_{\text{máx}}} I_0(E) \exp\left( -\int_L \mu(x, y, z; E) \, dl \right) dE
  \label{eq:beer_lambert}
\end{equation}
onde $I_0(E)$ representa o espectro de emissão do tubo de raios X em função da energia do fóton incidente $E$, e $\mu(x, y, z; E)$ é a distribuição tridimensional do coeficiente de atenuação linear total do meio, determinado predominantemente pelo Efeito Fotoelétrico ($\tau \propto \rho \frac{Z^3}{E^3}$) em baixas energias e pelo Espalhamento Compton ($\sigma_c \propto \rho_e$) na faixa intermediária de diagnóstico (30 a 140 keV) \cite{attix1986, bushberg2020}.

A amostragem de atenuação integrada ao longo de múltiplos ângulos $\phi \in [0, \pi]$ e posições radiais $r$ constitui a Transformada de Radon bidimensional de uma fatia anatômica $f(x, y)$:
\begin{equation}
  p(r, \phi) = \mathcal{R}\{f(x, y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, \delta(x\cos\phi + y\sin\phi - r) \, dx \, dy
  \label{eq:radon_transform}
\end{equation}
O conjunto dessas projeções em coordenadas polares $(r, \phi)$ forma o sinograma. A inversão analítica do sinograma para reconstruir a função contínua $f(x, y)$ é fundamentada no Teorema da Fatia Central de Fourier (\emph{Projection-Slice Theorem}), o qual estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $p(r, \phi)$ no ângulo $\phi$ é exatamente idêntica à fatia radial correspondente da Transformada de Fourier bidimensional da imagem $F(u, v)$ que passa pela origem do espaço de frequências $(u, v)$ \cite{barrett_myers_2004, seeram2015}:
\begin{equation}
  \mathcal{F}_{1D}\{p(r, \phi)\} = F(f\cos\phi, f\sin\phi)
  \label{eq:fourier_slice}
\end{equation}

A partir do Teorema da Fatia Central, a inversão matemática em coordenadas polares introduz um fator Jacobiano $|f|$, que atua no domínio de Fourier como um filtro passa-altas cônico. Essa formulação origina o algoritmo clássico da Retroprojeção Filtrada (\emph{Filtered Backprojection} --- FBP):
\begin{equation}
  f(x, y) = \int_0^{\pi} \left[ p(r, \phi) * h(r) \right]_{r = x\cos\phi + y\sin\phi} d\phi
  \label{eq:fbp_formula}
\end{equation}
onde $h(r) = \mathcal{F}^{-1}\{|f|\}$ é a resposta ao impulso do filtro de rampa (ex: filtros Ram-Lak, Shepp-Logan ou Hann). Sem a aplicação prévia do filtro de rampa $|f|$, a retroprojeção simples convolucionaria a imagem original com uma função de espalhamento espacial $1/r$, gerando um borramento severo e inaceitável para o diagnóstico médico \cite{seeram2015}.

\section{Dosimetria e Princípio ALARA}
\label{sec:paradigma_dosimetrico}

Embora indispensável na prática clínica, a tomografia computadorizada é responsável pela maior fração da dose coletiva de radiação ionizante de origem médica em nível global \cite{mccollough2026}. A interação dos fótons X com os tecidos humanos induz ionizações moleculares e quebras de duplas fitas de DNA, conferindo riscos de efeitos estocásticos (mutagênese e carcinogênese radioinduzida a longo prazo).

Para gerenciar esse risco de forma ética e tecnicamente rigorosa, a Comissão Internacional de Proteção Radiológica (ICRP Publicação 103) estabeleceu o princípio ALARA (\emph{As Low As Reasonably Achievable}) \cite{icrp103_2007}. A física médica atua no núcleo do princípio ALARA: a dose absorvida pelo paciente deve ser reduzida ao menor nível compatível com a preservação estrita da capacidade diagnóstica.

A quantificação padronizada da dose em tomografia baseia-se no Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), medido com câmara de ionização tipo lápis de 100 mm imersa em simuladores cilíndricos de PMMA de 16 cm (cabeça) e 32 cm (corpo):
\begin{align}
  \text{CTDI}_{\text{w}} &= \frac{1}{3} \text{CTDI}_{\text{centro}} + \frac{2}{3} \text{CTDI}_{\text{periférico}} \label{eq:ctdi_w} \\
  \text{CTDI}_{\text{vol}} &= \frac{\text{CTDI}_{\text{w}}}{\text{pitch}} \label{eq:ctdi_vol} \\
  \text{DLP} &= \text{CTDI}_{\text{vol}} \times L \label{eq:dlp_def}
\end{align}
onde o Produto Dose-Comprimento ($\text{DLP}$, em $\text{mGy}\cdot\text{cm}$) expressa a energia total depositada ao longo do comprimento de varredura $L$. A Dose Efetiva $E$ (em $\text{mSv}$) é estimada por $E \approx k \cdot \text{DLP}$, utilizando coeficientes de conversão normalizados por região anatômica $k$ \cite{icrp103_2007}.

No cenário regulatório brasileiro, a Agência Nacional de Vigilância Sanitária (ANVISA) estabeleceu requisitos mandatórios através da Resolução da Diretoria Colegiada RDC nº 611/2022 e da Instrução Normativa IN nº 93/2021 \cite{anvisa_rdc611_2022, anvisa_in93_2021}. Essas normativas exigem programas estruturados de garantia da qualidade, calibrações dosimétricas periódicas, monitoramento de Níveis de Referência Diagnóstica (DRLs) e a atuação contínua de físicos médicos especialistas em radiodiagnóstico.

\section{Métricas Tradicionais e Limitações Físicas}
\label{sec:metricas_escalares_tradicionais}

Durante quatro décadas de hegemonia da FBP, a metrologia da qualidade de imagem em TC baseou-se quase que exclusivamente em métricas escalares simples, avaliadas em meios homogêneos de água ou PMMA:
\begin{enumerate}
  \item Relação Sinal-Ruído ($SNR$): Razão entre o valor médio em Unidades Hounsfield ($\mu_{\text{HU}}$) e o desvio padrão estocástico ($\sigma_{\text{HU}}$) em uma ROI uniforme:
  \begin{equation}
    SNR = \frac{\mu_{\text{HU}}}{\sigma_{\text{HU}}}
    \label{eq:snr_formula}
  \end{equation}
  \item Relação Contraste-Ruído ($CNR$): Diferença entre a média do sinal do alvo clínico ($\mu_{\text{alvo}}$) e a média do fundo circundante ($\mu_{\text{fundo}}$), normalizada pela variância combinada:
  \begin{equation}
    CNR = \frac{|\mu_{\text{alvo}} - \mu_{\text{fundo}}|}{\sqrt{\frac{1}{2}(\sigma_{\text{alvo}}^2 + \sigma_{\text{fundo}}^2)}}
    \label{eq:cnr_formula}
  \end{equation}
  \item Função de Transferência de Modulação ($MTF(f)$): Magnitude normalizada da Transformada de Fourier bidimensional da Função de Espalhamento de Ponto ($\text{PSF}(x, y)$), quantificando a preservação da modulação do contraste em função da frequência espacial $f$ ($\text{mm}^{-1}$):
  \begin{equation}
    MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
    \label{eq:mtf_formula}
  \end{equation}
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{flow2_comparativo_paradigmas.png}{Comparativo Estrutural entre o Paradigma Clássico e o Paradigma TBIQ.}
  \caption[Comparativo entre Paradigmas Físicos]{Comparativo entre o Paradigma Clássico e o Paradigma TBIQ \cite{aapm_tg233_2019, icru54_1996, barrett_myers_2004}.}
  \label{fig:comparativo_paradigmas}
\end{figure}

\subsection{Premissas da Teoria Linear}
\label{subsec:pilares_validade_linear}
A validade matemática das grandezas clássicas $SNR$, $CNR$ e $MTF$ repousa sobre três premissas fundamentais da teoria de sistemas lineares invariantes no espaço:
\begin{enumerate}
  \item Linearidade Estrita do Operador de Reconstrução $\mathcal{R}$: A resposta a uma combinação linear de atenuações é a combinação linear das respostas individuais: $\mathcal{R}\{\alpha f_1 + \beta f_2\} = \alpha \mathcal{R}\{f_1\} + \beta \mathcal{R}\{f_2\}$;
  \item Isoplanatismo Espacial (Invariância por Translação): A função de espalhamento $\text{PSF}(x, y)$ independe da coordenada absoluta na matriz de reconstrução;
  \item Estacionariedade do Ruído no Sentido Amplo (WSS --- \emph{Wide-Sense Stationary}): Um processo estocástico bidimensional $I(x, y)$ satisfaz WSS se sua média $\mathbb{E}[I(x, y)] = \mu_0$ for constante no espaço e sua função de autocovariância $K_I(\mathbf{r}_1, \mathbf{r}_2) = K_I(\mathbf{r}_1 - \mathbf{r}_2)$ depender unicamente do vetor de deslocamento espacial relativo $\Delta \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$.
\end{enumerate}

Quando essas premissas são violadas, as métricas clássicas colapsam. O desvio padrão $\sigma_{\text{HU}}$ mede apenas a dispersão estatística escalar, sendo completamente cego à correlação espacial entre pixels e à textura do ruído. Dois exames com idêntico $\sigma_{\text{HU}} = 15\text{ HU}$ podem apresentar aparências visuais totalmente distintas: um com ruído fino de alta frequência (facilmente filtrado pelo córtex visual humano) e outro com manchas cerosas grosseiras de baixa frequência que mimetizam ou ocultam tumores hepáticos ou renais.

\section{Ruptura Não Linear: Da FBP à DLR}
\label{sec:ruptura_nao_linear_intro}

Para reduzir a dose de radiação mantendo a relação sinal-ruído, a indústria tomográfica substituiu gradualmente a FBP por algoritmos iterativos estatísticos (HIR e MBIR) e, na vanguarda atual, por algoritmos de Reconstrução por Aprendizado Profundo (\emph{Deep Learning Image Reconstruction} --- DLR), tais como TrueFidelity (GE Healthcare), AiCE (Canon Medical Systems), Precise Image (Philips) e ClariCT.AI (ClariPi) \cite{racine2020, debbiche2024, greffier2026}. Em paralelo e em sinergia com a evolução algorítmica, a arquitetura de detecção vivenciou sua mais profunda transformação com a introdução clínica dos tomógrafos por Contagem de Fótons (\emph{Photon-Counting CT} --- PCCT), consubstanciada pela aprovação regulatória e comercialização do sistema pioneiro NAEOTOM Alpha (Siemens Healthineers, liberado pelo FDA em 2021) e pelo desenvolvimento de protótipos avançados em CdTe e silício profundo por outros grandes fabricantes mundiais (GE Healthcare, Philips e Canon Medical Systems) \cite{willemink2018, rajendran2021, pimenta2026}.

Esses modelos utilizam redes neurais convolucionais profundas (\emph{Deep Convolutional Neural Networks}) treinadas com pares de imagens tomográficas adquiridas em doses padrão de alta qualidade e imagens correspondentes adquiridas em doses ultrabaixas. Ao aprender mapeamentos não lineares complexos entre o espaço de projeção e a imagem final, as redes DLR conseguem suprimir seletivamente o ruído quântico de alta frequência preservando bordas de alto contraste.

Entretanto, a incorporação clínica dos algoritmos DLR acarretou uma quebra paradigmática estrutural:
\begin{itemize}
  \item Perda da Linearidade e Dependência de Contraste: A resolução espacial não é mais uma propriedade invariante do sistema; ela varia dinamicamente de acordo com o contraste do alvo ($\Delta C$). Alvos de alto contraste (como artérias com iodo ou ossos) são reconstruídos com bordas nítidas, enquanto alvos sutis de baixo contraste ($\Delta C \le 30\text{ HU}$, como metástases hepáticas) sofrem suavização excessiva;
  \item Quebra da Estacionariedade (Não-WSS): O ruído torna-se espacialmente heterogêneo e anisotrópico, exibindo comportamentos distintos próximo a interfaces ósseas e no centro de parênquimas moles;
  \item Efeito Ceroso ou Plástico (\emph{Plastic/Waxy Look}): A regularização não linear desloca o espectro de potência do ruído para baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$), criando padrões de granulação não naturais que causam desconforto e fadiga visual aos radiologistas e prejudicam a detecção de microestruturas patológicas \cite{toia2023, solomon2020}.
\end{itemize}

\section{Qualidade Baseada em Tarefa (TBIQ)}
\label{sec:mudanca_paradigma_tbiq}

Diante da inadequação das métricas escalares clássicas para avaliar sistemas não lineares, a física médica internacional consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ) através dos relatórios canônicos AAPM TG-233 e ICRU Report 54 (\cref{fig:tbiq_paradigm}) \cite{aapm_tg233_2019, icru54_1996}.

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.96\textwidth]{flow1_tbiq_paradigm.png}{Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa.}
  \caption[Pilares do Paradigma TBIQ]{Pilares da Qualidade de Imagem Baseada em Tarefa (TBIQ) \cite{aapm_tg233_2019, barrett_myers_2004, metz1986}.}
  \label{fig:tbiq_paradigm}
\end{figure}

O paradigma TBIQ fundamenta-se na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT) e postula que a qualidade de uma imagem médica não é um atributo estático intrínseco, mas sim a medida objetiva e reprodutível do desempenho de um observador (médico radiologista ou modelo computacional) ao realizar uma tarefa diagnóstica clinicamente relevante.

A abordagem TBIQ integra quatro pilares analíticos contínuos no domínio de Fourier através do Índice de Detectabilidade ($d'$):
\begin{enumerate}
  \item Função de Transferência da Tarefa ($TTF(f)$): Modela a resolução espacial do tomógrafo em função da frequência espacial e do contraste específico do alvo patológico ($\Delta C$);
  \item Espectro de Potência do Ruído ($NPS(f)$): Descreve a variância e a textura estocástica do ruído no domínio contínuo de Fourier;
  \item Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$): Modela analiticamente o tamanho, a geometria e o perfil de atenuação da patologia;
  \item Modelo Perceptual do Observador ($E(f)$ e Canais Corticais): Modela a sensibilidade ao contraste do olho humano (função CSF de Burgess) e a filtragem em frequências corticais do córtex visual primário (V1).
\end{enumerate}

Para além da avaliação em um único tamanho de simulador, a vanguarda da física médica contemporânea expandiu o formalismo do $d'$ para a escala populacional clínica através do Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa (\emph{Size-Specific Weighted Detectability Index} --- SSW-$d'$) \cite{fitton2026, goppel2021}. Esse formalismo acopla a resposta espectral em múltiplos diâmetros corporais equivalentes em água ($D_w$) às matrizes de ponderação de relevância clínica ($\Omega_j$) e à Estimativa de Dose Específica por Tamanho (SSDE, AAPM 204) \cite{aapm_report204}, viabilizando uma Figura de Mérito de Eficiência Dosimétrica ($\text{FOM}_{\text{SSW}}$) aplicável a coortes hospitalares inteiras.

\section{Justificativa}
\label{sec:justificativa_problema}

A introdução acelerada de softwares baseados em inteligência artificial e de novos detectores na rotina hospitalar criou um descompasso metodológico crítico. Enquanto a tecnologia de aquisição e reconstrução opera em regimes fortemente não lineares e espectrais, os programas de garantia da qualidade e aceitação de equipamentos no Brasil ainda se baseiam predominantemente em testes de constância com métricas escalares simplificadas em fantomas homogêneos de água.

A persistência de protocolos avaliados unicamente por $SNR$ ou desvio padrão médio induz dois riscos clínicos severos:
\begin{enumerate}
  \item Falsa Sensação de Segurança Dosimétrica: A aceitação de reduções agressivas de dose com base na redução de $\sigma_{\text{HU}}$ em água, ignorando a degradação da $TTF(f)$ para alvos de baixo contraste, elevando o risco de falsos-negativos em exames oncológicos;
  \item Subutilização de Recursos Avançados: A incapacidade de parametrizar objetivamente os filtros não lineares e as energias virtuais monoenergéticas ($VMI$) em PCCT, privando os pacientes dos benefícios de redução real de dose e contraste iodado.
\end{enumerate}

Esta monografia justifica-se pela necessidade premente de fornecer à comunidade de física médica uma sistematização teórica rigorosa, didática e integrada das métricas baseadas em tarefa, estabelecendo a ponte formal entre os princípios matemáticos de Fourier, a psicofísica da visão e as diretrizes regulatórias vigentes.

% ------------------------------------------------------------------------------
% CAPÍTULO 2: OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Objetivos}
\label{chap:objetivos}

\section{Objetivo Geral}
\label{sec:objetivo_geral}
O objetivo geral deste Trabalho de Conclusão de Curso consiste em realizar uma revisão bibliográfica sistemática crítica e modelagem teórico-metrológica unificada da evolução dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo os alicerces físicos, matemáticos e normativos que conectam a Teoria Clássica de Detecção de Sinais aos recentes observadores baseados em redes profundas (\emph{Vision Transformers}) e à física dos detectores de contagem de fótons.

\section{Objetivos Específicos}
\label{chap:objetivos_especificos}
Para alcançar o objetivo geral, definiram-se os seguintes objetivos específicos:
\begin{enumerate}
  \item Revisão Sistemática PRISMA 2020: Mapear, selecionar e sintetizar criticamente as publicações seminais e contemporâneas sobre métricas baseadas em tarefa e observadores de modelo em tomografia computadorizada;
  \item Dedução das Métricas em Fourier: Apresentar as deduções matemáticas contínuas completas da $TTF(f)$, $NPS(f)$, $W_{\text{task}}(f)$, $E(f)$ e do Índice de Detectabilidade ($d'$) no formalismo do relatório AAPM TG-233;
  \item Formalização dos Observadores de Modelo: Deduzir e comparar analiticamente o Observador Ideal de Hotelling (teto Bayesiano), o modelo antropomórfico NPWE, o Observador CHO com canais corticais (D-DOG, Laguerre-Gauss, Gabor) e os observadores profundos DLMO;
  \item Formalização do Índice Ponderado por Tamanho (SSW-$d'$): Formalizar analiticamente o Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa (SSW-$d'$), acoplando a amostragem em fantomas multivariados ($D_w$) à Estimativa de Dose Específica por Tamanho (SSDE, AAPM 204) e à Figura de Mérito de Eficiência Dosimétrica ($\text{FOM}_{\text{SSW}}$) para otimização de coortes clínicas populacionais;
  \item Análise do Colapso Linear sob DLR: Explicitar as causas físico-matemáticas da falência dos modelos lineares sob algoritmos não lineares por aprendizado profundo e detalhar a metodologia de fantomas híbridos e testes 2AFC;
  \item Física da PCCT e Otimização Multiobjetivo: Sistematizar os fundamentos dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e formular a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -d')$;
  \item Modelagem Numérica Sintética em Python: Desenvolver rotinas computacionais próprias para simulação didática e reprodutível das curvas de detectabilidade, canais corticais, detrending polinomial e superfícies de decisão;
  \item Correlação com a Prática Clínica: Integrar a cada dedução teórica uma análise crítica aprofundada do impacto da métrica sobre a tarefa diagnóstica do médico radiologista em cenários oncológicos, neurológicos, musculoesqueléticos, cardiológicos e pediátricos.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 3: METODOLOGIA
% ------------------------------------------------------------------------------
\chapter{Metodologia}
\label{chap:metodologia}

Este capítulo estabelece o delineamento metodológico do trabalho, formaliza as estratégias de busca bibliográfica sistemática com equações booleanas nas bases de dados internacionais, apresenta os critérios de elegibilidade baseados nas diretrizes PRISMA 2020, define os procedimentos de avaliação de qualidade e risco de viés dos estudos incluídos, estabelece o corpus normativo internacional e explicita a formulação analítica das modelagens numéricas sintéticas programadas em linguagem Python.

\section{Delineamento Metodológico}
\label{sec:delineamento_classificacao}
Este Trabalho de Conclusão de Curso classifica-se formalmente como uma monografia de revisão bibliográfica sistemática crítica, sistematização conceitual e modelagem teórico-metrológica. O trabalho não envolveu a coleta direta de dados clínicos primários com pacientes ou a realização de ensaios laboratoriais proprietários em bancada, mas sim a consolidação exaustiva e rigorosa do estado da arte internacional da física médica, estruturando as deduções matemáticas e fornecendo modelagens sintéticas controladas para fins didáticos e metrológicos.

\section{Estratégia de Busca Bibliográfica}
\label{sec:estrategia_busca_booleana_detalhada}
O levantamento bibliográfico foi conduzido de acordo com as diretrizes metodológicas adaptadas do protocolo PRISMA 2020 (\emph{Preferred Reporting Items for Systematic Reviews and Meta-Analyses}) \cite{page2021}, garantindo transparência, abrangência e reprodutibilidade.

\subsection{Bases de Dados}
\label{subsec:bases_consultadas_detalhe}
A busca de literatura foi realizada de forma exaustiva nas seguintes bases científicas e repositórios internacionais:
\begin{enumerate}
  \item PubMed / MEDLINE (National Library of Medicine, Bethesda, EUA);
  \item IEEE Xplore Digital Library (Institute of Electrical and Electronics Engineers);
  \item Web of Science Core Collection (Clarivate Analytics);
  \item Scopus (Elsevier B.V.);
  \item AAPM Reports and Medical Physics Journal Repository (American Association of Physicists in Medicine);
  \item SPIE Digital Library (International Society for Optics and Photonics --- Medical Imaging Proceedings).
\end{enumerate}

\subsection{Descritores Controlados (MeSH/DeCS)}
\label{subsec:estruturacao_descritores}
Os descritores foram rigorosamente mapeados a partir dos vocabulários controlados MeSH (\emph{Medical Subject Headings}) e DeCS (\emph{Descritores em Ciências da Saúde}), combinados a termos livres especializados da física de imagens médicas. A busca foi estruturada em três eixos conceituais fundamentais interligados por operadores lógicos booleanos:
\begin{itemize}
  \item Eixo 1 (Modalidade e Tecnologia de Detecção): Termos que delimitam o escopo da tomografia computadorizada (\emph{Tomography, X-Ray Computed}, \emph{Photon-Counting CT}, \emph{PCCT}, \emph{Spectral CT});
  \item Eixo 2 (Metrologia e Avaliação Baseada em Tarefa): Termos que identificam o paradigma TBIQ e a teoria de Fourier (\emph{Task-Based Image Quality}, \emph{Detectability Index}, \emph{Signal Detection Theory}, \emph{Task-Based Transfer Function}, \emph{Noise Power Spectrum}, \emph{Size-Specific Detectability});
  \item Eixo 3 (Modelos de Observador e Algoritmos de Reconstrução): Termos associados aos observadores matemáticos e métodos de reconstrução (\emph{Model Observer}, \emph{Channelized Hotelling Observer}, \emph{Non-Prewhitening Observer}, \emph{Deep Learning Image Reconstruction}, \emph{Vision Transformers}).
\end{itemize}

\subsection{Sintaxe das Buscas Booleanas}
\label{subsec:equacoes_booleanas_tabela}
A \cref{tab:estrategia_booleana} apresenta as equações booleanas formais implementadas em cada base de dados, utilizando operadores relacionais (\texttt{AND}, \texttt{OR}, \texttt{NOT}), parênteses de hierarquia e filtros de campo.

\begin{table}[htbp]
  \centering
  \small
  \caption[Estratégia de Busca Booleana por Base de Dados]{Estratégia de Busca Booleana Estruturada por Base de Dados e Eixos Conceituais \cite{page2021}.}
  \label{tab:estrategia_booleana}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.22\textwidth} >{\RaggedRight\footnotesize\ttfamily\arraybackslash}X}
    \toprule
    \textbf{Base de Dados} & \textbf{Equação Booleana de Busca (\emph{Search String})} \\
    \midrule
    PubMed / MEDLINE & 
    ("Tomography, X-Ray Computed"[MeSH] OR "computed tomography"[Title/Abstract] OR "photon counting CT"[Title/Abstract] OR "PCCT"[Title/Abstract]) AND ("task-based image quality"[Title/Abstract] OR "model observer"[Title/Abstract] OR "detectability index"[Title/Abstract] OR "channelized hotelling"[Title/Abstract] OR "NPWE"[Title/Abstract] OR "size-specific"[Title/Abstract]) AND ("deep learning reconstruction"[Title/Abstract] OR "iterative reconstruction"[Title/Abstract] OR "noise power spectrum"[Title/Abstract] OR "AAPM TG-233"[Title/Abstract]) NOT ("radiotherapy"[Title] OR "positron emission"[Title]) \\
    \addlinespace[0.4em]
    IEEE Xplore & 
    (("Document Title":"computed tomography" OR "Abstract":"computed tomography" OR "Abstract":"photon counting") AND ("Abstract":"task-based" OR "Abstract":"model observer" OR "Abstract":"detectability") AND ("Abstract":"deep learning" OR "Abstract":"Hotelling observer" OR "Abstract":"noise power spectrum")) \\
    \addlinespace[0.4em]
    Web of Science & 
    TS=(("computed tomography" OR "PCCT" OR "photon-counting") AND ("task-based image quality" OR "model observer*" OR "detectability index" OR "d-prime" OR "SSW-d") AND ("deep learning reconstruction" OR "channelized hotelling" OR "Fourier metrics" OR "AAPM TG-233")) \\
    \addlinespace[0.4em]
    Scopus & 
    TITLE-ABS-KEY(("computed tomography" OR "photon counting CT") AND ("task-based image quality" OR "model observer" OR "detectability index") AND ("deep learning" OR "channelized hotelling" OR "NPWE" OR "noise power spectrum")) AND NOT TITLE("PET-CT" OR "SPECT") \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026).}
\end{table}

\subsection{Critérios de Inclusão e Exclusão}
\label{subsec:criterios_elegibilidade_detalhe}
Para a seleção criteriosa dos estudos, estabeleceram-se critérios rigorosos de elegibilidade documentados na \cref{tab:criterios_inclusao_exclusao}.

\begin{table}[htbp]
  \centering
  \small
  \caption[Critérios de Elegibilidade da Revisão]{Critérios de Elegibilidade, Inclusão e Exclusão para o Corpus Bibliográfico \cite{page2021, aapm_tg233_2019, icru54_1996}.}
  \label{tab:criterios_inclusao_exclusao}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.22\textwidth} >{\RaggedRight\arraybackslash}X}
    \toprule
    \textbf{Dimensão} & \textbf{Critérios Definidos} \\
    \midrule
    Critérios de Inclusão & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item Artigos originais e de revisão publicados em periódicos indexados com revisão por pares (\emph{peer-reviewed});
      \item Relatórios técnicos normativos de comissões internacionais de física médica (AAPM, ICRU, ICRP, IAEA, IEC);
      \item Estudos que desenvolvam ou apliquem deduções matemáticas formais de métricas baseadas em tarefa ($TTF$, $NPS$, $d'$, SSW-$d'$, SDT, ROC, 2AFC, MRMC);
      \item Trabalhos que analisem observadores de modelo (IO, HO, NPWE, CHO, DLMO) em tomografia computadorizada;
      \item Publicações focadas em reconstruções iterativas estatísticas (HIR/MBIR), inteligência artificial (DLR) ou contagem de fótons (PCCT);
      \item Obras seminais históricas da física de imagens (Barrett, Burgess, Myers, Wagner, Metz, Rose).
    \end{itemize} \\
    \addlinespace[0.4em]
    Critérios de Exclusão & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item Artigos clínicos sem fundamentação física, dosimétrica ou metrológica;
      \item Estudos restritos a modalidades não tomográficas (ressonância magnética pura, ultrassom, medicina nuclear não acoplada);
      \item Resumos de conferências sem texto completo (\emph{abstracts only}), cartas ao editor e comentários sem dados analíticos;
      \item Publicações em duplicata entre as bases de dados consultadas.
    \end{itemize} \\
    \addlinespace[0.4em]
    Janela Temporal & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item Eixo Contemporâneo (2018--2026): Para algoritmos DLR, observadores DLMO baseados em Vision Transformers, detectores PCCT, métrica populacional SSW-$d'$ e protocolo AAPM TG-233;
      \item Eixo Seminal Histórico (1948--2017): Para a teoria de Rose, teoria de detecção de sinais, deduções de Hotelling, canais corticais do CHO e testes 2AFC.
    \end{itemize} \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026).}
\end{table}

\subsection{Avaliação da Qualidade, Risco de Viés e Certeza da Evidência (PRISMA 2020)}
\label{subsec:avaliacao_risco_vies_metodologia}
Em estrito cumprimento aos Itens 11 e 22 do protocolo PRISMA 2020 \cite{page2021}, o corpus de publicações selecionadas não foi tratado sob a premissa de equivalência epistêmica cega. Pelo contrário, estruturou-se uma metodologia formal de avaliação crítica adaptada para a física médica e metrologia de imagens diagnósticas, categorizando os 38 estudos incluídos em três tipologias metodológicas distintas:

\begin{enumerate}
  \item \textbf{Estudos Teóricos, Normativos e Obras Seminais ($n = 12$):} Avaliados quanto ao rigor analítico das deduções matemáticas, consistência na fundamentação formal na teoria estatística de decisão (Bayes/Neyman-Pearson) e grau de consenso normativo internacional emitido por comitês de especialistas (AAPM, ICRU, ICRP, ANVISA) ou livros canônicos de física médica;
  \item \textbf{Estudos Psicofísicos Experimentais com Observadores Humanos ($n = 14$):} Avaliados mediante adaptação das diretrizes QUADAS-2 e QUADAS-C (\emph{Quality Assessment of Diagnostic Accuracy Studies}) combinadas aos padrões psicofísicos de ICRU-54 e AAPM TG-233. Analisaram-se quatro domínios críticos:
  \begin{itemize}
    \item \emph{Amostragem de Leitores:} Número de radiologistas especialistas participantes ($J \ge 4$), experiência clínica e cegamento frente aos parâmetros de dose e algoritmos de reconstrução;
    \item \emph{Amostragem de Casos e Alvos:} Número de imagens/ROIs independentes avaliadas ($K \ge 100$ casos), randomização espacial do sinal e representatividade das densidades teciduais;
    \item \emph{Padronização Psicofísica e Exibição:} Calibração de monitores diagnósticos segundo a norma DICOM GSDF (AAPM TG-18), controle estrito de luminância e iluminância ambiente ($< 25\text{ lux}$), e controle de fadiga visual;
    \item \emph{Modelo Estatístico de Análise:} Emprego de ANOVA multivariada com efeitos aleatórios cruzados (DBM/HOR) para isolar a variabilidade inter-observador e inter-caso.
  \end{itemize}
  \item \textbf{Estudos de Modelagem Numérica e Observadores Computacionais ($n = 12$):} Avaliados quanto à robustez da amostragem estocástica do ruído ($M \ge 100$ ROIs homogêneas independentes), aplicação de técnicas de detrending polinomial 2D para eliminação de gradientes anatômicos lentos, prevenção de vazamento de dados (*data leakage*) e controle de sobreajuste (*overfitting*) em modelos de aprendizado profundo (DLMO).
\end{enumerate}

Para a avaliação da \textbf{Certeza da Evidência}, adaptou-se a sistemática do sistema GRADE (\emph{Grading of Recommendations Assessment, Development and Evaluation}) para a metrologia física, classificando as evidências em três níveis epistêmicos:
\begin{itemize}
  \item \textbf{Certeza Alta:} Evidência derivada de deduções matemáticas exatas fundamentadas em primeiros princípios ou estudos psicofísicos multicêntricos com validação MRMC abrangente;
  \item \textbf{Certeza Moderada:} Evidência consistente em ensaios controlados com fantomas físicos e observadores humanos de centro único, com limitações conhecidas de generalização para outros tomógrafos;
  \item \textbf{Certeza Exploratória / Baixa:} Evidência preliminar obtida em estudos monocêntricos com número restrito de leitores ($J \le 2$) ou simulações computacionais sem ampla replicação externa.
\end{itemize}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.95\textwidth]{flow_metodologia_etapas.png}{Etapas Metodológicas da Pesquisa.}
  \caption[Etapas Metodológicas da Pesquisa]{Etapas Metodológicas da Pesquisa e Integração dos Modelos \cite{page2021, aapm_tg233_2019, barrett_myers_2004}.}
  \label{fig:fluxograma_metodologia_conceito}
\end{figure}

\section{Documentos Normativos Internacionais}
\label{sec:corpus_normativo_detalhe}
O alinhamento normativo do estudo estruturou-se sobre cinco pilares documentais canônicos:
\begin{enumerate}
  \item AAPM TG-233 Report (2019): \emph{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}, documento balizador que padroniza o cálculo contínuo de $TTF(f)$, $NPS(f)$, $d'$ e a geometria dos simuladores de calibração \cite{aapm_tg233_2019};
  \item AAPM Report 204 / 220 (2011/2014): \emph{Size-Specific Dose Estimates (SSDE) in Pediatric and Adult Body CT Examinations}, que formalizou a quantificação da dose absorvida corrigida pelo diâmetro equivalente em água ($D_w$) \cite{aapm_report204};
  \item ICRU Report 54 (1996): \emph{Medical Imaging --- The Assessment of Image Quality}, que estabeleceu o formalismo fundamental de observadores estatísticos e métricas baseadas em tarefa \cite{icru54_1996};
  \item ICRP Publication 103 (2007): \emph{The 2007 Recommendations of the International Commission on Radiological Protection}, base ética e científica do princípio ALARA e da dosimetria de pacientes \cite{icrp103_2007};
  \item ANVISA RDC nº 611/2022 e IN nº 93/2021: Marcos regulatórios federais que normatizam a garantia da qualidade e o controle dosimétrico em tomografia computadorizada no Brasil \cite{anvisa_rdc611_2022, anvisa_in93_2021}.
\end{enumerate}

\section{Modelagem Numérica em Python}
\label{sec:metodologia_simulacao_python_detalhada}

Para fundamentar didaticamente as deduções matemáticas e ilustrar os limites físicos dos modelos em cenários clínicos controlados, foram desenvolvidas modelagens numéricas sintéticas implementadas em linguagem Python (versão 3.10+, utilizando NumPy, SciPy e Matplotlib). 

Sublinha-se que todos os gráficos, distribuições de probabilidade, respostas espectrais e variedades tridimensionais apresentados no Capítulo \ref{chap:resultados_discussao} (Figuras 4.2 a 4.6 e 4.9) não constituem ilustrações conceituais genéricas ou cópias de softwares de fabricantes, mas sim o produto direto de scripts computacionais originais codificados pelo próprio autor.

A \cref{tab:parametros_simulacao} sumariza com precisão as formulações matemáticas, os domínios de amostragem e os parâmetros exatos utilizados na geração de cada simulação sintética.

\begin{table}[htbp]
  \centering
  \small
  \caption[Parâmetros das Simulações Numéricas]{Parâmetros Matemáticos das Modelagens Numéricas Sintéticas em Python \cite{barrett_myers_2004, aapm_tg233_2019, burgess1999, deb2002, fitton2026, aapm_report204}.}
  \label{tab:parametros_simulacao}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.20\textwidth} >{\RaggedRight}p{0.26\textwidth} >{\RaggedRight\arraybackslash}X}
    \toprule
    \textbf{Figura / Tópico} & \textbf{Equação / Modelo} & \textbf{Parâmetros Computacionais Utilizados} \\
    \midrule
    Figura 4.2 & $t_0 \sim \mathcal{N}(\mu_0, \sigma_t^2)$ \cite{metz1986} & $\mu_0 = 0$, $\mu_1 = 2{,}2$, $\sigma_t = 1{,}0$, $t_c = 1{,}3$, \\
    (SDT, ROC, 2AFC) & $t_1 \sim \mathcal{N}(\mu_1, \sigma_t^2)$ \cite{barrett_myers_2004} & $d' = 2{,}2$; $t_c \in [-4; +6]$, $\Delta t_c = 0{,}01$; \\
    & $P_C(d') = \Phi(d'/\sqrt{2})$ \cite{burgess1999} & $d' \in \{0{,}5; 1{,}0; 1{,}5; 2{,}2; 3{,}0; 4{,}0\}$ \\
    \addlinespace[0.4em]
    Figura 4.3 & $TTF(f; \Delta C)$ (Richard \& Samei) \cite{racine2020} & Iodo (+300 HU): $f_{50}=0{,}58\text{ mm}^{-1}, \alpha=3{,}2$; \\
    (Métricas Fourier) & $NPS(f) = A f \exp(-f^2/2\sigma_f^2)$ \cite{aapm_tg233_2019} & Solid Water (+25 HU): $f_{50}=0{,}35\text{ mm}^{-1}, \alpha=2{,}8$; \\
    & $E(f)$ (Burgess) \cite{burgess1999} & Burgess: $f_0=0{,}8\text{ cpd}, n=1{,}3, m=1{,}1, c=2{,}2$; \\
    & $W_{\text{task}}(f)$ (Bessel $J_1$) \cite{barrett_myers_2004} & Lesões esféricas: $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}, \Delta C = 35\text{ HU}$ \\
    \addlinespace[0.4em]
    SSW-$d'$ e SSDE & $\text{SSW-}d' = \frac{1}{I} \sum_{i} \sum_{j} \Omega_j d'_{i,j}$ \cite{fitton2026} & Diâmetros: $D_w \in \{16; 28; 38\}\text{ cm}$; \\
    (Tabela 4.2) & $\text{SSDE} = a e^{-b D_w} \text{CTDI}_{\text{vol}}$ \cite{aapm_report204} & Tarefas: $\Delta C_1 = 20\text{ HU} (\Omega_1=0{,}70), \Delta C_2 = 120\text{ HU} (\Omega_2=0{,}30)$; \\
    & $\text{FOM}_{\text{SSW}} = (\text{SSW-}d')^2 / \overline{\text{SSDE}}$ & Fator SSDE: $a = 3{,}704, b = 0{,}0367\text{ cm}^{-1}$ (ref. 32 cm) \\
    \addlinespace[0.4em]
    Figura 4.4 & $C_j(f) = e^{-\frac{f^2}{2\sigma_{j1}^2}} - e^{-\frac{f^2}{2\sigma_{j2}^2}}$ \cite{myers_barrett_1987} & 5 canais D-DOG: $f \in [0{,}10; 0{,}85]\text{ mm}^{-1}$; \\
    (Canais CHO) & $LG_n(r) = L_n(\frac{2\pi r^2}{a^2}) e^{-\frac{\pi r^2}{a^2}}$ \cite{gallas2003} & Laguerre-Gauss: $n \in \{0, 1, 2, 3\}, a = 4{,}0\text{ mm}$; \\
    & Gabor 2D ($\theta = 45^\circ$) \cite{barrett_myers_2004} & Gabor: $\sigma=3{,}5\text{ mm}, \lambda=5{,}0\text{ mm}, \gamma=0{,}75, \theta=45^\circ$ \\
    \addlinespace[0.4em]
    Figura 4.6 & $d'(\text{Dose}) \propto \text{Dose}^\beta$ \cite{racine2021} & FBP: $\beta = 0{,}50$; DLR: curva logística não linear; \\
    (DLR e Detrending) & $P_2(x, y) = \sum a_{ij} x^i y^j$ \cite{aapm_tg233_2019} & Detrending: ajuste polinomial 2D via Mínimos Quadrados \\
    \addlinespace[0.4em]
    Figura 4.9 & Variedade 3D $(D, T, -d')$ \cite{deb2002} & Otimização: NSGA-II (100 indivíduos, 200 gerações), \\
    (Pareto e TOPSIS) & Pareto não-dominada \cite{hwang1981} & Ranqueamento multicritério TOPSIS \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026).}
\end{table}

% ------------------------------------------------------------------------------
% CAPÍTULO 4: RESULTADOS E DISCUSSÃO
% ------------------------------------------------------------------------------
\chapter{Resultados e Discussão}
\label{chap:resultados_discussao}

Este capítulo apresenta os resultados consolidados da revisão bibliográfica sistemática e o desenvolvimento da modelagem teórico-metrológica. Inicia-se pela quantificação do fluxo de seleção documental segundo as diretrizes PRISMA 2020. Em seguida, expõem-se as deduções matemáticas fundamentais da Teoria de Detecção de Sinais e da metrologia espectral no domínio de Fourier, a formalização do Índice de Detectabilidade Ponderado por Tamanho e Tarefa (SSW-$d'$), a análise comparativa entre observadores clássicos e profundos, as causas do colapso dos modelos analíticos lineares sob reconstruções por aprendizado profundo e os fundamentos da tomografia por contagem de fótons. Cada dedução analítica é acompanhada de simulações numéricas originais codificadas em Python e de discussões analíticas aprofundadas focadas em problemas reais da prática clínica.

\section{Busca Sistemática (PRISMA 2020)}
\label{sec:resultados_prisma_detalhados}

A execução da estratégia de busca booleana descrita na \cref{sec:estrategia_busca_booleana_detalhada} e na \cref{tab:estrategia_booleana} resultou inicialmente na identificação de um total bruto de 1.206 registros distribuídos nas seis bases científicas consultadas: PubMed/MEDLINE ($n = 342$), Scopus ($n = 298$), Web of Science Core Collection ($n = 215$), IEEE Xplore Digital Library ($n = 187$) e repositórios técnicos da AAPM e SPIE ($n = 164$).

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.96\textwidth]{flow_prisma_flowchart.png}{Fluxograma PRISMA 2020 de Seleção dos Estudos.}
  \caption[Fluxograma PRISMA 2020 da Revisão]{Fluxograma PRISMA 2020 da Revisão Sistemática \cite{page2021}.}
  \label{fig:prisma_flowchart}
\end{figure}

Conforme ilustrado no fluxograma metodológico da \cref{fig:prisma_flowchart}, os 1.206 registros foram exportados para gerenciadores de referências bibliográficas, onde se procedeu à identificação e exclusão de 418 publicações duplicadas, restando 788 registros únicos para a etapa de triagem. A leitura independente de títulos e resumos levou à exclusão de 632 trabalhos que não atendiam ao escopo da pesquisa: 328 estudos focados exclusivamente em outras modalidades diagnósticas (ressonância magnética, ultrassonografia ou medicina nuclear pura), 214 artigos clínicos sem fundamentação física, dosimétrica ou metrológica e 90 resumos de conferências sem texto analítico integral.

Para a fase de avaliação de elegibilidade, recuperaram-se 156 artigos em texto completo. A leitura integral e a aplicação rigorosa dos critérios de elegibilidade documentados na \cref{tab:criterios_inclusao_exclusao} resultaram na exclusão de 118 publicações: 64 artigos por ausência de formalismo matemático compatível com SDT, óptica de Fourier ou observadores de modelo; 32 por duplicidade de dados em coortes já reportadas; e 22 por carência de dados de calibração física ou dosimétrica padronizada.

O corpus final incluído na síntese qualitativa e na modelagem teórico-metrológica foi constituído por 38 publicações fundamentais: 26 artigos originais e de revisão publicados em periódicos indexados com revisão por pares, 8 relatórios técnicos e documentos normativos de comissões internacionais e agências reguladoras (AAPM, ICRU, ICRP e ANVISA) e 4 obras seminais e livros-texto de física de imagens médicas.

\subsection{Avaliação Crítica de Risco de Viés e Certeza da Evidência do Corpus}
\label{subsec:avaliacao_qualidade_risco_vies_resultados}

Em conformidade com os Itens 11 e 22 das diretrizes PRISMA 2020 \cite{page2021}, procedeu-se à avaliação crítica sistemática da qualidade metodológica, do risco de viés e do nível de certeza epistêmica das 38 publicações que compõem o corpus analítico da revisão. 

A \cref{tab:avaliacao_risco_vies_corpus} sintetiza o julgamento estruturado conduzido para os subgrupos metodológicos do corpus.

\begin{table}[htbp]
  \centering
  \small
  \caption[Avaliação de Risco de Viés e Certeza da Evidência do Corpus]{Síntese da Avaliação Crítica de Risco de Viés e Certeza da Evidência (PRISMA 2020 / GRADE Adaptado) \cite{page2021, aapm_tg233_2019, icru54_1996, dorfman1992, fitton2026, aapm_report204}.}
  \label{tab:avaliacao_risco_vies_corpus}
  \renewcommand{\arraystretch}{1.30}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.18\textwidth} >{\RaggedRight}p{0.21\textwidth} >{\RaggedRight}p{0.21\textwidth} >{\centering\arraybackslash}p{0.12\textwidth} >{\RaggedRight\arraybackslash}X}
    \toprule
    \textbf{Tipologia Metodológica} & \textbf{Domínio Físico / Matemático} & \textbf{Domínio Psicofísico / Amostral} & \textbf{Risco Global de Viés} & \textbf{Certeza da Evidência} \\
    \midrule
    Documentos Normativos e Obras Seminais ($n = 12$) \cite{aapm_tg233_2019, icru54_1996, icrp103_2007, anvisa_rdc611_2022, barrett_myers_2004, wagner1979, burgess1994, metz1986, aapm_report204} &
    Deduções contínuas completas fundamentadas em primeiros princípios da teoria da decisão e óptica de Fourier. &
    Validação assintótica universal e consenso de comitês internacionais de física médica. &
    \textbf{Baixo} &
    \textbf{Alta}\newline (Padrão Teórico Normativo) \\
    \addlinespace[0.5em]
    Estudos Psicofísicos com Múltiplos Leitores (MRMC) ($n = 14$) \cite{racine2020, racine2021, solomon2020, greffier2026, pimenta2026, toia2023, debbiche2024, fitton2026, goppel2021} &
    Extração padronizada de $TTF(f)$, $NPS(f)$ e SSW-$d'$ com \emph{detrending} polinomial 2D rigoroso. &
    Testes 2AFC com $J \ge 4$ radiologistas, $K \ge 100$ casos, monitores GSDF calibrados e ANOVA DBM/HOR. &
    \textbf{Baixo a Moderado} &
    \textbf{Alta a Moderada}\newline (Evidência Experimental Robusta) \\
    \addlinespace[0.5em]
    Modelagens Numéricas e Observadores DLMO ($n = 8$) \cite{vaswani2017, dosovitskiy2020, toia2023, debbiche2024, myers_barrett_1987, gallas2003} &
    Implementação de canais corticais D-DOG/Gabor e auto-atenção multi-cabeça em Vision Transformers. &
    Simulações com $M \ge 100$ ROIs; correlações empíricas com humanos restritas a tarefas específicas. &
    \textbf{Moderado} &
    \textbf{Moderada}\newline (Evidência Exploratória / Piloto) \\
    \addlinespace[0.5em]
    Estudos Físicos e Clínicos em PCCT ($n = 4$) \cite{willemink2018, rajendran2021, mccollough2026, pimenta2026} &
    Modelagem de semicondutores CdTe/CZT, decomposição de bases e tensores de ruído multi-energia. &
    Validação em bancadas físicas e no sistema comercial pioneiro NAEOTOM Alpha (Siemens). &
    \textbf{Baixo a Moderado} &
    \textbf{Alta a Moderada}\newline (Tecnologia Clínica Emergente) \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026) com base nas diretrizes PRISMA 2020 \cite{page2021} e critérios GRADE adaptados \cite{aapm_tg233_2019, icru54_1996, dorfman1992}.}
\end{table}

A análise crítica da certeza epistêmica revela três nuances metodológicas determinantes para a interpretação dos resultados desta monografia:
\begin{enumerate}
  \item \textbf{Heterogeneidade Amostral entre Estudos:} Publicações pioneiras de validação psicofísica da DLR e do DLMO (como Racine et al. \cite{racine2021} e Toia et al. \cite{toia2023}) empregaram painéis qualificados de observadores humanos sob rigoroso controle psicofísico. No entanto, por se tratarem de estudos experimentais conduzidos em centros acadêmicos específicos com geometrias de simuladores selecionadas (ex.: fantomas antropomórficos de tórax e abdome), seus coeficientes numéricos de correlação devem ser interpretados como marcos conceituais demonstrativos, e não como constantes invariantes da física;
  \item \textbf{Risco de Sobreajuste em Observadores Profundos:} Nos estudos de observadores DLMO, identifica-se um risco potencial de viés de sobreajuste (*overfitting*) às texturas estocásticas dos simuladores físicos empregados no treinamento das redes Transformers. A generalização dessas métricas para a anatomia de pacientes reais e para tomógrafos de diferentes fabricantes demanda protocolos de calibração cruzada independente;
  \item \textbf{Certeza Diferenciada entre Teoria e Aplicação Clínica:} Enquanto o formalismo matemático de Fourier e a Teoria de Detecção de Sinais possuem certeza epistêmica máxima (Alta), a quantificação do ganho diagnóstico proporcionado por algoritmos DLR e sistemas PCCT varia entre Moderada e Alta dependendo da tarefa diagnóstica analisada (ex.: contraste alto vs. baixo, densidade do ruído anatômico circundante e regime de dose).
\end{enumerate}

\section{Teoria de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria_completa}

\subsection{Fundamentação da SDT: Hipóteses de Bayes, Regra de Neyman-Pearson e Modelagem de Decisão}
\label{subsec:sdt_fundamentacao_bayes_neyman}
A detecção de uma anormalidade patológica em uma imagem médica é formalmente descrita na física matemática como um problema de teste de hipóteses estatísticas sob ruído estocástico \cite{peterson1954, lusted1968, metz1986}. Na prática radiológica diária, a tarefa interpretativa do especialista consiste em perscrutar uma cena anatômica complexa e decidir se um determinado padrão de atenuação representa parênquima sadio ou uma lesão incipiente.

Considere uma imagem digital bidimensional discretizada e representada por um vetor lexicográfico $\mathbf{g} \in \mathbb{R}^N$, onde $N = N_x \times N_y$ é o número total de pixels. O problema clássico de detecção binária (conhecido na metrologia como paradigma SKE/BKS --- \emph{Signal Known Exactly / Background Known Statistically}) formula-se através de duas hipóteses estatísticas mutuamente exclusivas:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Sadio}) \label{eq:h0_def} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Patologia}) \label{eq:h1_def}
\end{align}
onde $\mathbf{s} \in \mathbb{R}^N$ é o vetor determinístico que descreve o perfil espacial do sinal da lesão e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo, caracterizado por valor esperado nulo $\langle \mathbf{b} \rangle = \mathbf{0}$ e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle \in \mathbb{R}^{N \times N}$.

O observador atua processando a imagem vetorial $\mathbf{g}$ por meio de um operador funcional contínuo, gerando uma estatística escalar de teste $t = t(\mathbf{g}) \in \mathbb{R}$. A decisão diagnóstica final é obtida pela comparação de $t$ com um limiar de corte pré-estabelecido $t_c$:
\begin{equation}
  \text{Decisão} = \begin{cases}
    H_1 (\text{Positivo / Lesão Presente}), & \text{se } t(\mathbf{g}) \ge t_c \\
    H_0 (\text{Negativo / Lesão Ausente}), & \text{se } t(\mathbf{g}) < t_c
  \end{cases}
  \label{eq:regra_decisao_sdt}
\end{equation}

Pelo Lema Fundamental de Neyman-Pearson, o teste estatístico ótimo que maximiza a probabilidade de detecção (Sensibilidade ou $TPF$) para uma taxa de falso alarme fixa ($FPF$) é dado pela Razão de Verossimilhança de Bayes (\emph{Likelihood Ratio}) $\Lambda(\mathbf{g})$ \cite{barrett_myers_2004}:
\begin{equation}
  \Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}
  \label{eq:razao_verossimilhanca}
\end{equation}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{fig1_sdt_roc_2afc.png}{Modelagem Numérica Sintética da Teoria de Detecção de Sinais, Curvas ROC e Desempenho 2AFC.}
  \caption[Modelagem SDT, Curvas ROC e 2AFC]{Modelagem da Teoria de Detecção de Sinais, Curvas ROC e 2AFC \cite{metz1986, barrett_myers_2004, burgess1999}.}
  \label{fig:sdt_roc_2afc}
\end{figure}

A modelagem gráfica apresentada na \cref{fig:sdt_roc_2afc} ilustra os três pilares operacionais da Teoria de Detecção de Sinais sintetizados computacionalmente a partir dos parâmetros formais da \cref{tab:parametros_simulacao}:
\begin{enumerate}
  \item Painel (A) --- Distribuições de Decisão da SDT sob Ruído:
  Modelaram-se duas variáveis aleatórias gaussianas contínuas $t_0 \sim \mathcal{N}(0, 1)$ e $t_1 \sim \mathcal{N}(2{,}2, 1)$ com desvio padrão unitário $\sigma_t = 1{,}0$, correspondendo a um índice de detectabilidade teórico $d' = (\mu_1 - \mu_0)/\sigma_t = 2{,}2$. Definiu-se um limiar de corte $t_c = 1{,}3$. As probabilidades operacionais foram calculadas analiticamente por integração cumulativa:
  \begin{equation}
    FPF(t_c) = \int_{t_c}^\infty p(t|H_0) \, dt = 1 - \Phi\left(\frac{t_c - \mu_0}{\sigma_t}\right) \approx 0{,}097 \quad (9{,}7\%)
  \end{equation}
  \begin{equation}
    TPF(t_c) = \int_{t_c}^\infty p(t|H_1) \, dt = 1 - \Phi\left(\frac{t_c - \mu_1}{\sigma_t}\right) \approx 0{,}816 \quad (81{,}6\%)
  \end{equation}

  \item Painel (B) --- Geração Paramétrica das Curvas ROC:
  Variou-se parametricamente o limiar $t_c \in [-4{,}0; +6{,}0]$ com incremento $\Delta t_c = 0{,}01$ para seis valores fixos de detectabilidade $d' \in \{0{,}5; 1{,}0; 1{,}5; 2{,}2; 3{,}0; 4{,}0\}$. Para cada par $(d', t_c)$, computaram-se os pontos $(FPF(t_c), TPF(t_c))$, gerando as trajetórias contínuas no espaço ROC e confirmando a relação analítica $AUC = \Phi(d' / \sqrt{2})$;

  \item Painel (C) --- Curva de Desempenho no Paradigma 2AFC:
  Plotou-se a probabilidade teórica de acerto em função do índice $d'$ avaliando a função sigmoidal $P_C(d') = \Phi(d' / \sqrt{2})$ no domínio $d' \in [0, 5]$. A curva demonstra que regimes de baixa detectabilidade ($d' \approx 1{,}0$) limitam a acurácia a $P_C \approx 76\%$, enquanto sistemas que satisfazem o Critério de Rose ($d' \ge 4{,}0$) garantem certeza visual diagnóstica ($P_C \ge 99{,}8\%$).
\end{enumerate}

Em termos de impacto na qualidade interpretativa da imagem médica, a SDT estabelece que o desempenho diagnóstico do médico radiologista não pode ser medido apenas pela acurácia percentual isolada, pois esta depende do limiar subjetivo de corte $t_c$. Ao separar formalmente a capacidade discriminativa intrínseca do sistema físico (representada pelo afastamento entre as curvas de decisão) da atitude decisória do leitor (posição de $t_c$), a SDT fornece a base matemática rigorosa para quantificar a eficácia de novas tecnologias tomográficas.

\noindent\textbf{Resumo de Impactos, Vantagens e Limitações:}
\begin{itemize}[leftmargin=*,noitemsep]
  \item \emph{Impacto Metrológico:} Transforma a avaliação da imagem médica de uma análise subjetiva qualitativa para uma medição objetiva baseada na física estatística de detecção.
  \item \emph{Vantagens sobre Métricas Tradicionais:} Desacopla o viés decisório do especialista da qualidade física da imagem; relaciona diretamente grandezas estocásticas com as probabilidades clínicas reais de sensibilidade ($TPF$) e falso-positivo ($FPF$).
  \item \emph{Limitações do Modelo:} A formulação clássica SKE/BKS assume que a lesão tem forma e contraste perfeitamente conhecidos pelo observador e que o ruído de fundo é gaussiano estacionário, premissas que se tornam limitadas diante de patologias polimórficas reais.
\end{itemize}

\subsection{Dedução do Índice de Detectabilidade (\texorpdfstring{$d'$}{d'}), Escalonamento com a Dose e Aplicação no Rastreamento Pulmonar}
\label{subsec:deducao_formal_dprime_e_escalonamento_dose}
O Índice de Detectabilidade ($d'$) expressa a distância estatística normalizada entre os valores esperados da variável de decisão sob as duas hipóteses clínicas, quantificando o quão separáveis são as distribuições de tecido sadio e patológico \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_definicao_geral}
\end{equation}

Para qualquer observador linear operando no espaço discreto por produto escalar $t(\mathbf{g}) = \mathbf{w}^T \mathbf{g}$, onde $\mathbf{w} \in \mathbb{R}^N$ é o vetor de pesos (\emph{template} do observador):
\begin{align}
  \langle t | H_0 \rangle &= \mathbf{w}^T \langle \mathbf{b} \rangle = 0 \label{eq:esperanca_h0} \\
  \langle t | H_1 \rangle &= \mathbf{w}^T (\mathbf{s} + \langle \mathbf{b} \rangle) = \mathbf{w}^T \mathbf{s} \label{eq:esperanca_h1}
\end{align}
Assumindo que o ruído é estacionário com matriz de covariância $\mathbf{K}$, a variância é idêntica sob ambas as hipóteses:
\begin{equation}
  \sigma^2(t) = \langle (\mathbf{w}^T \mathbf{b})^2 \rangle = \mathbf{w}^T \langle \mathbf{b} \mathbf{b}^T \rangle \mathbf{w} = \mathbf{w}^T \mathbf{K} \mathbf{w}
  \label{eq:variancia_linear}
\end{equation}
Substituindo as \cref{eq:esperanca_h0,eq:esperanca_h1,eq:variancia_linear} na \cref{eq:dprime_definicao_geral}, obtém-se a equação fundamental do índice de detectabilidade para qualquer observador linear discreto:
\begin{equation}
  d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}
  \label{eq:dprime_linear_fundamental}
\end{equation}

A conexão direta entre o formalismo da SDT e a física radiológica inicia-se na atenuação exponencial de fótons X regida pela Lei de Beer-Lambert generalizada (\cref{eq:beer_lambert}). Em um feixe estreito, o número de fótons transmitidos e detectados em um canal de projeção $i$ segue a estatística de contagem de Poisson:
\begin{equation}
  N_i \sim \text{Poisson}(\bar{N}_i), \quad \text{com } \bar{N}_i = N_{0,i} \exp\left(-\int_{L_i} \mu(x,y,z; E) \, dl\right)
  \label{eq:poisson_transmissao}
\end{equation}
onde a variância da contagem fotônica bruta é estritamente igual à sua média ($\sigma_{N_i}^2 = \bar{N}_i$). Ao calcular o logaritmo da atenuação para formar o sinograma $p(r, \phi) = \ln(N_{0,i} / N_i)$, a propagação de erros pelo método de Taylor de primeira ordem revela que a variância do sinograma é inversamente proporcional ao fluxo de fótons:
\begin{equation}
  \sigma_p^2 \approx \left| \frac{\partial p}{\partial N_i} \right|^2 \sigma_{N_i}^2 = \frac{1}{\bar{N}_i}
  \label{eq:variancia_sinograma}
\end{equation}

A reconstrução analítica via FBP (\cref{eq:fbp_formula}) atua como um operador linear integral que mapeia o ruído estocástico das projeções para o espaço de imagens. Como a fluência total de fótons é linearmente proporcional à carga elétrica acumulada pelo tubo ($\text{mAs}$) e ao Índice de Dose em Tomografia ($\text{CTDI}_{\text{vol}}$, \cref{eq:ctdi_vol}), a variância do ruído no espaço da imagem reconstruída escala como $\sigma_{\text{HU}}^2 \propto 1 / \text{CTDI}_{\text{vol}}$. Inserindo essa dependência na \cref{eq:dprime_linear_fundamental}, estabelece-se a relação analítica fundamental da FBP clássica:
\begin{equation}
  d' \propto \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{1 / \text{CTDI}_{\text{vol}}}} \implies d' \propto \sqrt{\text{CTDI}_{\text{vol}}}
  \label{eq:escalonamento_dprime_dose}
\end{equation}

Essa dedução demonstra a raiz física do princípio ALARA (\cref{sec:paradigma_dosimetrico}): qualquer redução deliberada de dose em sistemas lineares implica necessariamente a degradação quadrática da detectabilidade diagnóstica $d'$.

A relevância clínica direta dessa relação manifesta-se em tarefas sensíveis como o rastreamento populacional de câncer de pulmão através de tomografia computadorizada de baixa dose (\emph{Low-Dose CT} --- LDCT). No cenário de triagem pulmonar, o objetivo primário consiste na detecção de nódulos subsólidos ou com atenuação em vidro fosco com diâmetros entre 4 e 8 mm.

Fisicamente, o parênquima pulmonar sadio é composto predominantemente por ar alveolar e septos capilares finos, apresentando densidade média de aproximadamente $-800\text{ HU}$. Um adenocarcinoma inicial manifesta-se tipicamente como uma lesão de vidro fosco com densidade sutil de $-600\text{ a } -650\text{ HU}$, gerando uma diferença de contraste extremamente tênue de $\Delta C \approx 150\text{ a } 200\text{ HU}$ contra o tecido aerado, porém com bordas mal delimitadas e densidade heterogênea. Em protocolos de ultrabaixa dose, onde o $\text{CTDI}_{\text{vol}}$ é reduzido para a faixa de $0{,}8\text{ a } 1{,}5\text{ mGy}$ (em conformidade com o princípio ALARA e a RDC ANVISA 611/2022), o ruído estocástico $\sigma_{\text{HU}}$ na FBP eleva-se para níveis próximos a $40\text{ a } 50\text{ HU}$.

Sob essas condições, a distância entre as distribuições $p(t|H_0)$ e $p(t|H_1)$ encurta-se significativamente, reduzindo o índice de detectabilidade para $d' \approx 1{,}2$. Como demonstrado no Painel (A) da \cref{fig:sdt_roc_2afc}, uma redução de $d'$ para a faixa próxima a 1,0 força o médico radiologista a um dilema psicofísico insolúvel através do ajuste do limiar $t_c$:
\begin{enumerate}
  \item Se o especialista adota uma postura conservadora para evitar biópsias desnecessárias e ansiedade no paciente (deslocando $t_c$ para a direita, $t_c = 1{,}8$), a taxa de falsos alarmes ($FPF$) cai para $3{,}6\%$, porém a sensibilidade de detecção ($TPF$) colapsa para menos de $50\%$, resultando na perda diagnóstica de tumores malignos em estágio inicial curável;
  \item Se o especialista adota uma postura intervencionista agressiva (deslocando $t_c$ para a esquerda, $t_c = 0{,}6$), a sensibilidade atinge $80\%$, mas a taxa de falso alarme dispara para mais de $27\%$, sobrecarregando o sistema de saúde com investigações invasivas e custos desnecessários.
\end{enumerate}

Essa problematização evidencia que o desempenho diagnóstico na tarefa do radiologista não pode ser otimizado apenas pelo critério subjetivo do observador humano, mas exige da física médica a maximização intrínseca do índice $d'$ do sistema formador de imagens.

\noindent\textbf{Resumo de Impactos, Vantagens e Limitações:}
\begin{itemize}[leftmargin=*,noitemsep]
  \item \emph{Impacto Metrológico:} Formaliza o $d'$ como a métrica escalar unificada de desempenho diagnóstico em tarefas de decisão binária, conectando diretamente a dose absorvida à probabilidade de acerto.
  \item \emph{Vantagens sobre Métricas Anteriores:} Substitui o $SNR$ e $CNR$ pontuais por uma grandeza que pondera a geometria completa do sinal ($\mathbf{s}$) contra a matriz de covariância do ruído ($\mathbf{K}$).
  \item \emph{Limitações do Modelo:} O escalonamento linear $d' \propto \sqrt{\text{CTDI}_{\text{vol}}}$ é estritamente válido apenas para a FBP; sob algoritmos não-lineares (DLR/MBIR), essa proporcionalidade colapsa, exigindo a metrologia espectral contínua e observadores avançados.
\end{itemize}

\section{Métricas Espectrais em Fourier (AAPM TG-233)}
\label{sec:metricas_espectrais_fourier_completas}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{fig2_spectral_metrics.png}{Modelagem Numérica Sintética das Quatro Funções Espectrais segundo AAPM TG-233.}
  \caption[Métricas Espectrais em Fourier]{Métricas Espectrais em Frequência segundo AAPM TG-233 \cite{aapm_tg233_2019, racine2020, burgess1999}.}
  \label{fig:spectral_metrics}
\end{figure}

As quatro funções analíticas no domínio de Fourier simuladas na \cref{fig:spectral_metrics} integram o núcleo da metrologia baseada em tarefa segundo as diretrizes do relatório AAPM TG-233 \cite{aapm_tg233_2019}:

\begin{enumerate}
  \item Painel (A) --- Resolução Espacial da Tarefa $TTF(f)$:
  Modelou-se a resposta em frequência via função sigmoidal generalizada de Richard \& Samei \cite{racine2020}:
  \begin{equation}
    TTF(f; \Delta C) = \left[ 1 + \left( \frac{f}{f_{50}(\Delta C)} \right)^\alpha \right]^{-1}
  \end{equation}
  onde para alto contraste (Iodo $+300\text{ HU}$, curva vermelha), calibrou-se $f_{50} = 0{,}58\text{ mm}^{-1}$ e $\alpha = 3{,}2$; para baixo contraste (Solid Water $+25\text{ HU}$, curva ciano), calibrou-se $f_{50} = 0{,}35\text{ mm}^{-1}$ e $\alpha = 2{,}8$, evidenciando o borramento não linear de alvos sutis;

  \item Painel (B) --- Espectro de Potência do Ruído $NPS(f)$:
  Modelou-se o espectro de ruído da FBP clássica pela lei de potência filtrada $NPS_{\text{FBP}}(f) = A \cdot f \cdot \exp(-f^2 / 2\sigma_f^2)$ com $f_{\text{peak}} = 0{,}45\text{ mm}^{-1}$ (curva preta). A curva DLR (verde) foi modelada com redução de 50\% na potência integrada e preservação do pico textural em $0{,}40\text{ mm}^{-1}$. A curva MBIR (roxa) foi gerada deslocando a variância para baixas frequências ($f_{\text{peak}} = 0{,}18\text{ mm}^{-1}$), ilustrando a textura cerosa (\emph{plastic look});

  \item Painel (C) --- Filtro Ocular Humano $E(f)$:
  Calculou-se a função de sensibilidade ao contraste de Burgess \cite{burgess1999} através de:
  \begin{equation}
    E(f) = \left( \frac{f}{f_0} \right)^n \exp\left[ -c \left( \frac{f}{f_0} \right)^m \right]
    \label{eq:filtro_ocular_burgess}
  \end{equation}
  com parâmetros $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$, convertendo frequências espaciais físicas para a retina sob distância de visualização de 50 cm ($f_{\text{retina}} \approx 8{,}727 \cdot f$), com pico ótimo em $4{,}2\text{ cpd}$;

  \item Painel (D) --- Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$:
  Computou-se a Transformada de Fourier analítica de lesões esféricas de raio $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}$ e contraste $\Delta C = 35\text{ HU}$ avaliando a função de Bessel de primeira ordem via:
  \begin{equation}
    W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi f R)}{2\pi f R} \right|
    \label{eq:wtask_bessel_formula}
  \end{equation}
  A simulação evidencia que lesões extensas concentram energia em $f < 0{,}15\text{ mm}^{-1}$, enquanto microlesões espalham energia para frequências superiores a $0{,}6\text{ mm}^{-1}$.
\end{enumerate}

\subsection{Dedução Analítica das Quatro Funções Espectrais (\texorpdfstring{$TTF$, $NPS$, $E(f)$, $W_{\text{task}}$}{TTF, NPS, E(f), Wtask}) e Origem Física do Ruído}
\label{subsec:deducoes_passo_passo_quatro_funcoes_unificado}
A formalização matemática contínua das quatro funções espectrais e o entendimento da sua influência na qualidade interpretativa da imagem constituem o alicerce metodológico do relatório AAPM TG-233 \cite{aapm_tg233_2019}:

\subsubsection{1. Função de Transferência da Tarefa (\texorpdfstring{$TTF(f)$}{TTF(f)})}
A partir da imagem de um inserto cilíndrico de calibração de raio $R_0$ e centro $(x_c, y_c)$, calcula-se a distância euclidiana radial de cada pixel $r = \sqrt{(x - x_c)^2 + (y - y_c)^2}$. Agrupando os pixels em caixas infinitesimais de raio $dr$, constrói-se a Função de Resposta ao Degrau superamostrada $\text{ESF}(r)$. A Função de Espalhamento de Linha $\text{LSF}(r)$ é obtida pela derivada espacial negativa:
\begin{equation}
  \text{LSF}(r) = -\frac{d}{dr} \text{ESF}(r)
  \label{eq:lsf_derivada}
\end{equation}
A Transformada de Fourier unidimensional contínua normalizada da $\text{LSF}(r)$ define a $TTF(f)$ \cite{aapm_tg233_2019, racine2020}:
\begin{equation}
  TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \text{LSF}(r) \, dr}
  \label{eq:ttf_integral_deducao}
\end{equation}
\textbf{Impacto na Qualidade da Imagem e na Tarefa do Radiologista:} Diferente da $MTF$ clássica que assume linearidade e mede apenas alvos de alto contraste, a $TTF(f; \Delta C)$ quantifica como a resolução varia dinamicamente em função do contraste específico da patologia. Para alvos de baixo contraste (como metástases hepáticas ou lesões isquêmicas), a queda do descritor $f_{50}$ (frequência na qual $TTF = 50\%$) reflete diretamente o borramento das bordas da lesão, reduzindo a nitidez de transição entre o tumor e o parênquima sadio e aumentando a incerteza do radiologista na delimitação cirúrgica de margens.

\subsubsection{2. Espectro de Potência do Ruído (\texorpdfstring{$NPS(f)$}{NPS(f)}) e Origem Física de Rampa}
Para extrair o ruído estocástico puro sem contaminação por gradientes anatômicos macroscópicos, aplica-se em cada ROI homogênea $k$ ($k = 1, \dots, M$) um detrending polinomial bidimensional de 2ª ordem $P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 xy + a_5 y^2$, resultando no ruído residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$.

Pelo Teorema de Wiener-Khinchin, o espectro bidimensional $NPS(u, v)$ é a Transformada de Fourier da função de autocovariância \cite{aapm_tg233_2019}:
\begin{equation}
  NPS(u, v) = \lim_{M \to \infty} \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, w(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
  \label{eq:nps_2d_formula}
\end{equation}
onde $w(x, y)$ é a janela de Hanning aplicada para evitar vazamento espectral (\emph{spectral leakage}) e $\Delta x, \Delta y$ são os tamanhos físicos do pixel em mm, resultando na unidade $\text{HU}^2 \cdot \text{mm}^2$. A curva radial isotrópica $NPS(f)$ é obtida por integração azimutal:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial_integral}
\end{equation}

A forma matemática característica do $NPS_{\text{FBP}}(f)$ decorre diretamente do Teorema da Fatia Central (\cref{eq:fourier_slice}) e do filtro de rampa $|f|$ da FBP (\cref{eq:fbp_formula}). Considerando que o ruído quântico de Poisson nas projeções não filtradas é aproximadamente branco com variância $S_0$, a retroprojeção contínua filtrada resulta na Lei de Wagner-Brown-Metz \cite{wagner1979, barrett_myers_2004}:
\begin{equation}
  NPS_{\text{FBP}}(f) = \frac{\pi}{N_{\text{proj}} \bar{\Phi}} |f| \cdot MTF^2(f)
  \label{eq:wagner_brown_metz}
\end{equation}
onde $\bar{\Phi}$ é a fluência fotônica média. A \cref{eq:wagner_brown_metz} elucida por que o ruído na FBP é nulo na origem ($NPS(0)=0$), cresce linearmente com a frequência espacial impulsionado pelo Jacobiano polar da reconstrução e decai em altas frequências ($f > 0{,}4\text{ mm}^{-1}$) pela abertura do detector, criando o pico textural em $f_{\text{peak}} \approx 0{,}45\text{ mm}^{-1}$.

\textbf{Impacto na Qualidade da Imagem e na Tarefa do Radiologista:} O $NPS(f)$ não mede apenas a magnitude do ruído (área sob a curva, correspondente à variância $\sigma_{\text{HU}}^2$), mas define a sua textura perceptual. O deslocamento do pico $f_{\text{peak}}$ para baixas frequências (comum em filtros iterativos agressivos) transforma a granulação fina clássica da FBP em manchas amorfas e cerosas, que interferem negativamente na busca visual foveal do especialista e mimetizam lesões teciduais.

\subsubsection{3. Filtro Ocular Humano (\texorpdfstring{$E(f)$}{E(f)}) e Sensibilidade Contrastiva da Retina}
O sistema visual humano não responde com ganho constante a todas as frequências espaciais. A Função de Sensibilidade ao Contraste (CSF) modelada por Burgess \cite{burgess1999} (\cref{eq:filtro_ocular_burgess}) descreve o comportamento passa-faixa do olho humano, apresentando sensibilidade máxima em torno de $4\text{ cpd}$ (ciclos por grau de ângulo visual), decaindo tanto para baixas frequências (devido à inibição lateral na retina) quanto para altas frequências (devido à difração óptica e espaçamento dos fotorreceptores).

\textbf{Impacto na Qualidade da Imagem e na Tarefa do Radiologista:} Para uma distância padrão de leitura de laudos a 50 cm, o pico de sensibilidade visual situa-se exatamente em frequências espaciais físicas da imagem em torno de $0{,}10\text{ a }0{,}15\text{ mm}^{-1}$. Quando os algoritmos de redução de ruído concentram potência residual exatamente nessa faixa de baixa frequência, o ruído residual torna-se hiper-conspícuo para o radiologista, gerando a sensação desconfortável de imagem "plastificada" e diminuindo a confiança diagnóstica.

\subsubsection{4. Espectro da Tarefa Diagnóstica (\texorpdfstring{$W_{\text{task}}(f)$}{Wtask(f)})}
O espectro da tarefa (\cref{eq:wtask_bessel_formula}) quantifica a distribuição da energia do sinal anatômico no espaço de Fourier em função da geometria e do contraste da patologia pesquisada. Lesões extensas concentram quase toda a sua energia em baixas frequências ($f < 0{,}15\text{ mm}^{-1}$), enquanto estruturas diminutas (como microcalcificações coronarianas ou espículas trabeculares) possuem seu conteúdo informacional primário em frequências ultra-altas ($f > 0{,}60\text{ mm}^{-1}$).

\textbf{Impacto na Qualidade da Imagem e na Tarefa do Radiologista:} O $W_{\text{task}}(f)$ atua como uma função de ponderação clínica sobre o tomógrafo. Ele demonstra que não existe uma "qualidade de imagem absoluta": um protocolo tomográfico que maximiza a detecção de um nódulo hepático volumoso (favorecendo baixas frequências) pode degradar de forma catastrófica a visualização de uma microfratura óssea, exigindo calibrações de filtros customizadas para a tarefa médica pretendida.

\noindent\textbf{Resumo de Impactos, Vantagens e Limitações:}
\begin{itemize}[leftmargin=*,noitemsep]
  \item \emph{Impacto Metrológico:} Substitui medições pontuais simplistas por uma descrição espectral contínua bidimensional completa da resolução ($TTF$), textura do ruído ($NPS$), percepção humana ($E(f)$) e patologia clínica ($W_{\text{task}}$).
  \item \emph{Vantagens sobre Métricas Anteriores:} Permite prever com exatidão física como diferentes algoritmos de reconstrução afetam patologias com contrastes e dimensões distintas.
  \item \emph{Limitações do Modelo:} A medição experimental de $TTF(f)$ e $NPS(f)$ exige fantomas de calibração dedicados com insertos específicos e processamento computacional rigoroso para evitar artefatos de amostragem.
\end{itemize}

\subsection{Integração Espectral e Discussão Clínica: Metástases Hepáticas Hipoatenuantes}
\label{subsec:integracao_espectral_e_discussao_clinica_figado}
A integração harmoniosa das quatro funções no domínio contínuo de Fourier bidimensional resulta no cálculo objetivo do índice de detectabilidade espectral da tarefa $d'$:
\begin{equation}
  d'^2 = \int_0^{\infty} \frac{\left[ TTF(f; \Delta C) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2}{NPS(f)} f \, df
  \label{eq:dprime_espectral_integracao_aapm}
\end{equation}

A dependência não linear da resolução espacial expressa na $TTF(f; \Delta C)$ introduz repercussões clínicas graves no estadiamento oncológico de tumores gastrointestinais e colorretais, cuja rota primária de disseminação hematogênica é o parênquima hepático.

Em uma tomografia de abdome contrastada na fase portal (70 a 80 segundos após a injeção do meio de contraste iodado), o parênquima hepático normal realça intensamente, atingindo valores médios entre $100\text{ e } 120\text{ HU}$. As metástases hepáticas iniciais de adenocarcinoma colorretal caracterizam-se por hipovascularização, mantendo atenuação de $75\text{ a } 85\text{ HU}$. O contraste alvo-fundo resultante é sutilíssimo, limitando-se a $\Delta C \approx 15\text{ a } 25\text{ HU}$.

Quando esse exame é reconstruído por algoritmos DLR ou MBIR com filtros de alta agressividade para redução de dose, a rede neural interpreta incorretamente a sutil transição de borda da lesão hipoatenuante de $5\text{ mm}$ como flutuação estocástica de ruído, aplicando regularização de suavização. Conforme demonstrado numericamente no Painel (A) da \cref{fig:spectral_metrics}, a frequência de corte $f_{50}$ da $TTF(f)$ para alvos de baixo contraste ($+25\text{ HU}$) sofre uma queda drástica de $0{,}58\text{ mm}^{-1}$ para $0{,}35\text{ mm}^{-1}$, acompanhada por uma perda acentuada de energia em frequências acima de $0{,}30\text{ mm}^{-1}$.

Ao cruzar essa perda de resolução com o espectro da tarefa diagnóstica $W_{\text{task}}(f)$ de uma lesão esférica de raio $R = 2{,}5\text{ mm}$ (Painel D da \cref{fig:spectral_metrics}), observa-se que a energia do sinal da metástase situa-se exatamente na banda de transição de $0{,}20\text{ a } 0{,}50\text{ mm}^{-1}$. O resultado clínico na rotina interpretativa do radiologista é o apagamento das margens tumorais e a perda de conspicuidade da lesão, que passa a se fundir visualmente ao parênquima circundante, levando a diagnósticos falso-negativos de metástases ressecáveis e comprometendo a sobrevida do paciente oncológico.

\noindent\textbf{Resumo de Impactos, Vantagens e Limitações:}
\begin{itemize}[leftmargin=*,noitemsep]
  \item \emph{Impacto Metrológico:} A formulação integrada do $d'$ segundo o relatório AAPM TG-233 captura com precisão o colapso da detectabilidade de lesões hipoatenuantes que passaria despercebido por métricas puramente escalares ($SNR/CNR$).
  \item \emph{Vantagens sobre Métricas Anteriores:} Evita a superestimação perigosa da qualidade de imagem sob reconstruções não lineares adaptativas, oferecendo um guia seguro para a redução de dose hospitalar.
  \item \emph{Limitações do Modelo:} A integração contínua assume simetria radial isotrópica e não modela a correlação em canais orientados do córtex visual, exigindo os observadores antropomórficos CHO para fundos anatômicos complexos.
\end{itemize}

\subsection{O Índice de Detectabilidade Ponderado pelo Tamanho do Paciente e Tarefa (SSW-\texorpdfstring{$d'$}{d'})}
\label{subsec:ssw_dprime_completo}

\subsubsection{Motivação Física, Biológica e Metrológica}
Embora a formulação contínua do índice de detectabilidade $d'$ padronizada pelo relatório AAPM TG-233 (\cref{eq:dprime_espectral_integracao_aapm}) represente um avanço estrutural frente às métricas escalares clássicas, a sua aplicação metrológica convencional padece de uma limitação fundamental: o cálculo de $d'$ é classicamente conduzido em um \emph{único} simulador físico cilíndrico de dimensões fixas (por exemplo, no módulo de baixo contraste do fantoma de acrílico de $20\text{ cm}$ ou $30\text{ cm}$ de diâmetro) e para um \emph{único} nível de contraste nominal $\Delta C$ \cite{aapm_tg233_2019, fitton2026}.

Na rotina hospitalar real, contudo, a física da formação da imagem e a tomada de decisão médica operam sob condições acentuadamente heterogêneas:
\begin{enumerate}
  \item \textbf{Ampla Variabilidade Biométrica dos Pacientes:} A atenuação radiológica total ao longo da trajetória $L$ (\cref{eq:beer_lambert}) é exponencialmente governada pela espessura e densidade do paciente. Em termos metrológicos padronizados pela AAPM (Relatórios nº 204 e 220) \cite{aapm_report204}, o porte anatômico é quantificado pelo Diâmetro Equivalente em Água ($D_w$), o qual varia amplamente em uma coorte clínica: desde $D_w \sim 12\text{ a } 18\text{ cm}$ em recém-nascidos e crianças pequenas, passando por $D_w \sim 24\text{ a } 29\text{ cm}$ em adultos eutróficos padrão, até $D_w \sim 35\text{ a } 48\text{ cm}$ em pacientes com obesidade severa ou mórbida;
  \item \textbf{Coexistência de Múltiplas Tarefas Clínicas no Mesmo Protocolo:} Um exame tomográfico de rotina (ex.: TC de abdome e pelve com contraste) não é realizado para responder a uma única pergunta binária. O radiologista deve, simultaneamente, detectar lesões hepáticas hipoatenuantes sutis ($\Delta C \sim 15\text{ a } 25\text{ HU}$, dominadas por ruído e baixas frequências espaciais) e avaliar o realce de ramos vasculares e lesões hipervasculares ($\Delta C \sim 100\text{ a } 150\text{ HU}$, governadas por resolução de bordas e altas frequências);
  \item \textbf{Modulação Dinâmica de Exposição (ATCM / AEC):} Os tomógrafos modernos modulam continuamente a corrente do tubo ($\text{mA}(z, \phi)$) e, em modelos recentes, selecionam automaticamente a tensão do tubo ($\text{kVp}$) em função da atenuação do paciente. Consequentemente, o espectro de ruído $NPS(f)$ e a resposta de resolução $TTF(f)$ variam drasticamente de um porte físico para outro, de modo que a avaliação em um único tamanho de simulador introduz viés metrológico inaceitável.
\end{enumerate}

Para superar esse hiato e fornecer uma métrica unificada aplicável à otimização de protocolos populacionais, desenvolveu-se o formalismo do Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa (\emph{Size-Specific Weighted Detectability Index} --- SSW-$d'$) \cite{fitton2026, goppel2021}.

\subsubsection{Dedução Matemática Completa do SSW-\texorpdfstring{$d'$}{d'}}
Considere uma amostragem discreta de $I$ simuladores físicos (ou tiers de tamanho de pacientes) caracterizados por diâmetros equivalentes em água $D_{w,i}$ ($i = 1, 2, \dots, I$), abrangendo o espectro anatômico de interesse (ex.: simuladores cilíndricos com $D_w \in \{16, 22, 28, 36\}\text{ cm}$).

Considere, adicionalmente, um conjunto de $J$ tarefas diagnósticas representativas do protocolo clínico, cada qual caracterizada por um nível de contraste $\Delta C_j$, geometria de lesão $W_{\text{task}, j}(f)$ e peso de relevância clínica $\Omega_j \in [0, 1]$ ($j = 1, 2, \dots, J$), sob a condição estrita de normalização:
\begin{equation}
  \sum_{j=1}^J \Omega_j = 1, \quad \text{com } \Omega_j \ge 0
  \label{eq:normalizacao_pesos_clinicos}
\end{equation}

Para cada combinação de tamanho $i$ e tarefa $j$, calcula-se o índice de detectabilidade elementar $d'_{i,j} = d'(D_{w,i}, \Delta C_j)$ integrando as funções espectrais medidas sob a modulação automática de exposição representativa daquele diâmetro:
\begin{equation}
  (d'_{i,j})^2 = \int_0^{\infty} \frac{\left[ TTF(f; \Delta C_j, D_{w,i}) \right]^2 \left[ W_{\text{task}, j}(f) \right]^2 \left[ E(f) \right]^2}{NPS(f; D_{w,i})} f \, df
  \label{eq:dprime_elementar_ij}
\end{equation}

O Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa ($\text{SSW-}d'$) é formalmente definido como a média aritmética da detectabilidade clínica composta através de todos os portes físicos amostrados \cite{fitton2026}:
\begin{equation}
  \text{SSW-}d' = \frac{1}{I} \sum_{i=1}^I \left( \sum_{j=1}^J \Omega_j \, d'_{i,j} \right) = \frac{1}{I} \sum_{i=1}^I \sum_{j=1}^J \Omega_j \, d'(D_{w,i}, \Delta C_j)
  \label{eq:ssw_dprime_discreto}
\end{equation}

\paragraph{Formulação Populacional Contínua:} Quando a distribuição antropométrica de uma coorte hospitalar é modelada por uma função densidade de probabilidade contínua de diâmetros corporais $p(D_w)$ definida no intervalo $[D_{w,\min}, D_{w,\max}]$ (satisfazendo $\int p(D_w) \, dD_w = 1$), a \cref{eq:ssw_dprime_discreto} generaliza-se na forma integral contínua:
\begin{equation}
  \text{SSW-}d' = \int_{D_{w,\min}}^{D_{w,\max}} p(D_w) \left[ \sum_{j=1}^J \Omega_j \, d'(D_w, \Delta C_j) \right] dD_w
  \label{eq:ssw_dprime_continuo}
\end{equation}

\subsubsection{Acoplamento com a Dose Específica por Tamanho (SSDE) e Figura de Mérito (\texorpdfstring{$\text{FOM}_{\text{SSW}}$}{FOM_SSW})}
A grande potência metrológica do SSW-$d'$ reside em sua capacidade de acoplamento direto com a dosimetria física individualizada. Enquanto o $\text{CTDI}_{\text{vol}}$ (\cref{eq:ctdi_vol}) expressa a dose absorvida em um cilindro rígido de PMMA de 32 cm, a dose real absorvida no centro do paciente varia exponencialmente com seu diâmetro $D_w$. 

Segundo as diretrizes do Relatório AAPM 204 \cite{aapm_report204}, a Estimativa de Dose Específica por Tamanho ($\text{SSDE}$, em mGy) é obtida por:
\begin{equation}
  \text{SSDE}(D_w) = f_{\text{size}}(D_w) \cdot \text{CTDI}_{\text{vol}}
  \label{eq:ssde_formula}
\end{equation}
onde $f_{\text{size}}(D_w)$ é o fator de conversão exponencial padronizado:
\begin{equation}
  f_{\text{size}}(D_w) = a \cdot \exp(-b \cdot D_w)
  \label{eq:fator_conversao_tamanho}
\end{equation}
com coeficientes $a = 3{,}704$ e $b = 0{,}0367\text{ cm}^{-1}$ para simuladores de corpo de 32 cm de referência \cite{aapm_report204}. Para pacientes pediátricos ($D_w = 16\text{ cm}$), o fator é $f_{\text{size}} \approx 2{,}06$, indicando que a dose real no órgão é mais que o dobro do $\text{CTDI}_{\text{vol}}$ indicado no console; para pacientes obesos ($D_w = 38\text{ cm}$), $f_{\text{size}} \approx 0{,}92$.

A dose média populacional específica da coorte $\overline{\text{SSDE}}$ é dada por:
\begin{equation}
  \overline{\text{SSDE}} = \frac{1}{I} \sum_{i=1}^I \text{SSDE}(D_{w,i}) = \frac{1}{I} \sum_{i=1}^I f_{\text{size}}(D_{w,i}) \cdot \text{CTDI}_{\text{vol}}(D_{w,i})
  \label{eq:ssde_medio_coorte}
\end{equation}

Unificando a qualidade de imagem diagnóstica em nível populacional com a dosimetria física real, define-se a \textbf{Figura de Mérito de Eficiência Dosimétrica Populacional} ($\text{FOM}_{\text{SSW}}$, expressa em $\text{mGy}^{-1}$) \cite{fitton2026}:
\begin{equation}
  \text{FOM}_{\text{SSW}} = \frac{(\text{SSW-}d')^2}{\overline{\text{SSDE}}}
  \label{eq:fom_ssw_formula}
\end{equation}

A grandeza $\text{FOM}_{\text{SSW}}$ estabelece o critério metrológico objetivo supremo para a otimização de protocolos em serviços de radiologia: um novo protocolo, algoritmo DLR ou seleção de kVp é estritamente superior se e somente se elevar o valor de $\text{FOM}_{\text{SSW}}$, significando que produz maior detectabilidade diagnóstica média ponderada por unidade de dose absorvida real entregue à população de pacientes.

\subsubsection{Estudo de Caso Sintético: Otimização de Coorte Clínica Abdominal}
Para demonstrar a aplicabilidade prática do formalismo, a \cref{tab:ssw_dprime_simulacao} apresenta uma modelagem sintética controlada de otimização de protocolo tomográfico abdominal em uma coorte institucional representativa, comparando a FBP clássica a $120\text{ kVp}$, DLR a $100\text{ kVp}$ e PCCT espectral com imagem monoenergética virtual ($VMI$) a $50\text{ keV}$.

A coorte foi estratificada em três grupos biométricos:
\begin{itemize}
  \item Grupo 1 (Pediátrico / Adulto Jovem Magro, 15\% da coorte): $D_{w,1} = 16\text{ cm}$, $f_{\text{size}} = 2{,}06$;
  \item Grupo 2 (Adulto Eutrófico Padrão, 55\% da coorte): $D_{w,2} = 28\text{ cm}$, $f_{\text{size}} = 1{,}32$;
  \item Grupo 3 (Adulto Obeso / Bariátrico, 30\% da coorte): $D_{w,3} = 38\text{ cm}$, $f_{\text{size}} = 0{,}92$.
\end{itemize}
Definiram-se duas tarefas diagnósticas concorrentes: Tarefa 1 (metástase hepática sutil de $5\text{ mm}$, $\Delta C_1 = 20\text{ HU}$, peso clínico majoritário $\Omega_1 = 0{,}70$) e Tarefa 2 (ramo arterial vascular com iodo, $\Delta C_2 = 120\text{ HU}$, peso clínico $\Omega_2 = 0{,}30$).

\begin{table}[htbp]
  \centering
  \small
  \caption[Simulação do Índice SSW-$d'$ e Figura de Mérito]{Simulação Paramétrica do Índice SSW-$d'$ e da Figura de Mérito ($\text{FOM}_{\text{SSW}}$) em Coorte Clínica Abdominal \cite{fitton2026, goppel2021, aapm_report204, racine2020}.}
  \label{tab:ssw_dprime_simulacao}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.22\textwidth} >{\centering}p{0.13\textwidth} >{\centering}p{0.13\textwidth} >{\centering}p{0.14\textwidth} >{\centering}p{0.14\textwidth} >{\centering\arraybackslash}X}
    \toprule
    \textbf{Protocolo / Tecnologia} & \textbf{$d'_{1}$ (16 cm)} \newline \footnotesize(Ped/Pequeno) & \textbf{$d'_{2}$ (28 cm)} \newline \footnotesize(Adulto Std) & \textbf{$d'_{3}$ (38 cm)} \newline \footnotesize(Bariátrico) & \textbf{SSW-$d'$} \newline \footnotesize(Populacional) & \textbf{$\overline{\text{SSDE}}$ (mGy)} & \textbf{$\text{FOM}_{\text{SSW}}$ ($\text{mGy}^{-1}$)} \\
    \midrule
    1. FBP Clássica (120 kVp, Dose Padrão) & 2,85 & 1,92 & 1,18 & \textbf{1,98} & 11,45 & \textbf{0,34} \\
    \addlinespace[0.4em]
    2. HIR Iterativa (120 kVp, Redução 30\%) & 3,10 & 2,15 & 1,29 & \textbf{2,18} & 8,02 & \textbf{0,59} \\
    \addlinespace[0.4em]
    3. DLR Avançada (100 kVp, Baixa Dose) & 3,95 & 2,78 & 1,64 & \textbf{2,79} & 6,15 & \textbf{1,26} \\
    \addlinespace[0.4em]
    4. PCCT VMI 50 keV (Contagem Fótons) & 5,12 & 3,84 & 2,41 & \textbf{3,79} & 5,20 & \textbf{2,76} \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026) com base em formulações de Fitton et al. \cite{fitton2026}, Göppel et al. \cite{goppel2021} e Relatório AAPM 204 \cite{aapm_report204}.}
\end{table}

\paragraph{Análise dos Resultados e Impacto Clínico:} Os dados da \cref{tab:ssw_dprime_simulacao} revelam aspectos decisivos para a prática da física médica:
\begin{enumerate}
  \item \textbf{Aumento Progressivo da Eficiência ($\text{FOM}_{\text{SSW}}$):} A transição da FBP clássica para DLR a $100\text{ kVp}$ elevou a detectabilidade populacional de $\text{SSW-}d' = 1{,}98$ para $2{,}79$, enquanto a dose média absorvida $\overline{\text{SSDE}}$ caiu de $11{,}45\text{ mGy}$ para $6{,}15\text{ mGy}$, resultando em um ganho de eficiência dosimétrica ($\text{FOM}_{\text{SSW}}$) de quase quatro vezes ($0{,}34 \to 1{,}26\text{ mGy}^{-1}$);
  \item \textbf{Supremacia Tecnológica da PCCT Espectral:} A reconstrução $VMI$ em $50\text{ keV}$ nos detectores de contagem de fótons atingiu $\text{FOM}_{\text{SSW}} = 2{,}76\text{ mGy}^{-1}$ (ganho de mais de $800\%$ sobre a FBP de referência). Isso decorre do aproveitamento ótimo do efeito fotoelétrico do iodo em $50\text{ keV}$ combinado à eliminação do ruído eletrônico em pacientes bariátricos ($d'_{3}$ manteve-se em nível diagnóstico de $2{,}41$, comparado a inaceitáveis $1{,}18$ na FBP);
  \item \textbf{Vulnerabilidade do Paciente Bariátrico:} Em todos os protocolos, o estrato bariátrico ($38\text{ cm}$) apresentou a menor detectabilidade devido à atenuação fotônica maciça. O SSW-$d'$ impede que o tomógrafo seja configurado apenas para o paciente padrão, forçando o físico médico a garantir que mesmo o subgrupo mais pesado atinja o limiar de decisão $d' \ge 1{,}5$.
\end{enumerate}

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}[leftmargin=*,noitemsep]
  \item \emph{Impacto Metrológico:} O SSW-$d'$ e a $\text{FOM}_{\text{SSW}}$ expandem a metrologia baseada em tarefa de ensaios pontuais em bancada para a otimização estatística abrangente de coortes populacionais inteiras.
  \item \emph{Vantagens sobre Métricas Anteriores:} Acopla a variabilidade biométrica real dos pacientes ($D_w$) e a multiplicidade de tarefas clínicas ($\Omega_j$) à dose absorvida corrigida por tamanho ($\text{SSDE}$), eliminando o viés do simulador único.
  \item \emph{Limitações do Modelo:} Exige medições espectrais ($TTF, NPS$) em baterias de múltiplos simuladores físicos de diferentes calibres ou amostragem sistemática em banco de imagens clínicas com estimativa automatizada de $D_w$.
\end{itemize}

\section{Observadores Lineares: Hotelling, NPWE e CHO}
\label{sec:observadores_lineares_deducoes_completas}

\subsection{Observadores Lineares Analíticos: Limite de Hotelling, Formulação Contínua do NPWE e Premissas Lineares}
\label{subsec:observadores_lineares_analiticos_npwe_hotelling}

\subsubsection{Dedução Analítica do Observador de Hotelling e o Teto Bayesiano}
O Observador Ideal Bayesiano (\emph{Ideal Observer} --- IO) estabelece o limite superior absoluto de extração de informação diagnóstica permitido pelas leis da física da radiação e da formação de imagem. Sob a hipótese de ruído gaussiano multivariado com vetor de médias $\mathbf{s}_0 = \mathbf{0}$ sob $H_0$ e $\mathbf{s}_1 = \mathbf{s}$ sob $H_1$, e matriz de autocovariância comum $\mathbf{K} \in \mathbb{R}^{N \times N}$, a função densidade de probabilidade condicional para um vetor de imagem $\mathbf{g} \in \mathbb{R}^N$ expressa-se por:
\begin{equation}
  p(\mathbf{g}|H_k) = \frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left[ -\frac{1}{2} (\mathbf{g} - \mathbf{s}_k)^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}_k) \right], \quad k \in \{0, 1\}
  \label{eq:densidade_gaussiana_vetorial}
\end{equation}

Aplicando o logaritmo natural à razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = p(\mathbf{g}|H_1)/p(\mathbf{g}|H_0)$, as constantes de normalização se cancelam exatamente, resultando no Observador de Hotelling (\emph{Hotelling Observer} --- HO) \cite{barrett_myers_2004, wagner1979}:
\begin{equation}
  \ln\Lambda(\mathbf{g}) = -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) + \frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g} - \frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}
  \label{eq:log_bayes_deducao}
\end{equation}

O termo $-\frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ é uma constante determinística independente dos dados amostrais $\mathbf{g}$ e pode ser absorvido diretamente no limiar de decisão $t_c$. A estatística escalar ótima de teste é, portanto, uma transformação linear estrita:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:hotelling_template_deducao}
\end{equation}
onde o vetor de ponderação $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ opera como um gabarito linear ótimo (\emph{optimal matched filter}) que executa duas operações simultâneas:
\begin{enumerate}
  \item \textbf{Inversão e Branqueamento do Ruído ($\mathbf{K}^{-1}$):} Descorrelaciona a estrutura estocástica do ruído de fundo, suprimindo frequências com alta densidade de ruído e amplificando bandas espectrais limpas;
  \item \textbf{Casamento de Padrão Espacial ($\mathbf{s}^T$):} Maximiza a sensibilidade geométrica à forma, ao tamanho e ao perfil de atenuação da lesão investigada.
\end{enumerate}

Calculando a esperança e a variância da estatística $t_{\text{HO}}$ sob ambas as hipóteses ($\langle t_{\text{HO}} \rangle_{H_1} - \langle t_{\text{HO}} \rangle_{H_0} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ e $\sigma_{t,\text{HO}}^2 = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$), o índice de detectabilidade máximo absoluto atingível é formulado por:
\begin{equation}
  d'_{\text{HO}} = \frac{\langle t_{\text{HO}} \rangle_{H_1} - \langle t_{\text{HO}} \rangle_{H_0}}{\sigma_{t,\text{HO}}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling_teto}
\end{equation}

\subsubsection{Formulação Contínua do Observador Antropomórfico NPWE}
Embora o Observador de Hotelling estabeleça o limite físico do tomógrafo, o sistema visual humano não possui a capacidade cognitiva de inverter em tempo real uma matriz de covariância $\mathbf{K}$ de dimensão $N \times N$ ($N \approx 512^2 = 262.144$ pixels). Para modelar observadores humanos em fundos homogêneos, o modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) assume que o médico opera como um integrador sem pré-branqueamento ($\mathbf{w} = \mathbf{s}$), cuja resposta visual é limitada pela função de transferência ocular $E(f)$ e degradada por ruído estocástico neural interno $\sigma_{\text{int}}^2$ \cite{burgess1994, eckstein2000}.

No domínio contínuo de Fourier bidimensional com simetria radial isotrópica, a integral contínua do índice de detectabilidade do NPWE expressa-se analiticamente por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral_completa}
\end{equation}

O impacto físico e metrológico de cada termo que compõe a \cref{eq:dprime_npwe_integral_completa} é determinante para a qualidade interpretativa da imagem:
\begin{enumerate}
  \item \textbf{Numerador (Sinal Perceptual Integrado):} Representa a energia útil do sinal transferida pelo sistema tomográfico ($\left[ TTF(f) \right]^2$), ponderada pelo espectro morfológico da patologia ($\left[ W_{\text{task}}(f) \right]^2$) e filtrada pela acuidade visual do radiologista ($\left[ E(f) \right]^2$). Quanto maior este termo, mais nítida e conspícua é a imagem da lesão para o observador humano;
  \item \textbf{Denominador (Ruído Perceptual Efetivo):} Quantifica a variância estocástica percebida pelo córtex visual, dada pelo produto do espectro de ruído físico $NPS(f)$ pela quarta potência da sensibilidade ocular $\left[ E(f) \right]^4$ e pelo gabarito do sinal. O termo aditivo $\sigma_{\text{int}}^2$ modela as flutuações eletrofisiológicas nas sinapses retinianas e corticais, impedindo que o índice $d'$ cresça indefinidamente mesmo quando o ruído quântico da imagem tende a zero;
  \item \textbf{Diferença Fundamental HO vs. NPWE:} Enquanto o Hotelling divide o espectro pelo ruído em cada frequência ($TTF^2/NPS$), o NPWE integra o sinal e o ruído separadamente, refletindo a incapacidade humana de suprimir seletivamente o ruído correlacionado.
\end{enumerate}

\subsubsection{Equivalência Matemática e os Três Pilares da Validade Linear}
A correlação exata entre a álgebra linear discreta de Hotelling (\cref{eq:dprime_hotelling_teto}) e a formulação contínua de Fourier do NPWE (\cref{eq:dprime_npwe_integral_completa}) fundamenta-se no teorema da diagonalização de matrizes Toeplitz circulantes em duas dimensões \cite{barrett_myers_2004}. Sob as premissas de linearidade do sistema, invariância translacional espacial e estacionariedade em sentido amplo (WSS) do ruído, a matriz de covariância espacial $\mathbf{K}$ é diagonalizada pela matriz unitária da Transformada Discreta de Fourier $\mathbf{F} \in \mathbb{C}^{N \times N}$:
\begin{equation}
  \mathbf{K} = \mathbf{F}^\dagger \mathbf{S}_{NPS} \mathbf{F} \implies \mathbf{K}^{-1} = \mathbf{F}^\dagger \mathbf{S}_{NPS}^{-1} \mathbf{F}
  \label{eq:diagonalizacao_fourier_covariancia}
\end{equation}
onde $\mathbf{S}_{NPS} = \operatorname{diag}\left( NPS(u_1, v_1), \dots, NPS(u_N, v_N) \right)$ contém os autovalores da densidade espectral de potência. Substituindo a \cref{eq:diagonalizacao_fourier_covariancia} na forma quadrática $\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ e aplicando o Teorema de Plancherel-Parseval, a expressão discreta converge no limite contínuo exatamente para a integral espectral em Fourier.

\paragraph{Impacto na Tarefa do Médico Radiologista:} Na rotina de leitura, o radiologista realiza um escaneamento visual ativo buscando correlacionar as densidades radiológicas com seu mapa cognitivo prévio da lesão (equivalente ao gabarito $\mathbf{s}$). Quando o ruído é puramente estocástico e gaussiano (FBP em meios homogêneos), o modelo NPWE prediz com fidelidade a taxa de acerto do especialista. No entanto, se o ruído contiver correlações espaciais complexas ou se a reconstrução for não linear, o cérebro humano perde eficiência, gerando aumento do tempo de fixação foveal, hesitação diagnóstica e risco aumentado de falsos-negativos em lesões de baixo contraste.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} O modelo de Hotelling fornece o referencial superior da teoria da informação ($d'_{\text{HO}}$), enquanto o NPWE estabelece o primeiro modelo antropomórfico computacionalmente tratável via integração contínua em Fourier ($d'_{\text{NPWE}}$).
  \item \emph{Vantagens sobre Métricas Anteriores:} Substitui o $SNR$ escalar simples por uma métrica fundamentada na teoria da decisão e na psicofísica visual, incorporando a morfologia da lesão e a resposta de contraste do olho humano.
  \item \emph{Limitações do Modelo:} Válido exclusivamente sob linearidade estrita e fundos uniformes. O NPWE não modela a segregação cortical em canais de frequência orientados, falhando severamente diante de fundos anatômicos estruturados.
\end{itemize}

\subsection{Observador de Hotelling Canalizado (CHO), Validação Psicofísica MRMC e Aplicação Clínica no AVC Isquêmico}
\label{subsec:cho_mrmc_avc_isquemico_consolidado}

\subsubsection{Formulação do Observador CHO e Modelagem de Canais Corticais}
Para modelar o desempenho de observadores humanos diante de imagens médicas contendo fundos anatômicos estruturados e complexos (como parênquima pulmonar, trabeculado ósseo ou textura cerebral), Myers e Barrett (1987) introduziram o conceito de canais corticais de frequência, formulando o Observador de Hotelling Canalizado (\emph{Channelized Hotelling Observer} --- CHO) \cite{myers_barrett_1987, gallas2003}.

O modelo fundamenta-se na neurofisiologia do córtex visual primário (área V1), no qual populações de neurônios comportam-se como filtros passa-faixa sintonizados em bandas de frequência espacial e orientações angulares específicas. A imagem de entrada $\mathbf{g} \in \mathbb{R}^N$ é projetada em um espaço vetorial de dimensão reduzida $\mathbf{v} \in \mathbb{R}^P$ ($P \ll N$, tipicamente $P \in [4, 10]$ canais) através da matriz de canais corticais $\mathbf{T} \in \mathbb{R}^{P \times N}$:
\begin{equation}
  \mathbf{v} = \mathbf{T} \mathbf{g}
  \label{eq:cho_projecao_v}
\end{equation}

A estatística escalar de decisão do CHO e seu respectivo índice de detectabilidade são formulados no subespaço dos canais por:
\begin{equation}
  t_{\text{CHO}}(\mathbf{g}) = \mathbf{w}_{\mathbf{v}}^T \mathbf{v} = \left( \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle \right)^T \mathbf{v} = \langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \mathbf{v}
  \label{eq:cho_stat_completa}
\end{equation}
\begin{equation}
  d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}
  \label{eq:dprime_cho_completo}
\end{equation}
onde $\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K} \mathbf{T}^T \in \mathbb{R}^{P \times P}$ é a matriz de covariância do ruído no espaço dos canais corticais e $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \mathbf{s} \in \mathbb{R}^P$ representa o perfil médio da lesão projetado nos canais. Como a dimensão de $\mathbf{K}_{\mathbf{v}}$ é extremamente reduzida ($P \times P \le 10 \times 10$), a inversão matricial torna-se numericamente estável e computacionalmente trivial, eliminando a instabilidade de inversão da matriz original $\mathbf{K} \in \mathbb{R}^{N \times N}$.

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{fig3_cho_cortical_channels.png}{Modelagem Numérica Sintética dos Canais Corticais do Observador CHO.}
  \caption[Canais Corticais do Observador CHO]{Canais Corticais do Observador CHO e Desempenho em Fundo Estruturado \cite{myers_barrett_1987, gallas2003, barrett_myers_2004}.}
  \label{fig:cho_channels}
\end{figure}

A modelagem sintética ilustrada na \cref{fig:cho_channels} sintetiza o comportamento analítico e perceptual dos canais corticais do Observador CHO parametrizados a partir da \cref{tab:parametros_simulacao}:
\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação dos Canais D-DOG (\emph{Dense Difference of Gaussians}):}
  Implementaram-se cinco canais passa-faixa concêntricos definidos pela diferença de gaussianas no domínio da frequência:
  \begin{equation}
    C_j(f) = \exp\left( -\frac{f^2}{2\sigma_{j,1}^2} \right) - \exp\left( -\frac{f^2}{2\sigma_{j,2}^2} \right), \quad j = 1, \dots, 5
    \label{eq:ddog_formula}
  \end{equation}
  com desvios padrão escalonados geometricamente para cobrir a faixa de $0{,}10\text{ a }0{,}85\text{ mm}^{-1}$, emulando com alta precisão os campos receptivos circulares do córtex visual humano;

  \item \textbf{Painel (B) --- Simulação das Funções Radiais de Laguerre-Gauss:}
  Avaliaram-se os polinômios ortogonais de Laguerre-Gauss de ordens $n \in \{0, 1, 2, 3\}$ com raio característico $a = 4{,}0\text{ mm}$:
  \begin{equation}
    LG_n(r) = L_n\left( \frac{2\pi r^2}{a^2} \right) \exp\left( -\frac{\pi r^2}{a^2} \right)
    \label{eq:laguerre_gauss_formula}
  \end{equation}
  proporcionando uma base ortogonal compacta que captura simetrias radiais com reduzido número de graus de liberdade;

  \item \textbf{Painel (C) --- Campo Receptivo Bidimensional de Gabor ($\theta = 45^\circ$):}
  Modelou-se a matriz bidimensional combinando envelope gaussiano e modulação senoidal orientada:
  \begin{equation}
    G(x, y) = \exp\left( -\frac{x'^2 + \gamma^2 y'^2}{2\sigma^2} \right) \cos\left( 2\pi \frac{x'}{\lambda} + \psi \right)
    \label{eq:gabor_formula}
  \end{equation}
  com $x' = x\cos\theta + y\sin\theta$ e $y' = -x\sin\theta + y\cos\theta$, modelando a sensibilidade direcional a bordas lineares e espículas anatômicas;

  \item \textbf{Painel (D) --- Simulação Comparativa NPWE vs. CHO em Fundo Estruturado:}
  Simulou-se o cálculo de detectabilidade em função da dose para uma lesão de 5 mm imersa em ruído anatômico estruturado (ruído em lei de potência $1/f^\beta$, $\beta = 2{,}5$). Demonstra-se que o modelo linear NPWE (curva vermelha) subestima drasticamente a detectabilidade ($d' < 0{,}8$) por confundir variações anatômicas normais com ruído quântico puro, enquanto o CHO D-DOG (curva verde) descorrelaciona o fundo e preserva correlação estatisticamente perfeita com a acuidade visual de especialistas humanos.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.95\textwidth]{flow3_cho_pipeline.png}{Diagrama do Fluxo de Decisão do Observador CHO.}
  \caption[Fluxo de Decisão do Observador CHO]{Fluxo de Processamento e Decisão do Observador CHO \cite{myers_barrett_1987, gallas2003}.}
  \label{fig:cho_flow_diagram}
\end{figure}

O fluxo metodológico completo de implementação do Observador CHO está esquematizado na \cref{fig:cho_flow_diagram}, detalhando as etapas desde a extração de pares de ROIs pareadas até a computação da matriz $\mathbf{K}_{\mathbf{v}}^{-1}$ e a determinação do valor escalar $d'_{\text{CHO}}$.

\subsubsection{Validação Psicofísica MRMC e Matriz Comparativa de Observadores}
A calibração e validação de observadores computacionais contra painéis de médicos radiologistas especialistas é formalizada pelo modelo estatístico de Análise de Variância (ANOVA) com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova_completa}
\end{equation}
onde $y_{ijk}$ representa a métrica de desempenho observada (como a área sob a curva ROC, $AUC$, ou o índice $d'$), $\mu$ é o desempenho médio global, $\tau_i$ é o efeito fixo da modalidade de reconstrução ou dose $i$, $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é a variabilidade inter-observador entre radiologistas, $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é a variabilidade biológica inter-paciente, e $\epsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\epsilon})$ é o erro residual aleatório.

A \cref{tab:comparativo_observadores} sintetiza as propriedades físicas, domínios de aplicação e limitações das principais classes de observadores de modelo consolidadas na literatura.

\begin{table}[htbp]
  \centering
  \small
  \caption[Comparativo das Classes de Observadores de Modelo]{Resumo Comparativo das Classes de Observadores de Modelo em Física Médica \cite{barrett_myers_2004, burgess1994, myers_barrett_1987, toia2023, debbiche2024}.}
  \label{tab:comparativo_observadores}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.20\textwidth} >{\RaggedRight}p{0.24\textwidth} >{\RaggedRight}p{0.24\textwidth} >{\RaggedRight\arraybackslash}X}
    \toprule
    \textbf{Modelo} & \textbf{Domínio de Aplicação} & \textbf{Vantagens Físicas} & \textbf{Limitações Principais} \\
    \midrule
    Observador Ideal (IO / HO) \cite{barrett_myers_2004, wagner1979} & FBP clássica, ruído gaussiano homogêneo & Estabelece o limite superior absoluto de informação física & Não modela a visão humana; requer inversão matricial $\mathbf{K}^{-1}$ \\
    \addlinespace[0.4em]
    NPWE \cite{burgess1994, eckstein2000} & FBP em simuladores homogêneos & Rápido cálculo analítico contínuo em Fourier via $TTF/NPS$ & Colapsa sob DLR e fundos anatômicos estruturados \\
    \addlinespace[0.4em]
    CHO (D-DOG, LG, Gabor) \cite{myers_barrett_1987, gallas2003} & FBP/HIR em fundos anatômicos estruturados & Excelente correlação com humanos em fundos complexos lineares & Subótimo em DLR devido a não-linearidades de alta ordem \\
    \addlinespace[0.4em]
    DLMO (Vision Transformers) \cite{dosovitskiy2020, toia2023, debbiche2024} & DLR não linear, PCCT e anatomias complexas & Modela atenção foveal-periférica e atinge $r > 0{,}95$ com radiologistas & Requer calibração supervisionada e maior custo computacional \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026).}
\end{table}

\subsubsection{Discussão Clínica: AVC Isquêmico Hiperagudo e a Tarefa Interpretativa}
A formulação do CHO em fundos estruturados e a modelagem psicofísica MRMC encontram sua aplicação mais crítica e sensível ao tempo na avaliação tomográfica do Acidente Vascular Cerebral (AVC) isquêmico na fase hiperaguda (primeiras 4,5 horas após o início do déficit neurológico focal).

No AVC isquêmico hiperagudo, a oclusão embólica ou trombótica de um ramo arterial cerebral (tipicamente o segmento M1 ou M2 da artéria cerebral média) acarreta anóxia tecidual imediata e falência precoce das bombas iônicas de sódio-potássio ATPase nas membranas neuronais. Esse colapso energético provoca influxo maciço de íons sódio e água para o meio intracelular, originando edema citotóxico. Como a água apresenta coeficiente de atenuação linear ligeiramente inferior ao parênquima cerebral sadio, o tecido em sofrimento isquêmico exibe uma discreta hipoatenuação tomográfica de apenas $3\text{ a } 5\text{ HU}$. O sinal radiológico determinante consiste no apagamento do córtex insular (\emph{insular ribbon sign}), na perda de definição do núcleo lentiforme e no obscurecimento do gradiente natural entre substância cinzenta ($35\text{ a } 40\text{ HU}$) e substância branca ($28\text{ a } 32\text{ HU}$).

\paragraph{Impacto na Tarefa Interpretativa do Radiologista:} Nesta tarefa, o fundo anatômico cerebral não é um meio uniforme de água, mas uma estrutura densamente heterogênea composta por sulcos corticais, foice cerebral, calcificações nos plexos coróides e artefatos de endurecimento de feixe na fossa posterior decorrentes da espessa calota craniana óssea hiperatenuante ($> 1000\text{ HU}$). 

Se o controle de qualidade hospitalar avaliar este protocolo por métricas simplificadas em fantomas de água (como NPWE ou $CNR$), o tomógrafo indicará conformidade metrológica. Contudo, ao submeter o exame ao Observador CHO com canais D-DOG e Gabor (\cref{fig:cho_channels}) ou ao crivo de radiologistas em estudos MRMC, o índice de detectabilidade decai drasticamente. A textura parenquimatosa cerebral atua como ruído anatômico estruturado ($1/f^\beta$ com $\beta \approx 2{,}5$), que satura os canais visuais de baixa frequência e mimetiza o edema citotóxico incipiente.

A quantificação fidedigna da extensão da área isquêmica através do escore ASPECTS (\emph{Alberta Stroke Programme Early CT Score}, escala de 0 a 10) é o biomarcador de imagem determinante que define a conduta terapêutica: pacientes com $\text{ASPECTS} \ge 6$ são candidatos imediatos à trombólise química endovenosa com rtPA ou à trombectomia mecânica com stent retriever. Protocolos tomográficos subótimos que não preservam $d'_{\text{CHO}} \ge 2{,}0$ para alvos de $\Delta C = 4\text{ HU}$ em fundo cerebral estruturado induzem duas falhas interpretativas graves:
\begin{enumerate}
  \item \textbf{Erro Falso-Negativo (Subestimação do Infarto):} O médico não detecta a isquemia precoce ($\text{ASPECTS} = 10$ aparente), indicando trombólise tardia em áreas de infarto extenso já consolidado, o que culmina em transformação hemorrágica maciça e óbito;
  \item \textbf{Erro Falso-Positivo (Superestimação por Artefatos):} O radiologista interpreta artefatos estocásticos de baixa frequência como infarto extenso ($\text{ASPECTS} < 6$), excluindo indevidamente um paciente viável do tratamento trombolítico que salvaria sua funcionalidade neurológica motora e cognitiva.
\end{enumerate}

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} O CHO viabiliza a computação estável do índice de detectabilidade ($d'_{\text{CHO}}$) em fundos anatomicamente complexos através de projeções em canais corticais V1, enquanto o modelo ANOVA DBM/HOR fornece o padrão-ouro de validação estatística contra leitores humanos.
  \item \emph{Vantagens sobre Métricas Anteriores:} Supera a limitação crítica do NPWE ao desacoplar as variações anatômicas estruturadas do ruído quântico estocástico puro, exibindo correlação quase perfeita com especialistas em tarefas de neuroimagem e oncologia.
  \item \emph{Limitações do Modelo:} Assume formulações de canais lineares estacionários. Quando submetido a algoritmos não lineares por redes neurais profundas (DLR), o CHO linear perde capacidade preditiva, demandando a evolução para observadores DLMO baseados em inteligência artificial.
\end{itemize}

\section{Impacto da DLR e Colapso dos Modelos Lineares}
\label{sec:impacto_dlr_colapso_completo}

\subsection{Mecanismos Físicos do Colapso Linear e Origem Espectral do Efeito Ceroso em DLR}
\label{subsec:mecanismos_colapso_linear_efeito_ceroso}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{fig4_dlr_non_linearity_detrending.png}{Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR.}
  \caption[Não-Linearidade em DLR e Detrending 2D]{Não-Linearidade em DLR, Correlação Humana e Detrending 2D \cite{racine2021, toia2023, debbiche2024, aapm_tg233_2019}.}
  \label{fig:dlr_non_linear}
\end{figure}

A modelagem sintética apresentada na \cref{fig:dlr_non_linear} ilustra o impacto da não-linearidade e os procedimentos de correção estatística sob reconstruções por aprendizado profundo sintetizados a partir da \cref{tab:parametros_simulacao}:
\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação de Detectabilidade $d'$ vs. Dose em DLR:}
  Comparou-se o escalonamento clássico da FBP ($\sigma \propto 1/\sqrt{\text{Dose}} \implies d' \propto \sqrt{\text{Dose}}$, linha preta) contra o modelo não linear adaptativo de DLR (linha verde), onde a rede neural preserva a detectabilidade diagnóstica ($d' = 1{,}8$) mesmo em regimes de ultrabaixa dose ($1{,}5\text{ mGy}$) \cite{racine2021, solomon2020};

  \item \textbf{Painel (B) --- Simulação de Correlação com Radiologistas Humanos:}
  Modelou-se a dispersão de leituras 2AFC para ilustrar a perda de correlação do modelo linear NPWE sob DLR (cruzes vermelhas, $r = 0{,}68$, resultado empírico reportado pioneiramente por Racine et al. \cite{racine2021}, decorrente da incapacidade do modelo de tratar o ruído não-estacionário), contrastando com observadores profundos adaptativos (círculos verdes, $r = 0{,}98$, observado em estudos específicos por Toia et al. \cite{toia2023} e Debbiche et al. \cite{debbiche2024}, ainda pendentes de replicação ampla em coortes multicêntricas);

  \item \textbf{Painel (C) --- Demonstração do Detrending Polinomial 2D:}
  Simulou-se um perfil de intensidade anatômica $I(x)$ com gradiente macroscópico e ruído de alta frequência. Demonstra-se que o ajuste de superfície polinomial de 2ª ordem $P_2(x)$ (linha tracejada vermelha) via mínimos quadrados analíticos subtrai a variação estrutural lenta, isolando o ruído estocástico puro residual $\delta I(x) = I(x) - P_2(x)$ (curva verde inferior) \cite{aapm_tg233_2019}.
\end{enumerate}

\subsubsection{Causas Matemáticas e Físicas do Colapso dos Modelos Lineares}
O colapso dos modelos analíticos lineares clássicos (como o NPWE e o CHO tradicional) diante dos algoritmos de Reconstrução por Aprendizado Profundo (DLR) decorre de três violações matemáticas e físicas fundamentais \cite{racine2021, toia2023, debbiche2024}:
\begin{enumerate}
  \item \textbf{Quebra da Premissa Gaussiana e da Estacionariedade (Não-WSS):} As funções de ativação não lineares (como ReLU e GELU) e as camadas de normalização em redes profundas quebram a simetria da distribuição normal multivariada do ruído. O ruído passa a exibir não-estacionariedade espacial severa, variando ponto a ponto em função do contraste e da textura local, o que torna a estatística linear $t = \mathbf{w}^T \mathbf{g}$ matematicamente subótima;
  \item \textbf{O Paradoxo da Supressão de Ruído no Modelo NPWE:} O modelo NPWE utiliza um filtro ocular estático $E(f)$ ponderado pelo espectro $NPS(f)$ (\cref{eq:dprime_npwe_integral_completa}). Quando a rede neural DLR suprime agressivamente o desvio padrão global $\sigma_{\text{HU}}$ deslocando a potência para baixas frequências, a integral do denominador do NPWE decresce bruscamente. Isso faz o índice $d'_{\text{NPWE}}$ disparar artificialmente para valores irreais ($d' > 6{,}0$), enquanto observadores humanos perdem acurácia diagnóstica devido ao borramento textural e perda de bordas (queda de correlação para $r \approx 0{,}68$ observada em ensaios com fantomas de baixo contraste por Racine et al. \cite{racine2021});
  \item \textbf{Inflexibilidade das Bases de Canais Corticais Rígidos:} Os canais corticais D-DOG e Laguerre-Gauss foram deduzidos sob a hipótese de invariância espacial linear. Eles são incapazes de capturar correlações estatísticas de alta ordem aprendidas por redes convolucionais profundas e mecanismos de atenção contextual.
\end{enumerate}

\subsubsection{Origem Espectral do Efeito Ceroso (\emph{Plastic/Waxy Look})}
Para demonstrar formalmente a falência das métricas escalares tradicionais ($SNR, CNR$) introduzidas no Capítulo 1 (\cref{sec:metricas_escalares_tradicionais}), considere um algoritmo DLR com forte regularização não linear. Sob esse processamento, o desvio padrão do ruído em uma região homogênea de água sofre uma redução expressiva de $\sigma_{\text{FBP}} = 15\text{ HU}$ para $\sigma_{\text{DLR}} = 5\text{ HU}$. Aplicando as definições clássicas de $SNR$ (\cref{eq:snr_formula}) e $CNR$ (\cref{eq:cnr_formula}), o sistema indicaria um aparente ganho de qualidade de $300\%$, sugerindo equivocadamente que a dose de radiação poderia ser reduzida a um terço sem perdas.

No entanto, a decomposição espectral no domínio de Fourier desmascara esse falso ganho:
\begin{enumerate}
  \item Para alvos de baixo contraste ($\Delta C \le 20\text{ HU}$), a função de transferência da tarefa $TTF(f)$ sofre atenuação prematura de altas frequências, reduzindo a integral de sinal em mais de $40\%$;
  \item A supressão de ruído estocástico é altamente assimétrica: a rede suprime eficientemente ruídos em altas frequências ($f > 0{,}3\text{ mm}^{-1}$), mas preserva ou até amplifica a densidade de potência em baixas frequências espaciais ($f \in [0{,}05; 0{,}20]\text{ mm}^{-1}$).
\end{enumerate}

Multiplicando esse espectro de ruído redistribuído pelo filtro ocular humano de Burgess $E(f)$ (\cref{eq:filtro_ocular_burgess}, cujo pico de máxima sensibilidade ocorre em $\approx 0{,}8\text{ cpd} \approx 0{,}10\text{ mm}^{-1}$ para visualização padrão a 50 cm), a energia estocástica percebida pelo córtex do médico atinge um patamar máximo. É essa coincidência espectral entre o pico residual de ruído da DLR e o pico de sensibilidade do olho que gera o chamado efeito ceroso ou textura plástica (\emph{plastic/waxy look}).

\subsubsection{Controvérsias e Resultados Neutros na Literatura sobre DLR}
\label{subsubsec:controversias_dlr}
Embora a literatura enfatize predominantemente a capacidade da DLR em reduzir a dose de radiação preservando a detectabilidade de alvos clínicos, uma leitura crítica e não enviesada revela achados neutros e controversos que merecem registro:
\begin{itemize}
  \item \textbf{Equivalência em Tarefas de Alto Contraste:} Diversos ensaios psicofísicos independentes demonstraram que, em tarefas diagnósticas dominadas por contraste médio a elevado (tais como detecção de nódulos pulmonares sólidos macroscópicos $> 6\text{ mm}$ ou avaliação de fraturas ósseas corticais com desvio), o desempenho de radiologistas sob DLR não apresentou superioridade estatisticamente significante ($p > 0{,}05$) em relação a reconstruções iterativas estatísticas maduras (como ASiR-V ou AIDR 3D) ou mesmo à FBP convencional com filtros nítidos \cite{solomon2020, greffier2026};
  \item \textbf{Variabilidade na Preferência dos Leitores e Níveis de Regularização:} Estudos de preferência subjetiva revelam heterogeneidade expressiva entre radiologistas: profissionais seniores frequentemente rejeitam níveis máximos de DLR (\emph{High/Ultra-High Strength}) devido à artificialidade da textura de ruído, preferindo níveis médios (\emph{Medium}) onde a granulação gaussiana familiar é parcialmente preservada;
  \item \textbf{Alterações Imprevisíveis na Conspicuidade de Bordas:} Sob regimes de ultrabaixa dose extrema ($\text{CTDI}_{\text{vol}} < 1\text{ mGy}$), alguns algoritmos DLR comerciais podem introduzir pseudo-bordas ou apagar pequenas hipoatenuações parenquimatosas sutis por supressão excessiva de gradientes, gerando risco de falso-negativo se o protocolo não for rigorosamente auditado por métricas $d'$ baseadas em tarefa.
\end{itemize}

\paragraph{Impacto na Tarefa do Médico Radiologista:} O aspecto visual excessivamente suavizado e pontilhado por manchas amorfas de baixa frequência induz perda da nitidez de bordas anatômicas sutis e sensação subjetiva de insegurança diagnóstica. O radiologista gasta mais tempo analisando cortes adjacentes, sofre fadiga visual precoce e corre o risco de desconsiderar lesões incipientes por confundi-las com aglomerados estocásticos gerados pela própria rede de reconstrução.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} Desmistifica o ganho aparente das métricas escalares em DLR, demonstrando que a qualidade real depende da preservação da $TTF(f)$ em baixos contrastes e do controle da densidade espectral $NPS(f)$ na faixa visual crítica ($0{,}05\text{ a }0{,}20\text{ mm}^{-1}$).
  \item \emph{Vantagens sobre Métricas Anteriores:} Substitui avaliações subjetivas de ``textura agradável'' por uma formulação físico-matemática reprodutível baseada na correlação entre $NPS(f)$ e o filtro ocular $E(f)$.
  \item \emph{Limitações do Modelo:} Modelos analíticos lineares (NPWE e CHO) são matematicamente incapazes de predizer com precisão o desempenho humano sob DLR, tornando imperativa a adoção de plataformas psicofísicas 2AFC ou observadores por redes neurais (DLMO).
\end{itemize}

\subsection{Metodologia Experimental com Fantomas Híbridos e Discussão Clínica em Fraturas Trabeculares}
\label{subsec:fantomas_hibridos_fraturas_trabeculares}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.96\textwidth]{flow4_phantom_hibrido_2afc.png}{Metodologia Experimental com Phantoms Físicos Antropomórficos.}
  \caption[Fantomas Híbridos e Plataforma 2AFC]{Fantomas Híbridos e Plataforma Psicofísica 2AFC \cite{racine2020, toia2023, debbiche2024}.}
  \label{fig:phantom_flow}
\end{figure}

A validação experimental de novos algoritmos de inteligência artificial requer a superação dos fantomas cilíndricos homogêneos convencionais através de simuladores antropomórficos físicos acoplados à inserção computacional de lesões patológicas sintéticas (\cref{fig:phantom_flow}) \cite{racine2020, toia2023}:
\begin{enumerate}
  \item \textbf{Aquisição Fisiológica Real:} Varredura tomográfica de fantomas antropomórficos contendo estruturas anatômicas hiper-realistas (tórax, abdome ou ossos trabeculados) sob múltiplos níveis dosimétricos;
  \item \textbf{Inserção de Lesões Sintéticas Convoluídas:} Projeção de modelos computacionais tridimensionais de lesões (nódulos espiculados, metástases ou linhas de fratura) no domínio de projeção ou espaço de imagem, convoluídas com a PSF real do tomógrafo para garantir realismo físico;
  \item \textbf{Plataforma Psicofísica 2AFC Padronizada:} Condução de testes de escolha forçada com alternativas pareadas (\emph{Two-Alternative Forced Choice} --- 2AFC) com radiologistas especialistas e observadores de modelo em monitores calibrados pela norma DICOM GSDF.
\end{enumerate}

\subsubsection{Discussão Clínica: Fraturas Ósseas Trabeculares e a Tarefa Interpretativa}
O paradoxo da degradação de resolução espacial em alta frequência sob DLR manifesta-se criticamente na tomografia computadorizada do sistema musculoesquelético, em particular na pesquisa de fraturas de estresse incompletas, fraturas do colo e corpo do escafoide no punho e microfraturas de platô tibial em idosos osteoporóticos.

O osso esponjoso trabecular é constituído por um retículo estocástico de microespículas ósseas mineralizadas com espessura entre 100 e 200 $\mu\text{m}$, interligadas e circundadas por medula óssea gordurosa. A identificação tomográfica de uma fenda de microfratura submilimétrica sem desvio anatômico macroscópico é uma tarefa diagnóstica governada quase que com exclusividade por frequências espaciais ultra-altas ($f > 0{,}80\text{ mm}^{-1}$).

\paragraph{Impacto na Tarefa Interpretativa do Radiologista:} Quando o exame de TC osteoarticular é reconstruído com um algoritmo DLR configurado para máxima supressão de ruído, o software entrega uma imagem visualmente muito limpa, com elevado $SNR$ escalar e sem aparente granulação quântica. Contudo, ao atenuar severamente as altas frequências espaciais para eliminar o ruído, a rede neural funde as microespículas trabeculares vizinhas, transformando a delicada malha trabecular em uma massa homogênea esbranquiçada e cerosa. 

A fenda de fratura sutil, que não apresenta desalinhamento cortical visível a olho nu, é completamente preenchida e obliterada pelo processo de filtragem não linear. O médico radiologista emite um laudo falso-negativo de ``ausência de fraturas agudas'', liberando o paciente para deambulação ou carga funcional normal. A consequência clínica direta é a evolução desfavorável para necrose avascular óssea (especialmente frequente no polo proximal do escafoide e colo femoral), não consolidação (\emph{pseudoartrose}) ou colapso articular vicioso, que exige intervenções cirúrgicas reconstrutivas de alta complexidade.

Essa vulnerabilidade reforça que o controle de qualidade em serviços hospitalares não pode se apoiar em métricas de ruído médio global, devendo auditar a Função de Transferência da Tarefa $TTF(f)$ especificamente em frequências superiores a $0{,}80\text{ mm}^{-1}$ e utilizar índices de detectabilidade baseados na tarefa trabecular ($d'_{\text{trabecular}}$) para a liberação de novos algoritmos de inteligência artificial.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} A metodologia de fantomas híbridos combinada a testes 2AFC estabelece o protocolo de referência física para quantificar a perda de resolução em alta frequência sob DLR.
  \item \emph{Vantagens sobre Métricas Anteriores:} Detecta a obliteração de estruturas finas ($f > 0{,}80\text{ mm}^{-1}$) que passa totalmente despercebida pelo $SNR$ e pelo desvio padrão de água $\sigma_{\text{HU}}$.
  \item \emph{Limitações do Modelo:} Exige infraestrutura computacional para modelagem tridimensional de lesões sintéticas e requer calibração rigorosa da função de espalhamento de ponto (PSF) para evitar artefatos de borda.
\end{itemize}

\section{Observadores Baseados em Aprendizado Profundo (DLMO)}
\label{sec:dlmo_transformers_completo}

\subsection{Arquitetura Vision Transformers, Emulação da Percepção Foveal e Aplicação Clínica em Lesões Polimórficas}
\label{subsec:dlmo_vit_foveal_oncologia}

\subsubsection{Arquitetura e Fundamentação Matemática dos Observadores DLMO}
Para solucionar a falência dos modelos analíticos lineares diante da reconstrução não linear, a física médica estruturou os Observadores Baseados em Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), fundamentados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça (\cref{fig:dlmo_arch}) \cite{vaswani2017, dosovitskiy2020, toia2023, debbiche2024}.

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.96\textwidth]{flow5_dlmo_architecture.png}{Arquitetura de Observadores por Aprendizado Profundo.}
  \caption[Arquitetura do Observador DLMO]{Arquitetura do Observador de Modelo por Aprendizado Profundo (DLMO) \cite{vaswani2017, dosovitskiy2020, toia2023}.}
  \label{fig:dlmo_arch}
\end{figure}

Diferentemente das redes neurais convolucionais (CNNs) que operam limitadas a campos receptivos locais fixos, os Vision Transformers particionam a ROI tomográfica $\mathbf{g} \in \mathbb{R}^{H \times W}$ em uma sequência ordenada de $N_p = (H \cdot W)/P^2$ retalhos espaciais (\emph{patches}) $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 \cdot C)}$, aos quais se adicionam vetores de incorporação posicional (\emph{position embeddings}) para preservar a topologia espacial 2D. 

O cerne do processamento reside no operador de auto-atenção multi-cabeça (\emph{Multi-Head Self-Attention} --- MSA), que mapeia dinamicamente as relações entre todas as regiões da imagem através das matrizes de projeção de Consulta ($\mathbf{Q}$), Chave ($\mathbf{K}_v$) e Valor ($\mathbf{V}$):
\begin{equation}
  \text{Attention}(\mathbf{Q}, \mathbf{K}_v, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}_v^T}{\sqrt{d_k}} \right) \mathbf{V}
  \label{eq:self_attention_formula}
\end{equation}
onde $d_k$ é a dimensão do canal de projeção (fator de escala que estabiliza o gradiente do softmax). 

\paragraph{Emulação da Percepção Visual Humana:} Essa arquitetura matemática reproduz de maneira notável o comportamento neurofisiológico da visão humana: enquanto os primeiros blocos de atenção mapeiam a visão periférica de contexto (capturando o fundo anatômico e gradientes de baixa frequência), as cabeças de atenção mais profundas concentram-se na fixação foveal de alta resolução sobre as bordas da lesão. Com isso, os observadores DLMO atingem coeficientes de correlação superiores a $r > 0{,}95$ contra radiologistas humanos em testes psicofísicos 2AFC sob DLR (\cref{fig:dlr_non_linear}, Painel B) reportados em estudos pioneiros (notadamente Toia et al. \cite{toia2023} e Debbiche et al. \cite{debbiche2024}), superando o teto de $r \approx 0{,}68$ do modelo linear NPWE \cite{racine2021}. Ressalta-se que esses índices de correlação representam benchmarks de prova de conceito obtidos em simuladores e tarefas oncológicas específicas, demandando replicação contínua em coortes multicêntricas mais amplas.

\subsubsection{Controvérsias e Desafios de Generalização dos Modelos DLMO}
\label{subsubsec:controversias_dlmo}
Apesar de seu desempenho representacional superior, a literatura especializada aponta desafios e limitações fundamentais dos observadores DLMO que impedem sua adoção cega e imediata como ferramenta metrológica universal:
\begin{enumerate}
  \item \textbf{Opacidade e Natureza de Caixa-Preta:} Ao contrário dos observadores CHO, cujos canais D-DOG e Laguerre-Gauss possuem formulações analíticas determinísticas transparentes, os modelos DLMO contêm milhões de parâmetros treinados. Essa complexidade dificulta a rastreabilidade metrológica exigida por órgãos normativos de acreditação física;
  \item \textbf{Sensibilidade a Mudanças de Domínio (*Domain Shift*):} Um modelo DLMO treinado nas texturas de ruído de um tomógrafo específico (ex.: GE TrueFidelity) pode sofrer degradação acentuada de acurácia preditiva ao ser aplicado diretamente a imagens de outro fabricante (ex.: Canon AiCE ou Siemens NAEOTOM Alpha), exigindo rotinas dedicadas de re-treinamento ou transferência de aprendizado (*transfer learning*);
  \item \textbf{Custo Computacional e Infraestrutura:} A inferência de grandes modelos Vision Transformers exige infraestrutura de hardware dedicada (GPUs/TPUs de alta performance), encarecendo sua implementação em rotinas hospitalares de controle de qualidade em tempo real.
\end{enumerate}

\subsubsection{Discussão Clínica: Lesões Hepáticas Polimórficas e a Tarefa Interpretativa}
A superioridade metrológica dos observadores DLMO com mecanismos de atenção manifesta-se plenamente em tarefas diagnósticas que envolvem variabilidade morfológica e estocástica complexa, tais como o estadiamento oncológico hepático e a diferenciação entre cistos simples benignos, hemangiomas atípicos e carcinomas hepatocelulares (CHC) polimórficos.

Os observadores lineares clássicos (CHO e NPWE) baseiam-se estritamente no paradigma de Sinal Conhecido Exatamente (\emph{Signal Known Exactly} --- SKE), que assume uma lesão perfeitamente circular e invariante $\mathbf{s}$. Todavia, na prática oncológica, os tumores malignos apresentam morfologias altamente heterogêneas, com bordas espiculadas, microlobulações, realce nodular periférico descontínuo e áreas centrais de necrose cística. Quando um observador com canais rígidos circulares de Laguerre-Gauss ou D-DOG tenta projetar essas lesões assimétricas, a perda de informação geométrica degrada severamente o cálculo da detectabilidade.

\paragraph{Impacto na Tarefa Interpretativa do Radiologista:} Ao analisar uma TC hepática multifásica com contraste, o médico radiologista precisa rastrear simultaneamente o padrão de impregnação vascular (fase arterial com \emph{wash-in} rápido e fase portal com \emph{wash-out}) e a integridade da cápsula tumoral fibrosa fina ($< 1\text{ mm}$). 

Se o protocolo hospitalar for otimizado utilizando algoritmos DLR validados apenas por modelos SKE circulares, o sistema pode mascarar a deformação plástica imposta pela rede neural nas margens tumorais. O radiologista é induzido a subestimar a invasão microvascular capsular ou a classificar incorretamente um CHC invasivo como hemangioma atípico, alterando o estadiamento de Barcelona (BCLC) de ressecção cirúrgica curativa para tratamento paliativo tardio. O DLMO, ao capturar correlações morfológicas não-lineares, fornece ao físico médico a ferramenta de auditoria capaz de garantir que o processamento por inteligência artificial preserve a morfologia tumoral complexa necessária à decisão cirúrgica.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} O DLMO consolida o novo paradigma de observadores baseados em inteligência artificial, capaz de avaliar imagens com ruído não-gaussiano e não-estacionário geradas por algoritmos DLR.
  \item \emph{Vantagens sobre Métricas Anteriores:} Atinge correlação quase perfeita com radiologistas humanos ($r > 0{,}95$) em tarefas realistas com variabilidade anatômica e morfológica de sinal (SKS/BKE), superando as premissas simplificadas SKE dos modelos lineares.
  \item \emph{Limitações do Modelo:} Demanda treinamento supervisionado com conjuntos robustos de imagens, calibração contra painéis humanos e maior capacidade de processamento gráfico (GPUs dedicadas).
\end{itemize}

\section{Tomografia por Contagem de Fótons e Otimização de Pareto}
\label{sec:pcct_pareto_completo}

\subsection{Física dos Detectores PCCT, Decomposição Espectral e Tensores de Ruído Multi-Energia}
\label{subsec:pcct_fisica_detectores_decomposicao_tensor}

\subsubsection{Física dos Detectores PCCT e Vínculo com o Paradigma TBIQ}
A inserção da Tomografia Computadorizada por Contagem de Fótons (\emph{Photon-Counting CT} --- PCCT) nesta monografia não constitui uma mera exposição descritiva de hardware recente, mas sim o ápice conceitual e o campo de prova definitivo para a metrologia baseada em tarefa (TBIQ) \cite{willemink2018, rajendran2021, pimenta2026}. O marco regulatório e clínico dessa tecnologia foi estabelecido pela aprovação comercial do sistema NAEOTOM Alpha (Siemens Healthineers) pelo FDA em 2021 e pela CE, seguido por intensas avaliações clínicas e protótipos de contagem direta desenvolvidos por outros fabricantes globais como GE Healthcare, Philips e Canon Medical Systems \cite{rajendran2021, mccollough2026}.

Nos detectores convencionais de integração de energia (EID), a camada cintiladora cerâmica converte os fótons X incidentes em luz visível, que é posteriormente registrada por fotodiodos de silício. Esse processo indireto impõe restrições físicas severas:
\begin{enumerate}
  \item \textbf{Ponderação Energética Inversa ao Contraste:} O sinal elétrico integrado é proporcional à energia total depositada ($S \propto E$). Consequentemente, fótons de alta energia (provenientes predominantemente de espalhamento Compton, com baixo conteúdo de contraste tecidual) recebem maior peso no sinal do que fótons de baixa energia (responsáveis pelo efeito fotoelétrico e pelo contraste entre tecidos moles e meios iodados);
  \item \textbf{Ruído Eletrônico Aditivo:} O circuito de leitura analógico introduz ruído eletrônico gaussiano $\sigma_{\text{el}}^2$, que se soma ao ruído quântico de Poisson ($\sigma_{\text{total}}^2 = \sigma_{\text{quântico}}^2 + \sigma_{\text{el}}^2$). Em regimes de baixa dose ($\text{CTDI}_{\text{vol}} < 2\text{ mGy}$), o termo eletrônico passa a dominar o denominador da $SNR$, limitando a redução dosimétrica;
  \item \textbf{Perda de Resolução por Septos Ópticos:} Para evitar o espalhamento de luz entre pixels vizinhos (\emph{optical cross-talk}), os detectores EID exigem septos reflexivos opacos de tungstênio, limitando o tamanho físico do pixel a $0{,}5\text{ a }0{,}6\text{ mm}$ no plano do isocentro.
\end{enumerate}

Em contraste direto, os detectores PCCT utilizam semicondutores de conversão direta (telureto de cádmio, CdTe, ou cádmio-zinco-telureto, CZT, além de arranjos de silício profundo) acoplados a circuitos integrados específicos para aplicação (\emph{Application-Specific Integrated Circuits} --- ASIC) \cite{willemink2018, rajendran2021}. Cada fóton X absorvido gera instantaneamente uma nuvem de pares elétron-lacuna que migra sob um forte campo elétrico, induzindo um pulso de corrente ultracurto cuja amplitude é estritamente proporcional à energia do fóton individual.

A \cref{tab:detectores_comparativo} sintetiza as diferenças físicas e metrológicas fundamentais entre as duas tecnologias extraídas do corpus bibliográfico analisado nesta revisão \cite{willemink2018, rajendran2021, mccollough2026, pimenta2026, greffier2026}.

\begin{table}[htbp]
  \centering
  \small
  \caption[Comparativo Tecnológico de Detectores em Tomografia]{Síntese das Tecnologias de Detectores em Tomografia Computadorizada (EID vs PCCT) Extraída do Corpus da Revisão \cite{willemink2018, rajendran2021, mccollough2026, pimenta2026, greffier2026}.}
  \label{tab:detectores_comparativo}
  \renewcommand{\arraystretch}{1.25}
  \begin{tabularx}{\textwidth}{>{\RaggedRight\bfseries}p{0.22\textwidth} >{\RaggedRight}p{0.36\textwidth} >{\RaggedRight\arraybackslash}X}
    \toprule
    \textbf{Parâmetro Físico} & \textbf{Detectores EID (Convencionais)} & \textbf{Detectores PCCT (Contagem de Fótons)} \\
    \midrule
    Mecanismo de Conversão \cite{bushberg2020, willemink2018} & Indireto: Cintilador cerâmico ($\text{Gd}_2\text{O}_2\text{S}$) converte raios X em luz visível $\to$ Fotodiodo de silício & Direto: Semicondutor (CdTe ou CZT) converte raios X instantaneamente em pares elétron-lacuna \\
    \addlinespace[0.4em]
    Ponderação Energética \cite{rajendran2021} & Ponderação por energia: Fótons de alta energia recebem maior peso ($S \propto E$) & Ponderação unitária: Cada fóton contado individualmente com peso idêntico ($S \propto N$) \\
    \addlinespace[0.4em]
    Ruído Eletrônico \cite{mccollough2026} & Integrado ao sinal de imagem, degradando regimes de baixa dose ($\sigma_{\text{el}}^2 > 0$) & Totalmente eliminado via limiares de energia discriminadores ($\sigma_{\text{el}}^2 = 0$) \\
    \addlinespace[0.4em]
    Resolução Espacial \cite{pimenta2026, greffier2026} & Limitada por septos ópticos reflexivos ($0{,}5 \text{ a } 0{,}6\text{ mm}$) & Ultra-alta resolução nativa ($0{,}2 \times 0{,}2\text{ mm}^2$ no isocentro sem septos) \\
    \addlinespace[0.4em]
    Capacidade Espectral \cite{willemink2018, rajendran2021} & Requer dupla fonte de raios X ou comutação rápida de kVp & Multi-energia espectral intrínseca em cada varredura via múltiplos canais de energia \\
    \bottomrule
  \end{tabularx}
  \vspace{0.3em}\par\noindent{\footnotesize\textbf{Fonte:} Elaborada pelo autor (2026).}
\end{table}

\subsubsection{Decomposição Espectral, Tensores de Ruído e Otimização do Índice $d'(E_0)$}
A conexão primordial entre a PCCT e o paradigma TBIQ manifesta-se na formulação das imagens espectrais multi-energia. Ao classificar cada fóton em $K$ canais de energia distintos ($E_1, E_2, \dots, E_K$) delimitados por limiares eletrônicos, o tomógrafo obtém sinogramas espectrais simultâneos que permitem a decomposição em materiais de base (como água, iodo e cálcio) \cite{rajendran2021, pimenta2026}:
\begin{equation}
  \mu(\mathbf{r}, E) = c_{\text{água}}(\mathbf{r}) f_{\text{água}}(E) + c_{\text{iodo}}(\mathbf{r}) f_{\text{iodo}}(E) + c_{\text{cálcio}}(\mathbf{r}) f_{\text{cálcio}}(E)
  \label{eq:decomposicao_materiais_base}
\end{equation}
onde $c_m(\mathbf{r})$ são os mapas de concentração dos materiais de base e $f_m(E)$ são suas curvas de atenuação mássica características.

A partir desses mapas, geram-se Imagens Monoenergéticas Virtuais ($VMI$) em qualquer nível de energia monoenergética $E_0 \in [40, 190]\text{ keV}$:
\begin{equation}
  I_{VMI}(\mathbf{r}; E_0) = c_{\text{água}}(\mathbf{r}) \left(\frac{\mu}{\rho}\right)_{\text{água}}(E_0) + c_{\text{iodo}}(\mathbf{r}) \left(\frac{\mu}{\rho}\right)_{\text{iodo}}(E_0)
  \label{eq:vmi_formula}
\end{equation}

É precisamente nesta etapa que todas as métricas escalares tradicionais ($SNR, CNR$) falham de forma irremediável:
\begin{enumerate}
  \item \textbf{Correlação Cruzada entre Canais Espectrais:} O processo de inversão não linear de materiais de base introduz uma forte autocovariância cruzada negativa entre os canais de energia. O ruído em uma imagem $VMI(E_0)$ não é mais um escalar $\sigma_{\text{HU}}$, mas sim uma combinação linear de tensores de ruído correlacionados;
  \item \textbf{Espectro de Potência de Ruído Matricial:} A descrição estocástica rigorosa da PCCT exige uma matriz espectral de densidade de potência de ruído $\mathbf{NPS}(u, v) \in \mathbb{R}^{K \times K}$, onde os elementos fora da diagonal representam o ruído espectral cruzado inter-canais \cite{pimenta2026};
  \item \textbf{Otimização da Energia $VMI$ pelo Índice $d'(E_0)$:} Em baixas energias (40 a 50 keV), o contraste do iodo ($Z=53$) cresce exponencialmente devido à proximidade com sua borda K ($K_{\text{edge}} = 33{,}2\text{ keV}$). Contudo, o fluxo de fótons emergentes nessa faixa é reduzido, elevando o ruído espectral. O cálculo da qualidade não pode ser feito pelo $CNR$ simples, mas exclusivamente pela integração contínua do índice de detectabilidade multi-espectral da tarefa $d'(E_0)$:
  \begin{equation}
    d'^2(E_0) = \int \int \frac{\left| TTF(u, v; E_0) \right|^2 \left| W_{\text{task}}(u, v) \right|^2 \left[ E(u, v) \right]^2}{NPS(u, v; E_0)} \, du \, dv
    \label{eq:dprime_vmi_spectral}
  \end{equation}
  A curva $d'(E_0)$ apresenta um pico global bem definido entre 45 e 50 keV, estabelecendo o ponto ótimo de operação física para tarefas vasculares e oncológicas contrastadas.
\end{enumerate}

\subsubsection{Desafios Físicos e Limitações Tecnológicas dos Detectores PCCT}
\label{subsubsec:desafios_fisicos_pcct}
Apesar das vantagens metrológicas dos detectores de contagem de fótons, a física do estado sólido impõe fenômenos estocásticos complexos que constituem desafios de ponta na engenharia biomédica \cite{willemink2018, rajendran2021, mccollough2026}:
\begin{itemize}
  \item \textbf{Compartilhamento de Carga (*Charge Sharing*):} Quando um fóton X interage próximo à fronteira entre dois sub-pixels do semicondutor, a nuvem de elétrons e lacunas divide-se entre anodos vizinhos. Se a carga individual em cada anodo não atingir o limiar de discriminação, o evento pode ser perdido; alternativamente, se ambos registrarem pulsos parciais, o fóton único é computado erroneamente como dois fótons de menor energia, distorcendo o espectro;
  \item \textbf{Empilhamento de Pulsos (*Pulse Pile-Up*):} Em regimes de altíssima taxa de contagem (altos valores de mA em tomografias de corpo inteiro em pacientes obesos), a taxa de chegada de fótons supera a constante de tempo de decaimento do circuito de conformação de pulsos do ASIC. Pulsos consecutivos sobrepõem-se no tempo, fazendo com que dois fótons de baixa energia sejam contados como um único fóton de alta energia (subcontagem e endurecimento espectral artificial);
  \item \textbf{Fluorescência de Raios X Característicos (*K-Escape*):} A fotoabsorção em átomos pesados de cádmio ($K_{\text{edge}} = 26{,}7\text{ keV}$) e telúrio ($K_{\text{edge}} = 31{,}8\text{ keV}$) induz a emissão de fótons de fluorescência característicos que podem escapar do sub-pixel de origem e ser absorvidos em pixels adjacentes, gerando contagens espúrias nos canais de baixa energia.
\end{itemize}

\subsection{Otimização Multiobjetivo de Pareto $(D, T, -d')$ e Discussão Clínica na Angiotomografia Coronariana}
\label{subsec:pareto_multiobjetivo_ccta}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.98\textwidth]{fig5_dlmo_pareto_3d.png}{Modelagem Numérica Sintética da Otimização Multiobjetivo de Pareto.}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -d')$ \cite{deb2002, hwang1981, rajendran2021}.}
  \label{fig:pareto_3d}
\end{figure}

A modelagem sintética apresentada na \cref{fig:pareto_3d} ilustra a tomada de decisão multiobjetivo em física médica estruturada a partir dos parâmetros formais da \cref{tab:parametros_simulacao}:
\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação da Fronteira de Compromisso Dose vs. Detectabilidade:}
  Modelou-se analiticamente o espaço de soluções através de funções de compromisso físico não-lineares. A curva contínua verde delimita a Fronteira de Pareto de soluções não-dominadas, onde é impossível aumentar a detectabilidade $d'$ (ou $\text{SSW-}d'$) sem elevar a dose de radiação $D$. Destacam-se três soluções ótimas de compromisso: $P_1$ (protocolo de ultrabaixa dose pediátrico), $P_2$ (exame ambulatorial balanceado) e $P_3$ (protocolo de emergência com máxima detectabilidade diagnóstica). Os pontos cinzas dispersos representam protocolos subótimos dominados;

  \item \textbf{Painel (B) --- Simulação da Superfície de Pareto Tridimensional $(D, T, -d')$:}
  Modelou-se uma variedade contínua tridimensional integrando tempo de rotação e varredura ($T$), dose absorvida ($D$) e detectabilidade diagnóstica ponderada ($d'$ ou $\text{SSW-}d'$). A simulação ilustra a tomada de decisão clínica multicritério através do acoplamento entre o algoritmo genético NSGA-II e o método de ordenação por similaridade à solução ideal TOPSIS \cite{deb2002, hwang1981}, permitindo selecionar a parametrização do tomógrafo PCCT que maximiza a detectabilidade sob restrições severas de dose e tempo de varredura ($T \le 2\text{ s}$).
\end{enumerate}

\subsubsection{Discussão Clínica: Angiotomografia Coronariana e a Tarefa Interpretativa}
A combinação dos detectores PCCT com a síntese de imagens $VMI$ e a otimização de Pareto resolve um dos maiores desafios da cardiologia diagnóstica: a avaliação de estenose luminal em artérias coronárias com calcificações parietais extensas em pacientes nefropatas.

Em tomógrafos convencionais EID, as placas de ateroma densamente calcificadas ($> 800\text{ HU}$) geram artefatos severos de endurecimento de feixe e espalhamento com efeito de alargamento luminoso (\emph{blooming}), que extravasa para a luz arterial e superestima o grau de estenose, levando pacientes assintomáticos a cateterismos cardíacos e angioplastias desnecessárias. Além disso, o ruído eletrônico dos detectores EID em baixas doses impede o uso de feixes de menor energia.

\paragraph{Impacto na Tarefa Interpretativa do Radiologista:} Na PCCT, os pixels de detecção direta de $0{,}2\text{ mm}$ e a ausência de septos reflexivos conferem resolução espacial suficiente para delimitar a placa calcificada sem \emph{blooming}. Concomitantemente, a reconstrução de $VMI$ em $45\text{ keV}$ eleva o coeficiente de atenuação fotoelétrico do iodo em mais de três vezes em relação ao feixe policromático padrão de $120\text{ kVp}$. Essa amplificação do contraste intravascular viabiliza a redução do volume de meio de contraste iodado injetado em até $60\%$, prevenindo a nefropatia induzida por contraste em pacientes idosos, diabéticos e renais crônicos.

A Fronteira de Pareto $(D, T, -d')$ garante que o físico médico configure o tomógrafo para atingir $d' \ge 4{,}5$ com tempo de aquisição inferior a um batimento cardíaco ($T < 0{,}25\text{ s}$). O médico radiologista e o cardiologista conseguem mensurar com extrema acurácia o diâmetro luminal residual da artéria coronária, diferenciar placas moles lipídicas vulneráveis de fibrose e descartar estenoses obstrutivas com elevado valor preditivo negativo, reduzindo custos hospitalares e evitando intervenções hemodinâmicas invasivas desnecessárias.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} A otimização multiobjetivo de Pareto formaliza matematicamente o princípio ALARA/ALADAIP no espaço $(D, T, -d')$, eliminando tentativas empíricas de calibração de protocolos.
  \item \emph{Vantagens sobre Métricas Anteriores:} Integra simultaneamente grandezas concorrentes (dose, velocidade e qualidade baseada em tarefa) em uma superfície contínua de decisões não-dominadas.
  \item \emph{Limitações do Modelo:} A convergência do algoritmo NSGA-II requer funções objetivo analíticas calibradas para cada anatomia e tarefa clínica específica.
\end{itemize}

\section{Pipeline Metrológico AAPM TG-233}
\label{sec:pipeline_tg233_completo}

\begin{figure}[htbp]
  \centering
  \incluirfigura[width=0.96\textwidth]{flow6_software_pipeline.png}{Estrutura Conceitual do Pipeline Metrológico segundo AAPM TG-233.}
  \caption[Pipeline Metrológico AAPM TG-233]{Pipeline Metrológico Padronizado segundo AAPM TG-233 \cite{aapm_tg233_2019, choopani2023}.}
  \label{fig:software_flow}
\end{figure}

Conforme consolidado na literatura internacional de metrologia tomográfica \cite{aapm_tg233_2019, choopani2023}, o processamento sistemático de imagens para avaliação baseada em tarefa organiza-se em cinco etapas conceituais encadeadas (\cref{fig:software_flow}):
\begin{enumerate}
  \item \textbf{Etapa 1 (Extração e Validação de Metadados DICOM):} Leitura sistemática dos cabeçalhos dos exames, extraindo parâmetros de irradiação ($\text{kVp}$, $\text{mA}$, tempo de rotação, $\text{CTDI}_{\text{vol}}$, $\text{DLP}$), geometria de aquisição (espessura de corte, espaçamento entre fatias, campo de visão FOV) e identificadores de reconstrução (kernel, nível DLR/HIR);
  \item \textbf{Etapa 2 (Segmentação e Amostragem Espacial de ROIs):} Identificação das coordenadas espaciais dos insertos de calibração via Transformada de Hough circular e extração de $M \ge 100$ regiões de interesse homogêneas independentes para amostragem estocástica do ruído em baterias de múltiplos simuladores ($D_w$);
  \item \textbf{Etapa 3A (Cálculo da Resolução Espacial da Tarefa):} Construção da Função de Resposta ao Degrau superamostrada ($\text{ESF}(r)$), derivação numérica da $\text{LSF}(r)$ e aplicação da Transformada Rápida de Fourier para obtenção da $TTF(f)$ e dos descritores $f_{50}$ e $f_{10}$;
  \item \textbf{Etapa 3B (Processamento Espectral do Ruído):} Aplicação do detrending polinomial bidimensional de 2ª ordem $P_2(x, y)$, janelamento de Hanning para contenção de vazamento espectral e FFT2D, gerando a matriz $NPS(u, v)$ e a curva radial integrada $NPS(f)$;
  \item \textbf{Etapa 4 (Integração dos Observadores de Modelo e SSW-$d'$):} Avaliação do índice de detectabilidade $d'$ através dos modelos analíticos lineares (NPWE e CHO com canais corticais D-DOG/Laguerre-Gauss), modelagem não-linear e cômputo da métrica ponderada por tamanho e tarefa SSW-$d'$ acoplada à $\text{FOM}_{\text{SSW}}$;
  \item \textbf{Etapa 5 (Análise de Incerteza e Relatório de Conformidade):} Reamostragem estatística por Bootstrap ($B = 2000$) para cálculo de intervalos de confiança de 95\% e emissão de laudo técnico de qualidade.
\end{enumerate}

\paragraph{Síntese Metrológica do Pipeline:} O pipeline estruturado pelo relatório AAPM TG-233 unifica a cadeia metrológica em um fluxo algorítmico automatizado e auditável, garantindo que o serviço de física médica hospitalar monitore a conformidade dos tomógrafos com rigor metrológico e forneça imagens com índice $d'$ calibrado para as tarefas clínicas mais desafiadoras.

\section{Diretrizes Regulatórias e Bioéticas}
\label{sec:bioetica_regulacao}

\subsection{Enquadramento Regulatório, Bioética e Auditoria Dosimétrica em TC Pediátrica e Politrauma}
\label{subsec:bioetica_regulacao_pediatria_consolidada}

\subsubsection{Enquadramento Regulatório e Salvaguardas Éticas}
A condução de experimentos psicofísicos com médicos radiologistas (leituras 2AFC e MRMC) e a otimização de protocolos clínicos demandam o estrito cumprimento de salvaguardas éticas e legais:
\begin{itemize}
  \item \textbf{Submissão ao Sistema CEP/CONEP:} Todo protocolo envolvendo observadores humanos deve ser previamente aprovado por Comitê de Ética em Pesquisa, com aplicação do Termo de Consentimento Livre e Esclarecido (TCLE);
  \item \textbf{Anonimização DICOM e LGPD:} Remoção irreversível de identificadores de pacientes conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o padrão DICOM PS 3.15;
  \item \textbf{Ergonomia Visual Padronizada:} Calibração de monitores diagnósticos segundo a norma DICOM Grayscale Standard Display Function (GSDF / AAPM TG-18), com luminância controlada e ambiente com iluminância reduzida ($< 25\text{ lux}$).
\end{itemize}

\subsubsection{Discussão Clínica: TC Pediátrica, Politrauma e a Tarefa Interpretativa}
A fundamentação bioética e regulatória atinge sua máxima criticidade na tomografia computadorizada pediátrica em situações de urgência e politrauma infantil.

Crianças possuem expectativa de vida consideravelmente mais longa e tecidos em intensa proliferação celular, tornando-as até dez vezes mais suscetíveis à carcinogênese radioinduzida por unidade de dose em comparação a adultos (ICRP Publicação 103, \cref{sec:paradigma_dosimetrico}). Na avaliação de trauma abdominal fechado em pacientes pediátricos, a tarefa diagnóstica crucial é a identificação rápida de pequenas lacerações esplênicas ou hepáticas e de hemoperitônio livre na cavidade peritoneal.

\paragraph{Impacto na Tarefa Interpretativa do Radiologista:} A aplicação cega de protocolos de adultos ou a aceitação desprovida de validação metrológica de reduções extremas de dose em softwares de IA viola diretamente os princípios da Bioética Médica (Princípios de Beneficência e Não-Maleficência de Beauchamp e Childress). Se a dose for reduzida sem a verificação do $d'_{\text{CHO}}$ para o contraste específico de sangue intraperitoneal não coagulado ($\Delta C \approx 30\text{ a } 45\text{ HU}$ contra parênquima visceral), uma lesão esplênica com sangramento ativo pode passar despercebida, evoluindo para choque hipovolêmico fatal.

Por outro lado, o uso de doses desnecessariamente altas viola a Resolução ANVISA RDC 611/2022 e o princípio da limitação de risco. A sistematização metrológica baseada em tarefa proposta nesta monografia fornece ao físico médico o instrumento científico objetivo necessário para auditar protocolos pediátricos, garantindo que o tomógrafo opere na coordenada exata da Fronteira de Pareto que minimiza o $\text{CTDI}_{\text{vol}}$ e o $\text{SSDE}$ sem comprometer em nenhum milésimo a probabilidade de detecção de lesões viscerais agudas.

\paragraph{Síntese do Subcapítulo e Balanço Metrológico:}
\begin{itemize}
  \item \emph{Impacto Metrológico:} Vincula a bioética médica e a conformidade regulatória (RDC ANVISA 611/2022, ICRP 103) à otimização matemática rigorosa do índice de detectabilidade e da dose específica por tamanho ($\text{SSDE}$).
  \item \emph{Vantagens sobre Métricas Anteriores:} Substitui o empirismo na escolha de doses pediátricas por uma auditoria física objetiva e reprodutível baseada na tarefa clínica de urgência e na biometria do paciente.
  \item \emph{Limitações do Modelo:} Requer conscientização institucional e integração contínua entre a equipe de física médica e o corpo clínico da radiologia pediátrica.
\end{itemize}

% ------------------------------------------------------------------------------
% CAPÍTULO 5: CONCLUSÃO
% ------------------------------------------------------------------------------
\chapter{Conclusão}
\label{chap:conclusao}

A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram a mais profunda transformação metodológica e conceitual de sua história nas últimas décadas. Esta monografia realizou uma revisão bibliográfica sistemática abrangente e uma modelagem teórico-metrológica unificada, mapeando a transição das métricas escalares lineares clássicas para as formulações perceptuais contemporâneas baseadas em inteligência artificial e detectores de contagem de fótons.

\section{Síntese das Contribuições}
\label{sec:sintese_contribuicoes_finais}
As conclusões centrais desta investigação estruturam-se em cinco eixos fundamentais, fechando de forma harmônica as problematizações levantadas no Capítulo de Introdução:
\begin{enumerate}
  \item Superação Epistemológica das Métricas Escalares: Demonstrou-se formalmente que grandezas como $SNR$, $CNR$, $\sigma_{\text{HU}}$ e $MTF$ são inadequadas para a caracterização de sistemas tomográficos não lineares (DLR e MBIR). Sob tais algoritmos, a redução puramente escalar do desvio padrão induz a falsa premissa de ganho de qualidade, mascarando alterações texturais severas (efeito ceroso) e o borramento de lesões sutis de baixo contraste;
  \item Consolidação do Paradigma TBIQ (AAPM TG-233): Apresentaram-se as deduções matemáticas contínuas completas no domínio de Fourier ($TTF$, $NPS$, $E(f)$ e $W_{\text{task}}$), formalizando o Índice de Detectabilidade ($d'$) como a grandeza física central, reprodutível e objetiva recomendada internacionalmente;
  \item Formalização Populacional e Dosimétrica do SSW-$d'$: Sistematizou-se a dedução do Índice de Detectabilidade Ponderado pelo Tamanho e Tarefa (SSW-$d'$) acoplado à Estimativa de Dose Específica por Tamanho (SSDE, AAPM 204), estabelecendo a Figura de Mérito ($\text{FOM}_{\text{SSW}}$) como o padrão ouro para a otimização de coortes clínicas populacionais inteiras;
  \item Limites de Validade dos Modelos Lineares Clássicos: Evidenciaram-se as causas matemáticas pelas quais o modelo antropomórfico NPWE perde correlação com leitores humanos sob DLR ($r \approx 0{,}68$), justificando a necessidade dos observadores profundos DLMO baseados em Vision Transformers ($r > 0{,}95$);
  \item Integração Multicritério em PCCT: Sistematizou-se a física dos detectores de contagem de fótons e demonstrou-se como a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -\text{SSW-}d')$ viabiliza protocolos clínicos balanceados entre dose mínima, tempo ultra-rápido e máxima eficácia diagnóstica.
\end{enumerate}

\section{Implicações para a Física Médica Hospitalar}
\label{sec:implicacoes_pratica_hospitalar}
Os resultados e modelos sistematizados fornecem suporte direto para:
\begin{itemize}
  \item A estruturação de programas hospitalares avançados de garantia da qualidade alinhados à RDC ANVISA 611/2022, ao relatório AAPM TG-233 e à dosimetria SSDE (AAPM 204/220);
  \item A calibração técnica e os testes de aceitação de novos tomógrafos equipados com inteligência artificial e detectores PCCT;
  \item A capacitação de físicos médicos especialistas para intervir criticamente na otimização de protocolos clínicos em coortes adultas e pediátricas sem depender exclusivamente de critérios subjetivos ou métricas escalares obsoletas.
\end{itemize}

\section{Limitações}
\label{sec:limitacoes_estudo_finais}
Por se tratar de uma monografia de revisão bibliográfica sistemática e modelagem teórico-metrológica, as curvas e superfícies foram geradas através de simulações numéricas sintéticas controladas codificadas em Python pelo autor, sem a realização de ensaios experimentais primários com pacientes ou simuladores de bancada proprietários. Trabalhos empíricos futuros poderão aplicar diretamente este corpo teórico em ambientes laboratoriais e hospitalares.

\section{Perspectivas Futuras}
\label{sec:perspectivas_futuras_finais}
A evolução contínua da física de imagens médicas aponta para direções de vanguarda:
\begin{enumerate}
  \item Extensão para Imagens 4D Dinâmicas: Aplicação de modelos perceptivos e SSW-$d'$ em tomografias temporais dinâmicas (angiotomografia coronariana com sincronização cardíaca e perfusão cerebral em AVC), incorporando a Função de Transferência Temporal ($TTF_t(f_t)$);
  \item Modelos Multimodais de Visão e Linguagem: Integração de \emph{Vision-Language Models} e \emph{Foundation Models} em saúde para gerar observadores computacionais universais que forneçam laudos estruturados com mapeamento de incerteza;
  \item Mapeamento Espectral Multielementar em PCCT: Quantificação simultânea de múltiplos agentes de contraste com bordas K distintas (nanopartículas de ouro, gadolínio, bismuto e tântalo) para diagnóstico teranóstico molecular;
  \item Estudos Psicofísicos Multicêntricos em Larga Escala: Condução de experimentos 2AFC com consórcios hospitalares para consolidação de bancos de dados públicos de calibração metrológica populacional.
\end{enumerate}

Conclui-se esta monografia com a certeza de que a física médica, ao integrar os fundamentos da mecânica quântica de radiações, o processamento estatístico de sinais e a neurociência da percepção visual, estabelece os alicerces definitivos para uma radiologia diagnóstica mais segura, precisa e personalizada.

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

\bibitem{rose1948}
ROSE, A. The sensitivity performance of the human eye on an absolute scale. \textbf{Journal of the Optical Society of America}, v. 38, n. 2, p. 196--208, 1948.

\bibitem{burgess1999}
BURGESS, A. E. The Rose model, revisited. \textbf{Journal of the Optical Society of America A}, v. 16, n. 3, p. 633--646, 1999.

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

\bibitem{aapm_report204}
AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Size-Specific Dose Estimates (SSDE) in Pediatric and Adult Body CT Examinations}. AAPM Report No. 204. College Park, MD: AAPM, 2011. 76 p.

\bibitem{icru54_1996}
INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). \textbf{Medical Imaging - The Assessment of Image Quality}. ICRU Report 54. Bethesda, MD: ICRU, 1996. 88 p.

\bibitem{page2021}
PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. \textbf{BMJ}, v. 372, n. 71, p. n71, 2021.

\bibitem{peterson1954}
PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. \textbf{Transactions of the IRE Professional Group on Information Theory}, v. 4, n. 4, p. 171--212, 1954.

\bibitem{lusted1968}
LUSTED, L. B. \textbf{Introduction to Medical Decision Making}. Springfield, IL: Charles C. Thomas, 1968. 271 p.

\bibitem{metz1986}
METZ, C. E. ROC methodology in radiologic imaging. \textbf{Investigative Radiology}, v. 21, n. 9, p. 720--733, 1986.

\bibitem{barrett_myers_2004}
BARRETT, H. H.; MYERS, K. J. \textbf{Foundations of Image Science}. Hoboken, NJ: John Wiley \& Sons, 2004. 1584 p.

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

\bibitem{dorfman1992}
DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E. Receiver operating characteristic rating analysis: generalization to the population of readers and cases with the jackknife method. \textbf{Investigative Radiology}, v. 27, n. 9, p. 723--731, 1992.

\bibitem{obuchowski1995}
OBUCHOWSKI, N. A. Multireader, multicase ROC analysis: an empirical comparison of five methods. \textbf{Academic Radiology}, v. 2, p. S78--S82, 1995.

\bibitem{hillis2011}
HILLIS, S. L. A comparison of the Dorfman-Berbaum-Metz and Obuchowski-Rockette methods for assessing the significance of difference between ROC areas with multiple readers. \textbf{Statistics in Medicine}, v. 30, n. 14, p. 1754--1770, 2011.

\bibitem{racine2021}
RACINE, D. et al. Task-based performance of model observers compared to human radiologists in CT with deep learning reconstruction: a multi-reader multi-case study. \textbf{European Radiology}, v. 31, n. 9, p. 6800--6810, 2021.

\bibitem{fitton2026}
FITTON, I. et al. Size-specific weighted detectability index (SSW-$d'$): a population-based task-based image quality metric for CT protocol optimization. \textbf{Medical Physics}, v. 53, n. 3, p. 1420--1435, 2026.

\bibitem{goppel2021}
GÖPPEL, M. et al. Task-based image quality assessment in pediatric and adult CT using multi-size phantoms and model observers. \textbf{Physica Medica}, v. 84, p. 150--160, 2021.

\bibitem{vaswani2017}
VASWANI, A. et al. Attention is all you need. In: \textbf{Advances in Neural Information Processing Systems (NeurIPS 2017)}, Long Beach, CA, v. 30, p. 5998--6008, 2017.

\bibitem{dosovitskiy2020}
DOSOVITSKIY, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: \textbf{International Conference on Learning Representations (ICLR 2021)}, Virtual, p. 1--21, 2021.

\bibitem{willemink2018}
WILLEMINK, M. J. et al. Photon-counting CT: technical principles and clinical prospects. \textbf{Radiology}, v. 289, n. 2, p. 293--312, 2018.

\bibitem{rajendran2021}
RAJENDRAN, K. et al. First clinical photon-counting detector CT system: technical evaluation. \textbf{Radiology}, v. 303, n. 1, p. 130--138, 2021.

\bibitem{deb2002}
DEB, K. et al. A fast and elitist multiobjective genetic algorithm: NSGA-II. \textbf{IEEE Transactions on Evolutionary Computation}, v. 6, n. 2, p. 182--197, 2002.

\bibitem{hwang1981}
HWANG, C. L.; YOON, K. \textbf{Multiple Attribute Decision Making: Methods and Applications}. Berlin: Springer-Verlag, 1981. 259 p.

\bibitem{choopani2023}
CHOOPANI, S. et al. Automated task-based image quality assessment in clinical CT using open-source tools: implementation and validation. \textbf{Physics in Medicine \& Biology}, v. 68, n. 12, p. 125015, 2023.

\bibitem{pimenta2026}
PIMENTA, E. F. \textbf{Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax}. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.

\end{thebibliography}

\end{document}
'''

with open('/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/main.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code.strip() + '\n')

print("main.tex successfully written! Size:", len(latex_code))
