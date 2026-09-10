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
\hyphenation{To-mo-gra-fia Con-ta-gem Fó-tons Non-Pre-whi-te-ning Ob-ser-va-dor Clás-si-co Es-tru-tu-ral Re-cons-tru-ção Mul-ti-ob-je-ti-vo Di-ag-nós-ti-co Psi-co-fí-si-co An-tro-po-mór-fi-co Me-to-do-lo-gia Re-sul-ta-dos Dis-cus-são}

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
  \textit{Aos meus pais e familiares, pelo apoio incondicional e incentivo permanente aos estudos.\\
  A todos os físicos médicos e pesquisadores dedicados à proteção radiológica e à excelência diagnóstica.}
\end{flushright}
\clearpage

\chapter*{Agradecimentos}
\addcontentsline{toc}{chapter}{Agradecimentos}

Ao meu orientador, Prof. Dr. Paulo Roberto Costa, pela excepcional orientação acadêmica, pelo rigor científico transmitido e pelas discussões inspiradoras sobre física de imagens e metrologia das radiações.

Aos docentes e pesquisadores do Instituto de Física (IFUSP) e da Faculdade de Medicina (FMUSP) da Universidade de São Paulo, pela sólida formação teórica e interdisciplinar ao longo da graduação em Física Médica.

Aos colegas de curso e amigos de laboratório, pela convivência fraterna e trocas de conhecimento.

À Universidade de São Paulo, pelo ambiente acadêmico de excelência pública e compromisso com a ciência.
\clearpage

% 5. EPÍGRAFE
\chapter*{Epígrafe}
\addcontentsline{toc}{chapter}{Epígrafe}
\vspace*{\fill}
\begin{flushright}
  \textit{``A image is not good in itself; it is only good for a purpose.''}\\
  \vspace{0.3cm}
  --- Harrison H. Barrett \& Kyle J. Myers (\emph{Foundations of Image Science})
\end{flushright}
\clearpage

% 6. RESUMO
\chapter*{Resumo}
\addcontentsline{toc}{chapter}{Resumo}

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica contemporânea, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação da eficácia diagnóstica (princípio ALARA). Historicamente, a garantia da qualidade em TC baseou-se em métricas escalares lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR), o desvio padrão em Unidades Hounsfield ($\sigma_{\text{HU}}$) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores homogêneos de água ou acrílico. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares --- com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade estrita, isoplanatismo espacial e estacionariedade no sentido amplo (WSS) do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais (como o aspecto ceroso ou \emph{plastic look}) que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), fundamentado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade é formalmente definida pelo desempenho de um observador ao executar uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Esta monografia constitui uma \textbf{revisão bibliográfica sistemática e modelagem teórico-metrológica} da evolução dos observadores de modelo (\emph{model observers}) e das métricas TBIQ. A metodologia de busca foi conduzida através de equações booleanas estruturadas nas principais bases científicas (PubMed/MEDLINE, IEEE Xplore, Web of Science, Scopus e AAPM Reports), delimitando critérios rigorosos de elegibilidade e sistematização normativa (AAPM TG-233, ICRU 54, ANVISA RDC 611/2022). Apresentam-se as deduções matemáticas contínuas completas partindo do limite do Observador Ideal Bayesiano e de Hotelling, passando pelos modelos antropomórficos lineares com filtro ocular (NPWE) e canais corticais (CHO), até as fronteiras em redes neurais (\emph{Vision Transformers}) e Tomografia por Contagem de Fótons (PCCT). Para fundamentar pedagogicamente as deduções, o trabalho incorpora \textbf{modelagens numéricas sintéticas controladas} em Python, detalhando as equações analíticas que originam cada curva e superfície simulada. Este estudo estabelece um corpo de referência teórico e conceitual unificado para a física médica contemporânea.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Revisão Bibliográfica Sistemática. Busca Booleana. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Simulação Numérica. Tomografia por Contagem de Fótons. Relatório AAPM TG-233.
\clearpage

% 7. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), standard deviation in Hounsfield Units ($\sigma_{\text{HU}}$), and Modulation Transfer Function (MTF), evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity (WSS). Under non-linear processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a \textbf{systematic literature review and theoretical-metrological synthesis} of the evolution of model observers and Task-Based Image Quality (TBIQ) metrics. The search methodology was conducted using structured Boolean query equations across major international scientific databases (PubMed/MEDLINE, IEEE Xplore, Web of Science, Scopus, and AAPM Reports), with well-defined eligibility criteria and normative harmonization (AAPM TG-233, ICRU 54, ANVISA RDC 611/2022). We present complete step-by-step mathematical derivations transitioning from the Bayesian Ideal Observer and Hotelling Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), up to recent frontiers involving deep learning architectures (Vision Transformers) and Photon-Counting CT (PCCT) physics. To pedagogically support the theoretical deductions, this work incorporates \textbf{controlled synthetic numerical simulations} in Python, explicitly detailing the analytical formulations and computational parameters used to generate each simulated response curve and multi-dimensional surface. This study establishes a rigorous and unified theoretical reference framework for image quality metrology in modern computed tomography.

\vspace{0.8cm}
\noindent\textbf{Keywords:} Computed Tomography. Systematic Literature Review. Boolean Search Strategy. Task-Based Image Quality. Model Observers. Detectability Index. Deep Learning Reconstruction. Numerical Simulation. Photon-Counting CT. AAPM TG-233 Report.
\clearpage

