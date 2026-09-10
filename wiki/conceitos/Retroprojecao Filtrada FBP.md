---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, metrologia]
data: 2026-08-25
---

# Retroprojeção Filtrada (FBP)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Retroprojeção Filtrada (Filtered Backprojection - FBP)** é o algoritmo analítico padrão-ouro histórico e fundamental utilizado na reconstrução de imagens em Tomografia Computadorizada (TC) de raios X. Fisicamente, a aquisição de dados em um tomógrafo consiste na medição da atenuação linear dos fótons de raios X ao longo de linhas retas que atravessam o paciente em múltiplos ângulos de projeção, formando o conjunto de dados conhecido como **Sinograma** (ou Transformada de Radon bidimensional).

O processo intuitivo de reconstrução, denominado **retroprojeção simples** (ou *simple backprojection*), consiste em "espalhar" ou projetar de volta os valores de atenuação medidos em cada ângulo ao longo da trajetória original dos raios. Contudo, a aplicação direta da retroprojeção simples resulta em imagens severamente borradas (*blurred*). Do ponto de vista da física matemática, a retroprojeção simples de um objeto pontual gera um perfil de intensidade cuja amplitude decresce com o inverso da distância ao centro ($1/r$). No domínio de Fourier, isso equivale a ponderar as frequências espaciais da imagem real por um fator proporcional a $1/\rho$, onde $\rho$ é a frequência espacial radial.

Para corrigir este artefato físico-matemático inerente à geometria de projeção, a FBP aplica um filtro de rampa (*ramp filter*) unidimensional no domínio das frequências (ou espacial) a cada perfil de projeção antes da operação de retroprojeção geométrica. Esse filtro amplifica as altas frequências espaciais na exata proporção inversa ao desfoque introduzido pela retroprojeção simples ($|\rho|$), restaurando a nitidez espacial, a resolução de bordas e a exatidão quantitativa dos coeficientes de atenuação linear ($\mu$).

## 2. Formulação Matemática e Propriedades

A formulação matemática da FBP baseia-se no **Teorema da Slicing Central** (ou Teorema da Projeção-Fatia), que estabelece que a transformada de Fourier unidimensional de uma projeção paralela obtida a um ângulo $\theta$ corresponde a uma linha que passa pela origem da transformada de Fourier bidimensional da imagem original $f(x,y)$ sob o mesmo ângulo $\theta$.

Seja $p_\theta(t)$ a projeção paralela do objeto $f(x,y)$ a um ângulo $\theta$, onde $t$ é a coordenada linear ao longo do detector:

$$
p_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A Transformada de Fourier 1D de $p_\theta(t)$ em relação à coordenada $t$ é dada por:

$$
P_\theta(\omega) = \int_{-\infty}^{\infty} p_\theta(t) e^{-i 2\pi \omega t} dt
$$

Pelo Teorema da Slicing Central, a reconstrução exata da função $f(x,y)$ em coordenadas polares $(r, \phi)$ é obtida integrando-se as projeções filtradas sobre todos os ângulos de $\theta = 0$ a $\pi$:

$$
f(x,y) = \int_{0}^{\pi} Q_\theta(x \cos\theta + y \sin\theta) \, \, d\theta
$$

Onde $Q_\theta(t)$ representa a projeção filtrada, calculada pela convolução da projeção original $p_\theta(t)$ com um núcleo de filtro (*kernel*) $h(t)$:

$$
Q_\theta(t) = p_\theta(t) * h(t) = \int_{-\infty}^{\infty} p_\theta(t') h(t - t') \, dt'
$$

No domínio das frequências, a operação de filtragem corresponde à multiplicação pelo filtro de rampa ideal:

$$
\mathcal{F}\{h(t)\} = H(\omega) = |\omega|
$$

Na prática clínica, devido à presença inevitável de ruído quântico de alta frequência decorrente do número finito de fótons detectados, o filtro de rampa ideal $|\omega|$ (que amplifica ruído de forma ilimitada) é multiplicado por janelas de suavização (como *Hamming*, *Hann*, *Butterworth* ou *Shepp-Logan*):

$$
H_{\text{prático}}(\omega) = |\omega| \cdot W(\omega)
$$

Onde $W(\omega)$ atua como um filtro passa-baixas para controlar a relação sinal-ruído (SNR) e a granulosidade da imagem reconstruída.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A FBP consolidou-se como o algoritmo padrão na indústria de TC devido a três vantagens fundamentais: **determinismo analítico**, **exatidão geométrica** e **extrema eficiência computacional**. Sendo uma solução direta (não iterativa), seu tempo de processamento é extremamente baixo, permitindo a reconstrução em tempo real necessária para protocolos modernos de aquisição helicoidal (espiral) e feixe cônico (*cone-beam*).

No entanto, a FBP possui limitações intrínsecas severas quando operada em regimes de **baixa dose de radiação**:
* **Amplificação de Ruído:** O filtro de rampa amplifica drasticamente as altas frequências, onde o ruído estatístico quântico domina. Reduzir a dose de raios X degrada exponencialmente a SNR em imagens reconstruídas por FBP.
* **Artefatos de Feixe Duro e Ruído Estocástico:** Em condições de baixa contagem de fótons, a FBP gera artefatos de estrias (*streaking artifacts*) e distorções não lineares na quantificação dos números de Hounsfield (HU).

Devido a essas limitações, a FBP tem sido progressivamente complementada ou substituída em cenários de otimização de dose por algoritmos de **Reconstrução Iterativa (IR)** — como as reconstruções estatísticas e baseadas em modelos (MBIR) — e por métodos de **Aprendizado Profundo para Reconstrução (DLR - Deep Learning Reconstruction)**. Contudo, a FBP permanece como métrica de referência de velocidade e serve como etapa inicial (*initial guess*) para muitos algoritmos iterativos avançados.

Em termos de controle de qualidade metrológico, a FBP é o método de escolha para a avaliação analítica da função de espalhamento de ponto (PSF), função de transferência de modulação (MTF) e testes de constância em fantomas de TC, pois não introduz artefatos de suavização algorítmica não linear típicos de modelos iterativos complexos.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Sinograma]]
* [[Reconstrução Iterativa|Reconstrucao Iterativa (IR)]]
* [[Deep Learning para Reconstrucao (DLR)]]
* [[Fisica dos Raios X]]
* [[Controle de Qualidade em TC]]
* [[Otimizacao de Dose em Radiologia]]