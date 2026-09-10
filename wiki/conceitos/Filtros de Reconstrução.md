---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, filtragem]
data: 2026-08-25
---

# filtros-de-reconstrucao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os **filtros de reconstrução** (frequentemente referidos como *kernels* de convolução) representam um componente fundamental e incontornável nos algoritmos de Retroprojeção Filtrada (*Filtered Backprojection* - FBP) em Tomografia Computadorizada (TC). Fisicamente, a aquisição de dados em TC gera projeções que correspondem a integrais lineares dos coeficientes de atenuação linear $\mu(x,y)$ ao longo de trajetórias de raios X (transformada de Radon). De acordo com o Teorema da Seção Central (ou Teorema do Slice-Central), a transformada de Fourier unidimensional de uma projeção paralela em um dado ângulo corresponde a uma fatia radial bidimensional da transformada de Fourier bidimensional da imagem a ser reconstruída.

Contudo, ao mapear o domínio polar (projeções) para o domínio cartesiano (matriz de imagem) através da interpolação necessária na retroprojeção simples, observa-se uma densidade espectral não uniforme no espaço de Fourier: as altas frequências espaciais são subamostradas em relação às baixas frequências. Sem correção, isso resulta em uma imagem severamente borrada (*blurred*), cuja resposta impulsiva decai proporcionalmente a $1/r$ no espaço real.

Para corrigir analiticamente este artefato de desfocagem e satisfazer o teorema da inversão de Radon, aplica-se um filtro de rampa (*ramp filter*) no domínio das frequências espaciais, cuja amplitude cresce linearmente com a frequência espacial absoluta. No entanto, como o ruído quântico de alta frequência inerente aos fótons de raios X é amplificado de forma catastrófica por uma rampa pura, os filtros de reconstrução práticos combinam o filtro rampa com janelas de apodização (como Hamming, Hann, Shepp-Logan ou Butterworth). O resultado é um conjunto balanceado de kernels que ajustam a resolução espacial e a supressão de ruído conforme o requisito clínico específico (por exemplo, kernels de alta resolução espacial para estruturas ósseas versus kernels suaves para parênquima cerebral ou tecidos moles).

## 2. Formulação Matemática e Propriedades (se aplicável)

A operação de reconstrução por FBP é formalmente descrita pela aplicação da transformada de Fourier e sua inversa. Seja $p_\theta(t)$ o perfil de projeção obtido no ângulo $\theta$, onde $t$ representa a coordenada espacial ao longo do detector. A projeção filtrada $Q_\theta(t)$ é obtida através da convolução ($*$) entre a projeção original e o filtro espacial $h(t)$:

$$
Q_\theta(t) = p_\theta(t) * h(t) = \int_{-\infty}^{\infty} p_\theta(\tau) h(t - \tau) \, d\tau
$$

No domínio da frequência espacial $f$, correspondente à coordenada $t$, a operação de filtragem corresponde a uma multiplicação simples, conforme o Teorema da Convolução:

$$
\mathcal{F}\{Q_\theta(t)\} = \mathcal{F}\{p_\theta(t)\} \cdot H(f)
$$

Onde $H(f)$ é a função de transferência do filtro no domínio da frequência. O filtro rampa ideal é definido matematicamente como:

$$
H_{\text{rampa}}(f) = |f|
$$

Para limitar a amplificação de ruído de alta frequência, uma função de janela $W(f)$ é multiplicada pelo filtro rampa. O filtro composto geral $H(f)$ torna-se:

$$
H(f) = |f| \cdot W(f)
$$

### Exemplos Clássicos de Funções de Janela $W(f)$ com frequência de corte $f_c$:

1. **Filtro de Shepp-Logan**:
   
$$
W(f) = \begin{cases} \frac{\sin(\pi f / 2 f_c)}{\pi f / 2 f_c}, & |f| \le f_c \\ 0, & |f| > f_c \end{cases}
$$

2. **Filtro de Hann (Cosseno Hanning)**:
   
$$
W(f) = \begin{cases} \frac{1}{2} \left(1 + \cos\left(\frac{\pi f}{f_c}\right)\right), & |f| \le f_c \\ 0, & |f| > f_c \end{cases}
$$

3. **Filtro Hamming**:
   
$$
W(f) = \begin{cases} 0.54 + 0.46 \cos\left(\frac{\pi f}{f_c}\right), & |f| \le f_c \\ 0, & |f| > f_c \end{cases}
$$

Após a filtragem de todas as projeções para $\theta \in [0, \pi)$, a imagem reconstruída $\mu(x,y)$ é gerada pela retroprojeção ponderada:

$$
\mu(x,y) = \int_{0}^{\pi} Q_\theta(x \cos\theta + y \sin\theta) \, \, d\theta
$$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A seleção do filtro de reconstrução é uma das decisões clínicas e físicas mais críticas em um protocolo de Tomografia Computadorizada, impactando diretamente o compromisso fundamental (*trade-off*) entre **resolução espacial**, **ruído na imagem** e **detectabilidade de baixo contraste**.

* **Controle de Qualidade e Metrologia**: Em testes de garantia de qualidade (QA), funções de espalhamento de ponto (*Point Spread Function* - PSF) e a Função de Transferência de Modulação (*Modulation Transfer Function* - MTF) são estritamente dependentes do kernel selecionado. Kernels agudos (*sharp kernels*) expandem a largura da MTF para altas frequências, permitindo a visualização de microestruturas (como trabéculas ósseas ou pequenas fraturas), mas degradam a relação sinal-ruído (SNR).
* **Dosimetria e Otimização de Dose**: A escolha de um filtro inadequado pode forçar o aumento da dose de radiação ($CTDI_{vol}$) para compensar o ruído gerado por um kernel de alta resolução. Técnicas de otimização buscam associar kernels suaves a varreduras de baixa dose para mitigar artefatos de granulação quântica (*mottle*).
* **Transição para Reconstrução Iterativa e IA**: Embora os filtros de reconstrução sejam inerentes à FBP analítica, sistemas modernos de Reconstrução Iterativa (IR) e Reconstrução Baseada em Inteligência Artificial (Deep Learning Reconstruction - DLR) utilizam modelos avançados de estatística de ruído e priors espaciais que muitas vezes emulam, corrigem ou substituem o comportamento dos filtros lineares tradicionais para eliminar o ruído sem sacrificar a resolução espacial.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Transformada de Radon|transformada-de-radon]]
* [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[ruido-quantico-em-tc]]
* [[Artefatos em Tomografia Computadorizada|artefatos-em-tomografia-computadorizada]]