---
aliases:
  - contrast-to-noise-ratio
  - Relação Contraste-Ruído
  - CNR
categoria: Qualidade de Imagem
---

# Contrast-to-Noise Ratio (CNR)

## 1. Definição Conceitual e Fundamentação Física

O **Contrast-to-Noise Ratio (CNR)** — ou Relação Contraste-Ruído — é uma métrica quantitativa objetiva fundamental em física médica e tomografia computadorizada (TC) utilizada para avaliar a visibilidade de uma estrutura de interesse (lesão, órgão ou artefato anatômico) em relação ao fundo circundante, ponderando este contraste pelas flutuações estatísticas do ruído inerentes ao sistema de aquisição.

Diferentemente da relação sinal-ruído (SNR), que mede a intensidade do sinal global em relação ao ruído de fundo, o CNR isola especificamente a capacidade de diferenciar dois tecidos com propriedades de atenuação radiológica distintas na presença de ruído quântico e eletrônico.

## 2. Formulação Matemática

Matematicamente, o CNR é definido pela diferença entre os valores médios de número de Hounsfield (HU) ou intensidade de sinal ($S$) da região de interesse (ROI) da estrutura alvo e do tecido de fundo, normalizada pelo desvio padrão do ruído ($\sigma$) medido no fundo ou na região de referência:

$$
\\text{CNR} = \\frac{|S_{\\text{alvo}} - S_{\\text{fundo}}|}{\sigma_{\\text{fundo}}}
$$

Em sistemas avançados de imagem e reconstruções não-lineares, a propagação do ruído deixa de ser estacionária. Nesses cenários, a formulação espacial local pode ser expressa integrando as flutuações locais de intensidade através de operadores diferenciais ou em domínios de frequência, considerando a modulação espacial introduzida por filtros adaptativos:

$$
\\text{CNR}(x, y) = \\frac{\left| \Delta \mu(x, y) \
ight|}{\sqrt{\iint \\text{NPS}(u, v) \, du \, dv}}
$$

Onde $\Delta \mu$ representa a variação do coeficiente de atenuação linear entre as regiões, e $\\text{NPS}(u, v)$ é o [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]] espacialmente dependente.

## 3. Aplicações e Contexto no Acervo de Pesquisa

No acervo de pesquisas do laboratório (USP/FAPESP), o **contrast-to-noise-ratio** é frequentemente citado como uma métrica tradicional baseada puramente em pixels que, embora útil historicamente, apresenta limitações severas na era moderna dos tomógrafos computadorizados.

Com a introdução de algoritmos de [[Reconstrução Iterativa|reconstrucao-iterativa]], [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]] e tecnologias de contagem fótons ([[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]), o ruído nas imagens de TC tornou-se não-estacionário, texturizado e dependente dadose. Consequentemente, o CNR isolado demonstrou-se inadequado e falha em prever a acurácia diagnóstica humana ou o desempenho de observadores computacionais.

Atualmente, a literatura do acervo aponta para a superação do CNR em favor de figuras de mérito orientadas a tarefas clínicas, as quais combinam a resolução espacial e a textura do ruído através de ferramentas como a [[task-transfer-function-ttf]] e o [[indice-de-detectabilidade-d'-ideal-pre-whitening]], permitindo uma avaliação otimizada que reflete com fidelidade o desempenho diagnóstico real.

## 4. Conexões com Outros Conceitos

- [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]]
- [[task-transfer-function-ttf]]
- [[indice-de-detectabilidade-d'-ideal-pre-whitening]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]