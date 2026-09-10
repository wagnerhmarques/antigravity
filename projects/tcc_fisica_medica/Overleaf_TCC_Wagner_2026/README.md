# Monografia de Conclusão de Curso - Overleaf / LaTeX

**Autor:** Wagner H. M.  
**Título:** Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo  
**Instituição:** Instituto de Física da Universidade de São Paulo (IFUSP)  
**Orientador:** Prof. Dr. Paulo Roberto Costa  
**Ano:** 2026  

---

## 🚀 Como importar no Overleaf

1. Acesse sua conta no [Overleaf](https://www.overleaf.com).
2. Clique no botão verde **"New Project"** (Novo Projeto) no canto superior esquerdo.
3. Selecione **"Upload Project"** (Carregar Projeto).
4. Arraste e solte o arquivo compactado `Overleaf_TCC_Wagner_2026.zip` (ou selecione-o no seu computador).
5. O Overleaf criará automaticamente o projeto com toda a árvore de diretórios, figuras e referências.
6. Clique em **"Recompile"** (Recompilar) para gerar o PDF completo da monografia!

---

## 📁 Estrutura do Projeto

```
Overleaf_TCC_Wagner_2026/
├── main.tex                       # Documento mestre com capa, pré-textuais e configuração ABNT
├── references.bib                 # Base de dados bibliográfica BibTeX completa (25 referências)
├── README.md                      # Instruções de uso e compilação
├── figuras/                       # Gráficos científicos e diagramas de alta resolução (300 DPI)
│   ├── fig1_sdt_roc_2afc.png
│   ├── fig2_spectral_metrics.png
│   ├── fig3_cho_cortical_channels.png
│   ├── fig4_dlr_non_linearity_detrending.png
│   ├── fig5_dlmo_pareto_3d.png
│   ├── flow1_tbiq_paradigm.png
│   ├── flow2_comparativo_paradigmas.png
│   ├── flow3_cho_pipeline.png
│   ├── flow4_phantom_hibrido_2afc.png
│   ├── flow5_dlmo_architecture.png
│   └── flow6_software_pipeline.png
└── tex/                           # Capítulos modulares do trabalho
    ├── cap1_introducao.tex
    ├── cap2_fundamentos.tex
    ├── cap3_observadores.tex
    ├── cap4_colapso_linearidade.tex
    ├── cap5_estado_da_arte.tex
    ├── cap6_arquitetura_metrologia.tex
    └── cap7_conclusoes.tex
```

---

## ⚙️ Compatibilidade de Compilação
- **Engine padrão:** pdfLaTeX (ou XeLaTeX / LuaLaTeX)
- **Pacotes principais:** `amsmath`, `amssymb`, `graphicx`, `booktabs`, `tabularx`, `longtable`, `cleveref`, `hyperref`, `titlesec`, `fancyhdr`.
- **Bibliografia:** `references.bib` via BibTeX padrão ou biblatex.