% 8. LISTA DE ILUSTRAÇÕES
\chapter*{Lista de Ilustrações}
\addcontentsline{toc}{chapter}{Lista de Ilustrações}
\begin{itemize}[leftmargin=*,label={}]
  \item \textbf{Figura 1.1} -- Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 15
  \item \textbf{Figura 1.2} -- Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) \dotfill 17
  \item \textbf{Figura 3.1} -- Diagrama de Fluxo Metodológico da Revisão Sistemática (Protocolo de Busca Booleana e Seleção de Evidências) \dotfill 23
  \item \textbf{Figura 4.1} -- Modelagem Numérica Sintética da Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Desempenho Psicofísico 2AFC \dotfill 28
  \item \textbf{Figura 4.2} -- Modelagem Numérica Sintética das Quatro Funções Espectrais no Domínio de Fourier segundo o Relatório AAPM TG-233 \dotfill 34
  \item \textbf{Figura 4.3} -- Modelagem Numérica Sintética dos Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico \dotfill 41
  \item \textbf{Figura 4.4} -- Diagrama do Fluxo de Decisão do Observador de Hotelling Canalizado (CHO) \dotfill 43
  \item \textbf{Figura 4.5} -- Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D \dotfill 47
  \item \textbf{Figura 4.6} -- Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC \dotfill 50
  \item \textbf{Figura 4.7} -- Arquitetura de Redes Neurais para Observadores de Modelo por Aprendizado Profundo (DLMO / Vision Transformers) \dotfill 53
  \item \textbf{Figura 4.8} -- Modelagem Numérica Sintética da Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -W)$ \dotfill 58
  \item \textbf{Figura 4.9} -- Estrutura Conceitual do Pipeline Metrológico em Tomografia Computadorizada segundo o Relatório AAPM TG-233 \dotfill 61
\end{itemize}
\clearpage

% 9. LISTA DE TABELAS
\chapter*{Lista de Tabelas}
\addcontentsline{toc}{chapter}{Lista de Tabelas}
\begin{itemize}[leftmargin=*,label={}]
  \item \textbf{Tabela 3.1} -- Estratégia de Busca Booleana Estruturada por Eixo Temático e Termos MeSH/DeCS \dotfill 21
  \item \textbf{Tabela 3.2} -- Critérios de Elegibilidade, Inclusão e Exclusão para o Levantamento Bibliográfico \dotfill 22
  \item \textbf{Tabela 3.3} -- Parâmetros Matemáticos das Modelagens Numéricas Sintéticas em Python \dotfill 25
  \item \textbf{Tabela 4.1} -- Resumo Comparativo das Classes de Observadores de Modelo em Física Médica \dotfill 45
  \item \textbf{Tabela 4.2} -- Síntese das Tecnologias de Detectores em Tomografia Computadorizada (EID vs PCCT) \dotfill 56
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
  CHO    & \emph{Channelized Hotelling Observer} (Observador de Hotelling Canalizado) \\
  CNR    & \emph{Contrast-to-Noise Ratio} (Relação Contraste-Ruído) \\
  CTDI   & \emph{Computed Tomography Dose Index} (Índice de Dose em Tomografia) \\
  D-DOG  & \emph{Dense Difference of Gaussians} (Diferença Densa de Gaussianas) \\
  DLR    & \emph{Deep Learning Image Reconstruction} (Reconstrução por Aprendizado Profundo) \\
  DLMO   & \emph{Deep Learning Model Observer} (Observador por Aprendizado Profundo) \\
  DLP    & \emph{Dose-Length Product} (Produto Dose-Comprimento) \\
  EID    & \emph{Energy-Integrating Detector} (Detector de Integração de Energia) \\
  ESF    & \emph{Edge Spread Function} (Função de Espalhamento de Borda / Resposta ao Degrau) \\
  FBP    & \emph{Filtered Backprojection} (Retroprojeção Filtrada) \\
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
  PCCT   & \emph{Photon-Counting Computed Tomography} (Tomografia por Contagem de Fótons) \\
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

A Tomografia Computadorizada (TC) representa uma das mais importantes conquistas da física médica e da engenharia biomédica do século XX, transformando a prática médica diagnóstica desde a sua introdução clínica por Godfrey Hounsfield e Allan Cormack na década de 1970 \cite{bushberg2020, attix1986, seeram2015}. Ao possibilitar a reconstrução tomográfica tridimensional não invasiva da anatomia humana a partir de medições de atenuação de raios X, a TC tornou-se a modalidade de escolha para o diagnóstico rápido e preciso de patologias cardiovasculares, neurológicas, abdominais e oncológicas.

\section{Contextualização e o Princípio ALARA}
\label{sec:contexto_alara}
O uso intensivo da tomografia computadorizada na rotina médica implica a deposição de doses de radiação ionizante que, embora justificadas clinicamente, demandam rigoroso controle radiológico. De acordo com as recomendações da Comissão Internacional de Proteção Radiológica (ICRP Publicação 103) e com as diretrizes regulatórias sanitárias nacionais (ANVISA RDC 611/2022 e Instrução Normativa IN 93/2021), todo procedimento radiológico deve obedecer aos princípios de \textbf{Justificação}, \textbf{Otimização} e \textbf{Limitação de Doses} \cite{icrp103_2007, anvisa_rdc611_2022, anvisa_in93_2021}.

No âmbito da otimização, vigora o princípio ALARA (\emph{As Low As Reasonably Achievable}), que estabelece que as exposições à radiação devem ser mantidas nos níveis mais baixos que possam ser razoavelmente alcançados, compatíveis com a obtenção da informação diagnóstica necessária \cite{mccollough2026}. A física médica atua na interface desse compromisso permanente: a redução indiscriminada da dose de radiação ($D$) eleva as flutuações quânticas estocásticas de fótons (ruído de Poisson), degradando o contraste e a resolução da imagem a ponto de comprometer a acurácia diagnóstica do médico radiologista.

\section{As Métricas Escalares Tradicionais e Suas Limitações}
\label{sec:metricas_tradicionais}
Durante mais de quatro décadas, o controle de qualidade e a dosimetria em TC basearam-se no formalismo clássico da Retroprojeção Filtrada (FBP --- \emph{Filtered Backprojection}). Sob a FBP, o sistema formador de imagem é estritamente linear, isoplanático (invariante no espaço) e governado por ruído estacionário no sentido amplo (WSS --- \emph{Wide-Sense Stationary}).

