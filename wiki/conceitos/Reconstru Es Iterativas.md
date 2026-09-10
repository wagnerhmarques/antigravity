---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-iterativa, reducao-de-dose, processamento-de-imagem, otimizacao]
data: 2026-08-25
---

# reconstruções iterativas

## 1. Definição Conceitual e Fundamentação Física / Metrológica

As **reconstruções iterativas (RI)** na Tomografia Computadorizada (TC) representam uma classe avançada de algoritmos matemáticos e computacionais utilizados para gerar imagens tomográficas a partir de projeções (medidas de atenuação dos raios X) adquiridas em múltiplos ângulos. Historicamente precedidas pelos métodos analíticos — primariamente a [[Retroprojeção Filtrada (FBP)|retroprojecao filtrada]] (FBP\, do inglês *Filtered Back Projection*) —, as técnicas iterativas abandonam a suposição de que o feixe de raios X é perfeitamente colimado, monocromático e infinitesimalmente fino, operando através de um processo de aproximações sucessivas.

Do ponto de vista físico e metrológico, a aquisição de dados em TC descreve um problema inverso mal-posto (*ill-posed problem*). Os algoritmos analíticos resolvem este problema de forma direta, invertendo a Transformada de Radon sob condições ideais, o que inevitavelmente amplifica o ruído quântico de alta frequência e gera artefatos em cenários de baixa dose ou aquisições com amostragem subótima. Em contrapartida, as reconstruções iterativas modelam explicitamente a física do sistema de imagem, a estatística do ruído dos fótons (geralmente modelada pelas estatísticas de Poisson e Gaussiana) e a geometria tridimensional do escâner.

O processo iterativo opera comparando os dados reais medidos pelo detector com dados sintéticos (projeções estimadas) gerados a partir de uma imagem provisória (matriz de coeficientes de atenuação linear). A diferença entre a projeção estimada e a projeção medida é realimentada no sistema para corrigir a imagem provisória. Esse ciclo repete-se até que um critério de convergência seja atingido ou que um número pré-determinado de iterações seja concluído. Com isso, as RI permitem reduções substanciais na [[Radioproteção|dose de radiacao]] ao paciente — frequentemente variando de 30% a 70% — sem degradação proporcional na qualidade diagnóstica, mantendo a resolução espacial e a contrastabilidade em níveis aceitáveis.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, o sistema de aquisição em TC pode ser discretizado e modelado por um sistema linear de equações algébricas:

$$
y = Ax + \varepsilon
$$

Onde:
*   $y \in \mathbb{R}^M$ vetor que representa os dados de projeção medidos (sinograma).
*   $x \in \mathbb{R}^N$ vetor que representa a imagem a ser reconstruída (distribuição espacial do coeficiente de atenuação linear).
*   $A \in \mathbb{R}^{M \times N}$ é a matriz do sistema (ou operador de projeção/retroprojeção), cujos elementos $A_{ij}$ representam a probabilidade ou o contributo do vóxel $j$ para o detector $i$.
*   $\varepsilon$ representa o termo de ruído estatístico associado ao processo de contagem de fótons.

### Métodos Algébricos e Estatísticos

1. **Retroprojeção Filtrada Algébrica (ART) e SIR/SART:**
   Os primeiros métodos algébricos resolviam o sistema linha por linha. O algoritmo *Simultaneous Algebraic Reconstruction Technique* (SART) atualiza a estimativa da imagem $x^{(k)}$ na iteração $k$ utilizando a seguinte formulação de correção de ray-by-ray:

   

$$
x_j^{(k+1)} = x_j^{(k)} + \lambda \frac{\sum_{i \in I} A_{ij} \frac{y_i - \sum_{n} A_{\in} x_n^{(k)}}{\sum_n A_{\in}}}{\sum_{i \in I} A_{ij}}
$$

   Onde $\lambda$ é o parâmetro de relaxação que controla a velocidade de convergência e a estabilidade.

2. **Reconstruções Estatísticas (OSEM - *Ordered Subset Expectation Maximization*):**
   Para incorporar a estatística de Poisson do ruído de fótons, os métodos de máxima verossimilhança (ML-EM) foram desenvolvidos. O OSEM acelera o ML-EM particionando o sinograma em subconjuntos (subsets) de projeções angulares:

   

