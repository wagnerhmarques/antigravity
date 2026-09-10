---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem, reducao-de-ruido, metrologia]
data: 2026-08-25
---

# DLR_altera_estacionariedade_do_ruido

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **DLR_altera_estacionariedade_do_ruido** refere-se ao fenômeno físico-matemático pelo qual os algoritmos de Reconstrução Baseada em Deep Learning (*Deep Learning Reconstruction* - DLR) modificam a natureza estatística e espacial do ruído nas imagens de Tomografia Computadorizada (TC). 

Tradicionalmente, em sistemas de varredura que utilizam a Retroprojeção Filtrada (*Filtered Back-Projection* - FBP) analítica, o ruído nas imagens reconstruídas é predominantemente estacionário (ou fracamente não-estacionário), exibindo uma textura homogênea, isotrópica e com uma função de autocorrelação previsível que depende quase exclusivamente do filtro de rampa e do kernel de convolução aplicado. Em contrapartida, técnicas iterativas avançadas e\, de forma mais pronunciada, os modelos de DLR (muitas vezes estruturados como redes neurais convolucionais profundas treinadas com perdas baseadas em $L_1$, $L_2$ ou abordagens adversariais - GANs), operam como operadores altamente não-lineares e espacialmente variantes.

Como resultado dessa operação não-linear, o ruído residual gerado pelo DLR deixa de ser estacionário. A variância do ruído ($\sigma^2$), sua densidade espectral de potência (PSD) e sua textura tornam-se dependentes do sinal local. Regiões de alta atenuação (como áreas corticalizadas ósseas ou estruturas profundas no mediastino) e regiões de baixa atenuação (como parênquima pulmonar ou gordura subcutânea) sofrem transformações estatísticas distintas. O DLR tende a suprimir agressivamente o ruído em áreas de baixo contraste através de regularização adaptativa, gerando uma textura visualmente suave que se assemelha a "plástico" ou "acuarela" se sobre-regulada, enquanto preserva bordas nítidas (alta frequência). 

Metrologicamente, essa alteração na estacionariedade invalida métricas tradicionais de avaliação de qualidade de imagem baseadas na premissa de ruído branco Gaussiano estacionário — como o Desvio Padrão Global em regiões de interesse (ROI) circulares uniformes. A avaliação de desempenho passa a exigir ferramentas mais sofisticadas, como a Análise da Função de Transferência de Modulação baseada em Tarefas (Task-based MTF), a Detectabilidade de alvos via Observadores Ideais/Humanos e o Espectro de Potência do Ruído Local (Noise Power Spectrum - NPS espacialmente resolvido).

---

## 2. Formulação Matemática e Propriedades

Seja $f(x, y)$ a imagem reconstruída e $n(x, y)$ o campo estocástico associado ao ruído, onde $(x, y)$ representam as coordenadas espaciais no plano axial. Em um sistema linear e shift-invariante como a FBP ideal com filtro $h(r)$, a relação do ruído bruto do espaço de projeção para a imagem é dada linearmente\, de modo que a autocorrelação do ruído $R_n(x_1, y_1, x_2, y_2)$ depende apenas da diferença espacial $\Delta x = x_1 - x_2$ e $\Delta y = y_1 - y_2$:

$$
R_n(\Delta x, \Delta y) = \mathbb{E} \left\{ n(x, y) n(x + \Delta x, y + \Delta y) \right\}
$$

No caso de redes neurais profundas de DLR\, denotadas pelo operador não-linear $\mathcal{D}_{\theta}$ parametrizado por pesos $\theta$, a imagem reconstruída final $f_{\text{DLR}}$ a partir de uma estimativa inicial $f_0$ (geralmente FBP de baixa dose ou dados brutos) é expressa por:

$$
f_{\text{DLR}} = \mathcal{D}_{\theta} \left( f_0 + n_0 \right)
$$

