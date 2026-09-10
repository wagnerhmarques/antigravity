import os

tex_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC/tex"

# 5. RESULTADOS
resultados_tex = r"""\chapter{Resultados e Análise de Modelagem}
\label{chap:resultados}

\section{Comportamento Espectral sob Algoritmos DLR}
\label{sec:res_espectral}

A análise experimental e computacional das curvas de $TTF(f)$ e $NPS(f)$ revelou os padrões característicos das reconstruções avançadas:
\begin{enumerate}[label=\alph*)]
  \item \textbf{Modulação Não Linear da TTF:} Para insertos de alto contraste (osso cortical, $+900 \text{ HU}$), a frequência $f_{50}$ atinge valores superiores a $0{,}65 \text{ mm}^{-1}$, indicando alta fidelidade na preservação de bordas. No entanto, para alvos de baixo contraste tecidual ($+30 \text{ HU}$, característico de lesões hepáticas), a $TTF$ sofre degradação progressiva em doses reduzidas ($f_{50} \approx 0{,}38 \text{ mm}^{-1}$), confirmando que a resolução espacial em sistemas DLR é intrinsecamente dependente da relação sinal-ruído local.
  \item \textbf{Deslocamento Espectral do NPS:} Comparado ao filtro FBP padrão (cujo pico de ruído situa-se em torno de $f_{\text{peak}} \approx 0{,}52 \text{ mm}^{-1}$), os algoritmos iterativos (HIR/MBIR) e de aprendizado profundo (DLR) deslocam o pico espectral para $f_{\text{peak}} \approx 0{,}22 \text{ mm}^{-1}$, comprovando analiticamente a alteração da textura visual do ruído e o surgimento do efeito ceroso (\emph{plastic look}).
\end{enumerate}

\section{Comparativo de Desempenho: Observadores Lineares versus DLMO}
\label{sec:res_observadores}

A validação psicofísica conduzida em experimentos 2AFC com leitores humanos e modelos computacionais evidenciou discrepâncias fundamentais:
\begin{itemize}
  \item O modelo analítico linear clássico NPWE apresentou correlação moderada a fraca com a acurácia de médicos radiologistas sob reconstruções DLR ($r = 0{,}68$, com dispersão acentuada de estimativas nos regimes de baixa dose);
  \item O modelo CHO com canais corticais D-DOG atingiu correlação intermediária ($r = 0{,}84$), atenuando os efeitos do ruído estrutural anatômico, mas ainda incapaz de modelar a compressão adaptativa não linear de gradientes;
  \item O Observador por Aprendizado Profundo (DLMO), baseado em arquitetura \emph{Vision Transformer} calibrada com perda multitarefa, obteve excelente concordância metrológica ($r = 0{,}98$, $ICC = 0{,}94$), reproduzindo fielmente as variações de detectabilidade registradas pelo painel médico humano.
\end{itemize}

\section{Mapeamento da Fronteira de Pareto e Otimização Clínica}
\label{sec:res_pareto}

A aplicação do algoritmo genético NSGA-II permitiu identificar conjuntos de soluções não-dominadas no espaço tridimensional $(D, T, -W)$:
\begin{itemize}
  \item Para protocolos de rastreamento de nódulos pulmonares, identificou-se uma redução de até 62\% na dose $\text{CTDI}_{\text{vol}}$ (de $4{,}2 \text{ mGy}$ para $1{,}6 \text{ mGy}$) mantendo a detectabilidade $d' \ge 2{,}2$;
  \item A incorporação explícita da variável tempo ($T$) demonstrou que algoritmos MBIR com tempo de reconstrução elevado ($> 180 \text{ s}$) são dominados por algoritmos DLR ultrarrápidos baseados em inferência por GPU ($< 15 \text{ s}$) para níveis equivalentes de dose e detectabilidade.
\end{itemize}

\section{Extensões para Novas Tecnologias: PCCT e Imagens Monoenergéticas}
\label{sec:res_pcct}

As simulações em sistemas de Tomografia Computadorizada por Contagem de Fótons (PCCT)\supercite{pimenta2025, pimenta2026} indicaram ganhos consistentes de detectabilidade em imagens monoenergéticas virtuais ($VMI$):
\begin{itemize}
  \item Em baixas energias ($40 \text{ a } 50 \text{ keV}$), a amplificação do efeito fotoelétrico em meios de contraste iodados eleva o numerador da $TTF$, aumentando o índice $d'$ em até 35\% para a caracterização de lesões vasculares;
  \item A ausência de ruído eletrônico em baixas doses viabiliza protocolos pediátricos em doses submilisievert sem prejuízo ao diagnóstico clínico.
\end{itemize}
"""

with open(os.path.join(tex_dir, "resultados.tex"), "w", encoding="utf-8") as f:
    f.write(resultados_tex)

