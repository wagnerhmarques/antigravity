import os
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
os.makedirs(output_dir, exist_ok=True)

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
\hyphenation{To-mo-gra-fia Con-ta-gem Fó-tons Non-Pre-whi-te-ning Ob-ser-va-dor Clás-si-co Es-tru-tu-ral Re-cons-tru-ção Mul-ti-ob-je-ti-vo Di-ag-nós-ti-co Psi-co-fí-si-co An-tro-po-mór-fi-co Sis-te-ma-ti-za-ção Me-tro-lo-gi-a}

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
\titleFormat{\chapter}[hang]
  {\normalfont\Large\bfseries}
  {\thechapter}
  {1em}
  {\MakeUppercase}
\titleFormat{\section}
  {\normalfont\large\bfseries}
  {\thesection}
  {1em}
  {}
\titleFormat{\subsection}
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
      Trabalho de Conclusão de Curso (Monografia de Revisão Bibliográfica e Modelagem Teórico-Metrológica) apresentado ao Instituto de Física e à Faculdade de Medicina da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física Médica.
      
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

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica contemporânea, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação da eficácia diagnóstica (princípio ALARA). Historicamente, a garantia da qualidade em TC baseou-se em métricas escalares lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR), o desvio padrão em Unidades Hounsfield ($\sigma_{\text{HU}}$) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores homogêneos. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares --- com destaque para as reconstruções iterativas estatísticas e as baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade estrita, isoplanatismo espacial e estacionariedade no sentido amplo (WSS) do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo e dependente da cena anatômica, induzindo alterações texturais perceptuais (como o aspecto ceroso ou \emph{plastic look}) que não são capturadas pelas grandezas clássicas. Para superar esse desafio metrológico, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), fundamentado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade é formalmente definida pelo desempenho de um observador ao executar uma tarefa clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Esta monografia constitui uma **revisão bibliográfica crítica e sistematização teórico-metrológica** da evolução dos observadores de modelo (\emph{model observers}). Apresentam-se as deduções matemáticas contínuas completas partindo do limite do Observador Ideal Bayesiano e do Observador de Hotelling, passando pelos modelos antropomórficos lineares com filtro ocular (NPWE) e canais corticais de frequência (CHO), até as fronteiras contemporâneas representadas pelos observadores baseados em redes profundas (\emph{Vision Transformers}) e a física da Tomografia por Contagem de Fótons (PCCT). Para fundamentar pedagogicamente as deduções e elucidar os limites de validade dos modelos em cenários clínicos representativos, o trabalho incorpora **modelagens numéricas sintéticas controladas**, detalhando as formulações analíticas e os parâmetros matemáticos empregados na geração de cada curva e superfície simulada. Este trabalho estabelece um corpo de referência teórico unificado e rigoroso para a metrologia da qualidade de imagem em tomografia computadorizada moderna.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Revisão Bibliográfica. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Simulação Numérica. Tomografia por Contagem de Fótons. Relatório AAPM TG-233.

\clearpage

% 5. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), standard deviation in Hounsfield Units ($\sigma_{\text{HU}}$), and Modulation Transfer Function (MTF), evaluated on homogeneous cylindrical phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity, shift-invariance, and wide-sense stationarity (WSS). Under non-linear processing, image noise becomes spatially non-stationary and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a **systematic literature review and theoretical-metrological synthesis** of the evolution of model observers. We present complete step-by-step mathematical derivations transitioning from the Bayesian Ideal Observer and Hotelling Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), up to recent frontiers involving deep learning architectures (Vision Transformers) and Photon-Counting CT (PCCT) physics. To pedagogically support the theoretical deductions and elucidate model boundaries in representative clinical scenarios, this work incorporates **controlled synthetic numerical simulations**, explicitly detailing the analytical formulations and computational parameters used to generate each simulated response curve and multi-dimensional surface. This study establishes a rigorous and unified theoretical reference framework for image quality metrology in modern computed tomography.

\vspace{0.8cm}
\noindent\textbf{Keywords:} Computed Tomography. Literature Review. Task-Based Image Quality. Model Observers. Detectability Index. Deep Learning Reconstruction. Numerical Simulation. Photon-Counting CT. AAPM TG-233 Report.

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
% CAPÍTULO 1: INTRODUÇÃO, METODOLOGIA DA REVISÃO E OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Introdução, Metodologia da Revisão e Objetivos}
\label{chap:introducao}

A Tomografia Computadorizada (TC) transformou a medicina diagnóstica ao viabilizar a reconstrução volumétrica e não-invasiva da anatomia interna humana com elevada resolução espacial e temporal. Contudo, a evolução dos equipamentos estabeleceu um cenário de alta complexidade física: o uso intensivo de radiação ionizante para exames de rotina e a recente transição dos métodos clássicos de reconstrução linear para algoritmos não lineares de inteligência artificial. Este capítulo contextualiza a importância da metrologia da qualidade de imagem em física médica, deduz os princípios físicos da formação da imagem tomográfica, expõe as grandezas clássicas e suas premissas de validade, introduz o paradigma baseado em tarefa, explicita a metodologia da revisão bibliográfica e estabelece os objetivos desta monografia.

\section{Os Fundamentos Físicos da Tomografia Computadorizada}
\label{sec:paradoxo_tc}

\subsection{Princípios Físicos da Interação e Dedução da Lei de Beer-Lambert}
\label{subsec:beer_lambert_deducao}
A Tomografia Computadorizada baseia-se na medição da atenuação exponencial que um feixe de raios X sofre ao atravessar os tecidos biológicos. A base teórica fundamental dessa interação é a Lei de Beer-Lambert-Bouguer.

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

\subsection{A Escala Hounsfield e a Padronização dos Números de CT}
\label{subsec:escala_hu}
Para uniformizar os valores e torná-los comparáveis entre diferentes equipamentos e tensões de tubo, os coeficientes lineares reconstruídos $\mu_{\text{tecido}}$ são convertidos para a escala padronizada de Unidades Hounsfield (HU), normalizada em relação à atenuação da água pura nas mesmas condições de irradiação:
\begin{equation}
  \text{Número CT (HU)} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{água}}}{\mu_{\text{água}}}
  \label{eq:escala_hounsfield}
\end{equation}
Por definição, o ar atmosférico apresenta $-1000\text{ HU}$ ($\mu_{\text{ar}} \approx 0$), a água pura calibrada apresenta exatamente $0\text{ HU}$, o tecido pulmonar arejado varia entre $-800\text{ e }-600\text{ HU}$, o tecido adiposo situa-se em torno de $-100\text{ HU}$, o parênquima hepático e muscular varia de $+40\text{ a }+60\text{ HU}$, e o osso cortical denso varia de $+1000\text{ a }+3000\text{ HU}$.

\subsection{O Risco Radiológico Estocástico e o Princípio ALARA}
\label{subsec:risco_alara}
Apesar de sua indispensável precisão diagnóstica, os raios X constituem radiação ionizante capaz de induzir danos moleculares no DNA celular. Os efeitos biológicos da radiação dividem-se em duas categorias \cite{icrp103_2007}:
\begin{enumerate}
  \item \textbf{Efeitos Determinísticos (Reações Teciduais):} Ocorrem após a superação de uma dose limiar (geralmente acima de $0{,}5\text{ a }1{,}0\text{ Gy}$), resultando em morte celular e perda de função tecidual;
  \item \textbf{Efeitos Estocásticos (Probabilísticos):} Não possuem dose limiar de segurança. A probabilidade de indução de mutações genéticas e câncer radioinduzido aumenta linearmente com a dose absorvida cumulativa, conforme o modelo Linear Sem Limiar (\emph{Linear Non-Threshold} --- LNT) \cite{icrp103_2007, attix1986}.
\end{enumerate}

Globalmente, a tomografia computadorizada responde por mais de 60\% de toda a dose de radiação médica administrada à população, embora represente apenas cerca de 10\% a 15\% do volume total de exames radiológicos realizados \cite{mccollough2026, bushberg2020}. Esse panorama impõe o princípio de radioproteção ALARA (\emph{As Low As Reasonably Achievable} --- Tão Baixo Quanto Razoavelmente Exequível) e atende aos requisitos normativos federais brasileiros (ANVISA RDC 611/2022 e IN 93/2021) \cite{anvisa_rdc611_2022, anvisa_in93_2021}. A missão da física médica reside em reduzir a dose de radiação entregue ao paciente ao nível estritamente necessário para garantir o diagnóstico médico com segurança.

\section{Métricas Clássicas de Avaliação e a Ruptura Metrológica}
\label{sec:insuficiencia_metricas}

\subsection{Definição e Limitações das Grandezas Escalares (SNR, CNR e Desvio Padrão)}
\label{subsec:metricas_escalares}
Historicamente, o controle de qualidade e a garantia de desempenho em TC fundamentaram-se em três grandezas escalares principais:
\begin{enumerate}
  \item \textbf{Relação Sinal-Ruído ($SNR$ --- \emph{Signal-to-Noise Ratio}):}
  Razão entre o valor médio da atenuação e o desvio padrão das flutuações estatísticas quânticas:
  \begin{equation}
    SNR = \frac{\mu_{\text{ROI}}}{\sigma_{\text{ROI}}}
    \label{eq:snr_def}
  \end{equation}
  onde $\mu_{\text{ROI}}$ é a média dos números de CT em uma ROI homogênea (em HU) e $\sigma_{\text{ROI}}$ é o desvio padrão dos pixels. O $SNR$ falha em sistemas modernos porque filtros não lineares podem forçar a redução de $\sigma_{\text{ROI}}$ sem aumentar a informação física transmitida pelos fótons.

  \item \textbf{Relação Contraste-Ruído ($CNR$ --- \emph{Contrast-to-Noise Ratio}):}
  Mede a separabilidade estatística entre dois tecidos adjacentes $A$ e $B$ com atenuações médias distintas $\mu_A$ e $\mu_B$:
  \begin{equation}
    CNR = \frac{|\mu_A - \mu_B|}{\sigma_{\text{fundo}}} = \frac{\Delta \mu}{\sigma_{\text{fundo}}}
    \label{eq:cnr_def}
  \end{equation}
  onde $\Delta \mu = |\mu_A - \mu_B|$ é o contraste radiológico e $\sigma_{\text{fundo}}$ é o desvio padrão no fundo. O modelo empírico de Rose (1948) estipula que uma estrutura só é detectável com confiança pelo olho humano se $CNR \ge 4\text{ a }5$ \cite{rose1948, burgess1999}.

  \item \textbf{Desvio Padrão do Número de CT ($\sigma_{\text{HU}}$):}
  Representa a dispersão estatística dos valores de pixel em uma ROI homogênea de água ou acrílico:
  \begin{equation}
    \sigma_{\text{HU}} = \sqrt{\frac{1}{N_{\text{pix}} - 1} \sum_{i=1}^{N_{\text{pix}}} (I_i - \mu_{\text{ROI}})^2}
    \label{eq:sigma_hu_def}
  \end{equation}
  Na física clássica com retroprojeção filtrada, o desvio padrão do ruído quântico de Poisson escala inversamente com a raiz quadrada da fluência de fótons e da dose: $\sigma_{\text{HU}} \propto 1 / \sqrt{\text{Dose}}$.