Nesse regime linear, a qualidade da imagem era avaliada rotineiramente através de métricas escalares simples, obtidas em simuladores cilíndricos homogêneos de água ou PMMA:
\begin{itemize}
  \item \textbf{Relação Sinal-Ruído ($SNR$):} Razão entre a média do sinal $\mu$ e o desvio padrão do ruído $\sigma_{\text{HU}}$:
  \begin{equation}
    SNR = \frac{\mu}{\sigma_{\text{HU}}}
    \label{eq:snr_def}
  \end{equation}
  \item \textbf{Relação Contraste-Ruído ($CNR$):} Diferença entre o sinal da lesão $\mu_{\text{alvo}}$ e o sinal do fundo circundante $\mu_{\text{fundo}}$, ponderada pelo ruído:
  \begin{equation}
    CNR = \frac{|\mu_{\text{alvo}} - \mu_{\text{fundo}}|}{\sqrt{\frac{1}{2}(\sigma_{\text{alvo}}^2 + \sigma_{\text{fundo}}^2)}}
    \label{eq:cnr_def}
  \end{equation}
  \item \textbf{Função de Transferência de Modulação ($MTF(f)$):} Magnitude normalizada da Transformada de Fourier bidimensional da Função de Espalhamento de Ponto ($\text{PSF}(x, y)$), descrevendo a preservação da modulação do contraste em função da frequência espacial $f$:
  \begin{equation}
    MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
    \label{eq:mtf_def}
  \end{equation}
\end{itemize}

\section{A Ruptura Não Linear: Da FBP aos Algoritmos DLR}
\label{sec:ruptura_nao_linear}
A introdução clínica de algoritmos avançados de reconstrução não lineares --- inicialmente as Reconstruções Iterativas Híbridas e Baseadas em Modelo (HIR e MBIR) e, mais recentemente, a Reconstrução por Aprendizado Profundo (\emph{Deep Learning Image Reconstruction} --- DLR) baseada em redes neurais convolucionais profundas --- promoveu uma profunda quebra paradigmática na física médica (\cref{fig:comparativo_paradigmas}) \cite{racine2020, debbiche2024, greffier2026}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption[Comparativo Estrutural entre os Paradigmas Físicos]{Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

Sob processamentos não lineares adaptativos:
\begin{enumerate}
  \item A resposta do sistema passa a depender ativamente do contraste local e da morfologia anatômica da cena ($\mathcal{R}\{\alpha f_1 + \beta f_2\} \ne \alpha \mathcal{R}\{f_1\} + \beta \mathcal{R}\{f_2\}$);
  \item O ruído perde a estacionariedade espacial (quebra da condição WSS): a variância $\sigma^2(\mathbf{r})$ torna-se heterogênea e fortemente correlacionada à presença de bordas teciduais;
  \item O desvio padrão global $\sigma_{\text{HU}}$ é fortemente reduzido por regularizações matemáticas, mas a variância é deslocada para baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$), gerando o chamado aspecto ceroso ou plástico (\emph{plastic look}) que degrada a detecção visual de lesões sutis de baixo contraste por médicos radiologistas \cite{toia2023, solomon2020}.
\end{enumerate}

\section{A Mudança de Paradigma: Qualidade Baseada em Tarefa (TBIQ)}
\label{sec:paradigma_tbiq}
Para superar as limitações das métricas escalares, a física médica estruturou a abordagem da **Qualidade de Imagem Baseada em Tarefa** (\emph{Task-Based Image Quality} --- TBIQ), consolidada pelas forças-tarefa internacionais nos relatórios AAPM TG-233 e ICRU Report 54 (\cref{fig:tbiq_paradigm}) \cite{aapm_tg233_2019, icru54_1996}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow1_tbiq_paradigm.png}
  \caption[Pilares Fundamentais do Paradigma TBIQ]{Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:tbiq_paradigm}
\end{figure}

O paradigma TBIQ fundamenta-se na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT) e postula que a qualidade de imagem deve ser quantificada pelo desempenho de um observador (humano ou matemático) ao executar uma tarefa diagnóstica clinicamente relevante. Essa formulação unifica quatro grandezas contínuas no domínio de Fourier através do **Índice de Detectabilidade ($d'$)**:
\begin{enumerate}
  \item \textbf{Função de Transferência da Tarefa ($TTF(f)$):} Mede a resolução espacial efetiva em função do contraste específico do alvo clínico;
  \item \textbf{Espectro de Potência do Ruído ($NPS(f)$):} Mapeia a magnitude e a textura espectral das flutuações estocásticas de ruído;
  \item \textbf{Espectro da Tarefa ($W_{\text{task}}(f)$):} Representa matematicamente a geometria, o diâmetro e a densidade radiológica da patologia;
  \item \textbf{Modelo Perceptual do Observador ($E(f)$ e Canais Corticais):} Modela a sensibilidade ao contraste e o processamento neural do córtex visual humano.
\end{enumerate}

\section{Justificativa e Relevância do Estudo}
\label{sec:justificativa}
Com a rápida disseminação de tomógrafos com algoritmos DLR e o advento da Tomografia Computadorizada por Contagem de Fótons (\emph{Photon-Counting CT} --- PCCT), torna-se imperativo para a física médica dispor de um corpo teórico rigoroso, deduzido analiticamente e pedagogicamente estruturado. Uma revisão crítica aprofundada que sistematize a passagem dos modelos lineares para as formulações profundas preenche uma lacuna fundamental na literatura nacional e internacional de metrologia tomográfica.

% ------------------------------------------------------------------------------
% CAPÍTULO 2: OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Objetivos}
\label{chap:objetivos}

\section{Objetivo Geral}
\label{sec:objetivo_geral}
O \textbf{objetivo geral} deste Trabalho de Conclusão de Curso consiste em realizar uma **revisão bibliográfica sistemática e modelagem teórico-metrológica** da evolução dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo os fundamentos físicos, matemáticos e metodológicos que conectam a Teoria Clássica de Detecção de Sinais aos recentes observadores baseados em redes neurais profundas e à tomografia por contagem de fótons.

