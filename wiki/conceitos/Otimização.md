---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem\, dosimetria, controle-de-qualidade]
data: 2026-08-25
---

# otimização

## 1. Definição Conceitual e Fundamentação Física / Metrológica

No contexto da Física Médica\, da Tomografia Computadorizada (TC) e da Inteligência Artificial aplicada à saúde, o termo **otimização** transcende a acepção coloquial de mero aprimoramento; ele constitui um princípio fundamental de proteção radiológica e um pilar metodológico em engenharia de imagem e aprendizado de máquina. 

Segundo a Comissão Internacional de Proteção Radiológica (ICRP - *International Commission on Radiological Protection*), especificamente na Publicação 103, a otimização da proteção radiológica (conhecida como princípio **ALARA** - *As Low As Reasonably Achievable*, ou "tão baixo quanto razoavelmente exequível") dita que a magnitude das doses individuais, o número de pessoas expostas e a probabilidade de exposições acidentais devem ser mantidos tão baixos quanto razoavelmente exequível, levando em conta fatores econômicos e sociais. Na prática da TC, otimizar significa maximizar a utilidade diagnóstica da imagem adquirida enquanto se minimiza a dose de radiação ionizante depositada no paciente.

Do ponto de vista metrológico e de processamento de sinais, a otimização refere-se ao processo matemático de encontrar o vetor de parâmetros ótimos $\mathbf{x}^*$ dentro de um espaço de busca viável $\Omega$\, de modo a minimizar ou maximizar uma função objetivo (ou função de custo) $f(\mathbf{x})$. Em tomografia, isso se manifesta na resolução de problemas inversos mal-postos (ill-posed problems) durante a reconstrução de imagem, no ajuste de parâmetros de aquisição (corrente do tubo, tensão, pitch) e no treinamento de redes neurais profundas para reconstrução baseada em aprendizado profundo (*Deep Learning Reconstruction - DLR*).

---

## 2. Formulação Matemática e Propriedades

Matematicamente, um problema de otimização irrestrita ou restrita é formulado de maneira geral como:

$$
\min_{\mathbf{x} \in \Omega} f(\mathbf{x})
$$

sujeito a restrições do tipo:

$$
g_i(\mathbf{x}) \le 0, \quad i = 1, \dots, m
h_j(\mathbf{x}) = 0, \quad j = 1, \dots, p
$$

Onde $\mathbf{x} \in \mathbb{R}^n$ representa o vetor de variáveis de decisão (por exemplo, os coeficientes de atenuação linear de voxels em uma matriz de TC).

### 2.1 Otimização em Reconstrução Iterativa (IR)
Na reconstrução iterativa estatística, a otimização busca minimizar uma função de custo composta por um termo de fidelidade aos dados (frequência de Poisson ou Gaussiana baseada nas projeções medidas $\mathbf{y}$) e um termo de regularização (penalização espacial para controle de ruído e preservação de bordas):

$$
\hat{\mathbf{x}} = \arg\min_{\mathbf{x} \ge 0} \left\{ \frac{1}{2} \|\mathbf{P}\mathbf{x} - \mathbf{y}\|_{\Sigma^{-1}}^2 + \beta R(\mathbf{x}) \right\}
$$

Onde:
- $\mathbf{P}$ é a matriz do sistema (projetor/retroprojetor forward/backward).
- $\mathbf{y}$ é o vetor de sinograma medido.
- $\Sigma^{-1}$ é a matriz de ponderação estatística do ruído.
- $R(\mathbf{x})$ é a função de regularização (ex: variação total - *Total Variation*).
- $\beta$ é o hiperparâmetro de regularização que equilibra a resolução espacial e a supressão de ruído.

Para resolver problemas de grande escala como este, algoritmos de primeira ordem baseados em gradiente, como o gradiente descendente acelerado de Nesterov ou métodos de divisão de operador (ex: ADMM - *Alternating Direction Method of Multipliers*), são amplamente empregados.

### 2.2 Otimização em Inteligência Artificial e DLR
No treinamento de modelos de Inteligência Artificial para geração ou melhoria de imagens de TC, a otimização ajusta os pesos sinápticos $\theta$ da rede neural minimizando uma perda empírica sobre um conjunto de dados de treinamento:

$$
\theta^* = \arg\min_{\theta} \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}\left( f_{\theta}(\mathbf{x}_i^{\text{low-dose}}), \mathbf{x}_i^{\text{ref}}\right)
$$

Onde $\mathcal{L}$ pode combinar perdas baseadas em norma ($L_1$, $L_2$ para preservar acurácia de pixel) e perdas perceptuais ou adversariais (em Redes Generativas Adversariais - GANs) para garantir realismo visual e nitidez estrutural. Os otimizadores estocásticos mais comuns incluem o **Adam** (*Adaptive Moment Estimation*), cuja atualização iterativa do passo de gradiente é dada por:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

### 3.1 Protocolos Clínicos e Dosimetria
A otimização de protocolos em TC visa equilibrar a qualidade diagnóstica da imagem e a dose de radiação. Isso envolve o ajuste refinado de:
- **Tensão do Tubo ($kVp$):** Ajustada de acordo com o biótipo do paciente e a tarefa diagnóstica (ex: $70-80\text{ kVp}$ para angiotomografias pediátricas ou coronarianas com contraste iodado, maximizando o efeito fotoelétrico; $120-140\text{ kVp}$ para exames de abdome em pacientes corpulentos).
- **Corrente do Tubo Modulada ($mA$):** Utilização de sistemas de controle automático de exposição (CAE) que adaptam a intensidade da radiação em tempo real conforme a atenuação angular e longitudinal do paciente (modulação *angular x-y* e *z*), otimizando a relação sinal-ruído (SNR) e evitando super-irradiação em regiões de menor espessura (como os ombros ou o pescoço).

### 3.2 Reconstrução de Imagem e DLR
A transição histórica da Retroprojeção Filtrada (FBP) para a Reconstrução Iterativa (IR) e, mais recentemente, para a Reconstrução Baseada em Aprendizado Profundo (DLR), representa um marco de otimização computacional. Os algoritmos DLR conseguem resolver o problema inverso de suprimir artefatos de quantum noise e artefatos de feixe endurecido (*beam hardening*) em exames de baixa dose ultrarrápidos, superando as limitações de artefatos de textura plástica outrora comuns em métodos iterativos híbridos.

### 3.3 Controle de Qualidade (CQ) e Observadores Computacionais
Na metrologia de equipamentos, processos de otimização são aplicados para calibrar automaticamente os detectores de estado sólido, corrigir desvios de ganho e offset, e minimizar artefatos de anel (*ring artifacts*). Ademais, o uso de **observadores computacionais** (como o *Channelized Hotelling Observer* - CHO) modela matematicamente o desempenho do olho humano em tarefas de detecção de lesões, permitindo a otimização automatizada de parâmetros de reconstrução sem a necessidade exaustiva de estudos com leitores humanos (humanos observadores).

---

## 4. Conexões e Wikilinks

- [[F Sica M Dica|física-médica]]
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Inteligencia Artificial IA|inteligência-artificial]]
- [[Radioproteção|princípio-alara]]
- [[Reconstrução Iterativa|reconstrução-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Dosimetria em TC|dosimetria-em-tc]]
- [[Controle de Qualidade em TC|controle-de-qualidade]]
- [[SNR|relação-sinal-ruído]]
- [[Artefatos em TC|artefatos-em-tc]]