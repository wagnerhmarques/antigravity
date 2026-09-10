---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, fbp, processamento-de-sinal]
data: 2026-08-25
---

# filtragem-e-retroprojecao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Retroprojeção Filtrada** (em inglês, *Filtered Backprojection* - FBP) é o algoritmo analítico padrão ouro clássico utilizado na reconstrução de imagens em Tomografia Computadorizada (TC) de raios X. Fisicamente, a aquisição de dados em TC baseia-se na medição da atenuação dos fótons de raios X ao longo de linhas retas (percursos dos raios), mapeando o coeficiente de atenuação linear interno do objeto tridimensional sob a forma de projeções paralelas ou em leque, conhecidas matematicamente como a **Transformada de Radon**.

A retroprojeção simples (*simple backprojection*), que consiste em acumular e reescrever os valores de projeção de volta ao longo do caminho em que foram adquiridos, resulta inerentemente em uma imagem borrada. O fenômeno de borramento ocorre porque a retroprojeção simples atua como um filtro passa-baixas implícito no domínio espacial, cuja resposta ao impulso decai com a recíproca da distância radial ($1/r$). Para corrigir esse artefato físico e matemático, aplica-se um filtro de rampa (*ramp filter*) no domínio de Fourier das projeções antes de realizar a retroprojeção geométrica. Esse processo elimina o borramento $1/r$, recuperando a alta frequência espacial e a nitidez estrutural necessárias para a diferenciação de tecidos de alta e baixa atenuação na prática clínica.

Do ponto de vista metrológico, a FBP é determinística e linear. Ela preserva a fidelidade quantitativa dos números de tomografia (unidades Hounsfield - HU), permitindo a avaliação precisa de densidades teciduais, desde que os artefatos de enrijecimento de feixe (*beam hardening*), ruído quântico e espalhamento (*scatter*) sejam devidamente corrigidos durante o pré-processamento dos dados brutos (*raw data*).

---

## 2. Formulação Matemática e Propriedades

No sistema de coordenadas cartesianas bidimensionais, seja $f(x, y)$ a distribuição espacial do coeficiente de atenuação linear a ser reconstruída. A Transformada de Radon de $f(x, y)$, denotada por $P(\theta, t)$, representa a projeção obtida sob um ângulo $\theta$, onde $t$ é a coordenada de posição linear ao longo do detector:

$$
P(\theta, t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

O Teorema da Seção Central (ou Teorema do Slice-Theorem) estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $P(\theta, t)$ em relação à coordenada espacial $t$ é exatamente igual à fatia radial bidimensional da Transformada de Fourier bidimensional da imagem original $F(\omega_x, \omega_y)$, avaliada ao longo do ângulo $\theta$:

$$
S(\theta, \omega) = \int_{-\infty}^{\infty} P(\theta, t) \, e^{-i 2\pi \omega t} \, dt = F(\omega \cos\theta, \omega \sin\theta)
$$

Para recuperar a função original $f(x, y)$ a partir de suas projeções, aplica-se a inversão da Transformada de Radon. Na formulação contínua da Retroprojeção Filtrada, a imagem reconstruída é dada por:

$$
f(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} S(\theta, \omega) \, |\omega| \, e^{i 2\pi \omega t} \, d\omega \right]_{\substack{t = x \cos\theta + y \sin\theta}} \, d\theta
$$

O termo $|\omega|$ é o **filtro de rampa ideal** no domínio da frequência. Como a função rampa possui suporte infinito e amplifica severamente o ruído de alta frequência presente nas medições reais, filtros apodizados (ou janelados) são multiplicados ao filtro de rampa para controlar a resolução espacial em detrimento do ruído. As variantes analíticas mais comuns incluem:

* **Filtro de Hann:** 
  
$$
H(\omega) = |\omega| \cos^2\left(\frac{\pi \omega}{2 \omega_c}\right) \quad \text{para} \quad |\omega| \le \omega_c
$$

* **Filtro de Hamming:** 
  
$$
H(\omega) = |\omega| \left[ 0.54 + 0.46 \cos\left(\frac{\pi \omega}{\omega_c}\right) \right] \quad \text{para} \quad |\omega| \le \omega_c
$$

* **Filtro de Shepp-Logan:** 
  
$$
H(\omega) = |\omega| \left| \frac{\sin(\pi \omega / 2\omega_c)}{\pi \omega / 2\omega_c} \right| \quad \text{para} \quad |\omega| \le \omega_c
$$

Onde $\omega_c$ representa a frequência de corte de Nyquist do sistema de detecção.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A FBP constituiu a espinha dorsal tecnológica da tomografia computadorizada desde as suas primeiras gerações comerciais até a transição para a aquisição helicoidal (espiral) e multi-slice (MDCT). Suas principais características operacionais no ambiente clínico e de pesquisa incluem:

* **Velocidade Computacional:** Devido à sua natureza puramente analítica e linear, a FBP exige baixa complexidade computacional ($O(N^3)$ para reconstrução da matriz ou $O(N^2 \log N)$ utilizando algoritmos baseados em FFT), permitindo a reconstrução quase instantânea de imagens, o que é mandatório em exames de emergência e perfusão.
* **Controle de Qualidade e Metrologia:** Por não incorporar modelos estatísticos complexos ou regularizações não-lineares, a FBP garante uma resposta espacial homogênea e previsível. É o método de referência para a avaliação de parâmetros de Controle de Qualidade (CQ), como a Função de Transferência de Modulação (MTF), o Ruído Padrão, a Linearidade dos Números de Tomografia e a Curva de Limite de Detecção de Baixo Contraste em fantomas padronizados (ex: ACR, Catphan).
* **Limitações na Otimização da Dose:** Em doses baixas de radiação, o ruído quântico e o efeito de aliasing discreto tornam-se proeminentes na FBP, gerando artefatos de granulação severa ("salt and pepper") e estrias (*streak artifacts*). Isso limitou a sua capacidade de atingir reduções drásticas de dose sem comprometer o diagnóstico.
* **Transição para Métodos Avançados:** Embora a FBP continue a ser implementada em tempo de execução para monitoramento rápido, ela tem sido gradualmente suplementada ou substituída em protocolos de baixa dose por técnicas de Reconstrução Iterativa (IR - *Iterative Reconstruction*) e, mais recentemente, por Reconstruções Baseadas em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*), que utilizam redes neurais para suprimir o ruído mantendo a textura anatômica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Transformada de Radon|transformada-de-radon]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Aprendizado Profundo em TC|aprendizado-profundo-em-tc]]
* [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
* [[Unidades Hounsfield|unidades-hounsfield]]
* [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao]]
* [[Dosimetria em TC|dosimetria-em-tc]]