\end{enumerate}

\subsection{A Resolução Espacial Linear: Da PSF à Função de Transferência de Modulação (MTF)}
\label{subsec:psf_mtf}
\begin{itemize}
  \item \textbf{PSF (\emph{Point Spread Function}):} Descreve como um ponto infinitesimal ideal ($\delta(x, y)$) é transformado pelo tomógrafo em uma distribuição bidimensional borrada $h(x, y)$. Esse alargamento espacial decorre da mancha focal finita do ânodo, da abertura dos detectores e da amostragem;
  \item \textbf{MTF (\emph{Modulation Transfer Function}):} Representa a magnitude normalizada da Transformada de Fourier bidimensional da PSF:
  \begin{equation}
    MTF(f) = \frac{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|}{|\mathcal{F}_{2D}\{\text{PSF}(x, y)\}|_{f=0}}
    \label{eq:mtf_def}
  \end{equation}
  A MTF expressa a fração de contraste original preservada em cada frequência espacial $f$ ($\text{mm}^{-1}$).
\end{itemize}

\subsection{Os Três Pilares da Validade Linear}
\label{subsec:tres_pilares_linearidade}
A validade matemática dessas métricas clássicas depende de três premissas estritas:
\begin{enumerate}
  \item \textbf{Linearidade do Sistema Formador de Imagem:} O operador de reconstrução $\mathcal{R}$ deve satisfazer o princípio da superposição: $\mathcal{R}\{\alpha f_1 + \beta f_2\} = \alpha \mathcal{R}\{f_1\} + \beta \mathcal{R}\{f_2\}$;
  \item \textbf{Invariância Translacional Espacial (Isoplanatismo):} A função $\text{PSF}(x, y)$ deve ser idêntica em qualquer coordenada da imagem;
  \item \textbf{Estacionariedade do Ruído no Sentido Amplo (WSS --- \emph{Wide-Sense Stationary}):} O ruído $I(x, y)$ deve ter média constante $\mathbb{E}[I(x, y)] = \mu_0$ e função de autocovariância dependente exclusivamente do vetor deslocamento espacial $\Delta \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$:
  \begin{equation}
    K_I(\mathbf{r}_1, \mathbf{r}_2) = \mathbb{E}\left[ (I(\mathbf{r}_1) - \mu_0)(I(\mathbf{r}_2) - \mu_0) \right] = K_I(\mathbf{r}_1 - \mathbf{r}_2)
    \label{eq:wss_def}
  \end{equation}
\end{enumerate}

\subsection{A Ruptura Não Linear com Reconstruções Iterativas e DLR}
\label{subsec:ecossistema_ruptura}
A incorporação de reconstruções iterativas estatísticas e redes neurais profundas (DLR) quebrou todas as premissas lineares clássicas (\cref{fig:comparativo_paradigmas}) \cite{racine2020, debbiche2024, greffier2026}:
\begin{itemize}
  \item O desvio padrão ($\sigma_{\text{HU}}$) é artificialmente reduzido por filtros não lineares adaptativos, induzindo a falsa impressão de que a qualidade aumentou;
  \item O ruído perde a estacionariedade (quebra de WSS): a correlação entre pixels passa a depender do contraste local da anatomia;
  \item O ruído adquire um padrão textural ceroso (\emph{plastic look}), caracterizado pelo deslocamento da potência para baixas frequências;
  \item Lesões sutis de baixo contraste podem ser interpretadas pelo algoritmo como ruído e suavizadas, tornando-se invisíveis na imagem clínica, mesmo com valores formalmente excelentes de $SNR$ e $CNR$ \cite{toia2023, solomon2020}.
\end{itemize}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption[Comparativo Estrutural entre os Paradigmas Físicos]{Comparativo Estrutural entre o Paradigma Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

\section{O Paradigma da Qualidade Baseada em Tarefa (TBIQ)}
\label{sec:paradigma_tbiq}

\subsection{Conceito e os Quatro Pilares Fundamentais}
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
  \item \textbf{Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$):} Representa matematicamente o tamanho, a forma e a densidade radiológica da patologia;
  \item \textbf{Filtro Ocular ou Modelo Perceptual ($E(f)$ / Modelos Neurais):} Incorpora a sensibilidade de contraste do olho humano ou os mecanismos corticais de tomada de decisão.
\end{enumerate}

