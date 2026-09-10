---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, processamento-de-imagem, filtragem, reconstrução, ia]
data: 2026-08-25
---

# Filtros e Processamento de Imagem em TC

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O processamento de imagem e a filtragem em Tomografia Computadorizada (TC) abrangem o conjunto de operações matemáticas e computacionais aplicadas aos dados brutos (*raw data*, projeções) e às imagens reconstruídas com o objetivo de otimizar a qualidade diagnóstica, mitigar artefatos, extrair características quantitativas e minimizar a dose de radiação ionizante entregue ao paciente. 

Do ponto de vista da física médica, a imagem de TC é obtida a partir da solução do problema inverso da varredura por raios X, onde o coeficiente de atenuação linear espacial ($\mu(x,y)$) é estimado a partir de projeções angulares (sinograma). O Teorema Central da Projeção estabelece que a transformada de Fourier bidimensional de uma projeção paralela é equivalente a uma linha que passa pela origem do espaço de Fourier 2D da imagem original. 

A reconstrução analítica padrão, conhecida como Retroprojeção Filtrada (*Filtered Backprojection* - FBP), introduce inerentemente um desfoque matemático devido à natureza da retroprojeção (equivalente a uma convolução espacial por $1/r$). Para corrigir esse desfoque e recuperar a alta resolução espacial, aplica-se um filtro de rampa no domínio da frequência (ou equivalente espacial). No entanto, o filtro de rampa amplifica severamente o ruído de alta frequência associado aos fótons estatisticamente limitados (ruído quântico). Consequentemente, filtros apodizados (como Hann, Hamming, Shepp-Logan ou Butterworth) são empregados para modular o balanço entre resolução espacial e supressão de ruído.

Além da filtragem no espaço de Fourier durante a reconstrução, o processamento de imagem pós-reconstrução engloba técnicas avançadas no domínio espacial e transformadas wavelet, além de abordagens baseadas em Inteligência Artificial (IA) e Aprendizado Profundo (*Deep Learning* - DL), que operam como redutores de ruído adaptativos e estimadores estatísticos não lineares.

---

## 2. Formulação Matemática e Propriedades

### A. O Filtro de Rampa e a Retroprojeção Filtrada (FBP)
A reconstrução por FBP de um objeto bidimensional $f(x,y)$ a partir de suas projeções paralelas $P_\theta(t)$ é formalmente descrita pela aplicação de um filtro de rampa seguido pela retroprojeção:

$$
f(x,y) = \int_{0}^{\pi} \mathcal{Q} \left\{ P_\theta(t) \right\} \, d\theta
$$

Onde o operador de filtragem $\mathcal{Q}$ no domínio espacial consiste na convolução ($\ast$) da projeção com um núcleo de filtro $k(t)$:

$$
\mathcal{Q} \left\{ P_\theta(t) \right\} = P_\theta(t) \ast k(t) = \int_{-\infty}^{\infty} P_\theta(t') k(t - t') dt'
$$

No domínio da frequência (via Transformada de Fourier 1D $\mathcal{F}_{1D}$), o núcleo de convolução ideal (filtro de rampa) é expresso como:

$$
K(
u) = |
u|
$$

Onde $
u$representa a frequência espacial. Para limitar a amplificação de ruído nas altas frequências, um filtro de janela (ou função de apodização)$W(
u)$ é multiplicado ao filtro de rampa:

$$
K_{mod}(
u) = |
u| \cdot W(
u)
$$

### B. Exemplo de Janela de Suavização (Filtro Hann)
Uma das janelas clássicas utilizadas na prática clínica para controle de ruído é a janela de Hann, definida no domínio da frequência por:

$$
W_{Hann}(
u) = \begin{cases} 
\frac{1}{2} \left[ 1 + \cos\left( \frac{\pi 
u}{
u_c} \right) \right], & |
u| \le 
u_c \\ 
0, & |
u| > 
u_c 
\end{cases}
$$

Onde $
u_c$ é a frequência de corte (*cut-off frequency*), que dita o limite da resolução espacial recuperada.

### C. Filtragem Adaptativa e Processamento Baseado em IA
Modelos modernos de reconstrução iterativa (IR) e reconstrução baseada em inteligência artificial (DLR - *Deep Learning Reconstruction*) modelam o ruído estatístico utilizando distribuições de Poisson e Gaussianas combinadas. Uma rede neural convolucional (CNN) ou modelo gerador adversarial (GAN) otimiza uma função de perda (*loss function*) que penaliza o erro quadrático médio (MSE) ou a percepção estrutural, mapeando imagens de TC com alto ruído (baixa dose) $\mathbf{x}_{noisy}$ para imagens de referência de alta qualidade $\mathbf{x}_{clean}$:

$$
\mathcal{L}_{Total} = \lambda_1 \mathcal{L}_{MSE}(\mathbf{x}_{clean}, \mathcal{R}_\theta(\mathbf{x}_{noisy})) + \lambda_2 \mathcal{L}_{Perceptual}(\mathbf{x}_{clean}, \mathcal{R}_\theta(\mathbf{x}_{noisy}))
$$

Onde $\mathcal{R}_\theta$ representa a rede neural parametrizada pelos pesos $\theta$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

* **Otimização de Dose e Princípio ALARA:** A escolha criteriosa de filtros de reconstrução e algoritmos de processamento avançados permite a redução significativa da corrente do tubo de raios X (mAs) ou da tensão (kVp) sem comprometer a detectabilidade de lesões de baixo contraste (como em exames de fígado ou cérebro).
* **Controle de Qualidade (QC) e Metrologia:** Filtros inadequados podem introduzir artefatos de aliasing, *overshoot* (efeito de borda) ou suprimir estruturas anatômicas finas (como trabeculado ósseo ou pequenos nódulos pulmonares). A avaliação da Função de Transferência de Modulação (MTF) e do Ruído Espectral (NPS - *Noise Power Spectrum*) depende diretamente da análise dos filtros de reconstrução utilizados.
* **Redução de Artefatos:** Algoritmos de filtragem especializados são aplicados para mitigar artefatos de enrijecimento de feixe (*beam hardening*), artefatos metálicos (MAR - *Metal Artifact Reduction*) e ruído por fótons insuficientes em regiões de alta atenuação (ombros, pelve).
* **Radiômica e Quantificação:** Empregam-se filtros espaciais padronizados (como filtros de LoG - *Laplacian of Gaussian* com diferentes valores de escala $\sigma$) para extração de características de textura em análises radiômicas, garantindo reprodutibilidade na caracterização de fenótipos tumorais.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem|Reconstrução de Imagem em TC]]
* [[Filtro de Rampa e FBP]]
* [[Otimização de Dose em TC|Redução de Dose em TC]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Radiologia]]
* [[Física da Radiação e Dosimetria]]
* [[Controle de Qualidade em TC]]
* [[Artefatos em Tomografia Computadorizada]]