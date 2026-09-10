---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, formacao-de-imagem\, dosimetria, radiodiagnostico]
data: 2026-08-25
---

# Tomografia Computadorizada (CT)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Tomografia Computadorizada (CT) é uma modalidade de imagem médica de diagnóstico avançada que utiliza radiação ionizante (raios-X) para gerar representações tridimensionais (volumétricas) detalhadas da anatomia interna de um paciente. O princípio físico fundamental baseia-se na atenuação da radiação eletromagnética ao atravessar a matéria heterogênea do corpo humano.

Diferente da radiografia convencional bidimensional, onde há superposição anatômica de estruturas ao longo do trajeto do feixe de raios-X, a CT emprega uma fonte de raios-X colimada e um arranjo de detectores opostos que giram em torno do eixo longitudinal do paciente (eixo $z$). As medições de intensidade transmitida são coletadas em múltiplos ângulos de projeção ($\theta$), permitindo calcular a distribuição espacial espacial dos coeficientes de atenuação linear locais\, denotados por $\mu(x, y, z)$.

Metrologicamente, os valores de pixel/voxel na imagem de CT são padronizados e expressos em **Unidades Hounsfield (HU)**, também conhecidas como número CT. A escala Hounsfield é calibrada tendo a água pura como referência ($0 \text{ HU}$) e o ar sob condições padrão como $-1000 \text{ HU}$. A conversão matemática do coeficiente de atenuação linear $\mu$ para HU é dada por:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Onde $\mu_{\text{ar}}$ é tipicamente considerado igual a $0 \text{ cm}^{-1}$ para fins práticos. Esta padronização quantitativa confere à CT alta especificidade tecidual, viabilizando a diferenciação de densidades sutis, como entre substância cinzenta e branca no encéfalo, ou a caracterização de nódulos pulmonares.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A formação da imagem em tomografia computacional resolve um problema inverso: reconstruir uma função bidimensional $\mu(x, y)$ a partir de suas projeções unidimensionais em múltiplos ângulos. O modelo matemático fundamental é a **Transformada de Radon**, que descreve a integral de linha do coeficiente de atenuação ao longo de uma trajetória de raio $L$:

$$
P_{\theta}(t) = \iint_{-\infty}^{\infty} \mu(x, y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde:
- $P_{\theta}(t)$ representa o sinograma (conjunto de projeções paralelas obtidas no ângulo $\theta$ e posição de translação $t$).
- $\delta$ é a função delta de Dirac.

Para recuperar a imagem original $\mu(x, y)$ a partir do sinograma, o método analítico clássico é a **Retroprojeção Filtrada (Filtered Backprojection - FBP)**\, derivada do Teorema da Slice-Projection (Teorema do Corte Central). A formulação contínua da FBP é dada por:

$$
\mu(x, y) = \int_{0}^{\pi} Q_{\theta}(x \cos\theta + y \sin\theta) \, \, d\theta
$$

Onde $Q_{\theta}(t)$ é a projeção filtrada, obtida através da convolução do sinograma original com um filtro rampa (ou filtros apodizados como *Hann*, *Hamming* ou *Shepp-Logan*) no domínio espacial ou frequência:

$$
Q_{\theta}(t) = \int_{-\infty}^{\infty} P_{\theta}(t') \, h(t - t') \, dt'
$$

Sendo $h(t)$ a resposta ao impulso do filtro de rampa, cuja transformada de Fourier $|\omega$ penaliza as baixas frequências e amplifica as altas frequências para compensar o desfoque inerente da retroprojeção simples ($\frac{1}{r}$).

Nos sistemas modernos, métodos algébricos e iterativos (IR) e técnicas baseadas em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*) modelam estatísticas de ruído de Poisson e o sistema óptico do scanner para resolver a equação matricial linearizada:

$$
\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{n}
$$

Onde $\mathbf{y}$ é o vetor de dados de projeção ruidosos, $\mathbf{A}$ é a matriz do sistema (geometria do feixe e física de atenuação), $\mathbf{x}$ é a imagem discretizada e $\mathbf{n}$ representa o ruído estatístico.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A tomografia computacional é pilar central na medicina diagnóstica moderna, oncologia (estadiamento e acompanhamento terapêutico), cardiologia (escore de cálcio e angio-CT coronariana), planejamento radioterápico (CT de simulação) e emergências médicas (politraumatismo e AVC).

No entanto, o uso de radiação ionizante impõe desafios críticos de radioproteção, exigindo rigorosa otimização baseada no princípio ALARA (*As Low As Reasonably Achievable*). A gestão da dose envolve métricas dosimétricas padronizadas:
- **CTDIvol (Volume Computed Tomography Dose Index):** Medida da dose média absorvida no interior de um fantoma padronizado de acrílico (16 cm para crânio, 32 cm para abdome/corpo), corrigida para o passo de hélice (*pitch*).
- **DLP (Dose-Length Product):** Produto do $\text{CTDI}_{\text{vol}}$ pelo comprimento escaneado ($L$), refletindo a energia total depositada no paciente ($\text{mGy}\cdot\text{cm}$).

A otimização contemporânea da CT apoia-se em pilares tecnológicos fundamentais:
1. **Modulação Automática de Corrente (mA):** Ajuste dinâmico da intensidade do feixe conforme a atenuação angular e longitudinal do paciente.
2. **Filtros de Reconstrução Avançados:** Migração de FBP pura para algoritmos de Reconstrução Iterativa (IR) e Deep Learning Reconstruction (DLR), permitindo drástica redução de miliamperagem (dose) sem perda inaceitável de resolução espacial ou introdução de ruído textural indesejado.
3. **Controle de Qualidade (CQ) Metrológico:** Avaliação rotineira de parâmetros essenciais de imagem com fantomas especializados (ex: ACR ou Catphan), medindo ruído, uniformidade, linearidade de $\text{HU}$, resolução espacial de alto contraste (MTF - *Modulation Transfer Function*) e baixo contraste, além da dose glandular/superficial.

---

## 4. Conexões e Wikilinks

- [[Reconstrução de Imagem]]
- [[Retroprojeção Filtrada (FBP)|Retroprojeção Filtrada (FBP)]]
- [[Reconstru o Iterativa e Deep Learning DLR|Reconstrução Iterativa e Deep Learning (DLR)]]
- [[Dosimetria em Radiodiagn Stico|Dosimetria em Radiodiagnóstico]]
- [[Control de Qualidade em CT]]
- [[Unidades Hounsfield|Unidades Hounsfield (HU)]]
- [[F Sica do Raio X|Física do Raio-X]]