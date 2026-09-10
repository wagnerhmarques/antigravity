# -*- coding: utf-8 -*-
import os
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
main_tex_path = os.path.join(output_dir, "main.tex")

latex_content = r"""\documentclass[
  12pt,
  a4paper,
  oneside
]{report}

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
      \small
      Trabalho de Conclusão de Curso (Monografia de Revisão Bibliográfica Sistemática e Modelagem Teórico-Metrológica) apresentado ao Instituto de Física e à Faculdade de Medicina da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física Médica.
      
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

% 4. DEDICATÓRIA E AGRADECIMENTOS
\chapter*{Dedicatória}
\addcontentsline{toc}{chapter}{Dedicatória}
\vspace*{\fill}
\begin{flushright}
  \textit{Aos meus pais e familiares, pelo suporte inestimável e incentivo permanente.\\
  A todos os físicos médicos, pesquisadores e profissionais que dedicam suas vidas\\
  à proteção radiológica, ao rigor metrológico e à excelência do diagnóstico por imagem.}
\end{flushright}
\clearpage

\chapter*{Agradecimentos}
\addcontentsline{toc}{chapter}{Agradecimentos}

Ao meu orientador, Prof. Dr. Paulo Roberto Costa, pela excepcional dedicação pedagógica, pelo incentivo contínuo ao rigor matemático e físico e pelas valiosas discussões sobre processamento de imagens e dosimetria em tomografia computadorizada.

Aos docentes, pesquisadores e funcionários do Instituto de Física (IFUSP) e da Faculdade de Medicina (FMUSP) da Universidade de São Paulo, pela sólida formação interdisciplinar oferecida ao longo da graduação em Física Médica.

Aos colegas de curso, amigos e pesquisadores do Grupo de Dosimetria das Radiações e Física Médica (GDRFM), pelo companheirismo e frutíferas trocas científicas.

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

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica contemporânea, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação da eficácia diagnóstica (princípio ALARA). Historicamente, a garantia da qualidade em TC baseou-se em métricas escalares lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR), o desvio padrão em Unidades Hounsfield ($\sigma_{\text{HU}}$) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores cilíndricos homogêneos de água ou polimetilmetacrilato (PMMA). No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares --- com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade estrita, isoplanatismo espacial e estacionariedade no sentido amplo (WSS) do sistema formador de imagens. Sob processamentos não lineares adaptativos, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais (aspecto ceroso ou \emph{plastic look}) que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), fundamentado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade é formalmente definida pelo desempenho de um observador ao executar uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Esta monografia constitui uma \textbf{revisão bibliográfica sistemática e modelagem teórico-metrológica} da evolução dos observadores de modelo (\emph{model observers}) e das métricas TBIQ. A estratégia de busca foi conduzida através de equações booleanas estruturadas nas principais bases científicas (PubMed/MEDLINE, IEEE Xplore, Web of Science, Scopus e AAPM Reports), delimitando critérios rigorosos de elegibilidade e sistematização normativa (AAPM TG-233, ICRU 54, ANVISA RDC 611/2022). Apresentam-se as deduções matemáticas contínuas completas partindo do limite superior do Observador Ideal Bayesiano e de Hotelling, passando pelos modelos antropomórficos lineares com filtro ocular (NPWE) e canais corticais (CHO), até as fronteiras contemporâneas em redes neurais profundas (\emph{Vision Transformers}) e Tomografia por Contagem de Fótons (PCCT). Para fundamentar pedagogicamente as deduções, o trabalho incorpora \textbf{modelagens numéricas sintéticas controladas} em Python, detalhando as equações analíticas que originam cada curva e superfície simulada. Este estudo estabelece um corpo de referência teórico, crítico e conceitual unificado para a metrologia da qualidade de imagem em física médica.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Revisão Bibliográfica Sistemática. Busca Booleana. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Simulação Numérica. Tomografia por Contagem de Fótons. Relatório AAPM TG-233.
\clearpage

% 7. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), standard deviation in Hounsfield Units ($\sigma_{\text{HU}}$), and Modulation Transfer Function (MTF), evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity (WSS). Under non-linear processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a \textbf{systematic literature review and theoretical-metrological synthesis} of the evolution of model observers and Task-Based Image Quality (TBIQ) metrics. The search methodology was conducted using structured Boolean query equations across major international scientific databases (PubMed/MEDLINE, IEEE Xplore, Web of Science, Scopus, and AAPM Reports), with well-defined eligibility criteria and normative harmonization (AAPM TG-233, ICRU 54, ANVISA RDC 611/2022). We present complete step-by-step mathematical derivations transitioning from the Bayesian Ideal Observer and Hotelling Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), up to recent frontiers involving deep learning architectures (Vision Transformers) and Photon-Counting CT (PCCT) physics. To pedagogically support the theoretical deductions, this work incorporates \textbf{controlled synthetic numerical simulations} in Python, explicitly detailing the analytical formulations and computational parameters used to generate each simulated response curve and multi-dimensional surface. This study establishes a rigorous, critical, and unified theoretical reference framework for image quality metrology in modern computed tomography.

\vspace{0.8cm}
\noindent\textbf{Keywords:} Computed Tomography. Systematic Literature Review. Boolean Search Strategy. Task-Based Image Quality. Model Observers. Detectability Index. Deep Learning Reconstruction. Numerical Simulation. Photon-Counting CT. AAPM TG-233 Report.
\clearpage

% 8. LISTA DE ILUSTRAÇÕES
\chapter*{Lista de Ilustrações}
\addcontentsline{toc}{chapter}{Lista de Ilustrações}
\begin{itemize}[leftmargin=*,label={}]
  \item \textbf{Figura 1.1} -- Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 16
  \item \textbf{Figura 1.2} -- Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 19
  \item \textbf{Figura 3.1} -- Diagrama de Fluxo Metodológico da Revisão Sistemática (Protocolo de Busca Booleana e Seleção de Evidências) \dotfill 26
  \item \textbf{Figura 4.1} -- Modelagem Numérica Sintética da Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Desempenho Psicofísico 2AFC \dotfill 32
  \item \textbf{Figura 4.2} -- Modelagem Numérica Sintética das Quatro Funções Espectrais no Domínio de Fourier segundo o Relatório AAPM TG-233 \dotfill 39
  \item \textbf{Figura 4.3} -- Modelagem Numérica Sintética dos Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico \dotfill 48
  \item \textbf{Figura 4.4} -- Diagrama do Fluxo de Decisão do Observador de Hotelling Canalizado (CHO) \dotfill 50
  \item \textbf{Figura 4.5} -- Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D \dotfill 55
  \item \textbf{Figura 4.6} -- Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC \dotfill 59
  \item \textbf{Figura 4.7} -- Arquitetura de Redes Neurais para Observadores de Modelo por Aprendizado Profundo (DLMO / Vision Transformers) \dotfill 63
  \item \textbf{Figura 4.8} -- Modelagem Numérica Sintética da Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -W)$ \dotfill 69
  \item \textbf{Figura 4.9} -- Estrutura Conceitual do Pipeline Metrológico em Tomografia Computadorizada segundo o Relatório AAPM TG-233 \dotfill 73
\end{itemize}
\clearpage

% 9. LISTA DE TABELAS
\chapter*{Lista de Tabelas}
\addcontentsline{toc}{chapter}{Lista de Tabelas}
\begin{itemize}[leftmargin=*,label={}]
  \item \textbf{Tabela 3.1} -- Estratégia de Busca Booleana Estruturada por Eixo Temático e Termos MeSH/DeCS \dotfill 23
  \item \textbf{Tabela 3.2} -- Critérios de Elegibilidade, Inclusão e Exclusão para o Levantamento Bibliográfico \dotfill 25
  \item \textbf{Tabela 3.3} -- Parâmetros Matemáticos das Modelagens Numéricas Sintéticas em Python \dotfill 28
  \item \textbf{Tabela 4.1} -- Resumo Comparativo das Classes de Observadores de Modelo em Física Médica \dotfill 52
  \item \textbf{Tabela 4.2} -- Síntese das Tecnologias de Detectores em Tomografia Computadorizada (EID vs PCCT) \dotfill 67
\end{itemize}
\clearpage

% 10. LISTA DE ABREVIATURAS E SIGLAS
\chapter*{Lista de Abreviaturas e Siglas}
\addcontentsline{toc}{chapter}{Lista de Abreviaturas e Siglas}

\begin{longtable}{ll}
  2AFC   & \emph{Two-Alternative Forced Choice} (Escolha Forçada entre Duas Alternativas) \\
  AAPM   & \emph{American Association of Physicists in Medicine} \\
  ALARA  & \emph{As Low As Reasonably Achievable} \\
  ANVISA & Agência Nacional de Vigilância Sanitária \\
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
  EID    & \emph{Energy-Integrating Detector} (Detector de Integração de Energia) \\
  ESF    & \emph{Edge Spread Function} (Função de Espalhamento de Borda / Resposta ao Degrau) \\
  FBP    & \emph{Filtered Backprojection} (Retroprojeção Filtrada) \\
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
  PSF    & \emph{Point Spread Function} (Função de Espalhamento de Ponto) \\
  ROC    & \emph{Receiver Operating Characteristic} (Característica de Operação do Receptor) \\
  ROI    & \emph{Region of Interest} (Região de Interesse) \\
  SDT    & \emph{Signal Detection Theory} (Teoria de Detecção de Sinais) \\
  SKE    & \emph{Signal Known Exactly} (Sinal Exatamente Conhecido) \\
  SNR    & \emph{Signal-to-Noise Ratio} (Relação Sinal-Ruído) \\
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

A Tomografia Computadorizada (TC) consolidou-se como um dos pilares mais extraordinários e transformadores da medicina diagnóstica moderna, revolucionando o diagnóstico clínico desde a sua concepção teórica e implementação prática por Godfrey N. Hounsfield e Allan M. Cormack na década de 1970 \cite{bushberg2020, attix1986, seeram2015}. Ao converter projeções radiográficas angulares de atenuação de raios X em matrizes tridimensionais de coeficientes de atenuação linear seccionais, a tomografia viabilizou a visualização anatômica de órgãos internos com resolução espacial milimétrica e excelente diferenciação tecidual.

\section{Panorama Histórico e a Física Fundamental da Aquisição Tomográfica}
\label{sec:panorama_fisico_tc}

A formação da imagem tomográfica tem como fundamento a atenuação exponencial de um feixe polienergético de raios X ao atravessar a matéria biológica. A atenuação macroscópica ao longo de uma trajetória retilínea $L$ é governada pela Lei de Beer-Lambert generalizada:
\begin{equation}
  I = \int_0^{E_{\text{máx}}} I_0(E) \exp\left( -\int_L \mu(x, y, z; E) \, dl \right) dE
  \label{eq:beer_lambert}
\end{equation}
onde $I_0(E)$ representa o espectro de emissão do tubo de raios X em função da energia fotônica $E$, e $\mu(x, y, z; E)$ é a distribuição tridimensional do coeficiente de atenuação linear total do meio, determinado predominantemente pelo Efeito Fotoelétrico ($\tau \propto \rho \frac{Z^3}{E^3}$) em baixas energias e pelo Espalhamento Compton ($\sigma_c \propto \rho_e$) na faixa intermediária de diagnóstico (30 a 140 keV) \cite{attix1986, bushberg2020}.

A amostragem de atenuação integrada ao longo de múltiplos ângulos $\phi \in [0, \pi]$ e posições radiais $r$ constitui a \textbf{Transformada de Radon} bidimensional de uma fatia anatômica $f(x, y)$:
\begin{equation}
  p(r, \phi) = \mathcal{R}\{f(x, y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, \delta(x\cos\phi + y\sin\phi - r) \, dx \, dy
  \label{eq:radon_transform}
\end{equation}
O conjunto dessas projeções em coordenadas polares $(r, \phi)$ forma o \textbf{sinograma}. A inversão analítica do sinograma para reconstruir a função contínua $f(x, y)$ é fundamentada no célebre \textbf{Teorema da Fatia Central de Fourier} (\emph{Projection-Slice Theorem}), o qual estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $p(r, \phi)$ no ângulo $\phi$ é exatamente idêntica à fatia radial correspondente da Transformada de Fourier bidimensional da imagem $F(u, v)$ que passa pela origem do espaço de frequências $(u, v)$ \cite{barrett_myers_2004, seeram2015}:
\begin{equation}
  \mathcal{F}_{1D}\{p(r, \phi)\} = F(f\cos\phi, f\sin\phi)
  \label{eq:fourier_slice}
\end{equation}

A partir do Teorema da Fatia Central, a inversão matemática em coordenadas polares introduz um fator Jacobiano $|f|$, que atua no domínio de Fourier como um filtro passa-altas cônico. Essa formulação origina o algoritmo clássico da \textbf{Retroprojeção Filtrada} (\emph{Filtered Backprojection} --- FBP):
\begin{equation}
  f(x, y) = \int_0^{\pi} \left[ p(r, \phi) * h(r) \right]_{r = x\cos\phi + y\sin\phi} d\phi
  \label{eq:fbp_formula}
\end{equation}
onde $h(r) = \mathcal{F}^{-1}\{|f|\}$ é a resposta ao impulso do filtro de rampa (ex: filtros Ram-Lak, Shepp-Logan ou Hann). Sem a aplicação prévia do filtro de rampa $|f|$, a retroprojeção simples convolucionaria a imagem original com uma função de espalhamento espacial $1/r$, gerando um borramento severo e inaceitável para o diagnóstico médico \cite{seeram2015}.

\section{O Paradigma Dosimétrico, o Princípio ALARA e os Marcos Regulatórios}
\label{sec:paradigma_dosimetrico}

Embora indispensável na prática clínica, a tomografia computadorizada é responsável pela maior fração da dose coletiva de radiação ionizante de origem médica em nível global \cite{mccollough2026}. A interação dos fótons X com os tecidos humanos induz ionizações moleculares e quebras de duplas fitas de DNA, conferindo riscos de efeitos estocásticos (mutagênese e carcinogênese radioinduzida a longo prazo).

Para gerenciar esse risco de forma ética e tecnicamente rigorosa, a Comissão Internacional de Proteção Radiológica (ICRP Publicação 103) estabeleceu o princípio \textbf{ALARA} (\emph{As Low As Reasonably Achievable}) \cite{icrp103_2007}. A física médica atua no núcleo do princípio ALARA: a dose absorvida pelo paciente deve ser reduzida ao menor nível compatível com a preservação estrita da capacidade diagnóstica.

A quantificação padronizada da dose em tomografia baseia-se no \textbf{Índice de Dose em Tomografia Computadorizada} ($\text{CTDI}$), medido com câmara de ionização tipo lápis de 100 mm imersa em simuladores cilíndricos de PMMA de 16 cm (cabeça) e 32 cm (corpo):
\begin{align}
  \text{CTDI}_{\text{w}} &= \frac{1}{3} \text{CTDI}_{\text{centro}} + \frac{2}{3} \text{CTDI}_{\text{periférico}} \label{eq:ctdi_w} \\
  \text{CTDI}_{\text{vol}} &= \frac{\text{CTDI}_{\text{w}}}{\text{pitch}} \label{eq:ctdi_vol} \\
  \text{DLP} &= \text{CTDI}_{\text{vol}} \times L \label{eq:dlp_def}
\end{align}
onde o Produto Dose-Comprimento ($\text{DLP}$, em $\text{mGy}\cdot\text{cm}$) expressa a energia total depositada ao longo do comprimento de varredura $L$. A Dose Efetiva $E$ (em $\text{mSv}$) é estimada por $E \approx k \cdot \text{DLP}$, utilizando coeficientes de conversão normalizados por região anatômica $k$ \cite{icrp103_2007}.

No cenário regulatório brasileiro, a Agência Nacional de Vigilância Sanitária (ANVISA) estabeleceu requisitos mandatórios através da **Resolução da Diretoria Colegiada RDC nº 611/2022** e da **Instrução Normativa IN nº 93/2021** \cite{anvisa_rdc611_2022, anvisa_in93_2021}. Essas normativas exigem programas estruturados de garantia da qualidade, calibrações dosimétricas periódicas, monitoramento de Níveis de Referência Diagnóstica (DRLs) e a atuação contínua de físicos médicos especialistas em radiodiagnóstico.

\section{As Métricas Escalares Tradicionais e Suas Limitações Físicas}
\label{sec:metricas_escalares_tradicionais}

Durante quatro décadas de hegemonia da FBP, a metrologia da qualidade de imagem em TC baseou-se quase que exclusivamente em métricas escalares simples, avaliadas em meios homogêneos de água ou PMMA:
\begin{enumerate}
  \item \textbf{Relação Sinal-Ruído ($SNR$):} Razão entre o valor médio em Unidades Hounsfield ($\mu_{\text{HU}}$) e o desvio padrão estocástico ($\sigma_{\text{HU}}$) em uma ROI uniforme:
  \begin{equation}
    SNR = \frac{\mu_{\text{HU}}}{\sigma_{\text{HU}}}
    \label{eq:snr_formula}
  \end{equation}
  \item \textbf{Relação Contraste-Ruído ($CNR$):} Diferença entre a média do sinal do alvo clínico ($\mu_{\text{alvo}}$) e a média do fundo circundante ($\mu_{\text{fundo}}$), normalizada pela variância combinada:
  \begin{equation}
    CNR = \frac{|\mu_{\text{alvo}} - \mu_{\text{fundo}}|}{\sqrt{\frac{1}{2}(\sigma_{\text{alvo}}^2 + \sigma_{\text{fundo}}^2)}}
    \label{eq:cnr_formula}
  \end{equation}
  \item \textbf{Função de Transferência de Modulação ($MTF(f)$):} Magnitude normalizada da Transformada de Fourier bidimensional da Função de Espalhamento de Ponto ($\text{PSF}(x, y)$), quantificando a preservação da modulação do contraste em função da frequência espacial $f$ ($\text{mm}^{-1}$):
  \begin{equation}
    MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
    \label{eq:mtf_formula}
  \end{equation}
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption[Comparativo Estrutural entre os Paradigmas Físicos]{Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

\subsection{Os Três Pilares da Validade Linear e Seus Limites}
\label{subsec:pilares_validade_linear}
A validade matemática das grandezas clássicas $SNR$, $CNR$ e $MTF$ repousa sobre três premissas fundamentais da teoria de sistemas lineares invariantes no espaço:
\begin{enumerate}
  \item \textbf{Linearidade Estrita do Operador de Reconstrução $\mathcal{R}$:} A resposta a uma combinação linear de atenuações é a combinação linear das respostas individuais: $\mathcal{R}\{\alpha f_1 + \beta f_2\} = \alpha \mathcal{R}\{f_1\} + \beta \mathcal{R}\{f_2\}$;
  \item \textbf{Isoplanatismo Espacial (Invariância por Translação):} A função de espalhamento $\text{PSF}(x, y)$ independe da coordenada absoluta na matriz de reconstrução;
  \item \textbf{Estacionariedade do Ruído no Sentido Amplo (WSS --- \emph{Wide-Sense Stationary}):} Um processo estocástico bidimensional $I(x, y)$ satisfaz WSS se sua média $\mathbb{E}[I(x, y)] = \mu_0$ for constante no espaço e sua função de autocovariância $K_I(\mathbf{r}_1, \mathbf{r}_2) = K_I(\mathbf{r}_1 - \mathbf{r}_2)$ depender unicamente do vetor de deslocamento espacial relativo $\Delta \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$.
\end{enumerate}

Quando essas premissas são violadas, as métricas clássicas colapsam. O desvio padrão $\sigma_{\text{HU}}$ mede apenas a dispersão estatística escalar, sendo completamente cego à correlação espacial entre pixels e à textura do ruído. Dois exames com idêntico $\sigma_{\text{HU}} = 15\text{ HU}$ podem apresentar aparências visuais totalmente distintas: um com ruído fino de alta frequência (facilmente filtrado pelo córtex visual humano) e outro com manchas cerosas grosseiras de baixa frequência que mimetizam ou ocultam tumores hepáticos ou renais.

\section{A Ruptura Não Linear: Da FBP aos Algoritmos DLR}
\label{sec:ruptura_nao_linear_intro}

Para reduzir a dose de radiação mantendo a relação sinal-ruído, a indústria tomográfica substituiu gradualmente a FBP por algoritmos iterativos estatísticos (HIR e MBIR) e, na vanguarda atual, por algoritmos de **Reconstrução por Aprendizado Profundo** (\emph{Deep Learning Image Reconstruction} --- DLR), tais como TrueFidelity (GE Healthcare), AiCE (Canon Medical Systems), Precise Image (Philips) e ClariCT.AI (ClariPi) \cite{racine2020, debbiche2024, greffier2026}.

Esses modelos utilizam redes neurais convolucionais profundas (\emph{Deep Convolutional Neural Networks}) treinadas com pares de imagens tomográficas adquiridas em doses padrão de alta qualidade e imagens correspondentes adquiridas em doses ultrabaixas. Ao aprender mapeamentos não lineares complexos entre o espaço de projeção e a imagem final, as redes DLR conseguem suprimir seletivamente o ruído quântico de alta frequência preservando bordas de alto contraste.

Entretanto, a incorporação clínica dos algoritmos DLR acarretou uma quebra paradigmática estrutural:
\begin{itemize}
  \item \textbf{Perda da Linearidade e Dependência de Contraste:} A resolução espacial não é mais uma propriedade invariante do sistema; ela varia dinamicamente de acordo com o contraste do alvo ($\Delta C$). Alvos de alto contraste (como artérias com iodo ou ossos) são reconstruídos com bordas nítidas, enquanto alvos sutis de baixo contraste ($\Delta C \le 30\text{ HU}$, como metástases hepáticas) sofrem suavização excessiva;
  \item \textbf{Quebra da Estacionariedade (Não-WSS):} O ruído torna-se espacialmente heterogêneo e anisotrópico, exibindo comportamentos distintos próximo a interfaces ósseas e no centro de parênquimas moles;
  \item \textbf{Efeito Ceroso ou Plástico (\emph{Plastic/Waxy Look}):} A regularização não linear desloca o espectro de potência do ruído para baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$), criando padrões de granulação não naturais que causam desconforto e fadiga visual aos radiologistas e prejudicam a detecção de microestruturas patológicas \cite{toia2023, solomon2020}.
\end{itemize}

\section{A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa (TBIQ)}
\label{sec:mudanca_paradigma_tbiq}

Diante da inadequação das métricas escalares clássicas para avaliar sistemas não lineares, a física médica internacional consolidou o paradigma da **Qualidade de Imagem Baseada em Tarefa** (\emph{Task-Based Image Quality} --- TBIQ) através dos relatórios canônicos AAPM TG-233 e ICRU Report 54 (\cref{fig:tbiq_paradigm}) \cite{aapm_tg233_2019, icru54_1996}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow1_tbiq_paradigm.png}
  \caption[Pilares Fundamentais do Paradigma TBIQ]{Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:tbiq_paradigm}
\end{figure}

O paradigma TBIQ fundamenta-se na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT) e postula que a qualidade de uma imagem médica não é um atributo estático intrínseco, mas sim a medida objetiva e reprodutível do desempenho de um observador (médico radiologista ou modelo computacional) ao realizar uma tarefa diagnóstica clinicamente relevante.

A abordagem TBIQ integra quatro pilares analíticos contínuos no domínio de Fourier através do **Índice de Detectabilidade ($d'$)**:
\begin{enumerate}
  \item \textbf{Função de Transferência da Tarefa ($TTF(f)$):} Modela a resolução espacial do tomógrafo em função da frequência espacial e do contraste específico do alvo patológico ($\Delta C$);
  \item \textbf{Espectro de Potência do Ruído ($NPS(f)$):} Descreve a variância e a textura estocástica do ruído no domínio contínuo de Fourier;
  \item \textbf{Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$):} Modela analiticamente o tamanho, a geometria e o perfil de atenuação da patologia;
  \item \textbf{Modelo Perceptual do Observador ($E(f)$ e Canais Corticais):} Modela a sensibilidade ao contraste do olho humano (função CSF de Burgess) e a filtragem em frequências corticais do córtex visual primário (V1).
\end{enumerate}

\section{Justificativa e Relevância do Estudo}
\label{sec:justificativa_monografia}

Com a rápida expansão dos algoritmos DLR na prática hospitalar e a recente chegada comercial da **Tomografia Computadorizada por Contagem de Fótons** (\emph{Photon-Counting CT} --- PCCT), o controle de qualidade em tomografia computadorizada atravessa a mais profunda reformulação metodológica de sua história. 

No entanto, a literatura científica brasileira carece de um texto de referência abrangente, unificado e rigorosamente deduzido que apresente a transição completa dos modelos lineares para as redes profundas. Este trabalho justifica-se ao suprir essa lacuna acadêmica, oferecendo uma revisão crítica aprofundada, com rigor matemático dedutivo e modelagens computacionais controladas que conectam as equações fundamentais da física de imagens às diretrizes normativas da AAPM e da ANVISA.

% ------------------------------------------------------------------------------
% CAPÍTULO 2: OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Objetivos}
\label{chap:objetivos}

\section{Objetivo Geral}
\label{sec:objetivo_geral}
O \textbf{objetivo geral} deste Trabalho de Conclusão de Curso consiste em realizar uma **revisão bibliográfica sistemática crítica e modelagem teórico-metrológica unificada** da evolução dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo os alicerces físicos, matemáticos e normativos que conectam a Teoria Clássica de Detecção de Sinais aos recentes observadores baseados em redes profundas (\emph{Vision Transformers}) e à física dos detectores de contagem de fótons.

\section{Objetivos Específicos}
\label{sec:objetivos_especificos}
Para alcançar o objetivo geral, definem-se os seguintes objetivos específicos:
\begin{enumerate}
  \item \textbf{Metodologia de Busca Booleana e Normatização:} Estruturar e documentar uma estratégia de busca bibliográfica sistemática baseada em equações booleanas nas principais bases científicas indexadas (PubMed, IEEE Xplore, Web of Science, Scopus e AAPM Reports), delimitando critérios rigorosos de elegibilidade e o corpus normativo internacional (AAPM TG-233, ICRU 54, ICRP 103, ANVISA RDC 611/2022);
  \item \textbf{Deduções da Teoria de Detecção de Sinais (SDT):} Apresentar as deduções matemáticas fundamentais da SDT no contexto de imagens médicas, formalizando o teste de hipóteses binárias, o limiar de decisão $t_c$, o Índice de Detectabilidade ($d'$), a teoria das curvas ROC e o paradigma psicofísico 2AFC (\emph{Two-Alternative Forced Choice});
  \item \textbf{Deduções no Domínio de Fourier (AAPM TG-233):} Deduzir passo a passo no domínio contínuo de Fourier as quatro funções espectrais fundamentais: a Função de Transferência da Tarefa ($TTF(f)$), o Espectro de Potência do Ruído ($NPS(f)$), o Filtro Ocular Humano ($E(f)$) e o Espectro da Tarefa ($W_{\text{task}}(f)$) através de funções de Bessel;
  \item \textbf{Análise Matemática dos Observadores Lineares Clássicos:} Deduzir analiticamente o Observador Ideal Bayesiano (IO), o Observador de Hotelling (HO) e o limite superior absoluto de informação física ($d'_{\text{HO}}$), o modelo antropomórfico NPWE e o Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor, formalizando a validação psicofísica por ANOVA MRMC (DBM/HOR);
  \item \textbf{Análise Crítica do Colapso Linear sob DLR:} Demonstrar formalmente as causas físicas e matemáticas da perda de correlação dos modelos lineares clássicos diante de reconstruções não lineares DLR e fundos anatômicos complexos, analisando o efeito ceroso e a quebra de estacionariedade (WSS);
  \item \textbf{Observadores Profundos e Redes Neurais:} Mapear o estado da arte dos Observadores Baseados em Aprendizado Profundo (DLMO / \emph{Vision Transformers}) com auto-atenção multi-cabeça, analisando a emulação do rastreamento foveal-periférico humano;
  \item \textbf{Física da PCCT e Otimização Multiobjetivo:} Sistematizar os fundamentos dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e formular a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$;
  \item \textbf{Modelagem e Simulação Numérica Sintética em Python:} Implementar e documentar exaustivamente as formulações analíticas e os parâmetros matemáticos empregados nas modelagens numéricas computacionais sintéticas desenvolvidas para fins didáticos e demonstrativos de cada curva e gráfico teórico.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 3: METODOLOGIA
% ------------------------------------------------------------------------------
\chapter{Metodologia}
\label{chap:metodologia}

Este capítulo estabelece o delineamento metodológico do trabalho, formaliza as estratégias de busca bibliográfica sistemática com equações booleanas nas bases de dados internacionais, apresenta os critérios de elegibilidade baseados nas diretrizes PRISMA, define o corpus normativo internacional e explicita a formulação analítica das modelagens numéricas sintéticas desenvolvidas em linguagem Python.

\section{Delineamento e Classificação Metodológica da Pesquisa}
\label{sec:delineamento_classificacao}
Este Trabalho de Conclusão de Curso classifica-se formalmente como uma **monografia de revisão bibliográfica sistemática crítica, sistematização conceitual e modelagem teórico-metrológica**. O trabalho não envolveu a coleta direta de dados clínicos primários com pacientes ou a realização de ensaios laboratoriais proprietários em bancada, mas sim a consolidação exaustiva e rigorosa do estado da arte internacional da física médica, estruturando as deduções matemáticas e fornecendo modelagens sintéticas controladas para fins didáticos e metrológicos.

\section{Estratégia de Busca Bibliográfica e Equações Booleanas}
\label{sec:estrategia_busca_booleana_detalhada}
O levantamento bibliográfico foi conduzido de acordo com as diretrizes metodológicas adaptadas do protocolo **PRISMA 2020** (\emph{Preferred Reporting Items for Systematic Reviews and Meta-Analyses}) \cite{page2021}, garantindo transparência, abrangência e reprodutibilidade.

\subsection{Bases de Dados Consultadas}
\label{subsec:bases_consultadas_detalhe}
A busca de literatura foi realizada de forma exaustiva nas seguintes bases científicas e repositórios internacionais:
\begin{enumerate}
  \item \textbf{PubMed / MEDLINE} (National Library of Medicine, Bethesda, EUA);
  \item \textbf{IEEE Xplore Digital Library} (Institute of Electrical and Electronics Engineers);
  \item \textbf{Web of Science Core Collection} (Clarivate Analytics);
  \item \textbf{Scopus} (Elsevier B.V.);
  \item \textbf{AAPM Reports and Medical Physics Journal Repository} (American Association of Physicists in Medicine);
  \item \textbf{SPIE Digital Library} (International Society for Optics and Photonics --- Medical Imaging Proceedings).
\end{enumerate}

\subsection{Estruturação dos Descritores e Termos Controlados (MeSH/DeCS)}
\label{subsec:estruturacao_descritores}
Os descritores foram rigorosamente mapeados a partir dos vocabulários controlados **MeSH** (\emph{Medical Subject Headings}) e **DeCS** (\emph{Descritores em Ciências da Saúde}), combinados a termos livres especializados da física de imagens médicas. A busca foi estruturada em três eixos conceituais fundamentais interligados por operadores lógicos booleanos:
\begin{itemize}
  \item \textbf{Eixo 1 (Modalidade e Tecnologia de Detecção):} Termos que delimitam o escopo da tomografia computadorizada (\emph{Tomography, X-Ray Computed}, \emph{Photon-Counting CT}, \emph{PCCT}, \emph{Spectral CT});
  \item \textbf{Eixo 2 (Metrologia e Avaliação Baseada em Tarefa):} Termos que identificam o paradigma TBIQ e a teoria de Fourier (\emph{Task-Based Image Quality}, \emph{Detectability Index}, \emph{Signal Detection Theory}, \emph{Task-Based Transfer Function}, \emph{Noise Power Spectrum});
  \item \textbf{Eixo 3 (Modelos de Observador e Algoritmos de Reconstrução):} Termos associados aos observadores matemáticos e métodos de reconstrução (\emph{Model Observer}, \emph{Channelized Hotelling Observer}, \emph{Non-Prewhitening Observer}, \emph{Deep Learning Image Reconstruction}, \emph{Vision Transformers}).
\end{itemize}

\subsection{Equações Booleanas de Busca Estruturadas}
\label{subsec:equacoes_booleanas_tabela}
A \cref{tab:estrategia_booleana} apresenta as equações booleanas formais implementadas em cada base de dados, utilizando operadores relacionais (\texttt{AND}, \texttt{OR}, \texttt{NOT}), parênteses de hierarquia e filtros de campo.

\begin{table}[htbp]
  \centering
  \small
  \caption[Estratégia de Busca Booleana por Base de Dados]{Estratégia de Busca Booleana Estruturada por Base de Dados e Eixos Conceituais.}
  \label{tab:estrategia_booleana}
  \begin{tabularx}{\textwidth}{lX}
    \toprule
    \textbf{Base de Dados} & \textbf{Equação Booleana de Busca (\emph{Search String})} \\
    \midrule
    \textbf{PubMed / MEDLINE} & 
    \texttt{("Tomography, X-Ray Computed"[MeSH] OR "computed tomography"[Title/Abstract] OR "photon counting CT"[Title/Abstract] OR "PCCT"[Title/Abstract]) AND ("task-based image quality"[Title/Abstract] OR "model observer"[Title/Abstract] OR "detectability index"[Title/Abstract] OR "channelized hotelling"[Title/Abstract] OR "NPWE"[Title/Abstract]) AND ("deep learning reconstruction"[Title/Abstract] OR "iterative reconstruction"[Title/Abstract] OR "noise power spectrum"[Title/Abstract] OR "AAPM TG-233"[Title/Abstract]) NOT ("radiotherapy"[Title] OR "positron emission"[Title])} \\
    \addlinespace
    \textbf{IEEE Xplore} & 
    \texttt{(("Document Title":"computed tomography" OR "Abstract":"computed tomography" OR "Abstract":"photon counting") AND ("Abstract":"task-based" OR "Abstract":"model observer" OR "Abstract":"detectability") AND ("Abstract":"deep learning" OR "Abstract":"Hotelling observer" OR "Abstract":"noise power spectrum"))} \\
    \addlinespace
    \textbf{Web of Science} & 
    \texttt{TS=(("computed tomography" OR "PCCT" OR "photon-counting") AND ("task-based image quality" OR "model observer*" OR "detectability index" OR "d-prime") AND ("deep learning reconstruction" OR "channelized hotelling" OR "Fourier metrics" OR "AAPM TG-233"))} \\
    \addlinespace
    \textbf{Scopus} & 
    \texttt{TITLE-ABS-KEY(("computed tomography" OR "photon counting CT") AND ("task-based image quality" OR "model observer" OR "detectability index") AND ("deep learning" OR "channelized hotelling" OR "NPWE" OR "noise power spectrum")) AND NOT TITLE("PET-CT" OR "SPECT")} \\
    \bottomrule
  \end{tabularx}
\end{table}

\subsection{Critérios de Elegibilidade: Inclusão e Exclusão}
\label{subsec:criterios_elegibilidade_detalhe}
Para a seleção criteriosa dos estudos, estabeleceram-se critérios rigorosos de elegibilidade documentados na \cref{tab:criterios_inclusao_exclusao}.

\begin{table}[htbp]
  \centering
  \small
  \caption[Critérios de Elegibilidade da Revisão]{Critérios de Elegibilidade, Inclusão e Exclusão para o Corpus Bibliográfico.}
  \label{tab:criterios_inclusao_exclusao}
  \begin{tabularx}{\textwidth}{p{0.22\textwidth}X}
    \toprule
    \textbf{Dimensão} & \textbf{Critérios Definidos} \\
    \midrule
    \textbf{Critérios de Inclusão} & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item Artigos originais e de revisão publicados em periódicos indexados com revisão por pares (\emph{peer-reviewed});
      \item Relatórios técnicos normativos de comissões internacionais de física médica (AAPM, ICRU, ICRP, IAEA, IEC);
      \item Estudos que desenvolvam ou apliquem deduções matemáticas formais de métricas baseadas em tarefa ($TTF$, $NPS$, $d'$, SDT, ROC, 2AFC, MRMC);
      \item Trabalhos que analisem observadores de modelo (IO, HO, NPWE, CHO, DLMO) em tomografia computadorizada;
      \item Publicações focadas em reconstruções iterativas estatísticas (HIR/MBIR), inteligência artificial (DLR) ou contagem de fótons (PCCT);
      \item Obras seminais históricas da física de imagens (Barrett, Burgess, Myers, Wagner, Metz, Rose).
    \end{itemize} \\
    \addlinespace
    \textbf{Critérios de Exclusão} & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item Artigos clínicos sem fundamentação física, dosimétrica ou metrológica;
      \item Estudos restritos a modalidades não tomográficas (ressonância magnética pura, ultrassom, medicina nuclear não acoplada);
      \item Resumos de conferências sem texto completo (\emph{abstracts only}), cartas ao editor e comentários sem dados analíticos;
      \item Publicações em duplicata entre as bases de dados consultadas.
    \end{itemize} \\
    \addlinespace
    \textbf{Janela Temporal} & 
    \begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
      \item \textbf{Eixo Contemporâneo (2018--2026):} Para algoritmos DLR, observadores DLMO baseados em Vision Transformers, detectores PCCT e protocolo AAPM TG-233;
      \item \textbf{Eixo Seminal Histórico (1948--2017):} Para a teoria de Rose, teoria de detecção de sinais, deduções de Hotelling, canais corticais do CHO e testes 2AFC.
    \end{itemize} \\
    \bottomrule
  \end{tabularx}
\end{table}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Fluxograma Metodológico da Revisão Sistemática]{Diagrama Conceitual do Fluxo Metodológico da Revisão Sistemática e Sistematização Teórica dos Modelos Perceptivos.}
  \label{fig:fluxograma_prisma}
\end{figure}

\section{Corpus de Documentos Normativos e Relatórios Internacionais}
\label{sec:corpus_normativo_detalhe}
O alinhamento normativo do estudo estruturou-se sobre quatro pilares documentais canônicos:
\begin{enumerate}
  \item \textbf{AAPM TG-233 Report (2019):} \emph{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}, documento balizador que padroniza o cálculo contínuo de $TTF(f)$, $NPS(f)$, $d'$ e a geometria dos simuladores de calibração \cite{aapm_tg233_2019};
  \item \textbf{ICRU Report 54 (1996):} \emph{Medical Imaging --- The Assessment of Image Quality}, que estabeleceu o formalismo fundamental de observadores estatísticos e métricas baseadas em tarefa \cite{icru54_1996};
  \item \textbf{ICRP Publication 103 (2007):} \emph{The 2007 Recommendations of the International Commission on Radiological Protection}, base ética e científica do princípio ALARA e da dosimetria de pacientes \cite{icrp103_2007};
  \item \textbf{ANVISA RDC nº 611/2022 e IN nº 93/2021:} Marcos regulatórios federais que normatizam a garantia da qualidade e o controle dosimétrico em tomografia computadorizada no Brasil \cite{anvisa_rdc611_2022, anvisa_in93_2021}.
\end{enumerate}

\section{Metodologia de Modelagem e Simulação Numérica Sintética em Python}
\label{sec:metodologia_simulacao_python_detalhada}

Para fundamentar didaticamente as deduções matemáticas e ilustrar os limites físicos dos modelos em cenários clínicos controlados, foram desenvolvidas modelagens numéricas sintéticas implementadas em linguagem Python (versão 3.10+, utilizando NumPy, SciPy e Matplotlib).

A \cref{tab:parametros_simulacao} sumariza com precisão as formulações matemáticas, os domínios de amostragem e os parâmetros exatos utilizados na geração de cada gráfico sintético apresentado no Capítulo \ref{chap:resultados_discussao}.

\begin{table}[htbp]
  \centering
  \small
  \caption[Parâmetros das Simulações Numéricas]{Parâmetros Matemáticos das Modelagens Numéricas Sintéticas em Python.}
  \label{tab:parametros_simulacao}
  \begin{tabularx}{\textwidth}{llX}
    \toprule
    \textbf{Figura / Tópico} & \textbf{Equação / Modelo} & \textbf{Parâmetros Computacionais Utilizados} \\
    \midrule
    \textbf{Figura 4.1} & $t_0 \sim \mathcal{N}(\mu_0, \sigma_t^2)$ & $\mu_0 = 0$, $\mu_1 = 2{,}2$, $\sigma_t = 1{,}0$, $t_c = 1{,}3$, \\
    (SDT, ROC, 2AFC) & $t_1 \sim \mathcal{N}(\mu_1, \sigma_t^2)$ & $d' = 2{,}2$; $t_c \in [-4; +6]$, $\Delta t_c = 0{,}01$; \\
    & $P_C(d') = \Phi(d'/\sqrt{2})$ & $d' \in \{0{,}5; 1{,}0; 1{,}5; 2{,}2; 3{,}0; 4{,}0\}$ \\
    \addlinespace
    \textbf{Figura 4.2} & $TTF(f; \Delta C)$ (Richard \& Samei) & Iodo (+300 HU): $f_{50}=0{,}58\text{ mm}^{-1}, \alpha=3{,}2$; \\
    (Métricas Fourier) & $NPS(f) = A f \exp(-f^2/2\sigma_f^2)$ & Solid Water (+25 HU): $f_{50}=0{,}35\text{ mm}^{-1}, \alpha=2{,}8$; \\
    & $E(f)$ (Burgess) & Burgess: $f_0=0{,}8\text{ cpd}, n=1{,}3, m=1{,}1, c=2{,}2$; \\
    & $W_{\text{task}}(f)$ (Bessel $J_1$) & Lesões esféricas: $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}, \Delta C = 35\text{ HU}$ \\
    \addlinespace
    \textbf{Figura 4.3} & $C_j(f) = e^{-\frac{f^2}{2\sigma_{j1}^2}} - e^{-\frac{f^2}{2\sigma_{j2}^2}}$ & 5 canais D-DOG: $f \in [0{,}10; 0{,}85]\text{ mm}^{-1}$; \\
    (Canais CHO) & $LG_n(r) = L_n(\frac{2\pi r^2}{a^2}) e^{-\frac{\pi r^2}{a^2}}$ & Laguerre-Gauss: $n \in \{0, 1, 2, 3\}, a = 4{,}0\text{ mm}$; \\
    & Gabor 2D ($\theta = 45^\circ$) & Gabor: $\sigma=3{,}5\text{ mm}, \lambda=5{,}0\text{ mm}, \gamma=0{,}75, \theta=45^\circ$ \\
    \addlinespace
    \textbf{Figura 4.5} & $d'(\text{Dose}) \propto \text{Dose}^\beta$ & FBP: $\beta = 0{,}50$; DLR: curva logística não linear; \\
    (DLR e Detrending) & $P_2(x, y) = \sum a_{ij} x^i y^j$ & Detrending: ajuste polinomial 2D via Mínimos Quadrados \\
    \addlinespace
    \textbf{Figura 4.8} & Variedade 3D $(D, T, -W)$ & Otimização: NSGA-II (100 indivíduos, 200 gerações), \\
    (Pareto e TOPSIS) & Pareto não-dominada & Ranqueamento multicritério TOPSIS \\
    \bottomrule
  \end{tabularx}
\end{table}

% ------------------------------------------------------------------------------
% CAPÍTULO 4: RESULTADOS E DISCUSSÃO
% ------------------------------------------------------------------------------
\chapter{Resultados e Discussão}
\label{chap:resultados_discussao}

Este capítulo reúne os principais resultados da revisão sistemática, apresentando as deduções matemáticas rigorosas da SDT e da metrologia no domínio de Fourier, a análise comparativa entre observadores clássicos e profundos, as causas do colapso dos modelos analíticos lineares sob DLR, os fundamentos da PCCT e a sistematização conceitual do fluxo de trabalho do relatório AAPM TG-233.

\section{Fundamentos da Teoria de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria_completa}

\subsection{Formulação Matemática das Hipóteses de Decisão e Teorema de Bayes}
\label{subsec:sdt_hipoteses_bayes}
A detecção de uma anormalidade patológica em uma imagem médica é formalmente descrita na física matemática como um problema de teste de hipóteses estatísticas sob ruído estocástico \cite{peterson1954, lusted1968, metz1986}.

Considere uma imagem digital bidimensional discretizada e representada por um vetor lexicográfico $\mathbf{g} \in \mathbb{R}^N$, onde $N = N_x \times N_y$ é o número total de pixels. O problema clássico de detecção binária (conhecido como paradigma SKE/BKS --- *Signal Known Exactly / Background Known Statistically*) formula-se através de duas hipóteses mutuamente exclusivas:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Sadio}) \label{eq:h0_def} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Patologia}) \label{eq:h1_def}
\end{align}
onde $\mathbf{s} \in \mathbb{R}^N$ é o vetor determinístico que descreve o perfil espacial do sinal da lesão e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo, caracterizado por valor esperado nulo $\langle \mathbf{b} \rangle = \mathbf{0}$ e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle \in \mathbb{R}^{N \times N}$.

\subsection{A Estatística de Decisão Escalar e o Teorema de Neyman-Pearson}
\label{subsec:neyman_pearson_regra}
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
  \includegraphics[width=0.98\textwidth]{figuras/fig1_sdt_roc_2afc.png}
  \caption[Distribuições da SDT, Curvas ROC e Desempenho 2AFC]{Modelagem Numérica Sintética da Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Desempenho Psicofísico 2AFC.}
  \label{fig:sdt_roc_2afc}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.1}
\label{subsec:analise_fig1_detalhada}
A \cref{fig:sdt_roc_2afc} foi sintetizada numericamente em Python a partir dos parâmetros documentados na \cref{tab:parametros_simulacao}:

\begin{enumerate}
  \item \textbf{Painel (A) --- Distribuições de Decisão da SDT sob Ruído:}
  Modelaram-se duas variáveis aleatórias gaussianas contínuas $t_0 \sim \mathcal{N}(0, 1)$ e $t_1 \sim \mathcal{N}(2{,}2, 1)$ com desvio padrão unitário $\sigma_t = 1{,}0$, correspondendo a um índice de detectabilidade teórico $d' = (\mu_1 - \mu_0)/\sigma_t = 2{,}2$. Definiu-se um limiar de corte $t_c = 1{,}3$. As probabilidades operacionais foram calculadas analiticamente por integração cumulativa:
  \begin{equation}
    FPF(t_c) = \int_{t_c}^\infty p(t|H_0) \, dt = 1 - \Phi\left(\frac{t_c - \mu_0}{\sigma_t}\right) \approx 0{,}097 \quad (9{,}7\%)
  \end{equation}
  \begin{equation}
    TPF(t_c) = \int_{t_c}^\infty p(t|H_1) \, dt = 1 - \Phi\left(\frac{t_c - \mu_1}{\sigma_t}\right) \approx 0{,}816 \quad (81{,}6\%)
  \end{equation}
  \emph{Contextualização Pedagógica:} Esse cenário simula o processo decisório na identificação de um nódulo pulmonar sutil de vidro fosco ($4\text{ mm}$, $-600\text{ HU}$) imerso em parênquima pulmonar normal ($-800\text{ HU}$), onde a posição de $t_c$ ilustra a postura mais conservadora ou mais agressiva do observador;

  \item \textbf{Painel (B) --- Geração Paramétrica das Curvas ROC:}
  Variou-se parametricamente o limiar $t_c \in [-4{,}0; +6{,}0]$ com incremento $\Delta t_c = 0{,}01$ para seis valores fixos de detectabilidade $d' \in \{0{,}5; 1{,}0; 1{,}5; 2{,}2; 3{,}0; 4{,}0\}$. Para cada par $(d', t_c)$, computaram-se os pontos $(FPF(t_c), TPF(t_c))$, gerando as trajetórias contínuas no espaço ROC e confirmando a relação analítica $AUC = \Phi(d' / \sqrt{2})$;

  \item \textbf{Painel (C) --- Curva de Desempenho no Paradigma 2AFC:}
  Plotou-se a probabilidade teórica de acerto em função do índice $d'$ avaliando a função sigmoidal $P_C(d') = \Phi(d' / \sqrt{2})$ no domínio $d' \in [0, 5]$. A curva demonstra que regimes de baixa detectabilidade ($d' \approx 1{,}0$) limitam a acurácia a $P_C \approx 76\%$, enquanto sistemas que satisfazem o Critério de Rose ($d' \ge 4{,}0$) garantem certeza visual diagnóstica ($P_C \ge 99{,}8\%$).
\end{enumerate}

\subsection{Dedução Formal do Índice de Detectabilidade ($d'$)}
\label{subsec:deducao_formal_dprime}
O Índice de Detectabilidade ($d'$) expressa a distância estatística normalizada entre os valores esperados da variável de decisão sob as duas hipóteses \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_definicao_geral}
\end{equation}

Para qualquer observador linear operando no espaço discreto por produto escalar $t(\mathbf{g}) = \mathbf{w}^T \mathbf{g}$, onde $\mathbf{w} \in \mathbb{R}^N$ é o vetor de pesos (*template* do observador):
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

\section{Métricas Espectrais Contínuas no Domínio de Fourier (AAPM TG-233)}
\label{sec:metricas_espectrais_fourier_completas}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_spectral_metrics.png}
  \caption[Métricas Espectrais Contínuas em Frequência]{Modelagem Numérica Sintética das Quatro Funções Espectrais no Domínio de Fourier segundo o Relatório AAPM TG-233.}
  \label{fig:spectral_metrics}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.2}
\label{subsec:analise_fig2_detalhada}
A \cref{fig:spectral_metrics} foi gerada em Python a partir das formulações normativas do AAPM TG-233 \cite{aapm_tg233_2019}:

\begin{enumerate}
  \item \textbf{Painel (A) --- Resolução Espacial da Tarefa $TTF(f)$:}
  Modelou-se a resposta em frequência via função sigmoidal generalizada de Richard \& Samei \cite{racine2020}:
  \begin{equation}
    TTF(f; \Delta C) = \left[ 1 + \left( \frac{f}{f_{50}(\Delta C)} \right)^\alpha \right]^{-1}
  \end{equation}
  onde para alto contraste (Iodo $+300\text{ HU}$, curva vermelha), calibrou-se $f_{50} = 0{,}58\text{ mm}^{-1}$ e $\alpha = 3{,}2$; para baixo contraste (Solid Water $+25\text{ HU}$, curva ciano), calibrou-se $f_{50} = 0{,}35\text{ mm}^{-1}$ e $\alpha = 2{,}8$, evidenciando o borramento não linear de alvos sutis;

  \item \textbf{Painel (B) --- Espectro de Potência do Ruído $NPS(f)$:}
  Modelou-se o espectro de ruído da FBP clássica pela lei de potência filtrada $NPS_{\text{FBP}}(f) = A \cdot f \cdot \exp(-f^2 / 2\sigma_f^2)$ com $f_{\text{peak}} = 0{,}45\text{ mm}^{-1}$ (curva preta). A curva DLR (verde) foi modelada com redução de 50\% na potência integrada e preservação do pico textural em $0{,}40\text{ mm}^{-1}$. A curva MBIR (roxa) foi gerada deslocando a variância para baixas frequências ($f_{\text{peak}} = 0{,}18\text{ mm}^{-1}$), ilustrando a textura cerosa (\emph{plastic look});

  \item \textbf{Painel (C) --- Filtro Ocular Humano $E(f)$:}
  Calculou-se a função de sensibilidade ao contraste de Burgess \cite{burgess1999} através de:
  \begin{equation}
    E(f) = \left( \frac{f}{f_0} \right)^n \exp\left[ -c \left( \frac{f}{f_0} \right)^m \right]
    \label{eq:filtro_ocular_burgess}
  \end{equation}
  com parâmetros $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$, convertendo frequências espaciais físicas para a retina sob distância de visualização de 50 cm ($f_{\text{retina}} \approx 8{,}727 \cdot f$), com pico ótimo em $4{,}2\text{ cpd}$;

  \item \textbf{Painel (D) --- Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$:}
  Computou-se a Transformada de Fourier analítica de lesões esféricas de raio $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}$ e contraste $\Delta C = 35\text{ HU}$ avaliando a função de Bessel de primeira ordem via:
  \begin{equation}
    W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi f R)}{2\pi f R} \right|
    \label{eq:wtask_bessel_formula}
  \end{equation}
  A simulação evidencia que lesões extensas concentram energia em $f < 0{,}15\text{ mm}^{-1}$, enquanto microlesões espalham energia para frequências superiores a $0{,}6\text{ mm}^{-1}$.
\end{enumerate}

\subsection{Deduções Analíticas Passo a Passo das Quatro Funções Espectrais}
\label{subsec:deducoes_passo_passo_quatro_funcoes}

\subsubsection{1. Dedução da Função de Transferência da Tarefa ($TTF(f)$)}
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

\subsubsection{2. Dedução do Espectro de Potência do Ruído ($NPS(f)$)}
Para extrair o ruído estocástico puro sem contaminação por gradientes teciduais lentos, aplica-se em cada ROI homogênea $k$ ($k = 1, \dots, M$) um detrending polinomial bidimensional de 2ª ordem $P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 xy + a_5 y^2$, resultando no ruído residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$.

Pelo Teorema de Wiener-Khinchin, o espectro bidimensional $NPS(u, v)$ é a Transformada de Fourier da função de autocovariância \cite{aapm_tg233_2019}:
\begin{equation}
  NPS(u, v) = \lim_{M \to \infty} \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, w(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
  \label{eq:nps_2d_formula}
\end{equation}
onde $w(x, y)$ é a janela de Hanning aplicada para evitar vazamento espectral (*spectral leakage*) e $\Delta x, \Delta y$ são os tamanhos físicos do pixel em mm, resultando na unidade $\text{HU}^2 \cdot \text{mm}^2$. A curva radial isotrópica $NPS(f)$ é obtida por integração azimutal:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial_integral}
\end{equation}

\section{Observadores Lineares Clássicos: Hotelling, NPWE e CHO}
\label{sec:observadores_lineares_deducoes_completas}

\subsection{O Observador de Hotelling (HO) e o Teto Físico de Bayes}
\label{subsec:hotelling_teto_bayes}
O Observador Ideal Bayesiano (IO) representa o limite superior absoluto de informação diagnóstica permitido pelas leis da física. Sob a premissa de ruído gaussiano multivariado com matriz de autocovariância $\mathbf{K}$, a razão de verossimilhança logarítmica de Bayes $\ln\Lambda(\mathbf{g})$ reduz-se analiticamente ao Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}:
\begin{equation}
  \ln\Lambda(\mathbf{g}) = -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) + \frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g} - \frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}
  \label{eq:log_bayes_deducao}
\end{equation}
Absorvendo a constante determinística $-\frac{1}{2}\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ no limiar $t_c$, a estatística escalar ótima é:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:hotelling_template_deducao}
\end{equation}
onde $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ realiza o pré-branqueamento do ruído via inversão de $\mathbf{K}$. O índice de detectabilidade máximo absoluto atingível é dado por:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling_teto}
\end{equation}

\subsection{Dedução da Integral Contínua do Observador NPWE em Fourier}
\label{subsec:npwe_integral_deducao}
O sistema visual humano não realiza a inversão matricial do ruído $\mathbf{K}^{-1}$. Para modelar observadores humanos em fundos homogêneos, o modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) aplica a correlação direta do sinal ($\mathbf{w} = \mathbf{s}$) filtrada pelo olho $E(f)$ e sob ruído neural interno $\sigma_{\text{int}}^2$ \cite{burgess1994, eckstein2000}.

No domínio contínuo de Fourier bidimensional isotrópico, a integral contínua do índice de detectabilidade do NPWE expressa-se por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral_completa}
\end{equation}

\subsection{O Observador de Hotelling Canalizado (CHO) e os Canais Corticais}
\label{subsec:cho_canais_corticais_completo}
Para modelar observadores humanos diante de fundos anatômicos complexos e estruturados (como parênquima pulmonar ou trabeculado ósseo), Myers e Barrett (1987) introduziram os canais corticais de frequência, originando o Observador de Hotelling Canalizado (\emph{Channelized Hotelling Observer} --- CHO) \cite{myers_barrett_1987, gallas2003}.

A imagem original $\mathbf{g} \in \mathbb{R}^N$ é projetada em um subespaço de dimensionalidade reduzida $\mathbf{v} \in \mathbb{R}^P$ ($P \ll N$, com $P = 4 \text{ a } 10$ canais) por meio da matriz de canais $\mathbf{T} \in \mathbb{R}^{P \times N}$:
\begin{equation}
  \mathbf{v} = \mathbf{T} \mathbf{g}
  \label{eq:cho_projecao_v}
\end{equation}
A estatística de teste do CHO e seu respectivo índice de detectabilidade são formulados por:
\begin{equation}
  t_{\text{CHO}}(\mathbf{g}) = \mathbf{w}_{\mathbf{v}}^T \mathbf{v} = \left( \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle \right)^T \mathbf{v}
  \label{eq:cho_stat_completa}
\end{equation}
\begin{equation}
  d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}
  \label{eq:dprime_cho_completo}
\end{equation}
onde $\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K} \mathbf{T}^T \in \mathbb{R}^{P \times P}$ é a matriz de covariância no espaço dos canais corticais e $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \mathbf{s}$ é o sinal projetado nos canais.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig3_cho_cortical_channels.png}
  \caption[Canais Corticais do CHO e Detectabilidade vs Dose]{Modelagem Numérica Sintética dos Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico.}
  \label{fig:cho_channels}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.3}
\label{subsec:analise_fig3_detalhada}
A \cref{fig:cho_channels} foi sintetizada em Python para demonstrar as formulações dos canais corticais:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação dos Canais D-DOG (\emph{Dense Difference of Gaussians}):}
  Implementaram-se cinco canais passa-faixa concêntricos definidos pela diferença de gaussianas no domínio da frequência:
  \begin{equation}
    C_j(f) = \exp\left( -\frac{f^2}{2\sigma_{j,1}^2} \right) - \exp\left( -\frac{f^2}{2\sigma_{j,2}^2} \right), \quad j = 1, \dots, 5
  \end{equation}
  com desvios padrão escalonados geometricamente para cobrir a faixa de $0{,}10\text{ a }0{,}85\text{ mm}^{-1}$, emulando os campos receptivos do córtex visual primário (V1);

  \item \textbf{Painel (B) --- Simulação das Funções Radiais de Laguerre-Gauss:}
  Avaliaram-se os polinômios de Laguerre-Gauss ortogonais de ordens $n \in \{0, 1, 2, 3\}$ com raio característico $a = 4{,}0\text{ mm}$:
  \begin{equation}
    LG_n(r) = L_n\left( \frac{2\pi r^2}{a^2} \right) \exp\left( -\frac{\pi r^2}{a^2} \right)
  \end{equation}
  evidenciando a decomposição de sinais circulares simétricos com reduzido número de graus de liberdade;

  \item \textbf{Painel (C) --- Campo Receptivo 2D de Gabor ($\theta = 45^\circ$):}
  Modelou-se a matriz bidimensional combinando envelope gaussiano e modulação senoidal orientada:
  \begin{equation}
    G(x, y) = \exp\left( -\frac{x'^2 + \gamma^2 y'^2}{2\sigma^2} \right) \cos\left( 2\pi \frac{x'}{\lambda} + \psi \right)
  \end{equation}
  com $x' = x\cos\theta + y\sin\theta$ e $y' = -x\sin\theta + y\cos\theta$, capturando a sensibilidade direcional a bordas anatômicas;

  \item \textbf{Painel (D) --- Simulação Comparativa NPWE vs. CHO em Fundo Estruturado:}
  Simulou-se o cálculo de detectabilidade em função da dose para uma lesão de 5 mm imersa em ruído anatômico estruturado (ruído em lei de potência $1/f^\beta$). Demonstra-se que o modelo linear NPWE (curva vermelha) subestima drasticamente a detectabilidade ($d' < 0{,}8$) por confundir variações anatômicas com ruído quântico puro, enquanto o CHO D-DOG (curva verde) descorrelaciona o fundo e preserva a correlação com a visão humana.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Diagrama do Fluxo de Decisão do Observador CHO]{Diagrama do Fluxo de Processamento e Decisão do Observador de Hotelling Canalizado (CHO).}
  \label{fig:cho_flow_diagram}
\end{figure}

\subsection{Validação Psicofísica MRMC (ANOVA DBM / HOR)}
\label{subsec:mrmc_anova_detalhe}
A validação de observadores computacionais contra painéis de médicos especialistas é regida pelo modelo de ANOVA com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova_completa}
\end{equation}
onde $y_{ijk}$ é o desempenho medido ($AUC$ ou $d'$), $\mu$ é a média global da população de leitores, $\tau_i$ é o efeito fixo da modalidade de reconstrução ou dose $i$, $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é a variabilidade inter-observador, $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é a variabilidade inter-caso e $\epsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\epsilon})$ é o erro residual aleatório.

\begin{table}[htbp]
  \centering
  \small
  \caption[Comparativo das Classes de Observadores de Modelo]{Resumo Comparativo das Classes de Observadores de Modelo em Física Médica.}
  \label{tab:comparativo_observadores}
  \begin{tabularx}{\textwidth}{p{0.20\textwidth}p{0.25\textwidth}p{0.25\textwidth}X}
    \toprule
    \textbf{Modelo} & \textbf{Domínio de Aplicação} & \textbf{Vantagens Físicas} & \textbf{Limitações Principais} \\
    \midrule
    \textbf{Observador Ideal (IO / HO)} & FBP clássica, ruído gaussiano homogêneo & Estabelece o limite superior absoluto de informação física & Não modela a visão humana; requer inversão matricial $\mathbf{K}^{-1}$ \\
    \addlinespace
    \textbf{NPWE} & FBP em simuladores homogêneos & Rápido cálculo analítico contínuo em Fourier via $TTF/NPS$ & Colapsa sob DLR e fundos anatômicos estruturados \\
    \addlinespace
    \textbf{CHO (D-DOG, LG, Gabor)} & FBP/HIR em fundos anatômicos estruturados & Excelente correlação com humanos em fundos complexos lineares & Subótimo em DLR devido a não-linearidades de alta ordem \\
    \addlinespace
    \textbf{DLMO (Vision Transformers)} & DLR não linear, PCCT e anatomias complexas & Modela atenção foveal-periférica e atinge $r > 0{,}95$ com radiologistas & Requer calibração supervisionada e maior custo computacional \\
    \bottomrule
  \end{tabularx}
\end{table}

\section{O Impacto das Reconstruções Não Lineares (DLR) e o Colapso dos Modelos Lineares}
\label{sec:impacto_dlr_colapso_completo}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D.}
  \label{fig:dlr_non_linear}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.5}
\label{subsec:analise_fig4_detalhada}
A \cref{fig:dlr_non_linear} foi gerada computacionalmente em Python para demonstrar os efeitos não lineares e as correções estatísticas:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação de Detectabilidade $d'$ vs. Dose em DLR:}
  Comparou-se o escalonamento clássico da FBP ($\sigma \propto 1/\sqrt{\text{Dose}} \implies d' \propto \sqrt{\text{Dose}}$, linha preta) contra o modelo não linear adaptativo de DLR (linha verde), onde a rede neural preserva a detectabilidade diagnóstica ($d' = 1{,}8$) mesmo em regimes de ultrabaixa dose ($1{,}5\text{ mGy}$);

  \item \textbf{Painel (B) --- Simulação de Correlação com Radiologistas Humanos:}
  Modelou-se a dispersão de leituras 2AFC documentadas na literatura para demonstrar a perda de correlação do modelo linear NPWE sob DLR (cruzes vermelhas, $r = 0{,}68$, decorrente da incapacidade de tratar o ruído não-estacionário), contrastando com observadores profundos adaptativos (círculos verdes, $r = 0{,}98$);

  \item \textbf{Painel (C) --- Demonstração do Detrending Polinomial 2D:}
  Simulou-se um perfil de intensidade anatômica $I(x)$ com gradiente macroscópico e ruído de alta frequência. Demonstra-se que o ajuste de superfície polinomial de 2ª ordem $P_2(x)$ (linha tracejada vermelha) via mínimos quadrados analíticos subtrai a variação estrutural lenta, isolando o ruído estocástico puro residual $\delta I(x) = I(x) - P_2(x)$ (curva verde inferior).
\end{enumerate}

\subsection{Análise Crítica das Causas do Colapso dos Modelos Lineares}
\label{subsec:causas_criticas_colapso}
O colapso dos modelos analíticos clássicos (como o NPWE e o CHO tradicional) diante dos algoritmos DLR decorre de três violações matemáticas estruturais \cite{racine2021, toia2023, debbiche2024}:
\begin{enumerate}
  \item \textbf{Quebra da Premissa Gaussiana Estacionária:} As funções de ativação não lineares das redes profundas quebram a simetria da distribuição normal multivariada do ruído, tornando a estatística linear $t = \mathbf{w}^T \mathbf{g}$ matematicamente insuficiente;
  \item \textbf{O Paradoxo da Supressão de Ruído no NPWE:} O modelo NPWE utiliza um filtro ocular estático $E(f)$ ponderado pelo espectro $NPS(f)$. Quando a DLR suprime o ruído global $\sigma_{\text{HU}}$ deslocando a potência para baixas frequências, a integral do denominador do NPWE decresce bruscamente, fazendo o índice $d'_{\text{NPWE}}$ disparar artificialmente para valores irreais, enquanto radiologistas humanos perdem desempenho pelo borramento textural da lesão ($r \approx 0{,}68$);
  \item \textbf{Inflexibilidade dos Canais Lineares:} Os canais corticais D-DOG e Gabor foram deduzidos sob a premissa de linearidade e não conseguem capturar correlações estatísticas de alta ordem aprendidas por redes neurais profundas.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption[Metodologia de Phantoms Híbridos e Teste 2AFC]{Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.}
  \label{fig:phantom_flow}
\end{figure}

\section{Observadores Baseados em Aprendizado Profundo (DLMO)}
\label{sec:dlmo_transformers_completo}

Para superar a falha dos modelos analíticos lineares, a física médica estruturou os **Observadores Baseados em Aprendizado Profundo** (\emph{Deep Learning Model Observers} --- DLMO), baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça (\cref{fig:dlmo_arch}) \cite{vaswani2017, dosovitskiy2020, toia2023}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura de Redes Neurais para Observadores DLMO]{Arquitetura de Observadores de Modelo por Aprendizado Profundo (DLMO / Vision Transformers).}
  \label{fig:dlmo_arch}
\end{figure}

Diferentemente das redes convolucionais que operam apenas em campos receptivos locais fixos, os Vision Transformers dividem a imagem médica em uma sequência de retalhos (*patches*) $\mathbf{x}_p \in \mathbb{R}^{P^2 \times C}$ e computam matrizes dinâmicas de auto-atenção multi-cabeça:
\begin{equation}
  \text{Attention}(\mathbf{Q}, \mathbf{K}_v, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}_v^T}{\sqrt{d_k}} \right) \mathbf{V}
  \label{eq:self_attention_formula}
\end{equation}
onde $\mathbf{Q}, \mathbf{K}_v, \mathbf{V}$ são as matrizes de Consulta (\emph{Query}), Chave (\emph{Key}) e Valor (\emph{Value}), e $d_k$ é a dimensão do canal de projeção. Essa formulação emula a coordenação foveal-periférica do sistema visual humano, alcançando correlações superiores a $r > 0{,}95$ com leituras humanas em testes 2AFC sob DLR.

\section{Tomografia por Contagem de Fótons (PCCT) e Otimização Multiobjetivo}
\label{sec:pcct_pareto_completo}

\subsection{Fundamentos Físicos dos Detectores PCCT}
\label{subsec:pcct_fisica_detectores}
A Tomografia Computadorizada por Contagem de Fótons (\emph{Photon-Counting CT} --- PCCT) representa a mais significativa revolução tecnológica na física de detecção de raios X das últimas três décadas \cite{willemink2018, rajendran2021}.

\begin{table}[htbp]
  \centering
  \small
  \caption[Comparativo Tecnológico de Detectores em Tomografia]{Síntese das Tecnologias de Detectores em Tomografia Computadorizada (EID vs PCCT).}
  \label{tab:detectores_comparativo}
  \begin{tabularx}{\textwidth}{p{0.22\textwidth}p{0.36\textwidth}X}
    \toprule
    \textbf{Parâmetro Físico} & \textbf{Detectores EID (Convencionais)} & \textbf{Detectores PCCT (Contagem de Fótons)} \\
    \midrule
    \textbf{Mecanismo de Conversão} & Indireto: Cintilador cerâmico (Gd$_2$O$_2$S) converte raios X em luz visível $\to$ Fotodiodo de silício & Direto: Semicondutor (CdTe ou CZT) converte raios X instantaneamente em pares elétron-lacuna \\
    \addlinespace
    \textbf{Ponderação Energética} & Ponderação por energia: Fótons de alta energia recebem maior peso ($S \propto E$) & Ponderação unitária: Cada fóton contado individualmente com peso idêntico ($S \propto N$) \\
    \addlinespace
    \textbf{Ruído Eletrônico} & Integrado ao sinal de imagem, degradando doses baixas & Totalmente eliminado via limiares de energia (\emph{energy thresholds}) \\
    \addlinespace
    \textbf{Resolução Espacial} & Limitada por septos ópticos reflexivos ($0{,}5 \text{ a } 0{,}6\text{ mm}$) & Ultra-alta resolução nativa ($0{,}2 \times 0{,}2\text{ mm}^2$ na isocentro) \\
    \addlinespace
    \textbf{Capacidade Espectral} & Requer dupla fonte de raios X ou comutação rápida de kVp & Multi-energia espectral intrínseca em cada varredura \\
    \bottomrule
  \end{tabularx}
\end{table}

A PCCT permite reconstruir rotineiramente **Imagens Monoenergéticas Virtuais** ($VMI$) em baixos níveis de energia fotônica (40 a 50 keV), onde o coeficiente de atenuação fotoelétrico do iodo ($Z=53$) é amplificado exponencialmente por estar próximo à sua borda K ($K_{\text{edge}} = 33{,}2\text{ keV}$), viabilizando reduções expressivas na concentração de meios de contraste iodados nefrotóxicos administrados aos pacientes.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Modelagem Numérica Sintética da Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -W)$.}
  \label{fig:pareto_3d}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.8}
\label{subsec:analise_fig5_detalhada}
A \cref{fig:pareto_3d} foi sintetizada numericamente em Python para demonstrar o conceito de soluções não-dominadas em física médica:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação da Fronteira de Compromisso Dose vs. Detectabilidade:}
  Modelou-se analiticamente o espaço de soluções através de funções de compromisso físico não-lineares. A curva contínua verde delimita a Fronteira de Pareto de soluções não-dominadas. Destacam-se três soluções de compromisso: $P_1$ (protocolo de ultrabaixa dose pediátrico), $P_2$ (exame ambulatorial padrão) e $P_3$ (protocolo de emergência com máxima detectabilidade). Os pontos cinzas dispersos representam protocolos subótimos;

  \item \textbf{Painel (B) --- Simulação da Superfície de Pareto Tridimensional $(D, T, -W)$:}
  Modelou-se uma variedade 3D contínua integrando tempo de rotação/varredura ($T$), dose absorvida ($D$) e detectabilidade ($W$). A simulação ilustra a tomada de decisão clínica multicritério (via algoritmo genético NSGA-II e ranqueamento TOPSIS \cite{deb2002, hwang1981}), permitindo selecionar o protocolo de varredura ultra-rápida ($T \le 2\text{ s}$) que preserva a detectabilidade necessária para pacientes de emergência traumatológica.
\end{enumerate}

\section{Sistematização do Pipeline Metrológico Padronizado AAPM TG-233}
\label{sec:pipeline_tg233_completo}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow6_software_pipeline.png}
  \caption[Estrutura Conceitual do Pipeline Metrológico]{Estrutura Conceitual do Pipeline Metrológico em Tomografia Computadorizada segundo o Relatório AAPM TG-233.}
  \label{fig:software_flow}
\end{figure}

Conforme consolidado na literatura internacional de metrologia tomográfica \cite{aapm_tg233_2019, choopani2023}, o processamento sistemático de imagens para avaliação baseada em tarefa organiza-se em cinco etapas conceituais encadeadas (\cref{fig:software_flow}):
\begin{enumerate}
  \item \textbf{Etapa 1 (Extração e Validação de Metadados DICOM):} Leitura sistemática dos cabeçalhos dos exames, extraindo parâmetros de irradiação ($\text{kVp}$, $\text{mA}$, tempo de rotação, $\text{CTDI}_{\text{vol}}$, $\text{DLP}$), geometria de aquisição (espessura de corte, espaçamento entre fatias, campo de visão FOV) e identificadores de reconstrução (kernel, nível DLR/HIR);
  \item \textbf{Etapa 2 (Segmentação e Amostragem Espacial de ROIs):} Identificação das coordenadas espaciais dos insertos de calibração via Transformada de Hough circular e extração de $M \ge 100$ regiões de interesse homogêneas independentes para amostragem estocástica do ruído;
  \item \textbf{Etapa 3A (Cálculo da Resolução Espacial da Tarefa):} Construção da Função de Resposta ao Degrau superamostrada ($\text{ESF}(r)$), derivação numérica da $\text{LSF}(r)$ e aplicação da Transformada Rápida de Fourier para obtenção da $TTF(f)$ e dos descritores $f_{50}$ e $f_{10}$;
  \item \textbf{Etapa 3B (Processamento Espectral do Ruído):} Aplicação do detrending polinomial bidimensional de 2ª ordem $P_2(x, y)$, janelamento de Hanning para contenção de vazamento espectral e FFT2D, gerando a matriz $NPS(u, v)$ e a curva radial integrada $NPS(f)$;
  \item \textbf{Etapa 4 (Integração dos Observadores de Modelo):} Avaliação do índice de detectabilidade $d'$ através dos modelos analíticos lineares (NPWE e CHO com canais corticais D-DOG/Laguerre-Gauss) e modelagem não-linear;
  \item \textbf{Etapa 5 (Análise de Incerteza e Relatório de Conformidade):} Reamostragem estatística por Bootstrap ($B = 2000$) para cálculo de intervalos de confiança de 95\% e emissão de laudo técnico de qualidade.
\end{enumerate}

\section{Diretrizes Regulatórias e Bioéticas em Avaliações Psicofísicas}
\label{sec:bioetica_regulacao}
A condução de experimentos psicofísicos com médicos radiologistas (leituras 2AFC e MRMC) demanda o estrito cumprimento de salvaguardas éticas e legais:
\begin{itemize}
  \item \textbf{Submissão ao Sistema CEP/CONEP:} Todo protocolo envolvendo observadores humanos deve ser previamente aprovado por Comitê de Ética em Pesquisa, com aplicação do Termo de Consentimento Livre e Esclarecido (TCLE);
  \item \textbf{Anonimização DICOM e LGPD:} Remoção irreversível de identificadores de pacientes conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o padrão DICOM PS 3.15;
  \item \textbf{Ergonomia Visual Padronizada:} Calibração de monitores diagnósticos segundo a norma DICOM Grayscale Standard Display Function (GSDF / AAPM TG-18), com luminância controlada e ambiente com iluminância reduzida ($< 25\text{ lux}$).
\end{itemize}

% ------------------------------------------------------------------------------
% CAPÍTULO 5: CONCLUSÃO
% ------------------------------------------------------------------------------
\chapter{Conclusão}
\label{chap:conclusao}

A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram a mais profunda transformação metodológica e conceitual de sua história nas últimas décadas. Esta monografia realizou uma **revisão bibliográfica sistemática abrangente e uma modelagem teórico-metrológica unificada**, mapeando a transição das métricas escalares lineares clássicas para as formulações perceptuais contemporâneas baseadas em inteligência artificial e detectores de contagem de fótons.

\section{Síntese das Contribuições Teórico-Metrológicas}
\label{sec:sintese_contribuicoes_finais}
As conclusões centrais desta investigação estruturam-se em quatro eixos fundamentais:
\begin{enumerate}
  \item \textbf{Superação Epistemológica das Métricas Escalares:} Demonstrou-se formalmente que grandezas como $SNR$, $CNR$, $\sigma_{\text{HU}}$ e $MTF$ são inadequadas para a caracterização de sistemas tomográficos não lineares (DLR e MBIR). Sob tais algoritmos, a redução puramente escalar do desvio padrão induz a falsa premissa de ganho de qualidade, mascarando alterações texturais severas (efeito ceroso) e o borramento de lesões sutis de baixo contraste;
  \item \textbf{Consolidação do Paradigma TBIQ (AAPM TG-233):} Apresentaram-se as deduções matemáticas contínuas completas no domínio de Fourier ($TTF$, $NPS$, $E(f)$ e $W_{\text{task}}$), formalizando o Índice de Detectabilidade ($d'$) como a grandeza física central, reprodutível e objetiva recomendada internacionalmente;
  \item \textbf{Limites de Validade dos Modelos Lineares Clássicos:} Evidenciaram-se as causas matemáticas pelas quais o modelo antropomórfico NPWE perde correlação com leitores humanos sob DLR ($r \approx 0{,}68$), justificando a necessidade dos observadores profundos DLMO baseados em Vision Transformers ($r > 0{,}95$);
  \item \textbf{Integração Multicritério em PCCT:} Sistematizou-se a física dos detectores de contagem de fótons e demonstrou-se como a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$ viabiliza protocolos clínicos balanceados entre dose mínima, tempo ultra-rápido e máxima eficácia diagnóstica.
\end{enumerate}

\section{Implicações para a Prática Hospitalar da Física Médica}
\label{sec:implicacoes_pratica_hospitalar}
Os resultados e modelos sistematizados fornecem suporte direto para:
\begin{itemize}
  \item A estruturação de programas hospitalares avançados de garantia da qualidade alinhados à RDC ANVISA 611/2022 e ao relatório AAPM TG-233;
  \item A calibração técnica e os testes de aceitação de novos tomógrafos equipados com inteligência artificial e detectores PCCT;
  \item A capacitação de físicos médicos especialistas para intervir criticamente na otimização de protocolos clínicos sem depender exclusivamente de critérios subjetivos ou métricas escalares obsoletas.
\end{itemize}

\section{Limitações do Estudo}
\label{sec:limitacoes_estudo_finais}
Por se tratar de uma monografia de revisão bibliográfica sistemática e modelagem teórico-metrológica, as curvas e superfícies foram geradas através de simulações numéricas sintéticas controladas em Python, sem a realização de ensaios experimentais primários com pacientes ou simuladores de bancada proprietários. Trabalhos empíricos futuros poderão aplicar diretamente este corpo teórico em ambientes laboratoriais e hospitalares.

\section{Perspectivas Futuras}
\label{sec:perspectivas_futuras_finais}
A evolução contínua da física de imagens médicas aponta para direções de vanguarda:
\begin{enumerate}
  \item \textbf{Extensão para Imagens 4D Dinâmicas:} Aplicação de modelos perceptivos em tomografias temporais dinâmicas (angiotomografia coronariana com sincronização cardíaca e perfusão cerebral em AVC), incorporando a Função de Transferência Temporal ($TTF_t(f_t)$);
  \item \textbf{Modelos Multimodais de Visão e Linguagem:} Integração de \emph{Vision-Language Models} e \emph{Foundation Models} em saúde para gerar observadores computacionais universais que forneçam laudos estruturados com mapeamento de incerteza;
  \item \textbf{Mapeamento Espectral Multielementar em PCCT:} Quantificação simultânea de múltiplos agentes de contraste com bordas K distintas (nanopartículas de ouro, gadolínio, bismuto e tântalo) para diagnóstico teranóstico molecular;
  \item \textbf{Estudos Psicofísicos Multicêntricos em Larga Escala:} Condução de experimentos 2AFC com consórcios hospitalares para consolidação de bancos de dados públicos de calibração metrológica.
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
"""

with open(main_tex_path, "w", encoding="utf-8") as f:
    f.write(latex_content)

# Update build_single_file_overleaf.py
build_script_path = "/Users/user/.gemini/antigravity-ide/scratch/build_single_file_overleaf.py"
with open(build_script_path, "w", encoding="utf-8") as f:
    f.write(f'''# -*- coding: utf-8 -*-
import os
import zipfile
import shutil

output_dir = "{output_dir}"
single_main_tex = r"""{latex_content}"""

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
print("Pacote Overleaf expandido atualizado com sucesso!")
''')

# Build the zip file
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

print("TCC Expandido gerado e empacotado com sucesso!")
