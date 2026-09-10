---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, deep-learning, reconstrucao-de-imagem, dosimetria, metrologia]
data: 2026-08-25
---

# Physics-Informed Neural Networks (PINNs)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

As **Physics-Informed Neural Networks (PINNs)** representam um paradigma de aprendizado de máquina (Machine Learning) que integra leis físicas fundamentais — expressas tipicamente por equações diferenciais parciais (EDPs) ou ordinárias (EDOs) — diretamente na função de custo (loss function) de uma rede neural artificial. Diferentemente das redes neurais puramente baseadas em dados (*data-driven*), que exigem grandes volumes de amostras empíricas e frequentemente sofrem com a falta de interpretabilidade e generalização fora da distribuição de treinamento, as PINNs utilizam o arcabouço matemático da física como um mecanismo de regularização indutiva.

Do ponto de vista da **Física Médica** e da **Metrologia**, as PINNs oferecem uma ferramenta poderosa para resolver problemas inversos mal-postos (*ill-posed inverse problems*), comuns em modalidades de imagem médica. Elas contornam a escassez de dados clínicos rotulados ao impor restrições físicas conhecidas — como a equação de atenuação de raios X (Transformada de Radon), a conservação de energia, a equação de difusão ou o transporte de radiação. Em termos metrológicos, isso reduz a incerteza estatística e sistemática associada às reconstruções puramente empíricas, assegurando que as soluções preditas respeitem os princípios de conservação e as leis de escala que regem a interação da radiação ionizante com a matéria.

---

## 2. Formulação Matemática e Propriedades

Considere um sistema físico geral governado por uma Equação Diferencial Parcial não linear parametrizada em um domínio espacial $\Omega \subset \mathbb{R}^d$ e domínio temporal $t \in [0, T]$:

$$
\mathcal{N} \left[ u(\mathbf{x}, t); \boldsymbol{\lambda} \right] = f(\mathbf{x}, t), \quad \mathbf{x} \in \Omega, \ t \in [0, T]
$$

onde $u(\mathbf{x}, t)$ representa o campo físico de interesse (por exemplo, o coeficiente de atenuação linear $\mu(\mathbf{x})$ ou o fluxo de radiação), $\mathcal{N}[\cdot; \boldsymbol{\lambda}]$ é um operador diferencial não linear com parâmetros físicos desconhecidos ou conhecidos $\boldsymbol{\lambda}$, e $f(\mathbf{x}, t)$ é uma função de fonte externa. As condições de contorno e iniciais são dadas por:

$$
\mathcal{B} \left( u(\mathbf{x}, t), \mathbf{x}, t \right) = 0, \quad \mathbf{x} \in \partial\Omega, \ t \in [0, T]
u(\mathbf{x}, 0) = u_0(\mathbf{x}), \quad \mathbf{x} \in \Omega
$$

Para resolver este sistema via PINN, aproxima-se a solução $u(\mathbf{x}, t)$ por uma rede neural profunda parametrizada por pesos e vieses $\boldsymbol{\theta}$, denotada por $\hat{u}(\mathbf{x}, t; \boldsymbol{\theta})$. A rede neural atua como um *universal approximator* diferenciável.

A função de perda total (Loss Function) da PINN é formulada como uma soma ponderada de termos que penalizam o desvio dos dados observados e a violação das leis físicas no domínio e nas fronteiras:

$$
\mathcal{L}(\boldsymbol{\theta}) = w_{\text{data}} \mathcal{L}_{\text{data}}(\boldsymbol{\theta}) + w_{\text{pde}} \mathcal{L}_{\text{pde}}(\boldsymbol{\theta}) + w_{\text{bc}} \mathcal{L}_{\text{bc}}(\boldsymbol{\theta})
$$

Onde cada componente é definido por:

$$
\mathcal{L}_{\text{data}}(\boldsymbol{\theta}) = \frac{1}{N_{d}} \sum_{i=1}^{N_{d}} \left| \hat{u}(\mathbf{x}_i, t_i; \boldsymbol{\theta}) - u_i \right|^2
\mathcal{L}_{\text{pde}}(\boldsymbol{\theta}) = \frac{1}{N_{f}} \sum_{j=1}^{N_{f}} \left| \mathcal{N} \left[ \hat{u}(\mathbf{x}_j^f, t_j^f; \boldsymbol{\theta}); \boldsymbol{\lambda} \right] - f(\mathbf{x}_j^f, t_j^f) \right|^2
\mathcal{L}_{\text{bc}}(\boldsymbol{\theta}) = \frac{1}{N_{b}} \sum_{k=1}^{N_{b}} \left| \mathcal{B} \left( \hat{u}(\mathbf{x}_k^b, t_k^b; \boldsymbol{\theta}), \mathbf{x}_k^b, t_k^b \right) \right|^2
$$

Os conjuntos de pontos $\{\mathbf{x}_i, t_i\}$ representam as medições empíricas, enquanto os pontos de colocação $\{\mathbf{x}_j^f, t_j^f\}$ são amostrados (frequentemente via amostragem de Monte Carlo baseada em quase-aleatoriedade, como sequências de Sobol) em todo o domínio $\Omega \times [0, T]$ para impor a física estipulada pelo operador $\mathcal{N}$. As derivadas necessárias para computar $\mathcal{N}[\hat{u}]$ são obtidas analiticamente ou via **Diferenciação Automática** (*Automatic Differentiation*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema da **Tomografia Computadorizada (TC)** moderna, as PINNs desempenham papéis cruciais na superação de limitações inerentes aos métodos tradicionais de reconstrução e aquisição:

1. **Reconstrução de Dose Baixa (*Low-Dose CT*) e Redução de Ruído:** Em exames de TC de baixa dose, a alta contaminação por ruído quântico e artefatos de streak compromete o diagnóstico. PINNs podem ser formuladas incorporando a estatística de Poisson dos fótons de raios X e a física da Transformada de Radon no processo de otimização, permitindo a reconstrução de imagens de alta fidelidade sem exigir milhares de exames de referência.
2. **TC de Poucas Projeções (*Sparse-View CT*) e Tomografia de Ângulo Limitado:** Quando o número de projeções angulares é drasticamente reduzido para minimizar a dose do paciente, os algoritmos analíticos como FBP (*Filtered Backprojection*) falham catastroficamente. As PINNs resolvem o problema inverso impondo a consistência de dados (através da equação de projeção direta) combinada com priors de regularização espacial (como variação total física).
3. **Dosimetria Computacional e Simulação de Transporte de Radiação:** Na radioterapia guiada por imagem (IGRT) e planejamento de tratamento, as PINNs servem como substitutas rápidas (*surrogate models*) para simulações complexas de Monte Carlo da equação de transporte de Boltzmann. Elas permitem o cálculo em tempo real da distribuição de dose absorvida em geometrias heterogêneas de pacientes.
4. **Calibração Metrológica e Correção de Endurecimento do Feixe (*Beam Hardening*):** A modelagem física não linear da atenuação policromática dos raios X pode ser embutida na arquitetura da rede para estimar e corrigir mapas de endurecimento de feixe sem a necessidade de fantomas de calibração complexos para cada protocolo.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem]]
* [[FBP|Filtered Backprojection (FBP)]]
* [[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction (DLR)]]
* [[Dosimetria e Controle de Qualidade]]
* [[Observadores de Modelo (Model Observers)|Observadores Computacionais]]
* [[Transformada de Radon]]