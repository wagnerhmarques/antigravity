import os

tex_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC/tex"

metodos_tex = r"""\chapter{Metodologia Experimental e Modelagem Computacional}
\label{chap:metodos}

\section{Taxonomia e Comportamento dos Algoritmos de Reconstrução}
\label{sec:taxonomia_reconstrucao}

A evolução algorítmica da tomografia computadorizada compreende quatro gerações principais de processamento numérico de sinogramas, detalhadas na \cref{tab:algoritmos_fabricantes}.

\begin{table}[htbp]
  \centering
  \small
  \caption{Taxonomia dos algoritmos comerciais de reconstrução tomográfica por fabricante.}
  \label{tab:algoritmos_fabricantes}
  \begin{tabularx}{\textwidth}{lXXX}
    \toprule
    \textbf{Fabricante} & \textbf{Reconstrução Iterativa Híbrida (HIR)} & \textbf{Reconstrução Iterativa Baseada em Modelos (MBIR)} & \textbf{Reconstrução por Aprendizado Profundo (DLR)} \\
    \midrule
    \textbf{GE Healthcare} & ASiR / ASiR-V & Veo & \textbf{TrueFidelity} (treinado com FBP de dose plena) \\
    \textbf{Canon Medical} & AIDR 3D / AIDR 3D Enhanced & FIRST & \textbf{AiCE} (\emph{Advanced intelligent Clear-IQ Engine}) \\
    \textbf{Siemens Healthineers} & SAFIRE / ADMIRE & REDUCE & \textbf{Precise Image} / \textbf{Alpha Engine} (PCCT) \\
    \textbf{Philips Healthcare} & iDose4 & IMR (\emph{Iterative Model Reconstruction}) & \textbf{Precise Image} (redes convolucionais profundas) \\
    \bottomrule
  \end{tabularx}
\end{table}

\section{A Quebra da Linearidade e o Efeito Ceroso}
\label{sec:quebra_linearidade}

Em sistemas tomográficos que utilizam reconstruções por aprendizado profundo (DLR) e MBIR, a relação matemática entre as projeções brutas $\mathbf{y}$ e a imagem final $\mathbf{x}$ é estritamente não linear\supercite{greffier2026, debbiche2024}:
\begin{equation}
  \mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}
  \label{eq:nao_linearidade_dlr}
\end{equation}

Essa não-linearidade acarreta fenômenos físicos complexos, evidenciados na \cref{fig:dlr_non_linearity}:
\begin{enumerate}
  \item \textbf{Dependência do Contraste e da Cena:} A resolução espacial da imagem deixa de ser constante, variando dinamicamente de acordo com o contraste do objeto e o nível de ruído local;
  \item \textbf{Não-Estacionariedade Espacial:} O ruído da imagem não possui propriedades estatísticas homogêneas. Em torno de bordas de alto contraste, o algoritmo preserva frequências espaciais elevadas, enquanto em regiões homogêneas de tecidos moles atua com agressiva remoção de ruído;
  \item \textbf{Efeito Ceroso (\emph{Plastic/Waxy Look}):} A excessiva concentração de energia do ruído em frequências baixas gera uma textura artificialmente lisa, que mascara lesões sutis de baixo contraste e reduz a sensibilidade de radiologistas\supercite{toia2023, greffier2026};
  \item \textbf{Colapso dos Modelos Lineares Tradicionais:} O modelo analítico linear NPWE falha em prever a acurácia diagnóstica real sob reconstruções DLR, apresentando dispersão acentuada e baixa correlação ($r \approx 0{,}68$, Painel B da \cref{fig:dlr_non_linearity}).
\end{enumerate}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig4_dlr_non_linearity_detrending.png}
  \caption{Impacto da Não-Linearidade em DLR, Colapso de Modelos Analíticos Lineares e Metodologia de Detrending. (A) Detectabilidade $d'$ em função do nível de dose $\text{CTDI}_{\text{vol}}$ para FBP, HIR e DLR. (B) Dispersão e quebra de correlação linear do modelo NPWE ($r = 0{,}68$) versus a alta correlação do modelo DLMO ancorado na percepção de radiologistas ($r = 0{,}98$). (C) Processo de Detrending Polinomial 2D: remoção do gradiente anatômico macroscópico $P_2(x, y)$ para isolamento do ruído quântico residual $\delta I(x, y)$.}
  \label{fig:dlr_non_linearity}
\end{figure}

\section{Metodologia de Phantoms Híbridos e Detrending Polinomial}
\label{sec:phantoms_hibridos}

Para superar os limites dos simuladores homogêneos tradicionais e viabilizar a avaliação de sistemas DLR em anatomias complexas, adotou-se a metodologia dos \emph{Phantoms} Antropomórficos Híbridos (\cref{fig:phantom_hibrido_flow})\supercite{solomon2020, racine2020}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow4_phantom_hibrido_2afc.png}
  \caption{Metodologia Experimental com Phantoms Físicos Antropomórficos, Inserção Híbrida de Lesões 3D e Plataforma Psicofísica 2AFC.}
  \label{fig:phantom_hibrido_flow}
\end{figure}

O protocolo de \emph{Detrending} Polinomial 2D ajusta, para cada sub-região de interesse $I_k(x, y)$, uma superfície polinomial bidimensional de 2ª ordem $P_2(x, y)$ por mínimos quadrados:
\begin{equation}
  P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy
  \label{eq:polinomio_detrending}
\end{equation}

A matriz de ruído puro residual $\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$ é então submetida a janelamento de Hanning 2D para cálculo do $NPS$ sem vazamento espectral.

Para estimar o erro padrão e os intervalos de confiança de 95\% do índice $d'$ sem impor premissas gaussianas arbitrárias, aplica-se a técnica estatística de reamostragem Bootstrap não-paramétrica com $B = 2000$ replicações com reposição.

\section{Observadores Baseados em Aprendizado Profundo}
\label{sec:dlmo_metodologia}

Para modelar a percepção visual sob regimes não lineares, implementou-se o Observador de Modelo Baseado em Aprendizado Profundo (\emph{Deep Learning Model Observer} --- DLMO), estruturado em uma rede neural profunda com blocos de Auto-Atenção Multi-Cabeça (\emph{Vision Transformer} --- ViT)\supercite{zhou2021, schilder2026}, conforme ilustrado na \cref{fig:dlmo_flow}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow5_dlmo_architecture.png}
  \caption{Arquitetura Neural do Observador por Aprendizado Profundo (DLMO) com Auto-Atenção Multi-Cabeça (Vision Transformer) e Calibração Perceptual.}
  \label{fig:dlmo_flow}
\end{figure}

A estatística de teste não linear $t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$ permite calcular o índice de detectabilidade não linear:
\begin{equation}
  d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}
  \label{eq:dlmo_dprime}
\end{equation}

A calibração perceptual com médicos radiologistas utiliza a função de perda multitarefa:
\begin{equation}
  \mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{classificação}}(y, \hat{y}) + \lambda \, \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2
  \label{eq:perda_multitarefa}
\end{equation}

A transferibilidade do modelo é validada pelo protocolo \emph{Leave-One-Scanner-Out} (LOSO) entre múltiplos tomógrafos.

\section{Formulação da Otimização Multiobjetivo: Fronteira de Pareto Tridimensional}
\label{sec:pareto_metodologia}

O problema de otimização multiobjetivo de protocolos tomográficos é formalizado no espaço tridimensional $(\text{Dose } D, \text{Tempo } T, -\text{Detectabilidade } W)$\supercite{oostveen2021}:
\begin{equation}
  \min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}
  \label{eq:otimizacao_multiobjetivo}
\end{equation}
sujeito a:
\begin{align}
  D(\mathbf{p}) &\le \text{DRL} \label{eq:restricao_dose} \\
  T(\mathbf{p}) &\le T_{\text{máx}} \label{eq:restricao_tempo} \\
  W(\mathbf{p}) &= d'(\mathbf{p}) \ge d'_{\text{mín}} \label{eq:restricao_dprime}
\end{align}

A \cref{fig:pareto_3d} ilustra a superfície da Fronteira de Pareto resultante do mapeamento genético com o algoritmo NSGA-II acoplado ao método TOPSIS.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.98\textwidth]{figuras/fig5_dlmo_pareto_3d.png}
  \caption{Otimização Multiobjetivo em Tomografia Computadorizada e Fronteira de Pareto. (A) Trade-off bidimensional entre Dose e Detectabilidade, ilustrando soluções ótimas na fronteira e protocolos dominados ineficientes. (B) Fronteira de Pareto Tridimensional $(D, T, -W)$, integrando Dose de Radiação ($D$), Tempo Operacional total ($T$) e Detectabilidade Diagnóstica ($W = d'$).}
  \label{fig:pareto_3d}
\end{figure}

\section{Arquitetura do Pipeline Computacional e Protocolos Experimentais}
\label{sec:pipeline_software}

O pipeline de software integrado foi estruturado de forma modular em linguagem Python, conforme esquematizado na \cref{fig:software_pipeline}.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{figuras/flow6_software_pipeline.png}
  \caption{Arquitetura Modular do Software de Metrologia em Tomografia Computadorizada (Pipeline Integrado GDRFM-IFUSP).}
  \label{fig:software_pipeline}
\end{figure}

Os protocolos experimentais seguem os parâmetros normativos do relatório AAPM TG-233\supercite{aapm_tg233_2019}, e os testes psicofísicos com médicos radiologistas atendem aos preceitos éticos do sistema CEP/CONEP, com aplicação de TCLE, estações de trabalho calibradas segundo o padrão DICOM GSDF ($\ge 400 \text{ cd/m}^2$) e iluminação controlada ($< 15 \text{ lux}$).
"""

with open(os.path.join(tex_dir, "metodos.tex"), "w", encoding="utf-8") as f:
    f.write(metodos_tex)

print("Metodos written.")