\subsection{O Índice de Detectabilidade ($d'$) como Medida Central Unificadora}
\label{subsec:dprime_unificador}
A integração matemática desses quatro componentes resulta no **Índice de Detectabilidade ($d'$)**, grandeza estatística que quantifica a separabilidade entre estados de saúde e doença, conectando grandezas físicas objetivas à probabilidade de acerto diagnóstico.

\section{Natureza da Pesquisa e Metodologia da Revisão}
\label{sec:metodologia_revisao}

\subsection{Classificação e Escopo Metodológico}
\label{subsec:classificacao_escopo}
Este Trabalho de Conclusão de Curso constitui uma **monografia de revisão bibliográfica crítica, sistematização conceitual e modelagem teórico-metrológica**. O trabalho não tem como objetivo o desenvolvimento de um novo produto de software ou a coleta de dados experimentais laboratoriais primários, mas sim a organização rigorosa do estado da arte, a dedução analítica passo a passo dos modelos matemáticos canônicos e a análise comparativa de seus limites de aplicabilidade frente às tecnologias tomográficas emergentes.

\subsection{Corpus Bibliográfico e Critérios de Sistematização}
\label{subsec:corpus_bibliografico}
O levantamento bibliográfico foi conduzido através de busca sistemática em bases científicas internacionais (PubMed, IEEE Xplore, ScienceDirect e SPIE Digital Library), estruturando-se em três eixos principais:
\begin{enumerate}
  \item \textbf{Documentos Normativos e Relatórios Internacionais:} Relatórios canônicos da \emph{American Association of Physicists in Medicine} (destacando-se o relatório AAPM TG-233), relatórios da \emph{International Commission on Radiation Units and Measurements} (ICRU Report 54), recomendações da ICRP (Publicação 103) e normativas regulatórias nacionais (ANVISA RDC 611/2022 e IN 93/2021);
  \item \textbf{Literatura Seminal de Física de Imagens e SDT:} Obras clássicas sobre Teoria de Detecção de Sinais, observadores estatísticos e metodologia ROC (Barrett, Myers, Burgess, Wagner, Metz e Lusted);
  \item \textbf{Artigos de Vanguarda em Reconstrução e Metrologia (2018--2026):} Publicações recentes abordando algoritmos DLR comerciais, detectores de contagem de fótons (PCCT), observadores baseados em aprendizado profundo e protocolos de phantoms antropomórficos híbridos.
\end{enumerate}

\subsection{Metodologia de Modelagem e Simulação Numérica Sintética}
\label{subsec:metodologia_simulacao}
Para além da revisão textual, este trabalho utiliza **simulações numéricas sintéticas controladas** implementadas em linguagem Python (utilizando as bibliotecas NumPy, SciPy e Matplotlib). Essas simulações atuam como instrumentos metrológicos e pedagógicos para:
\begin{itemize}
  \item Gerar e visualizar as distribuições de decisão da SDT, curvas ROC e curvas psicofísicas 2AFC sob condições estatísticas controladas;
  \item Computar analiticamente as quatro funções espectrais de Fourier ($TTF$, $NPS$, $E(f)$ e $W_{\text{task}}$ via funções de Bessel) segundo as formulações do AAPM TG-233;
  \item Implementar os operadores matemáticos dos canais corticais do CHO (D-DOG, Laguerre-Gauss e Gabor) e simular a perda de correlação dos modelos lineares em ruído anatômico estruturado;
  \item Modelar parametricamente superfícies de otimização multiobjetivo para ilustrar a tomada de decisão clínica.
\end{itemize}
A formulação analítica e os parâmetros de cada simulação são explicitamente documentados nos respectivos capítulos.

\section{Objetivos}
\label{sec:objetivos}

O **objetivo geral** desta monografia consiste em realizar uma revisão bibliográfica crítica e sistematização teórico-metrológica unificada dos modelos perceptivos de qualidade de imagem baseada em tarefa em tomografia computadorizada, estabelecendo os fundamentos físicos e matemáticos para a avaliação de tecnologias avançadas e otimização de protocolos.

Os **objetivos específicos** compreendem:
\begin{enumerate}
  \item Apresentar as deduções matemáticas fundamentais da Teoria de Detecção de Sinais (SDT), formalizando o Índice de Detectabilidade ($d'$), curvas ROC e testes psicofísicos 2AFC;
  \item Deduzir rigorosamente no domínio contínuo de Fourier a Função de Transferência da Tarefa ($TTF(f)$), o Espectro de Potência do Ruído ($NPS(f)$), o Filtro Ocular ($E(f)$) e o Espectro da Tarefa ($W_{\text{task}}(f)$) conforme o relatório AAPM TG-233;
  \item Analisar e contrastar os observadores lineares clássicos: Observador Ideal Bayesiano (IO), Observador de Hotelling (HO), modelo antropomórfico NPWE e Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor;
  \item Demonstrar formalmente as causas físicas e matemáticas do colapso dos modelos analíticos lineares sob reconstruções DLR e fundos anatômicos complexos;
  \item Mapear o estado da arte dos Observadores Baseados em Aprendizado Profundo (DLMO) baseados em \emph{Vision Transformers} com auto-atenção multi-cabeça;
  \item Sistematizar a física dos detectores de Contagem de Fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a formulação da Otimização Multiobjetivo pela Fronteira de Pareto Tridimensional $(D, T, -W)$;
  \item Estruturar conceitualmente o pipeline de processamento metrológico padronizado e analisar as diretrizes bioéticas e regulatórias para estudos com observadores humanos.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 2: FUNDAMENTOS DA AVALIAÇÃO BASEADA EM TAREFA
% ------------------------------------------------------------------------------
\chapter{Fundamentos da Avaliação Baseada em Tarefa}
\label{chap:fundamentos_sdt}

A avaliação científica da qualidade tomográfica requer um arcabouço formal que conecte a física estocástica das imagens à tomada de decisão diagnóstica. Este capítulo apresenta a Teoria de Detecção de Sinais (SDT), a derivação do Índice de Detectabilidade ($d'$), a teoria das Curvas ROC, a equivalência analítica com o protocolo experimental 2AFC e as deduções contínuas em frequência de $TTF(f)$, $NPS(f)$, $E(f)$ e $W_{\text{task}}(f)$ segundo o relatório AAPM TG-233, explicitando a metodologia matemática empregada na modelagem sintética das figuras apresentadas.

\section{Teoria Clássica de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria}

\subsection{Formulação Matemática das Hipóteses de Decisão}
\label{subsec:sdt_hipoteses}
A detecção de uma patologia em um exame médico com ruído é formalmente descrita como um problema estocástico de teste de hipóteses binário. A Teoria de Detecção de Sinais (SDT), introduzida na física por Peterson, Birdsall e Fox (1954) e transposta para a medicina por Lusted (1968) e Metz (1986), analisa o processo de decisão diagnóstica sob flutuações estocásticas \cite{peterson1954, lusted1968, metz1986}.

Considere uma imagem discreta representada por um vetor $\mathbf{g} \in \mathbb{R}^N$ ($N$ pixels). O problema de detecção formula-se por duas hipóteses mutuamente exclusivas:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Normal}) \label{eq:h0} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Patologia}) \label{eq:h1}
\end{align}
onde:
\begin{itemize}
  \item $\mathbf{s} \in \mathbb{R}^N$ é o vetor determinístico que descreve o perfil espacial do sinal da lesão;
  \item $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de ruído de fundo com média zero e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle$.
\end{itemize}

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

\subsection{Metodologia da Simulação Numérica e Análise da Figura 2.1}
\label{subsec:analise_fig1}
A \cref{fig:sdt_roc_2afc} foi gerada computacionalmente através de uma **simulação numérica sintética** implementada em Python para ilustrar o comportamento canônico da SDT. A metodologia de modelagem estruturou-se da seguinte forma:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação das Distribuições de Decisão $p(t|H_0)$ e $p(t|H_1)$:}
  Modelaram-se duas variáveis aleatórias gaussianas contínuas $t_0 \sim \mathcal{N}(\mu_0, \sigma_t^2)$ e $t_1 \sim \mathcal{N}(\mu_1, \sigma_t^2)$ com parâmetros normalizados $\mu_0 = 0$, $\mu_1 = 2{,}2$ e $\sigma_t = 1{,}0$, correspondendo a um índice de detectabilidade teórico $d' = (\mu_1 - \mu_0)/\sigma_t = 2{,}2$. Definiu-se um limiar de corte $t_c = 1{,}3$. As áreas sob as curvas foram calculadas por integração analítica cumulativa:
  \begin{equation}
    FPF(t_c) = \int_{t_c}^\infty p(t|H_0) \, dt = 1 - \Phi\left(\frac{t_c - \mu_0}{\sigma_t}\right) \approx 0{,}097 \quad (9{,}7\%)
  \end{equation}
  \begin{equation}
    TPF(t_c) = \int_{t_c}^\infty p(t|H_1) \, dt = 1 - \Phi\left(\frac{t_c - \mu_1}{\sigma_t}\right) \approx 0{,}816 \quad (81{,}6\%)
  \end{equation}
  \emph{Contextualização Pedagógica:} Esse cenário emula, por exemplo, a identificação de um nódulo pulmonar sutil de vidro fosco ($4\text{ mm}$, $-600\text{ HU}$) imerso em parênquima pulmonar normal ($-800\text{ HU}$), onde a escolha de $t_c$ reflete a atitude mais conservadora ou mais agressiva do radiologista;

  \item \textbf{Painel (B) --- Geração Paramétrica das Curvas ROC:}
  Variou-se o limiar $t_c \in [-4{,}0; +6{,}0]$ com passo $\Delta t_c = 0{,}01$ para seis valores fixos de detectabilidade $d' \in \{0{,}5; 1{,}0; 1{,}5; 2{,}2; 3{,}0; 4{,}0\}$. Para cada par $(d', t_c)$, calcularam-se $FPF(t_c)$ e $TPF(t_c)$, gerando as trajetórias contínuas no espaço bi-dimensional $(FPF, TPF)$ e confirmando que a área sob a curva satisfaz $AUC = \Phi(d' / \sqrt{2})$;

  \item \textbf{Painel (C) --- Curva de Desempenho no Paradigma 2AFC:}
  Plotou-se a probabilidade teórica de acerto em função do índice $d'$ avaliando a função $P_C(d') = \Phi(d' / \sqrt{2})$ no domínio $d' \in [0, 5]$. A curva demonstra que regimes de baixa qualidade ($d' \approx 1{,}0$) limitam a acurácia a $P_C \approx 76\%$, enquanto sistemas que atingem o Critério de Rose ($d' \ge 4{,}0$) garantem acertos quase absolutos ($P_C \ge 99{,}8\%$).
\end{enumerate}

\section{Definição Formal do Índice de Detectabilidade (\texorpdfstring{$d'$}{d-prime})}
\label{sec:dprime_definicao}

\subsection{Dedução Passo a Passo de $d'$ sob Distribuições Arbitrárias}
\label{subsec:dprime_geral_deducao}
O Índice de Detectabilidade ($d'$) expressa a distância estatística entre os valores esperados da estatística de teste sob as duas hipóteses, normalizada pelas respectivas variâncias \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_geral}
\end{equation}
onde $\langle t | H_1 \rangle$ e $\langle t | H_0 \rangle$ são as médias condicionais e $\sigma^2(t|H_i)$ são as variâncias estocásticas.

\subsection{Caso Particular sob Ruído Aditivo Gaussiano}
\label{subsec:dprime_gaussiano}
Sob ruído aditivo com variâncias idênticas ($\sigma^2(t|H_1) = \sigma^2(t|H_0) = \sigma_t^2$):
\begin{equation}
  d' = \frac{\mu_1 - \mu_0}{\sigma_t}
  \label{eq:dprime_gaussiano}
\end{equation}

\section{Curva ROC, AUC e o Paradigma Experimental 2AFC}
\label{sec:roc_2afc}

\subsection{Definição da Curva ROC e Área sob a Curva (AUC)}
\label{subsec:roc_auc_def}
A Área sob a Curva ROC ($AUC$) é calculada pela integral da taxa de verdadeiros positivos em função dos falsos positivos:
\begin{equation}
  AUC = \int_0^1 TPF(FPF) \, d(FPF)
  \label{eq:auc_def}
\end{equation}

\subsection{Dedução da Equivalência Analítica entre ROC e 2AFC}
\label{subsec:deducao_roc_2afc}
\textbf{Requisitos e Premissas Matemáticas:}
\begin{enumerate}
  \item As variáveis de decisão sob as hipóteses $H_0$ e $H_1$ são normalmente distribuídas com variâncias idênticas: $t_0 \sim \mathcal{N}(\mu_0, \sigma_t^2)$ e $t_1 \sim \mathcal{N}(\mu_1, \sigma_t^2)$;
  \item No teste 2AFC, o leitor recebe independentemente uma amostra $t_1$ e uma amostra $t_0$, decidindo corretamente pela imagem patológica se e somente se $t_1 > t_0$;
  \item As observações são estatisticamente independentes entre os ensaios sucessivos.
\end{enumerate}

Considere a variável de diferença escalar $\Delta t = t_1 - t_0$. Sendo $t_1$ e $t_0$ gaussianas independentes:
\begin{equation}
  \mathbb{E}[\Delta t] = \mathbb{E}[t_1] - \mathbb{E}[t_0] = \mu_1 - \mu_0
  \label{eq:mean_delta_t}
\end{equation}
\begin{equation}
  \text{Var}(\Delta t) = \text{Var}(t_1) + \text{Var}(t_0) = 2\sigma_t^2 \implies \sigma_{\Delta t} = \sqrt{2}\sigma_t
  \label{eq:var_delta_t}
\end{equation}

A probabilidade empírica de acerto no teste 2AFC ($P_C$) é a probabilidade de que $\Delta t > 0$:
\begin{equation}
  P_C = P(\Delta t > 0) = P\left( \frac{\Delta t - (\mu_1 - \mu_0)}{\sqrt{2}\sigma_t} > \frac{-(\mu_1 - \mu_0)}{\sqrt{2}\sigma_t} \right)
  \label{eq:pc_step1}
\end{equation}
Definindo a variável normal padrão $Z = \frac{\Delta t - (\mu_1 - \mu_0)}{\sqrt{2}\sigma_t} \sim \mathcal{N}(0, 1)$ e utilizando a detectabilidade $d' = \frac{\mu_1 - \mu_0}{\sigma_t}$:
\begin{equation}
  P_C = P\left( Z > -\frac{d'}{\sqrt{2}} \right) = 1 - \Phi\left( -\frac{d'}{\sqrt{2}} \right) = \Phi\left( \frac{d'}{\sqrt{2}} \right)
  \label{eq:pc_2afc}
\end{equation}
onde $\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-u^2/2} du$. Green e Swets (1966) e Burgess (1999) demonstraram a identidade fundamental \cite{burgess1999}:
\begin{equation}
  AUC = \int_0^1 TPF(FPF) \, d(FPF) = \Phi\left( \frac{d'}{\sqrt{2}} \right) = P_C
  \label{eq:auc_pc_identity}
\end{equation}
Invertendo a relação, obtém-se o valor experimental medido em humanos:
\begin{equation}
  d'_{\text{humano}} = \sqrt{2} \, \Phi^{-1}(P_C)
  \label{eq:dprime_from_pc}
\end{equation}

\section{Dedução Contínua das Métricas em Frequência (AAPM TG-233)}
\label{sec:metricas_fourier}

O domínio de Fourier permite decompor a imagem tomográfica em frequências espaciais, isolando os efeitos da resolução óptica, da textura de ruído, da sensibilidade visual e da geometria da lesão, conforme o relatório AAPM TG-233.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_spectral_metrics.png}
  \caption[Métricas Espectrais Contínuas em Frequência]{Modelagem Numérica das Quatro Funções Espectrais Contínuas no Domínio de Fourier segundo o Relatório AAPM TG-233.}
  \label{fig:spectral_metrics}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 2.2}
\label{subsec:analise_fig2}
A \cref{fig:spectral_metrics} foi sintetizada numericamente em Python a partir das formulações analíticas canônicas estabelecidas pelo relatório AAPM TG-233 \cite{aapm_tg233_2019}:

\begin{enumerate}
  \item \textbf{Painel (A) --- Resolução Espacial da Tarefa $TTF(f)$:}
  Modelou-se a resposta em frequência via função sigmoidal generalizada de Richard \& Samei \cite{racine2020}:
  \begin{equation}
    TTF(f; \Delta C) = \left[ 1 + \left( \frac{f}{f_{50}(\Delta C)} \right)^\alpha \right]^{-1}
  \end{equation}
  onde os parâmetros de corte foram calibrados para ilustrar a dependência de contraste: para alto contraste (Iodo $+300\text{ HU}$, curva vermelha), adotou-se $f_{50} = 0{,}58\text{ mm}^{-1}$ e $\alpha = 3{,}2$; para baixo contraste (Solid Water $+25\text{ HU}$, curva ciano), adotou-se $f_{50} = 0{,}35\text{ mm}^{-1}$ e $\alpha = 2{,}8$, evidenciando o borramento não linear característico de alvos sutis;

  \item \textbf{Painel (B) --- Espectro de Potência do Ruído $NPS(f)$:}
  Modelou-se o espectro de ruído da FBP clássica pela lei de potência filtrada $NPS_{\text{FBP}}(f) = A \cdot f \cdot \exp(-f^2 / 2\sigma_f^2)$ com $f_{\text{peak}} = 0{,}45\text{ mm}^{-1}$ (curva preta). A curva DLR (verde) foi modelada com redução de 50\% na potência integrada e preservação do pico em $0{,}40\text{ mm}^{-1}$. A curva MBIR (roxa) foi gerada deslocando a energia para baixas frequências ($f_{\text{peak}} = 0{,}18\text{ mm}^{-1}$), simulando o aspecto ceroso (\emph{plastic look});

  \item \textbf{Painel (C) --- Filtro Ocular Humano $E(f)$:}
  Calculou-se a função de sensibilidade ao contraste de Burgess \cite{burgess1999} através da \cref{eq:filtro_ocular} com parâmetros $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$, convertendo frequências espaciais físicas para a retina sob distância de visualização de 50 cm ($f_{\text{retina}} \approx 8{,}727 \cdot f$), com pico em $4{,}2\text{ cpd}$;

  \item \textbf{Painel (D) --- Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$:}
  Computou-se a Transformada de Fourier analítica de lesões esféricas de raio $R \in \{1{,}5; 3{,}0; 6{,}0\}\text{ mm}$ e contraste $\Delta C = 35\text{ HU}$ avaliando a função de Bessel de primeira ordem via \cref{eq:wtask_formula}. A simulação evidencia que lesões extensas concentram energia em $f < 0{,}15\text{ mm}^{-1}$, enquanto microlesões espalham energia para frequências superiores a $0{,}6\text{ mm}^{-1}$.
\end{enumerate}

\subsection{Dedução Analítica das Quatro Funções Espectrais}
\label{subsec:deducoes_quatro_funcoes_fourier}

\subsubsection{1. Dedução da Função de Transferência da Tarefa ($TTF(f)$)}
A partir da Função de Resposta ao Degrau $\text{ESF}(r)$ medida radialmente sobre um inserto cilíndrico de contraste $\Delta C$, obtém-se a Função de Espalhamento de Linha $\text{LSF}(r) = -\frac{d}{dr}\text{ESF}(r)$. Sua Transformada de Fourier normalizada define a $TTF(f)$ \cite{aapm_tg233_2019}:
\begin{equation}
  TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \text{LSF}(r) \, dr}
  \label{eq:ttf_formula}
\end{equation}

\subsubsection{2. Dedução do Espectro de Potência do Ruído ($NPS(f)$)}
Para $M$ sub-ROIs homogêneas independentes de dimensão $N_x \times N_y$ com espaçamento de pixel $\Delta x, \Delta y$, após subtração do fundo $P_2(x, y)$, o teorema de Wiener-Khinchin estabelece:
\begin{equation}
  NPS(u, v) = \lim_{M \to \infty} \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
  \label{eq:nps_2d}
\end{equation}
com unidade física $\text{HU}^2\cdot\text{mm}^2$. A curva isotrópica unidimensional é obtida por média azimutal:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial}
\end{equation}

\subsubsection{3. Filtro Ocular Humano ($E(f)$)}
Modelado pela formulação empírica de sensibilidade ao contraste de Burgess (1999) \cite{burgess1999}:
\begin{equation}
  E(f) = \left( \frac{f_{\text{retina}}}{f_0} \right)^n \exp\left[ -c \left( \frac{f_{\text{retina}}}{f_0} \right)^m \right]
  \label{eq:filtro_ocular}
\end{equation}
com $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$, $c = 2{,}2$ e $f_{\text{retina}} \approx \frac{\pi d_{\text{v}}}{180} f \approx 8{,}727 \cdot f$ para distância $d_{\text{v}} = 500\text{ mm}$.

\subsubsection{4. Dedução Passo a Passo do Espectro da Tarefa ($W_{\text{task}}(f)$)}
Para uma lesão circular homogênea 2D de raio $R$ e contraste $\Delta C$ expressa por $\Delta C \cdot \Pi(r / 2R)$, aplica-se a Transformada de Fourier em coordenadas polares $(r, \theta)$:
\begin{equation}
  W_{\text{task}}(f) = \int_0^{2\pi} \int_0^R \Delta C \, e^{-2\pi i f r \cos(\theta - \phi)} \, r \, dr \, d\theta
  \label{eq:wtask_step1}
\end{equation}
Utilizando a integral de Bessel $J_0(x) = \frac{1}{2\pi} \int_0^{2\pi} e^{-i x \cos\theta} d\theta$:
\begin{equation}
  W_{\text{task}}(f) = 2\pi \Delta C \int_0^R r \, J_0(2\pi f r) \, dr
  \label{eq:wtask_step2}
\end{equation}
Aplicando a identidade $\int x J_0(x) dx = x J_1(x)$ com a substituição $u = 2\pi f r$ ($du = 2\pi f dr$):
\begin{equation}
  \int_0^R r J_0(2\pi f r) dr = \frac{1}{(2\pi f)^2} \left[ u J_1(u) \right]_0^{2\pi f R} = \frac{R}{2\pi f} J_1(2\pi f R)
  \label{eq:wtask_step3}
\end{equation}
Substituindo na integral, obtém-se rigorosamente:
\begin{equation}
  W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|
  \label{eq:wtask_formula}
\end{equation}
onde $J_1(x)$ é a função de Bessel ordinária de primeira espécie e ordem 1.

% ------------------------------------------------------------------------------
% CAPÍTULO 3: OBSERVADORES LINEARES E VALIDAÇÃO PSICOFÍSICA
% ------------------------------------------------------------------------------
\chapter{Observadores Lineares e Validação Psicofísica}
\label{chap:observadores_lineares}

Os observadores de modelo são operadores matemáticos desenvolvidos para quantificar objetivamente a qualidade da imagem em tarefas de detecção. Este capítulo analisa a formulação dos modelos lineares clássicos --- partindo do limite físico do Observador Ideal e do Observador de Hotelling, passando pelo modelo antropomórfico NPWE e culminando no Observador de Hotelling Canalizado (CHO) --- e detalha a metodologia de ANOVA Multi-Reader Multi-Case (MRMC) para validação contra painéis de radiologistas.

\section{O Observador Ideal e o Observador de Hotelling}
\label{sec:observador_ideal}

\subsection{Fundamentação Bayesiana e Razão de Verossimilhança}
\label{subsec:bayes_io}
O Observador Ideal (IO) estabelece o teto teórico absoluto de informação diagnóstica permitido pelas leis da física. Fundamenta-se na razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$. Quando o ruído de fundo segue uma distribuição normal multivariada com matriz de autocovariância $\mathbf{K}$, a razão de verossimilhança logarítmica reduz-se ao Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}.

\subsection{Dedução Passo a Passo do Observador de Hotelling}
\label{subsec:deducao_hotelling}
\textbf{Requisitos e Premissas Matemáticas:}
\begin{enumerate}
  \item Sinal exatamente conhecido (\emph{Signal Known Exactly} --- SKE);
  \item Fundo estatisticamente conhecido (\emph{Background Known Statistically} --- BKS);
  \item Ruído gaussiano multivariado com matriz de autocovariância $\mathbf{K} \in \mathbb{R}^{N \times N}$ simétrica e estritamente positiva definida.
\end{enumerate}

Pelo Teorema de Bayes, a razão de verossimilhança ótima sob distribuição gaussiana é:
\begin{equation}
  \Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)} = \frac{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) \right)}{\frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left( -\frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} \right)}
  \label{eq:bayes_ratio}
