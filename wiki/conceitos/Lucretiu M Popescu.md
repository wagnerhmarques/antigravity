---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, metrologia, historia-da-ciencia]
data: 2026-08-25
---

# Lucretiu M. Popescu

## 1. Definição Conceitual e Fundamentação Física / Metrológica

**Lucretiu M. Popescu** (frequentemente citado na literatura científica como *L. M. Popescu*) é uma figura seminal na história e no desenvolvimento matemático da Tomografia Computadorizada (TC) e dos métodos de reconstrução de imagem por raios X. O seu principal e mais duradouro contributo para a física médica e para a tecnologia de imagem diagnóstica foi a formulação, em 1970, da aplicação da transformada de Radon e de métodos de inversão algébrica para a reconstrução de distribuições espaciais de atenuação a partir de projeções múltiplas, antecipando ou operando em paralelo aos desenvolvimentos fundamentais que culminaram no prêmio Nobel de Allan Cormack e Godfrey Hounsfield.

Do ponto de vista metrológico e físico, o trabalho pioneiro de Popescu abordou o problema fundamental da tomografia: como mapear a distribuição espacial tridimensional ou bidimensional de um coeficiente de atenuação linear interno $\mu(x,y)$ de um objeto físico, utilizando medidas de intensidade de radiação transmitida integradas ao longo de linhas retas (trajetórias dos fótons de raios X). 

Popescu formalizou a conexão rigorosa entre a física da atenuação da radiação — descrita pela Lei de Beer-Lambert — e o aparato matemático da teoria de inversão de operadores integrais. Na sua formulação, a intensidade medida $I$ após atravessar um meio com coeficiente de atenuação $\mu(x,y)$ ao longo de uma linha de trajetória $L$ é expressa como:

$$
I = I_0 \exp \left( -\int_L \mu(x,y) \, dl \right)
$$

Onde o logaritmo da razão de intensidades (o projeção ou sinograma bruto) representa a linha integral direta do coeficiente de atenuação:

$$
p(s, \theta) = \ln\left(\frac{I_0}{I}\right) = \int_L \mu(x,y) \, dl
$$

A contribuição de Popescu destacou-se pela abordagem computacional e algébrica inicial para resolver este sistema de equações integrais discretizadas, estabelecendo bases para o que mais tarde evoluiria para os métodos iterativos de reconstrução e a compreensão formal da amostragem em tomografia computadorizada.

---

## 2. Formulação Matemática e Propriedades

Para compreender o impacto formal das formulações associadas aos trabalhos de Popescu e à reconstrução tomográfica da época, é necessário analisar o mapeamento entre o espaço físico de atenuação e o espaço de projeção (espaço de Radon).

Seja $\mu(x,y) \in L_2(\mathbb{R}^2)$ a função contínua que representa o coeficiente de atenuação linear de um corte transversal de um paciente. A Transformada de Radon bidimensional $\mathcal{R}\{\mu\}$ é definida para um dado ângulo de projeção $\theta$ e distância ao centro $s$ como:

$$
\mathcal{R}\{\mu\}(s, \theta) = \iint_{-\infty}^{\infty} \mu(x,y) \delta(x \cos\theta + y \sin\theta - s) \, dx \, dy
$$

O problema inverso consiste em recuperar $\mu(x,y)$ a partir do conjunto completo de projeções $\{p(s, \theta)\}_{\theta \in [0, \pi)}$. 

Nos primórdios da modelagem matemática aplicada por Popescu e colaboradores, o problema contínuo foi discretizado em uma malha de pixels (ou voxels) $j = 1, 2, \dots, N$, onde cada linha de raio $i = 1, 2, \dots, M$ intercepta o pixel $j$ com um comprimento de corda w_{ij}$. Isso resulta em um sistema linear de equações algébricas:

$$
\sum_{j=1}^{N} w_{ij} \mu_j = p_i, \quad \text{para } i = 1, 2, \dots, M
$$

Ou, em forma matricial compacta:

$$
\mathbf{W} \boldsymbol{\mu} = \mathbf{p}
$$

Onde:
- $\mathbf{W} \in \mathbb{R}^{M \times N}$ é a matriz de ponderação geométrica (pesos de contribuição dos raios).
- $\boldsymbol{\mu} \in \mathbb{R}^N$ é o vetor desconhecido contendo os valores de atenuação dos pixels.
- $\mathbf{p} \in \mathbb{R}^M$ é o vetor de medidas de projeção (sinograma).

Propriedades fundamentais investigadas nestas formulações incluem:
1. **Mal-condicionamento (Ill-posedness)**: O operador de Radon é compacto, e sua inversão não é contínua na norma $L_2$, o que significa que pequenos ruídos nas medições $\mathbf{p}$ (ruído estatístico de fótons, ruído quântico) resultam em erros catastróficos na imagem reconstruída $\boldsymbol{\mu}$ se não houver regularização adequada.
2. **Esparsidade e Amostragem**: A necessidade de satisfazer o Teorema de Amostragem de Nyquist-Shannon no domínio angular e espacial para evitar artefatos de aliasing (estrelas ou raias).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Apesar de a tomografía moderna ter avançado exponencialmente desde a década de 1970 — passando da Retroprojeção Filtrada (FBP) analítica para métodos iterativos avançados (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR) —, os alicerces matemáticos postos por pioneiros como Lucretiu M. Popescu continuam altamente relevantes:

- **Reconstrução Algébrica (ART, SIRT, SART)**: Os métodos algébricos iterativos modernos descendem diretamente da formulação matricial de sistemas lineares esparsos propostos nos primórdios da TC. Algoritmos como a *Algebraic Reconstruction Technique* (ART) resolvem o sistema $\mathbf{W} \boldsymbol{\mu} = \mathbf{p}$ iterativamente através de projeções ortogonais sucessivas:
  
  
$$
\boldsymbol{\mu}^{(k+1)} = \boldsymbol{\mu}^{(k)} + \lambda \frac{p_i - \mathbf{w}_i \cdot \boldsymbol{\mu}^{(k)}}{\|\mathbf{w}_i\|^2} \mathbf{w}_i
$$

  Onde $\lambda$ é o parâmetro de relaxação. Estes métodos são cruciais hoje em dia para protocolos de dose ultra-baixa (*low-dose CT*) e tomografia de feixe cônico (*Cone-Beam CT* - CBCT) com dados incomtruncados ou ruidosos.

- **Controle de Qualidade e Metrologia de Sistemas**: A compreensão rigorosa da formação de imagem baseada em linhas integrais permite aos físicos médicos modelar com precisão a resposta do sistema de aquisição, incluindo o espalhamento Compton, o endurecimento do feixe (*beam hardening*) e a geometria focal finita do tubo de raios X.

---

## 4. Conexões e Wikilinks

- [[Transformada de Radon]]
- [[Retroprojetor Filtrada (FBP)]]
- [[Reconstrução Iterativa|Reconstrução Iterativa (IR)]]
- [[Sinograma]]
- [[Lei de Beer-Lambert]]
- [[Artefatos em Tomografia Computadorizada]]
- [[Dosimetria em Radiologia|Dosimetria em Tomografia Computadorizada]]