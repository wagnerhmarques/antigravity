---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, image-reconstruction, processamento-de-sinal, inteligencia-artificial, fbp]
data: 2026-08-25
---

# image-reconstruction

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **reconstrução de imagem** (*image-reconstruction*) em Tomografia Computadorizada (TC) é o processo matemático e computacional pelo qual imagens tomográficas transversais (cortes axiais) são geradas a partir de projeções unidimensionais ou bidimensionais adquiridas em múltiplos ângulos ao redor do paciente. Fisicamente, o sistema mede a atenuação da radiação X atravessando o meio material, descrita macroscopicamente pela **Lei de Beer-Lambert**:

$$
I = I_0 \exp\left( -\int_L \mu(x, y) \, dl \right)
$$

Onde $I_0$ é a intensidade inicial do feixe de raios X, $I$ é a intensidade transmitida, e $\mu(x, y)$ é o coeficiente de atenuação linear espacialmente variante do tecido biológico ao longo da trajetória de linha $L$. O objetivo primário da reconstrução de imagem é resolver o problema inverso: recuperar o mapa espacial exato de $\mu(x, y)$ a partir de infinitas (ou discretas) medições da projeção integral logarítmica, conhecida formalmente como a **Transformada de Radon** do objeto.

Do ponto de vista metrológico, o processo de reconstrução afeta diretamente propriedades fundamentais da imagem, tais como:
* **Exatidão numérica:** Fidelidade dos valores de pixel expressos em Unidades Hounsfield (HU).
* **Resolução espacial:** Capacidade de discernir estruturas anatômicas de pequeno porte, governada pela função de espalhamento de ponto (PSF).
* **Ruído estatístico e textura:** Flutuações quânticas decorrentes do número finito de fótons detectados (estatística de Poisson), regidas pelo teorema do limite central e propagação de variância.
* **Artefatos:** Distorções geométricas ou de intensidade induzidas por endurecimento de feixe (*beam hardening*), movimento, ruído de quantum ou amostragem insuficiente.

Historicamente, a evolução da reconstrução de imagem passou de abordagens puramente analíticas (como a Retroprojeção Filtrada - FBP) para métodos iterativos estatísticos (IR) e, mais recentemente, métodos baseados em Aprendizado Profundo e Inteligência Artificial (Deep Learning Reconstruction - DLR), que visam otimizar o balanço entre dose de radiação e qualidade diagnóstica (*ALARA principle*).

---

## 2. Formulação Matemática e Propriedades

### A Transformada de Radon e o Teorema da Seção Central
As projeções paralelas adquiridas pelo sistema de aquisição formam a Transformada de Radon $P_\theta(t)$, definida como:

$$
P_\theta(t) = \iint_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde $f(x, y) = \mu(x, y)$, $\theta$ é o ângulo de projeção, e $t$ é a distância do detector ao isocentro. O **Teorema da Seção Central** (ou Teorema de Fourier da Projeção) estabelece que a transformada de Fourier unidimensional de uma projeção paralela $P_\theta(t)$ em relação à coordenada $t$ corresponde a uma linha radial na transformada de Fourier bidimensional da imagem $F(u, v)$ sob o mesmo ângulo $\theta$.

### Retroprojeção Filtrada (Filtered Backprojection - FBP)
Derivada analiticamente da inversão da Transformada de Radon, a FBP é formulada no domínio espacial como a retroprojeção de projeções filtradas por um filtro rampa:

$$
f(x, y) = \int_{0}^{\pi} \mathcal{Q} \left\{ P_\theta(t) \right\}_{t = x \cos\theta + y \sin\theta} \, d\theta
$$

Onde $\mathcal{Q}$ representa a operação de filtragem convolucional com um núcleo (kernel) $q(t)$, cuja transformada de Fourier $|\omega|$ atenua o desfoque inerente à retroprojeção simples ($1/r$). Na prática discreta, aproxima-se por:

$$
f(x, y) \approx \frac{\pi}{N_\theta} \sum_{i=1}^{N_\theta} \tilde{P}_{\theta_i}(x \cos\theta_i + y \sin\theta_i)
$$

