---tipo: conceito
titulo: "Avaliação de Qualidade de Imagem Baseada em Tarefa em TC"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
tags:
  - qualidade-de-imagem
  - ttf
  - dosimetria
  - tomografia-computadorizada
fontes_origem:
  - "[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]"
aliases: [task-based-image-quality, tbiq, TBIQ, "qualidade de imagem baseada em tarefas", "task based image quality"]
---

# Avaliação de Qualidade de Imagem Baseada em Tarefa em TC

A **Avaliação de Qualidade de Imagem Baseada em Tarefas** (*Task-based Image Quality Assessment*) é o paradigma moderno da física médica para caracterizar o desempenho de sistemas de Tomografia Computadorizada (TC), superando métricas tradicionais objetivas lineares (como a SNR simples e a MTF convencional).

Em sistemas não lineares — tais como os que utilizam [[Deep Learning Image Reconstruction (DLR)|reconstrução iterativa (IR) e reconstrução por deep learning (DLR)]] —, a resolução espacial e o ruído dependem diretamente do nível de dose (exposição) e do contraste do objeto/tecido examinado.

## Componentes Fundamentais

1. **[[Noise Power Spectrum|Espectro de Potência do Ruído (NPS)]]:** Avalia a magnitude e a textura espacial do ruído na imagem.
2. **Função de Transferência Baseada em Tarefas (TTF):** Mede a resolução espacial do sistema como uma função do contraste da estrutura em estudo ($TTF(f)$). Utiliza a técnica da borda circular (*circular edge technique*) em insertos de diferentes atenuadores (ex.: Iodo para alto contraste e Solid Water® para baixo contraste).
   * O valor de $f_{50}$ representa a frequência espacial na qual a resposta do sistema cai para 50% de sua amplitude original.
3. **[[Índice de Detectabilidade|Índice de Detectabilidade (d')]]:** Combina a resposta do sistema (TTF), o ruído (NPS) e o modelo visual humano/observador matemático para quantificar quão bem uma tarefa clínica específica (ex.: detectar um nódulo hepático de 10 mm e 85 HU) pode ser realizada.

## Relevância na Era do DLR
Estudos como o de [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]] demonstram que a análise baseada em tarefas é indispensável para comprovar que algoritmos de DLR mantêm ou elevam a resolução espacial ($f_{50}$) em condições de ultrabaixa dose, ao contrário de filtros de suavização convencionais.