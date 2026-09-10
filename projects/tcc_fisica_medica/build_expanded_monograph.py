import os
import re
import zipfile
import shutil

output_dir = "/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile"
fig_dir = os.path.join(output_dir, "figuras")
os.makedirs(fig_dir, exist_ok=True)

# Build the complete enriched monolithic text
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

% Informações Institucionais (Conforme especificações do usuário)
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

A Tomografia Computadorizada (TC) desempenha papel indispensável na medicina diagnóstica moderna, operando sob o permanente compromisso físico entre a minimização da dose de radiação ionizante e a preservação do desempenho diagnóstico (princípio ALARA). Historicamente, a metrologia e a garantia da qualidade em TC apoiaram-se em grandezas físicas escalares e lineares, como a Relação Sinal-Ruído (SNR), a Relação Contraste-Ruído (CNR) e a Função de Transferência de Modulação (MTF), avaliadas em simuladores geométricos homogêneos. No entanto, a incorporação clínica de algoritmos avançados não lineares --- com destaque para as reconstruções iterativas estatísticas e, fundamentalmente, as reconstruções baseadas em aprendizado profundo (\emph{Deep Learning Image Reconstruction} --- DLR) --- quebrou as premissas de linearidade e invariância translacional do sistema formador de imagens. Sob processamentos não lineares, o ruído tomográfico tornou-se espacialmente heterogêneo, dependente da dose, do contraste e da geometria local da imagem, induzindo alterações texturais perceptuais, como a textura cerosa ou \emph{plastic/waxy look} que não são capturadas pelas métricas clássicas. Para superar essa limitação, a física médica consolidou o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ), ancorado na Teoria de Detecção de Sinais (\emph{Signal Detection Theory} --- SDT), no qual a qualidade da imagem é formalmente definida pelo desempenho de um observador (humano ou computacional) na execução de uma tarefa diagnóstica clínica específica, quantificada pelo Índice de Detectabilidade ($d'$). Este trabalho apresenta uma investigação exaustiva e estruturada da evolução dos observadores de modelo (\emph{model observers}). Analisa-se a transição histórica do Observador Ideal Bayesiano para os modelos lineares antropomórficos com filtro ocular (NPWE) e canais corticais de frequência (CHO), demonstrando suas deduções matemáticas contínuas no domínio de Fourier e evidenciando os limites biofísicos que causam seu colapso sob reconstruções DLR e fundos anatômicos complexos. Em resposta, investiga-se a fronteira científica representada pelos Observadores Baseados em Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), baseados em arquiteturas \emph{Vision Transformers} (ViT) com mecanismos de auto-atenção multi-cabeça, calibrados diretamente contra leituras psicofísicas de radiologistas em experimentos de Escolha Forçada entre Duas Alternativas (2AFC) sob análise estatística \emph{Multi-Reader Multi-Case} (MRMC). Detalham-se a física dos detectores de contagem de fótons (PCCT), a síntese de Imagens Monoenergéticas Virtuais ($VMI$) e a formulação da Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, que integra dose de radiação ($D$), tempo operacional total ($T$) e detectabilidade ($W$). Esta monografia consolida as bases teóricas, biofísicas e metrológicas que sustentam a pesquisa de Doutorado Direto do autor no InRad-HCFMUSP.

\vspace{0.8cm}
\noindent\textbf{Palavras-chave:} Tomografia Computadorizada. Qualidade de Imagem Baseada em Tarefa. Observadores de Modelo. Índice de Detectabilidade. Reconstrução por Aprendizado Profundo. Vision Transformers. Tomografia por Contagem de Fótons. Simuladores Antropomórficos. Otimização Multiobjetivo. Fronteira de Pareto.
\clearpage

% 5. ABSTRACT
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving diagnostic efficacy (the ALARA principle). Historically, image quality assurance in CT relied on linear scalar metrics, such as Signal-to-Noise Ratio (SNR), Contrast-to-Noise Ratio (CNR), and Modulation Transfer Function (MTF), evaluated on homogeneous geometric phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms---including iterative reconstructions and Deep Learning Image Reconstruction (DLR)---has broken the foundational assumptions of system linearity and shift-invariance. Under non-linear processing, image noise becomes spatially non-stationary, dose-dependent, and scene-dependent, introducing perceptual texture alterations (such as the ``plastic'' or ``waxy'' appearance) that cannot be properly captured by conventional scalar metrics. To overcome this metrological limitation, medical physics has consolidated the Task-Based Image Quality (TBIQ) paradigm, grounded in Signal Detection Theory (SDT), where image quality is rigorously defined by the performance of an observer (human radiologist or mathematical model) executing a specific clinical task, quantified by the Detectability Index ($d'$). This monograph provides a comprehensive investigation of the evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer to anthropomorphic linear models incorporating eye filters (NPWE) and cortical frequency channels (CHO), detailing their continuous mathematical derivations in the Fourier domain and demonstrating their breakdown in non-linear DLR regimes and structured anatomical backgrounds. In response, we investigate the state of the art in Deep Learning Model Observers (DLMO), which leverage self-attention neural architectures (Vision Transformers) calibrated against expert radiologists' psychophysical performance in Two-Alternative Forced Choice (2AFC) paradigms under Multi-Reader Multi-Case (MRMC) statistical modeling. Furthermore, we explore the physics of Photon-Counting CT (PCCT), the synthesis of Virtual Monoenergetic Images (VMI), and the formulation of Multi-Objective Optimization via the Three-Dimensional Pareto Frontier $(D, T, -W)$, which integrates radiation dose ($D$), operational time ($T$), and diagnostic detectability ($W$). This study establishes the theoretical, computational, and physical foundation required for next-generation CT metrology, directly supporting the author's Direct Doctorate research at InRad-HCFMUSP.

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
\textbf{OR} & Obuchowski-Rockette \\
\textbf{PACS} & \emph{Picture Archiving and Communication System} \\
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
\setcounter{page}{31}

% ------------------------------------------------------------------------------
% CAPÍTULO 1: INTRODUÇÃO, CONTEXTUALIZAÇÃO E OBJETIVOS
% ------------------------------------------------------------------------------
\chapter{Introdução, Contextualização e Objetivos}
\label{chap:introducao}

A Tomografia Computadorizada (TC) transformou a prática médica global ao permitir a visualização volumétrica do corpo humano com alta resolução anatômica e temporal. Contudo, a evolução dos equipamentos tomográficos nas últimas décadas estabeleceu um cenário complexo: o uso intensivo de radiação ionizante para exames de rotina e a substituição dos métodos clássicos de reconstrução por algoritmos não lineares de inteligência artificial. Este capítulo contextualiza a importância da metrologia da qualidade de imagem em física médica, introduz os conceitos físicos básicos da formação da imagem tomográfica, expõe a falha das métricas tradicionais e apresenta formalmente a proposta e os objetivos deste trabalho de conclusão de curso.

\section{Os dois lados da Tomografia Computadorizada}
\label{sec:paradoxo_tc}

\subsection{Contextualização e Relevância para o Tema}
Para compreender a necessidade de novos modelos perceptivos de qualidade de imagem, é fundamental analisar a física que rege a tomografia computadorizada e os riscos associados ao uso da radiação X em seres humanos.

\subsection{Fundamentos da Formação da Imagem em Tomografia Computadorizada}
A Tomografia Computadorizada baseia-se na medição da atenuação exponencial que um feixe colimado de raios X sofre ao atravessar os tecidos biológicos. De acordo com a Lei de Beer-Lambert-Bouguer, para um feixe monoenergético com intensidade inicial $I_0$, a intensidade transmitida $I$ ao longo de uma trajetória retilínea $L$ é expressa por:
\begin{equation}
  I = I_0 \exp\left( -\int_L \mu(x, y, z; E) \, dl \right)
  \label{eq:beer_lambert}
\end{equation}
onde $\mu(x, y, z; E)$ representa o coeficiente de atenuação linear do tecido na posição espacial $(x, y, z)$ para uma energia de fótons $E$, medido em $\text{cm}^{-1}$.

Ao rotacionar o conjunto tubo-detector ao redor do paciente, o tomógrafo adquire milhares de perfis de projeção angular (o sinograma, fundamentado na Transformada de Radon). O algoritmo clássico de Retroprojeção Filtrada (\emph{Filtered Backprojection} --- FBP) reconstrói a distribuição bidimensional de $\mu(x, y)$, aplicando um filtro de rampa no domínio de Fourier para cancelar o borramento intrínseco ($1/r$) da retroprojeção simples \cite{bushberg2020, seeram2015}.

Para uniformizar os valores independentemente do espectro de energia do feixe, os coeficientes lineares são normalizados em relação à atenuação da água pura, gerando os Números de CT na escala Hounsfield (HU):
\begin{equation}
  \text{Número CT (HU)} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{água}}}{\mu_{\text{água}}}
  \label{eq:escala_hounsfield}
\end{equation}
Nessa escala padronizada, o ar corresponde a $-1000\text{ HU}$, a água destilada a $0\text{ HU}$, o parênquima pulmonar a $-700\text{ HU}$, o tecido adiposo a $-100\text{ HU}$, tecidos moles a $+40\text{ HU}$ e o osso cortical denso varia de $+1000$ a $+3000\text{ HU}$.

\subsection{O Risco Radiológico e o Princípio ALARA}
Apesar de sua indispensável utilidade clínica, a radiação X é uma radiação ionizante capaz de romper ligações químicas e induzir danos estocásticos no DNA celular (efeitos carcinogênicos e mutagênicos sem limiar de dose, descritos pelo modelo linear sem limiar --- LNT) \cite{icrp103_2007, attix1986}. Estatísticas internacionais indicam que a TC responde por mais de 60\% da dose coletiva de radiação médica mundial, mesmo representando menos de 15\% do total de procedimentos radiológicos realizados \cite{mccollough2026, bushberg2020}.

Esse cenário impõe o permanente imperativo da radioproteção: o princípio ALARA (\emph{As Low As Reasonably Achievable} --- Tão Baixo Quanto Razoavelmente Exequível) e as regulamentações sanitárias nacionais brasileiras (ANVISA RDC 611/2022 e IN 93/2021) \cite{anvisa_rdc611_2022, anvisa_in93_2021}. A missão da física médica é reduzir a dose absorvida ao menor nível possível, garantindo simultaneamente que a imagem mantenha a qualidade diagnóstica necessária para a detecção de patologias sutis.

\subsection{Transição para a Próxima Seção}
Para cumprir o princípio ALARA, os físicos médicos necessitam de grandezas físicas precisas para medir se a qualidade da imagem foi preservada após uma redução de dose. No entanto, as grandezas escalares utilizadas nos últimos quarenta anos tornaram-se obsoletas frente aos tomógrafos modernos, conforme será demonstrado a seguir.

\section{A Insuficiência das Métricas Escalares Clássicas}
\label{sec:insuficiencia_metricas}

\subsection{Contextualização e Relevância para o Tema}
A garantia da qualidade em radiologia dependeu historicamente de parâmetros simples e globais. Nesta seção, investiga-se por que esses parâmetros falham drasticamente quando aplicados às tecnologias contemporâneas de inteligência artificial.

\subsection{As Grandezas Físicas Clássicas e suas Premissas}
Durante quatro décadas, a avaliação da qualidade em TC baseou-se em métricas escalares globais (\cref{fig:comparativo_paradigmas}):
\begin{itemize}
  \item \textbf{Relação Sinal-Ruído ($SNR$):} Razão entre a média do sinal e o desvio padrão do ruído em uma região homogênea ($SNR = \mu / \sigma$);
  \item \textbf{Relação Contraste-Ruído ($CNR$):} Diferença entre as médias de sinal de dois tecidos dividida pelo desvio padrão do fundo ($CNR = |\mu_{\text{alvo}} - \mu_{\text{fundo}}| / \sigma$);
  \item \textbf{Desvio padrão do número de CT ($\sigma_{\text{HU}}$):} Variância pontual dos números de CT em simuladores físicos uniformes de água ou acrílico;
  \item \textbf{Função de Transferência de Modulação global ($MTF$):} Medida da resolução espacial do sistema calculada a partir da resposta a fios finos ou esferas metálicas.
