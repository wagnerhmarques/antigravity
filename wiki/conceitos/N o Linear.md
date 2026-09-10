---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, processamento-de-sinal, reconstrucao-iterativa, inteligencia-artificial, nao-linearidade]
data: 2026-08-25
---

# não linear

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Física Médica, da Tomografia Computadorizada (TC) e da Inteligência Artificial aplicada à imagem, o termo **não linear** descreve sistemas, operadores, transformações ou respostas cujas saídas não são proporcionalmente escaladas ou diretamente superponíveis às suas entradas. Matematicamente, um operador $\mathcal{H}$ é classificado como não linear se violar pelo menos uma das duas propriedades fundamentais da linearidade: **homogeneidade** (ou escalamento) e **aditividade** (princípio da superposição).

Enquanto sistemas lineares são regidos por convoluções e matrizes de projeção lineares (como o modelo idealizado da Transformada de Radon), a cadeia de aquisição, processamento e reconstrução na TC moderna é profundamente marcada por fenômenos e algoritmos não lineares. 

Do ponto de vista físico e metrológico, a não linearidade manifesta-se em diversos estágios:
* **Física da Aquisição:** O feixe de raios X policromático sofre **endurecimento do feixe** (*beam hardening*), fazendo com que o coeficiente de atenuação linear efetivo $\mu$ dependa do caminho percorrido pelo fóton através do objeto, quebrando a linearidade da lei de Lambert-Beer para espectros contínuos.
* **Estatística de Ruído e Contagem:** A contagem de fótons detectados obedece à estatística de Poisson. A subsequente transformação logarítmica aplicada aos dados brutos para estimar as projeções lineares transforma a distribuição de ruído, tornando-o dependente do sinal e heteroscedástico.
* **Reconstrução e Processamento:** Métodos avançados de reconstrução, como a **Reconstrução Iterativa (IR)** com penalização baseada em bordas (ex: variação total - *Total Variation*) e algoritmos de **Aprendizado Profundo (Deep Learning Reconstruction - DLR)**, empregam funções de ativação não lineares (ex: ReLU, GELU), limiares (*thresholding*) e regularizadores espaciais. Isso faz com que a resolução espacial, a textura do ruído e a detectabilidade de lesões passem a depender da dose de radiação e do contraste local da imagem, invalidando o uso estrito da Função de Dispersão do Ponto (PSF) linear e invariante no espaço (LSIV).

---

## 2. Formulação Matemática e Propriedades

Seja um operador de sistema $\mathcal{H}$ que mapeia um espaço de entrada (espaço de funções ou vetores) para um espaço de saída. Dizemos que $\mathcal{H}$ é **não linear** se existirem entradas $\mathbf{x}_1, \mathbf{x}_2$ e um escalar $\alpha$ tais que:

1. **Falha na Aditividade:**

$$
\mathcal{H}\{\mathbf{x}_1 + \mathbf{x}_2\} 
eq \mathcal{H}\{\mathbf{x}_1\} + \mathcal{H}\{\mathbf{x}_2\}
$$

2. **Falha na Homogeneidade:**

$$
\mathcal{H}\{\alpha \mathbf{x}\} 
eq \alpha \mathcal{H}\{\mathbf{x}\}
$$

Em tomografia computadorizada avançada, consideremos um operador de reconstrução não linear $\mathcal{R}_{\text{NL}}$ que reconstrói a imagem $\mathbfmu$ a partir dos dados de projeção ruidosos $\mathbf{y}$:

$$
\mathbf{\mu} = \mathcal{R}_{\text{NL}}(\mathbf{y})
$$

Em métodos baseados em otimização regularizada (como *Compressed Sensing* ou *Total Variation*), o problema inverso é formulado como a minimização de uma função custo que frequentemente inclui termos de penalização não diferenciáveis ou não lineares:

$$
\hat{\mathbf{\mu}} = \arg\min_{\mathbf{\mu}} \left\{ \frac{1}{2} \left\| \mathbf{A}\mathbf{\mu} - \mathbf{y} \right\|_{\Sigma^{-1}}^2 + \lambda \mathcal{R}(\mathbf{\mu}) \right\}
$$

Onde:
* $\mathbf{A}$ é a matriz de projeção do sistema (sistema linear de Radon discretizado).
* $\mathbf{y}$ vetor de projeções log-transformadas.
* $\Sigma^{-1}$ é a matriz de ponderação estatística baseada na variância dos fótons (tratando a não linearidade estatística).
* $\mathcal{R}(\mathbf{\mu})$ é o regularizador espacial **não linear** (por exemplo, a norma $L_1$ dos gradientes da imagem, $\|
abla \mathbf{\mu}\|_1$, ou penalizações baseadas em *patch* não locais).
* $\lambda$ é o hiperparâmetro de regularização.

Em redes neurais profundas utilizadas para DLR ou denoising, a operação em cada camada $l$ é dada por:

$$
\mathbf{z}^{(l)} = f\left( \mathbf{W}^{(l)} \mathbf{z}^{(l-1)} + \mathbf{b}^{(l)} \right)
$$

Onde $f(\cdot)$ é uma função de ativação **não linear** (por exemplo, $\text{ReLU}(x) = \max(0, x)$). A composição sucessiva dessas funções confere à rede a capacidade de mapear relações altamente complexas e não lineares entre dados corrompidos por ruído/artefatos e imagens de alta qualidade de referência.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A transição paradigmática de algoritmos estritamente lineares (como a Retroprojeção Filtrada - FBP) para abordagens computacionais **não lineares** revolucionou a dosimetria e o controle de qualidade na TC moderna:

* **Gerenciamento de Dose e Redução de Ruído:** Algoritmos de reconstrução iterativa e redes neurais DLR exploram propriedades não lineares para suprimir o ruído quântico em regiões homogêneas de baixa dose, enquanto preservam bordas anatômicas nítidas. Em sistemas lineares tradicionais, a redução de ruído inevitablementefazia o borramento (*blurring*) estrutural.
* **Complexidade na Metrologia e CQ:** A não linearidade introduz desafios significativos para o controle de qualidade físico-médico. Parâmetros tradicionais como a Modulação da Função de Transferência (MTF) e a Curva de Indicação de Ruído (NPS), que dependem da linearidade e da estacionaridade do sistema, deixam de ser constantes universales. A resolução espacial e a resolução de baixo contraste em imagens reconstruídas por métodos não lineares passam a ser dependentes do nível de sinal (amplitude do objeto) e da dose, exigindo o desenvolvimento de métricas baseadas em observadores computacionais e tarefas específicas (ex: *Task-based MTF* e *Detectability Index*).
* **Correção de Artefatos:** Técnicas de correção de feixe policromático e de endurecimento iterativo exigem modelos físicos não lineares para estimar a atenuação espectral correta dos tecidos (osso, água, meio de contraste iodado).

---

## 4. Conexões e Wikilinks

* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Transformada de Radon|transformada-de-radon]]
* [[filtros-e-kernels]]
* [[Ruído Quântico|ruido-quantico]]
* [[dose-em-tc]]
* [[funcao-de-dispersao-do-ponto]]
* [[total-variation]]