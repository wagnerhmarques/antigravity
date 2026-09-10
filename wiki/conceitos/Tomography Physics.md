---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, fisica-da-tomografia, radiologia-digital, reconstrucao-de-imagem]
data: 2026-08-25
---

# Tomography Physics

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Física da Tomografia** (do grego *tomos*, corte/fatia, e *graphein*, escrever) abrange o conjunto de princípios físicos, matemáticos e metrológicos que regem a geração, aquisição, processamento e reconstrução de imagens tomográficas tridimensionais a partir de projeções bidimensionais transmitidas por radiação ionizante (ou outros campos penetrantes). 

No contexto da Tomografia Computadorizada (TC) de raios-X médica, o fundamento físico primário reside na **Lei de Atenuação de Lambert-Beer**, que descreve a atenuação exponencial de um feixe de fótons de raios-X policromático ao interagir com a matéria através de processos como o Efeito Fotoelétrico e o Efeito Compton. Diferente da radiografia planar — que projeta a superposições tridimensional de estruturas anatômicas em um receptor bidimensional, resultando em perda de profundidade e contraste inerente —, a tomografia supera essa limitação ao medir múltiplos coeficientes de atenuação linear espacialmente resolvidos em um plano de corte axial.

Do ponto de vista metrológico, a quantificação precisa da tomografia é expressa na escala de **Unidades Hounsfield (HU)**, calibrada em relação à água pura ($0 \text{ HU}$) e ao ar (aproximadamente $-1000 \text{ HU}$) sob condições padrão de temperatura e pressão. A fidelidade metrológica da imagem depende diretamente do controle rigoroso de artefatos físicos (endurecimento do feixe, efeito de volume parcial, ruído quântico e espalhamento Compton) e da estabilidade da geometria do sistema de variação angular (gantry), composto pela fonte de raios-X e pela matriz de detetores de estado sólido (geralmente cintiladores acoplados a fotodiodos).

---

## 2. Formulação Matemática e Propriedades

O problema fundamental da física da tomografia é recuperar uma função espacialmente distribuída do coeficiente de atenuação linear, denotada por $\mu(x, y)$, a partir de um conjunto de medidas de intensidade de raios-X obtidas em múltiplos ângulos de projeção $\theta$.

### A Lei de Atenuação de Lambert-Beer e a Transformada de Radon
Para um feixe colimado de raios-X monocromáticos que percorre uma linha reta L (caminho de integração) através do objeto, a intensidade emergente $I$ em relação à intensidade incidente $I_0$ é dada por:

$$
I = I_0 \exp \left( -\int_{L} \mu(x, y) \, dl \right)
$$

Tomando o logaritmo neperiano da razão de intensidades, define-se a projeção ou perfil de atenuação $P(\theta, p)$, onde $\theta$ é o ângulo de rotação do sistema e $p$ é a coordenada de translação do detetor (distância ao isocentro):

$$
P(\theta, p) = \ln \left( \frac{I_0}{I} \right) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x, y) \delta(x \cos\theta + y \sin\theta - p) \, dx \, dy
$$

Esta integral de linha bidimensional é conhecida como a **Transformada de Radon**, denotada formalmente por $\mathcal{R}\{\mu(x,y)\}$.

### O Teorema da Seção Central (Fourier Slice Theorem)
O princípio matemático que viabiliza a reconstrução analítica da imagem é o Teorema da Seção Central. Ele estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $P(\theta, p)$ obtida a um ângulo $\theta$ é idêntica à fatia (ou seção) bidimensional da Transformada de Fourier bidimensional da função original $\mu(x,y)$, tomada ao longo de uma linha que passa pela origem fazendo o mesmo ângulo $\theta$ no espaço de frequências espaciais $(f_x, f_y)$.

Seja $\mathcal{F}_1\{P(\theta, p)\}$ a transformada de Fourier 1D da projeção com respeito à coordenada espacial $p$:

$$
\mathcal{F}_1\{P(\theta, p)\} = S(\theta, f_p) = \iint_{-\infty}^{\infty} \mu(x, y) e^{-j 2\pi f_p (x \cos\theta + y \sin\theta)} \, dx \, dy
$$

### Retroprojeção Filtrada (Filtered Backprojection - FBP)
Para inverter a Transformada de Radon e reconstrução espacial no domínio de imagem, aplica-se a fórmula de inversão que incorpora um filtro rampa para compensar a atenuação das altas frequências espaciais inerente à retroprojeção simples (que gera imagens borradas proporcionalmente a $1/r$):

$$
\mu(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} S(\theta, f_p) |f_p| e^{j 2\pi f_p p} \, df_p \right]_{\substack{p = x\cos\theta + y\sin\theta}} \, d\theta
$$

O termo $|f_p|$ representa o **filtro rampa** (Ram-Lak), frequentemente modificado por janelas de apodização (Hamming, Hann, Shepp-Logan) para controlar o balanço entre resolução espacial e supressão de ruído quântico.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão aprofundada da física da tomografia é indispensável para o desenvolvimento, controle de qualidade e otimização clínica dos sistemas modernos de TC. Suas principais frentes de impacto incluem:

* **Otimização da Dose de Radiação e Dosimetria:** O estudo da interação fóton-matéria permite modelar índices dosimétricos fundamentais como o $CTDI_{w}$ (Computed Tomography Dose Index weighted) e o $DLP$ (Dose Length Product). A física da atenuação orienta o desenvolvimento de protocolos de modulação de corrente de tubo automática (angular e longitudinal) baseados nas dimensões anatômicas do paciente.
* **Mitigação de Artefatos Físicos:**
  * *Endurecimento do feixe (Beam Hardening):* Causado pela atenuação preferencial de fótons de baixa energia em feixes policromáticos, resultando em artefatos em forma de "copa" (*cupping*). A física fornece algoritmos de correção pré e pós-reconstrução.
  * *Efeito de Volume Parcial:* Ocorre quando múltiplos tecidos com propriedades de atenuação distintas coexistem no mesmo voxel, resolvido parcialmente com matrizes de detetores de ultra-alta resolução.
* **Evolução dos Algoritmos de Reconstrução:**
  * **FBP (Filtered Backprojection):** Padrão histórico analítico rápido, porém sensível a baixas relações sinal-ruído (SNR).
  * **Reconstrução Iterativa (IR) e Deep Learning Reconstruction (DLR):** Modelam estatísticas de ruído complexas (Poisson e Gaussiana) e a física exata da formação do feixe (matriz de sistema $A$), permitindo reduções drásticas na dose de radiação mantendo a detectabilidade de lesões de baixo contraste.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Computed Tomography]]
* [[X-Ray Attenuation Coefficient]]
* [[Radon Transform]]
* [[Retroprojeção Filtrada (FBP)|Filtered Backprojection]]
* [[CTDI and Dosimetry]]
* [[Beam Hardening Artifact]]
* [[Reconstrução Iterativa|Iterative Reconstruction]]
* [[Deep Learning Image Reconstruction (DLR)|Deep Learning Reconstruction]]