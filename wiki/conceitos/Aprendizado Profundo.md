---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, aprendizado-profundo, reconstrucao-de-imagem\, dosimetria]
data: 2026-08-25
---

# aprendizado profundo

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **aprendizado profundo** (do inglês *Deep Learning* - DL) constitui uma subclasse avançada de [[Machine Learning|aprendizado de maquina]] baseada em redes neurais artificiais com múltiplas camadas de ocultação (*hidden layers*) entre a camada de entrada e a de saída. Diferentemente dos algoritmos tradicionais de aprendizado de máquina, que dependem fortemente de engenharia de características (*feature engineering*) manual e heurísticas baseadas em domínio, os modelos de aprendizado profundo possuem a capacidade inerente de realizar a extração hierárquica e automatizada de características diretamente a partir de dados brutos e multidimensionais.

No contexto da Física Médica e da [[Tomografia Computadorizada|tomografia-computadorizada]] (TC), o aprendizado profundo opera como um formalismo matemático altamente não linear capaz de mapear espaços de alta dimensionalidade. Fisicamente, os dados de entrada na TC frequentemente originam-se de medições de atenuação de fótons de raios-X por meio de projeções angulares (sinogramas), regidas pela Lei de Atenuação de Lambert-Beer e pela Transformada de Radon. O aprendizado profundo permite modelar inversões complexas e mal-postas (*ill-posed problems*) da física de imageamento, mitigando ruídos quânticos, artefatos de feixe policromático (*beam hardening*), artefatos de movimento e perdas associadas à subamostragem angular ou espacial.

Do ponto de vista metrológico, a aplicação de modelos de aprendizado profundo exige rigor metodológico estrito. Questões como calibração radiométrica, generalizabilidade, reprodutibilidade e mitigação de vieses (alucinações algorítmicas) são fundamentais para garantir a fidelidade quantitativa das imagens médicas, evitando que artefatos induzidos pela rede sejam confundidos com patologias reais ou comprometam a exatidão em medições dosimétricas e volumétricas.

---

## 2. Formulação Matemática e Propriedades

Uma rede neural profunda é composta por uma composição de funções matemáticas parametrizadas. Seja $\mathbf{x} \in \mathbb{R}^{d_{\text{in}}}$ o vetor de entrada (por exemplo, um pixel em uma imagem de TC ou um elemento de sinograma) e $\mathbf{y} \in \mathbb{R}^{d_{\text{out}}}$ a saída desejada (por exemplo, uma imagem reconstruída de alta resolução e baixo ruído). 

A arquitetura de uma rede feedforward profunda de $L$ camadas é definida recursivamente. Para a camada $l$ (onde $l \in \{1, 2, \dots, L\}$):

$$
\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}
\mathbf{a}^{(l)} = \sigma\left(\mathbf{z}^{(l)}\right)
$$

Onde:
- $\mathbf{a}^{(0)} = \mathbf{x}$ é a entrada da rede (camada 0).
- $\mathbf{W}^{(l)} \in \mathbb{R}^{n_l \times n_{l-1}}$ é a matriz de pesos sinápticos da camada $l$.
- $\mathbf{b}^{(l)} \in \mathbb{R}^{n_l}$ é o vetor de viés (*bias*) da camada $l$.
- $\mathbf{z}^{(l)}$ é a ativação linear intermediária.
- $\sigma(\cdot)$ é uma função de ativação não linear aplicada elemento a elemento, como a unidade linear retificada (ReLU)\, definida por $\sigma(z) = \max(0, z)$, ou variantes parametrizadas (LeakyReLU, GELU).
- $\mathbf{a}^{(l)}$ é o vetor de ativações da camada $l$.

A predição final da rede é expressa por $\hat{\mathbf{y}} = \mathbf{a}^{(L)}$. 

### Otimização e Função de Perda

O treinamento do modelo consiste em ajustar o conjunto global de parâmetros $\Theta = \left\{ \mathbf{W}^{(l)}, \mathbf{b}^{(l)} \right\}_{l=1}^L$ para minimizar uma função de perda (*loss function*) $\mathcal{L}(\Theta)$ em um conjunto de treinamento com $N$ amostras $\{(\mathbf{x}_i, \mathbf{y}_i)\}_{i=1}^N$:

$$
\Theta^* = \arg\min_{\Theta} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}\left( f(\mathbf{x}_i; \Theta), \mathbf{y}_i \right) + \lambda \Omega(\Theta)
$$

Onde:
- $f(\mathbf{x}_i; \Theta)$ representa a saída predita pela rede para a amostra $i$.
- $\Omega(\Theta)$ é um termo de regularização (como a norma $L_1$ ou $L_2$ dos pesos) utilizado para prevenir o sobreajuste (*overfitting*).
- $\lambda$ é o hiperparâmetro de regularização.

A otimização é primordialmente conduzida por algoritmos de gradiente descendente estocástico (SGD) ou otimizadores adaptativos (como Adam), utilizando o algoritmo de retropropagação (*backpropagation*) baseado na aplicação sucessiva da regra da cadeia do cálculo multivariado para computar o gradiente da perda em relação a cada parâmetro:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} \left(\mathbf{a}^{(l-1)}\right)^T
$$

No contexto de redes convolucionais (CNNs) — amplamente aplicadas em processamento de imagens de TC —, as multiplicações matriciais densas $\mathbf{W}^{(l)} \mathbf{a}^{(l-1)}$ são substituídas por operações de convolução discreta em 2D ou 3D, preservando a localidade espacial e reduzindo drasticamente o número de parâmetros livres.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O aprendizado profundo revolucionou o ecossistema da tomografia computadorizada, impactando desde a aquisição até a pós-processamento clínico:

1. **Reconstrução de Imagem Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*):**
   Algoritmos tradicionais como a Retroprojeção Filtrada ([[Retroprojeção Filtrada (FBP)|FBP]]) sofrem com artefatos de ruído quântico em doses baixas, enquanto a Reconstrução Iterativa ([[Reconstrução Iterativa|IR]]) computacionalmente custosa pode gerar texturas artificiais ("plásticas"). Abordagens de DLR operam em três domínios principais:
   - **Correção no domínio dos dados brutos (sinograma):** Reduz ruído estatístico e corrige inconsistências físicas antes da retroprojeção.
   - **Pós-processamento no domínio da imagem:** Redes convolucionais profundas (como redes U-Net) recebem imagens ruidosas geradas por FBP e aprendem a mapeá-las para imagens de referência de alta dose ou alta qualidade.
   - **Reconstrução híbrida/iterativa unificada:** Incorpora priors aprendidos por redes neurais diretamente dentro do ciclo de otimização iterativa.

2. **Otimização de Dose e Radioproteção:**
   Permite a implementação clínica viável de protocolos de baixa dose (*low-dose CT* - LDCT). Ao mitigar a degradação da relação sinal-ruído (SNR) inerente à redução de produto corrente-tempo ($mAs$), o aprendizado profundo viabiliza exames pediátricos e cardiológicos com menor risco radiobiológico, mantendo a detectabilidade de lesões de baixo contraste.

3. **Controle de Qualidade (CQ) e Dosimetria Computacional:**
   Redes neurais profundas são empregadas na segmentação automática de órgãos de risco, estimativa tridimensional de mapas de dose absorvida (*dose tracking*) através de simulações rápidas de Monte Carlo emuladas, e na detecção de desvios de calibração em scanners de TC por meio da análise de imagens de controle de qualidade (fantasmas).

4. **Observadores Computacionais:**
   Modelos de aprendizado profundo atuam como observadores ideais ou humanos simulados para avaliar a qualidade de imagem em tarefas específicas (como detecção de nódulos pulmonares), correlacionando métricas físicas com o desempenho diagnóstico real.

---

## 4. Conexões e Wikilinks

- [[Machine Learning|aprendizado de maquina]]
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Reconstrução Iterativa|IR]]
- [[Qualidade de Imagem em Tomografia Computadorizada]]
- [[Dosimetria em Radiologia|dosimetria em tomografia computadorizada]]
- [[Artefatos em Tomografia Computadorizada]]