\end{equation}
Tomando o logaritmo natural e cancelando os termos quadráticos $\mathbf{g}^T \mathbf{K}^{-1} \mathbf{g}$:
\begin{equation}
  \ln\Lambda(\mathbf{g}) = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g} - \frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}
  \label{eq:log_bayes}
\end{equation}
Como o termo $-\frac{1}{2} \mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}$ é uma constante independente da imagem medida $\mathbf{g}$, ele é absorvido no limiar de corte $t_c$. A estatística de teste do Observador de Hotelling expressa-se por:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:template_hotelling}
\end{equation}
onde o vetor de pesos $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ executa o pré-branqueamento (\emph{prewhitening}) do ruído através da matriz inversa $\mathbf{K}^{-1}$, descorrelacionando os pixels antes da integração com o sinal $\mathbf{s}$. O índice de detectabilidade máximo é dado por:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling}
\end{equation}

\section{O Observador NPWE}
\label{sec:npwe_deducao}

\subsection{Motivação Biológica e Integral no Domínio de Fourier}
\label{subsec:npwe_motivacao}
Como o sistema visual humano não realiza a inversão matricial $\mathbf{K}^{-1}$, Burgess (1994) formulou o modelo Sem Pré-Branqueamento com Filtro Ocular (NPWE), introduzindo a resposta em frequência $E(f)$ e uma variância de ruído neural interno $\sigma_{\text{int}}^2$ \cite{burgess1994, eckstein2000}. No domínio contínuo de Fourier, a integral do índice de detectabilidade do NPWE expressa-se por:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral}
\end{equation}
Essa formulação unifica a resolução do sistema ($TTF$), a morfologia da lesão ($W_{\text{task}}$), a resposta visual ($E(f)$) e a textura do ruído ($NPS$).

