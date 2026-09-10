---
tipo: fonte
titulo: "Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom"
data_criacao: 2026-08-25
data_atualizacao: 2026-08-25
autores:
  - Joël Greffier
  - Alexa Liogier
  - Maxime Pastor
  - Fabien de Oliveira
  - Quentin Chaine
  - Skander Sammoud
  - Jean Paul Beregi
  - Djamel Dabli
ano: 2026
veiculo: "Diagnostic and Interventional Imaging"
doi: "10.1016/j.diii.2026.01.003"
fonte_bruta: "raw/Deep-learning image reconstruction algorithms for CT A task-based image quality assessment of four CT systems using a phantom.md"
tags:
  - tomografia-computadorizada
  - reconstrucao-deep-learning
  - qualidade-de-imagem
  - dosimetria
  - phantom
fontes_origem: []
---

# Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom

## Resumo Executivo
Este estudo pré-clínico multicêntrico avaliou e comparou o desempenho da qualidade de imagem baseada em tarefas de quatro algoritmos de [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]] (DLR) em comparação com seus respectivos algoritmos de reconstrução iterativa ([[Deep Learning Image Reconstruction (DLR)|IR]]) em tomógrafos de quatro grandes fabricantes: Canon (C-CT), GE Healthcare (G-CT), Philips Healthcare (P-CT) e United Imaging Healthcare (U-CT).

A avaliação foi conduzida utilizando o phantom de qualidade de imagem Mercury v4.0 (31 cm de diâmetro) sob condições de varredura abdominal em três níveis de dose ($CTDI_{vol}$ de 11,0, 6,0 e 1,8 mGy). As métricas analisadas pelo software iQMetrix-CT incluíram a magnitude e textura do ruído via [[Noise Power Spectrum|noise-power-spectrum]] (NPS), a resolução espacial dependente de contraste via [[Task Based Image Quality|Função de Transferência Baseada em Tarefas]] (TTF) e o [[Índice de Detectabilidade|detectability-index]] ($d'$) para duas tarefas clínicas simuladas (lesão de baixo contraste sem contraste e lesão de alto contraste impregnada).

Os resultados demonstram de forma consistente que os algoritmos de DLR superam os algoritmos de IR na redução da magnitude do ruído e na melhoria drástica do índice de detectabilidade ($d'$), enquanto mantêm ou aprimoram a resolução espacial e preservam uma textura de ruído mais natural (frequências espaciais médias mais altas).

---

## Principais Achados & Dados Quantitativos

### 1. Reconstruções e Configurações Testadas
* **Canon (C-CT - Aquilion Prime):** IR: AIDR3D (Standard) vs DLR: AiCE (Body Sharp, DNN treinado com dados de pacientes/Model-based IR).
* **GE Healthcare (G-CT - Revolution CT):** IR: ASiR-V 50% vs DLR: TrueFidelity Medium (DNN treinado com phantom/pacientes/FBP).
* **Philips (P-CT - CT5300):** IR: iDose4 nível 4 vs DLR: Precise Image Smooth (CNN treinado com dados de pacientes/FBP).
* **United Imaging (U-CT - uCT 780):** IR: KARL 3D nível 5 vs DLR: DELTA nível 2 (CNN treinado com dados de pacientes/FBP).

### 2. Magnitude e Textura de Ruído ([[Noise Power Spectrum|NPS]])
* **Magnitude do Ruído:** O DLR reduziu significativamente o ruído em relação ao IR em todos os sistemas e níveis de dose.
  * **GE (G-CT):** Redução média constante de $-21,1 \pm 1,5\%$.
  * **Philips (P-CT):** Redução constante de $-48,4 \pm 0,1\%$.
  * **Canon (C-CT):** Redução de $-43,8\%$ a 1,8 mGy e $-29,9\%$ a 11 mGy.
  * **United Imaging (U-CT):** Maior redução de ruído observada em ultrabaixa dose: $-83,8\%$ a 1,8 mGy e $-59,7\%$ a 11 mGy.
* **Frequência Espacial Média ($f_{av}$):** O DLR deslocou as curvas de NPS para frequências mais altas em C-CT, G-CT e P-CT, resultando em grânulos de ruído mais finos. O U-CT apresentou os maiores valores de $f_{av}$ ($0,353 - 0,358\text{ mm}^{-1}$), indicando textura extremamente fina.

### 3. Resolução Espacial Baseada em Tarefas ([[Task Based Image Quality|TTF]])
* Os valores de $f_{50}$ (frequência espacial em 50% da TTF) foram superiores com DLR em relação ao IR para a maioria dos cenários.
* **Inserto de Iodo (Alto Contraste):** O ganho de $f_{50}$ com DLR foi pronunciado em 11 mGy (ex.: ganho de $+55,1\%$ na GE e $+26,1\%$ na Canon).
* **Inserto de Solid Water (Baixo Contraste):** DLR aumentou o $f_{50}$ na GE ($+26,5\%$ a $+38,6\%$), Philips ($+6,6\%$ a $+31,2\%$) e United Imaging ($+6,1\%$ a $+25,1\%$).

### 4. Índice de Detectabilidade ([[Índice de Detectabilidade|d']])
* O índice $d'$ foi significativamente maior para DLR em todas as marcas e doses:
  * **Canon (C-CT):** Aumento médio de $+77,5 \pm 8,7\%$ em $d'$.
  * **GE (G-CT):** Aumento médio de $+33,7 \pm 5,6\%$ em $d'$.
  * **Philips (P-CT):** Aumento médio de $+112,7 \pm 4,7\%$ em $d'$.
  * **United Imaging (U-CT):** Aumento massivo em ultrabaixa dose (1,8 mGy): $d'$ foi $6,5$ vezes maior com DLR do que com IR ($5,53$ vs $0,86$ para baixo contraste).

---

## Contexto Científico e Implicações Clínicas
Os algoritmos de reconstrução iterativa (IR), embora reduzissem a dose de radiação em relação à projeção retrofiltrada (FBP), introduziram limitações visuais conhecidas como modificação da textura do ruído (aparência borrada, plástico ou moinho de vento/coarse granularity), o que prejudicava a interpretação de lesões de baixo contraste no abdômen.

Este estudo valida que o avanço das redes neurais convolucionais (CNN) e redes neurais profundas (DNN) empregadas pelos quatro grandes fabricantes supera essa limitação. O DLR permite avançar com segurança para protocolos de Tomografia Computadorizada em ultrabaixa dose ($CTDI_{vol} < 2\text{ mGy}$), mantendo o desempenho diagnóstico e a qualidade textural indispensáveis para a prática radiológica abdominal.