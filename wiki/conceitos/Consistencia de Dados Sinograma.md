---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, sinograma, processamento-de-sinal, reconstrucao-de-imagem, inteligencia-artificial]
data: 2026-08-25
---

# Consistencia_de_Dados_Sinograma

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **consistência de dados do sinograma** refere-se ao conjunto de propriedades matemáticas, físicas e estatísticas que um conjunto de projeções tomográficas adquiridas (o sinograma) deve satisfazer para que corresponda a uma função de atenuação real, fisicamente realizável e finita no espaço de imagem. Em Tomografia Computadorizada (TC) de raios X, o sinograma é uma representação bidimensional onde os eixos coordenados correspondem tipicamente à posição do detector ($\xi$ ou $s$) e ao ângulo de projeção ($\theta$ ou $\phi$). 

Para que este plano de dados represente um objeto físico tridimensional (ou bidimensional, no modelo de feixe paralelo) sem a introdução de artefatos severos na etapa de reconstrução, os dados devem obedecer a leis fundamentais de conservação de energia, linearidade do feixe e geometria projetiva. Violações dessas condições — causadas por artefatos de feixe endurecido (*beam hardening*), retroespalhamento Compton, radiação espalhada não corrigida, movimento do paciente, ruído quântico extremo ou falhas de calibração nos elementos do detector — resultam em inconsistências no sinograma.

Do ponto de vista metrológico, a verificação da consistência de dados atua como uma ferramenta de controle de qualidade e pré-processamento. Ela garante que algoritmos de reconstrução analítica (como a Retroprojeção Filtrada - FBP), iterativa (IR) ou baseados em aprendizado profundo (Deep Learning Reconstruction - DLR) operem dentro de domínios matemáticos válidos, prevenindo o surgimento de artefatos em anel (*ring artifacts*), estrias (*streaking*), borramentos anômalos ou alucinações geradas por redes neurais expostas a distribuições de dados fora do domínio esperado (*out-of-distribution*).

---

## 2. Formulação Matemática e Propriedades

A formulação matemática da consistência de dados baseia-se na teoria das transformadas integrais, especificamente na **Transformada de Radon** e em suas propriedades de alcance (*range*). 

Seja $f(x, y)$ uma função bidimensional integrável de suporte compacto que representa o coeficiente de atenuação linear de um objeto. A Transformada de Radon de $f$, denotada por $p(s, \theta)$, é definida como a integral de linha ao longo de uma reta parametrizada pela distância $s$ à origem e pelo ângulo normal $\theta$:

$$
p(s, \theta) = \iint_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - s) \, dx \, dy
$$

onde $\delta$ é a função delta de Dirac. O sinograma é o arranjo matricial ou contínuo de $p(s, \theta)$ para $s \in [-R, R]$ e $\theta \in [0, \pi)$ (ou $[0, 2\pi)$ dependendo da simetria).

### Teorema dos Momentos de John (John's Conditions)
As condições de consistência mais clássicas para a Transformada de Radon em duas dimensões foram estabelecidas por Fritz John. Elas estipulam que os momentos do sinograma em relação à variável espacial $s$ devem ser polinômios homogêneos da ordem correspondente em $\cos\theta$ e $\sin\theta$.

Formalmente, o $k$-ésimo momento da projeção para um ângulo fixo $\theta$ é dado por:

$$
M_k(\theta) = \int_{-\infty}^{\infty} s^k p(s, \theta) \, ds
$$

O Teorema de John dita que $M_k(\theta)$ deve ser expresso exatamente como um polinômio homogêneo de grau $k$ nas variáveis $\cos\theta$ e $\sin\theta$:

$$
M_k(\theta) = \sum_{j=0}^{k} a_{j, k-j} \cos^j\theta \sin^{k-j}\theta
$$

onde $a_{j, k-j}$ são constantes reais que dependem exclusivamente dos momentos espaciais internos do objeto $f(x, y)$. Qualquer desvio dessa relação polinomial indica uma inconsistência nos dados de projeção.

