import subprocess

# Let's create a minimal test LaTeX file with TikZ PRISMA flowchart to verify it compiles with pdflatex
latex_test = r"""\documentclass{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazilian]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit, calc}

\begin{document}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[
  node distance=0.8cm and 0.8cm,
  box/.style={
    rectangle, rounded corners=3pt, draw=blue!70!black, fill=blue!5, 
    line width=0.8pt, inner sep=6pt, text width=6.2cm, font=\footnotesize, align=left
  },
  exbox/.style={
    rectangle, rounded corners=3pt, draw=red!70!black, fill=red!5, 
    line width=0.8pt, inner sep=6pt, text width=5.2cm, font=\footnotesize, align=left
  },
  phase/.style={
    rectangle, rounded corners=2pt, draw=blue!80!black, fill=blue!15, 
    line width=0.8pt, inner sep=4pt, font=\bfseries\footnotesize, rotate=90, anchor=center
  },
  arrow/.style={-{Stealth[scale=1.0]}, line width=1.0pt, draw=blue!70!black},
  exarrow/.style={-{Stealth[scale=1.0]}, line width=1.0pt, draw=red!70!black}
]

% Phases labels on left
\node[phase] (p1) at (-4.2, 0) {IDENTIFICAÇÃO};
\node[phase] (p2) at (-4.2, -3.2) {TRIAGEM};
\node[phase] (p3) at (-4.2, -6.6) {ELEGIBILIDADE};
\node[phase] (p4) at (-4.2, -10.0) {INCLUSÃO};

% Identification
\node[box] (id1) at (0, 0) {
  \textbf{Registros Identificados nas Bases ($n = 1.206$):}\\
  $\bullet$ PubMed / MEDLINE ($n = 342$)\\
  $\bullet$ Scopus - Elsevier ($n = 298$)\\
  $\bullet$ Web of Science Core ($n = 215$)\\
  $\bullet$ IEEE Xplore ($n = 187$)\\
  $\bullet$ AAPM \& SPIE Digital Library ($n = 164$)
};

\node[exbox, right=1.0cm of id1] (dup) {
  \textbf{Duplicatas Removidas ($n = 418$):}\\
  $\bullet$ Identificação algorítmica e\\
  \phantom{$\bullet$} triagem manual cruzada\\
  $\bullet$ Registros únicos: $n = 788$
};

% Screening
\node[box, below=1.0cm of id1] (screen) {
  \textbf{Registros Triados ($n = 788$):}\\
  $\bullet$ Avaliação de Título e Resumo\\
  $\bullet$ Aplicação preliminar de escopo
};

\node[exbox, right=1.0cm of screen] (ex_screen) {
  \textbf{Registros Excluídos ($n = 632$):}\\
  $\bullet$ Modalidades não tomográficas ($n = 328$)\\
  $\bullet$ Estudos puramente clínicos ($n = 214$)\\
  $\bullet$ Resumos sem texto completo ($n = 90$)
};

% Eligibility
\node[box, below=1.0cm of screen] (elig) {
  \textbf{Texto Completo Recuperado ($n = 156$):}\\
  $\bullet$ Avaliação contra critérios de\\
  \phantom{$\bullet$} elegibilidade formais (Tabela 3.2)
};

\node[exbox, right=1.0cm of elig] (ex_elig) {
  \textbf{Artigos Excluídos na Íntegra ($n = 118$):}\\
  $\bullet$ Ausência de formalismo SDT/Fourier ($n = 64$)\\
  $\bullet$ Coortes ou dados duplicados ($n = 32$)\\
  $\bullet$ Falta de dados dosimétricos ($n = 22$)
};

% Inclusion
\node[box, below=1.0cm of elig] (inc) {
  \textbf{Corpus Incluído na Síntese ($n = 38$):}\\
  $\bullet$ Artigos em periódicos revisados ($n = 26$)\\
  $\bullet$ Relatórios normativos (AAPM/ICRU) ($n = 8$)\\
  $\bullet$ Obras seminais e livros-texto ($n = 4$)
};

% Arrows
\draw[arrow] (id1) -- (screen);
\draw[exarrow] (id1) -- (dup);
\draw[arrow] (screen) -- (elig);
\draw[exarrow] (screen) -- (ex_screen);
\draw[arrow] (elig) -- (inc);
\draw[exarrow] (elig) -- (ex_elig);

\end{tikzpicture}
\caption{Fluxograma PRISMA 2020 de Seleção dos Estudos.}
\label{fig:prisma_flowchart_tikz}
\end{figure}

\end{document}
"""

with open("/Users/user/.gemini/antigravity-ide/scratch/test_tikz.tex", "w") as f:
    f.write(latex_test)

print("Test TikZ file created successfully.")
