---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-iterativa, reducao-de-ruido, processamento-de-imagem, otimizacao]
data: 2026-08-25
---

# iterative-reconstruction

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Reconstrução Iterativa (RI)** em Tomografia Computadorizada (TC) representa uma classe avançada de algoritmos matemáticos utilizados para converter os dados de projeção adquiridos pelos detectores (sinograma) em imagens tomográficas bidimensionais ou tridimensionais. Historicamente, a prática clínica foi dominada pela Retroprojeção Filtrada ([[Retroprojeção Filtrada (FBP)|filtered-back-projection]]), fundamentada na transformada analítica de Radon e na fórmula de inversão de ramp-filtering. Embora a FBP seja computacionalmente eficiente e de tempo de execução linear, ela assume um modelo físico idealizado de aquisição e propagação de raios X, negligenciam-se fenômenos estocásticos (como ruído quântico governado por estatística de Poisson), efeitos de feixe policromático (endurecimento de feixe), espalhamento Compton, amostragem discreta e a geometria finita do ponto focal e dos elementos de detecção.

Em contrapartida, a Reconstrução Iterativa abandona a inversão analítica direta e formula o problema da formação da imagem como um problema inverso mal-posto (*ill-posed inverse problem*). Os algoritmos de RI operam através de um ciclo iterativo contínuo que compara as projeções estimadas da imagem atual (obtidas por meio de um operador de projeção adiante ou *forward projector*) com os dados reais medidos pelo scanner. A discrepância entre esses dados é utilizada para atualizar a matriz de imagem pixel a pixel (ou voxel a voxel). 

Do ponto de vista metrológico, a RI permite a modelagem explícita de:
1. **Estatística do Ruído:** Incorporação de modelos de ruído estatisticamente realistas (como a distribuição de Poisson combinada com ruído eletrônico gaussiano), substituindo a aproximação gaussiana simplista da FBP.
2. **Modelos do Sistema (System Matrix):** Caracterização precisa da resposta espacial do sistema ([[Point Spread Function (PSF)|point-spread-function]]), largura do feixe de raios X, geometria do detector e efeitos de amostragem volumétrica.
3. **Regularização Espacial:** Introdução de penalidades matemáticas (priori) que suprimem o ruído e preservam bordas anatômicas nítidas, mitigando o aumento descontrolado de artefatos de alta frequência comuns em abordagens puramente algébricas.

---

## 2. Formulação Matemática e Propriedades

O problema de reconstrução em TC pode ser modelado linearmente em sua forma discretizada. Seja $y \in \mathbb{R}^M$ o vetor que representa o sinograma medido (contendo $M$ elementos de projeção) e $x \in \mathbb{R}^N$ o vetor que representa a imagem de atenuação linear a ser reconstruída (contendo $N$ voxels). A relação entre a imagem e as projeções é expressa pela matriz do sistema $A \in \mathbb{R}^{M \times N}$, cujos elementos $A_{ij}$ representam a probabilidade ou o contributo do voxel $j$ para o detector $i$:

$$
y = Ax + \epsilon
$$

onde $\epsilon$ representa o vetor de ruído estatístico.

### Métodos Algébricos e Estatísticos Clássicos
Os primeiros métodos algébricos, como o *Algebraic Reconstruction Technique* (ART) e suas variantes ordenadas como o *Ordered Subset Algebraic Reconstruction Technique* (OS-ART) ou *Ordered Subset Expectation Maximization* (OS-EM), buscam minimizar a divergência entre o modelo e os dados medidos. O algoritmo OSEM, amplamente adotado na prática devido à sua convergência acelerada dividindo o sinograma em subconjuntos (subsets) $S_k$, é formalizado pela atualização multiplicativa:

$$
x_j^{(n+1)} = \frac{x_j^{(n)}}{\sum_{i \in S_k} A_{ij}} \sum_{i \in S_k} A_{ij} \frac{y_i}{(Ax^{(n)})_i}
$$

onde $x^{(n)}$ é a estimativa da imagem na iteração $n$, e $(Ax^{(n)})_i$ representa a projeção adiante do $n$-ésimo passo calculada para o elemento de detecção $i$.

