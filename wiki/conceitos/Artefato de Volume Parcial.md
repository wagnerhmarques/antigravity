---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, artefatos-de-imagem, qualidade-de-imagem, processamento-de-sinal]
data: 2026-08-25
---

# artefato de volume parcial

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **artefato de volume parcial** (AVP) é um fenômeno de degradação da imagem que ocorre na Tomografia Computadorizada (TC) — e em outras modalidades de imagem médica — quando múltiplos tecidos com propriedades de atenuação radiológica distintas coexistem dentro do mesmo elemento de volume elementar (o *voxel*) discretizado pelo sistema de aquisição e reconstrução.

Fisicamente, o sistema de aquisição de TC mede a atenuação integrada dos raios X ao longo de trajetórias discretas. No entanto, o espaço tridimensional é amostrado de forma finita em uma matriz de *voxels* (onde a dimensão do plano é dada pelo tamanho do pixel e a espessura do corte pelo feixe colimado ou pelo perfil de sensibilidade do plano z). Quando um *voxel* abrange a interface entre duas estruturas de densidades eletrônicas e números atômicos muito diferentes — como a interface entre o osso cortical de alta atenuação e o parênquima cerebral ou gordura, ou entre o sangue contrastado e a parede vascular —, o coeficiente de atenuação linear efetivo atribuído a esse *voxel* resulta de uma média ponderada dos materiais constituintes.

Metrologicamente, este efeito manifesta-se sob duas formas principais na prática clínica:
1. **Efeito de Volume Parcial no Plano (In-plane Partial Volume Effect):** Causado pela amostragem espacial finita na matriz de reconstrução (tamanho do pixel). Estruturas pequenas, como vasos finos, trabéculas ósseas ou nódulos pulmonares subcentimétricos, têm suas intensidades atenuadas (subestimadas se de alta densidade, ou superestimadas se de baixa densidade) e seus contornos borrados (*blurry*).
2. **Efeito de Volume Parcial ao Longo do Eixo Z (Through-plane Partial Volume Effect):** Decorrente da espessura finita do corte tomográfico. Se uma estrutura anatômica possui dimensões menores do que a espessura nominal do corte, ou se cruza o plano de corte obliquamente, o sinal medido reflete a integração ao longo do eixo longitudinal. Isso gera artefatos clássicos de "falso endurecimento de feixe" aparente, perda de definição de bordas e o aparecimento de estruturas fantasma (*ghosting* ou *cupping* artificial) em imagens reformatadas ou multiplanares (MPR).

---

## 2. Formulação Matemática e Propriedades

Seja $\mu(x, y, z) spatial$ o coeficiente de atenuação linear real e contínuo do objeto a ser escaneado. O processo de formação de imagem discretiza este espaço em uma grade tridimensional de *voxels* de dimensões $\Delta_x \times \Delta_y \times \Delta_z$.

O valor medido e atribuído a um *voxel* indexado por $(i, j, k)$, correspondente ao número de Tomografia Computadorizada ($CT_num$ em unidades Hounsfield - HU), é formalmente uma média espacial ponderada pelo perfil de sensibilidade do voxel $h(x, y, z)$:

$$
CT(i, j, k) = \frac{1000}{\mu_{\text{água}}} \left[ \iint\int_{-\infty}^{\infty} \mu(x, y, z) \, h\left(x - i\Delta_x, y - j\Delta_y, z - k\Delta_z\right) dx \, dy \, dz - \mu_{\text{água}} \right]
$$

Onde o perfil de ponderação espacial $h(x, y, z)$ pode ser modelado, em uma aproximação ideal de caixa retangular (*pillbox*), como:

$$
h(x, y, z) = \begin{cases} 
\frac{1}{\Delta_x \Delta_y \Delta_z}, & \text{se } |x| \le \frac{\Delta_x}{2}, |y| \le \frac{\Delta_y}{2}, |z| \le \frac{\Delta_z}{2} \\ 
0, & \text{caso contrário}
\end{cases}
$$

