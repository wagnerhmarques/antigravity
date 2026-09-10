---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, nps, processamento-de-sinal]
data: 2026-08-25
---

# espectro-de-potencia-do-ruido-nps

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Espectro de Potência do Ruído** (*Noise Power Spectrum* - NPS), frequentemente referido na literatura clássica de engenharia elétrica e processamento de imagem como a **Função de Densidade Espectral de Potência** (*Power Spectral Density* - PSD) do ruído, é uma métrica fundamental na Física Médica para a caracterização quantitativa e espacial das flutuações de intensidade (ruído) em imagens médicas digitais, com ênfase primordial em [[Tomografia Computadorizada|tomografia-computadorizada-tc]].

Enquanto a variância global do ruído ($\sigma^2$) fornece apenas uma medida escalar da magnitude das flutuações de pixel (o "quanto" ruído existe na imagem), o NPS provê uma descrição completa e detalhada em função da frequência espacial (o "como" o ruído está distribuído espacialmente). Em Tomografia Computadorizada, o ruído não é tipicamente branco (estatisticamente independente e uniformemente distribuído por todas as frequências espaciais); ele sofre modificações severas decorrentes da filtragem rampa (*ramp filter*) e dos filtros de retroprojeção aplicados durante a [[reconstrucao-por-retroprojecao-filtrada-fbp]], bem como dos algoritmos não-lineares de [[Reconstrução Iterativa|reconstrucao-iterativa-ir]] e [[reconstrucao-por-aprendizado-profundo-dlr]].

Metrologicamente, o NPS quantifica a variância do ruído decomposta em suas componentes de frequência espacial bidimensionais ($u, v$) ou tridimensionais. A relevância clínica e física desta métrica reside no fato de que o olho humano e os observadores computacionais possuem sensibilidade dependente da frequência espacial ao ruído. Ruídos de baixa frequência espacial manifestam-se visualmente como granulações grosseiras ou "manchas" (*mottle*), que podem mimetizar lesões reais de baixo contraste, enquanto ruídos de alta frequência aparecem como uma granulação fina ("sal e pimenta"), facilmente mascarada pelo sistema visual humano ou atenuada por funções de transferência de modulação (*MTF*). Portanto, duas imagens com exatamente a mesma desvio-padrão de ruído ($\sigma$) podem apresentar desempenhos diagnósticos radicalmente distintos se os seus NPS forem diferentes.

---

## 2. Formulação Matemática e Propriedades

Seja $\Delta(x, y)$ o mapa bidimensional de ruído em uma região de interesse (ROI) homogênea de uma imagem de Tomografia Computadorizada. O mapa de ruído é obtido subtraindo-se o valor médio local ou a imagem de sinal determinístico (frequentemente estimada através de médias de múltiplos scans de um fantoma homogêneo) da imagem ruidosa observada $I(x, y)$:

$$
\Delta(x, y) = I(x, y) - \bar{I}(x, y)
$$

O Espectro de Potencia do Ruído bidimensional, $\text{NPS}(u, v)$, é formalmente definido como o limite do valor esperado do quadrado da magnitude da transformada de Fourier bidimensional do ruído truncado, normalizado pela área da ROI ($L_x \times L_y$):

$$
\text{NPS}(u, v) = \lim_{L_x, L_y \to \infty} \frac{1}{L_x L_y} E \left\{ \left| \iint_{L_x, L_y} \Delta(x, y) e^{-j 2 \pi (u x + v y)} \, dx \, dy \right|^2 \text{ \right\} }
$$

Onde:
* $u$ e $v$ representam as frequências espaciais nas direções $x$ e $y$ (tipicamente expressas em $\text{mm}^{-1}$ ou $\text{cycles/cm}$).
* $E\{\cdot\}$ denota o operador de valor esperado (enamble average), estimado na prática através da média de múltiplas realizações independentes de ruído (múltiplos cortes ou varreduras de fantomas).
* $\Delta(x,y)$ é a flutuação do número Hounsfield (HU) ou coeficiente de atenuação linear.

Na prática computacional discreta, dada uma matriz de imagem digital com dimensões $N \times N$ e tamanho de pixel $\Delta_x$, a estimativa empírica do NPS bidimensional via Transformada Rápida de Fourier (FFT) é calculada como:

$$
\text{NPS}(u_i, v_j) = \frac{\Delta_x \Delta_y}{N_x N_y} \sum_{k=1}^{K} \left| \sum_{m=0}^{N_x-1} \sum_{n=0}^{N_y-1} \Delta_k(x_m, y_n) e^{-j 2 \pi \left(\frac{i m}{N_x} + \frac{j n}{N_y}\right)} \right|^2
$$

Onde $K$ é o número de realizações independentes (amostras de ROI) utilizadas para reduzir a variância estatística da estimativa do próprio espectro.

### Redução a NPS Unidimensional (Radial)
Devido à simetria azimutal frequentemente encontrada em sistemas de TC de gantry circular, o NPS 2D é muitas vezes convertido em um perfil unidimensional $\text{NPS}(f)$, onde $f = \sqrt{u^2 + v^2}$, através de amostragem em coordenadas polares ou integração radial:

$$
\text{NPS}(f) = \int_{0}^{2\pi} \text{NPS}(f \cos\theta, f \sin\theta) \, \, d\theta
$$

### Propriedade Fundamental de Conservação da Variância
A integral (ou somatório) do NPS sobre todo o domínio de frequência espacial é matematicamente rigorosa e igual à variância do ruído $\sigma^2$ na imagem espacial:

$$
\sigma^2 = \iint_{-\infty}^{\infty} \text{NPS}(u, v) \, du \, dv
$$

Esta propriedade serve como teste de consistência metrológica para algoritmos de cálculo de NPS.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### Controle de Qualidade e Metrologia de Sistemas
O NPS é uma ferramenta indispensável no controle de qualidade avançado de scanners de Tomografia Computadorizada. Permite monitorar a integridade dos componentes do sistema, a estabilidade do tubo de raios X, os algoritmos de correção de feixe policromático (*beam hardening*) e os efeitos de pós-processamento. Alterações no hardware ou falhas em canais de detetores manifestam-se frequentemente como picos espúrios ou anisotropias direcionais no NPS 2D (anomalias conhecidas como artefatos de anel ou estrias que alteram o espectro de potência).

### Avaliação de Algoritmos de Reconstrução (FBP vs. IR vs. DLR)
Com a evolução tecnológica, a transição da retroprojeção filtrada tradicional para a [[Reconstrução Iterativa|reconstrucao-iterativa-ir]] e, subsequentemente, para a [[reconstrucao-por-aprendizado-profundo-dlr]] alterou drasticamente a textura da imagem. 
* A **FBP** produz um NPS característico que segue rigorosamente o filtro rampa na alta frequência.
* A **IR** introduz não-linearidades espaciais, resultando tipicamente em uma depressão do NPS em altas frequências (suavização seletiva) e dependência do nível de sinal (o ruído muda dependendo se o tecido é denso ou adiposo).
* A **DLR** (redes neurais convolucionais treinadas para redução de ruído) frequentemente gera formas de NPS altamente complexas, por vezes suprimindo faixas inteiras de frequência espacial, o que pode induzir uma aparência visual "plástica" ou textura não natural se não for rigorosamente calibrada.

### Otimização da Dose de Radiação e Detectabilidade de Lesões
Na busca contínua pela otimização de protocolos sob o princípio ALARA (*As Low As Reasonably Achievable*), o NPS é combinado com a [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]] para o cálculo da [[detectabilidade-de-baixo-contraste-nрd-ncdd]] e métricas baseadas na [[teoria-dos-observadores-computacionais-ideal-observer]]. O desempenho de um observador humano ou matemático (como o *Channelized Hotelling Observer* - CHO) na tarefa de detecção de lesões de baixo contraste (ex: nódulos hepáticos hipodensos) depende diretamente da razão entre o quadrado da MTF (sinal) e o NPS (ruído) em cada frequência espacial, métrica formalizada pela **Detectabilidade Detectora (Detectability Index - $d'$ )**:

$$
d'^2 = \iint \frac{|\text{MTF}(u, v)|^2 |\text{W}(u, v)|^2}{\text{NPS}(u, v)} \, du \, dv
$$

Onde $\text{W}(u, v)$ representa a transformada de Fourier do perfil da lesão a ser detectada.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada-tc]]
* [[reconstrucao-por-retroprojecao-filtrada-fbp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa-ir]]
* [[reconstrucao-por-aprendizado-profundo-dlr]]
* [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
* [[teoria-dos-observadores-computacionais-ideal-observer]]
* [[detectabilidade-de-baixo-contraste-nрd-ncdd]]
* [[dose-e-qualidade-de-imagem-em-tc]]