\end{itemize}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption[Comparativo Estrutural entre os Paradigmas Físicos]{Comparativo Estrutural entre o Paradigma Físico Clássico (Linear/Escalar) e o Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

Essas grandezas assumem premissas matemáticas muito restritivas:
\begin{enumerate}
  \item \textbf{Linearidade Estrita do Sistema:} O processamento de uma soma de sinais equivale à soma dos processamentos individuais ($f(a + b) = f(a) + f(b)$);
  \item \textbf{Invariância Espacial (Isoplanatismo):} A função de resposta ao ponto (PSF) é idêntica em qualquer coordenada da matriz de imagem;
  \item \textbf{Estacionariedade do Ruído no Sentido Amplo (WSS):} As propriedades estatísticas do ruído não dependem da posição nem do conteúdo da imagem circundante.
\end{enumerate}

\subsection{A Ruptura Metrológica das Reconstruções Avançadas}
Nos tomógrafos clínicos modernos, a retroprojeção filtrada linear foi gradualmente substituída por algoritmos de Reconstrução Iterativa Híbrida (HIR), Reconstrução Iterativa Baseada em Modelos (MBIR) e, mais recentemente, Reconstrução por Aprendizado Profundo (\emph{Deep Learning Image Reconstruction} --- DLR) \cite{racine2020, debbiche2024, greffier2026, greffier2023}.

Esses novos algoritmos são estritamente não lineares: aplicam suavização adaptativa em áreas homogêneas enquanto tentam preservar bordas de alto contraste. Como consequência:
\begin{itemize}
  \item O desvio padrão ($\sigma_{\text{HU}}$) diminui artificialmente, dando a falsa impressão de que a qualidade aumentou;
  \item O ruído ganha uma textura atípica cerosa (\emph{plastic/waxy look}), caracterizada pela perda de frequências médias e altas fundamentais para a percepção humana;
  \item Lesões patológicas sutis de baixo contraste (como metástases hepáticas iniciais) são borradas pelo algoritmo e desaparecem da imagem, mesmo apresentando excelentes valores numéricos de $SNR$ e $CNR$ \cite{toia2023, solomon2020}.
\end{itemize}

\subsection{Transição para a Próxima Seção}
Diante da falência das grandezas escalares clássicas para qualificar algoritmos não lineares, a física médica internacional desenvolveu uma nova metodologia científica fundamentada na tarefa clínica do médico, denominada Avaliação de Qualidade Baseada em Tarefa (TBIQ).

\section{O Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ)}
\label{sec:paradigma_tbiq}

\subsection{Contextualização e Relevância para o Tema}
Nesta seção, estabelece-se o alicerce conceitual do paradigma TBIQ, articulando como a física dos detectores, o processamento de sinais e a biologia da percepção visual integram-se em uma métrica objetiva única.

\subsection{Conceito e Pilares Fundamentais do TBIQ}
O paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ) foi formalmente consolidado pela Associação Americana de Físicos em Medicina através do Relatório AAPM TG-233 e pela Comissão Internacional de Unidades e Medições de Radiação no Relatório ICRU 54 \cite{aapm_tg233_2019, icru54_1996}.

Conforme esquematizado no \cref{fig:tbiq_paradigm}, a qualidade da imagem não é tratada como um valor abstrato, mas sim quantificada diretamente pelo desempenho de um observador (médico radiologista ou modelo computacional matemático) ao executar uma tarefa médica real.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow1_tbiq_paradigm.png}
  \caption[Pilares Fundamentais do Paradigma TBIQ]{Pilares Fundamentais do Paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ).}
  \label{fig:tbiq_paradigm}
\end{figure}

O paradigma TBIQ sustenta-se sobre quatro pilares biofísicos e matemáticos:
\begin{enumerate}
  \item \textbf{A Resolução Espacial Dependente da Tarefa ($TTF(f)$):} Mede a fidelidade na transferência de frequências espaciais em função do contraste específico da lesão clínica investigada;
  \item \textbf{A Textura e Magnitude do Ruído ($NPS(f)$):} Quantifica a potência do ruído distribuída no domínio de Fourier, descrevendo se o ruído é fino, granular ou ceroso;
  \item \textbf{O Espectro da Patologia Clínica ($W_{\text{task}}(f)$):} Descreve matematicamente a geometria, o tamanho e a densidade radiológica do alvo diagnóstico investigado;
  \item \textbf{O Sistema Visual e Perceptual do Observador ($E(f)$ ou Modelos Neurais):} Incorpora a sensibilidade ao contraste do olho humano ou as propriedades corticais de processamento de imagem na tomada de decisão diagnóstica.
\end{enumerate}