### Reconstrução Baseada em Penalização / Regularização (MAP)
Para resolver a natureza mal-posta do problema e evitar a amplificação de ruído nas iterações avançadas, a formulação estatística avançada emprega a estimativa de Máxima A Posteriori (MAP). O objetivo é maximizar a probabilidade condicional da imagem dado o sinograma medido, o que equivale a minimizar uma função custo objetiva $\Phi(x)$ composta por um termo de fidelidade aos dados (baseado na log-verossimilhança estatística $L(y|Ax)$) e um termo de penalização ou regularização $R(x)$:

$$
\hat{x} = \arg\min_{x \ge 0} \left\{ -L(y \mid Ax) + \beta R(x) \right\}
$$

Onde:
- $-L(y \mid Ax)$ quantifica o erro estatístico (frequentemente modelado via log-verossimilhança de Poisson: $\sum_{i=1}^{M} \left[ (Ax)_i - y_i \ln((Ax)_i) \right]$).
- $R(x)$ é a função de penalização espacial, tal como a variação total (Total Variation - TV):

$$
R(x) = \sum_{j} \sqrt{|
abla x_j|^2 + \delta^2}
$$

sendo $\delta$ um parâmetro de suavização infinitesimal e $\beta$ o hiperparâmetro de regularização que controla o balanço entre a resolução espacial e a supressão de ruído.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A introdução e maturação comercial dos algoritmos de Reconstrução Iterativa (frequentemente comercializados sob nomenclaturas proprietárias como ASiR, AIDR 3D, Veo, IMR, SAFIRE, ADMIRE) transformaram profundamente a prática da Tomografia Computadorizada clínica e a metrologia radiológica.

### Otimização da Dose de Radiação e Princípio ALARA
O principal motor clínico da RI é a capacidade de manter a detectabilidade de baixo contraste (low-contrast detectability - LCD) mesmo quando a corrente do tubo ($mAs$) ou a tensão ($kVp$) são drasticamente reduzidas. Na FBP, a redução de fótons resulta em um aumento proporcional do ruído estocástico e da granulação da imagem, mascarando lesões de baixa atenuação (como metástases hepáticas incipientes ou pequenos acidentes vasculares cerebrais isquêmicos). Os algoritmos de RI conseguem separar o ruído quântico real da informação anatômica estrutural graças aos modelos estatísticos de ruído, permitindo reduções de dose de radiação ionizante que variam tipicamente de **30% a até 80%** dependendo da modalidade e do fabricante.

### Mitigação de Artefatos
Diferente da FBP, que assume trajetórias ideais de raios X, a RI modela as imperfeições físicas do sistema. Isso resulta na redução acentuada de:
* **Artefatos de Endurecimento de Feixe:** Através da modelagem espectral no cálculo do operador de projeção.
* **Artefatos de Metal (MAR iterativo):** Substituição de dados corrompidos por projeções estimadas pelo modelo anatômico circundante.
* **Artefatos de Subamostragem e *Streak*:** Comuns em protocolos de varredura rápida ou rotações incompletas.

### Desafios Metrológicos e Texturais
Apesar das vantagens dosimétricas, a RI introduz desafios significativos na avaliação da qualidade de imagem e na radiômica quantitativa:
* **Não-linearidade:** Ao contrário da FBP, que é um operador linear (o ruído na imagem é estacionário e gaussiano), a RI é altamente não-linear. Isso significa que a textura do ruído depende do sinal local e da dose (o ruído é espacialmente variante e não-estacionário).
* **Efeito "Plástico" ou "Aquarela":** Níveis excessivos de regularização podem suprimir texturas finas e alterar a aparência visual de pequenas estruturas anatômicas, simulando patologias ou apagando margens de tumores.
* **Impacto em Observadores Computacionais e Radiômica:** Recursos de textura extraídos para fins de medicina de precisão podem ser severamente enviesados se os parâmetros de reconstrução iterativa não forem padronizados em estudos multicêntricos.

---

## 4. Conexões e Wikilinks

- [[Retroprojeção Filtrada (FBP)|filtered-back-projection]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[qualidade-de-imagem-tc]]
- [[Dosimetria em TC|dosimetria-em-tc]]
- [[Artefatos em TC|artefatos-em-tc]]
- [[SNR|relacao-sinal-ruido]]