### Condições de Helgason-Ludwig
Uma formulação complementar e extremamente útil é dada pelas condições de Helgason-Ludwig. Para que uma função $P(s, \theta)$ seja a Transformada de Radon de uma função com suporte compacto, ela deve satisfazer a condição de que a integral:

$$
\int_0^{\pi} \int_{-\infty}^{\infty} s^k P(s, \theta) \, ds \, \, d\theta
$$

exibe restrições específicas para diferentes valores de $k$, além de decair assintoticamente de maneira apropriada no domínio da frequência espacial (conhecido como *Central Slice Theorem* ou Teorema da Fatia Central).

No contexto estatístico (para dados contendo ruído de Poisson provenientes de fótons contados ou integrados), a consistência também pode ser avaliada por meio de métricas de verossimilhança (*log-likelihood*) baseadas no modelo estatístico de aquisição:

$$
L(Y | \bar{Y}) = \sum_{i} \left( Y_i \ln \bar{Y}_i - \bar{Y}_i \right)
$$

onde $Y_i$ representa as contagens medidas e $\bar{Y}_i$ o valor esperado derivado do modelo físico de atenuação ($\bar{Y}_i = I_0 e^{-p_i} + R_i$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimización

A manutenção e a correção da consistência de dados do sinograma são cruciais em diversas etapas da imagem médica moderna:

1. **Correção de Artefatos Geométricos e Físicos:**
   - **Enrijecimento do Feixe (*Beam Hardening*):** Como os raios X policromáticos violam a linearidade da lei de Lambert-Beer, os sinogramas gerados carecem de consistência matemática linear. Técnicas de linearização aplicadas diretamente no sinograma corrigem essa violação.
   - **Espalhamento Compton:** A radiação espalhada adiciona um pedestal de intensidade difusa ao sinograma, destruindo a consistência das integrais de linha. Algoritmos de correção estimam esse fundo e o subtraem antes da reconstrução.

2. **Reconstrução Iterativa (IR) e Regularização:**
   - Métodos iterativos baseados em otimização (como *Ordered Subset Expectation Maximization* - OSEM, ou penalizados por regularizadores de variação total - *Total Variation*) utilizam modelos avançados de formação de imagem. Quando há dados corrompidos ou truncados (campo de visão limitado), impor restrições de consistência de dados atua como um forte prior matemático para mitigar artefatos de truncamento.

3. **Inteligência Artificial e Redes Neurais (DLR):**
   - Modelos de aprendizado profundo aplicados ao domínio do sinograma (para redução de dose, preenchimento de dados faltantes em varreduras de varredura limitada - *limited-angle CT*) dependem de restrições de consistência. Redes que não incorporam camadas de consistência de dados (*Data Consistency Layers*) frequentemente geram imagens anatomicamente plausíveis, mas clinicamente falsas (alucinações). A inclusão explícita de uma camada de consistência garante que a imagem reconstruída obedeça à física da varredura:

$$
\hat{P} = \arg\min_{P} || P - P_{\text{neural}} ||^2 \quad \text{sujeito a restrições físicas}
$$

4. **Controle de Qualidade Metrológico:**
   - Desalinhamentos mecânicos do pórtico (centro de rotação deslocado) geram sinogramas com assimetrias sinusoidais detectáveis por análises de consistência de fase, permitindo correções geométricas automáticas (*shift correction*).

---

## 4. Conexões e Wikilinks

- [[Transformada de Radon|Transformada_de_Radon]]
- [[Teorema da Fatia Central|Teorema_da_Fatia_Central]]
- [[FBP|Retroprojecao_Filtrada]]
- [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
- [[Artefatos em TC|Artefatos_em_Tomografia]]
- [[Correcao_Beam_Hardening]]
- [[Modelagem_Estatistica_Ruido_Poisson]]
- [[Deep_Learning_Reconstruction_TC]]