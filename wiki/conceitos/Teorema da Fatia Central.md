---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, transformada-de-fourier, matematica-aplicada]
data: 2026-08-25
---

# Teorema_da_Fatia_Central

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Teorema da Fatia Central** (também conhecido como *Teorema da Projeção no Domínio da Frequência* ou *Central Slice Theorem*) é o pilar matemático fundamental que sustenta a reconstrução analítica de imagens em Tomografia Computadorizada (TC) convencional, particularmente nos algoritmos de Retroprojeção Filtrada (*Filtered Backprojection* - FBP). 

Fisicamente, o teorema estabelece uma ponte direta entre a realidade espacial de um objeto físico e o seu espectro de frequências espaciais. Em termos práticos, ele afirma que a Transformada de Fourier unidimensional (1D) de uma projeção paralela (ou perfil de atenuação) de um objeto bidimensional, adquirida sob um determinado ângulo $\theta$, é exatamente idêntica a uma linha (ou "fatia") que passa pela origem da Transformada de Fourier bidimensional (2D) desse mesmo objeto, orientada ao longo do mesmo ângulo $\theta$ no plano de Fourier.

Metrologicamente, este teorema permite traduzir o problema complexo de reconstruir uma distribuição espacial interna de coeficientes de atenuação linear $\mu(x,y)$ a partir de medições externas de raios X em um problema algébrico-espectral tratável computacionalmente. A compreensão rigorosa de suas limitações — como o subamostragem em altas frequências e a necessidade de interpolação em coordenadas polares para cartesianas — é vital para a garantia da qualidade de imagem, controle de qualidade de equipamentos e mitigação de artefatos em TC.

---

## 2. Formulação Matemática e Propriedades

Para formalizar o Teorema da Fatia Central, considere uma função bidimensional contínua e integrável $f(x,y)$ que representa a distribuição espacial do coeficiente de atenuação linear no plano de corte do paciente.

A projeção paralela $p_\theta(t)$ de $f(x,y)$, obtida ao longo de linhas de integração (raios) orientadas a um ângulo $\theta$ com o eixo $y$ positivo, é descrita pela Transformada de Radon:

$$
p_\theta(t) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

onde $t$ representa a coordenada de posição linear ao longo do detector, $\delta$ é a função delta de Dirac e a linha de integração é dada por $x \cos\theta + y \sin\theta = t$.

A Transformada de Fourier 1D da projeção $p_\theta(t)$ em relação à coordenada espacial $t$ é definida como:

$$
P_\theta(\omega) = \mathcal{F}_{1\{p_\theta(t)\}}(\omega) = \int_{-\infty}^{\infty} p_\theta(t) e^{-j 2\pi \omega t} \, dt
$$

onde $\omega$ denota a frequência espacial associada à coordenada $t$.

Por outro lado, a Transformada de Fourier 2D da função original $f(x,y)$ é dada por:

$$
F(U, V) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j 2\pi (Ux + Vy)} \, dx \, dy
$$

onde $U$ e $V$ são as frequências espaciais cartesianas conjugadas a $x$ e $y$, respectivamente.

Introduzindo coordenadas polares no domínio de Fourier, onde $U = \omega \cos\theta$ e $V = \omega \sin\theta$, o Teorema da Fatia Central estabelece a seguinte igualdade fundamental:

$$
P_\theta(\omega) = F(\omega \cos\theta, \omega \sin\theta)
$$

### Propriedades Matemáticas Relevantes:
1. **Linearidade:** Sendo a Transformada de Radon e a Transformada de Fourier operadores lineares, o teorema preserva a superposição de feixes e atenuações.
2. **Esparsidade Espectral e Amostragem:** O teorema evidencia que o preenchimento do espaço de Fourier ocorre de maneira radial. Isso exige o uso de técnicas de interpolação (de polar para cartesiano) ou a aplicação direta da fórmula de inversão em coordenadas polares, o que deu origem ao filtro rampa ($\lvert \omega \rvert$) na reconstrução FBP.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada moderna, o Teorema da Fatia Central não é tipicamente implementado de forma direta computacionalmente devido aos erros inerentes à interpolação de dados de uma malha polar para uma malha cartesiana no domínio de Fourier (que geram artefatos de borramento e perda de resolução espacial). No entanto, sua dedução teórica é a base absoluta para a derivação da fórmula da **Retroprojeção Filtrada (FBP)**.

* **Reconstrução FBP:** A aplicação analítica do teorema, seguida pela inversão da transformada polar em coordenadas cartesianas e inclusão do filtro rampa (compensação para a densidade de amostragem radial que decresce com $1/\omega$), permite a reconstrução exata de imagens em tempo hábil para a rotina clínica.
* **Inteligência Artificial e Reconstrução Profunda (DLR):** Redes neurais modernas voltadas para reconstrução de TC (*Deep Learning Reconstruction*) utilizam operadores inspirados no Teorema da Fatia Central para mapear o domínio dos dados brutos (*sinograma*) diretamente para o domínio da imagem, ou para corrigir artefatos originados por amostragem insuficiente no domínio espectral.
* **Controle de Qualidade e Dosimetria:** A análise de frequências espaciais fundamentada pelo teorema permite avaliar a Função de Transferência de Modulação (MTF) de sistemas de TC, quantificar a resolução espacial de alto contraste e otimizar protocolos para equilibrar ruído quântico e dose de radiação ionizante absorvida pelo paciente.

---

## 4. Conexões e Wikilinks

* [[Transformada de Radon|Transformada_de_Radon]]
* [[Transformada_de_Fourier]]
* [[FBP|Retroprojet_Filtrada_FBP]]
* [[Modulation Transfer Function (MTF)|Funcao_de_Transferencia_de_Modulacao_MTF]]
* [[Artefatos em TC|Artefatos_em_Tomografia]]
* [[Reconstrucao_por_Aprendizado_Profundo_DLR]]