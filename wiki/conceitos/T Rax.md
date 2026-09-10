---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada\, dosimetria, radiodiagnostico, qualidade-da-imagem]
data: 2026-08-25
---

# tórax

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **tórax**, no contexto da Física Médica e da Tomografia Computadorizada (TC), representa uma das regiões anatômicas mais complexas e desafiadoras para a aquisição, processamento e otimização de imagens diagnósticas. Do ponto de vista anatômico, o compartimento torácico abriga órgãos de alta criticidade radiológica — como o coração, os grandes vasos, o mediastino e o parênquima pulmonar —, caracterizados por uma faixa extremamente ampla de atenuação aos raios X.

Fisicamente, a imagem de TC de tórax é governada pela interação da radiação ionizante com tecidos que apresentam coeficientes de atenuação linear ($\mu$) díspares. O parênquima pulmonar, predominantemente composto por ar alveolar, possui $\mu$ próximo ao do vácuo ($\mu \approx 0.0004 \text{ mm}^{-1}$ em condições de inspiração plena a 70-120 keV), enquanto as estruturas ósseas do arcabouço torácico (costelas, esterno e coluna vertebral) apresentam alta densidade eletrônica e número atômico efetivo ($Z_{\text{ef}}$) elevado, resultando em $\mu$ significativamente superiores. Adicionalmente, tecidos moles mediastinais e o sangue circulante ocupam uma faixa intermediária.

Essa heterogeneidade extrema gera desafios metrológicos severos:
1. **Dinâmica de Intensidade:** A transição abrupta entre o ar pulmonar e as estruturas ósseas compactas impõe uma exigência rigorosa à faixa dinâmica analógica-digital dos detectores de estado sólido (geralmente cintiladores de granada de gadolínio e cérmio - GOS ou cerâmica de óxido de terra rara) e à capacidade do sistema de conversão A/D.
2. **Artefatos de Endurecimento do Feixe (*Beam Hardening*):** Como o feixe de raios X policromático atravessa caminhos de alta densidade (como o mediastino e os ombros), os fótons de baixa energia são preferencialmente absorvidos\, deslocando o espectro médio para energias mais altas. Isso resulta em artefatos de faixa escura (*cupping artifact* ou bandas) entre as regiões de alta atenuação.
3. **Ruído Quântico Localizado:** O fluxo de fótons que atinge os detectores após atravessar o parênquima pulmonar é alto, gerando baixo ruído nessa região; em contrapartida, o feixe atenuado pelo mediastino e ombros sofre severa estocasticidade, resultando em degradação da razão sinal-ruído (SNR) e contraste-ruído (CNR) nas interfaces mediastinais.

## 2. Formulação Matemática e Propriedades

A modelagem da aquisição tomográfica do tórax baseia-se na lei da atenuação exponencial de feixes policromáticos. O sinal medido pelo detector na posição angular $\theta$ e posição linear $l$ é expresso pela transformada de Radon modificada para espectros poliméricos:

$$
I(l, \theta) = \int_{0}^{E_{\max}} I_0(E) \exp \left( -\int_{L(l, \theta)} \mu(x, y, E) \, ds \right) dE
$$

Onde:
- $I_0(E)$ é o espectro de energia inicial dos fótons de raios X gerados no anodo do tubo.
- $\mu(x, y, E)$ é o coeficiente de atenuação linear espacial e energético dependente.
- $L(l, \theta)$ representa a trajetória do raio linha que cruza o tórax.

Devido à ampla variação de $\mu$ no tórax, a reconstrução exige algoritmos robustos capazes de minimizar artefatos de truncamento e ruído estocástico. Seja $\mathcal{P}\{\mu\}$ o operador de projeção (sinograma). A reconstrução analítica tradicional por Retroprojeção Filtrada (*Filtered Back Projection* - FBP) é formulada como:

$$
f(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(l, \theta) |k| W(k) e^{2\pi i k l} dl \right]_{\text{backprojection}} \, d\theta
$$

Onde $W(k)$ é a função de filtro rampa modificada (por exemplo, Hann ou Hamming) aplicada para modular as altas frequências espaciais. No entanto, em exames de tórax de baixa dose, a FBP amplifica severamente o ruído de alta frequência. 

Para contornar isso, utilizam-se métodos iterativos avançados e Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR). A formulação de otimização para reconstrução iterativa penalizada (IR) minimiza a seguinte função de custo:

$$
\hat{\mu} = \arg\min_{\mu} \left\{ \frac{1}{2} \left\| Y - \mathcal{P}(\mu) \right\|_{\Sigma^{-1}}^{2} + \beta \mathcal{R}(\mu) \right\}
$$

Onde:
- $Y$ é o vetor de dados de projeção ruidosos.
- $\Sigma^{-1}$ é a matriz de ponderação estatística baseada na variância do fóton (modelo de ruído de Poisson-Gaussiano).
- $\mathcal{R}(\mu)$ é o termo de regularização (penalização espacial) projetado para preservar bordas finas das estruturas pulmonares (como fissuras e pequenas vias aéreas) enquanto suaviza o ruído no mediastino.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O exame de TC de tórax é o padrão-ouro para avaliação de patologias pulmonares difusas, nódulos pulmonares solitários, embolia pulmonar (Angio-TC de artérias pulmonares) e estadiamento oncológico. A otimização física e dosimétrica nessa região exige atenção meticulosa devido à sensibilidade radiológica de órgãos como as mamas, a glândula tireoide e o tecido medular ósseo ativo.

### Protocolos de Baixa Dose e Redução de Dose
Como o pulmão possui alto contraste natural intrínseco (tecido mole versus ar), a aquisição de tórax é primariamente otimizada para baixas correntes de tubo ($mA$) e tensões nominais reduzidas ($kVp$ baixo, tipicamente 70 a 100 kVp em sistemas modernos), o que simultaneamente aumenta o contraste fotoelétrico do meio de contraste iodado em exames angiográficos e reduz a dose absorvida. 

A métrica dosimétrica padrão para monitoramento é o Índice de Dose em Tomografia Computadorizada volumétrico ($\text{CTDI}_{\text{vol}}$) e o Produto Dose-Comprimento ($\text{DLP}$), calculados utilizando fantasmas cilíndricos padronizados de Poliestireno de 16 cm (equivalente à cabeça/pediátrico) ou 32 cm (equivalente ao corpo/tórax adulto):

$$
\text{CTDI}_{\text{vol}} = \frac{1}{pitch} \cdot \left( \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}} \right)
$$

### Controle de Qualidade e Observadores Computacionais
No controle de qualidade de rotina, a avaliação do tórax em simuladores físicos (*phantoms* antropomórficos) testa a capacidade do sistema em resolver detalhes de alto contraste (parênquima pulmonar, vasos subsegmentares) e baixo contraste (nódulos com atenuação em vidro despolimento — *ground-glass opacities*). 

Modelos de observadores computacionais, baseados na Função de Detetability Index ($d'$), frequentemente empregam o *Channelized Hotelling Observer* (CHO) para avaliar a detectabilidade de lesões pulmonares sutis sob diferentes algoritmos de reconstrução (FBP vs. DLR), correlacionando a física da formação da imagem com a acurácia diagnóstica observada clinicamente.

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Coeficiente de Atenuação Linear|coeficiente-de-atenuacao-linear]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-imagem-medica]]
- [[dosimetria-em-radiodiagnostico]]
- [[filtro-rampa-e-retroprojecao]]