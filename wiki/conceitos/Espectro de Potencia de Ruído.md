---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, ruido, qualidade-de-imagem, processamento-de-sinal]
data: 2026-08-25
---

# espectro-de-potencia-de-ruido

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Espectro de Potência de Ruído** (em inglês, *Noise Power Spectrum* - NPS), frequentemente referido na literatura clássica de engenharia de imagem como a Densidade Espectral de Potência (*Power Spectral Density* - PSD) do ruído, é uma métrica fundamental na Física Médica e na Tomografia Computadorizada (TC) para a caracterização espacial e estatística das flutuações de ruído em imagens digitais.

Enquanto a desvio padrão ou a variância global do ruído fornecem apenas uma medida escalar da magnitude do ruído (ignorando sua textura ou dependência espacial), o NPS descreve como a variância do ruído está distribuída no domínio das frequências espaciais. Em sistemas de TC modernos, o ruído não é puramente branco (estatisticamente independente e com distribuição uniforme de energia por frequência). Devido aos algoritmos de filtragem de retroprojeção (como o uso de filtros de rampa e apodização) e, mais drasticamente, aos algoritmos de reconstrução iterativa (IR) e inteligência artificial/reconstrução baseada em aprendizado profundo (DLR), o ruído sofre coloração (*noise coloring*). Isso significa que o NPS exibe texturas de ruído específicas, alterando a percepção visual do grão da imagem, a detectabilidade de lesões de baixo contraste e o desempenho de tarefas de diagnóstico executadas por humanos ou observadores computacionais.

Metrologicamente, o NPS é definido como a transformada de Fourier da função de autocorrelação espacial das flutuações de ruído em uma imagem estática ou homogênea.

## 2. Formulação Matemática e Propriedades (se aplicável)

Seja $I(x, y)$ a imagem reconstruída de um objeto perfeitamente homogêneo (como um fantoma cilíndrico de água ou polietileno), e $\Delta I(x, y) = I(x, y) - \mu$ a flutuação de ruído em cada pixel, onde $\mu$ é o valor médio do sinal na região de interesse (ROI). Assumindo um sistema bidimensional discretizado em uma matriz de $N \times N$ pixels com tamanhos de pixel $\Delta_x$ e $\elta_y$, o NPS bidimensional, denominado $W(u, v)$, é formalmente definido no domínio das frequências espaciais $(u, v)$ pela expectativa estatística do quadrado da magnitude da Transformada de Fourier bidimensional das flutuações de ruído:

$$
W(u, v) = \lim_{N \to \infty} \frac{\Delta_x \Delta_y}{N^2} E \left\{ \left| \sum_{n=1}^{N} \sum_{m=1}^{N} \Delta I(x_n, y_m) e^{-i 2\pi (u x_n + v y_m)} \right|^2 \right\}
$$

Na prática laboratorial e clínica, o NPS bidimensional é estimado a partir de múltiplas realizações independentes (fatias ou varreduras repetidas) ou por meio de técnicas de múltiplas ROIs em uma única imagem homogênea, utilizando o estimador de Período Modificado:

$$
W(u_k, v_l) = \frac{\Delta_x \Delta_y}{M_x M_y} \sum_{r=1}^{R} \left| \mathcal{F}_{2D} \left\{ \Delta I_r(x, y) \cdot W_{\text{win}}(x, y) \right\} \right|^2
$$

Onde:
- $\mathcal{F}_{2D}\{\cdot\}$ denota o operador de Transformada Rápida de Fourier 2D (FFT).
- $W_{\text{win}}(x, y)$ é uma função de janela de apodização (ex: Hann ou Hamming) aplicada para mitigar o vazamento espectral (*spectral leakage*) devido ao tamanho finito da ROI.
- $R$ é o número de amostras ou realizações independentes.

### Redução Radial (NPS 1D)
Como a maioria dos sistemas de aquisição e reconstrução de TC exibe simetria rotacional aproximada no plano axial, o NPS 2D é frequentemente convertido em um perfil unidimensional radial $W(f)$, integrando-se o NPS em coordenadas polares:

$$
W(f) = \int_{0}^{2\pico} W(f \cos\theta, f \sin\theta) \, \, d\theta
$$

Onde $f = \sqrt{u^2 + v^2}$ representa a frequência espacial radial (em ciclos por milímetro, $\text{cycles/mm}$).

### Propriedades Notáveis
1. **Invariância à Dose e Escala:** O valor absoluto do NPS escala inversamente com o quadrado da dose de radiação (produto corrente-tempo, mAs) em reconstruções lineares (FBP), refletindo a lei estatística de Poisson dos fótons de raios X.
2. **Momento Zero:** A integral do NPS 2D sobre todo o espaço de frequências espaciais é exatamente igual à variância espacial do ruído ($\sigma^2$) na imagem:

$$
\sigma^2 = \iint_{-\infty}^{\infty} W(u, v) \, du \, dv
$$

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O NPS é uma ferramenta indispensável no ciclo de vida de sistemas de Tomografia Computadorizada, atuando em frentes críticas:

- **Controle de Qualidade Avançado e Homologação de Scanners:** Permite avaliar o comportamento do sistema para além da simples medição do desvio padrão do ruído. Diferentes filtros de reconstrução (*kernels*) alteram drasticamente a frequência de corte do NPS, mudando o ruído de uma textura de grão fino para uma textura de grão grosso (frequências espaciais mais baixas).
- **Avaliação de Reconstruções Iterativas (IR) e IA (DLR):** Algoritmos avançados de reconstrução frequentemente exibem um NPS não-estacionário e não-linear, dependente do contraste local do objeto. O estudo do NPS sob diferentes níveis de dose ajuda a quantificar o fenômeno de "plastificação" ou perda de textura fina da imagem (*noise texture mismatch*), onde o ruído é suprimido em altas frequências, mas preserva texturas artificiais que podem mimetizar patologias ou mascarar microcalcificações.
- **Acoplamento com a FSD (Função de Espalhamento de Ponto - PSF) para Task-Based Image Quality:** A qualidade de imagem em TC moderna não pode ser isolada em resolução espacial (avaliada pela [[Modulation Transfer Function (MTF)|MTF]]) ou ruído (NPS). Ambas as métricas são sintetizadas no cálculo da Detectabilidade Neta ([[detectabilidade-ideal-e-humana|Detectability Index]]), utilizando [[Observadores de Modelo (Model Observers)|observadores computacionais]] (como o Observador de Hotelling Prewhitening), onde a matriz de covariância do ruído é diretamente derivada do NPS.
- **Otimização de Protocolos Clínicos:** Permite ajustar os parâmetros de varredura (kVp, mAs, filtros de reconstrução e fatores de regularização de IR/DLR) para maximizar a detectabilidade de lesões específicas (ex: nódulos pulmonares, metástases hepáticas) mantendo a dose de radiação tão baixa quanto razoavelmente exequível ([[Radioproteção|ALARA]]).

## 4. Conexões e Wikilinks

- [[Modulation Transfer Function (MTF)|Função de Transferência de Modulação (MTF)]]
- [[detectabilidade-ideal-e-humana|Detectabilidadde Ideal e Humana]]
- [[Observadores de Modelo (Model Observers)|Observadores Computacionais]]
- [[Reconstrução Iterativa|Reconstrução Iterativa]]
- [[reconstrucao-por-aprendizado-profundo|Reconstrução por Aprendizado Profundo (DLR)]]
- [[Qualidade de Imagem em TC|Qualidade de Imagem em Tomografia Computadorizada]]
- [[Radioproteção|Princípio ALARA e Dosimetria em TC]]