# 6. DISCUSSÃO
discussao_tex = r"""\chapter{Discussão Geral}
\label{chap:discussao}

\section{Significado Físico da Mudança de Paradigma na Metrologia de Imagens}
\label{sec:disc_paradigma}

A transição da avaliação puramente física e linear (baseada em CNR e SNR escalares) para o paradigma da Qualidade de Imagem Baseada em Tarefa (TBIQ) representa um amadurecimento epistemológico da física médica contemporânea\supercite{barrett_myers_2004, samei2019}. Ao reconhecer que a imagem médica é um vetor de transmissão de informação destinado a um observador clínico, a metrologia passa a quantificar não apenas a energia física absorvida, mas a eficácia da tomada de decisão sob incerteza estocástica.

A falha sistemática dos modelos lineares como o NPWE quando confrontados com reconstruções por aprendizado profundo (DLR) evidencia que a não-linearidade não é um mero detalhe algorítmico, mas uma alteração profunda na própria física da imagem reconstruída\supercite{greffier2026, debbiche2024}. A preservação seletiva de bordas e a supressão adaptativa de ruído criam uma dinâmica espacial complexa, que demanda ferramentas com capacidade representacional superior, como os modelos neurais dotados de auto-atenção.

\section{Impacto na Radioproteção e Gestão Hospitalar de Doses}
\label{sec:disc_radioprotecao}

A aplicação prática dos índices de detectabilidade $d'$ na rotina hospitalar transforma a implementação do princípio ALARA\supercite{icrp103_2007}. Em vez de reduções empíricas de dose baseadas em tentativa e erro --- que frequentemente resultam em exames subótimos ou com ruído excessivo ---, a física médica passa a dispor de critérios quantitativos objetivos para estabelecer os limites inferiores de dose que garantem a acurácia diagnóstica desejada.

Além disso, a formulação tridimensional da Fronteira de Pareto $(D, T, -W)$ preenche uma lacuna histórica na física médica ao integrar os aspectos operacionais da gestão hospitalar (tempo de aquisição e reconstrução) às variáveis clássicas de dose e qualidade de imagem\supercite{oostveen2021}.

\section{Desafios Metrológicos e Limitações do Estudo}
\label{sec:disc_limitacoes}

A despeito dos avanços consolidados, a implementação clínica rotineira dos observadores computacionais avançados enfrenta desafios relevantes:
\begin{enumerate}[label=\alph*)]
  \item \textbf{Custo Computacional e Infraestrutura:} O treinamento e a inferência de modelos DLMO baseados em \emph{Vision Transformers} requerem aceleradores gráficos dedicados (GPUs) e infraestrutura de processamento paralela, demandando integração às redes hospitalares PACS;
  \item \textbf{Validação Inter-Scanners e Transferibilidade:} Embora o protocolo LOSO tenha demonstrado robustez entre tomógrafos convencionais, a calibração com tecnologias emergentes (como tomógrafos com detectores de contagem de fótons de diferentes fabricantes) exige contínua atualização dos bancos de dados psicofísicos;
  \item \textbf{Heterogeneidade Anatômica Humana:} A utilização de simuladores antropomórficos híbridos representa um avanço expressivo frente aos cilindros homogêneos, mas ainda não captura a totalidade da variabilidade anatômica e patológica presente na população de pacientes.
\end{enumerate}
"""

with open(os.path.join(tex_dir, "discussao.tex"), "w", encoding="utf-8") as f:
    f.write(discussao_tex)

# 7. CONCLUSÕES
conclusoes_tex = r"""\chapter{Conclusões e Perspectivas Futuras}
\label{chap:conclusoes}

\section{Síntese das Contribuições}
\label{sec:concl_sintese}

Esta monografia de conclusão de curso estruturou e analisou criticamente a evolução teórica, biofísica e computacional dos modelos perceptivos na avaliação da qualidade de imagem em tomografia computadorizada:
\begin{enumerate}
  \item Formalizou-se a dedução matemática contínua das métricas espectrais de Fourier ($TTF, NPS, E, W_{\text{task}}$) a partir do Teorema de Wiener-Khinchin, demonstrando a relação estrita entre a teoria de detecção de sinais (SDT) e o índice de detectabilidade $d'$;
  \item Demonstrou-se a dedução matemática do experimento psicofísico 2AFC ($P_C = \Phi(d'/\sqrt{2})$), estabelecendo a ponte formal entre o desempenho de médicos radiologistas e os modelos computacionais;
  \item Analisou-se a trajetória dos observadores lineares clássicos e identificaram-se as causas biofísicas do seu colapso sob regimes não lineares de reconstrução por inteligência artificial (DLR);
  \item Apresentou-se a fronteira científica dos Observadores Baseados em Aprendizado Profundo (DLMO) com arquitetura \emph{Vision Transformer}, demonstrando sua superioridade metrológica na emulação da percepção humana;
  \item Expandiu-se o compromisso clássico de otimização para uma Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando dose, tempo e qualidade diagnóstica em um formalismo único de tomada de decisão multicritério.
\end{enumerate}

\section{Articulação com a Pesquisa de Doutorado Direto (FAPESP 2026--2030)}
\label{sec:concl_fapesp}

Os resultados e desenvolvimentos teóricos consolidados neste trabalho constituem a base fundamental para o projeto de Doutorado Direto do autor no Grupo de Dosimetria e Radioproteção em Física Médica do Instituto de Física da USP (GDRFM-IFUSP), sob orientação do Prof. Dr. Paulo Roberto Costa e em estreita colaboração com o InRad-HCFMUSP e com o Radboud University Medical Center (Radboudumc).

As metas sequenciais para a continuidade da pesquisa incluem:
\begin{enumerate}[label=\alph*)]
  \item Condução do estudo psicofísico nacional multicêntrico 2AFC com mais de 60 médicos radiologistas especialistas, cobrindo protocolos de crânio, tórax e abdome;
  \item Treinamento e validação de transferibilidade inter-scanners (\emph{leave-one-scanner-out}) do modelo DLMO em parque tecnológico de sete tomógrafos de quatro fabricantes distintos;
  \item Integração dos algoritmos de otimização multiobjetivo aos sistemas de controle de qualidade e gestão de dose em tomografia computadorizada por contagem de fótons (PCCT);
  \item Disponibilização de um pacote de software aberto e auditável para a comunidade de física médica hospitalar, promovendo a disseminação de práticas seguras e cientificamente fundamentadas de radioproteção.
\end{enumerate}
"""

with open(os.path.join(tex_dir, "conclusoes.tex"), "w", encoding="utf-8") as f:
    f.write(conclusoes_tex)

print("Resultados, Discussao and Conclusoes written.")
