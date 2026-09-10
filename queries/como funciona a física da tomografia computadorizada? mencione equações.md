> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Transformada de Radon]], [[Teorema da Fatia Central de Fourier]], [[Retroprojeção Filtrada (FBP)]], [[Unidades Hounsfield]], [[Endurecimento do Feixe]]

## 1. Princípios Físicos da Aquisição e Atenuação Radiológica

A **[[Tomografia Computadorizada]]** (TC) fundamenta-se na medição da atenuação diferencial de um feixe policromático de raios X ao atravessar um volume anatômico a partir de múltiplos ângulos de projeção ($\theta \in [0, \pi)$). A interação primária da radiação com os tecidos biológicos nas energias diagnósticas (30 a 140 keV) é governada pelo **efeito fotoelétrico** ($\propto Z^3 / E^3$) e pelo **espalhamento Compton** (fracamente dependente de $Z$).

A intensidade do feixe transmitido em relação à intensidade incidente $I_0$ é descrita pela lei de atenuação de Beer-Lambert generalizada para meios heterogêneos:

$$
I(\theta, t) = I_0 \exp\left( -\int_{L_{\theta,t}} \mu(x, y) \, dl \right)
$$

Onde $\mu(x, y)$ representa a distribuição espacial do coeficiente de atenuação linear ($\text{cm}^{-1}$) e $L_{\theta, t}$ é a linha de integração (trajeto do fóton) correspondente ao detector na posição $t$ e ângulo $\theta$.

---

## 2. A Transformada de Radon e o Sinograma

O conjunto bidimensional de todas as integrações lineares obtidas durante a rotação completa do pórtico (*gantry*) constitui o **sinograma** $p(\theta, t)$, matematicamente formalizado pela **Transformada de Radon 2D**:

$$
p(\theta, t) = \iint_{-\infty}^{\infty} \mu(x, y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

O objetivo fundamental da reconstrução tomográfica é inverter essa transformada para recuperar o mapa espacial de atenuação, cujos valores são convertidos para a escala padronizada de **Unidades Hounsfield (HU)** para fins de quantificação clínica:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{agua}}}{\mu_{\text{agua}} - \mu_{\text{ar}}}
$$

---

## 3. Reconstrução Analítica: Retroprojeção Filtrada (FBP)

A solução analítica clássica para a inversão da Transformada de Radon baseia-se no **Teorema da Fatia Central** (*Central Slice Theorem*). A Retroprojeção Filtrada (FBP) aplica um filtro de rampa no domínio da frequência espacial para compensar o desfoque geométrica inerente ($\frac{1}{r}$), seguido pela retroprojeção angular:

$$
\mu(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(\theta, \omega) |\omega| e^{j 2 \pi \omega t} \, d\omega \right]_{t = x\cos\theta + y\sin\theta} \, d\theta
P(\theta, \omega) = \int_{-\infty}^{\infty} p(\theta, t) e^{-j 2 \pi \omega t} \, dt
$$

Onde $|\omega|$
é a função de transferência do filtro rampa ideal, frequentemente suavizada por janelas de apodização para conter a amplificação do ruído quântico estocástico de alta frequência.

---

## 4. Evolução Moderna: Reconstrução Iterativa e Deep Learning

Em regimes de baixa dose de radiação (aderência ao princípio ALARA), a FBP amplifica severamente o ruído estatístico. Os tomógrafos modernos substituem ou complementam a FBP por **[[reconstrucao-iterativa]]** (IR) e **[[Deep Learning Image Reconstruction (DLR)]]** (DLR), modelando o problema inverso estatisticamente (estatística de Poisson dos fótons) por meio de otimização regularizada:

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \frac{1}{2} \left\lVert \mathbf{A}\mu - \mathbf{p} \right\Vert_{\mathbf{\Sigma}^{-1}}^2 + \lambda \mathcal{R}(\mu) \right\}
$$

Onde $\mathbf{A}$ é a matriz do sistema de projeção, $\mathbf{\Sigma}$ é a matriz de covariância do ruído e $\mathcal{R}(\mu)$ é o termo regularizador espacial (estruturado via modelos estatísticos ou aprendizado profundo por redes neurais convolucionais).

A avaliação metrológica do desempenho desses sistemas não-lineares exige o uso de métricas orientadas à tarefa, tais como a **[[Task Transfer Function]]** (TTF), o **[[Noise Power Spectrum]]** (NPS) e o **[[Índice de Detectabilidade]]** ($d'$), superando as limitações da Relação Contraste-Ruído convencional (CNR).
