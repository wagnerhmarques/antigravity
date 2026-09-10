---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp]
data: 2026-08-25
---

# filtro-de-retroprojeccao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Filtro de Retroprojeção** (frequentemente associado ao algoritmo de *Filtered Back-Projection* ou FBP) é a pedra angular matemática e computacional da reconstrução analítica de imagens em Tomografia Computadorizada (TC) médica. Historicamente derivado do Teorema da Fatia Central (ou Teorema de Radon Direto), o processo de retroprojeção simples (*simple back-projection*) reconstrói o espaço objeto através do somatório (ou integração) de projeções adquiridas em múltiplos ângulos ao longo de uma trajetória de varredura.

Contudo, a retroprojeção simples padece de um grave artefato físico-matemático: a degradação espacial inerente à natureza geométrica da projeção, resultando em um perfil de indefinição espacial caracterizado por uma resposta impulsiva proporcional a $\frac{1}{r}$ no domínio espacial (onde $r$ é a distância radial). No domínio da frequência espacial, isso se traduz em um excesso de peso nas baixas frequências e uma atenuação severa nas altas frequências, gerando a clássica imagem borrada (*blurring*). 

Para corrigir essa distorção e recuperar a alta resolução espacial (nítida definição de bordas e estruturas anatômicas finas), aplica-se um filtro de rampa (*ramp filter*) unidimensional nas projeções no domínio de Fourier antes de realizar a operação de retroprojeção geométrica. Metrologicamente, o filtro atua como um equalizador de frequência espacial que compensa o fator de amostragem radial inerente à transformada de Radon, convertendo o sinal degradado em uma representação tomográfica quantitativamente precisa do coeficiente de atenuação linear $\mu(x,y)$ dos tecidos investigados.

## 2. Formulação Matemática e Propriedades

A formulação matemática do filtro de retroprojeção fundamenta-se na Transformada de Radon e no Teorema da Inversão de Radon. Seja $f(x,y)$ a distribuição espacial bidimensional do coeficiente de atenuação linear, e $p(\theta, t)$ o sinograma representando as projeções paralelas, onde $\theta$ é o ângulo de projeção e $t$ é a coordenada linear ao longo do detector, definida por:

$$
t = x \cos\theta + y \sin\theta
$$

A transformada de Radon bidimensional de $f(x,y)$ é expressa por:

$$
p(\theta, t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Pelo Teorema da Fatia Central, a transformada de Fourier unidimensional de uma projeção paralela $p(\theta, t)$ em relação à coordenada $t$, denotada por $P(\theta, \omega)$, corresponde exatamente a uma linha radial de valor $\omega$ na transformada de Fourier bidimensional de duas variáveis de $f(x,y)$, $F(\omega_x, \omega_y)$, avaliada no ângulo $\theta$:

$$
P(\theta, \omega) = \mathcal{F}_{1D}\{p(\theta, t)\} = \left. F(\omega_x, \omega_y) \right|_{\omega_x = \omega \cos\theta, \omega_y = \omega \sin\theta}
$$

Para recuperar $f(x,y)$ através da transformada inversa de Fourier em coordenadas polares, introduz-se o Jacobiano da transformação de coordenadas (que é $|\omega|$ ou $r$), atuando como o filtro de rampa ideal. A equação analítica contínua da Retroprojeção Filtrada (FBP) é dada por:

$$
f(x,y) = \int_{0}^{\pi} Q_\theta(x \cos\theta + y \sin\theta) \, \, d\theta
$$

Onde $Q_\theta(t)$ representa a projeção filtrada, obtida pela convolução ($*$) da projeção original $p(\theta, t)$ com um núcleo de filtro $h(t)$:

$$
Q_\theta(t) = p(\theta, t) * h(t) = \int_{-\infty}^{\infty} p(\theta, t - t') h(t') \, dt'
$$

No domínio da frequência, a função de transferência do filtro ideal de rampa é definida como:

$$
H(\omega) = |\omega|
$$

Onde $\omega$ representa a frequência espacial. Como o filtro de rampa ideal $|\omega|$ amplifica excessivamente o ruído de alta frequência (inerente à contagem de fótons de raios X e ruído eletrônico do sistema), filtros apodizados ou janelados são empregados na prática clínica para modular o balanço entre resolução espacial e supressão de ruído. Um filtro modificado genérico $H_{mod}(\omega)$ é expresso por:

$$
H_{mod}(\omega) = |\omega| \cdot W(\omega)
$$

Onde $W(\omega)$ representa uma função de janela (como *Hamming*, *Hann*, *Butterworth* ou *Cosine*). A propriedade central do filtro de retroprojeção é sua linearidade e determinismo, permitindo forte previsibilidade na propagação de ruído, embora seja altamente sensível a artefatos de feixe endurecido (*beam hardening*) e caindo em desvantagem em regimes de baixa dose onde o ruído estatístico domina.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No contexto clínico e industrial contemporâneo, o filtro de retroprojeção permanece como componente crítico na infraestrutura de processamento de imagem dos scanners de Tomografia Computadorizada, apesar do avanço de algoritmos iterativos e abordagens baseadas em inteligência artificial:

- **Velocidade de Reconstrução:** A natureza analítica e puramente determinística da FBP, acoplada à separação em etapas de filtragem 1D e retroprojeção (frequentemente aceleradas via hardware em unidades de processamento gráfico - GPUs), permite tempos de reconstrução em tempo quase real, essenciais para exames de alta demanda temporal como angiotomografias e perfusões cerebrais.
- **Controle de Qualidade (QC) e Metrologia:** Devido à sua linearidade matemática, a FBP é o método padrão ouro na metrologia de imagens para avaliar a Função de Espalhamento de Ponto (PSF), a Função de Transferência de Modulação (MTF), o Ruído Textural e o Espectro de Potência de Ruído (NPS) de sistemas de TC, sem os vieses introduzidos por não-linearidades de algoritmos iterativos.
- **Otimização de Dose e Dosimetria:** Embora a FBP amplifique o ruído quântico em baixas correntes de tubo (baixo mAs), serviu historicamente como base para estimativas de risco estocástico e protocolos de otimização (ALARA). Hoje, ela atua frequentemente em conjunto ou como termo de inicialização para algoritmos de Reconstrução Iterativa (IR) e Redes Neurais Profundas (DLR - *Deep Learning Reconstruction*).
- **Observadores Computacionais:** Estudos de detectabilidade em tarefas específicas utilizando observadores ideais ou humanos (como o *Channelized Hotelling Observer*) frequentemente utilizam imagens reconstruídas por FBP parametrizadas para isolar artefatos algorítmicos de artefatos introduzidos por modelos estatísticos de ruído.

## 4. Conexões e Wikilinks

- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Teorema da Fatia Central|teorema-da-fatia-central]]
- [[Transformada de Radon|transformada-de-radon]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]
- [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao]]
- [[Noise Power Spectrum|espectro-de-potencia-de-ruido]]
- [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]