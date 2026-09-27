> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Função de Espalhamento de Borda (ESF)|funcao-de-espalhamento-de-borda-esf]], [[Função de Espalhamento de Ponto (PSF)|funcao-de-espalhamento-de-ponto-psf]], [[Resolução Espacial]], [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]

> 📅 **Data:** 2026-08-25 | 🔗 **Conexões:** [[Resolução Espacial]], [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Espalhamento de Borda** (ESF - *Edge Spread Function*) representa a resposta de um sistema de imagem médica — como um scanner de Tomografia Computadorizada (TC) — a uma interface ideal de degrau (mudança abrupta e unidimensional entre dois níveis de atenuação distintos, simulando uma borda perfeita entre materiais de diferentes densidades). Na metrologia de sistemas de imagem, a ESF descreve como a descontinuidade matemática de uma borda ideal é suavizada e espalhada espacialmente devido à finura do ponto focal do tubo de raios X, à finiteza do tamanho do pixel e aos filtros de reconstrução aplicados.

A obtenção da ESF é uma etapa intermediária e fundamental na cadeia de avaliação da **[[Resolução Espacial]]**. Devido à dificuldade prática de fabricar e alinhar um fio infinitamente fino necessário para medir diretamente a **[[Função de Espalhamento de Ponto (PSF)|funcao-de-espalhamento-de-ponto-psf]]**, a ESF é frequentemente preferida em protocolos de controle de qualidade e metrologia clínica por utilizar fantomas com interfaces planas de alto contraste (como placas de teflon, poliestireno ou tungstênio imersas em água).

## 2. Formulação Matemática e Propriedades

Matematicamente, a ESF é modelada como a integração espacial da **Função de Espalhamento de Linha** (LSF - *Line Spread Function*) ao longo de uma direção transversal à borda. Sendo $h(x)$ a LSF unidimensional do sistema de imagem, a ESF, denotada por $E(x)$, é expressa por:

$$
E(x) = \int_{-\infty}^{x} h(x') \\, dx'
$$

De forma inversa, a Função de Espalhamento de Linha pode ser obtida calculando-se a derivada primeira da ESF em relação à coordenada espacial $x$:

$$
h(x) = \frac{d}{dx} E(x)
$$

No domínio das frequências espaciais, a relação analítica permite conectar a ESF diretamente à **[[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]**. Aplicando a Transformada de Fourier à derivada da ESF, obtém-se a MTF:

$$
\text{MTF}(u) = \left| \mathcal{F} \left\{ \frac{d}{dx} E(x) \right\} \right|
$$

Onde:
- $E(x)$ é a **Função de Espalhamento de Borda** medida experimentalmente.
- $h(x)$ é a **Função de Espalhamento de Linha (LSF)**.
- $u$ é a frequência espacial expressa em ciclos por centímetro ($\text{ciclos/cm}$) ou pares de linhas por centímetro ($\text{lp/cm}$).
- $\mathcal{F}$ denota o operador de Transformada de Fourier.

### Propriedades Metrológicas Relevantes:
- **Sensibilidade ao Ruído:** Como a ESF envolve um processo de integração espacial dos dados da imagem, ela apresenta menor sensibilidade ao ruído estocástico flutuante em comparação à medição direta da PSF ou da LSF.
- **Derivada Numérica:** A necessidade de calcular a derivada primeira da ESF para extrair a LSF exige procedimentos rigorosos de suavização (*smoothing*) para evitar a ampliação de artefatos de alta frequência causados por ruído de quantização.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A ESF é amplamente utilizada na avaliação quantitativa de desempenho de sistemas de Tomografia Computadorizada no contexto do projeto de tese em física médica e controle de qualidade hospitalar (InRad-HCFMUSP):

1. **Caracterização de Kernels de Reconstrução:** Permite quantificar o impacto de diferentes funções de filtro (*sharp* vs. *smooth*) sobre a nitidez de bordas e o comportamento da alta frequência espacial.
2. **Avaliação de Algoritmos Avançados (IR e DLR):** Permite mensurar a preservação de bordas e estruturas anatômicas finas ao comparar imagens obtidas por **[[Reconstrução Iterativa|reconstrucao-iterativa]]** e **[[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]** frente aos padrões tradicionais de **[[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada-fbp]]**.
3. **Padronização Metrológica:** Serve como base computacional para softwares automatizados de garantia da qualidade que calculam a MTF de rotina em tomógrafos clínicos multislice e de contagem de fótons (**[[Photon Counting Detector CT (PCD-CT)]]**).

## 4. Conexões e Wikilinks

- [[Resolução Espacial]]
- [[Função de Espalhamento de Ponto (PSF)|funcao-de-espalhamento-de-ponto-psf]]
- [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
- [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada-fbp]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Controle de Qualidade em TC]]