A união dessas quatro grandezas resulta no **Índice de Detectabilidade ($d'$)**, uma grandeza adimensional e universal que traduz com precisão estatística a probabilidade de um diagnóstico correto.

\subsection{Transição para a Próxima Seção}
Compreendidos os desafios da TC e a formulação conceitual do paradigma TBIQ, definem-se a seguir os objetivos gerais e específicos que estruturam a investigação desenvolvida nesta monografia.

\section{Objetivos da Monografia}
\label{sec:objetivos}

\subsection{Objetivo Geral}
Desenvolver uma formulação teórica, biofísica e computacional unificada dos modelos perceptivos de qualidade de imagem baseada em tarefa aplicados à tomografia computadorizada, estabelecendo as bases metrológicas para a otimização multiobjetivo de protocolos clínicos e suportando a pesquisa de Doutorado Direto do autor no InRad-HCFMUSP.

\subsection{Objetivos Específicos}
\begin{enumerate}
  \item Apresentar as deduções matemáticas fundamentais da Teoria de Detecção de Sinais (SDT), formalizando o Índice de Detectabilidade ($d'$), curvas ROC e experimentos 2AFC;
  \item Deduzir rigorosamente no domínio contínuo de Fourier as métricas da física médica moderna: Função de Transferência da Tarefa ($TTF(f)$), Espectro de Potência do Ruído ($NPS(f)$), Filtro Ocular de Sensibilidade ao Contraste ($E(f)$) e Espectro da Tarefa ($W_{\text{task}}(f)$);
  \item Analisar a evolução dos observadores de modelo lineares clássicos: Observador Ideal Bayesiano (IO), Observador Sem Pré-Branqueamento com Filtro Ocular (NPWE) e Observador de Hotelling Canalizado (CHO) com canais corticais D-DOG, Laguerre-Gauss e Gabor;
  \item Evidenciar as falhas metrológicas dos modelos analíticos lineares frente à quebra de linearidade em algoritmos DLR e fundos anatômicos complexos;
  \item Investigar a fronteira do conhecimento em Observadores por Aprendizado Profundo (DLMO) baseados em \emph{Vision Transformers} com mecanismos de auto-atenção multi-cabeça;
  \item Investigar os fundamentos biofísicos da Tomografia por Contagem de Fótons (PCCT) e a síntese de Imagens Monoenergéticas Virtuais ($VMI$);
  \item Formular matematicamente o problema de Otimização Multiobjetivo através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose ($D$), tempo operacional ($T$) e detectabilidade diagnóstica ($W$);
  \item Estruturar a arquitetura de software e o desenho experimental com validação psicofísica MRMC em radiologistas segundo as diretrizes éticas CEP/CONEP.
\end{enumerate}

% ------------------------------------------------------------------------------
% CAPÍTULO 2: FUNDAMENTOS BIOFÍSICOS E MATEMÁTICOS DA AVALIAÇÃO BASEADA EM TAREFA
% ------------------------------------------------------------------------------
\chapter{Fundamentos Biofísicos e Matemáticos da Avaliação Baseada em Tarefa}
\label{chap:fundamentos_sdt}

Para estabelecer uma metodologia científica rigorosa na avaliação da qualidade tomográfica, é indispensável construir o arcabouço matemático que conecta a física estatística das imagens médicas à tomada de decisão diagnóstica. Este capítulo aborda a Teoria de Detecção de Sinais (SDT), a definição formal do Índice de Detectabilidade ($d'$), a teoria das Curvas ROC, o protocolo psicofísico 2AFC e as deduções analíticas contínuas no domínio de Fourier da Função de Transferência da Tarefa ($TTF$), do Espectro de Potência do Ruído ($NPS$), do Filtro Ocular ($E(f)$) e do Espectro da Tarefa ($W_{\text{task}}$).

\section{Teoria Clássica de Detecção de Sinais (SDT)}
\label{sec:sdt_teoria}

\subsection{Contextualização e Relevância para o Tema}
A detecção de uma lesão patológica em um exame tomográfico ruidoso é, por definição física, um problema estocástico de detecção de sinal sob fundo ruidoso. A Teoria de Detecção de Sinais fornece a linguagem matemática necessária para modelar esse processo sem ambiguidades subjetivas.

\subsection{Formalismo Matemático do Teste Binário de Hipóteses}
A Teoria de Detecção de Sinais (SDT), introduzida na física matemática por Peterson, Birdsall e Fox (1954) e transposta para a radiologia médica por Lusted (1968) e Metz (1986), analisa o desempenho de tomada de decisão sob ruído estocástico \cite{peterson1954, lusted1968, metz1986}.

Considera-se o problema binário fundamental em que uma imagem discreta $\mathbf{g} \in \mathbb{R}^N$ (composta por $N$ pixels) pertence a uma de duas hipóteses mutuamente exclusivas:
\begin{align}
  H_0 &: \mathbf{g} = \mathbf{b} \quad (\text{Hipótese Nula: Sinal Ausente / Tecido Normal}) \label{eq:h0} \\
  H_1 &: \mathbf{g} = \mathbf{s} + \mathbf{b} \quad (\text{Hipótese Alternativa: Sinal Presente / Tecido com Lesão}) \label{eq:h1}
\end{align}
onde $\mathbf{s} \in \mathbb{R}^N$ representa o perfil determinístico do sinal de atenuação da lesão e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico de flutuações quânticas de ruído e textura anatômica com vetor média zero e matriz de autocovariância $\mathbf{K}_{\mathbf{b}} = \langle \mathbf{b} \mathbf{b}^T \rangle$.

Um observador qualquer processa o vetor de dados brutos $\mathbf{g}$ através de um funcional escalar contínuo $t = t(\mathbf{g})$. A decisão diagnóstica final é obtida pela comparação de $t$ com um limiar de corte $t_c$:
\begin{equation}
  \text{Decisão} = \begin{cases}
    H_1 (\text{Positivo para Lesão}), & \text{se } t(\mathbf{g}) \ge t_c \\
    H_0 (\text{Negativo para Lesão}), & \text{se } t(\mathbf{g}) < t_c
  \end{cases}
  \label{eq:criterio_decisao}
\end{equation}

A \cref{fig:sdt_roc_2afc} ilustra o comportamento das funções de densidade de probabilidade de decisão $p(t|H_0)$ e $p(t|H_1)$, a família de curvas ROC geradas pela variação de $t_c$ e a correspondência com a proporção de acertos no paradigma 2AFC.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig1_sdt_roc_2afc.png}
  \caption[Distribuições da SDT, Curvas ROC e Desempenho 2AFC]{Teoria de Detecção de Sinais (SDT), Análise ROC e Paradigma 2AFC. (A) Distribuições de probabilidade da variável escalar de decisão sob as hipóteses $H_0$ e $H_1$, com o limiar de corte $t_c$ e áreas de sensibilidade (TPF) e falso positivo (FPF). (B) Família de Curvas Características de Operação do Receptor (ROC) para diferentes valores de $d'$. (C) Relação analítica entre a proporção de acertos $P_C$ no teste 2AFC e o índice de detectabilidade $d'$.}
  \label{fig:sdt_roc_2afc}
\end{figure}

\subsection{Transição para a Próxima Seção}
A separabilidade entre as duas distribuições de probabilidade $p(t|H_0)$ e $p(t|H_1)$ determina o grau de facilidade com que o observador acerta o diagnóstico. Essa separabilidade é quantificada formalmente pelo Índice de Detectabilidade ($d'$), deduzido a seguir.

\section{Definição Formal do Índice de Detectabilidade (\texorpdfstring{$d'$}{d-prime})}
\label{sec:dprime_definicao}

\subsection{Contextualização e Relevância para o Tema}
O índice $d'$ é a grandeza escalar mestra do paradigma TBIQ. Compreender sua derivação estatística permite comparar diretamente algoritmos tomográficos, níveis de dose e observadores humanos sob a mesma métrica física.

\subsection{Dedução Estatística do \texorpdfstring{$d'$}{d-prime}}
O Índice de Detectabilidade ($d'$, pronunciado \emph{d-prime}) quantifica a distância estatística normalizada entre os valores médios da estatística de teste sob as duas hipóteses, ponderada pela variância das distribuições \cite{barrett_myers_2004}:
\begin{equation}
  d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}
  \label{eq:dprime_geral}
\end{equation}
onde $\langle t | H_i \rangle$ denota o valor esperado condicional de $t$ sob a hipótese $H_i$, e $\sigma^2(t|H_i) = \langle (t - \langle t | H_i \rangle)^2 | H_i \rangle$ representa a variância estocástica correspondente.

Sob as premissas de ruído aditivo estacionário com variâncias iguais sob ambas as hipóteses ($\sigma^2(t|H_1) = \sigma^2(t|H_0) = \sigma_t^2$), a expressão simplifica-se para a clássica formulação de Signal-to-Noise Ratio generalizada:
\begin{equation}
  d' = \frac{\mu_1 - \mu_0}{\sigma_t}
  \label{eq:dprime_gaussiano}
\end{equation}
onde $\mu_1 = \langle t | H_1 \rangle$ e $\mu_0 = \langle t | H_0 \rangle$.

Quanto maior o valor de $d'$, menor a sobreposição entre as distribuições $p(t|H_0)$ e $p(t|H_1)$, resultando em maior taxa de diagnósticos corretos e menor taxa de erros médicos (falsos positivos e falsos negativos).

\subsection{Transição para a Próxima Seção}
Embora o índice $d'$ seja uma grandeza matemática teórica, na prática clínica é necessário medi-lo através do comportamento de observadores humanos. Isso é realizado conectando $d'$ às curvas ROC e aos testes psicofísicos 2AFC.

\section{Curva ROC, AUC e o Paradigma Experimental 2AFC}
\label{sec:roc_2afc}

\subsection{Contextualização e Relevância para o Tema}
A avaliação clínica de radiologistas depende da caracterização do equilíbrio entre sensibilidade e especificidade. Esta seção demonstra como a física médica traduz experimentos psicofísicos cegos em valores exatos de $d'$.

\subsection{Formulações da Análise ROC e do Paradigma 2AFC}
Ao variar o limiar de decisão $t_c$ em todo o eixo real ($-\infty < t_c < +\infty$), definem-se a Fração de Falsos Positivos ($FPF$) e a Fração de Verdadeiros Positivos ($TPF$ ou Sensibilidade):
\begin{align}
  FPF(t_c) &= \int_{t_c}^{\infty} p(t|H_0) \, dt = 1 - \Phi\left( \frac{t_c - \mu_0}{\sigma_0} \right) \label{eq:fpf} \\
  TPF(t_c) &= \int_{t_c}^{\infty} p(t|H_1) \, dt = 1 - \Phi\left( \frac{t_c - \mu_1}{\sigma_1} \right) \label{eq:tpf}
\end{align}
onde $\Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-u^2/2} du$ é a função de distribuição cumulativa da variável normal padrão.

A Curva ROC (\emph{Receiver Operating Characteristic}) é a trajetória paramétrica traçada no plano $(FPF, TPF)$. A Área sob a Curva ROC ($AUC$) é uma medida clássica de acurácia diagnóstica independente do limiar subjetivo adotado pelo radiologista \cite{metz1986}:
\begin{equation}
  AUC = \int_0^1 TPF(FPF) \, d(FPF) = \Phi\left( \frac{d'}{\sqrt{2}} \right)
  \label{eq:auc_formula}
\end{equation}

No experimento psicofísico de Escolha Forçada entre Duas Alternativas (\emph{Two-Alternative Forced Choice} --- 2AFC), são exibidas simultaneamente duas imagens ao observador: uma imagem de controle contendo apenas ruído de fundo ($H_0$) e uma imagem contendo o sinal patológico adicionado ao fundo ($H_1$). O observador deve escolher obrigatoriamente qual das duas imagens contém a lesão.

Green e Swets (1966) e Burgess (1999) demonstraram que a proporção empírica de acertos $P_C$ em um número elevado de pares 2AFC é matematicamente idêntica à $AUC$ de um teste ROC de leitura única \cite{burgess1999}:
\begin{equation}
  P_C = AUC = \Phi\left( \frac{d'}{\sqrt{2}} \right)
  \label{eq:pc_2afc}
\end{equation}

Essa identidade fundamental permite estimar experimentalmente o índice de detectabilidade perceptual de leitores humanos ($d'_{\text{humano}}$) através da função quantil (inversa de $\Phi$):
\begin{equation}
  d'_{\text{humano}} = \sqrt{2} \, \Phi^{-1}(P_C)
  \label{eq:dprime_from_pc}
\end{equation}
Por exemplo, uma taxa de acerto de $P_C = 84{,}1\%$ corresponde a $d' \approx 1{,}41$; $P_C = 92{,}1\%$ corresponde a $d' \approx 2{,}00$; e $P_C = 99{,}8\%$ atinge o Critério de Rose ($d' \ge 4{,}00$).

\subsection{Transição para a Próxima Seção}
Estabelecida a ponte entre a estatística de decisão e a percepção humana, o próximo passo consiste em deduzir analiticamente como a física do tomógrafo, o ruído e o alvo diagnóstico se manifestam no domínio contínuo de Fourier.

\section{Dedução Contínua das Métricas no Domínio de Fourier}
\label{sec:metricas_fourier}

\subsection{Contextualização e Relevância para o Tema}
O espaço das frequências espaciais $\mathbf{f} = (u, v)$ permite isolar os efeitos de resolução óptica, textura de ruído e sensibilidade visual em funções contínuas tratáveis analiticamente, conforme preconizado pelo relatório internacional AAPM TG-233.

\subsection{As Quatro Funções Espectrais Fundamentais}
A \cref{fig:spectral_metrics} apresenta a caracterização das quatro métricas no domínio espectral de Fourier.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig2_spectral_metrics.png}
  \caption[Métricas Espectrais Contínuas em Frequência]{Métricas Espectrais Contínuas no Domínio de Fourier segundo o Relatório AAPM TG-233. (A) Função de Transferência da Tarefa $TTF(f)$ para insertos de diferentes contrastes. (B) Espectro de Potência do Ruído $NPS(f)$ para retroprojeção filtrada (FBP), reconstrução iterativa (HIR), inteligência artificial (DLR) e modelos físicos (MBIR). (C) Filtro Ocular Humano de Sensibilidade ao Contraste $E(f)$. (D) Espectro da Tarefa Diagnóstica $W_{\text{task}}(f)$ para nódulos esféricos de diferentes diâmetros.}
  \label{fig:spectral_metrics}
\end{figure}

\subsubsection{1. Função de Transferência da Tarefa (\texorpdfstring{$TTF(f)$}{TTF(f)})}
A $TTF(f)$ quantifica a resolução espacial do tomógrafo de forma dependente do contraste local do objeto. Em simuladores de controle de qualidade (como o módulo de baixo contraste do Catphan\textregistered\ ou insertos do phantom antropomórfico), utiliza-se a técnica da borda circular de insertos cilíndricos com raio $R_0$ \cite{aapm_tg233_2019, racine2020}:
\begin{enumerate}
  \item Calcula-se a distância euclidiana radial de cada pixel em relação ao baricentro do inserto cilíndrico: $r_i = \sqrt{(x_i - x_c)^2 + (y_i - y_c)^2}$;
  \item Constrói-se a Função de Resposta ao Degrau superamostrada ($\text{ESF}(r)$) por agrupamento radial com sub-espaçamento de pixel;
  \item Diferencia-se a $\text{ESF}(r)$ para obter a Função de Espalhamento de Linha radial: $\text{LSF}(r) = -\frac{d}{dr}\text{ESF}(r)$;
  \item Aplica-se a Transformada de Fourier unidimensional e normaliza-se na frequência zero ($f = 0$):
  \begin{equation}
    TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, e^{-2\pi i f r} \, dr \right|}{\int_{-\infty}^{\infty} \text{LSF}(r) \, dr}
    \label{eq:ttf_formula}
  \end{equation}
\end{enumerate}
Os descritores $f_{50}$ e $f_{10}$ indicam as frequências espaciais nas quais a modulação decai para 50\% e 10\% do valor inicial, respectivamente.

\subsubsection{2. Espectro de Potência do Ruído (\texorpdfstring{$NPS(f)$}{NPS(f)})}
O $NPS(u, v)$ mede a distribuição espectral da variância do ruído tomográfico em $\text{HU}^2\cdot\text{mm}^2$. A partir de $M$ sub-regiões de interesse (ROIs) homogêneas de dimensão $N_x \times N_y$ pixels com amostragem $\Delta x, \Delta y$:
\begin{equation}
  NPS(u, v) = \frac{\Delta x \Delta y}{M \cdot N_x N_y} \sum_{k=1}^M \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \delta I_k(x, y) \, e^{-2\pi i (ux + vy)} \right|^2
  \label{eq:nps_2d}
\end{equation}
onde $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é o ruído purificado após a subtração de uma superfície polinomial de 2ª ordem $P_2(x, y)$ (\emph{detrending}).

O espectro radial unidimensional $NPS(f)$ é obtido pela integração azimutal:
\begin{equation}
  NPS(f) = \frac{1}{2\pi} \int_0^{2\pi} NPS(f\cos\theta, f\sin\theta) \, d\theta
  \label{eq:nps_radial}
\end{equation}
A frequência de pico $f_{\text{peak}} = \arg\max NPS(f)$ define a granularidade textural da imagem.

\subsubsection{3. Filtro Ocular Humano (\texorpdfstring{$E(f)$}{E(f)})}
O sistema visual humano atua como um filtro passa-faixa sintonizado pela Função de Sensibilidade ao Contraste (\emph{Contrast Sensitivity Function} --- CSF), descrita pelo modelo de Burgess (1999) \cite{burgess1999}:
\begin{equation}
  E(f) = \left( \frac{f_{\text{retina}}}{f_0} \right)^n \exp\left[ -c \left( \frac{f_{\text{retina}}}{f_0} \right)^m \right]
  \label{eq:filtro_ocular}
\end{equation}
com parâmetros empíricos calibrados: $f_0 = 0{,}8\text{ cpd}$, $n = 1{,}3$, $m = 1{,}1$ e $c = 2{,}2$. A conversão para frequências espaciais retinianas em ciclos por grau ($f_{\text{retina}}$) sob distância de visualização médica $d_{\text{v}} \approx 500\text{ mm}$ é dada por $f_{\text{retina}} = \frac{\pi d_{\text{v}}}{180} f$. O olho humano atinge sua sensibilidade máxima em torno de $4\text{ a }5\text{ cpd}$, atenuando tanto frequências extremamente baixas quanto ruídos de altíssima frequência.

\subsubsection{4. Espectro da Tarefa Diagnóstica (\texorpdfstring{$W_{\text{task}}(f)$}{W\_task(f)})}
Para um nódulo esférico ou lesão circular de raio físico $R$ e contraste central uniforme $\Delta C$ em relação ao tecido vizinho, o perfil espacial bidimensional corresponde a uma função degrau circular $\Delta C \cdot \Pi(r / 2R)$. A Transformada de Fourier em coordenadas polares resulta na função de Bessel de primeira espécie e ordem 1 ($J_1(x)$):
\begin{equation}
  W_{\text{task}}(f) = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|
  \label{eq:wtask_formula}
\end{equation}
Lesões volumosas concentram sua energia em frequências muito baixas, enquanto microcalcificações e bordas finas exigem altas frequências espaciais.

\subsection{Transição para o Próximo Capítulo}
Com as quatro funções fundamentais ($TTF$, $NPS$, $E(f)$ e $W_{\text{task}}$) formalizadas matematicamente, o próximo capítulo explora como a física médica combinou esses componentes na formulação analítica dos Observadores de Modelo Lineares (IO, NPWE e CHO) e sua validação com leitores humanos via modelos ANOVA MRMC.

% ------------------------------------------------------------------------------
% CAPÍTULO 3: A EVOLUÇÃO DOS OBSERVADORES DE MODELO LINEARES E VALIDAÇÃO PSICOFÍSICA MRMC
% ------------------------------------------------------------------------------
\chapter{A Evolução dos Observadores de Modelo Lineares e Validação Psicofísica MRMC}
\label{chap:observadores_lineares}

Os observadores de modelo são algoritmos matemáticos projetados para emular ou superar o desempenho de leitores humanos na execução de tarefas de detecção diagnóstica. Este capítulo apresenta a trajetória histórica dos observadores lineares clássicos: partindo do limite físico absoluto do Observador Ideal Bayesiano e do Observador de Hotelling, passando pelo modelo biofísico antropomórfico NPWE e culminando no Observador de Hotelling Canalizado (CHO) com canais corticais de frequência. Por fim, detalha-se o modelo estatístico de ANOVA Multi-Reader Multi-Case (MRMC) para a validação psicofísica desses modelos contra painéis de médicos radiologistas.

\section{O Observador Ideal Bayesiano e o Observador de Hotelling}
\label{sec:observador_ideal}

\subsection{Contextualização e Relevância para o Tema}
Para julgar a eficiência de qualquer equipamento tomográfico, é necessário estabelecer o teto teórico absoluto de informação diagnóstica contido nos fótons de raios X. O Observador Ideal Bayesiano define esse limite superior fundamental imposto pelas leis da física.

\subsection{Dedução Matemática do Observador de Hotelling}
O Observador Ideal (IO) fundamenta-se na razão de verossimilhança de Bayes $\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$. Quando o ruído quântico de fundo segue uma distribuição gaussiana multivariada com matriz de covariância $\mathbf{K}$, a razão de verossimilhança logarítmica reduz-se a uma operação estritamente linear, denominada Observador de Hotelling (HO) \cite{barrett_myers_2004, wagner1979}:
\begin{equation}
  t_{\text{HO}}(\mathbf{g}) = \mathbf{w}_{\text{HO}}^T \mathbf{g} = \left( \mathbf{K}^{-1} \mathbf{s} \right)^T \mathbf{g} = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}
  \label{eq:template_hotelling}
\end{equation}
onde o vetor de pesos $\mathbf{w}_{\text{HO}} = \mathbf{K}^{-1} \mathbf{s}$ atua como um template ótimo que realiza o pré-branqueamento (\emph{prewhitening}) do ruído através da matriz inversa $\mathbf{K}^{-1}$, descorrelacionando os pixels antes de integrá-los com o perfil do sinal $\mathbf{s}$.

O índice de detectabilidade máximo atingível pelo Observador de Hotelling é dado pela forma quadrática:
\begin{equation}
  d'_{\text{HO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}}
  \label{eq:dprime_hotelling}
\end{equation}
Nenhum observador biológico ou computacional pode superar $d'_{\text{HO}}$, tornando-o o padrão-ouro teórico para avaliação de sistemas de aquisição e eficiência quântica de detecção ($DQE$).

\subsection{Transição para a Próxima Seção}
Embora o Observador de Hotelling seja ótimo do ponto de vista matemático, o cérebro humano não realiza a inversão matricial do ruído $\mathbf{K}^{-1}$. Para modelar com fidelidade o comportamento de radiologistas humanos em imagens homogêneas, a física médica formulou o modelo Sem Pré-Branqueamento com Filtro Ocular (NPWE).

\section{O Observador NPW e a Dedução Contínua do Modelo NPWE}
\label{sec:npwe_deducao}

\subsection{Contextualização e Relevância para o Tema}
O modelo NPWE é a formulação analítica mais amplamente utilizada em controle de qualidade de rotina em tomografia computadorizada. Esta seção deduz sua integral contínua no domínio de Fourier e expõe suas premissas biofísicas.

\subsection{Dedução da Integral Contínua do Modelo NPWE}
Em tarefas de detecção com fundo uniforme, o observador humano atua correlacionando visualmente a imagem diretamente com a forma esperada da lesão, sem capacidade neural de descorrelacionar o ruído com $\mathbf{K}^{-1}$. Esse comportamento é modelado pelo Observador Sem Pré-Branqueamento (\emph{Non-Prewhitening} --- NPW), cujo template é o próprio sinal determinístico: $\mathbf{w}_{\text{NPW}} = \mathbf{s}$ \cite{burgess1994}.

Para reproduzir as limitações do olho humano, Burgess (1994) e Eckstein et al. (2000) introduziram o filtro ocular $E(f)$ e uma componente de ruído neural interno $\sigma_{\text{int}}^2$, originando o modelo antropomórfico NPWE (\emph{Non-Prewhitening with Eye Filter}) \cite{burgess1994, eckstein2000}.

No domínio contínuo de Fourier, o sinal percebido no plano de visualização após a transferência do tomógrafo e do filtro ocular é $S_{\text{percebido}}(f) = TTF(f) \cdot W_{\text{task}}(f) \cdot E(f)$. A variância do ruído integrado pelo template ocular é $\sigma_t^2 = \int NPS(f) [TTF(f)]^2 [W_{\text{task}}(f)]^2 [E(f)]^4 f \, df + \sigma_{\text{int}}^2$.

A substituição dessas grandezas na definição de $d'$ resulta na integral contínua do NPWE:
\begin{equation}
  d'_{\text{NPWE}} = \frac{\displaystyle \int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^2 f \, df}{\displaystyle \sqrt{\int_0^{\infty} \left[ TTF(f) \right]^2 \left[ W_{\text{task}}(f) \right]^2 \left[ E(f) \right]^4 NPS(f) f \, df + \sigma_{\text{int}}^2}}
  \label{eq:dprime_npwe_integral}
\end{equation}

Essa equação elegante sintetiza em uma única integral unidimensional toda a biofísica da detecção de lesões em simuladores homogêneos de TC.

\subsection{Transição para a Próxima Seção}
Embora o modelo NPWE funcione com excelente precisão em simuladores cilíndricos uniformes, ele colapsa quando aplicado a fundos anatômicos reais com estruturas heterogêneas (como vasos pulmonares e osso trabecular). Para superar essa limitação, a física médica introduziu o conceito de canais corticais de frequência no Observador de Hotelling Canalizado (CHO).

\section{O Observador de Hotelling Canalizado (CHO)}
\label{sec:cho_teoria}

\subsection{Contextualização e Relevância para o Tema}
Na prática clínica, as patologias nunca ocorrem em fundos uniformes de água, mas sim imersas em complexas anatomias estruturadas. O modelo CHO representa o ápice dos observadores lineares clássicos ao incorporar os mecanismos neurofisiológicos da área V1 do córtex visual humano.

\subsection{Pipeline Matemático e Redução Dimensional por Canais Corticais}
Em imagens clínicas com matriz $N = 128 \times 128 = 16.384$ pixels, a matriz de covariância anatômica $\mathbf{K}_{\mathbf{b}} \in \mathbb{R}^{N \times N}$ possui mais de 268 milhões de elementos. Estimar e inverter numericamente essa matriz exige um número proibitivo de amostras tomográficas ($M > 10^5$), gerando ruído de amostragem inaceitável \cite{barrett1993, myers1987}.

Para solucionar esse problema, Myers e Barrett (1987) e Yao e Barrett (1992) propuseram a introdução de uma matriz de operadores de canais corticais $\mathbf{T} \in \mathbb{R}^{C \times N}$, onde o número de canais $C$ é muito menor que $N$ (tipicamente $C = 4$ a $15$) \cite{myers1987, yao1992}.

O pipeline completo do CHO está esquematizado no \cref{fig:cho_flow}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow3_cho_pipeline.png}
  \caption[Pipeline Computacional do Observador CHO]{Pipeline Computacional do Observador de Hotelling Canalizado (CHO).}
  \label{fig:cho_flow}
\end{figure}

O vetor de imagem $\mathbf{g}$ é projetado no subespaço dos canais, gerando o vetor reduzido $\mathbf{v} \in \mathbb{R}^C$:
\begin{equation}
  \mathbf{v} = \mathbf{T} \mathbf{g}
  \label{eq:vetor_canais}
\end{equation}

A matriz de covariância reduzida dos canais $\mathbf{K}_{\mathbf{v}} \in \mathbb{R}^{C \times C}$ é de pequeníssima dimensão (ex: $5 \times 5$), sendo estimada de forma extremamente estável:
\begin{equation}
  \mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K}_{\mathbf{b}} \mathbf{T}^T = \frac{1}{2} \left[ \text{Cov}(\mathbf{v}|H_0) + \text{Cov}(\mathbf{v}|H_1) \right]
  \label{eq:covariancia_canais}
\end{equation}

O vetor de decisão ótimo no subespaço dos canais é $\mathbf{w}_{\mathbf{v}} = \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle$, onde $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \mathbf{s}$, e o índice de detectabilidade do CHO é:
\begin{equation}
  d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}
  \label{eq:dprime_cho}
\end{equation}

\subsection{Famílias de Canais Corticais}
A \cref{fig:cho_channels} apresenta as principais famílias de canais corticais utilizadas na física médica:
\begin{enumerate}
  \item \textbf{Canais D-DOG (\emph{Dense Difference of Gaussians}):} Filtros concêntricos passa-faixa isotrópicos que emulam campos receptivos corticais circulares:
  \begin{equation}
    C_j(f) = \exp\left( -\frac{f^2}{2\sigma_j^2} \right) - \exp\left( -\frac{f^2}{2(\alpha \sigma_j)^2} \right)
    \label{eq:ddog}
  \end{equation}
  \item \textbf{Canais de Laguerre-Gauss (LG):} Base ortogonal radial com funções de Laguerre, ideal para sinais com simetria rotacional:
  \begin{equation}
    LG_n(r; a_u) = \frac{\sqrt{2}}{a_u} \exp\left( -\frac{\pi r^2}{a_u^2} \right) L_n\left( \frac{2\pi r^2}{a_u^2} \right)
    \label{eq:laguerre_gauss}
  \end{equation}
  \item \textbf{Canais de Gabor Orientados:} Modelam simultaneamente a frequência radial e a seletividade angular de orientação $\theta_k$ de campos receptivos simples em V1 \cite{abbey2001}.
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig3_cho_cortical_channels.png}
  \caption[Canais Corticais do CHO e Detectabilidade vs Dose]{Canais Corticais do Observador CHO e Desempenho em Fundo Anatômico. (A) Resposta espectral dos canais passa-faixa D-DOG. (B) Perfis espaciais das funções ortogonais de Laguerre-Gauss. (C) Campo receptivo de Gabor 2D orientado a $45^\circ$. (D) Detectabilidade $d'$ em função da dose para o modelo CHO versus modelos sem canais.}
  \label{fig:cho_channels}
\end{figure}

\subsection{Transição para a Próxima Seção}
Para comprovar cientificamente que um modelo matemático (como o CHO ou NPWE) reflete com fidelidade o olho de médicos radiologistas, é obrigatório submeter os dados a uma análise estatística multivariada rigorosa que controle a variabilidade de múltiplos leitores e múltiplos casos clínicos (ANOVA MRMC).

\section{Metodologia Estatística Multi-Reader Multi-Case (MRMC)}
\label{sec:mrmc_teoria}

\subsection{Contextualização e Relevância para o Tema}
A avaliação de tecnologias médicas por humanos sofre com duas fontes gigantescas de variabilidade aleatória: diferentes médicos interpretam exames de forma distinta (variabilidade entre leitores), e diferentes pacientes apresentam anatomias variadas (variabilidade entre casos). A metodologia MRMC é a ferramenta estatística mandatória em estudos regulatórios da FDA e em publicações de alto impacto de física médica para validar observadores de modelo.

\subsection{Modelo de ANOVA com Efeitos Aleatórios Cruzados}
Adota-se o modelo estatístico de Análise de Variância (ANOVA) com efeitos aleatórios cruzados de Dorfman-Berbaum-Metz e Hillis-Obuchowski-Rockette (DBM/HOR) \cite{dorfman1992, obuchowski1995, hillis2011, racine2021}:
\begin{equation}
  y_{ijk} = \mu + \tau_i + R_j + C_k + (\tau R)_{ij} + (\tau C)_{ik} + (RC)_{jk} + \epsilon_{ijk}
  \label{eq:mrmc_anova}
\end{equation}
onde:
\begin{itemize}
  \item $y_{ijk}$ é a acurácia diagnóstica (ex: $AUC$ ou $d'$) medida para a modalidade tomográfica $i$, leitor $j$ e caso clínico $k$;
  \item $\mu$ é a média global da população de leitores e casos;
  \item $\tau_i$ é o efeito fixo da tecnologia de reconstrução ou nível de dose $i$;
  \item $R_j \sim \mathcal{N}(0, \sigma^2_R)$ é a variância aleatória entre os médicos radiologistas;
  \item $C_k \sim \mathcal{N}(0, \sigma^2_C)$ é a variância aleatória entre as imagens dos pacientes;
  \item $(\tau R)_{ij} \sim \mathcal{N}(0, \sigma^2_{\tau R})$ é a interação modalidade $\times$ leitor;
  \item $(\tau C)_{ik} \sim \mathcal{N}(0, \sigma^2_{\tau C})$ é a interação modalidade $\times$ caso;
  \item $(RC)_{jk} \sim \mathcal{N}(0, \sigma^2_{RC})$ é a interação leitor $\times$ caso;
  \item $\epsilon_{ijk} \sim \mathcal{N}(0, \sigma^2_{\epsilon})$ é o erro experimental aleatório residual.
\end{itemize}

\subsection{Graus de Liberdade de Satterthwaite e Coeficiente de Correlação Intraclasse}
O teste da hipótese nula de equivalência entre o modelo computacional e os radiologistas humanos ($H_0: \tau_{\text{modelo}} = \tau_{\text{humanos}}$) utiliza a estatística $F$ com graus de liberdade ajustados de Satterthwaite ($df_{\text{den}}$) para lidar com a dependência correlacionada dos leitores que avaliam os mesmos casos:
\begin{equation}
  F = \frac{MS(\tau)}{MS(\tau R) + MS(\tau C) - MS(\tau RC)} \sim F(df_{\text{num}}, df_{\text{den}})
  \label{eq:satterthwaite}
\end{equation}

Exige-se que o Coeficiente de Correlação Intraclasse ($ICC$) atinja $ICC \ge 0{,}90$ com intervalo de confiança de 95\% para que o modelo computacional seja aceito como substituto metrológico confiável da avaliação humana.

\subsection{Transição para o Próximo Capítulo}
Com a consolidação dos observadores lineares clássicos e de sua validação psicofísica MRMC, o próximo capítulo investiga o fenômeno que desafiou a física médica na última década: o colapso dos modelos analíticos lineares frente à quebra de linearidade provocada pelos algoritmos de Reconstrução por Aprendizado Profundo (DLR).

% ------------------------------------------------------------------------------
% CAPÍTULO 4: O COLAPSO DA LINEARIDADE, ALGORITMOS DLR E SIMULADORES HÍBRIDOS
% ------------------------------------------------------------------------------
\chapter{O Colapso da Linearidade, Algoritmos DLR e Simuladores Híbridos}
\label{chap:colapso_linearidade}

A incorporação em larga escala de redes neurais convolucionais profundas diretamente nos tomógrafos clínicos comerciais (DLR) produziu uma ruptura paradigmática na formação de imagens médicas. Este capítulo analisa a taxonomia física dos algoritmos comerciais de reconstrução, demonstra as causas matemáticas do colapso dos modelos lineares, descreve o efeito ceroso e apresenta a metodologia experimental de Phantoms Antropomórficos Híbridos e Detrending Polinomial 2D.

\section{Taxonomia e Comparativo Físico dos Algoritmos de Reconstrução}
\label{sec:taxonomia_dlr}

\subsection{Contextualização e Relevância para o Tema}
Cada fabricante global de tomógrafos adotou uma arquitetura e filosofia de rede neural distinta para reduzir ruído e dose. Compreender essas diferenças é essencial para formular um método de avaliação de qualidade que seja independente de fornecedor (*vendor-neutral*).

\subsection{As Quatro Gerações de Algoritmos de Reconstrução}
A evolução dos algoritmos tomográficos compreende quatro etapas históricas fundamentais:
\begin{enumerate}
  \item \textbf{1ª Geração --- Retroprojeção Filtrada (FBP):} Algoritmo analítico linear exato baseado na inversão da Transformada de Radon. Preserva textura clássica em formato de rampa ($NPS(f) \propto f$), mas exige doses elevadas de radiação para evitar ruído excessivo;
  \item \textbf{2ª Geração --- Reconstrução Iterativa Híbrida (HIR):} Aplica laços iterativos estatísticos entre o espaço de projeções brutas e a imagem reconstruída (ex: ASiR, AIDR 3D, SAFIRE, iDose4), permitindo reduções de 20\% a 40\% na dose;
  \item \textbf{3ª Geração --- Reconstrução Baseada em Modelos Físicos (MBIR):} Modela a geometria óptica do ponto focal do tubo, o espalhamento de raios X e a resposta dos detectores (ex: Veo, FIRST, IMR), permitindo reduções de até 70\% de dose, porém com altíssimo custo computacional e alteração na textura do ruído;
  \item \textbf{4ª Geração --- Reconstrução por Aprendizado Profundo (DLR):} Redes neurais convolucionais profundas (CNNs) com conexões residuais treinadas para mapear projeções de baixa dose diretamente em imagens de altíssima qualidade instantaneamente \cite{greffier2026, debbiche2024}.
\end{enumerate}

A \cref{tab:taxonomia_algoritmos} sintetiza os algoritmos comerciais implementados pelos quatro principais fabricantes globais de tomógrafos.

\begin{table}[htbp]
  \centering
  \small
  \caption{Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante.}
  \label{tab:taxonomia_algoritmos}
  \begin{tabularx}{\textwidth}{>{\bfseries\raggedright\arraybackslash}p{0.18\textwidth} >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X}
    \toprule
    Fabricante & Reconstrução Iterativa Híbrida (HIR) & Reconstrução Iterativa Baseada em Modelos (MBIR) & Reconstrução por Aprendizado Profundo (DLR) \\
    \midrule
    GE Healthcare & ASiR / ASiR-V & Veo & \textbf{TrueFidelity} (treinado com FBP de dose plena) \\
    \addlinespace
    Canon Medical & AIDR 3D / AIDR 3D Enhanced & FIRST & \textbf{AiCE} (\emph{Advanced intelligent Clear-IQ Engine}) \\
    \addlinespace
    Siemens Healthineers & SAFIRE / ADMIRE & REDUCE & \textbf{Precise Image} / \textbf{Alpha Engine} (PCCT) \\
    \addlinespace
    Philips Healthcare & iDose4 & IMR (\emph{Iterative Model Reconstruction}) & \textbf{Precise Image} (redes convolucionais profundas) \\
    \bottomrule
  \end{tabularx}
\end{table}

\subsection{Filosofias de Treinamento por Fabricante}
\begin{itemize}
  \item \textbf{GE Healthcare (TrueFidelity):} Adota uma filosofia de preservação textural estrita. Seu treinamento supervisionado utilizou como alvo (\emph{ground truth}) imagens de FBP em dose plena, ensinando a rede a remover o ruído sem alterar o formato clássico de rampa do $NPS(f)$;
  \item \textbf{Canon Medical (AiCE):} Utiliza como alvo imagens reconstruídas por MBIR (FIRST). A rede aprende a maximizar a resolução de bordas em alto contraste e suprime intensamente o ruído em partes moles;
  \item \textbf{Siemens Healthineers (Precise Image e Alpha Engine):} Aplica regularização adaptativa nos domínios de sinograma e imagem simultaneamente, atuando com destaque na preservação de resolução em sistemas PCCT;
  \item \textbf{Philips Healthcare (Precise Image):} Emprega redes residuais multi-escala operando em cascata para suprimir artefatos de feixe endurecido.
\end{itemize}

\subsection{Transição para a Próxima Seção}
Embora essas arquiteturas profundas produzam imagens visualmente atraentes com baixíssimo desvio padrão de HU, a natureza não linear dessas redes introduz efeitos físicos adversos que causam o colapso dos modelos metrológicos clássicos.

\section{A Quebra da Linearidade, Não-Estacionariedade e o Efeito Ceroso}
\label{sec:quebra_linearidade}

\subsection{Contextualização e Relevância para o Tema}
Nesta seção, analisa-se a fundamentação matemática que explica por que os modelos analíticos (como o NPWE) falham sob DLR e como a textura cerosa impacta negativamente o trabalho diagnóstico dos radiologistas.

\subsection{Mecanismos Físicos e Matemáticos da Não-Linearidade}
Em algoritmos DLR, a relação funcional que mapeia os dados brutos de sinograma $\mathbf{y}$ na imagem final $\mathbf{x}$ é estritamente não linear, operando através de camadas convolucionais combinadas com funções de ativação não lineares (como ReLU ou LeakyReLU) \cite{greffier2026, debbiche2024}:
\begin{equation}
  \mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}
  \label{eq:nao_linear_dlr}
\end{equation}
onde $\mathbf{A}^\dagger$ representa a pseudo-inversa linear clássica do operador de projeção de Radon.

Essa não-linearidade profunda induz quatro manifestações físicas críticas (\cref{fig:dlr_non_linear}):
\begin{enumerate}
  \item \textbf{Dependência do Contraste e da Cena:} A resolução espacial deixa de ser constante: bordas de osso ou contraste iodado (+300 HU) mantêm resolução elevada, enquanto lesões de baixo contraste (+20 HU) sofrem forte atenuação de frequências altas;
  \item \textbf{Não-Estacionariedade Espacial do Ruído:} O ruído deixa de ser espacialmente homogêneo, variando de acordo com a proximidade de interfaces anatômicas de alta densidade;
  \item \textbf{Efeito Ceroso (\emph{Plastic/Waxy Look}):} A rede neural concentra a energia espectral do ruído residual em baixas frequências espaciais ($f < 0{,}2\text{ mm}^{-1}$). O ruído perde a granularidade natural e adquire uma aparência plástica/cerosa que mascara a visualização de microcalcificações e bordas tumorais sutis \cite{toia2023};
  \item \textbf{Colapso dos Modelos Lineares Tradicionais:} O modelo analítico linear NPWE falha em prever a acurácia dos radiologistas sob DLR, apresentando dispersão e baixa correlação ($r \approx 0{,}68$, Painel B da \cref{fig:dlr_non_linear}).
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption[Não-Linearidade em DLR e Detrending Polinomial]{Impacto da Não-Linearidade em DLR, Colapso de Modelos Analíticos Lineares e Metodologia de Detrending. (A) Detectabilidade $d'$ em função do nível de dose $\text{CTDI}_{\text{vol}}$ para FBP, HIR e DLR. (B) Dispersão do modelo NPWE ($r = 0{,}68$) versus alta correlação do modelo DLMO ($r = 0{,}98$). (C) Processo de Detrending Polinomial 2D para isolamento do ruído puro.}
  \label{fig:dlr_non_linear}
\end{figure}

\subsection{Transição para a Próxima Seção}
Para quantificar com rigor físico essas não-linearidades, os simuladores geométricos homogêneos de acrílico tornaram-se insuficientes, exigindo o desenvolvimento de simuladores antropomórficos híbridos.

\section{A Transição dos Simuladores: De Cilindros Homogêneos a Phantoms Antropomórficos Híbridos}
\label{sec:phantoms_hibridos}

\subsection{Contextualização e Relevância para o Tema}
Simuladores homogêneos de acrílico ou água foram concebidos para sistemas lineares. Quando submetidos a redes neurais DLR (que foram treinadas exclusivamente com anatomias humanas), os simuladores homogêneos geram artefatos atípicos por estarem fora da distribuição de treinamento (*out-of-distribution*). Esta seção apresenta a metodologia de simuladores antropomórficos híbridos.

\subsection{A Metodologia do Phantom Híbrido 2AFC}
Para restabelecer a validade metrológica em tomografia de última geração, a física médica adotou os Phantoms Antropomórficos Híbridos (\cref{fig:phantom_flow}) \cite{solomon2020, debbiche2024}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption[Metodologia de Phantoms Híbridos e Teste 2AFC]{Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.}
  \label{fig:phantom_flow}
\end{figure}

Essa metodologia baseia-se em quatro etapas rigorosas:
\begin{enumerate}
  \item **Aquisição Física Real:** Utilizam-se simuladores físicos antropomórficos de alta fidelidade anatômica (como o *phantom* FREDDIE), impressos em 3D com polímeros e resinas equivalentes a tecido ósseo, parênquima pulmonar e tecidos moles;
  \item **Banco de Fundos Anatômicos Reais ($H_0$):** Realizam-se varreduras tomográficas em múltiplos tomógrafos clínicos sob diversos níveis de dose, extraindo-se milhares de regiões de interesse anatômicas reais sem patologia física;
  \item **Inserção Híbrida Tridimensional ($H_1$):** Modelam-se computacionalmente lesões clínicas tridimensionais (nódulos pulmonares esféricos e espiculados, metástases hepáticas e lesões líticas/blásticas), as quais são convolvidas com a PSF tridimensional real do equipamento e somadas linearmente às ROIs anatômicas antes da reconstrução ou na imagem final;
  \item **Verdade de Campo Absoluta:** O método produz um conjunto com dezenas de milhares de casos com localização, tamanho e contraste central exatamente conhecidos (*ground truth* perfeito), viabilizando o treinamento supervisionado de inteligência artificial e a condução de testes psicofísicos 2AFC com radiologistas.
\end{enumerate}

\subsection{Transição para a Próxima Seção}
Ao calcular o espectro de ruído ($NPS$) sobre esses fundos anatômicos reais, surge o desafio físico dos gradientes macroscópicos de densidade tecidual. A solução metrológica é a técnica de Detrending Polinomial 2D.

\section{Tratamento de Ruído em Anatomias Complexas: Detrending Polinomial 2D e Incerteza Bootstrap}
\label{sec:detrending}

\subsection{Contextualização e Relevância para o Tema}
O cálculo do $NPS$ exige amostras de ruído com média zero. Em anatomias complexas, variações anatômicas normais (como a transição entre o pulmão e a pleura) contaminam o espectro com frequências muito baixas espúrias. O detrending polinomial remove essa contaminação.

\subsection{Formulação Matemática do Detrending 2D e Incerteza por Bootstrap}
Para cada sub-região anatômica $I_k(x, y)$ de dimensão $N_x \times N_y$ pixels, ajusta-se por mínimos quadrados uma superfície polinomial bidimensional de 2ª ordem $P_2(x, y)$ (Painel C da \cref{fig:dlr_non_linear}):
\begin{equation}
  P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy
  \label{eq:polinomio_2d}
\end{equation}

Os coeficientes ótimos $\mathbf{a} = (a_0, \dots, a_5)^T$ são calculados analiticamente através da matriz de Vandermonde $\mathbf{V}$:
\begin{equation}
  \mathbf{a} = (\mathbf{V}^T \mathbf{V})^{-1} \mathbf{V}^T \mathbf{i}_k
  \label{eq:ajuste_minimos_quadrados}
\end{equation}
onde $\mathbf{i}_k$ é o vetor unidimensional obtido pela vetorização de $I_k(x, y)$.

A imagem de ruído puro residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é subtraída do gradiente anatômico macroscópico e multiplicada por uma janela de Hanning bidimensional antes do cálculo da Transformada de Fourier 2D, eliminando vazamentos espectrais de borda.

Para quantificar a incerteza experimental e os intervalos de confiança de 95\% do índice $d'$ sem impor premissas gaussianas arbitrárias, aplica-se a técnica estatística de reamostragem Bootstrap não-paramétrica com $B = 2000$ replicações com reposição:
\begin{equation}
  \text{SE}_{\text{boot}}(d') = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B \left( d'^{*(b)} - \bar{d}'^* \right)^2}
  \label{eq:bootstrap_se}
\end{equation}

\subsection{Transição para o Próximo Capítulo}
Compreendidos o colapso da linearidade e os métodos experimentais com simuladores antropomórficos, o próximo capítulo explora o estado da arte na física médica: os Observadores Baseados em Aprendizado Profundo com Vision Transformers (DLMO), a física dos detectores de Contagem de Fótons (PCCT) e a Otimização Multiobjetivo pela Fronteira de Pareto 3D.

% ------------------------------------------------------------------------------
% CAPÍTULO 5: O ESTADO DA ARTE: OBSERVADORES POR APRENDIZADO PROFUNDO, PCCT E OTIMIZAÇÃO MULTIOBJETIVO
% ------------------------------------------------------------------------------
\chapter{O Estado da Arte: Observadores por Aprendizado Profundo, PCCT e Otimização Multiobjetivo}
\label{chap:estado_da_arte}

Este capítulo consolida a fronteira científica da metrologia em tomografia computadorizada. Apresenta-se o Observador de Modelo por Aprendizado Profundo (DLMO) fundamentado em arquiteturas Vision Transformers (ViT) com auto-atenção multi-cabeça e calibração perceptual multitarefa. Em seguida, detalha-se a biofísica da Tomografia por Contagem de Fótons (PCCT) e a síntese de Imagens Monoenergéticas Virtuais ($VMI$). Por fim, formula-se o problema de Otimização Multiobjetivo Não Linear através do mapeamento da Fronteira de Pareto Tridimensional $(D, T, -W)$.

\section{Observadores Baseados em Aprendizado Profundo e Auto-Atenção}
\label{sec:dlmo}

\subsection{Contextualização e Relevância para o Tema}
Para superar as limitações dos observadores analíticos lineares em reconstruções DLR, a física médica desenvolveu os Observadores de Modelo por Aprendizado Profundo (\emph{Deep Learning Model Observers} --- DLMO), capazes de aprender funções de decisão não lineares que mimetizam a percepção foveal-periférica dos radiologistas.

\subsection{Arquitetura Neural Vision Transformer (ViT)}
Em vez de assumir templates lineares rígidos, o DLMO emprega arquiteturas neurais avançadas baseadas em \emph{Vision Transformers} (ViT) com mecanismos de Auto-Atenção Multi-Cabeça (MHSA), conforme esquematizado no \cref{fig:dlmo_arch} \cite{dosovitskiy2021, zhou2021, schilder2026}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption[Arquitetura Neural do DLMO]{Arquitetura Neural do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer) e Calibração Perceptual.}
  \label{fig:dlmo_arch}
\end{figure}

A imagem tomográfica $\mathbf{x} \in \mathbb{R}^{H \times W \times C}$ é dividida em uma grade de $N_p = \frac{HW}{P^2}$ blocos espaciais bidimensionais não-sobrepostos (\emph{patches}) $\mathbf{x}_p \in \mathbb{R}^{N_p \times (P^2 C)}$, onde $P \times P$ é a dimensão de cada bloco (ex: $8 \times 8$ pixels). Cada bloco é projetado linearmente para um espaço latente contínuo de dimensão $D_{\text{model}}$ através de uma matriz treinável $\mathbf{E}$:
\begin{equation}
  \mathbf{z}_0 = \left[ \mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \mathbf{x}_p^2 \mathbf{E}; \, \dots; \, \mathbf{x}_p^{N_p} \mathbf{E} \right] + \mathbf{E}_{\text{pos}}
  \label{eq:vit_embedding}
\end{equation}
onde $\mathbf{x}_{\text{class}}$ é o token de classificação diagnóstica e $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N_p + 1) \times D_{\text{model}}}$ adiciona a codificação posicional bidimensional aprendida.

\subsection{Mecanismo de Auto-Atenção Multi-Cabeça e Analogia Neurofisiológica}
Para cada bloco da imagem, calculam-se as matrizes de Consulta (\emph{Query} --- $Q$), Chave (\emph{Key} --- $K$) e Valor (\emph{Value} --- $V$) através de matrizes de peso lineares $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V$:
\begin{equation}
  Q = \mathbf{z} \mathbf{W}_Q, \qquad K = \mathbf{z} \mathbf{W}_K, \qquad V = \mathbf{z} \mathbf{W}_V
  \label{eq:qkv}
\end{equation}

O operador de auto-atenção por produto escalar escalonado é expresso por:
\begin{equation}
  \text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
  \label{eq:attention_formula}
\end{equation}
onde o fator $\sqrt{d_k}$ evita a saturação de gradientes na função softmax.

Do ponto de vista da neurociência da visão, a auto-atenção mimetiza perfeitamente a coordenação foveal-periférica humana: as cabeças de atenção calculam as correlações contextuais globais do parênquima anatômico periférico enquanto concentram alta capacidade discriminativa na fóvea central onde a lesão diagnóstica se localiza.

A saída não linear da rede $t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$ permite calcular o índice de detectabilidade do modelo profundo:
\begin{equation}
  d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}
  \label{eq:dprime_dl}
\end{equation}

\subsection{Transição para a Próxima Seção}
Para garantir que o DLMO funcione como um verdadeiro instrumento metrológico da percepção médica, a rede neural não pode ser treinada apenas como um classificador puramente matemático, mas sim ancorada diretamente nas leituras de radiologistas através de perdas perceptuais e validação cruzada LOSO.

\section{Calibração Perceptual com Radiologistas e Transferibilidade Leave-One-Scanner-Out}
\label{sec:loso}

\subsection{Contextualização e Relevância para o Tema}
Um modelo de inteligência artificial sobreajustado pode atingir acurácia de 100\% em dados de treinamento, mas falhar em refletir a realidade perceptual humana ou em generalizar para tomógrafos de outros hospitais. Esta seção detalha como garantir fidelidade clínica e transferibilidade inter-scanners.

\subsection{Função de Perda Perceptual Multitarefa}
Para forçar a rede neural a mimetizar a sensibilidade perceptual de especialistas humanos, o treinamento adota uma função de perda de otimização multitarefa que penaliza desvios em relação à detectabilidade medida em experimentos psicofísicos 2AFC reais com médicos radiologistas \cite{zhou2021}:
\begin{equation}
  \mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{BCE}}(y, \hat{y}) + \lambda \, \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2
  \label{eq:perceptual_loss}
\end{equation}
onde $\mathcal{L}_{\text{BCE}}$ é a entropia cruzada binária clássica e o hiperparâmetro de regularização $\lambda$ calibra o alinhamento perceptual.

\subsection{Protocolo de Validação Cruzada Leave-One-Scanner-Out (LOSO)}
A robustez do modelo frente a diferentes fornecedores é testada pelo esquema de validação cruzada \emph{Leave-One-Scanner-Out} (LOSO): para um conjunto de $K$ tomógrafos clínicos distintos (ex: $K = 7$ tomógrafos de fabricantes GE, Siemens, Canon e Philips), treina-se o observador utilizando dados de $K - 1$ equipamentos e avalia-se cegamente o desempenho no tomógrafo restante omitido. A obtenção de coeficientes de correlação $r > 0{,}95$ em todos os ciclos LOSO comprova que o modelo aprendeu as invariâncias físicas universais da formação de imagem.

\subsection{Transição para a Próxima Seção}
Enquanto as reconstruções por IA aprimoram os tomógrafos convencionais, a maior revolução física recente nos detectores de radiação é a Tomografia Computadorizada por Contagem de Fótons (PCCT), analisada a seguir.

\section{Física da Tomografia Computadorizada por Contagem de Fótons}
\label{sec:pcct_fisica}

\subsection{Contextualização e Relevância para o Tema}
A tecnologia PCCT representa o salto tecnológico mais expressivo da tomografia computadorizada na última década. Compreender sua física no nível dos semicondutores é crucial para a pesquisa de doutoramento do autor no IFUSP e InRad-HCFMUSP.

\subsection{Detectores Semicondutores de Conversão Direta versus Cintiladores}
A \cref{tab:eict_vs_pcct} sintetiza as diferenças fundamentais entre os detectores tradicionais de Integração de Energia (EICT) e os novos detectores de Contagem de Fótons (PCCT) \cite{flohr2020, mccollough2026, pimenta2025, pimenta2026}.

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

Enquanto os detectores EICT convertem raios X em luz visível dentro de cintiladores cerâmicos (induzindo espalhamento de luz que exige septos refletores entre pixels), os detectores PCCT utilizam cristais semicondutores de conversão direta (Telureto de Cádmio --- CdTe, CZT ou Silício com espessura de $1{,}5\text{ a }3{,}0\text{ mm}$ polarizados sob alta tensão de $-800\text{ a }-1000\text{ V}$).

A absorção fotoelétrica de cada fóton gera instantaneamente uma nuvem de pares elétron-lacuna que migra em nanossegundos em direção aos ânodos pixelados, produzindo um pulso de tensão cuja amplitude é estritamente proporcional à energia do fóton incidente:
\begin{equation}
  V_{\text{pulso}} \propto Q = \frac{E_{\text{fóton}}}{W_{\text{ionização}}}
  \label{eq:vpulso}
\end{equation}
onde $W_{\text{ionização}} \approx 4{,}43\text{ eV}$ para o CdTe (frente a mais de $30\text{ eV}$ exigidos para produzir um elétron em cintiladores convencionais).

\subsection{Fenômenos Estocásticos e Imagens Monoenergéticas Virtuais (VMI)}
Dois fenômenos estocásticos em PCCT exigem modelagem metrológica criteriosa:
\begin{itemize}
  \item \textbf{Compartilhamento de Carga (\emph{Charge Sharing}):} Quando um fóton interage próximo à borda de dois pixels, a nuvem de elétrons divide-se entre ânodos vizinhos, sendo corrigida por circuitos eletrônicos ultra-rápidos de soma de carga em tempo real;
  \item \textbf{Empilhamento de Pulsos (\emph{Pulse Pile-Up}):} Em fluxos muito intensos de radiação ($> 10^7\text{ fótons}/(\text{mm}^2\cdot\text{s})$), fótons sucessivos sobrepõem-se antes do restabelecimento da linha de base, exigindo modelagem de tempo morto paralyzable e non-paralyzable \cite{knoll2010}.
\end{itemize}

A separação dos pulsos em múltiplos comparadores com limiares de energia programáveis ($E_1, E_2, E_3, E_4$) viabiliza a síntese de Imagens Monoenergéticas Virtuais ($VMI$) em qualquer quiloeletron-volt desejado (de 40 a 140 keV):
\begin{equation}
  I_{\text{VMI}}(x, y; E_0) = a_1(x, y) \cdot f_{\text{foto}}(E_0) + a_2(x, y) \cdot f_{\text{Compton}}(E_0)
  \label{eq:vmi_formula}
\end{equation}

Em baixas energias ($40\text{ a }50\text{ keV}$), maximiza-se o contraste fotoelétrico do iodo ($K\text{-edge} = 33{,}2\text{ keV}$), elevando a $TTF$ de lesões vasculares sem a elevação de ruído eletrônico observada nos tomógrafos EICT.

\subsection{Transição para a Próxima Seção}
A coexistência de múltiplos parâmetros de aquisição em EICT e PCCT (kVp, mA, espessura, pitch, energia de VMI e algoritmo de DLR) gera um espaço combinatório imenso. A resposta da física médica para encontrar o protocolo clínico ideal é a Otimização Multiobjetivo pela Fronteira de Pareto Tridimensional.

\section{Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional}
\label{sec:pareto_otimizacao}

\subsection{Contextualização e Relevância para o Tema}
Na rotina hospitalar real de emergências e centros cirúrgicos, a otimização não pode considerar apenas a dose e a qualidade: o tempo total do procedimento ($T$) é uma variável crítica para a sobrevivência de pacientes politraumatizados ou com acidente vascular cerebral (AVC). Esta seção formaliza a otimização simultânea dessas três grandezas.

\subsection{Formulação Matemática da Fronteira de Pareto Tridimensional}
A otimização de protocolos tomográficos é modelada como um problema de Programação Não Linear Multiobjetivo \cite{oostveen2021}:
\begin{equation}
  \min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}
  \label{eq:multiobjetivo_pareto}
\end{equation}
onde o vetor de decisão $\mathbf{p} = (\text{kVp}, \text{mA}, t_{\text{rot}}, \text{pitch}, \text{corte}, \text{kernel}, \text{nível DLR}, E_{\text{VMI}})^T$ pertence ao espaço viável $\Omega$, sujeito às restrições clínicas formais:
\begin{itemize}
  \item $D(\mathbf{p}) \le \text{DRL}$ (restrição de dose de radioproteção segundo Níveis de Referência Diagnóstica);
  \item $T(\mathbf{p}) \le T_{\text{máx}}$ (restrição operacional de tempo para evitar artefatos de movimento respiratório e cardíaco);
  \item $W(\mathbf{p}) = d'(\mathbf{p}) \ge d'_{\text{mín}}$ (restrição diagnóstica de detectabilidade para preservar a acurácia médica).
\end{itemize}

A \cref{fig:pareto_3d} apresenta o compromisso bi-objetivo e a superfície de Pareto tridimensional completa.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption[Otimização Multiobjetivo e Fronteira de Pareto]{Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto. (A) Trade-off bidimensional entre Dose de Radiação e Detectabilidade Diagnóstica, ilustrando a fronteira ótima e os protocolos clínicos dominados ineficientes. (B) Superfície de Pareto Tridimensional $(D, T, -W)$, integrando simultaneamente Dose de Radiação ($D$), Tempo Operacional total ($T$) e Detectabilidade Diagnóstica ($W = d'$).}
  \label{fig:pareto_3d}
\end{figure}

Uma solução $\mathbf{p}^*$ pertence à Fronteira de Pareto se não existir nenhum outro protocolo $\mathbf{p}$ que reduza a dose ou o tempo sem degradar a detectabilidade diagnóstica.

O mapeamento dessa superfície não-dominada é computado pelo Algoritmo Genético NSGA-II (\emph{Non-dominated Sorting Genetic Algorithm II}). A seleção da solução ideal para cada perfil hospitalar é determinada pelo método de Tomada de Decisão Multicritério TOPSIS (\emph{Technique for Order Preference by Similarity to Ideal Solution}), permitindo configurar automaticamente o tomógrafo para protocolos pediátricos de ultrabaixa dose, protocolos de trauma ultrarrápidos ou protocolos de oncologia de alta resolução.

\subsection{Transição para o Próximo Capítulo}
Com a teoria biofísica, os modelos neurais e a formulação de Pareto consolidados, o próximo capítulo descreve a arquitetura do software modular desenvolvido e os aspectos éticos de pesquisa com seres humanos.

% ------------------------------------------------------------------------------
% CAPÍTULO 6: ARQUITETURA COMPUTACIONAL, METROLOGIA EXPERIMENTAL E ASPECTOS ÉTICOS
% ------------------------------------------------------------------------------
\chapter{Arquitetura Computacional, Metrologia Experimental e Aspectos Éticos}
\label{chap:arquitetura_metrologia}

Este capítulo detalha a infraestrutura computacional modular em Python desenvolvida para a execução automatizada do pipeline metrológico no Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP (GDRFM-IFUSP). Apresentam-se a padronização das aquisições segundo o Relatório AAPM TG-233 e as diretrizes regulatórias e bioéticas (CEP/CONEP) para a realização dos testes psicofísicos com médicos radiologistas.

\section{Arquitetura de Software do Pipeline Integrado de Metrologia}
\label{sec:software_arch}

\subsection{Contextualização e Relevância para o Tema}
A aplicabilidade prática de qualquer formulação teórica de física médica depende de uma arquitetura de software robusta, reproduzível e computacionalmente eficiente, capaz de processar gigabytes de exames tomográficos DICOM automaticamente.

\subsection{Estrutura dos Módulos do Software}
O software foi desenvolvido em linguagem Python utilizando as bibliotecas de computação científica e aprendizado profundo NumPy, SciPy, PyDICOM e PyTorch, esquematizado no \cref{fig:software_flow} \cite{choopani2023}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.96\textwidth]{figuras/flow6_software_pipeline.png}
  \caption[Arquitetura Modular do Software de Metrologia]{Arquitetura Modular do Software de Metrologia em Tomografia Computadorizada (Pipeline Integrado GDRFM-IFUSP).}
  \label{fig:software_flow}
\end{figure}

O sistema organiza-se em cinco módulos encadeados:
\begin{itemize}
  \item \textbf{Módulo 1 (Leitura DICOM e Parser de Metadados):} Faz a ingestão direta de arquivos DICOM padronizados, extraindo e validando parâmetros do feixe (kVp, mA, tempo de rotação, pitch, espessura, kernel e nível de DLR);
  \item \textbf{Módulo 2 (Segmentação e Amostragem Automática):} Identifica as coordenadas dos insertos de calibração via Transformada Circular de Hough e amostra mosaicos com $M \ge 100$ ROIs anatômicas independentes;
  \item \textbf{Módulo 3A (Resolução Espacial da Tarefa):} Executa o algoritmo de agrupamento radial superamostrado na borda de insertos cilíndricos, calculando $\text{ESF}(r) \to \text{LSF}(r) \to TTF(f)$ e extraindo o descritor $f_{50}$;
  \item \textbf{Módulo 3B (Textura e Espectro de Ruído):} Aplica o detrending polinomial 2D $P_2(x, y)$, janelamento de Hanning e Transformada Rápida de Fourier 2D (FFT2), gerando $NPS(u, v)$ e a curva radial $NPS(f)$;
  \item \textbf{Módulo 4 (Observadores de Modelo):} Executa o cálculo da detectabilidade pelos observadores lineares clássicos (NPWE e CHO com canais D-DOG/LG/Gabor) e pelo observador de aprendizado profundo (DLMO com Vision Transformers);
  \item \textbf{Módulo 5 (Incerteza e Otimização de Pareto):} Realiza a reamostragem Bootstrap não-paramétrica ($B = 2000$) para cálculo dos intervalos de confiança e executa o algoritmo genético NSGA-II com ranqueamento TOPSIS.
\end{itemize}

\subsection{Transição para a Próxima Seção}
Para garantir a comparabilidade internacional das medições geradas por esse pipeline de software, as aquisições tomográficas foram padronizadas segundo as diretrizes da AAPM TG-233.

\section{Protocolo Metrológico Padronizado segundo o Relatório AAPM TG-233}
\label{sec:protocolo_tg233}

\subsection{Contextualização e Relevância para o Tema}
A padronização metrológica rigorosa é a garantia de que as medições de detectabilidade realizadas no Brasil sejam diretamente reprodutíveis em centros de excelência internacionais (como a Clínica Mayo, Harvard e Radboudumc).

\subsection{Parâmetros de Aquisição e Modelagem de Lesões}
As aquisições tomográficas para calibração seguem as diretrizes internacionais da AAPM \cite{aapm_tg233_2019}:
\begin{itemize}
  \item Matriz de imagem de $512 \times 512$ pixels com FOV ajustado ao diâmetro do simulador ($200 \text{ a } 350 \text{ mm}$);
  \item Espessuras de corte de $0{,}5 \text{ a } 1{,}0 \text{ mm}$ para alta resolução e $2{,}5 \text{ a } 5{,}0 \text{ mm}$ para rotina clínica;
  \item Tensões de tubo de 80, 100, 120 e 140 kVp, cobrindo doses de $\text{CTDI}_{\text{vol}}$ de $0{,}5 \text{ mGy}$ a $15 \text{ mGy}$;
  \item Modelagem de lesões esféricas padronizadas com diâmetros de 3, 5, 8 e 10 mm e contrastes clínicos de $-600 \text{ HU}$ (nódulo subsólido pulmonar), $+100 \text{ HU}$ (nódulo sólido hiperatenuante) e $+30 \text{ HU}$ (lesão hepática de baixo contraste).
\end{itemize}

\subsection{Transição para a Próxima Seção}
Como o estudo envolve a participação de médicos radiologistas para a calibração psicofísica dos observadores computacionais, é imprescindível cumprir os requisitos éticos e regulatórios da pesquisa com seres humanos.

\section{Aspectos Bioéticos, Regulatórios e Desenho Experimental com Seres Humanos}
\label{sec:bioetica}

\subsection{Contextualização e Relevância para o Tema}
A realização de experimentos psicofísicos com seres humanos exige rigor ético estrito para garantir o consentimento livre, a proteção dos dados profissionais dos participantes e a validade científica das condições de observação.

\subsection{Diretrizes Éticas e Controle de Fadiga Visual}
A condução dos testes psicofísicos 2AFC com médicos radiologistas para obtenção dos dados de calibração segue as diretrizes do sistema CEP/CONEP:
\begin{itemize}
  \item Recrutamento de no mínimo 20 médicos radiologistas com título de especialista pelo CBR para cada anatomia clínica avaliada ($\ge 60$ leitores no total para tórax, abdome e crânio);
  \item Aplicação obrigatória de Termo de Consentimento Livre e Esclarecido (TCLE) com garantia de anonimização dos dados de desempenho individual;
  \item Monitores diagnósticos com luminância calibrada segundo o padrão DICOM GSDF ($\ge 400 \text{ cd/m}^2$) e iluminação ambiente controlada ($< 15 \text{ lux}$);
  \item Mitigação de fadiga visual através de sessões curtas com no máximo 100 a 150 pares de imagens 2AFC por sessão (duração inferior a 25 minutos).
\end{itemize}

\subsection{Transição para o Próximo Capítulo}
Com a arquitetura computacional, os protocolos de aquisição e as salvaguardas bioéticas devidamente estruturadas, o próximo capítulo sintetiza as conclusões desta monografia e apresenta as perspectivas de continuidade na pesquisa de Doutorado Direto do autor.

% ------------------------------------------------------------------------------
% CAPÍTULO 7: CONSIDERAÇÕES FINAIS E PERSPECTIVAS
% ------------------------------------------------------------------------------
\chapter{Considerações Finais e Perspectivas}
\label{chap:conclusoes}

Este capítulo final sintetiza as principais contribuições científicas desenvolvidas ao longo desta monografia, analisa o impacto clínico e normativo para os serviços de radiologia e articula formalmente os desdobramentos desta pesquisa no projeto de Doutorado Direto (FAPESP 2026--2030) do autor no Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP e InRad-HCFMUSP.

\section{Síntese da Trajetória Biofísica e Metrológica}
\label{sec:sintese_biofisica}

\subsection{Contextualização e Relevância para o Tema}
A evolução da garantia da qualidade em tomografia computadorizada reflete um processo contínuo de superação de modelos simplificados em direção à descrição exata da física quântica e da neurobiologia da percepção humana.

\subsection{As Quatro Fases da Avaliação de Qualidade de Imagem}
A trajetória histórica e metodológica percorrida nesta monografia consolida-se em quatro marcos científicos fundamentais:
\begin{enumerate}
  \item \textbf{A Fase Linear Analítica (1950--1990):} Partiu da Teoria de Detecção de Sinais e do limite teórico do Observador Ideal Bayesiano, introduzindo filtros de sensibilidade ao contraste ocular (NPWE) para quantificar imagens em fundos uniformes;
  \item \textbf{A Modelagem Cortical (1990--2015):} Desenvolveu o Observador de Hotelling Canalizado (CHO), aplicando filtros inspirados no córtex visual humano para contornar a barreira dimensional e tratar o ruído anatômico estruturado;
  \item \textbf{A Ruptura da Linearidade (2015--2026):} A introdução clínica de redes neurais convolucionais de reconstrução (DLR) quebrou as premissas de linearidade e estacionariedade, demonstrando que métricas escalares clássicas ($SNR$, $CNR$, desvio padrão em HU) são incapazes de garantir segurança diagnóstica;
  \item \textbf{O Paradigma da IA Perceptual e Otimização Multiobjetivo (2026+):} A consolidação dos observadores baseados em \emph{Vision Transformers} com mecanismos de auto-atenção (DLMO), calibrados diretamente contra leituras humanas em testes 2AFC/MRMC e integrados ao espaço tridimensional de Pareto $(D, T, -W)$.
\end{enumerate}

\subsection{Transição para a Próxima Seção}
A consolidação teórica e computacional dessa metodologia produz impactos imediatos na segurança dos pacientes e na rotina operacional dos hospitais.

\section{Impacto Clínico, Operacional e Normativo}
\label{sec:impacto_clinico}

\subsection{Benefícios Diretos para a Física Médica e a Saúde Pública}
A implementação desse pipeline metrológico acarreta benefícios práticos diretos:
\begin{itemize}
  \item \textbf{Segurança Radiológica Personalizada:} Proporciona comprovação física de que reduções de até 60\% de dose em exames pediátricos e de rastreio oncológico preservam integralmente a detectabilidade diagnóstica;
  \item \textbf{Auditoria Hospitalar e Conformidade Internacional:} Viabiliza a automação dos testes de comissionamento de tomógrafos de acordo com o relatório AAPM TG-233 e com o sistema internacional IAEA 5-Star de auditoria em radiologia \cite{iaea_5star_2026};
  \item \textbf{Harmonização de Parques Tecnológicos Multimarca:} Permite equalizar o desempenho diagnóstico entre tomógrafos de diferentes fornecedores (GE, Siemens, Canon e Philips) em grandes complexos hospitalares.
\end{itemize}

\subsection{Transição para a Próxima Seção}
Esta monografia de conclusão de curso cumpre o papel de alicerce teórico e metodológico que fundamenta diretamente a pesquisa de pós-graduação do autor.

\section{Articulação com a Pesquisa de Doutorado Direto (FAPESP 2026--2030)}
\label{sec:fapesp_doutorado}

\subsection{Contextualização e Metas Futuras}
Esta monografia consolida o embasamento biofísico, matemático e computacional que sustenta o projeto de pesquisa de Doutorado Direto do autor (FAPESP 2026--2030) no Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP e no Instituto de Radiologia do Hospital das Clínicas da FMUSP (InRad-HCFMUSP).

O trabalho articula-se com os avanços em PCCT da Dra. Elsa Pimenta (Doutorado 2026) \cite{pimenta2026, pimenta2025} e com o pipeline de automação linear no tórax de Davi Amaral (Mestrado FAPESP), estabelecendo as seguintes metas para a tese de doutorado:
\begin{enumerate}[label=\alph*)]
  \item Treinamento e validação experimental em larga escala do observador DLMO baseado em \emph{Vision Transformers} com auto-atenção multi-cabeça;
  \item Execução do estudo psicofísico nacional 2AFC com mais de 60 médicos radiologistas especialistas sob modelagem ANOVA MRMC completa;
  \item Validação cruzada de transferibilidade inter-scanners (\emph{leave-one-scanner-out}) em sete tomógrafos clínicos de quatro fabricantes distintos no InRad-HCFMUSP e Radboudumc;
  \item Mapeamento experimental exaustivo da Fronteira de Pareto Tridimensional $(D, T, -W)$ para os principais protocolos tomográficos de crânio, tórax e abdome em sistemas EICT e PCCT.
\end{enumerate}

Conclui-se, assim, este trabalho acadêmico com a convicção de que a física médica brasileira continua contribuindo ativamente para a vanguarda científica internacional, unindo o rigor analítico da física nuclear e da inteligência artificial à missão humanitária de proteger vidas.
"""

# Now handle the Bibliography:
# Extract ordered cite keys from text
cites = re.findall(r"\\cite\{([^}]+)\}", expanded_tex)
ordered_keys = []
for c in cites:
    keys = [k.strip() for k in c.split(",")]
    for k in keys:
        if k not in ordered_keys:
            ordered_keys.append(k)

# Raw dictionary of all references
bib_database = {
    "mccollough2026": r"MCCOLLOUGH, C. H. et al. Radiation dose in computed tomography: technological advances and clinical optimization over two decades. \textbf{Radiology}, v. 318, n. 2, p. e251200, 2026.",
    "bushberg2020": r"BUSHBERG, J. T.; SEIBERT, J. A.; LEIDHOLDT, E. M.; BOONE, J. M. \textbf{The Essential Physics of Medical Imaging}. 4. ed. Philadelphia: Lippincott Williams \& Wilkins, 2020. 1048 p.",
    "seeram2015": r"SEERAM, E. \textbf{Computed Tomography: Physical Principles, Clinical Applications, and Quality Control}. 4. ed. St. Louis: Elsevier Health Sciences, 2015. 560 p.",
    "icrp103_2007": r"INTERNATIONAL COMMISSION ON RADIOLOGICAL PROTECTION (ICRP). \textbf{The 2007 Recommendations of the International Commission on Radiological Protection}. ICRP Publication 103. Annals of the ICRP, v. 37, n. 2-4, p. 1--332, 2007.",
    "attix1986": r"ATTIX, F. H. \textbf{Introduction to Radiological Physics and Radiation Dosimetry}. New York: John Wiley \& Sons, 1986. 607 p.",
    "anvisa_rdc611_2022": r"AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Resolução da Diretoria Colegiada - RDC nº 611, de 9 de março de 2022}: Estabelece os requisitos sanitários para a organização e o funcionamento de serviços de radiologia diagnóstica ou intervencionista. Brasília: ANVISA, 2022.",
    "anvisa_in93_2021": r"AGÊNCIA NACIONAL DE VIGILÂNCIA SANITÁRIA (ANVISA). \textbf{Instrução Normativa nº 93, de 27 de maio de 2021}: Estabelece os requisitos sanitários para a garantia da qualidade e da segurança em sistemas de tomografia computadorizada médica. Brasília: ANVISA, 2021.",
    "racine2020": r"RACINE, D. et al. Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. \textbf{Physics in Medicine \& Biology}, v. 65, n. 18, p. 185011, 2020.",
    "debbiche2024": r"DEBBICHE, I. et al. Task-based image quality assessment of deep learning image reconstruction in abdominal CT: a multi-reader phantom study. \textbf{European Radiology}, v. 34, n. 5, p. 3120--3132, 2024.",
    "greffier2026": r"GREFFIER, J. et al. Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. \textbf{Diagnostic and Interventional Imaging}, v. 107, n. 1, p. 1016--1025, 2026.",
    "greffier2023": r"GREFFIER, J. et al. Comparison of iterative and deep learning reconstruction algorithms in low-dose abdominal CT: a task-based image quality study on a phantom. \textbf{European Radiology}, v. 33, p. 7890--7901, 2023.",
    "toia2023": r"TOIA, G. V. et al. Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. \textbf{European Radiology}, v. 33, p. 4310--4322, 2023.",
    "solomon2020": r"SOLOMON, J. et al. Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. \textbf{Medical Physics}, v. 47, n. 8, p. 3412--3425, 2020.",
    "aapm_tg233_2019": r"AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM). \textbf{Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233}. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., Medical Physics, v. 46, n. 11, p. e735--e756, 2019).",
    "icru54_1996": r"INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU). \textbf{Medical Imaging - The Assessment of Image Quality}. ICRU Report 54. Bethesda, MD: ICRU, 1996.",
    "peterson1954": r"PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C. The theory of signal detectability. \textbf{Transactions of the IRE Professional Group on Information Theory}, v. 4, n. 4, p. 171--212, 1954.",
    "lusted1968": r"LUSTED, L. B. \textbf{Introduction to Medical Decision Making}. Springfield, IL: Charles C Thomas, 1968.",
    "metz1986": r"METZ, C. E. ROC methodology in radiologic imaging. \textbf{Investigative Radiology}, v. 21, n. 9, p. 720--733, 1986.",
    "barrett_myers_2004": r"BARRETT, H. H.; MYERS, K. J. \textbf{Foundations of Image Science}. Hoboken: John Wiley \& Sons, 2004. 1540 p.",
    "burgess1999": r"BURGESS, A. E. The Rose model, revisited. \textbf{Journal of the Optical Society of America A}, v. 16, n. 3, p. 633--646, 1999.",
    "wagner1979": r"WAGNER, R. F.; BROWN, D. G.; METZ, C. E. Application of information theory to the assessment of computed tomography. \textbf{Medical Physics}, v. 6, n. 2, p. 83--94, 1979.",
    "burgess1994": r"BURGESS, A. E. Statistically defined backgrounds: performance of a modified nonprewhitening observer model. \textbf{Journal of the Optical Society of America A}, v. 11, n. 4, p. 1237--1242, 1994.",
    "eckstein2000": r"ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P. Role of knowledge in human visual search for signals in noise. \textbf{Journal of the Optical Society of America A}, v. 17, n. 11, p. 2064--2076, 2000.",
    "barrett1993": r"BARRETT, H. H.; YAO, J.; ROLAND, P. X.; MYERS, K. J. Model observers for assessment of image quality. \textbf{Physics in Medicine \& Biology}, v. 38, n. 2, p. 277--295, 1993.",
    "myers1987": r"MYERS, K. J.; BARRETT, H. H. Addition of a channel mechanism to the ideal-observer model. \textbf{Journal of the Optical Society of America A}, v. 4, n. 12, p. 2447--2457, 1987.",
    "yao1992": r"YAO, J.; BARRETT, H. H. Predicting human performance by a channelized Hotelling observer model. In: \textbf{SPIE Medical Imaging: Image Perception}, v. 1654, p. 268--278, 1992.",
    "abbey2001": r"ABBEY, C. K.; BARRETT, H. H. Human- and model-observer performance in ramp-spectrum noise with regularization. \textbf{Journal of the Optical Society of America A}, v. 18, n. 3, p. 473--488, 2001.",
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
    "knoll2010": r"KNOLL, G. F. \textbf{Radiation Detection and Measurement}. 4. ed. Hoboken: John Wiley \& Sons, 2010. 860 p.",
    "oostveen2021": r"OOSTVEEN, L. J. et al. Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. \textbf{European Radiology}, v. 31, p. 7412--7421, 2021.",
    "choopani2023": r"CHOOPANI, R. et al. Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. \textbf{Physics in Medicine \& Biology}, v. 68, n. 14, p. 145002, 2023.",
    "iaea_5star_2026": r"INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA). Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. \textbf{European Journal of Radiology}, v. 184, p. 113133, 2026.",
    "rose1948": r"ROSE, A. The sensitivity performance of the human eye on an absolute scale. \textbf{Journal of the Optical Society of America}, v. 38, n. 2, p. 196--208, 1948.",
    "burgess2011": r"BURGESS, A. E. Visual perception studies and observer models in medical imaging. \textbf{Seminars in Nuclear Medicine}, v. 41, n. 6, p. 419--436, 2011."
}

# Assemble reordered thebibliography
bib_entries = []
for k in ordered_keys:
    if k in bib_database:
        bib_entries.append(f"\\bibitem{{{k}}}\n{bib_database[k]}")
    else:
        print(f"Alerta: {k} citado mas ausente no banco!")

for k, content in bib_database.items():
    if k not in ordered_keys:
        bib_entries.append(f"\\bibitem{{{k}}}\n{content}")

bib_block = "\n\n% ==============================================================================\n% ELEMENTOS PÓS-TEXTUAIS (REFERÊNCIAS BIBLIOGRÁFICAS NUMÉRICAS ABNT)\n% ==============================================================================\n\\begin{thebibliography}{99}\n\\addcontentsline{toc}{chapter}{Referências}\n\n" + "\n\n".join(bib_entries) + "\n\n\\end{thebibliography}\n\n\\end{document}\n"

final_tex_content = expanded_tex + bib_block

main_tex_target = os.path.join(output_dir, "main.tex")
with open(main_tex_target, "w", encoding="utf-8") as f:
    f.write(final_tex_content)

# Update build_single_file_overleaf.py as well
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

print("Monografia enriquecida com conexões orgânicas, contextualizações, conceitos básicos e ordenação numérica gerada com sucesso!")