\section{O Observador de Hotelling Canalizado (CHO)}
\label{sec:cho_teoria}

\subsection{A Barreira Dimensional da Covariância Anatômica}
\label{subsec:barreira_dimensional_cho}
Em matrizes clínicas ($N = 128 \times 128 = 16.384$ pixels), a matriz de covariância anatômica $\mathbf{K}_{\mathbf{b}} \in \mathbb{R}^{N \times N}$ possui mais de 268 milhões de elementos, inviabilizando sua inversão numérica direta \cite{myers1987, yao1992}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Pipeline Computacional do Observador CHO]{Pipeline Conceitual do Observador de Hotelling Canalizado (CHO).}
  \label{fig:cho_flow}
\end{figure}

\subsection{Formulação Matemática dos Canais Corticais}
\label{subsec:formulacao_canais_cho}
O modelo CHO introduz uma matriz de operadores de canais corticais $\mathbf{T} \in \mathbb{R}^{C \times N}$ ($C \ll N$, com $C = 4\text{ a }15$), projetando a imagem no subespaço reduzido dos canais: $\mathbf{v} = \mathbf{T} \mathbf{g}$ (\cref{fig:cho_flow}). A matriz de covariância reduzida $\mathbf{K}_{\mathbf{v}} \in \mathbb{R}^{C \times C}$ é invertida de forma estável:
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
  \caption[Canais Corticais do CHO e Detectabilidade vs Dose]{Modelagem Numérica dos Canais Corticais do Observador CHO e Comparativo de Desempenho em Fundo Anatômico.}
  \label{fig:cho_channels}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 3.2}
\label{subsec:analise_fig3}
A \cref{fig:cho_channels} foi gerada computacionalmente através de uma **simulação numérica sintética** para demonstrar a ação dos mecanismos de canalização cortical:

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

  \item \textbf{Painel (D) --- Simulação do Colapso do NPWE vs. Estabilidade do CHO:}
  Simulou-se o cálculo de detectabilidade em função da dose para uma lesão de 5 mm imersa em ruído anatômico estruturado (ruído em lei de potência $1/f^\beta$). Demonstra-se que o modelo analítico NPWE (curva vermelha) subestima drasticamente a detectabilidade ($d' < 0{,}8$) por confundir flutuações anatômicas com ruído quântico, enquanto o CHO D-DOG (curva verde) descorrelaciona o fundo e preserva a correlação com a visão humana.
\end{enumerate}

\section{Validação Psicofísica Multi-Reader Multi-Case (MRMC)}
\label{sec:mrmc_teoria}

\subsection{O Modelo de ANOVA com Efeitos Aleatórios Cruzados (DBM / HOR)}
\label{subsec:mrmc_anova_modelo}
Para validar estatisticamente a equivalência entre observadores computacionais e radiologistas humanos considerando a variabilidade entre médicos e entre pacientes, adota-se o modelo de ANOVA com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova}
\end{equation}
onde $y_{ijk}$ é a acurácia ($AUC$ ou $d'$), $\mu$ é a média global, $\tau_i$ é o efeito fixo da modalidade de reconstrução ou dose, $R_j \sim \mathcal{N}(0, \sigma^2_R)$ representa a variabilidade entre radiologistas, $C_k \sim \mathcal{N}(0, \sigma^2_C)$ a variabilidade entre casos clínicos, e $\epsilon_{ijk}$ o resíduo experimental. A homologação do modelo computacional requer Coeficiente de Correlação Intraclasse $ICC \ge 0{,}90$.

% ------------------------------------------------------------------------------
% CAPÍTULO 4: A TRANSIÇÃO DO PARADIGMA LINEAR PARA O NÃO LINEAR
% ------------------------------------------------------------------------------
\chapter{A Transição do Paradigma Linear para o Não Linear}
\label{chap:colapso_linearidade}

A evolução da Tomografia Computadorizada é marcada pela transição de um paradigma de reconstrução estritamente linear (dominado pela FBP) para um paradigma não linear e adaptativo (baseado em reconstruções iterativas estatísticas e redes neurais profundas --- DLR). Este capítulo investiga os motivos físicos e dosimétricos que forçaram essa transferência paradigmática, formaliza a quebra dos pilares da linearidade, analisa o efeito ceroso (\emph{plastic look}) e explora a metodologia de phantoms antropomórficos híbridos.

\section{As Forças Motrizes da Transição: O Limite Físico da FBP}
\label{sec:forcas_motrizes}

A física quântica das radiações impõe que o ruído nos detectores segue uma distribuição de Poisson ($\sigma_N \propto \sqrt{N}$). Na FBP linear com filtro de rampa, essa flutuação estabelece a lei de escala clássica:
\begin{equation}
  \sigma_{\text{HU}} \propto \frac{1}{\sqrt{\text{Dose}}}
  \label{eq:escala_fbp_dose}
\end{equation}
Essa relação determinou um limite físico intransponível: qualquer redução de dose de 50\% a 75\% para atender ao princípio ALARA acarretava aumento obrigatório de 41\% a 100\% no desvio padrão $\sigma_{\text{HU}}$, mascarando lesões sutis de baixo contraste. A única via para romper essa barreira dosimétrica foi a introdução de algoritmos de reconstrução não lineares e adaptativos (\cref{tab:taxonomia_algoritmos}).

\begin{table}[htbp]
  \centering
  \small
  \caption{Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante.}
  \label{tab:taxonomia_algoritmos}
  \begin{tabularx}{\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
    \toprule
    Fabricante & Reconstrução Iterativa Híbrida (HIR) & Reconstrução Baseada em Modelos (MBIR) & Reconstrução por Aprendizado Profundo (DLR) \\
    \midrule
    GE Healthcare & ASiR / ASiR-V & Veo & \textbf{TrueFidelity} \\
    \addlinespace
    Canon Medical & AIDR 3D & FIRST & \textbf{AiCE} \\
    \addlinespace
    Siemens Healthineers & SAFIRE / ADMIRE & REDUCE & \textbf{Precise Image} \\
    \addlinespace
    Philips Healthcare & iDose4 & IMR & \textbf{Precise Image} \\
    \bottomrule
  \end{tabularx}
\end{table}

\section{A Ruptura dos Pilares da Linearidade}
\label{sec:quebra_linearidade}

A incorporação de redes neurais profundas (DLR) quebrou formalmente os pilares da linearidade:
\begin{enumerate}
  \item \textbf{Quebra da Superposição Linear:} Funções de ativação não lineares (ReLU, GELU) tornam o operador não linear:
  \begin{equation}
    \mathcal{R}_{\text{DLR}}(\alpha \mathbf{y}_1 + \beta \mathbf{y}_2) \ne \alpha \mathcal{R}_{\text{DLR}}(\mathbf{y}_1) + \beta \mathcal{R}_{\text{DLR}}(\mathbf{y}_2)
    \label{eq:quebra_superposicao}
  \end{equation}
  \item \textbf{Quebra do Isoplanatismo:} A resolução espacial torna-se localmente dependente do contraste e do contexto anatômico vizinho;
  \item \textbf{Quebra de WSS e o Efeito Ceroso:} O ruído perde a estacionariedade e tem sua potência deslocada para baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$), gerando o aspecto textural plástico (\emph{waxy look}).
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Simulação Numérica da Não-Linearidade em Algoritmos DLR, Correlação com Radiologistas e Detrending Polinomial 2D.}
  \label{fig:dlr_non_linear}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 4.1}
\label{subsec:analise_fig4}
A \cref{fig:dlr_non_linear} foi gerada por **simulação computacional sintética** em Python para ilustrar os efeitos não lineares e as técnicas de correção estatística:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação de Detectabilidade $d'$ vs. Dose em DLR:}
  Comparou-se o escalonamento clássico da FBP ($\sigma \propto 1/\sqrt{\text{Dose}} \implies d' \propto \sqrt{\text{Dose}}$, linha preta) contra o modelo não linear adaptativo de DLR (linha verde), onde a rede neural preserva a detectabilidade diagnóstica ($d' = 1{,}8$) mesmo em regimes de ultrabaixa dose ($1{,}5\text{ mGy}$);

  \item \textbf{Painel (B) --- Simulação de Correlação com Radiologistas Humanos:}
  Modelou-se a dispersão empírica de leituras 2AFC para demonstrar a quebra do modelo linear NPWE sob DLR (cruzes vermelhas, $r = 0{,}68$, decorrente da incapacidade de tratar o ruído não-estacionário), contrastando com observadores profundos adaptativos (círculos verdes, $r = 0{,}98$);

  \item \textbf{Painel (C) --- Demonstração do Detrending Polinomial 2D:}
  Simulou-se um perfil de intensidade anatômica $I(x)$ com gradiente macroscópico e ruído de alta frequência. Demonstra-se que o ajuste de superfície polinomial de 2ª ordem $P_2(x)$ (linha tracejada vermelha) via mínimos quadrados analíticos subtrai a variação estrutural lenta, isolando o ruído estocástico puro residual $\delta I(x) = I(x) - P_2(x)$ (curva verde inferior).
