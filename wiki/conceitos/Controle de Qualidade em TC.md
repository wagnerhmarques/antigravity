---
tipo: conceito
aliases: [QC, "Controle de Qualidade", Controle_Qualidade_TC, Controle_de_Qualidade, "Controle de Qualidade em Radiologia", "Controle de Qualidade em Imagem Médica", "Controle de Qualidade (QC) em TC", "Controle de Qualidade em Radiodiagnostico", "Controle de Qualidade e Metrologia em Imagem Médica", "Controle de Qualidade em Física Médica"]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# Controle de Qualidade em TC

## 1. Definição Conceitual e Fundamentação Física
O **Controle de Qualidade em Tomografia Computadorizada (TC)** engloba o conjunto sistemático de procedimentos físicos, operacionais e metrológicos destinados a garantir que os sistemas de imagem operem com o máximo desempenho diagnóstico, acurácia quantitativa e mínima dose de radiação ionizante para o paciente. Do ponto de vista da física médica, o controle de qualidade atua na verificação rigorosa da estabilidade e conformidade de parâmetros fundamentais do equipamento, tais como: precisão do número de Hounsfield (conversão dos coeficientes de atenuação linear), linearidade e uniformidade espacial, resolução espacial de alto contraste, resolução de baixo contraste, ruído radiométrico, artefatos de imagem e dosimetria quantitativa ($CTDI_{vol}$ e $DLP$). A degradação sutil desses parâmetros — provocada por envelhecimento do tubo de raios X\, descalibração dos arranjos de detectores semicondutores, instabilidades no gerador de alta tensão ou falhas nos algoritmos de aquisição — impacta diretamente a detectabilidade de lesões e a reprodutibilidade de biomarcadores de imagem.

## 2. Formulação Matemática e Propriedades
A avaliação quantitativa da qualidade de imagem em TC fundamenta-se em métricas estatísticas e na análise de sistemas lineares. O ruído da imagem, expresso pelo desvio padrão $\sigma$ do Número de Hounsfield ($UH$) em uma região de interesse ($\text{ROI}$) homogênea de um fantoma de água, é modelado por:

$$
\sigma_{UH} = \frac{1000}{\mu_{\text{agua}}} \sigma_{\mu}
$$

onde $\mu_{\text{agua}}$ é o coeficiente de atenuação linear nominal da água e $\sigma_{\mu}$ é o desvio padrão dos coeficientes de atenuação medidos.

A resolução espacial de alto contraste é caracterizada pela **Função de Transferência de Modulação (MTF)**, obtida através da transformada de Fourier da derivada da resposta ao degrau ou da função de espalhamento de ponto ($PSF$)\, dada em uma dimensão por:

$$
\text{MTF}(f) = \left| \int_{-\infty}^{\infty} PSF(x) e^{-i 2 \pi f x} \, dx \right|
$$

Onde $f$ representa a frequência espacial (em lp/cm). Por sua vez, a textura do ruído e a resolução de baixo contraste são avaliadas pelo **Espectro de Potência de Ruído (NPS)**, que descreve a distribuição espacial da variância do ruído no domínio das frequências espaciais $(f_x, f_y)$:

$$
\text{NPS}(f_x, f_y) = \lim_{X, Y \to \infty} \frac{XY}{N_x N_y} \left\langle \left| \sum_{x,y} \left[ \mu(x,y) - \bar{\mu} \right] e^{-i 2\pi (f_x x + f_y y)} \right|^2 \right\rangle
$$

Essas métricas métricas formam a base matemática para a otimização conjunta entre dose e qualidade de imagem, sendo diretamente afetadas por técnicas avançadas de reconstrução.

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de notas e pesquisas do laboratório (USP/FAPESP), o **Controle de Qualidade em TC** atua como o eixo metrológico central que valida as inovações em processamento de imagem e dosimetria. 

Historicamente, protocolos tradicionais de controle de qualidade focavam em métricas analíticas lineares aplicadas sobre imagens obtidas por [[Retroprojeção Filtrada (FBP)|FBP]]. Contudo, com a introdução de métodos avançados como a [[Reconstrução Iterativa|Reconstrução Iterativa]] ([[Reconstrução Iterativa|IR - Reconstrução Iterativa]]) e técnicas baseadas em inteligência artificial — a exemplo de [[Deep Learning Image Reconstruction (DLR)|DLR]], [[U-Net|Redes U-Net]] e arquiteturas discutidas em [[CNNs]] e [[Deep Learning|deep-learning]] —, o paradigma do controle de qualidade evoluiu. Algoritmos baseados em aprendizado profundo podem suprimir o ruído de maneira não linear, alterando a textura da imagem e potencialmente mascarando estruturas de baixo contraste ou introduciendo vieses radiômicos.

Portanto, as rotinas de controle de qualidade conectam-se diretamente à [[Dosimetria em Radiologia|dosimetria-em-radiologia]] e aos conceitos de otimização alinhados à filosofia [[Radioproteção|ALARA]], garantindo que reduções no [[Métricas de Dose em TC|CTDI]] e no [[Métricas de Dose em TC|DLP]] (estudados em [[Níveis de Referência Diagnóstica (DRL)|drl]]) não comprometam a detectabilidade clínica. Ademais, ferramentas avançadas de avaliação de desempenho de imagem, como a [[Task Transfer Function|MTF]] e o [[Noise Power Spectrum|Espectro de Potência de Ruído (NPS)]] (fundamentadas nos trabalhos de [[Donovan Bakalyar|donovan-bakalyar]]), são imprescindíveis para auditar a fidelidade espacial e espectral de sistemas modernos de tomografia frente aos rigorosos padrões exigidos pela [[Fisica Medica]].

## 4. Conexões e Wikilinks
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Reconstrução Iterativa|Reconstrução Iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|DLR]]
- [[Unidades Hounsfield|Unidades Hounsfield]]
- [[Métricas de Dose em TC|CTDI]]
- [[Métricas de Dose em TC|DLP]]
- [[Task Transfer Function|MTF]]
- [[Noise Power Spectrum|Espectro de Potência de Ruído (NPS)]]
- [[Dosimetria em Radiologia|dosimetria-em-radiologia]]
- [[Radioproteção|Radioprotecao]]