\section{Objetivos Específicos}
\label{sec:objetivos_especificos}
Os \textbf{objetivos específicos} desta monografia compreendem:
\begin{enumerate}
  \item \textbf{Metodologia de Busca Booleana:} Estruturar e documentar uma estratégia de busca bibliográfica sistemática baseada em equações booleanas nas principais bases de dados internacionais (PubMed, IEEE Xplore, Web of Science, Scopus e AAPM Reports), delimitando critérios rigorosos de elegibilidade e o corpus normativo de referência;
  \item \textbf{Deduções Fundamentais da SDT:} Apresentar a dedução matemática passo a passo da Teoria de Detecção de Sinais, formulando o Índice de Detectabilidade ($d'$), as curvas de Característica de Operação do Receptor (ROC) e o protocolo psicofísico 2AFC (\emph{Two-Alternative Forced Choice});
  \item \textbf{Deduções no Domínio de Fourier:} Deduzir rigorosamente no domínio contínuo de Fourier as quatro funções fundamentais da metrologia TBIQ conforme o relatório AAPM TG-233: $TTF(f)$, $NPS(f)$, o Filtro Ocular $E(f)$ e o Espectro da Tarefa $W_{\text{task}}(f)$ via funções de Bessel;
  \item \textbf{Modelos Lineares Clássicos:} Deduzir e contrastar matematicamente o Observador Ideal Bayesiano (IO), o Observador de Hotelling (HO), o modelo antropomórfico NPWE e o Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor, formalizando o modelo estatístico MRMC de ANOVA para validação contra painéis de médicos radiologistas;
  \item \textbf{Análise do Colapso Linear sob DLR:} Demonstrar analiticamente as causas biofísicas da falha dos modelos lineares clássicos diante de reconstruções DLR não lineares e fundos anatômicos complexos, analisando o efeito ceroso e a quebra de estacionariedade (WSS);
  \item \textbf{Observadores Profundos e PCCT:} Mapear o estado da arte dos Observadores Baseados em Aprendizado Profundo (DLMO / \emph{Vision Transformers}), sistematizar os fundamentos físicos dos detectores de Contagem de Fótons (PCCT / $VMI$) e formular a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$;
  \item \textbf{Modelagem e Simulação Numérica Sintética:} Implementar e explicitar as equações matemáticas e os parâmetros computacionais utilizados nas modelagens numéricas sintéticas desenvolvidas em Python para fins pedagógicos e ilustrativos das curvas e superfícies teóricas.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 3: METODOLOGIA
% ------------------------------------------------------------------------------
\chapter{Metodologia}
\label{chap:metodologia}

Este capítulo estabelece o delineamento metodológico da pesquisa, formaliza as estratégias de busca sistemática por equações booleanas nas bases de dados indexadas, detalha os critérios de inclusão e exclusão do corpus documental e explicita a formulação matemática das modelagens numéricas sintéticas desenvolvidas em linguagem computacional para ilustrar as deduções teóricas.

\section{Delineamento e Classificação da Pesquisa}
\label{sec:delineamento_pesquisa}
Este Trabalho de Conclusão de Curso constitui uma **monografia de revisão bibliográfica sistemática crítica, sistematização conceitual e modelagem teórico-metrológica**. O trabalho não envolve coleta direta de imagens DICOM clínicas com pacientes nem o desenvolvimento de software proprietário de processamento laboratorial primário. Seu escopo reside na organização exaustiva do estado da arte internacional, na dedução formal passo a passo das grandezas físicas e na integração didática dos modelos perceptivos de qualidade tomográfica.

\section{Estratégia de Busca Bibliográfica e Equações Booleanas}
\label{sec:estrategia_busca_booleana}
Para garantir reprodutibilidade, abrangência e rigor científico, o levantamento da literatura seguiu diretrizes metodológicas adaptadas do protocolo PRISMA (\emph{Preferred Reporting Items for Systematic Reviews and Meta-Analyses}) \cite{page2021}.

\subsection{Bases de Dados Consultadas}
\label{subsec:bases_consultadas}
A busca de literatura foi executada de forma independente nas seguintes bases bibliográficas internacionais e repositórios institucionais:
\begin{enumerate}
  \item \textbf{PubMed / MEDLINE} (National Library of Medicine, EUA);
  \item \textbf{IEEE Xplore Digital Library} (Institute of Electrical and Electronics Engineers);
  \item \textbf{Web of Science Core Collection} (Clarivate Analytics);
  \item \textbf{Scopus} (Elsevier);
  \item \textbf{AAPM Publications \& Reports Repository} (American Association of Physicists in Medicine);
  \item \textbf{SPIE Digital Library} (International Society for Optics and Photonics --- Medical Imaging).
\end{enumerate}

\subsection{Estruturação dos Vocabulários Controlados e Termos MeSH/DeCS}
\label{subsec:vocabularios_mesh_decs}
Os descritores foram selecionados a partir do vocabulário controlado MeSH (\emph{Medical Subject Headings}) e DeCS (\emph{Descritores em Ciências da Saúde}), complementados por palavras-chave livres específicas da física de imagens médicas. A busca foi estruturada em três eixos conceituais obrigatórios combinados por operadores lógicos:
\begin{itemize}
  \item \textbf{Eixo 1 (Modalidade e Física):} Termos relacionados à tomografia computadorizada e tecnologias de detecção (\emph{Tomography, X-Ray Computed}, \emph{Photon-Counting CT}, \emph{Computed Tomography});
  \item \textbf{Eixo 2 (Metrologia e Teoria de Decisão):} Termos relacionados à avaliação baseada em tarefa e teoria de Fourier (\emph{Signal Detection Theory}, \emph{Task-Based Image Quality}, \emph{Detectability Index}, \emph{Modulation Transfer Function}, \emph{Noise Power Spectrum});
  \item \textbf{Eixo 3 (Modelos e Algoritmos de Reconstrução):} Termos relacionados a observadores matemáticos e métodos de reconstrução (\emph{Model Observer}, \emph{Channelized Hotelling Observer}, \emph{Non-Prewhitening Observer}, \emph{Deep Learning Reconstruction}, \emph{Vision Transformers}).
\end{itemize}

\subsection{Equações Booleanas de Busca}
\label{subsec:strings_busca_booleana}
A \cref{tab:estrategia_booleana} apresenta as equações booleanas estruturadas com operadores lógicos relacionais (\texttt{AND}, \texttt{OR}, \texttt{NOT}), parênteses de agrupamento hierárquico e truncamentos aplicados nos campos de Título, Resumo e Palavras-chave (\emph{Title/Abstract/Keywords}).

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
\label{subsec:criterios_elegibilidade}
Para refinar a seleção dos estudos, aplicaram-se critérios sistemáticos de inclusão e exclusão documentados na \cref{tab:criterios_inclusao_exclusao}.

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

\section{Corpus Normativo e Regulatório}
\label{sec:corpus_normativo}
O referencial normativo foi estruturado a partir dos principais relatórios técnicos internacionais e marcos regulatórios nacionais:
\begin{enumerate}
  \item \textbf{AAPM TG-233 Report (2019):} \emph{Performance Evaluation of Computed Tomography Systems}, que padroniza o cálculo de $TTF(f)$, $NPS(f)$, $d'$ e a metodologia de simuladores cilíndricos com insertos de calibração \cite{aapm_tg233_2019};
  \item \textbf{ICRU Report 54 (1996):} \emph{Medical Imaging --- The Assessment of Image Quality}, que estabelece as bases da análise baseada em tarefa e dos observadores estatísticos \cite{icru54_1996};
  \item \textbf{ICRP Publication 103 (2007):} \emph{The 2007 Recommendations of the International Commission on Radiological Protection}, que fundamenta o princípio ALARA e a otimização de dose \cite{icrp103_2007};
  \item \textbf{ANVISA RDC nº 611/2022 e IN nº 93/2021:} Regulamentações sanitárias federais que regem o controle de qualidade, os níveis de referência diagnóstica e a garantia da qualidade em tomografia médica no Brasil \cite{anvisa_rdc611_2022, anvisa_in93_2021}.
\end{enumerate}

\section{Metodologia de Modelagem e Simulação Numérica Sintética}
\label{sec:metodologia_simulacao_python}
Para além da síntese bibliográfica textual, utilizou-se a modelagem computacional sintética em linguagem Python (com as bibliotecas científicas NumPy, SciPy e Matplotlib) como instrumento pedagógico e demonstrativo das deduções analíticas.

A \cref{tab:parametros_simulacao} sumariza as formulações analíticas e os parâmetros matemáticos exatos empregados para a geração de cada curva e gráfico sintético apresentados no Capítulo \ref{chap:resultados_discussao}.

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

Este capítulo apresenta os resultados da revisão sistemática e as deduções físico-matemáticas completas que estruturam o paradigma TBIQ, analisando comparativamente os observadores lineares e profundos, os efeitos não lineares de algoritmos DLR, a física da PCCT e a sistematização normativa do pipeline AAPM TG-233.

\section{Fundamentos da Teoria de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria}

\subsection{Formulação Matemática das Hipóteses de Decisão}
\label{subsec:sdt_hipoteses}
A detecção de uma lesão patológica em um exame de tomografia computadorizada é formalmente tratada na física matemática como um problema de teste de hipóteses binárias sob ruído estocástico \cite{peterson1954, lusted1968, metz1986}.

Considere uma imagem discreta representada lexicograficamente por um vetor $\mathbf{g} \in \mathbb{R}^N$ ($N$ pixels). As duas hipóteses mutuamente exclusivas são formuladas por:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Sadio}) \label{eq:h0} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Lesão}) \label{eq:h1}
\end{align}
onde $\mathbf{s} \in \mathbb{R}^N$ é o vetor determinístico que descreve o sinal da patologia e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo com média zero e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle$.

