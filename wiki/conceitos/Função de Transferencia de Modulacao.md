---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, processamento-de-sinal, metrologia]
data: 2026-08-25
---

# funcao-de-transferencia-de-modulacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Transferência de Modulação** (do inglês *Modulation Transfer Function* - **MTF**) é a métrica padrão-ouro na física de imagem médica e metrologia de sistemas para quantificar a **resolução espacial** e a **fidelidade de reprodução de detalhes** de um sistema de imagem. Em termos rigorosos, a MTF descreve a capacidade do sistema de transferir o contraste de um objeto para a imagem final em função da frequência espacial.

Em sistemas de Tomografia Computadorizada (TC), a imagem digital resultante é uma representação discreta e ruidosa de um objeto contínuo tridimensional. O processo de formação de imagem é influenciado por múltiplos fatores físicos e geométricos que degradam o sinal, tais como:
* O tamanho finito do ponto focal do tubo de raios X (borramento geométrico).
* O espectro policromático dos raios X (que gera artefatos de endurecimento do feixe).
* O movimento da gantry e do paciente.
* A resposta finita dos elementos do detector (tamanho do pixel do detector e diafonia óptica/elétrica - *crosstalk*).
* Os filtros de reconstrução (*kernels*) aplicados durante a Retroprojeção Filtrada (FBP) ou algoritmos iterativos.

A modulação ($M$) de um sinal senoidal (ou padrão de barras) é definida em termos de suas intensidades máxima ($I_{\max}$) e mínima ($I_{\min}$) por meio da seguinte relação de contraste de Michelson:

$$
M = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}
$$

A MTF, portanto, representa a razão entre a modulação do sinal da imagem ($\mathcal{M}_{\text{imagem}}$) e a modulação do sinal do objeto original ($\mathcal{M}_{\text{objeto}}$) em uma dada frequência espacial $u$:

$$
\text{MTF}(u) = \frac{\mathcal{M}_{\text{imagem}}(u)}{\mathcal{M}_{\text{objeto}}(u)}
$$

Por convenção, a MTF é normalizada para o valor unitário na frequência espacial zero ($\text{MTF}(0) = 1$), indicando que o contraste de grandes estruturas (baixas frequências) é perfeitamente preservado. À medida que a frequência espacial aumenta (estruturas cada vez menores), o borramento (*blurring*) inerente ao sistema faz com que o contraste decaia, aproximando-se de zero. A frequência na qual a MTF cai para um determinado limiar (tipicamente 10% ou 50%, denotados como $MTF_{10}$ e $MTF_{50}$) é frequentemente utilizada para caracterizar e comparar o limite de resolução espacial de diferentes protocolos e escâneres de TC.

---

## 2. Formulação Matemática e Propriedades

Do ponto de vista da teoria linear de sistemas espaço-invariantes (LSI), o sistema de formação de imagem de TC pode ser modelado por uma operação de convolução. Se a entrada do sistema for representada por uma distribuição de atenuação ideal $f(x, y)$ e o sistema for caracterizado por sua **Função de Espalhamento de Ponto** (*Point Spread Function* - PSF), denotada por $h(x, y)$, a imagem degradada $g(x, y)$ é expressa como:

$$
g(x, y) = \iint_{-\infty}^{\infty} f(\xi, \eta) \, h(x - \xi, y - \eta) \, d\xi \, d\eta + n(x, y)
$$

onde $n(x, y)$ representa o ruído estocástico inerente ao processo de aquisição por raios X.

A **Função de Transferência Óptica** (OTF - *Optical Transfer Function*) é definida formalmente como a Transformada de Fourier bidimensional da PSF normalizada:

$$
\text{OTF}(u, v) = \frac{\mathcal{F} \left\{ h(x, y) \right\}}{\iint_{-\infty}^{\infty} h(x, y) \, dx \, dy}
$$

Como a PSF é uma função real, a OTF é, em geral, uma função complexa cuja fase indica deslocamentos espaciais e cuja magnitude constitui a **MTF**:

$$
\text{MTF}(u, v) = \left| \text{OTF}(u, v) \right| = \left| \frac{\iint_{-\infty}^{\infty} h(x, y) e^{-j 2\pi (ux + vy)} \, dx \, dy}{\iint_{-\infty}^{\infty} h(x, y) \, dx \, dy} \right|
$$

Para sistemas de TC com simetria radial ou avaliados em perfis unidimensionais, a formulação reduz-se ao domínio de uma única frequência espacial $u$:

$$
\text{MTF}(u) = \left| \frac{\int_{-\infty}^{\infty} LSF(x) e^{-j 2\pi u x} \, dx}{\int_{-\infty}^{\infty} LSF(x) \, dx} \right|
$$

sendo $LSF(x)$ a **Função de Espalhamento de Linha** (*Line Spread Function*), obtida integrando a PSF ao longo de uma direção.

### Propriedades Matemáticas Fundamentais:
1. **Normalização:** $\text{MTF}(0) = 1$.
2. **Teorema da Convolução:** Se duas fontes independentes de borramento com PSFs $h_1$ e $h_2$ atuam sequencialmente no sistema, a MTF total é o produto das MTFs individuais:
   
$$
\text{MTF}_{\text{total}}(u) = \text{MTF}_1(u) \cdot \text{MTF}_2(u)
$$

3. **Limitação de Banda:** Sistemas reais possuem uma frequência de corte ($u_c$) acima da qual a MTF é essencialmente nula, delimitada pelo espaçamento de amostragem dos detectores de acordo com o Teorema de Nyquist-Shannon.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica e industrial da Tomografia Computadorizada, a MTF é uma ferramenta indispensável para o controle de qualidade, projeto de hardwares e otimização de algoritmos de reconstrução.

* **Controle de Qualidade e Metrologia:** Programas de garantia de qualidade (QA) utilizam phantoms específicos para medir a MTF. Métodos comuns incluem a análise do fio fino (*wire method*), a borda afiada (*edge method* utilizando esferas de alta densidade como tungstênio ou teflon) e a avaliação direta por fatias finas de objetos pontuais. Acompanhar a degradação da MTF ao longo do tempo alerta para falhas mecânicas, desalinhamentos da gantry ou degradação do tubo de raios X.
* **Seleção de Filtros de Reconstrução (*Kernels*):** Na Retroprojeção Filtrada (FBP), os filtros matemáticos são projetados diretamente no domínio de Fourier para modular a MTF do sistema. *Kernels* de alta resolução acentuam as altas frequências (ampliando a MTF nessa faixa), o que melhora a visualização de estruturas finas (como trabeculações ósseas ou parênquima pulmonar), mas incorre em uma penalidade severa: a amplificação proporcional do ruído quântico. Em contrapartida, *kernels* suaves atenuam as altas frequências, reduzindo o ruído em detrimento da nitidez (ex: imagens de fígado ou cérebro).
* **Interação com Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Algoritmos avançados de reconstrução frequentemente quebram a linearidade estrita do sistema. A MTF em sistemas com DLR (*Deep Learning Reconstruction*) pode ser dependente do contraste local e do nível de dose, exigindo métricas estendidas (como a *Task-Specific MTF* ou MTF local) para avaliar se a supressão de ruído promovida por redes neurais está preservando a resolução espacial real ou gerando perda de textura ("efeito plástico").
* **Otimização de Dose:** Compreender a relação entre a MTF do sistema e a modulação do ruído (descrita pelo *Noise Power Spectrum* - NPS) é a base para o desenvolvimento de protocolos de tomografia de baixa dose que mantêm a detectabilidade de lesões através de observadores computacionais e modelos de avaliação da qualidade de imagem baseados na *Detective Quantum Efficiency* (DQE).

---

## 4. Conexões e Wikilinks

* [[funcao-de-espalhamento-de-ponto-psf]]
* [[funcao-de-espalhamento-de-linha-lsf]]
* [[Noise Power Spectrum|noise-power-spectrum-nps]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada-fbp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa-ir]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]
* [[teorema-de-nyquist-shannon]]
* [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
* [[Detective Quantum Efficiency DQE|detective-quantum-efficiency-dqe]]