$$
x_j^{(k, s+1)} = \frac{x_j^{(k, s)}}{\sum_{i \in S_s} A_{ij}} \sum_{i \in S_s} A_{ij} \frac{y_i}{\sum_n A_{\in} x_n^{(k, s)}}
$$

3. **Reconstruções Iterativas Híbridas e Modeladas (IR / MBIR):**
   As gerações mais avançadas, conhecidas como *Model-Based Iterative Reconstruction* (MBIR) ou reconstruções iterativas baseadas em modelos completos, formulam o problema como uma otimização convexa minimizando uma função custo objetiva que combina a verossimilhança dos dados com termos de regularização espacial (penalização):

   

$$
\hat{x} = \arg\min_{x} \left\{ \mathcal{L}(y | Ax) + \beta \mathcal{R}(x) \right\}
$$

   Onde:
   *   $\mathcal{L}(y | Ax)$ é a função de log-verossimilhança baseada na física do ruído.
   *   $\mathcal{R}(x)$ é a função de penalização ou regularização (ex: prior de suavização por variação total - *Total Variation*, ou *edge-preserving priors*).
   *   $\beta$ é o hiperparâmetro que pondera o peso da regularização em relação à fidelidade aos dados medidos.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A implementação de algoritmos de reconstrução iterativa revolucionou a prática clínica da tomografia computadorizada, impactando diretamente os pilares da [[Radioproteção|protecao radiologica]] e do [[Controle de Qualidade em TC|controle de qualidade]] em imagem médica.

### Otimização de Dose e Dosimetria
A principal força motriz para a adoção clínica das RI foi a necessidade de mitigar o risco estocástico associado à radiação ionizante. Em exames pediátricos, cardiologia (escore de cálcio e angio-TC coronariana) e exames de rastreamento (como o de câncer de pulmão por baixa dose), as técnicas de FBP tradicional geravam níveis de ruído intoleráveis quando a corrente do tubo ($mAs$) era reduzida. As RI permitem que escaneamentos sejam realizados com frações da dose original, preservando a detectabilidade de lesões de baixo contraste.

### Modelagem de Sistemas Físicos Avançados
Diferente da FBP, as RI permitem a inclusão de modelos físicos complexos na matriz $A$:
*   **Modelo Óptico e Geométrico:** Considera o tamanho focal finito do tubo de raios X e a resposta espacial tridimensional dos elementos do detector.
*   **Modelo Estatístico:** Minimiza o viés introduzido pela transformação logarítmica de dados de contagem baixa (prevenindo artefatos de quantum mottle e *streak artifacts*).
*   **Correção de Espectro e Espalhamento:** Modelagem do endurecimento do feixe (*beam hardening*) e da radiação espalhada diretamente no laço iterativo.

### Limitações e Desafios Metrológicos
Apesar das vantagens, as RI apresentam desafios metrológicos específicos:
*   **Textura de Imagem Não-Linear:** Ao contrário da FBP, onde o ruído é estacionário e gaussiano, as RI produzem texturas de ruído espaciais que dependem do sinal (o ruído varia com a densidade do tecido). Isso pode alterar a percepção visual do radiologista e afetar o desempenho de [[Observadores de Modelo (Model Observers)|observadores computacionais]].
*   **Custo Computacional:** A necessidade de múltiplas projeções e retroprojeções exige poder de processamento massivo, impulsionando o uso de unidades de processamento gráfico (GPUs) dedicadas.
*   **Efeito "Plástico" ou "Manchado":** Em níveis extremos de redução de dose combinados com forte regularização, as imagens podem perder detalhes anatômicos finos ou apresentar uma textura borrada, embora isso tenha sido amplamente mitigado com o advento das abordagens de [[reconstrucao baseada em aprendizado profundo]] (DLR).

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|tomografia computadorizada]]
*   [[Retroprojeção Filtrada (FBP)|retroprojecao filtrada]]
*   [[reconstrucao baseada em aprendizado profundo]]
*   [[qualidade de imagem em tomografia]]
*   [[Radioproteção|dose de radiacao]]
*   [[Artefatos em Tomografia Computadorizada]]
*   [[Controle de Qualidade em TC|controle de qualidade]]
*   [[Observadores de Modelo (Model Observers)|observadores computacionais]]