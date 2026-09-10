import os

tex_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC/tex"

# 1. INTRODUÇÃO
introducao_tex = r"""\chapter{Introdução}
\label{chap:introducao}

\section{O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico}
\label{sec:dilema_dose}

A Tomografia Computadorizada (TC) revolucionou a medicina diagnóstica desde a sua introdução clínica na década de 1970 por Godfrey Hounsfield. Ao permitir a reconstrução tridimensional de secções transversais do corpo humano com elevada diferenciação de densidades de tecidos moles e resolução espacial submilimétrica, a TC consolidou-se como a modalidade de escolha para o estadiamento oncológico, o planejamento cirúrgico e radioterápico, a avaliação de traumas agudos e o rastreamento precoce de doenças pulmonares e vasculares\supercite{mccollough2026, seeram2015, bushberg2020}.

Contudo, o princípio físico basilar da formação da imagem tomográfica reside na atenuação exponencial de feixes de raios X transmitidos através do paciente\supercite{attix1986}. A absorção e o espalhamento dessa radiação ionizante no tecido biológico provocam ionizações atômicas e quebras de ligações moleculares em estruturas de DNA celular, associando-se a riscos estocásticos de carcinogênese a longo prazo\supercite{icrp103_2007}. Consequentemente, embora represente apenas de 10\% a 15\% do total de procedimentos radiológicos executados mundialmente, a TC responde por aproximadamente 65\% a 70\% de toda a dose coletiva de radiação ionizante de origem médica absorvida pela população humana\supercite{iaea_5star_2026, mccollough2026}.

Essa assimetria impõe a aplicação rigorosa do princípio fundamental da radioproteção: o princípio ALARA (\emph{As Low As Reasonably Achievable})\supercite{icrp103_2007, anvisa_rdc611_2022, anvisa_in93_2021}. De acordo com essa diretriz, os protocolos tomográficos devem ser continuamente otimizados para operar na menor dose de radiação compatível com o objetivo diagnóstico desejado.

Para compreender a dificuldade física dessa otimização, é necessário analisar como os fótons de raios X se comportam estatisticamente. A detecção de fótons é um processo estocástico regido pela distribuição de Poisson\supercite{knoll2010}. Em termos intuitivos, quanto menor o número de fótons emitidos pelo tubo de raios X, maiores são as flutuações estatísticas percentuais registradas pelos detectores. No domínio da imagem reconstruída, essa incerteza manifesta-se visualmente sob a forma de ruído quântico.

A relação matemática fundamental entre o desvio padrão do ruído ($\sigma_{\text{ruído}}$), o número de fótons detectados ($N_{\text{fótons}}$) e o índice de dose volumétrico ($\text{CTDI}_{\text{vol}}$) é expressa por:
\begin{equation}
  \sigma_{\text{ruído}} \propto \frac{1}{\sqrt{N_{\text{fótons}}}} \propto \frac{1}{\sqrt{\text{CTDI}_{\text{vol}}}}
  \label{eq:ruido_dose}
\end{equation}

Em termos práticos, se um físico médico tentar reduzir a dose de radiação pela metade sem alterar a tecnologia do tomógrafo ou o algoritmo de reconstrução, o nível de ruído da imagem aumentará automaticamente em um fator de $\sqrt{2} \approx 1{,}41$ (ou seja, cerca de 41\% de acréscimo de ruído). Esse ruído adicional sobrepõe-se às estruturas anatômicas sutis, reduzindo a capacidade do radiologista de identificar lesões de baixo contraste, como metástases hepáticas incipientes ou pequenos nódulos pulmonares em vidro fosco.

\section{Limitações Estruturais das Métricas Físicas Globais Tradicionais}
\label{sec:limitacoes_metricas}

Durante quatro décadas, o controle de qualidade e a avaliação de desempenho de tomógrafos hospitalares apoiaram-se em grandezas físicas escalares derivadas da teoria de sistemas lineares e invariantes no espaço\supercite{barrett_myers_2004}:
\begin{enumerate}[label=\alph*)]
  \item Desvio padrão do número CT ($\sigma_{\text{HU}}$), mensurado no centro de um simulador geométrico homogêneo de água;
  \item Relação Sinal-Ruído (SNR) e Relação Contraste-Ruído (CNR), calculadas classicamente pela diferença de médias entre o alvo e o fundo dividida pelo desvio padrão:
  \begin{equation}
    \text{CNR} = \frac{|\overline{\mu}_{\text{alvo}} - \overline{\mu}_{\text{fundo}}|}{\sigma_{\text{fundo}}}
    \label{eq:cnr_classica}
  \end{equation}
  \item Função de Transferência de Modulação (MTF), obtida a partir da resposta ao impulso de fios finos metálicos ou micro-esferas de alta densidade suspensas em meio uniforme.
\end{enumerate}

Embora essas métricas fossem adequadas para caracterizar o algoritmo analítico clássico da Retroprojeção Filtrada (FBP) --- que atua de forma estritamente linear e produz ruído gaussiano espacialmente estacionário ---, elas falham de maneira substancial na avaliação dos tomógrafos modernos\supercite{aapm_tg233_2019, samei2019}.

Essa falha decorre do fato de que os equipamentos contemporâneos utilizam algoritmos não lineares, como as reconstruções iterativas e as redes neurais profundas. A CNR convencional possui limitações conceituais severas:
\begin{itemize}
  \item Primeiramente, a CNR avalia apenas a dispersão pontual dos valores em pixels isolados, sendo completamente cega para a textura espacial do ruído. Duas imagens podem apresentar exatamente o mesmo valor numérico de $\sigma_{\text{fundo}}$ e a mesma diferença de contraste, mas uma conter ruído fino e granular enquanto a outra apresenta manchas borradas de baixa frequência. Para a percepção do olho humano, a facilidade de encontrar uma lesão em cada uma dessas imagens é completamente distinta.
  \item Em segundo lugar, a aplicação de filtros matemáticos de suavização espacial reduz o desvio padrão do fundo, inflando artificialmente o valor da CNR, ao mesmo tempo em que apaga bordas anatômicas e diminui a nitidez de detalhes diagnósticos finos.
  \item Por fim, a CNR não incorpora nenhuma propriedade fisiológica do sistema visual humano, tratando a tomada de decisão médica como se fosse uma simples subtração aritmética de intensidades.
\end{itemize}

\section{A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa}
\label{sec:mudanca_paradigma}

Diante dessas inconsistências, órgãos normativos internacionais, como o relatório AAPM TG-233\supercite{aapm_tg233_2019} e o ICRU Report 54\supercite{icru54_1996}, formalizaram a transição para o paradigma da Qualidade de Imagem Baseada em Tarefa (\emph{Task-Based Image Quality} --- TBIQ).

No escopo da TBIQ, a qualidade da imagem deixa de ser tratada como um atributo físico isolado e passa a ser definida como a eficácia estatística com que um observador específico consegue responder a uma pergunta clínica sobre a imagem\supercite{barrett_myers_2004, samei2019}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow2_comparativo_paradigmas.png}
  \caption{Comparativo Estrutural entre o Paradigma Físico Clássico (Linear/Escalar) e o Paradigma Contemporâneo Baseado em Tarefa (TBIQ).}
  \label{fig:comparativo_paradigmas}
\end{figure}

O pilar quantitativo da TBIQ é o Índice de Detectabilidade ($d'$), que integra de forma coerente as grandezas físicas do sistema tomográfico com as propriedades da visão humana, conforme esquematizado na \cref{fig:pilares_tbiq}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.90\textwidth]{figuras/flow1_tbiq_paradigm.png}
  \caption{Pilares Fundamentais da Avaliação de Qualidade de Imagem Baseada em Tarefa (TBIQ), articulando Resolução ($TTF$), Ruído ($NPS$) e Fisiologia Visual ($E(f)$) no Índice de Detectabilidade ($d'$).}
  \label{fig:pilares_tbiq}
\end{figure}
"""

