---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, filtragem-espacial, processamento-de-sinal]
data: 2026-08-25
---

# filtro_de_rampa

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **filtro de rampa** (frequentemente associado à *Ramp Filter* ou *Ramachandran-Lakshminarayanan filter*) é um filtro de frequência unidimensional fundamental empregado no algoritmo de **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP) em Tomografia Computadorizada (TC). 

Do ponto de vista da física matemática e da transformada de Radon, a reconstrução analítica exata de uma função bidimensional a partir de suas projeções paralelas (sinograma) exige a aplicação do Teorema da Seção Central (ou Teorema do Slice Central). Este teorema estabelece que a transformada de Fourier 1D de uma projeção paralela obtida a um ângulo $\theta$ corresponde a uma linha que passa pela origem da transformada de Fourier 2D do objeto original, orientada ao longo do mesmo ângulo $\theta$.

Ao coletar projeções em múltiplos ângulos de 0 a $\pi$ (ou $2\pi$), o espaço de Fourier bidimensional do objeto é preenchido em coordenadas polares. A densidade de amostragem no domínio de Fourier em coordenadas polares é inversamente proporcional à distância radial ($| 
u |$) ao centro da origem. Em termos práticos, as regiões periféricas do espaço de Fourier (altas frequências) são menos amostradas do que as regiões centrais (baixas frequências). 

Se a retroprojeção simples for aplicada diretamente sem correção, ocorre uma degradação severa da imagem, caracterizada por um borramento (*blurding*) característico regido pela função $1/r$ no espaço real. Para compensar essa distorção geométrica e física inerente à amostragem polar, aplica-se um ganho linearmente proporcional à frequência espacial nas projeções antes da retroprojeção. Este ganho compensa exatamente a densidade de volume no espaço de Fourier polar, atuando como um filtro passa-alta ideal cuja resposta em frequência tem o perfil geométrico de uma rampa.

## 2. Formulação Matemática e Propriedades (se aplicável)

No domínio da frequência espacial, a resposta do filtro de rampa ideal, denjonado por $H(
u)$, é expressa em função da frequência espacial$
u$ (em ciclos por unidade de comprimento) como:

$$
H(
u) = |
u|
$$

Para limitar o ruído de alta frequência inerente aos sistemas físicos de raios X, o filtro de rampa puro é frequentemente multiplicado por uma janela de apodização ou corte (como os filtros de Hamming, Hann, Butterworth ou Shepp-Logan). A formulação geral de um filtro de reconstrução combinado $Q(
u)$ é dada por:

$$
Q(
u) = |
u| \cdot W(
u)
$$

onde $W(
u)$ representa a função de janela. Por exemplo, o filtro de Shepp-Logan utiliza a seguinte ponderação:

$$
W_{Shepp-Logan}(
u) = \frac{\sin\left(\frac{\pi 
u}{2 
u_{\max}}\right)}{\frac{\pi 
u}{2 
u_{\max}}}, \quad \text{para } |
u| \le 
u_{\max}
$$

No domínio espacial, a resposta ao impulso do filtro de rampa puro (sua transformada inversa de Fourier) é calculada analiticamente para uma linha de projeção discreta $p(x)$. A operação de filtragem convolucional correspondente no espaço real para uma projeção discretizada com espaçamento de amostragem $\Delta_x$ é expressa como a convolução discreta:

$$
q(i \Delta_x) = \sum_{k=-\infty}^{\infty} p(k \Delta_x) h((i - k) \Delta_x)
$$

Onde o núcleo do filtro no domínio espacial $h(x)$ para o filtro de rampa ideal é derivado analiticamente como:

$$
h(x) = \begin{cases} 
\frac{1}{4 \Delta_x^2}, & \text{se } x = 0 \\ 
0, & \text{se } x \text{ é par e } x 
eq 0 \\ 
-\frac{1}{\pi^2 x^2 \Delta_x^2}, & \text{se } x \text{ é ímpar}
\end{cases}
$$

Esta formulação demonstra que o filtro de rampa possui valores alternados positivos e negativos de longo alcance no domínio espacial, o que acentua as bordas e as altas frequências espaciais, aumentando consequentemente a relação sinal-ruído (SNR) desfavorável se não for devidamente regularizado.

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em sistemas modernos de Tomografia Computadorizada, o filtro de rampa e suas variações desempenham um papel crítico na balança entre **resolução espacial** e **ruído da imagem**:

* **Otimização Clínica (kernels de reconstrução):** Fabricantes de equipamentos de TC fornecem diferentes *kernels* (núcleos de convolução) que combinam o filtro de rampa com diferentes funções de janela. Kernels agudos (com maior inclinação nas altas frequências ou menor atenuação por janelas) são aplicados para estruturas ósseas e pulmões, onde a alta resolução espacial é primordial. Kernels suaves (com forte atenuação de altas frequências) são empregados para exames de crânio e fígado, suprimindo o ruído quântico em detrimento de bordas mais nítidas.
* **Impacto Dosimétrico:** A escolha do filtro de rampa afeta indiretamente a estratégia de otimização da dose de radiação. Filtros excessivamente ruidosos exigem doses maiores de radiação (maior produto corrente-tempo, mAs) para manter a detectabilidade de baixo contraste (Teoria de Detecção de Rose).
* **Relação com Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Embora os algoritmos de Reconstrução Iterativa (estatística ou baseada em modelos) e Reconstrução por Aprendizado Profundo mitiguem ou substituam a FBP tradicional para operar em doses ultrabaixas, o entendimento da filtragem de rampa permanece vital. Muitos métodos híbridos de IR utilizam a FBP filtrada como passo inicial (estimativa de alta frequência) ou incorporam penalizações baseadas em gradientes espaciais análogos aos efeitos do filtro de rampa.
* **Controle de Qualidade Metrológico:** Em testes de garantia de qualidade (QA) de scanners de TC, a análise da função de dispersão de ponto (PSF), da função de transferência de modulação (MTF) e do ruído textural depende diretamente do kernel de reconstrução selecionado, cujas propriedades fundamentais derivam da implementação matemática do filtro de rampa.

## 4. Conexões e Wikilinks

* [[FBP|retroprojecao_filtrada]]
* [[Transformada de Radon|transformada_de_radon]]
* [[teorema_da_secao_central]]
* [[Reconstrução Iterativa|reconstrucao_iterativa]]
* [[Task Transfer Function|funcao_de_transferencia_de_modulacao]]
* [[Ruído Quântico|ruido_quantico]]
* [[kernels_de_reconstrucao]]