Onde $\tilde{P}$ é a projeção convoluída com um filtro passa-alta (ex: Ram-Lak, Hamming, Shepp-Logan).

### Reconstrução Iterativa Estatística (Iterative Reconstruction - IR)
Os métodos iterativos modelam a física estatística da aquisição (ruído de Poisson e eletrônico) e a geometria do sistema por meio de um operador matricial de projeção adiante $\mathbf{A}$, onde o vetor de dados medidos $\mathbf{y}$ relaciona-se com a imagem discretizada $\mathbf{x}$ por:

$$
\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{ε}
$$

O problema de otimização busca minimizar uma função custo penalizada:

$$
\hat{\mathbf{x}} = \arg\min_{\mathbf{x} \ge 0} \left( L(\mathbf{y}, \mathbf{A}\mathbf{x}) + \beta R(\mathbf{x}) \right)
$$

Onde $L$ é a log-verossimilhança baseada no ruído estatístico (ex: ponderada por variância ou estatística exata de Poisson), $R(\mathbf{x})$ é um termo de regularização (prior) espacial que preserva bordas (ex: variação total - *Total Variation*, penalizações de Huber), e $\beta$ é o hiperparâmetro de regularização.

### Reconstrução Baseada em Aprendizado Profundo (Deep Learning Reconstruction - DLR)
Abordagens modernas utilizam redes neurais profundas (frequentemente redes adversariais geradoras - GANs, ou arquiteturas U-Net) para mapear imagens de baixa qualidade (ruidosas ou subamostradas) $\mathbf{x}_{\text{low}}$ para estimativas de alta qualidade $\mathbf{x}_{\text{DLR}}$:

$$
\mathbf{x}_{\text{DLR}} = \mathcal{G}_{\boldsymbol{\theta}}\left(\mathbf{x}_{\text{low}}\right)
$$

Onde $\mathcal{G}$ é a rede neural parametrizada por pesos $\boldsymbol{\theta}$, treinada por meio de minimização de funções de perda perceptuais, de fidelidade de dados e adversariais.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha e o ajuste do algoritmo de reconstrução de imagem impactam diretamente o ecossistema clínico da Tomografia Computadorizada:

* **Otimização de Dose e Redução de Ruído:** Enquanto a FBP clássica amplifica o ruído quântico em baixas correntes de tubo ($mA$), os algoritmos de reconstrução iterativa e baseada em IA permitem reduções significativas de dose de radiação (frequentemente superiores a 50%) mantendo a detectabilidade de lesões e a acurácia diagnóstica.
* **Controle de Qualidade e Metrologia:** Em avaliações fantoma (ex: protocolos ACR ou AAPM), a reconstrução afeta diretamente métricas como a Modulação da Função de Transferência (MTF), a Curva de Ruído de Potência (NPS) e a Detectability Index ($d'$), sendo mandatória a padronização rigorosa dos kernels de reconstrução.
* **Mitigação de Artefatos:** Técnicas avançadas de reconstrução incorporam correção iterativa para endurecimento de feixe, artefatos de metal (MAR - *Metal Artifact Reduction*) e espalhamento Compton (*scatter correction*), modelando com precisão a física da aquisição.
* **Observadores Computacionais:** A avaliação de novos algoritmos de reconstrução depende frequentemente de modelos de observadores humanos e matemáticos (como o *Channelized Hotelling Observer*), garantindo que ganhos visuais subjetivos se traduzam em desempenho quantitativo real na detecção de patologias.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|computed-tomography]]
* [[Retroprojeção Filtrada (FBP)|filtered-backprojection]]
* [[Reconstrução Iterativa|iterative-reconstruction]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[radon-transform]]
* [[Noise Power Spectrum|noise-power-spectrum]]
* [[Modulation Transfer Function (MTF)|modulation-transfer-function]]
* [[hounsfield-unit]]
* [[Beam Hardening|beam-hardening]]
* [[dose-optimization]]