---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal]
data: 2026-08-25
---

# Retroprojeção Filtrada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Retroprojeção Filtrada** (FBP — *Filtered Backprojection*) é o algoritmo analítico padrão ouro histórico e amplamente utilizado na reconstrução de imagens em Tomografia Computadorizada (TC) médica. Conceitualmente, a FBP resolve o problema inverso de recuperar uma função espacial bidimensional desconhecida — que representa o mapa de coeficientes de atenuação linear dos tecidos do paciente — a partir de um conjunto de projeções unidimensionais obtidas em múltiplos ângulos (o Sinograma).

Historicamente, a simples retroprojeção geométrica das projeções de volta ao plano da imagem resulta em uma representação borrada e de baixa qualidade diagnóstica. Esse artefato de borramento ocorre porque a retroprojeção direta pondera erroneamente as frequências espaciais, atenuando as altas frequências e amplificando a componente de baixa frequência na razão de $1/|r|$ no domínio espacial (onde $r$ é a distância radial). 

Para corrigir essa distorção física e matemática, a FBP introduz uma etapa de filtragem (convolução) das projeções unidimensionais antes da retroprojeção espacial. Esse filtro corretor, frequentemente denominado filtro rampa (*ramp filter*), atua como um realçador de bordas de alta frequência que compensa exatamente o desfoque inerente ao operador de retroprojeção, permitindo a recuperação quantitativa e espacialmente acurada do objeto escaneado.

## 2. Formulação Matemática e Propriedades

A formulação matemática da Retroprojeção Filtrada baseia-se diretamente no Teorema da Fatia Central (ou Teorema de Fourier para Projeções). 

Seja $f(x, y)$ a distribuição espacial do coeficiente de atenuação linear. A transformada de Radon de $f$, denotada por $P_\theta(t)$, representa a projeção obtida a um ângulo $\theta$, onde $t$ é a coordenada linear ao longo do detector:

$$
P_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

A transformada de Fourier unidimensional de $P_\theta(t)$ em relação à coordenada $t$ é dada por:

$$
S_\theta(\omega) = \mathcal{F}\{P_\theta(t)\} = \int_{-\infty}^{\infty} P_\theta(t) e^{-2\pi i \omega t} \, dt
$$

O Teorema da Fatia Central estabelece que $S_\theta(\omega)$ é exatamente igual à transformada de Fourier bidimensional de $f(x,y)$ avaliada ao longo de uma linha radial no domínio das frequências espaciais sob o ângulo $\theta$. 

Para recuperar $f(x,y)$ por meio da inversão da transformada de Radon, aplica-se a transformada de Fourier bidimensional inversa em coordenadas polares, o que resulta na equação fundamental da Retroprojeção Filtrada:

$$
f(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} S_\theta(\omega) |\omega| e^{2\pi i \omega t} \, d\omega \right]_{\theta = x\cos\theta + y\sin\theta} \, d\theta
$$

Definindo o termo interno entre colchetes como a projeção filtrada $\tilde{P}_\theta(t)$, temos:

$$
\tilde{P}_\theta(t) = P_\theta(t) * k(t)
$$

Onde $k(t)$ é o núcleo do filtro (*kernel*) correspondente à transformada de Fourier inversa de $|\omega|$ (o filtro rampa ideal). No domínio digital discreto, o filtro rampa perfeito gera ruído excessivo nas altas frequências, exigindo a multiplicação de $S_\theta(\omega)$ por funções de janela de corte (*apodization windows*), tais como os filtros de *Hamming*, *Hann*, *Butterworth* ou *Shepp-Logan*:

$$
H(\omega) = |\omega| \cdot W(\omega)
$$

A imagem reconstruída final é obtida pela retroprojeção dessas projeções filtradas por todos os ângulos de aquisição $\theta$:

$$
f(x, y) \approx \frac{\pi}{N_{\theta}} \sum_{i=1}^{N_{\theta}} \tilde{P}_{\theta_i} (x \cos\theta_i + y \sin\theta_i)
$$

Onde $N_{\theta}$ é o número total de projeções angulares.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em sistemas modernos de Tomografia Computadorizada, a FBP continua a desempenhar um papel crítico devido à sua extrema velocidade computacional, determinismo analítico e ausência de parâmetros de ajuste heurístico dependentes do paciente. Suas principais aplicações e interfaces metodológicas incluem:

* **Controle de Qualidade e Metrologia:** Por ser um algoritmo linear, a FBP preserva a relação linear entre o número CT (unidades Hounsfield) e o coeficiente de atenuação linear, sendo o método padrão exigido em protocolos de garantia da qualidade para avaliação de resolução espacial, ruído, linearidade e uniformidade.
* **Linha de Base para Reconstrução Iterativa (IR):** Embora algoritmos iterativos estatísticos (como ASiR, Veo, ADMIRE) e métodos baseados em Inteligência Artificial — Aprendizado Profundo para Reconstrução (DLR / *Deep Learning Reconstruction*) tenham superado a FBP em termos de redução de ruído em doses baixas, a FBP ainda é frequentemente utilizada para gerar a imagem inicial de estimativa (*seed image*) ou atua como termo de referência em funções de custo.
* **Desafios de Dosimetria e Ruído:** A principal limitação da FBP ocorre em cenários de baixa dose de radiação ionizante. Como o filtro rampa amplifica linearmente as altas frequências, o ruído quântico estatístico presente nos dados brutos é severamente potencializado, resultando em imagens granuladas com degradação da relação sinal-ruído (SNR). Isso impulsionou historicamente a transição para métodos que mitigam essa deficiência por meio de modelagem estatística de ruído e priors espaciais.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Sinograma]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Imagem Médica]]
* [[Unidades Hounsfield|Unidades Hounsfield]]
* [[Dosimetria em Radiologia]]
* [[Processamento de Sinal em Medicina]]