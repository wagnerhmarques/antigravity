---
tipo: conceito
aliases: [Qualidade de Imagem em TC]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# Qualidade de Imagem em TC

## 1. Definição Conceitual e Fundamentação Física
A **Qualidade de Imagem em Tomografia Computadorizada (TC)** é um construto multidimensional que dita a capacidade diagnóstica de um exame, ponderando a fidelidade geométrica, radiométrica e temporal com a restrição fundamental da otimização radiológica (princípio ALARA). Fisicamente, a qualidade de imagem em TC não pode ser reduzida a uma única métrica visual; ela emerge da interação estocástica e determinística entre a geometria do feixe de raios X, a eficiência quântica de detecção, os algoritmos de processamento de sinal e a reconstrução tomográfica. 

Os pilares fundamentais que regem a qualidade de imagem em TC englobam:
- **Resolução Espacial:** A capacidade de discriminar pequenas estruturas anatômicas espacialmente próximas, governada pelo tamanho do ponto focal, amostragem do detector, matriz de reconstrução e pelo filtro de retroprojeção (kernel).
- **Resolução de Baixo Contraste (Detectabilidade):** A habilidade de distinguir tecidos com pequenas diferenças nos coeficientes de atenuação linear ($\mu$), intimamente limitada pelo **Espectro de Potência de Ruído (NPS)** e pela dose de radiação aplicada.
- **Ruído e Textura da Imagem:** Flutuações estatísticas dos números de TC (valores Hounsfield - HU) decorrentes da contagem finita de fótons (ruído quântico) e da amplificação espacial induzida pelos filtros de reconstrução.
- **Artefatos:** Distorções espaciais ou radiométricas estruturadas que não refletem a anatomia real, induzidas por endurecimento do feixe, efeito de volume parcial, movimento e ruído de fótons severos.

---

## 2. Formulação Matemática e Propriedades
Matematicamente, a avaliação objetiva da qualidade de imagem em TC fundamenta-se na teoria de sistemas lineares invariantes no espaço (LSI) e na estatística de processos estocásticos.

A relação fundamental entre o ruído da imagem, a dose e os parâmetros de aquisição pode ser modelada pela variância do coeficiente de atenuação $\sigma^2(\mu)$, que é inversamente proporcional à dose absorvida ($D$) e ao cubo da resolução espacial voxel ($(\Delta x)^3 \Delta z$):

$$
\sigma^2(\mu) \propto \frac{1}{D \cdot E \cdot (\Delta x)^2 \Delta z}
$$

Onde:
- $D$ é a dose de radiação.
- $E$ representa a eficiência quântica de detecção (DQE).
- $\Delta x, \Delta y, \Delta z$ representam as dimensões do voxel.

A **Função de Transferência de Modulação (FTM ou MTF)**, que quantifica a resolução espacial, é definida como a magnitude da transformada de Fourier da Função de Espalhamento de Pontuado (PSF - *Point Spread Function*):

$$
\text{MTF}(u, v) = \left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-j 2\pi (ux + vy)} \, dx \, dy \right|
$$

O **Espectro de Potência de Ruído (NPS - *Noise Power Spectrum*)** descreve a textura espacial do ruído em função das frecuencias espaciais ($u, v$):

$$
\text{NPS}(u, v) = \lim_{X, Y \to \infty} \frac{1}{X Y} \left\langle \left| \iint_{X, Y} \left[ \mu(x, y) - \bar{\mu} \right] e^{-j 2\pi (ux + vy)} \, dx \, dy \right|^2 \right\rangle
$$

Para integrar a qualidade física com a performance do observador humano ou computacional, utiliza-se a **Detectabilidade de Modelo ($d'$)**\, derivada da teoria de detecção de sinais:

$$
d'^2 = \iint_{-\infty}^{\infty} \frac{\left| W(u, v) \cdot \text{MTF}(u, v) \right|^2}{\text{NPS}(u, v)} \, du \, dv
$$

Onde $W(u, v)$ representa a transformada de Fourier do perfil do objeto ou tarefa de sinal a ser detectado.

---

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo de notas e artigos da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP), a **Qualidade de Imagem em TC** atua como o nó central que une a otimização dos protocolos de aquisição à segurança do paciente e à acurácia diagnóstica. 

Conforme identificado nas conexões do acervo:
- No documento [[Artigo Autor Ano Titulocurto|artigo_autor_ano_titulocurto]], o conceito surge atrelado às discussões sobre [[Noise Power Spectrum|Espectro de Potencia de Ruido]], [[Função de Modulacao Ftm|Funcao de Modulacao (FTM)]] e [[Otimização de Dose em TC|Otimizacao da Dose em Tomografia]], evidenciando a necessidade de balancear ganhos de dose com a degradação estocástica da imagem.
- No estudo de tarefas visuais e metodologias de avaliação descritas em [[Estudo de Observadores 2AFC|2afc]] (Testes de Escolha Forçada Alternada), a qualidade de imagem é avaliada não apenas por métricas físicas puras (como FTM e NPS), mas por métricas baseadas no desempenho do observador, integrando [[Deep Learning Image Reconstruction (DLR)|IR e DLR]] para mitigar o ruído sem perda de detectabilidade.
- Na nota de [[Dosimetria|dosimetria]], a Qualidade de Imagem em TC estabelece o limite inferior de dose aceitável: reduzir a dose além do limiar tolerado pela [[Retroprojeção Filtrada (FBP)|FBP]] colapsa a qualidade de imagem, tornando indispensável o uso de abordagens avançadas como a [[Deep Learning Image Reconstruction (DLR)|IR e DLR]] para manter a integridade diagnóstica na presença de [[Artefatos em Tomografia Computadorizada]].

---

## 4. Conexões e Wikilinks
* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Fisica Medica]]
* [[Noise Power Spectrum|Espectro de Potencia de Ruido]]
* [[Função de Modulacao Ftm|Funcao de Modulacao (FTM)]]
* [[Otimização de Dose em TC|Otimizacao da Dose em Tomografia]]
* [[Deep Learning Image Reconstruction (DLR)|IR e DLR]]
* [[Retroprojeção Filtrada (FBP)|FBP]]
* [[Dosimetria em Radiologia]]
* [[Artefatos em Tomografia Computadorizada]]