\subsection{A Regra de Decisão Escalar e o Limiar de Corte}
\label{subsec:sdt_regra_decisao}
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
  \caption[Distribuições da SDT, Curvas ROC e Desempenho 2AFC]{Modelagem Numérica Sintética da Teoria de Detecção de Sinais (SDT), Curvas ROC Paramétricas e Desempenho Psicofísico 2AFC.}
  \label{fig:sdt_roc_2afc}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.1}
\label{subsec:analise_fig1}
A \cref{fig:sdt_roc_2afc} foi gerada computacionalmente em Python a partir dos parâmetros documentados na \cref{tab:parametros_simulacao}:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação das Distribuições $p(t|H_0)$ e $p(t|H_1)$:}
  Modelaram-se duas variáveis aleatórias gaussianas contínuas $t_0 \sim \mathcal{N}(0, 1)$ e $t_1 \sim \mathcal{N}(2{,}2, 1)$ com desvio padrão normalizado $\sigma_t = 1{,}0$, correspondendo a um índice de detectabilidade teórico $d' = (\mu_1 - \mu_0)/\sigma_t = 2{,}2$. Definiu-se um limiar de corte $t_c = 1{,}3$. As probabilidades operacionais foram calculadas analiticamente por integração cumulativa:
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

\subsection{Definição Formal e Dedução do Índice de Detectabilidade ($d'$)}
\label{subsec:dprime_geral_deducao}
O Índice de Detectabilidade ($d'$) expressa a distância estatística entre os valores esperados da estatística de teste sob as duas hipóteses, normalizada pelas respectivas variâncias \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_geral}
\end{equation}

Para observadores lineares da forma $t(\mathbf{g}) = \mathbf{w}^T \mathbf{g}$, onde $\mathbf{w} \in \mathbb{R}^N$ é o vetor de pesos (*template* do observador):
\begin{align}
  \langle t | H_0 \rangle &= \mathbf{w}^T \langle \mathbf{b} \rangle = 0 \label{eq:exp_h0} \\
  \langle t | H_1 \rangle &= \mathbf{w}^T (\mathbf{s} + \langle \mathbf{b} \rangle) = \mathbf{w}^T \mathbf{s} \label{eq:exp_h1}
\end{align}
A variância sob ambas as hipóteses (assumindo ruído estacionário com matriz $\mathbf{K}$) é idêntica:
\begin{equation}
  \sigma^2(t) = \langle (\mathbf{w}^T \mathbf{b})^2 \rangle = \mathbf{w}^T \langle \mathbf{b} \mathbf{b}^T \rangle \mathbf{w} = \mathbf{w}^T \mathbf{K} \mathbf{w}
  \label{eq:var_t}
\end{equation}
Substituindo as \cref{eq:exp_h0,eq:exp_h1,eq:var_t} na \cref{eq:dprime_geral}, obtém-se a expressão fundamental do índice de detectabilidade para qualquer observador linear discreto:
\begin{equation}
  d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}
  \label{eq:dprime_linear_discreto}
\end{equation}

\section{Métricas Espectrais Contínuas no Domínio de Fourier}
\label{sec:metricas_espectrais_fourier}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_spectral_metrics.png}
  \caption[Métricas Espectrais Contínuas em Frequência]{Modelagem Numérica Sintética das Quatro Funções Espectrais no Domínio de Fourier segundo o Relatório AAPM TG-233.}
  \label{fig:spectral_metrics}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.2}