with open(os.path.join(tex_dir, "introducao.tex"), "w", encoding="utf-8") as f:
    f.write(introducao_tex)

# 2. OBJETIVOS
objetivos_tex = r"""\chapter{Objetivos}
\label{chap:objetivos}

\section{Objetivo Geral}
\label{sec:obj_geral}

Estruturar, deduzir matematicamente e analisar criticamente a evolução dos modelos perceptivos e computacionais de avaliação de qualidade de imagem baseada em tarefas em Tomografia Computadorizada, partindo das formulações lineares clássicas até os observadores de aprendizado profundo contemporâneos e sua aplicação na otimização multiobjetivo de protocolos clínicos.

\section{Objetivos Específicos}
\label{sec:obj_especificos}

Para atingir a meta geral proposta, estabeleceram-se os seguintes objetivos específicos:
\begin{enumerate}[label=\alph*)]
  \item Formalizar as deduções matemáticas da Teoria de Detecção de Sinais nos domínios espacial e de frequências, demonstrando a diagonalização da matriz de covariância via Teorema de Wiener-Khinchin;
  \item Analisar a trajetória dos observadores lineares (Observador Ideal, NPW, NPWE, HO e CHO), explicitando as aproximações do córtex visual e os métodos psicofísicos de validação humana (2AFC e MRMC);
  \item Investigar o colapso da linearidade em sistemas DLR, demonstrando o surgimento da não-estacionariedade e justificando a necessidade de simuladores antropomórficos híbridos e técnicas de \emph{detrending};
  \item Examinar a fronteira científica dos Observadores Baseados em Aprendizado Profundo (DLMO), sua calibração com radiologistas e validação de transferibilidade inter-scanners (\emph{leave-one-scanner-out});
  \item Formular o problema de Otimização Multiobjetivo em TC através da Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose ($D$), tempo operacional ($T$) e detectabilidade ($W$).
\end{enumerate}

\section{Justificativa e Aderência ao Contexto Hospitalar}
\label{sec:justificativa}

A física médica desempenha um papel ético e técnico indispensável na interface entre o avanço tecnológico e a proteção radiológica do paciente. A introdução acelerada de sistemas de reconstrução por inteligência artificial nos hospitais brasileiros --- particularmente no Instituto de Radiologia do Hospital das Clínicas (InRad-HCFMUSP) --- demanda instrumentos metrológicos de validação independentes dos fabricantes.

A presente monografia estabelece a base teórica e matemática necessária para o desenvolvimento de rotinas automatizadas de garantia de qualidade, apoiando diretamente a pesquisa de Doutorado Direto do autor no Grupo de Dosimetria e Radioproteção em Física Médica do IFUSP.
"""

with open(os.path.join(tex_dir, "objetivos.tex"), "w", encoding="utf-8") as f:
    f.write(objetivos_tex)

print("Introducao and Objetivos written.")
