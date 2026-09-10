---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, radiologia-digital, reconstrucao-de-imagem, inteligencia-artificial]
data: 2026-08-25
---

# computed-tomography

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Tomografia Computadorizada (TC) é uma modalidade de imagem médica avançada que reconstrói mapas tridimensionais (ou bidimensionais) dos coeficientes de atenuação linear de raios X de um meio material. Diferentemente da radiografia convencional, na qual há sobreposição anatómica de estruturas ao longo do caminho de propagação do feixe, a TC utiliza um feixe colimado de radiação ionizante e detectores posicionados de maneira opuesta à fonte (ou em arranjos anulares complexos) para adquirir projeções angulares sob múltiplos ângulos de incidência $\theta \in [0, \pi)$ ou $[0, 2\pi)$.

Do ponto de vista da física radiológica, a formação da imagem fundamenta-se na **Lei de Atenuação de Beer-Lambert** para feixes policromáticos e monocromáticos. Para um feixe monocromático ideal de intensidade inicial $I_0$, a intensidade transmitida $I$ após atravessar um objeto ao longo de uma linha reta de trajetória $L$ é dada por:

$$
I = I_0 \exp\left(-\int_L \mu(x, y) \, dl\right)
$$

Onde $\mu(x, y)$ representa o coeficiente de atenuação linear espacial (em $\text{cm}^{-1}$). A tarefa metrológica da TC consiste em resolver o problema inverso: estimar a distribuição espacial de $\mu(x, y)$ a partir de medições discretas e ruidosas da intensidade transmitida, transformadas nos chamados perfis de projeção ou senogramas.

Clinicamente, os valores absolutos de atenuação linear são convertidos em uma escala normalizada e estandardizada denominada **Unidades Hounsfield (HU)**, definida em relação à atenuação da água ($\mu_{\text{água}}$) e do ar ($\mu_{\text{ar}}$):

$$
\text{HU} = 1000 \times \frac{\mu(x, y) - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Como o ar possui $\mu_{\text{ar}} \approx 0$, a expressão simplifica-se comumente para:

$$
\text{HU} = 1000 \times \frac{\mu(x, y) - \mu_{\text{água}}}{\mu_{\text{água}}}
$$

Esta normalização garante reprodutibilidade metrológica entre diferentes scanners e fabricantes, permitindo a quantificação precisa de densidades teciduais (como gordura, parênquima hepático, sangue, osso trabecular e cortical).

---

## 2. Formulação Matemática e Propriedades

O núcleo matemático da tomografia computadorizada baseia-se na **Transformada de Radon** e no seu respetivo operador inverso. Seja $f(x, y) = \mu(x, y)$ a função contínua de duas dimensões que representa o corte anatômico. A Transformada de Radon $P_\theta(t)$ mapeia $f(x, y)$ para um conjunto de linhas integrais (projeções paralelas) parametrizadas pela distância $t$ ao centro de rotação e pelo ângulo de projeção $\theta$:

$$
P_\theta(t) = \mathcal{R}\{f\}(t, \theta) = \iint_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde $\delta(\cdot)$ é a função delta de Dirac. O arranjo bidimensional formado por $P_\theta(t)$ para todos os ângulos $\theta e deslocamentos$t$ é denominado **senograma**.

### O Teorema da Seção Central (Fourier Slice Theorem)
O princípio matemático que viabiliza a reconstrução analítica é o Teorema da Seção Central. Ele estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $P_\theta(t)$, tomada em relação à variável espacial $t$, é idêntica a uma fatia radial (com ângulo $\theta$) da Transformada de Fourier bidimensional da imagem original $F(u, v)$:

$$
S(\omega, \theta) = \mathcal{F}_{1D}\{P_\theta(t)\} = F(\omega \cos\theta, \omega \sin\theta)
$$

Onde $\omega$ é a frequência espacial nas coordenadas polares do domínio de Fourier.

### Retroprojeção Filtrada (Filtered Backprojection - FBP)
Para recuperar $f(x, y)$ a partir das projeções, aplica-se a transformada inversa de Fourier em coordenadas polares, resultando no algoritmo analítico clássico de **Retroprojeção Filtrada (FBP)**:

$$
f(x, y) = \int_{0}^{\pi} \int_{-\infty}^{\infty} P_\theta(t) \, k(x \cos\theta + y \sin\theta - t) \, dt \, \, d\theta
$$

Onde $k(t)$ é o filtro de rampa (ou filtros apodizados equivalentes, como *Ram-Lak*, *Shepp-Logan*, *Hamming*), cuja função no domínio das frequências $|\omega|$ compensa a atenuação inerente à amostragem radial que superam as altas frequências espaciais, amplificando o ruído se não forem devidamente regulados.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A evolução tecnológica da tomografia computadorizada abrange a otimização do tripé fundamental da física médica: **qualidade de imagem, resolução temporal/espacial e dose de radiação**.

### Dosimetria e Controle de Qualidade (CQ)
A avaliação metrológica de sistemas de TC exige a medição rigorosa de grandezas dosimétricas como o **CTDI** (*Computed Tomography Dose Index*), nas suas vertentes $\text{CTDI}_{100}$, $\text{CTDI}_{w}$ (ponderado) e $\text{CTDI}_{vol}$ (volumétrico), além do produto dose-comprimento ($\text{DLP}$). A otimização baseia-se no princípio ALARA (*As Low As Reasonably Achievable*), ajustando parâmetros como corrente do tubo ($mA$), tensão nominal ($kVp$), tempo de rotação, passo helicoidal (*pitch*) e filtragem do feixe de raios X.

### Reconstrução Iterativa (IR) e Aprendizagem Profunda (Deep Learning Reconstruction - DLR)
Enquanto a FBP assume hipóteses simplificadas de aquisição e ruído gaussiano, os métodos modernos de reconstrução superam suas limitações físicas:
1. **Reconstrução Iterativa Estatística (SIR / MBIR):** Modelam estatísticas de ruído complexas (Poisson e Gaussiano mistos) e a física do sistema (matriz de projeção e retroprojeção avançada), permitindo reduções drásticas de dose sem perda inaceitável de resolução de baixo contraste.
2. **Reconstrução Baseada em Inteligência Artificial (DLR):** Redes neurais profundas (ex: redes convolucionais U-Net adaptadas, Redes Generativas Adversariais - GANs) são treinadas para remover ruído quântico e artefatos de feixe endurecido (*beam hardening*) diretamente do espaço de projeção ou do domínio de imagem, preservando texturas anatómicas finas com eficiência computacional superior aos métodos iterativos puramente analíticos.

### Observadores Computacionais
A avaliação de desempenho de novos algoritmos de reconstrução em TC emprega frequentemente **observadores computacionais** (como o Observador Linear de Modelos - CMO, ou canais de observadores baseados em perfis visuais humanos) para quantificar a detectabilidade de lesões de baixo contraste (ex: nódulos pulmonares incipientes ou metástases hepáticas) em ambientes ruidosos, correlacionando métricas físicas puras (MTD, NPS, DQE) com a eficácia diagnóstica real.

---

## 4. Conexões e Wikilinks

- [[FBP|fbp-filtered-backprojection]]
- [[Reconstrução Iterativa|iterative-reconstruction]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Radiation Dosimetry|radiation-dosimetry]]
- [[Métricas de Dose em TC|ctdi-vol]]
- [[Unidades Hounsfield|hounsfield-units]]
- [[radon-transform]]
- [[quality-control-physics]]
- [[beam-hardening-artifact]]