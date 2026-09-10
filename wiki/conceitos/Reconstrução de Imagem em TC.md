---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, transformada-de-radon, aprendizado-profundo, processamento-de-sinal]
data: 2026-08-25
---

# Reconstrucao de Imagem em TC

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Reconstrução de Imagem em Tomografia Computadorizada (TC)** engloba o conjunto de algoritmos matemáticos e computacionais utilizados para converter medidas de atenuação de raios X obtidas de múltiples ângulos de projeção em uma representação espacial bi- ou tridimensional do coeficiente de atenuação linear interno ($\mu(x,y)$ ou $\mu(x,y,z)$) de um objeto. 

Fisicamente, o feixe de raios X policromático diverge da fonte e atravessa o corpo, sofrendo atenuação exponencial descrita pela **Lei de Beer-Lambert**:

$$
I = I_0 \exp\left( -\int_L \mu(x,y) \, dl \right)
$$

Onde $I_0$ é a intensidade incidente, $I$ é a intensidade transmitida e a integral de linha $L$ representa a trajetória do fóton. O processo de aquisição mede a projeção linearizada, denominada *sinograma* ($p(\theta, t)$), que corresponde ao logaritmo da razão de intensidades:

$$
p(\theta, t) = \ln\left(\frac{I_0}{I}\right) = \int_L \mu(x,y) \, dl
$$

O objetivo da reconstrução de imagem é resolver este problema inverso. Historicamente e tecnologicamente, a evolução dos métodos de reconstrução reflete a busca por maior resolução espacial, supressão de artefatos (como endurecimento de feixe, crivo metálico e ruído quântico) e minimização da dose de radiação ionizante administrada ao paciente, em estrita conformidade com os princípios de radioproteção (ALARA).

## 2. Formulação Matemática e Propriedades (se aplicável)

A formulação matemática clássica baseia-se na **Transformada de Radon** bidimensional, que mapeia a função espacial $\mu(x,y)$ em um conjunto de integrais de linha parametrizadas pelo ângulo de projeção $\theta$ e pela distância ao isocentro $t$:

$$
p(\theta, t) = \iint_{-\infty}^{\infty} \mu(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

O Teorema da **Filtração Central de Projeção** (ou *Fourier Slice Theorem*) estabelece que a transformada de Fourier unidimensional de uma projeção paralela $p(\theta, t)$ em relação à coordenada espacial $t$ resulta em uma linha que passa pela origem do espaço de Fourier bidimensional da imagem $\mathcal{F}\{\mu(x,y)\}$ sob o ângulo $\theta$.

Para recuperar a imagem espacial a partir do sinograma, utiliza-se analiticamente a **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP):

$$
\mu(x,y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(\theta, \omega) |\omega| e^{j 2 \pi \omega (x \cos\theta + y \sin\theta)} \, d\omega \right] \, d\theta
$$

Onde $P(\theta, \omega)$ é a transformada de Fourier de $p(\theta, t)$ e $|\omega|$ representa o filtro rampa (*ramp filter*), essencial para compensar o desfoque inerente da retroprojeção simples ($\frac{1}{r}$). Na prática discreta, o operador de retroprojeção filtrada é implementado por:

$$
\mu(x,y) = \int_{0}^{\pi} Q_{\text{filtro}}(\theta, x \cos\theta + y \sin\theta) \, \, d\theta
$$

Com $Q_{\text{filtro}}$ sendo a convolução do sinograma com um núcleo de filtro (ex: Ram-Lak, Hann, Hamming, Shepp-Logan).

Em contraste com os métodos analíticos, a **Reconstrução Iterativa (IR)** formula o problema inverso como um sistema algébrico linear de grande escala:

$$
\mathbf{p} = \mathbf{A}\mathbf{\mu} + \epsilon
$$

Onde $\mathbf{p}$ é o vetor de dados do sinograma, $\mathbf{A}$ é a matriz do sistema (matriz de projeção geométrica que modela o tamanho finito do ponto focal, largura do detector e trajetória do feixe), $\mathbf{\mu}$ é a imagem discretizada e $\epsilon$ representa o ruído estatístico (modelado frequentemente por distribuições de Poisson e Gaussiana). Algoritmos como OS-EM (*Ordered Subset Expectation Maximization*) resolvem este problema otimizando a função de verossimilhança:

$$
\hat{\mathbf{\mu}} = \arg\max_{\mathbf{\mu} \ge 0} L(\mathbf{p} \mid \mathbf{\mu})
$$

Os métodos de **Aprendizado Profundo para Reconstrução (DLR)** utilizam redes neurais convolucionais (CNNs), Redes Generativas Adversariais (GANs) ou modelos baseados em difusão para mapear dados de baixa dose/sinogramas esparsos diretamente em imagens de alta qualidade estrutural:

$$
\hat{\mathbf{\mu}}_{\text{DLR}} = \mathcal{G}_{\theta}\left( \mu_{\text{FBP\_baixo\_dose}} \right)
$$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha do algoritmo de reconstrução de imagem afeta diretamente métricas fundamentais de qualidade de imagem e dosimetria em física médica:

* **Controle de Qualidade (CQ) e Metrologia:** Algoritmos analíticos como a FBP mantêm a linearidade espacial e estatística do ruído, sendo preferidos para testes de constância que avaliam a função de transferência de modulação (MTF), ruído, uniformidade e linearidade do número de Hounsfield ($HU$).
* **Otimização de Dose e Redução de Ruído:** Métodos iterativos estatísticos (IR) e de aprendizado profundo (DLR) permitem a modelagem avançada do sistema físico e estatístico do ruído, viabilizando reduções expressivas na dose de radiação (frequentemente superiores a 50%) sem comprometer a detectabilidade de lesões de baixo contraste.
* **Mitigação de Artefatos:** Técnicas iterativas avançadas atenuam artefatos de enrijecimento de feixe, *beam hardening*, e artefatos metálicos (*Metal Artifact Reduction* - MAR) ao incorporar restrições físicas e modelos estatísticos direcionados na matriz de projeção $\mathbf{A}$.
* **Avaliação por Observadores Computacionais:** A introdução de DLR altera a textura do ruído e a resposta espacial (tornando-a não-linear e dependente do sinal), exigindo novas abordagens baseadas em observadores humanos e modelos matemáticos de canais para avaliar a detectabilidade de lesões com precisão.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Física das Radiações|Fisica da Radiacao]]
* [[Dosimetria em Radiologia|Dosimetria em Raio-X]]
* [[Qualidade de Imagem em TC]]
* [[Filtro Rampa]]
* [[Transformada de Radon]]
* [[Reconstrução Iterativa|Reconstrucao Iterativa]]
* [[Inteligencia Artificial IA|Inteligencia Artificial em Imagem Medica]]