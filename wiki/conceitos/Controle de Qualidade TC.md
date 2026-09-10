---
tipo: conceito
aliases: [Controle_de_Qualidade_TC]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# Controle_de_Qualidade_TC

## 1. Definição Conceitual e Fundamentação Física
O Controle de Qualidade em Tomografia Computadorizada ($\text{CQ-TC}$) engloba o conjunto sistemático de procedimentos físicos, metrológicos e operacionais destinados a garantir que o sistema imageador opere com o máximo desempenho diagnóstico, segurança radiológica e conformidade regulatória. Do ponto de vista da física médica, o $\text{CQ-TC}$ monitora a estabilidade e a acurácia de parâmetros críticos que governam a formação da imagem digital e a dosimetria. Estes incluem a constância do número de Hounsfield ($\text{UH}$), a linearidade e o contraste de atenuação, a resolução espacial de alto contraste (avaliada por meio da [[Task Transfer Function|MTF]]), a resolução de baixo contraste, a uniformidade do ruído, bem como a precisão e exatidão dos índices dosimétricos como o $\text{CTDI}_{vol}$ e o DLP. 

A garantia da qualidade mitiga artefatos de imagem, previne flutuações na calibração do feixe de raios X decorrentes do envelhecimento do tubo ou instabilidades do gerador, e assegura que algoritmos avançados de pós-processamento — como a [[Reconstrução Iterativa|Reconstrucao_Iterativa]] e a [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]] — recebam dados brutos (sinograma) com estabilidade estatística e geométrica previsíveis.

## 2. Formulação Matemática e Propriedades
A avaliação quantitativa no $\text{CQ-TC}$ baseia-se em métricas estatísticas e determinísticas extraídas de imagens de fantomas padronizados. 

A acurácia do número de Hounsfield para um material de referência (como a água) é expressa por:

$$
\text{UH} = 1000 \times \frac{\mu - \mu_{\text{agua}}}{\mu_{\text{agua}} - \mu_{\text{ar}}}
$$

onde $\mu$, $\mu_{\text{agua}}$ e $\mu_{\text{ar}}$ representam os coeficientes de atenuação linear efetivos do voxel avaliado\, da água pura e do ar, respectivamente.

O ruído da imagem ($\sigma$), parâmetro fundamental de desempenho avaliado rotineiramente, é calculado como o desvio padrão dos valores de pixels em uma região de interesse ($\text{ROI}$) central posicionada sobre um meio homogêneo (fantoma de água):

$$
\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} \left( \text{UH}_i - \overline{\text{UH}} \right)^2}
$$

onde $N$ é o número total de pixels na $\text{ROI}$ e $\overline{\text{UH}}$ é o valor médio de Hounsfield na região.

A uniformidade espacial da imagem ($\mathcal{U}$) ao longo do plano axial é quantificada pelas variações do número de Hounsfield entre o centro e a periferia:

$$
\mathcal{U} = \left| \overline{\text{UH}}_{\text{centro}} - \overline{\text{UH}}_{\text{periferia}} \right|
$$

A dosimetria associada ao controle de qualidade baseia-se no Índice de Dose em Tomografia Computadorizada ($\text{CTDI}$), integrado ao longo do eixo z para varreduras helicoidais considerando o fator de pitch ($P$):

$$
\text{CTDI}_{\text{vol}} = \frac{1}{P} \cdot \text{CTDI}_{100}
$$

onde $\text{CTDI}_{100}$ representa a dose integral normalizada medida com uma câmara de ionização tipo lápis de $100\text{ mm}$ de comprimento em fantomas acrílicos padronizados (cabeça de $16\text{ cm}$ e corpo de $32\text{ cm}$ de diâmetro).

## 3. Contexto no Acervo do Pesquisador & Aplicações
No ecossistema de pesquisas do laboratório (USP/FAPESP), o [[Controle de Qualidade em TC|Controle_de_Qualidade_TC]] atua como o alicerce metrológico indispensável que valida tanto os modelos físicos prospectivos quanto os dados orientados a aprendizado de máquina. 

Conforme evidenciado no documento [[Dependencias Eixo1|dependencias_eixo1]], o $\text{CQ-TC}$ está profundamente acoplado às cadeias de processamento que envolvem a [[Dosimetria em TC|Dosimetria_em_TC]], a modulação de dose por [[Filtragem Bowtie|Filtro Bow-Tie]] e a otimização de parâmetros operacionais como o [[Pitch Helicoidal|Pitch Helicoidal]]. Variações não controladas no desempenho do scanner invalidam a constância estatística exigida por algoritmos de [[Reconstrução Iterativa|Reconstrucao_Iterativa]] e causam desvios nos pesos sinogramas processados por redes neurais em [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]], além de comprometerem a integridade da resposta espacial medida pela [[Task Transfer Function|MTF]].

Adicionalmente, no contexto do documento [[Dataset|dataset_]], a padronização e o rigor do $\text{CQ-TC}$ garantem que os dados quantitativos extraídos para a [[Radiomica|Radiomica]] e análises via [[Transformada de Radon|Transformada de Radon]] e [[Retroprojeção Filtrada (FBP)|FBP]] não sofram de vieses instrumentais. Variações na calibração de [[Unidades Hounsfield|Unidades_Hounsfield]] decorrentes de falhas no controle de qualidade introduziram artefatos de textura que mascaram bioindicadores radiômicos legítimos.

## 4. Conexões e Wikilinks
- [[Métricas de Dose em TC|CTDI]]
- [[Pitch Helicoidal|Pitch Helicoidal]]
- [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]]
- [[Dosimetria em TC|Dosimetria_em_TC]]
- [[Filtragem Bowtie|Filtro Bow-Tie]]
- [[Task Transfer Function|MTF]]
- [[Unidades Hounsfield|Unidades_Hounsfield]]
- [[Radiomica|Radiomica]]
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Transformada de Radon|Transformada de Radon]]