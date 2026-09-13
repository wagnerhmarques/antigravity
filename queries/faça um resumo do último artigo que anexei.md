> 📅 **Data:** 2026-09-13 | 🔗 **Conexões:** [[Deep Learning Image Reconstruction (DLR)]], [[Índice de Detectabilidade]], [[Noise Power Spectrum]], [[Task Transfer Function]], [[Tomografia Computadorizada]]

## 1. Visão Geral e Contexto Metodológico

Estudo multicêntrico recente (Greffier et al., 2026) avaliou o desempenho de quatro algoritmos comerciais de [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]] (DLR) em comparação direta com a reconstrução iterativa ([[Reconstrução Iterativa|IR]]) tradicional em tomógrafos de quatro grandes fabricantes (Canon, GE Healthcare, Philips e United Imaging). Utilizando o phantom antropomórfico Mercury v4.0 sob condições de varredura abdominal em três níveis de dose ($CTDI_{\text{vol}}$ de 11,0, 6,0 e 1,8 mGy), a avaliação empregou a metodologia de qualidade de imagem baseada em tarefas ([[Task Based Image Quality|task-based-image-quality]]), mensurando a magnitude e textura do ruído por meio do [[Noise Power Spectrum|noise-power-spectrum]] (NPS), a resolução espacial dependente de contraste via [[Task Transfer Function|task-transfer-function]] (TTF) e o [[Índice de Detectabilidade|detectability-index]] ($d'$).

## 2. Principais Achados Quantitativos por Fabricante

Os resultados demonstram que as arquiteturas baseadas em redes neurais superam expressivamente os algoritmos de reconstrução iterativa, sobretudo em protocolos de ultrabaixa dose:

* **Canon (C-CT / AiCE):** Redução de ruído de $-29,9%$ (11 mGy) a $-43,8%$ (1,8 mGy), com aumento médio de $+77,5%$ no [[Índice de Detectabilidade|detectability-index]] ($d'$).
* **GE Healthcare (G-CT / TrueFidelity):** Redução constante de ruído de $-21,1%$, preservando a estabilidade textural e elevando o $d'$ em média $+33,7%$.
* **Philips (P-CT / Precise Image):** Redução expressiva de ruído de $-48,4%$ e incremento médio de $+112,7%$ em $d'$.
* **United Imaging (U-CT / DELTA):** Maior supressão de ruído em ultrabaixa dose (1,8 mGy), alcançando $-83,8%$ de redução e um aumento de até $6,5$ vezes no $d'$ comparado ao IR ($5,53$ vs $0,86$).

## 3. Impacto na Textura de Ruído e Resolução Espacial

O uso de DLR modificou favoravelmente o espectro de frequências espaciais médias ($f_{\text{av}}$), deslocando o ruído para frequências mais altas e gerando uma granulação mais fina (menos 'plástica' ou borrada que nas gerações anteriores de IR). A resolução espacial baseada em tarefas ([[Task Transfer Function|TTF]]), medida na frequência $f_{50}$, apresentou ganhos expressivos tanto para insertos de alto contraste (iodo) quanto de baixo contraste (*Solid Water*), viabilizando a transição segura para protocolos clínicos com $CTDI_{\text{vol}} < 2\text{ mGy}$ sem perda de acurácia diagnóstica.
