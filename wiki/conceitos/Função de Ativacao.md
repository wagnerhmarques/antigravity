---
tipo: conceito
tags: [inteligencia-artificial, redes-neurais, tomografia-computadorizada, reconstrucao-iterativa, aprendizado-profundo]
data: 2026-08-25
---

# funcao-de-ativacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica
No contexto de arquiteturas de redes neurais artificiais aplicadas à Física Médica e à Tomografia Computadorizada (TC), a **função de ativação** é uma operação matemática não linear aplicada à saída ponderada de um neurônio artificial (o somatório do produto dos pesos sinápticos pelas entradas, acrescido do viés ou *bias*). 

Do ponto de vista fundamental, a introdução de funções de ativação não lineares é o elemento arquitetural que dota as redes neurais de capacidade de aproximação universal (conforme o Teorema da Aproximação Universal de Cybenko/Hornik). Sem essa não linearidade, uma rede neural profunda — independentemente de quantas camadas ocultas possua — colapsaria matematicamente em uma única transformação linear equivalente, sendo incapaz de modelar fenômenos físicos complexos, mal-condicionados ou altamente não lineares, como a atenuação radiológica poliespectral, a dispersão Compton (${\text{Compton scattering}}$) e os artefactos de enrijecimento de feixe (*beam hardening*) em TC.

Metrologicamente, as funções de ativação operam como mapeadores de transferência de sinal, determinando o limiar de excitação e a sensibilidade do neurônio a variações infinitesimais nos tensores de entrada (por exemplo, matrizes de projeções sinodais ou volumes reconstruídos). A escolha da função de ativação dota o modelo de características essenciais para a otimização baseada em gradiente, influenciando diretamente a estabilidade numérica, a velocidade de convergência e a mitigação de patologias de treinamento, como o desaparecimento (*vanishing*) ou a explosão (*explosion*) de gradientes.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Seja $z_j^{(l)}$ o sinal pré-ativação do $j$-ésimo neurônio na camada $l$, definido como:

$$
z_j^{(l)} = \sum_{k} w_{jk}^{(l)} a_k^{(l-1)} + b_j^{(l)}
$$

Onde $w_{jk}^{(l)}$ representa os pesos sinápticos, $a_k^{(l-1)}$ as ativações da camada anterior e $b_j^{(l)}$ o termo de viés. A saída pós-ativação $a_j^{(l)}$ é obtida aplicando-se a função de ativação $f$:

$$
a_j^{(l)} = f\left(z_j^{(l)}\right)
$$

As funções de ativação mais relevantes na literatura de Tomografia Computadorizada e Inteligência Artificial médica incluem:

### A. Rectified Linear Unit (ReLU)
Definida como:

$$
f(z) = \max(0, z) = \begin{cases} z, & \text{se } z > 0 \\ 0, & \text{se } z \le 0 \end{cases}
$$

Sua derivada direcional (exceto em $z=0$) é:

$$
f'(z) = \begin{cases} 1, & \text{se } z > 0 \\ 0, & \text{se } z < 0 \end{cases}
$$

### B. Leaky ReLU
Projetada para mitigar o problema do "ReLU morreu" (*dying ReLU*):

$$
f(z) = \max(\alpha z, z)
$$

Onde $\alpha$ é um hiperparâmetro pequeno (tipicamente $\alpha = 0.01$).

### C. Sigmóide Logística
Frequentemente utilizada em camadas de saída para mapear probabilidades ou limites estritos $[0, 1]$:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Possui a propriedade notável de autoderivabilidade:

$$
\sigma'(z) = \sigma(z)\left(1 - \sigma(z)\right)
$$

### D. Tangente Hiperbólica (Tanh)
Mapeia o intervalo $[-1, 1]$, sendo centrado na origem:

$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

Sua derivada é dada por:

$$
\frac{d}{dz}\tanh(z) = 1 - \tanh^2(z)
$$

### E. Parametric ReLU (PReLU) e Scaled Exponential Linear Unit (SELU)
Em arquiteturas auto-normalizadoras (muito aplicadas em redes profundas de reconstrução de TC), a SELU mantém a média e a variância dos ativações controladas através de constantes estritas $\lambda$ e $\alpha$:

$$
\text{SELU}(z) = \lambda \begin{cases} z, & \text{se } z > 0 \\ \alpha e^z - \alpha, & \text{se } z \le 0 \end{cases}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema moderno de Tomografia Computadorizada (TC), as funções de ativação desempenham papéis críticos em diferentes frentes tecnológicas:

1. **Reconstrução Baseada em Aprendizado Profundo (DLR - *Deep Learning Reconstruction*):** Redes do tipo U-Net ou Redes Generativas Adversariais (GANs) utilizam combinações de **Leaky ReLU** em blocos convolucionais intermediários para preservar características de alta frequência espacial (como bordas de órgãos, trabeculações ósseas e microlesões pulmonares) enquanto suprimem o ruído quântico decorrente de varreduras de baixa dose (*low-dose CT*). Funções sigmóides ou lineares modificadas são tipicamente empregadas na camada final para assegurar que os valores de saída respeitem as unidades Hounsfield (HU) fisicamente plausíveis.
2. **Correção de Artefatos e Redução de Dose:** Modelos voltados para a eliminação de artefatos de metal (*metal artifact reduction* - MAR) ou truncagem de projeção dependem criticamente de ativações não lineares para modelar a não-linearidade inerente à lei de atenuação de Beer-Lambert polychromatic.
3. **Optimização e Métodos Iterativos Aprendidos:** Abordagens híbridas que desdobram algoritmos de reconstrução iterativa (como ADMM ou SART) em redes neurais recorrentes (*Plug-and-Play Priors* e *Deep Equilibrium Models*) utilizam funções de ativação como operadores proxuais (*proximal operators*), garantindo a convexidade local e a convergência do processo de otimização dos coeficientes de atenuação linear $\mu(x,y)$.
4. **Dosimetria Computacional e Observadores Modificados:** Redes neurais que simulam fântomas virtuais antropomórficos ou avaliam a qualidade de imagem perceptual baseada em observadores humanos utilizam funções de ativação suaves (como **GELU** - *Gaussian Error Linear Unit*) para modelar a resposta não linear do sistema visual humano e a deposição estocástica de energia por fótons de raios X.

---

## 4. Conexões e Wikilinks
* [[rede-neural-artificial]]
* [[reconstrucao-por-aprendizado-profundo]]
* [[retroprojecion-filtrada]]
* [[ruido-quantico-em-tc]]
* [[Unidades Hounsfield|unidade-hounsfield]]
* [[Artefatos em TC|artefatos-em-tomografia]]
* [[Dosimetria em TC|dosimetria-em-tc]]