import os
import shutil
import zipfile

base_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC"
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "config"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "tex"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "figuras"), exist_ok=True)

# Copy assets to figuras
src_assets = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/assets"
for img in os.listdir(src_assets):
    if img.endswith(".png"):
        shutil.copy2(os.path.join(src_assets, img), os.path.join(base_dir, "figuras", img))

# Copy relatese.sty and config/preamble.tex
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/relatese.sty", os.path.join(base_dir, "relatese.sty"))
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/config/preamble.tex", os.path.join(base_dir, "config", "preamble.tex"))
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/latexmkrc", os.path.join(base_dir, "latexmkrc"))
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/Makefile", os.path.join(base_dir, "Makefile"))

# Build main.tex
main_tex = r"""\documentclass[
  12pt,
  a4paper,
  oneside
]{report}

\input{config/preamble}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% DEFINIÇÃO DE FONTES
\setmainfont{Linux Libertine O}
\setsansfont{Roboto Condensed}
\setmathfont{XITS Math}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% METADADOS DO TCC
\newcommand{\tccautor}{Wagner H. M.}
\newcommand{\tcctitulo}{Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo}
\newcommand{\tccorientador}{Prof. Dr. Paulo Roberto Costa}
\newcommand{\tccano}{2026}
\newcommand{\tccinstituicao}{Universidade de São Paulo}
\newcommand{\tccunidade}{Instituto de Física e Faculdade de Medicina}
\newcommand{\tccdepartamento}{Departamento de Física Nuclear -- Grupo de Dosimetria e Radioproteção em Física Médica (GDRFM)}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\title{\tcctitulo}
\author{\tccautor}
\date{\tccano}

\addbibresource{references.bib}

\begin{document}

\pagenumbering{roman}

\begin{titlepage}
  \centering

  {\large \tccinstituicao\par}
  {\large \tccunidade\par}
  {\large Bacharelado em Física Médica\par}

  \vfill

  {\Large\bfseries
  \tcctitulo
  \par}

  \vspace{2cm}

  {\large \tccautor\par}

  \vfill

  \begin{flushright}
    \begin{minipage}{0.55\textwidth}
      Trabalho de Conclusão de Curso apresentado ao Bacharelado em Física Médica do Instituto de Física e da Faculdade de Medicina da Universidade de São Paulo.

      \vspace{0.75cm}

      Orientador(a): \tccorientador
    \end{minipage}
  \end{flushright}

  \vfill

  {\large São Paulo\\\tccano\par}
\end{titlepage}

\tableofcontents
\clearpage
\listoffigures
\clearpage
\listoftables
\clearpage

\pagenumbering{arabic}

\include{tex/introducao}
\include{tex/objetivos}
\include{tex/fundamentacao}
\include{tex/metodos}
\include{tex/resultados}
\include{tex/discussao}
\include{tex/conclusoes}

\printbibliography[heading=bibintoc,title={Referências}]

\end{document}
"""

with open(os.path.join(base_dir, "main.tex"), "w", encoding="utf-8") as f:
    f.write(main_tex)

print("Main.tex written.")