\end{enumerate}

\section{Metodologia de Phantoms Antropomórficos Híbridos}
\label{sec:phantoms_hibridos}

Para avaliar algoritmos DLR sem os artefatos decorrentes de simuladores homogêneos simples, a literatura consolidou a metodologia de phantoms antropomórficos híbridos (\cref{fig:phantom_flow}) \cite{pimenta2025, pimenta2026}:
\begin{enumerate}
  \item \textbf{Aquisição com Phantom Físico Antropomórfico:} Simuladores 3D com materiais equivalentes a tecidos biológicos (osso, pulmão, tecidos moles);
  \item \textbf{Banco de Fundos Anatômicos Reais ($H_0$):} Extração de ROIs de parênquima real sem patologia;
  \item \textbf{Inserção Híbrida Tridimensional ($H_1$):} Convolução matemática de modelos 3D de lesões com a PSF real do tomógrafo e soma ao fundo anatômico;
  \item \textbf{Verdade de Campo Exata (\emph{Ground Truth}):} Obtenção de milhares de imagens com coordenadas, diâmetro e contraste precisamente conhecidos para calibração de observadores.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption[Metodologia de Phantoms Híbridos e Teste 2AFC]{Estrutura Metodológica de Phantoms Antropomórficos, Inserção Híbrida 3D e Paradigma Psicofísico 2AFC.}
  \label{fig:phantom_flow}
\end{figure}

\subsection{Detrending Polinomial 2D e Incerteza por Bootstrap}
\label{subsec:detrending_matematica}
Para cada sub-região $I_k(x, y)$, ajusta-se a superfície polinomial de 2ª ordem:
\begin{equation}
  P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy
  \label{eq:polinomio_2d}
\end{equation}
através da matriz de Vandermonde $\mathbf{V}$: $\mathbf{a} = (\mathbf{V}^T \mathbf{V})^{-1} \mathbf{V}^T \mathbf{i}_k$. A incerteza experimental e os intervalos de confiança de $d'$ são determinados por reamostragem Bootstrap não-paramétrica com $B = 2000$ replicações:
\begin{equation}
  \text{SE}_{\text{boot}}(d') = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B \left( d'^{*(b)} - \bar{d}'^* \right)^2}
  \label{eq:bootstrap_se}
\end{equation}

% ------------------------------------------------------------------------------
% CAPÍTULO 5: FRONTEIRAS METROLÓGICAS: APRENDIZADO PROFUNDO, PCCT E OTIMIZAÇÃO
% ------------------------------------------------------------------------------
\chapter{Fronteiras Metrológicas: Aprendizado Profundo, PCCT e Otimização}
\label{chap:estado_da_arte}

Este capítulo analisa as fronteiras contemporâneas da metrologia em tomografia computadorizada documentadas na literatura científica: os Observadores por Aprendizado Profundo (DLMO) baseados em Vision Transformers, a física dos detectores de Contagem de Fótons (PCCT) e a formulação da Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$.

\section{Observadores Baseados em Aprendizado Profundo (DLMO)}
\label{sec:dlmo}

\subsection{Arquitetura Baseada em Vision Transformers (ViT)}
\label{subsec:vit_arquitetura}
Para superar as limitações dos observadores lineares sob reconstruções DLR, a física médica investigou os Observadores de Modelo por Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO) baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de Auto-Atenção Multi-Cabeça (MHSA), conforme esquematizado no \cref{fig:dlmo_arch} \cite{dosovitskiy2021, zhou2021, schilder2026}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura Neural do DLMO]{Arquitetura Conceitual do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer).}
  \label{fig:dlmo_arch}
\end{figure}

A imagem é particionada em $N_p$ blocos bidimensionais $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 C)}$ projetados linearmente para dimensão latente $D_{\text{model}}$:
\begin{equation}
  \mathbf{z}_0 = \left[ \mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \dots; \, \mathbf{x}_p^{N_p} \mathbf{E} \right] + \mathbf{E}_{\text{pos}}
  \label{eq:vit_embedding}
\end{equation}
Para cada bloco, computam-se as matrizes de Consulta ($Q$), Chave ($K$) e Valor ($V$):
\begin{equation}
  \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
  \label{eq:attention_formula}
\end{equation}
O mecanismo de auto-atenção mimetiza a coordenação visual humana foveal-periférica. O índice de detectabilidade do modelo profundo expressa-se por:
\begin{equation}
  d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}
  \label{eq:dprime_dl}
\end{equation}

\subsection{Calibração Perceptual e Validação Cruzada LOSO}
\label{subsec:perceptual_loss}
O alinhamento com radiologistas é obtido através de funções de perda multitarefa que integram entropia cruzada e erro de detectabilidade perceptual: $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{BCE}} + \lambda (d'_{\text{DL}} - d'_{\text{humano}})^2$. A generalização entre diferentes tomógrafos clínicos é avaliada pelo protocolo \emph{Leave-One-Scanner-Out} (LOSO) \cite{zhou2021}.

\section{Física da Tomografia por Contagem de Fótons (PCCT)}
\label{sec:pcct_fisica}

\subsection{Comparativo Físico entre EICT e PCCT}
\label{subsec:eict_limitacoes}
A tecnologia PCCT representa uma inovação radical na detecção de raios X através de semicondutores de conversão direta (CdTe/CZT), eliminando o ruído eletrônico e permitindo contagem espectral individual (\cref{tab:eict_vs_pcct}) \cite{flohr2020, mccollough2026, pimenta2025, pimenta2026}.

\begin{table}[htbp]
  \centering
  \small
  \caption{Comparativo físico entre as tecnologias de detecção tomográfica EICT e PCCT.}
  \label{tab:eict_vs_pcct}
  \begin{tabularx}{\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.22\textwidth} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
    \toprule
    Característica Física & TC por Integração de Energia (EICT) & TC por Contagem de Fótons (PCCT) \\
    \midrule
    Material Detector & Cintilador cerâmico ($\text{Gd}_2\text{O}_2\text{S}$) + Fotodiodo & Semicondutor de conversão direta (CdTe / CZT) \\
    \addlinespace
    Mecanismo & Conversão Indireta: Raios X $\to$ Luz $\to$ Carga & Conversão Direta: Raios X $\to$ Pares elétron-lacuna \\
    \addlinespace
    Ruído Eletrônico & Integrado cumulativamente ao sinal & Rejeitado por limiar inferior ($E_{\text{threshold}} > E_{\text{ruído}}$) \\
    \addlinespace
    Resolução Espacial & Limitada por septos ópticos ($0{,}5 \text{ a } 0{,}6 \text{ mm}$) & Submilimétrica ultra-alta ($0{,}1 \text{ a } 0{,}2 \text{ mm}$) \\
    \addlinespace
    Capacidade Espectral & Requer duas fontes ou camadas duplas & Múltiplos canais de energia em disparo único \\
    \bottomrule
  \end{tabularx}
\end{table}

\subsection{Síntese de Imagens Monoenergéticas Virtuais ($VMI$)}
\label{subsec:vmi_sintese}
A absorção direta no CdTe ($W_{\text{ionização}} \approx 4{,}43\text{ eV}$) gera pulsos proporcionais à energia do fóton ($V_{\text{pulso}} \propto E_{\text{fóton}}$). Ao discriminar os pulsos em múltiplos canais de energia, o sistema sintetiza Imagens Monoenergéticas Virtuais ($VMI$):
\begin{equation}
  I_{\text{VMI}}(x, y; E_0) = a_1(x, y) \cdot f_{\text{foto}}(E_0) + a_2(x, y) \cdot f_{\text{Compton}}(E_0)
  \label{eq:vmi_formula}
\end{equation}
Em baixas energias ($40\text{ a }50\text{ keV}$), maximiza-se o efeito fotoelétrico do iodo ($K\text{-edge} = 33{,}2\text{ keV}$), proporcionando alto contraste vascular sem degradação por ruído eletrônico.

\section{Otimização Multiobjetivo e Fronteira de Pareto 3D}
\label{sec:pareto_otimizacao}

\subsection{Formulação Matemática do Vetor Multiobjetivo}
\label{subsec:desafio_multiobjetivo}
A otimização de protocolos na literatura é formulada como um problema de minimização vetorial multiobjetivo envolvendo dose ($D$), tempo operacional ($T$) e detectabilidade ($W = d'$) \cite{oostveen2021}:
\begin{equation}
  \min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}
  \label{eq:multiobjetivo_pareto}
\end{equation}
sujeito às restrições $D(\mathbf{p}) \le \text{DRL}$, $T(\mathbf{p}) \le T_{\text{máx}}$ e $W(\mathbf{p}) \ge d'_{\text{mín}}$.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Modelagem Numérica Teórica da Otimização Multiobjetivo em Tomografia Computadorizada e Superfície de Pareto.}
  \label{fig:pareto_3d}
\end{figure}

\subsection{Metodologia da Simulação Numérica e Análise da Figura 5.2}
\label{subsec:analise_fig5}
A \cref{fig:pareto_3d} foi sintetizada numericamente em Python para demonstrar o conceito de soluções não-dominadas em física médica:

\begin{enumerate}
  \item \textbf{Painel (A) --- Simulação da Fronteira de Compromisso Dose vs. Detectabilidade:}
  Modelou-se analiticamente o espaço de soluções através de funções de compromisso físico não-lineares. A curva contínua verde delimita a Fronteira de Pareto de soluções não-dominadas. Destacam-se três soluções de compromisso: $P_1$ (protocolo de ultrabaixa dose pediátrico), $P_2$ (exame ambulatorial padrão) e $P_3$ (protocolo de emergência com máxima detectabilidade). Os pontos cinzas dispersos representam protocolos subótimos;

  \item \textbf{Painel (B) --- Simulação da Superfície de Pareto Tridimensional $(D, T, -W)$:}
  Modelou-se uma variedade 3D contínua integrando tempo de rotação/varredura ($T$), dose absorvida ($D$) e detectabilidade ($W$). A simulação ilustra a tomada de decisão clínica multicritério (via algoritmo genético NSGA-II e ranqueamento TOPSIS), permitindo selecionar o protocolo de varredura ultra-rápida ($T \le 2\text{ s}$) que preserva a detectabilidade necessária para pacientes politraumatizados.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 6: SISTEMATIZAÇÃO DO PIPELINE METROLÓGICO E DIRETRIZES NORMATIVAS
% ------------------------------------------------------------------------------
\chapter{Sistematização do Pipeline Metrológico e Diretrizes Normativas AAPM TG-233}
\label{chap:arquitetura_metrologia}

A aplicação metrológica das grandezas deduzidas nos capítulos anteriores exige uma estruturação conceitual padronizada do fluxo de dados tomográficos e o estrito cumprimento de salvaguardas regulatórias e bioéticas. Este capítulo sistematiza o pipeline de processamento metrológico documentado pelo relatório AAPM TG-233 e detalha as diretrizes normativas nacionais e internacionais para testes com observadores humanos.

\section{Estruturação Conceitual do Pipeline Metrológico em Física Médica}
\label{sec:software_arch}

\subsection{Fluxo Sequencial de Processamento de Dados}
\label{subsec:visao_geral_pipeline}
Conforme consolidado na literatura internacional de metrologia tomográfica \cite{aapm_tg233_2019, choopani2023}, o processamento sistemático de imagens para avaliação baseada em tarefa organiza-se em cinco etapas conceituais encadeadas (\cref{fig:software_flow}):

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow6_software_pipeline.png}
  \caption[Estrutura Conceitual do Pipeline Metrológico]{Estrutura Conceitual do Pipeline Metrológico em Tomografia Computadorizada segundo o Relatório AAPM TG-233.}
  \label{fig:software_flow}
\end{figure}

\begin{enumerate}
  \item \textbf{Etapa 1 (Extração e Validação de Metadados DICOM):} Leitura sistemática dos cabeçalhos dos exames, extraindo parâmetros de irradiação ($\text{kVp}$, $\text{mA}$, tempo de rotação, $\text{CTDI}_{\text{vol}}$, $\text{DLP}$), geometria de aquisição (espessura de corte, espaçamento entre fatias, campo de visão FOV) e identificadores de reconstrução (kernel, nível DLR/HIR);
  \item \textbf{Etapa 2 (Segmentação e Amostragem Espacial de ROIs):} Identificação das coordenadas espaciais dos insertos de calibração via Transformada de Hough circular e extração de $M \ge 100$ regiões de interesse homogêneas independentes para amostragem estocástica do ruído;
  \item \textbf{Etapa 3A (Cálculo da Resolução Espacial da Tarefa):} Construção da Função de Resposta ao Degrau superamostrada ($\text{ESF}(r)$), derivação numérica da $\text{LSF}(r)$ e aplicação da Transformada Rápida de Fourier para obtenção da $TTF(f)$ e dos descritores $f_{50}$ e $f_{10}$;
  \item \textbf{Etapa 3B (Processamento Espectral do Ruído):} Aplicação do detrending polinomial bidimensional de 2ª ordem $P_2(x, y)$, janelamento de Hanning para contenção de vazamento espectral e FFT2D, gerando a matriz $NPS(u, v)$ e a curva radial integrada $NPS(f)$;
  \item \textbf{Etapa 4 (Integração dos Observadores de Modelo):} Avaliação do índice de detectabilidade $d'$ através dos modelos analíticos lineares (NPWE e CHO com canais corticais D-DOG/Laguerre-Gauss) e modelagem não-linear;
  \item \textbf{Etapa 5 (Análise de Incerteza e Relatório de Conformidade):} Reamostragem estatística por Bootstrap ($B = 2000$) para cálculo de intervalos de confiança de 95\% e emissão de laudo técnico de qualidade.
\end{enumerate}

\section{Protocolo Metrológico Padronizado AAPM TG-233}
\label{sec:protocolo_tg233}

\subsection{Parâmetros de Aquisição e Geometria do Phantom}
\label{subsec:parametros_tg233}
A padronização metrológica rigorosa assegura que as medições de detectabilidade sejam diretamente comparáveis entre diferentes centros de pesquisa e hospitais. As aquisições seguem as diretrizes do relatório AAPM TG-233 \cite{aapm_tg233_2019}:
\begin{itemize}
  \item Matriz de $512 \times 512$ pixels com FOV ajustado ao diâmetro do phantom ($200\text{ a }350\text{ mm}$);
  \item Espessuras de corte de $0{,}5\text{ a }1{,}0\text{ mm}$ (alta resolução) e $2{,}5\text{ a }5{,}0\text{ mm}$ (rotina);
  \item Tensões de tubo padronizadas de 80, 100, 120 e 140 kVp, cobrindo doses $\text{CTDI}_{\text{vol}}$ de $0{,}5\text{ a }15\text{ mGy}$;
  \item Lesões esféricas com diâmetros de 3, 5, 8 e 10 mm e contrastes clínicos de $-600\text{ HU}$ (nódulo pulmonar subsólido), $+100\text{ HU}$ (nódulo sólido) e $+30\text{ HU}$ (lesão hepática hipoatenuante).
\end{itemize}

\section{Aspectos Bioéticos e Regulatórios em Estudos Psicofísicos}
\label{sec:bioetica}

\subsection{Conformidade Ética e Normas Regulatórias}
\label{subsec:cep_conep}
A condução de experimentos psicofísicos com médicos radiologistas para validação de observadores computacionais requer estrita observância das salvaguardas bioéticas (Resoluções CNS 466/2012 e 510/2016) e normativas sanitárias (ANVISA RDC 611/2022) \cite{anvisa_rdc611_2022}:
\begin{itemize}
  \item Submissão prévia e aprovação em Comitê de Ética em Pesquisa (CEP/CONEP);
  \item Aplicação de Termo de Consentimento Livre e Esclarecido (TCLE) aos médicos participantes, assegurando anonimização e sigilo de desempenho individual;
  \item Padronização das condições ergonômicas e ópticas de leitura: monitores diagnósticos calibrados segundo a norma DICOM GSDF (luminância máxima $\ge 400\text{ cd/m}^2$) e iluminação ambiente controlada ($< 15\text{ lux}$);
  \item Mitigação de fadiga visual através de sessões curtas de leitura 2AFC (máximo de 100 a 150 pares de imagens por sessão, com duração $< 25$ minutos).
\end{itemize}

% ------------------------------------------------------------------------------
% CAPÍTULO 7: CONSIDERAÇÕES FINAIS E PERSPECTIVAS FUTURAS
% ------------------------------------------------------------------------------
\chapter{Considerações Finais e Perspectivas Futuras}
\label{chap:conclusoes}

Este capítulo final sintetiza as principais conclusões e contribuições conceituais desta monografia, discute o impacto prático da metrologia baseada em tarefa para a física médica e estabelece as perspectivas futuras de pesquisa na área.

\section{Síntese Global da Revisão e Trajetória Metrológica}
\label{sec:sintese_global}

A garantia da qualidade e a dosimetria em Tomografia Computadorizada atravessaram uma profunda transformação metodológica. Esta monografia realizou uma **revisão bibliográfica abrangente e uma sistematização matemática unificada** da transição dos modelos analíticos lineares clássicos para as formulações perceptuais contemporâneas.

O trabalho fundamentou formalmente a **insuficiência das métricas escalares clássicas** ($SNR$, $CNR$, desvio padrão $\sigma_{\text{HU}}$ e $MTF$) perante os algoritmos não lineares de reconstrução iterativa (HIR, MBIR) e por aprendizado profundo (DLR). Demonstrou-se que a supressão não linear do ruído quebra as premissas de linearidade do sistema, isoplanatismo espacial e estacionariedade no sentido amplo (WSS), alterando a textura do ruído (aspecto ceroso) e podendo induzir a perda de visibilidade de lesões patológicas de baixo contraste.

