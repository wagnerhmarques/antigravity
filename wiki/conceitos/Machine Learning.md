---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, machine-learning, reconstrucao-de-imagem\, dosimetria]
data: 2026-08-25
---

# Machine Learning

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O *Machine Learning* (Aprendizado de Máquina), um subcampo fundamental da Inteligência Artificial (IA), refere-se ao estudo e desenvolvimento de algoritmos e modelos estatísticos que sistemas computacionais utilizam para executar tarefas específicas sem instruções explícitas, baseando-se em padrões e inferências derivados de dados. No contexto da Física Médica e da Tomografia Computadorizada (TC), o *Machine Learning* atua como uma ponte entre os dados brutos de aquisição física — como as projeções senoidais atenuadas de raios X — e a interpretação clínica ou quantitativa de alta precisão.

Do ponto de vista metrológico, os algoritmos de *Machine Learning* operam mapeando espaços de alta dimensionalidade. Dada uma matriz de entrada $\mathbf{x} \in \mathbb{R}^d$ (que pode representar um sinograma ruidoso ou uma imagem reconstruída) e um espaço de alvos $\mathbf{y} \in \mathbb{R}^c$ (como mapas de número CT quantitativos, imagens livres de ruído ou segmentações de órgãos de risco), o aprendizado de máquina busca otimizar uma função de mapeamento $f_{\mathbf{\theta}}(\mathbf{x})$ parametrizada por um vetor de pesos e vieses $\mathbf{\theta}$. 

A fundamentação física subjacente frequentemente envolve a inversão de problemas mal-postos de Hadamard. A aquisição de dados em TC é modelada pela Transformada de Radon e pela atenuação de fótons regida pela Lei de Beer-Lambert. Devido a limitações de dose de radiação ionizante (otimização ALARA), ruído quântico de Poisson e artefatos de feixe endurecido (*beam hardening*), as medições físicas são incompletas ou corrompidas. O *Machine Learning* introduz restrições a priori baseadas em dados empíricos, permitindo a regularização espacial e espectral avançada que supera as limitações de modelos puramente analíticos.

---

## 2. Formulação Matemática e Propriedades

O processo de aprendizado fundamenta-se na minimização de uma função de perda empírica ($\mathcal{L}$). Seja $\mathcal{D} = \{(\mathbf{x}_i, \mathbf{y}_i)\}_{i=1}^N$ o conjunto de treinamento composto por $N$ amostras, o objetivo do algoritmo é encontrar os parâmetros ótimos $\mathbf{\theta}^*$:

$$
\mathbf{\theta}^* = \arg\min_{\mathbf{\theta}} \frac{1}{N} \sum_{i=1}^N \mathcal{L}\left( f_{\mathbf{\theta}}(\mathbf{x}_i), \mathbf{y}_i \right) + \lambda R(\mathbf{\theta})
$$

Onde $R(\mathbf{\theta})$ representa um termo de regularização (como a norma $L_2$ ou *Ridge*) para evitar o sobreajuste (*overfitting*), e $\lambda$ é o hiperparâmetro de penalização.

Em arquiteturas profundas voltadas para a reconstrução e processamento de imagens de TC, a função de perda frequentemente combina métricas de erro de intensidade e percepção visual. Por exemplo, a perda combinada de Erro Quadrático Médio ($MSE$) e perda perceptual baseada em redes pré-treinadas é formulada como:

$$
\mathcal{L}_{\text{total}} = \frac{1}{M} \left\| \mathbf{y} - f_{\mathbf{\theta}}(\mathbf{x}) \right\|_2^2 + \gamma \left\| \Phi(\mathbf{y}) - \Phi(f_{\mathbf{\theta}}(\mathbf{x})) \right\|_2^2
$$

Onde $\Phi(\cdot)$ denota a extração de características de camadas intermediárias de uma rede neural convolucional de referência, e $\gamma$ pondera a contribuição perceptual.

No contexto de Redes Neurais Profundas (*Deep Learning*, uma subcategoria de *Machine Learning*), a propagação do sinal através de uma camada $l$ é descrita por:

$$
\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}
\mathbf{a}^{(l)} = \sigma\left(\mathbf{z}^{(l)}\right)
$$

Sendo $\mathbf{W}^{(l)}$ a matriz de pesos sinápticos, $\mathbf{b}^{(l)}$ o vetor de viés, $\mathbf{a}^{(l-1)}$ a ativação da camada anterior, e $\sigma(\cdot)$ a função de ativação não linear (por exemplo, ReLU, Leaky ReLU ou GELU), essencial para que o modelo aprenda representações não lineares complexas inerentes à física de interação radiação-matéria.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O *Machine Learning* revolucionou a física da Tomografia Computadorizada em múltiplos domínios críticos:

* **Reconstrução de Imagem (Deep Learning Reconstruction - DLR):** Métodos tradicionais como a Retroprojeção Filtrada (FBP) geram ruído acentuado em doses baixas, enquanto a Reconstrução Iterativa (IR) é computacionalmente custosa. Modelos de *Machine Learning* baseados em arquiteturas tipo U-Net aprendem a mapear sinogramas ou imagens de baixa dose diretamente para o espaço de alta qualidade diagnóstica, preservando a resolução espacial e a exatidão dos números Hounsfield (HU).
* **Correção de Artefatos:** Algoritmos supervisionados são amplamente empregados na mitigação de artefatos de feixe endurecido, espalhamento Compton (*scatter*), ruído quântico severo e artefatos metálicos causados por próteses ortopédicas ou clipes cirúrgicos.
* **Dosimetria Computacional e Gestão de Dose:** Redes de *Machine Learning* predizem mapas de distribuição tridimensional de dose absorvida (Gy) e estimam o risco estocástico de câncer (dôse efetiva, mSv) com base em parâmetros de escaneamento anatômico e corrente do tubo ($mAs$), otimizando protocolos clínicos sob o princípio ALARA.
* **Controle de Qualidade (QC) Automatizado:** Modelos analíticos de aprendizado supervisionado e não supervisionado avaliam a constância de parâmetros físicos do equipamento de TC — como ruído, uniformidade, função de espalhamento de ponto (PSF) e modulação da função de transferência (MTF) — a partir de imagens de controle de qualidade (fantasmas)\, detectando desvios metrológicos antes que afetem a precisão diagnóstica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem|Reconstrucao de Imagem]]
* [[Deep Learning Image Reconstruction (DLR)|Deep Learning Reconstruction]]
* [[Retroprojeção Filtrada (FBP)|Filtro de Retroprojecao]]
* [[Reconstrução Iterativa|Reconstrucao Iterativa]]
* [[Dosimetria em Radiologia|Dosimetria em Raio-X]]
* [[Controle de Qualidade em TC]]
* [[CNNs|Redes Neurais Convolucionais]]