Onde $n_0$ representa o ruído estocástico de entrada. Devido à natureza não-linear do operador $\mathcal{D}_{\theta}$, a expansão de Taylor de primeira ordem mostra que a propagação do ruído não é homogênea:

$$
n_{\text{DLR}}(x, y) \approx \left. 
abla \mathcal{D}_{\theta} \right|_{f_0} n_0 + \mathcal{O}(n_0^2)
$$

O operador de gradiente local $\left. 
abla \mathcal{D}_{\theta} \right|_{f_0}$varia ponto a ponto em função do valor subjacente do sinal$f_0(x,y)$. Consequentemente, a **Função de Autocorrelação do Ruído (NAC)** deixa de ser invariante por translação:

$$
R_{n_{\text{DLR}}}(x_1, y_1, x_2, y_2)
eq R_{n_{\text{DLR}}}(x_1 - x_2, y_1 - y_2)
$$

O Espectro de Potência do Ruído (NPS)\, definido como a transformada de Fourier bidimensional da função de autocorrelação do ruído, passa a ser espacialmente resolvido ($\text{NPS}(f_x, f_y; x, y)$):

$$
\text{NPS}(f_x, f_y; x, y) = \iint_{-\infty}^{\infty} R_{n_{\text{DLR}}}(\au_x, \au_y; x, y) e^{-j 2 \pi (f_x \au_x + f_y \au_y)} \, d\au_x \, d\au_y
$$

Propriedades fundamentais desta alteração incluem:
1. **Anisotropia Local:** O ruído perde a simetria radial típica de filtros analíticos.
2. **Supressão de Baixas Frequências Desproporcional:** O DLR frequentemente remove componentes de ruído de baixa frequência (manchas ou *mottled clouds*)\, deslocando o pico do NPS para frequências mais altas, o que altera radicalmente a textura visual da imagem sem perda real de resolução espacial de alto contraste.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão de que o **DLR_altera_estacionariedade_do_ruido** é de suma importância para a prática clínica, a dosimetria e o controle de qualidade em Tomografia Computadorizada pelos seguintes motivos:

* **Protocolos de Baixa Dose:** O DLR permite reduções expressivas no produto dose-comprimento (DLP) e no Índice de Dose em Tomografia Computadorizada ($CTDI_{vol}$). No entanto, à medida que a dose diminui, a não-linearidade do DLR se acentua, podendo criar artefatos de textura em "teia de aranha" ou apagar estruturas anatômicas de baixo contraste (como lesões hepáticas sutis ou limites de substância cinzenta/branca cerebral) por interpretá-las erroneamente como ruído de alta frequência.
* **Limitações das Métricas Convencionais de CQ:** O uso do desvio padrão ($\sigma$) em fatias de água de fantomas de qualidade de imagem (como o ACR ou catphan) torna-se enganoso. Uma imagem reconstruída por DLR pode apresentar um desvio padrão numericamente baixo (indicando supostamente alta supressão de ruído), mas o NPS revelará que a textura foi alterada de maneira a mascarar patologias reais ou simular falsas texturas patológicas.
* **Observadores Computacionais e Tarefas Clínicas:** Para otimização de protocolos, a avaliação deve transacionar para métricas baseadas em tarefas (*task-based image quality*), empregando o Índice de Detectabilidade ($d'$) derivado do modelo de observador não-prejudicado por canal (*Channelized Hotelling Observer* - CHO), que contabiliza corretamente a não-estacionariedade e a coloração do ruído imposta pelo DLR.

---

## 4. Conexões e Wikilinks

* [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]
* [[Task Transfer Function|MTF]]
* [[Noise Power Spectrum|noise-power-spectrum]]
* [[Retroprojeção Filtrada (FBP)|retroprojeção filtrada]]
* [[Otimização de Dose em TC|otimizacao_de_dose_em_tc]]
* [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
* [[Filtro de Rampa|filtro_de_rampa]]
* [[Noise Power Spectrum|teoria_de_propagacao_de_ruido]]