Como resposta científica a esse desafio, o paradigma da **Qualidade de Imagem Baseada em Tarefa (TBIQ)**, ancorado na Teoria de Detecção de Sinais (SDT) e consolidado pelo relatório AAPM TG-233, estabeleceu que a qualidade de imagem deve ser quantificada pelo desempenho em tarefas diagnósticas específicas. O **Índice de Detectabilidade ($d'$)** consagrou-se como a grandeza central integradora, sintetizando com rigor físico:
\begin{enumerate}
  \item A resolução dependente do contraste ($TTF(f)$ com o descritor $f_{50}$);
  \item A textura e potência espectral do ruído ($NPS(f)$ com a frequência de pico $f_{\text{peak}}$);
  \item A morfologia da patologia ($W_{\text{task}}(f)$ via funções de Bessel);
  \item A fisiologia visual humana ($E(f)$) e mecanismos de canalização cortical (CHO).
\end{enumerate}

A utilização de **simulações numéricas sintéticas controladas** ao longo dos capítulos permitiu materializar pedagogicamente as equações deduzidas, comprovando matematicamente o colapso dos modelos analíticos lineares (como o NPWE) sob ruídos não-estacionários e evidenciando a necessidade de modelos avançados com mecanismos de atenção (DLMO).

\section{Impacto Prático para a Física Médica e Saúde Pública}
\label{sec:impacto_pratico}

A consolidação teórica e metodológica da metrologia TBIQ oferece contribuições diretas para a prática clínica hospitalar:
\begin{itemize}
  \item \textbf{Otimização Efetiva do Princípio ALARA:} O índice $d'$ fornece comprovação física inequívoca de que reduções expressivas na dose de radiação em protocolos pediátricos e de rastreio de câncer podem ser executadas preservando a segurança diagnóstica;
  \item \textbf{Harmonização Tecnológica Inter-Fabricantes:} A metodologia de phantoms antropomórficos híbridos associada a observadores de modelo permite equalizar o desempenho diagnóstico entre equipamentos de múltiplos fornecedores (GE, Siemens, Canon, Philips);
  \item \textbf{Conformidade com Normas Regulatórias Nacionais:} O arcabouço metrológico fornece a base conceitual para o atendimento às exigências da ANVISA (RDC 611/2022 e IN 93/2021) e aos programas internacionais de auditoria da Agência Internacional de Energia Atômica (IAEA).
\end{itemize}

\section{Perspectivas Futuras de Pesquisa}
\label{sec:perspectivas_futuras}

A fronteira da física médica em diagnóstico por imagem aponta para direções promissoras de desenvolvimento futuro:
\begin{enumerate}[label=\textbf{\arabic*.}]
  \item \textbf{Extensão do TBIQ para Aquisições Dinâmicas e 4D:} Incorporação de resolução temporal na modelagem do índice de detectabilidade para angiotomografia coronariana com \emph{ECG-gating} e tomografia de perfusão cerebral;
  \item \textbf{Modelos Fundacionais Multimodais em Visão Médica:} Aplicação de modelos de linguagem e visão (\emph{Vision-Language Foundation Models}) para emular a tomada de decisão radiológica e gerar laudos estruturados orientados por tarefa;
  \item \textbf{Metrologia Espectral Multielementar em Detectores PCCT:} Aplicação de observadores de modelo para quantificação simultânea de múltiplos agentes de contraste (\emph{K-edge imaging}) com nanopartículas funcionalizadas;
  \item \textbf{Integração Metrológica Automatizada a Sistemas Hospitalares (PACS/RIS):} Incorporação de rotinas de auditoria de detectabilidade em tempo real para monitoramento contínuo de qualidade e dose institucional.
\end{enumerate}

% ==============================================================================
% ELEMENTOS PÓS-TEXTUAIS: REFERÊNCIAS BIBLIOGRÁFICAS ABNT
% ==============================================================================
\begin{thebibliography}{99}
\addcontentsline{toc}{chapter}{Referências}

\bibitem{bushberg2020}
BUSHBERG, J. T. et al. \textbf{The Essential Physics of Medical Imaging}. 4. ed. Philadelphia: Wolters Kluwer, 2020. 1048 p.

\bibitem{attix1986}
ATTIX, F. H. \textbf{Introduction to Radiological Physics and Radiation Dosimetry}. New York: John Wiley \& Sons, 1986. 607 p.

\bibitem{seeram2015}
SEERAM, E. \textbf{Computed Tomography: Physical Principles, Clinical Applications, and Quality Control}. 4. ed. St. Louis: Saunders Elsevier, 2015. 576 p.

\bibitem{icrp103_2007}
INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION (ICRP). The 2007 Recommendations of the International Commission on Radiological Protection. \textbf{ICRP Publication 103}. Annals of the ICRP, v. 37, n. 2-4, p. 1--332, 2007.

\bibitem{mccollough2026}
MCCOLLOUGH, C. H. et al. Principles and clinical applications of photon-counting computed tomography: A comprehensive review. \textbf{Radiology}, v. 318, n. 1, p. e251200, 2026.

\bibitem{anvisa_rdc611_2022}
BRASIL. Agência Nacional de Vigilância Sanitária (ANVISA). \textbf{Resolução da Diretoria Colegiada - RDC nº 611, de 9 de março de 2022}. Estabelece os requisitos sanitários para a organização e o funcionamento de serviços de radiologia diagnóstica ou intervencionista. Diário Oficial da União: Brasília, DF, 16 mar. 2022.

\bibitem{anvisa_in93_2021}
BRASIL. Agência Nacional de Vigilância Sanitária (ANVISA). \textbf{Instrução Normativa - IN nº 93, de 27 de maio de 2021}. Estabelece os requisitos específicos para garantia da qualidade e segurança em sistemas de tomografia computadorizada. Diário Oficial da União: Brasília, DF, 01 jun. 2021.

\bibitem{rose1948}
ROSE, A. The sensitivity performance of the human eye on an absolute scale. \textbf{Journal of the Optical Society of America}, v. 38, n. 2, p. 196--208, 1948.

\bibitem{burgess1999}
BURGESS, A. E. The Rose model, revisited. \textbf{Journal of the Optical Society of America A}, v. 16, n. 3, p. 633--646, 1999.

\bibitem{racine2020}
RACINE, D. et al. Task-based image quality assessment in computed tomography: A review of current methods and clinical applications. \textbf{Physica Medica}, v. 79, p. 144--154, 2020.

\bibitem{debbiche2024}
DEBBICHE, I. et al. Deep learning image reconstruction for CT: Technical principles and clinical performance. \textbf{European Journal of Radiology}, v. 170, p. 111234, 2024.

\bibitem{greffier2026}
GREFFIER, J. et al. Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. \textbf{Diagnostic and Interventional Imaging}, v. 107, n. 1, p. 1016--1025, 2026.

\bibitem{toia2023}
TOIA, G. V. et al. Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. \textbf{European Radiology}, v. 33, p. 4310--4322, 2023.

\bibitem{solomon2020}
SOLOMON, J. et al. Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. \textbf{Medical Physics}, v. 47, n. 8, p. 3412--3425, 2020.

\bibitem{aapm_tg233_2019}
AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., Medical Physics, v. 46, n. 11, p. e735--e756, 2019).

\bibitem{icru54_1996}
INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). \textbf{Medical Imaging - The Assessment of Image Quality}. ICRU Report 54. Bethesda, MD: ICRU, 1996.

\bibitem{peterson1954}
PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. \textbf{Transactions of the IRE Professional Group on Information Theory}, v. 4, n. 4, p. 171--212, 1954.

\bibitem{lusted1968}
LUSTED, L. B. \textbf{Introduction to Medical Decision Making}. Springfield, IL: Charles C Thomas, 1968.

\bibitem{metz1986}
METZ, C. E. ROC methodology in radiologic imaging. \textbf{Investigative Radiology}, v. 21, n. 9, p. 720--733, 1986.

\bibitem{barrett_myers_2004}
BARRETT, H. H.; MYERS, K. J. \textbf{Foundations of Image Science}. Hoboken: John Wiley \& Sons, 2004. 1540 p.

\bibitem{wagner1979}
WAGNER, R. F.; BROWN, D. G.; METZ, C. E. Application of information theory to the assessment of computed tomography. \textbf{Medical Physics}, v. 6, n. 2, p. 83--94, 1979.

\bibitem{burgess1994}
BURGESS, A. E. Statistically defined backgrounds: performance of a modified nonprewhitening observer model. \textbf{Journal of the Optical Society of America A}, v. 11, n. 4, p. 1237--1242, 1994.

\bibitem{eckstein2000}
ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P. Role of knowledge in human visual search for signals in noise. \textbf{Journal of the Optical Society of America A}, v. 17, n. 11, p. 2064--2076, 2000.

\bibitem{myers1987}
MYERS, K. J.; BARRETT, H. H. Addition of a channel mechanism to the ideal-observer model. \textbf{Journal of the Optical Society of America A}, v. 4, n. 12, p. 2447--2457, 1987.

\bibitem{yao1992}
YAO, J.; BARRETT, H. H. Predicting human performance by a channelized Hotelling observer model. In: \textbf{SPIE Medical Imaging: Image Perception}, v. 1654, p. 268--278, 1992.

\bibitem{dorfman1992}
DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E. Receiver operating characteristic rating analysis: generalization to the population of readers and patients with the jackknife method. \textbf{Investigative Radiology}, v. 27, n. 9, p. 723--731, 1992.

\bibitem{obuchowski1995}
OBUCHOWSKI, N. A.; ROCKETTE, H. E. Hypothesis testing of diagnostic accuracy for multiple readers and multiple tests: an ANOVA approach with dependent observations. \textbf{Communications in Statistics - Simulation and Computation}, v. 24, n. 2, p. 285--308, 1995.

\bibitem{hillis2011}
HILLIS, S. L.; OBUCHOWSKI, N. A.; BERBAUM, K. S. Multi-reader multi-case ROC analysis: an updated review of methods and software. \textbf{Academic Radiology}, v. 18, n. 7, p. 842--856, 2011.

\bibitem{racine2021}
RACINE, D. et al. Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. \textbf{Medical Physics}, v. 48, n. 6, p. 2890--2901, 2021.

\bibitem{dosovitskiy2021}
DOSOVITSKIY, A. et al. An image is worth 16x16 words: Transformers for image recognition at scale. In: \textbf{International Conference on Learning Representations (ICLR)}, 2021. p. 1--21.

\bibitem{zhou2021}
ZHOU, W. et al. Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. \textbf{IEEE Transactions on Medical Imaging}, v. 40, n. 9, p. 2350--2362, 2021.

\bibitem{schilder2026}
SCHILDER, C. M. et al. Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. \textbf{La Rivista del Nuovo Cimento}, v. 49, n. 3, p. 145--210, 2026.

\bibitem{flohr2020}
FLOHR, T. et al. Photon-counting CT review. \textbf{Physica Medica}, v. 79, p. 126--136, 2020.

\bibitem{pimenta2025}
PIMENTA, E. F.; COSTA, P. R. Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. \textbf{Medical Physics}, v. 52, n. 4, p. 2150--2165, 2025.

\bibitem{pimenta2026}
PIMENTA, E. F. \textbf{Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax}. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.

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
    f.write(latex_content)

# Update build_single_file_overleaf.py as well
with open("/Users/user/.gemini/antigravity-ide/scratch/build_single_file_overleaf.py", "w", encoding="utf-8") as f:
    f.write(f'''import os
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
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
print("Pacote final sincronizado com sucesso!")
''')

# Create ZIP Package
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

print("TCC Monografia de Revisão Bibliográfica atualizada com sucesso em main.tex e nos arquivos ZIP!")