\label{subsec:analise_fig2}
A \cref{fig:spectral_metrics} foi sintetizada em Python a partir das formulações analíticas padronizadas pelo relatório AAPM TG-233 \cite{aapm_tg233_2019}:

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
    \label{eq:filtro_ocular}
  \end{equation}
  com parâmetros $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$, convertendo frequências espaciais físicas para a retina sob distância de visualização de 50 cm ($f_{\text{retina}} \approx 8{,}727 \cdot f$), com pico ótimo em $4{,}2\text{ cpd}$;

  \item \textbf{Painel (D) --- Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$:}
  Computou-se a Transformada de Fourier analítica de lesões esféricas de raio $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}$ e contraste $\Delta C = 35\text{ HU}$ avaliando a função de Bessel de primeira ordem via:
  \begin{equation}
    W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi f R)}{2\pi f R} \right|
    \label{eq:wtask_formula}
  \end{equation}
  A simulação evidencia que lesões extensas concentram energia em $f < 0{,}15\text{ mm}^{-1}$, enquanto microlesões espalham energia para frequências superiores a $0{,}6\text{ mm}^{-1}$.
\end{enumerate}

\subsection{Dedução Analítica das Quatro Funções Espectrais}
\label{subsec:deducoes_quatro_funcoes_fourier}

\subsubsection{1. Dedução da Função de Transferência da Tarefa ($TTF(f)$)}
A partir do centróide $(x_c, y_c)$ de um inserto cilíndrico de calibração homogêneo imerso em fundo uniforme com raio $R_0$, calcula-se a distância euclidiana radial $r = \sqrt{(x - x_c)^2 + (y - y_c)^2}$. Agrupando os pixels em sub-intervalos radiais infinitesimais $dr$, constrói-se a Função de Resposta ao Degrau superamostrada $\text{ESF}(r)$. Como a Função de Espalhamento de Linha $\text{LSF}(r)$ é a derivada espacial negativa do degrau ($\text{LSF}(r) = -\frac{d}{dr}\text{ESF}(r)$), sua Transformada de Fourier normalizada define a $TTF(f)$ \cite{aapm_tg233_2019, racine2020}:
\begin{equation}
  TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \left( -\frac{d}{dr}\text{ESF}(r) \right) e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \left( -\frac{d}{dr}\text{ESF}(r) \right) dr} = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \text{LSF}(r) \, dr}
  \label{eq:ttf_formula}
\end{equation}

\subsubsection{2. Dedução do Espectro de Potência do Ruído ($NPS(f)$)}
Para cada uma das $M$ ROIs homogêneas independentes, o ruído puro residual é $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$, onde $P_2(x, y)$ é o ajuste de superfície polinomial 2D de 2ª ordem. Pelo Teorema de Wiener-Khinchin, o espectro de potência é dado por:
\begin{equation}
  NPS(u, v) = \lim_{M \to \infty} \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
  \label{eq:nps_2d}
\end{equation}
onde $\Delta x, \Delta y$ são as dimensões espaciais do pixel em mm, resultando na unidade física $\text{HU}^2\cdot\text{mm}^2$. A curva radial isotrópica $NPS(f)$ é obtida por integração azimutal:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial}
\end{equation}

\section{Observadores Lineares Clássicos: Hotelling, NPWE e CHO}
\label{sec:observadores_lineares_classicos}

\subsection{Dedução do Observador de Hotelling (HO) e o Teto Físico de Bayes}
\label{subsec:deducao_hotelling}
O Observador Ideal Bayesiano (IO) fundamenta-se na razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$. Quando o ruído de fundo segue uma distribuição normal multivariada com matriz de autocovariância $\mathbf{K}$, a razão de verossimilhança logarítmica reduz-se ao Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}:
\begin{equation}
  \Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)} = \frac{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) \right)}{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} \right)}
  \label{eq:bayes_ratio}
\end{equation}
Tomando o logaritmo natural e eliminando constantes independentes de $\mathbf{g}$:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:template_hotelling}
\end{equation}
onde $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ executa o pré-branqueamento (\emph{prewhitening}) do ruído via $\mathbf{K}^{-1}$. O índice de detectabilidade máximo absoluto atingível pelas leis da física é:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling}
\end{equation}

\subsection{Dedução da Integral Contínua do Observador NPWE em Fourier}
\label{subsec:deducao_integral_npwe}
O sistema visual humano não realiza a inversão matricial $\mathbf{K}^{-1}$. O modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) correlaciona a imagem diretamente com o sinal ponderado pelo filtro ocular $E(f)$ e ruído interno $\sigma_{\text{int}}^2$ \cite{burgess1994, eckstein2000}. No domínio contínuo de Fourier, a integral contínua do índice de detectabilidade expressa-se por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral}
\end{equation}

\subsection{O Observador de Hotelling Canalizado (CHO) e Canais Corticais}
\label{subsec:cho_canais_corticais}
Para modelar o córtex visual primário (área V1) em fundos estruturados não homogêneos, Myers e Barrett (1987) introduziram os canais corticais de frequência, originando o Observador de Hotelling Canalizado (\emph{Channelized Hotelling Observer} --- CHO) \cite{myers_barrett_1987}.

A imagem $\mathbf{g} \in \mathbb{R}^N$ é projetada em um subespaço de dimensionalidade reduzida $\mathbf{v} \in \mathbb{R}^P$ ($P \ll N$, tipicamente $P = 4 \text{ a } 10$ canais) através de uma matriz de canais $\mathbf{T} \in \mathbb{R}^{P \times N}$:
\begin{equation}
  \mathbf{v} = \mathbf{T} \mathbf{g}
  \label{eq:cho_projecao}
\end{equation}
A estatística de teste e o índice de detectabilidade do CHO são dados por:
\begin{equation}
  t_{\text{CHO}}(\mathbf{g}) = \mathbf{w}_{\mathbf{v}}^T \mathbf{v} = \left( \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle \right)^T \mathbf{v}
  \label{eq:cho_stat}
