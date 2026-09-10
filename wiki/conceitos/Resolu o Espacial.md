---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, metrologia, reconstrucao-de-imagem]
data: 2026-08-25
---

# resolução espacial

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **resolução espacial** em Tomografia Computadorizada (TC) define a capacidade do sistema de imagem de discernir e separar dois pequenos objetos estruturais de alto contraste geometricamente próximos um do outro. Do ponto de vista metrológico e da física dos sistemas de imagem, a resolução espacial descreve o limite de alta frequência espacial até o qual o sistema consegue transferir informação com fidelidade mensurável.

Diferentemente da [[resolucao-de-baixo-contraste]], que é limitada primariamente pelo ruído quântico e pela dose de radiação ionizante administrada, a resolução espacial é governada fundamentalmente por fatores geométricos, físicos e algorítmicos do sistema de aquisição e reconstrução. Estes incluem:

1. **Tamanho e distribuição do ponto focal (focal spot):** O feixe de raios X não é emitido por um ponto infinitesimal, gerando um efeito de penumbra geométrica no detector.
2. **Abertura e tamanho dos elementos do detector:** O pixel físico do detector atua como um filtro integrador espacial de média local.
3. **Frequência de amostragem (sampling rate):** A taxa com que os dados de projeção são adquiridos ao longo da rotação do gantry.
4. **Filtro de retroprojeção (kernel ou função de reconstrução):** O filtro rampa aplicado na retroprojeção filtrada (FBP) que realça altas frequências espaciais em detrimento do ruído.
5. **Matriz de reconstrução e tamanho do FOV (Field of View):** Determina o tamanho nominal do pixel da imagem reconstruída ($\Delta x = \text{FOV} / N$).

A quantificação padrão da resolução espacial é realizada no domínio espacial por meio da **Função de Espalhamento de Ponto (PSF - *Point Spread Function*)** ou sua contrapartida unidimensional, a **Função de Espalhamento de Linha (LSF - *Line Spread Function*)**, e no domínio da frequência por meio da **Função de Transferência de Modulação (MTF - *Modulation Transfer Function*)**. A MTF normaliza a resposta do sistema em diferentes frequências espaciais (geralmente expressas em pares de linhas por centímetro, $\text{lp/cm}$, ou ciclos por centímetro), sendo o limite prático de resolução frequentemente definido na frequência onde a MTF cai para $10\%$ de seu valor máximo ($\text{MTF}_{10}$).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, a formação de imagem linear e regida por invariância espacial (*shift-invariant*) em TC pode ser modelada como a convolução da distribuição real do objeto $f(x,y)$ com a PSF do sistema $h(x,y)$, acrescida de ruído estocástico $\eta(x,y)$:

$$
g(x,y) = f(x,y) * h(x,y) + \eta(x,y)
$$

Onde $g(x,y)$ representa a imagem reconstruída. Aplicando a Transformada de Fourier bidimensional, a relação no domínio das frequências espaciais ($u, v$) torna-se:

$$
G(u,v) = F(u,v) \cdot H(u,v) + N(u,v)
$$

A **Função de Transferência Óptica (OTF - *Optical Transfer Function*)** é definida como a transformada de Fourier complexa da PSF normalizada:

$$
\text{OTF}(u,v) = \frac{\iint_{-\infty}^{\infty} h(x,y) e^{-j 2\pi (ux + vy)} \, dx\, dy}{\iint_{-\infty}^{\infty} h(x,y) \, dx\, dy}
$$

A **Função de Transferência de Modulação (MTF)** é o módulo da OTF:

$$
\text{MTF}(u,v) = \left| \text{OTF}(u,v) \right|
$$

Para sistemas de TC com simetria axial ou avaliados em perfis unidimensionais, a LSF é convertida em MTF por meio da Transformada de Fourier unidimensional:

$$
\text{MTF}(u) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-j 2\pi u x} \, dx \right| \left/ \int_{-\infty}^{\infty} \text{LSF}(x) \, dx \right.
$$

### Propriedades Críticas:
* **Linearidade e Aditividade:** Valem estritamente apenas para sistemas ideais ou linearizados. Em TC helicoidal com interpolação e pós-processamento não linear (como algoritmos iterativos avançados - IR ou *Deep Learning Reconstruction* - DLR), a MTF pode tornar-se dependente da intensidade do sinal (não-linear) e da dose.
* **Teorema da Amostragem de Nyquist-Shannon:** Para evitar artefatos de *aliasing*, a frequência de amostragem espacial do sistema de detecção deve ser pelo menos o dobro da máxima frequência espacial significativa presente no objeto atenuado:

$$
u_{\text{amostragem}} \ge 2 \cdot u_{\max}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A otimização da resolução espacial é um dos pilares no projeto e controle de qualidade de scanners de Tomografia Computadorizada, impactando diretamente o diagnóstico clínico de estruturas finas (como ossos do ouvido interno, microcalcificações mamográficas em TC de mama dedicada, stents vasculares e parênquima pulmonar).

### Controle de Qualidade (QC) e Metrologia
Phantoms específicos contendo padrões de alta resolução (fios finos de tungstênio, lâminas de ar/tecido, ou estruturas de teste do tipo *wire phantom* e *edge phantom*) são rotineiramente escaneados para derivar a PSF/LSF e calcular a curva MTF. Isso permite aos físicos médicos monitorar a degradação do sistema causada por instabilidades mecânicas do tubo de raios X ou desgaste do conjunto de detecção.

### Otimização em Reconstrução de Imagem
1. **Filtros de Retroprojeção (Kernels):** Kernels agudos (*sharp kernels*) amplificam as altas frequências espaciais, melhorando a resolução espacial visual, mas multiplicando severamente o ruído da imagem. Em contrapartida, kernels suaves (*smooth kernels*) atenuam o ruído à custa da perda de nitidez (borramento).
2. **Iterative Reconstruction (IR) e Deep Learning Reconstruction (DLR):** Algoritmos modernos modelam a física exata do sistema (incluindo o tamanho focal tridimensional e a resposta do detector - *system matrix modeling*). Redes neurais profundas treinadas para DLR conseguem recuperar texturas e detalhes estruturais próximos ao limite de Nyquist sem a penalidade clássica de amplificação de ruído observada na FBP linear.

---

## 4. Conexões e Wikilinks

* [[resolucao-de-baixo-contraste]]
* [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
* [[funcao-de-espalhamento-de-ponto-psf]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada-fbp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa-ir]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]
* [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
* [[ruido-quantico-e-dose]]