Se um *voxel* contém uma fração volumétrica $f_1$ de um tecido com coeficiente de atenuação $\mu_1$ e uma fração $f_2 = 1 - f_1$ de um tecido com coeficiente $\mu_2$, o valor efetivo medido $\mu_{\text{ef}}$ é estritamente linear em termos de fração volumétrica:

$$
\mu_{\text{ef}} = f_1 \mu_1 + (1 - f_1) \mu_2
$$

No entanto, a relação entre o coeficiente de atenuação e o número CT (em HU) é linear, mas a conversão não linear ocorre quando há dependência espectral (endurecimento do feixe). O erro de volume parcial $\epsilon_{VP}$ na estimativa do coeficiente de atenuação de uma interface pontual pode ser expresso pela convolução entre a função indicadora da geometria real do objeto $I(x,y,z)$ e a resposta ao impulso do sistema (PSF - *Point Spread Function*):

$$
\mu_{\text{medido}}(x,y,z) = \left[ \mu(x,y,z) \cdot I(x,y,z) \right] * \text{PSF}(x,y,z)
$$

Propriedades fundamentais do AVP incluem:
- **Viés de Amplitude:** Extremos de densidade (máximos e mínimos locais) nunca são atingidos em estruturas menores que o dobro do *FWHM* (*Full Width at Half Maximum*) da PSF do sistema.
- **Invariância à Dose:** Por ser um artefato de amostragem geométrica e discretização espacial, o AVP é independente da dose de radiação ($mAs$), não sendo mitigado pelo aumento do fluxo de fótons.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle e a mitigação do artefato de volume parcial são críticos para a garantia da qualidade diagnóstica e para a metrologia em TC:

- **Redução da Espessura de Corte:** Historicamente combatido com a redução mecânica da espessura de colimação no eixo z. A introdução da Tomografia Computadorizada Multidetectores (MDCT) e, posteriormente, de sistemas baseados em detectores de contagem de fótons (PCD-CT), permitiu espessuras de corte submilimétricas isotropicamente (ex: $\Delta_x \approx \Delta_y \approx \Delta_z$), reduzindo drasticamente o AVP tridimensional.
- **Reconstrução Iterativa (IR) e Inteligência Artificial (DLR):** Algoritmos avançados de reconstrução utilizam modelos estatísticos e de formação de imagem mais precisos (modelagem avançada do sistema - *system modeling*), permitindo recuperar frequências espaciais elevadas e mitigar o borramento característico de matrizes de aquisição grosseiras. Redes neurais profundas treinadas para super-resolução (*Deep Learning-based Super-Resolution*) são aplicadas para estimar sub-voxels e afinar bordas degradadas por AVP.
- **Dosimetria e Radioterapia:** Na definição de volumes alvo (GTV/CTV) em planejamento radioterápico, o AVP em limites ósseos ou entre tecidos moles e cavidades aéreas pode introduzir erros sistemáticos significativos no cálculo de dose baseada em heterogeneidades (alocação incorreta de unidades Hounsfield para o cálculo do *Relative Stopping Power* - RSP).
- **Quantificação de Biomarcadores de Imagem:** Em radiômica e oncologia quantitativa, o AVP altera as métricas de textura e os valores de intensidade dos voxels, exigindo normalização rigorosa da espessura de corte e do tamanho do pixel em estudos multicêntricos.

---

## 4. Conexões e Wikilinks

- [[artefato de endurecimento de feixe]]
- [[funcao de dispersao de ponto - psf]]
- [[Unidades Hounsfield|unidade hounsfield]]
- [[Reconstrução Iterativa|reconstrucao iterativa]]
- [[tomografia computadorizada de contagem de fotons]]
- [[resolucao espacial em tomografia]]
- [[radiomica e texturas de imagem]]