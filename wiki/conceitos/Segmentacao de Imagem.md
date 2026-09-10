---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, processamento-de-imagem, radioterapia]
data: 2026-08-25
---

# Segmentacao de Imagem

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A segmentação de imagem é o processo computacional de particionar uma imagem digital em múltiplos subconjuntos (segmentos ou regiões de interesse - *ROIs*), com o objetivo de simplificar ou alterar a representação da imagem em algo que seja mais significativo e fácil de analisar. No contexto da Física Médica e da Tomografia Computadorizada (TC), a segmentação visa isolar estruturas anatômicas específicas (como o fígado, os pulmões, o miocárdio ou lesões tumorais) do fundo e dos tecidos adjacentes, fundamentando-se nas propriedades radiométricas e espaciais dos voxels.

Do ponto de vista metrológico, a imagem de TC representa um mapa espacial tridimensional de coeficientes de atenuação linear efetivos, quantificados em unidades Hounsfield (HU):

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{agua}}}{\mu_{\text{agua}} - \mu_{\text{ar}}}
$$

A segmentação atua sobre este espaço métrico calibrado. Tecidos com assinaturas radiodensitárias distintas (por exemplo, osso cortical com alta atenuação, parênquima pulmonar com baixa atenuação e tecidos moles com atenuações intermediárias) podem, teoricamente, ser separados por limiares estatísticos (*thresholding*). Contudo, a heterogeneidade intrínseca dos tecidos biológicos, o ruído quântico inerente à aquisição tomográfica, artefatos de endurecimento de feixe (*beam hardening*), artefatos de movimento e o fenômeno de volume parcial (*partial volume effect*) tornam a segmentação baseada estritamente em limiares de HU insuficiente, exigindo abordagens avançadas baseadas em gradientes, topologia, otimização global e, modernamente, Inteligência Artificial (IA) e Aprendizado Profundo (*Deep Learning*).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, seja um domínio espacial tridimensional $\Omega \subset \mathbb{R}^3$ correspondente ao volume escaneado, e uma função de imagem de TC representada por $I: \Omega \to \mathbb{R}$, onde $I(x)$ denota o valor em unidades Hounsfield no voxel $x = (x_1, x_2, x_3)$. O objetivo da segmentação é encontrar uma partição do domínio $\Omega$ em $N$ regiões disjuntas $\Omega_i$ tais que:

$$
\bigcup_{i=1}^{N} \Omega_i = \Omega \quad \text{e} \quad \Omega_i \cap \Omega_j = \emptyset, \forall i 
eq j
$$

associando a cada voxel um rótulo $L(x) \in \{1, 2, \dots, N\}$.

### Modelos Variacionais e Contornos Ativos (*Active Contours / Level Sets*)
Uma das formulações clássicas mais rigorosas para a segmentação de estruturas anatômicas em TC é o modelo de Mumford-Shah e sua evolução através de contornos ativos baseados em conjuntos de nível (*Level Sets*), popularizado pelo modelo de Chan-Vese. 

O problema é formulado como a minimização de uma função de energia $E(C, c_1, c_2)$ em relação a uma fronteira fechada $C$ (interface entre o tecido de interesse e o fundo) e constantes aproximadas de intensidade $c_1$ e $c_2$ dentro e fora da região:

$$
E(c_1, c_2, C) = \mu \cdot \text{Length}(C) + 
u \cdot \text{Area}(\text{inside}(C)) + \lambda_1 \int_{\text{inside}(C)} \left| I(x) - c_1 \right|^2 dx + \lambda_2 \int_{\text{outside}(C)} \left| I(x) - c_2 \right|^2 dx
$$

Onde:
- $\text{Length}(C)$ e $\text{Area}(\text{inside}(C))$ são termos deregularização geométrica.
- $\mu, 
u, \lambda_1, \lambda_2$ são parâmetros de ponderação estipulados pelo físico ou otimizados empiricamente.

### Formulação por Redes Neurais Convolucionais (Deep Learning)
No paradigma atual de Inteligência Artificial, a segmentação é tratada como um mapeamento não-linear supervisionado de alta dimensionalidade. Dada uma rede parametrizada por pesos $\theta$, a função de probabilidade preditiva para um voxel pertencer à classe de interesse é dada por:

$$
\hat{P}(L(x) = 1 \mid I; \theta) = \sigma \left( f_{\theta}(I)(x) \right)
$$

Onde $\sigma$ é a função ativação *softmax* ou *sigmóide*. O treinamento da rede otimiza $\theta$ minimizando uma função de perda global, sendo a perda de Dice (*Dice Loss*) amplamente utilizada para lidar com o desbalanço de classes em imagens médicas (onde o órgão de interesse ocupa uma fração reduzida do volume total $\Omega$):

$$
\mathcal{L}_{\text{Dice}} = 1 - \frac{2 \sum_{x \in \Omega} Y(x)\hat{P}(x) + \epsilon}{\sum_{x \in \Omega} Y(x) + \sum_{x \in \Omega} \hat{P}(x) + \epsilon}
$$

Onde $Y(x) \in \{0, 1\}$ representa a máscara ground-truth (anotação especialista) e $\epsilon$ é um parâmetro de suavização infinitesimal para evitar divisão por zero.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A segmentação de imagem constitui um pilar tecnológico indispensável em diversos domínios da Física Médica e da Tomografia Computadorizada:

1. **Radioterapia Externa e Planejamento de Tratamento (TPS):** A segmentação precisa de volumes alvo tumorais (GTV, CTV, PTV) e órgãos em risco (OARs - *Organs at Risk*, como medula espinhal, tronco cerebral, parótidas) é mandatório para a distribuição otimizada de dose por feixes de radiação modulada (IMRT e VMAT). Erros de segmentação propagam-se diretamente para os histogramas Dose-Volume (DVH), podendo induzir toxicidade severa ou subdosagem tumoral.
2. **Dosimetria Baseada em Imagem e Correção de Atenuação em PET/CT:** Na fusão multimodal (PET/CT), a segmentação dos mapas de atenuação derivados da TC é usada para gerar os fatores de correção de atenuação (*ACF*) necessários para quantificar corretamente a atividade radioativa no PET. Em medicina nuclear terapêutica (teranóstica), a segmentação de órgãos em séries temporais de TC/SPECT permite o cálculo dosabsorbed doses em nível voxel (*voxel-based dosimetry*).
3. **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Algoritmos avançados de reconstrução utilizam priors de segmentação ou penalizações baseadas em estruturas anatômicas segmentadas para preservar bordas e suprimir ruído estatístico em exprotocols de baixa dose (*low-dose CT*).
4. **Radiômica e Extração de Biomarcadores Quantitativos:** A radiômica baseia-se na extração de centenas de features de textura, forma e intensidade de volumes segmentados de lesões em TC para predizer respostas a tratamentos oncológicos ou subtipos genéticos de forma não-invasiva.
5. **Controle de Qualidade Automatizado (QA):** Ferramentas de segmentação baseadas em IA automatizam a análise de fantomas de controle de qualidade em TC, medindo automaticamente parâmetros como modulação de função de transferência de modulação (MTF), ruído e uniformidade sem intervenção humana.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Unidades Hounsfield|Unidade Hounsfield]]
- [[Reconstrução de Imagem|Reconstrucao de Imagem]]
- [[Retroprojeção Filtrada (FBP)|Filtro de Retroprojecao]]
- [[CNNs|Redes Neurais Convolucionais]]
- [[Radioterapia]]
- [[Dosimetria]]
- [[Radiomica|Radiomica]]
- [[Controle de Qualidade em TC]]
- [[Efeito de Volume Parcial]]