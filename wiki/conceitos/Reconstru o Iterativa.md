---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-iterativa, processamento-de-sinal, otimizacao, reducao-de-dose]
data: 2026-08-25
---

# Reconstrução Iterativa

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Reconstrução Iterativa (RI)** em Tomografia Computadorizada (TC) representa uma classe avançada de algoritmos computacionais utilizados para gerar imagens tomográficas a partir de projeções (projeções atenuadas de raios X, conhecidas como sinogramas) adquiridas em múltiplos ângulos. Historicamente, a TC clínica baseou-se na Retroprojeção Filtrada (FBP, do inglês *Filtered Backprojection*), um método analítico direto baseado na Transformada de Radon e no Teorema do Slice Central. Embora a FBP seja computacionalmente eficiente e produza imagens em tempo real, ela assume um modelo físico idealizado: ausência de ruído estatístico, amostragem contínua e perfeita, e linearidade estrita do sistema de aquisição. 

Quando submetida a condições de campo reais — caracterizadas por baixas doses de radiação (gerando ruído quântico severo), artefatos de enrijecimento de feixe, espalhamento Compton, ruído eletrônico e amostragem discreta —, a FBP degrada-se drasticamente, resultando em ruído texturizado, artefatos de estrias (*streaking artifacts*) e perda de resolução de baixo contraste.

A Reconstrução Iterativa supera essas limitações ao formular o problema de reconstrução como um **problema inverso mal-posto**. Em vez de aplicar uma operação matemática direta e única, a RI emprega um ciclo repetitivo (iterativo) de aproximações. O algoritmo compara repetidamente as projeções estimadas de uma imagem gerada (por meio de um modelo de sistema direto ou *forward projector*) com os dados brutos reais adquiridos pelo scanner. A diferença entre os dados medidos e os estimados é quantificada e utilizada para atualizar a imagem de forma a minimizar o erro, integrando gradualmente modelos estatísticos complexos do ruído e da física do sistema de aquisição.

Do ponto de vista metrológico, a RI permite otimizar a balança entre a dose de radiação ionizante administrada ao paciente e a qualidade diagnóstica da imagem (princípio ALARA - *As Low As Reasonably Achievable*). Ao modelar estatísticas de fótons de Poisson e Gaussianas, a RI reduz a variância do ruído sem sacrificar a resolução espacial inerente, permitindo reduções drásticas de dose que variam tipicamente de 30% a até 80% em protocolos específicos, quando comparada à FBP convencional.

---

## 2. Formulação Matemática e Propriedades

O processo de aquisição em TC pode ser modelado linearmente de forma matricial como:

$$
y = Hx + \epsilon
$$

Onde:
* $y \in \mathbb{R}^M$ é o vetor que representa o sinograma medido (dados de projeção com $M$ elementos).
* $x \in \mathbb{N}^N$ é o vetor que representa a imagem discretizada (matriz de coeficientes de atenuação linear com $N$ voxels).
* $H \in \mathbb{R}^{M \times N}$ é a matriz do sistema (ou operador de projeção direta), cujos elementos $H_{ij}$ representam a probabilidade ou o contributo geométrico do voxel $j$ para o detector $i$.
* $\epsilon$ representa o vetor de ruído estatístico associado ao processo de contagem de fótons.

### Abordagens Estatísticas e Algoritmos de Otimização

Os métodos de RI mais robustos baseiam-se na maximização da verossimilhança (*Maximum Likelihood*, ML) ou na penalização bayesiana (Maximum A Posteriori, MAP). Considerando a natureza quântica dos fótons de raios X, o ruído nos dados brutos segue a distribuição estatística de Poisson.

#### 1. ML-EM (Maximum Likelihood Expectation Maximization)
O algoritmo fundamenta-se na estatística de Poisson dos fótons detectados. A função objetivo a ser maximizada é a verossimilhança logarítmica:

$$
L(x) = \sum_{i=1}^{M} \left( y_i \ln(\bar{y}_i) - \bar{y}_i - \ln(y_i!) \right)
$$

Onde $\bar{y}_i = \sum_{j=1}^{N} H_{ij}x_j + r_i$, sendo $r_i$ uma correção para espalhamento e ruído de fundo. O passo de atualização iterativa do EM de Dempster-Laird para o voxel $j$ na iteração $k+1$ é dado por:

$$
x_j^{(k+1)} = \frac{x_j^{(k)}}{\sum_{i=1}^{M} H_{ij}} \sum_{i=1}^{M} H_{ij} \frac{y_i}{\sum_{l=1}^{N} H_{il}x_l^{(k)} + r_i}
$$

#### 2. OSEM (Ordered Subsets Expectation Maximization)
Embora o ML-EM garanta convergência para a máxima verossimilhança, sua taxa de convergência é extremamente lenta, exigindo dezenas ou centenas de iterações, o que o torna inviável para a prática clínica em TC. O algoritmo OSEM acelera o processo dividindo o sinograma completo $y$ em subconjuntos disjuntos ordenados (subconjuntos angulares) $S_1, S_2, \dots, S_S$. A atualização é realizada para cada subconjunto sequencialmente dentro de uma única iteração:

$$
x_j^{(k, s+1)} = \frac{x_j^{(k, s)}}{\sum_{i \in S_s} H_{ij}} \sum_{i \in S_s} H_{ij} \frac{y_i}{\sum_{l=1}^{N} H_{il}x_l^{(k, s)} + r_i}
$$

#### 3. MAP e Regularização (Métodos Híbridos / Iterativos Estatísticos Avançados)
Para mitigar a amplificação de ruído nas iterações avançadas do OSEM e controlar a granulosidade da imagem, introduz-se uma função de penalização (ou regularização) $R(x)$ no quadro bayesiano (MAP):

$$
\Phi(x) = L(x) - \beta R(x)
$$

Onde $\beta$ é o parâmetro de regularização que controla o peso da penalidade espacial. Funções de penalização comuns incluem a suavização baseada em bordas (como o prior de Huber ou funções de custo de *Total Variation* - TV):

$$
R(x) = \sum_{j} \sum_{k \in N(j)} w_{jk} \psi(x_j - x_k)
$$

Onde $N(j)$ denota a vizinhança do voxel $j$, $w_{jk}$ são pesos espaciais, e $\psi$ é uma função de custo convexa que penaliza diferenças grandes, preservando contornos anatômicos nítidos (arestas).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A adoção generalizada da Reconstrução Iterativa transformou a prática da Tomografia Computadorizada médica através de múltiplos domínios:

1. **Redução de Dose de Radiação:** Como a RI modela estatisticamente a distribuição de Poisson do ruído, ela elimina a necessidade de filtros de rampa agressivos que amplificam o ruído de alta frequência na FBP. Protocolos pediátricos, exames de angio-TC e exames oncológicos de acompanhamento tiram proveito direto ao manter a detectabilidade de lesões de baixo contraste mesmo com reduções drásticas na corrente do tubo (mAs).
2. **Modelagem Avançada do Sistema (*Advanced Modeling*):** Os algoritmos modernos de RI incorporam o **Modelo Geométrico do Sistema** (tamanho real do ponto focal, formato e resposta dos elementos do detector), o **Modelo Físico** (atenuação policromática, enrijecimento do feixe, espalhamento Compton) e o **Modelo Estatístico** (distribuição do ruído eletrônico e quântico).
3. **Mitigação de Artefatos:** Artefatos metálicos causados por próteses dentárias, implantes ortopédicos ou clipes cirúrgicos criam feixes severamente endurecidos e lacunas de dados no sinograma. Métodos de RI com modelagem de feixe policromático e interpolação estatística conseguem preencher e corrigir essas regiões de forma superior à interpolação linear tradicional da FBP.
4. **Evolução para a Reconstrução Baseada em Aprendizado Profundo (DLR):** A RI serviu como alicerce conceitual para o desenvolvimento atual da Inteligência Artificial em tomografia, onde redes neurais convolucionais (CNNs) e modelos gerativos substituem ou aceleram os termos de regularização iterativa, permitindo reconstruções ultrarrápidas com fidelidade física sem precedentes.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[FBP|Retroprojeção Filtrada (FBP)]]
* [[Controle de Qualidade em TC]]
* [[Dosimetria em Radiologia]]
* [[Inteligencia Artificial IA|Inteligência Artificial em Radiologia]]
* [[Física da Radiação X]]
* [[Redução de Dose]]