\end{equation}
\begin{equation}
  d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}
  \label{eq:dprime_cho}
\end{equation}
onde $\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K} \mathbf{T}^T \in \mathbb{R}^{P \times P}$ é a matriz de covariância no espaço dos canais e $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \mathbf{s}$.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig3_cho_cortical_channels.png}
  \caption[Canais Corticais do CHO e Detectabilidade vs Dose]{Modelagem Numérica Sintética dos Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico.}
  \label{fig:cho_channels}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.3}
\label{subsec:analise_fig3}
A \cref{fig:cho_channels} foi sintetizada em Python para demonstrar a formulação matemática dos canais corticais:

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
\label{subsec:mrmc_anova}
Para comprovar a concordância entre observadores computacionais e médicos radiologistas, aplica-se o modelo de ANOVA com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova}
\end{equation}
onde $y_{ijk}$ é a acurácia ($AUC$ ou $d'$), $\mu$ é a média global, $\tau_i$ é o efeito fixo da modalidade de reconstrução ou dose $i$, $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é a variância entre radiologistas, $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é a variância entre pacientes e $\epsilon_{ijk}$ é o erro experimental residual.

\section{O Impacto das Reconstruções Não Lineares (DLR) e o Colapso dos Modelos Lineares}
\label{sec:impacto_dlr_colapso}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Modelagem Numérica Sintética do Impacto da Não-Linearidade em DLR, Correlação com Radiologistas e Detrending Polinomial 2D.}
  \label{fig:dlr_non_linear}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.5}
\label{subsec:analise_fig4}
A \cref{fig:dlr_non_linear} foi gerada por simulação computacional sintética em Python:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação de Detectabilidade $d'$ vs. Dose em DLR:}
  Comparou-se o escalonamento clássico da FBP ($\sigma \propto 1/\sqrt{\text{Dose}} \implies d' \propto \sqrt{\text{Dose}}$, linha preta) contra o modelo não linear adaptativo de DLR (linha verde), onde a rede neural preserva a detectabilidade diagnóstica ($d' = 1{,}8$) mesmo em regimes de ultrabaixa dose ($1{,}5\text{ mGy}$);

  \item \textbf{Painel (B) --- Simulação de Correlação com Radiologistas Humanos:}
  Modelou-se a dispersão de leituras 2AFC documentadas na literatura para demonstrar a perda de correlação do modelo linear NPWE sob DLR (cruzes vermelhas, $r = 0{,}68$, decorrente da incapacidade de tratar o ruído não-estacionário), contrastando com observadores profundos adaptativos (círculos verdes, $r = 0{,}98$);

  \item \textbf{Painel (C) --- Demonstração do Detrending Polinomial 2D:}
  Simulou-se um perfil de intensidade anatômica $I(x)$ com gradiente macroscópico e ruído de alta frequência. Demonstra-se que o ajuste de superfície polinomial de 2ª ordem $P_2(x)$ (linha tracejada vermelha) via mínimos quadrados analíticos subtrai a variação estrutural lenta, isolando o ruído estocástico puro residual $\delta I(x) = I(x) - P_2(x)$ (curva verde inferior).
\end{enumerate}

\subsection{Causas do Colapso dos Observadores Lineares}
\label{subsec:causas_colapso_lineares}
O colapso dos modelos analíticos lineares clássicos sob DLR decorre de três violações estruturais:
\begin{enumerate}
  \item \textbf{Não-Gaussianidade do Ruído:} As ativações não lineares (ReLU, GELU) nas redes neurais quebram a premissa de distribuição normal multivariada do ruído;
  \item \textbf{Incompatibilidade com o Efeito Ceroso:} O NPWE calcula uma redução artificial do ruído integrado no denominador, fazendo $d'_{\text{NPWE}}$ disparar falsamente enquanto o olho humano sofre com a perda de textura da lesão;
  \item \textbf{Rigidez dos Canais Corticais:} Os canais lineares do CHO não conseguem capturar correlações espaciais de alta ordem aprendidas pelos modelos neurais.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption[Metodologia de Phantoms Híbridos e Teste 2AFC]{Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.}
  \label{fig:phantom_flow}
\end{figure}

\section{Observadores Baseados em Aprendizado Profundo (DLMO)}
\label{sec:dlmo_vision_transformers}
Em resposta ao colapso dos modelos lineares, a física médica desenvolveu os Observadores Baseados em Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO) baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça (\cref{fig:dlmo_arch}) \cite{vaswani2017, dosovitskiy2020, toia2023}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura de Redes Neurais para Observadores DLMO]{Arquitetura de Observadores de Modelo por Aprendizado Profundo (DLMO / Vision Transformers).}
  \label{fig:dlmo_arch}
\end{figure}

O mecanismo de auto-atenção calcula matrizes de afinidade espacial dinâmica entre regiões foveais centrais e contexto periférico:
\begin{equation}
  \text{Attention}(\mathbf{Q}, \mathbf{K}_v, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}_v^T}{\sqrt{d_k}} \right) \mathbf{V}
  \label{eq:self_attention}
\end{equation}
calibrando seus pesos diretamente contra as probabilidades empíricas de acerto $P_C$ obtidas em leituras de radiologistas no paradigma 2AFC.

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

\section{Tomografia por Contagem de Fótons (PCCT) e Otimização Multiobjetivo}
\label{sec:pcct_pareto_otimizacao}

\subsection{Fundamentos Físicos dos Detectores PCCT}
\label{subsec:pcct_fundamentos}
Os detectores semicondutores de conversão direta da PCCT (CdTe / CZT) superam os detectores convencionais de integração de energia (EID), eliminando o ruído eletrônico via limiares de energia e permitindo a reconstrução de Imagens Monoenergéticas Virtuais ($VMI$) em níveis ótimos de 40 a 50 keV para máxima amplificação do contraste iodado \cite{willemink2018, rajendran2021}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Modelagem Numérica Sintética da Otimização Multiobjetivo e Fronteira de Pareto Tridimensional $(D, T, -W)$.}
  \label{fig:pareto_3d}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.8}
\label{subsec:analise_fig5}
A \cref{fig:pareto_3d} foi sintetizada numericamente em Python para demonstrar o conceito de soluções não-dominadas em física médica:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação da Fronteira de Compromisso Dose vs. Detectabilidade:}
  Modelou-se analiticamente o espaço de soluções através de funções de compromisso físico não-lineares. A curva contínua verde delimita a Fronteira de Pareto de soluções não-dominadas. Destacam-se três soluções de compromisso: $P_1$ (protocolo de ultrabaixa dose pediátrico), $P_2$ (exame ambulatorial padrão) e $P_3$ (protocolo de emergência com máxima detectabilidade). Os pontos cinzas dispersos representam protocolos subótimos;

  \item \textbf{Painel (B) --- Simulação da Superfície de Pareto Tridimensional $(D, T, -W)$:}
  Modelou-se uma variedade 3D contínua integrando tempo de rotação/varredura ($T$), dose absorvida ($D$) e detectabilidade ($W$). A simulação ilustra a tomada de decisão clínica multicritério (via algoritmo genético NSGA-II e ranqueamento TOPSIS), permitindo selecionar o protocolo de varredura ultra-rápida ($T \le 2\text{ s}$) que preserva a detectabilidade necessária para pacientes de emergência.
\end{enumerate}

\section{Sistematização do Pipeline Metrológico Padronizado AAPM TG-233}
\label{sec:sistematizacao_pipeline_tg233}

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

% ------------------------------------------------------------------------------
% CAPÍTULO 5: CONCLUSÃO
% ------------------------------------------------------------------------------
\chapter{Conclusão}
\label{chap:conclusao}

A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram uma profunda transformação metodológica nas últimas décadas. Esta monografia realizou uma **revisão bibliográfica sistemática abrangente e uma modelagem teórico-metrológica unificada** da transição dos modelos analíticos lineares clássicos para as formulações perceptuais contemporâneas baseadas em inteligência artificial e detectores de contagem de fótons.

\section{Síntese das Contribuições Teórico-Metrológicas}
\label{sec:sintese_contribuicoes}
As principais conclusões e sínteses deste estudo estruturam-se em quatro eixos fundamentais:
\begin{enumerate}
  \item \textbf{Superação das Métricas Escalares Tradicionais:} Demonstrou-se formalmente que grandezas como $SNR$, $CNR$ e $\sigma_{\text{HU}}$ são inadequadas para avaliar tomógrafos com algoritmos não lineares (DLR e MBIR), uma vez que a redução artificial do ruído mascara alterações texturais severas (efeito ceroso) e o borramento de lesões sutis de baixo contraste;
  \item \textbf{Rigor Matemático do Paradigma TBIQ:} Consolidou-se a dedução analítica das quatro funções espectrais contínuas de Fourier ($TTF$, $NPS$, $E(f)$ e $W_{\text{task}}$), formalizando o Índice de Detectabilidade ($d'$) como a grandeza física central e unificadora preconizada pelo relatório AAPM TG-233;
  \item \textbf{Limites de Validade dos Modelos Lineares:} Evidenciaram-se as causas matemáticas pelas quais o modelo antropomórfico NPWE perde correlação com leitores humanos sob DLR ($r \approx 0{,}68$), justificando a necessidade dos observadores profundos DLMO baseados em Vision Transformers ($r > 0{,}95$);
  \item \textbf{Integração Multicritério em PCCT:} Sistematizou-se a física da contagem de fótons e demonstrou-se como a Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$ viabiliza protocolos clínicos balanceados entre dose mínima, tempo ultra-rápido e máxima eficácia diagnóstica.
\end{enumerate}

\section{Implicações para a Prática da Física Médica e Serviços de Radiologia}
\label{sec:implicacoes_pratica}
Os resultados desta revisão fornecem subsídios conceituais diretos para:
\begin{itemize}
  \item A elaboração de programas hospitalares avançados de garantia da qualidade alinhados à RDC ANVISA 611/2022 e ao relatório AAPM TG-233;
  \item A calibração e aceitação de novos tomógrafos clínicos equipados com reconstrução por aprendizado profundo e detectores PCCT;
  \item A fundamentação teórica necessária para que físicos médicos hospitalares atuem criticamente na otimização de protocolos clínicos sem depender exclusivamente de métricas subjetivas ou escalares obsoletas.
\end{itemize}

\section{Limitações do Estudo}
\label{sec:limitacoes_estudo}
Por se tratar de uma monografia de revisão bibliográfica e modelagem teórico-metrológica, as curvas e superfícies foram geradas através de simulações numéricas sintéticas controladas em Python, sem aquisição direta de imagens DICOM clínicas com pacientes ou simuladores físicos de bancada. Investigações empíricas futuras poderão implementar tais modelos em ambientes laboratoriais e hospitalares reais.

\section{Perspectivas Futuras}
\label{sec:perspectivas_futuras}
A evolução contínua da física de imagens médicas abre horizontes promissores para desenvolvimentos futuros:
\begin{enumerate}
  \item \textbf{Extensão para Imagens 4D Dinâmicas:} Aplicação de modelos perceptivos em tomografias temporais dinâmicas (angiotomografia coronariana com \emph{ECG-gating} e perfusão cerebral em AVC), incorporando a Função de Transferência Temporal ($TTF_t(f_t)$);
  \item \textbf{Modelos de Linguagem e Visão Multimodal:} Integração de \emph{Foundation Models} em saúde para gerar laudos estruturados com mapeamento de incerteza diagnóstica;
  \item \textbf{Mapeamento Espectral Multielementar em PCCT:} Quantificação de nanopartículas de bismuto, gadolínio e ouro para diagnóstico teranóstico molecular;
  \item \textbf{Estudos Psicofísicos Multicêntricos em Larga Escala:} Condução de experimentos 2AFC com grandes consórcios hospitalares para consolidação de bancos de dados públicos de referência metrológica.
\end{enumerate}

Conclui-se esta monografia com a convicção de que a física médica, ao integrar a mecânica quântica das radiações, o processamento estatístico de sinais e a neurociência da percepção visual, estabelece os alicerces definitivos para uma radiologia diagnóstica mais segura, precisa e personalizada.

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
print("Pacote Overleaf reestruturado e atualizado com sucesso!")
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

print("TCC reestruturado em 5 capitulos com Busca Booleana e Simulação concluído com sucesso!")
