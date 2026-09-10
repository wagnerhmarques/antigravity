---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem, processamento-de-sinal, metrologia]
data: 2026-08-25
---

# Convencoes_Pipeline_Compartilhado

## 1. Definição Conceitual e Fundamentação Física / Metrológica

As **Convenções de Pipeline Compartilhado** referem-se ao conjunto padronizado de premissas geométricas, físicas, numéricas e de amostragem adotadas de maneira unificada entre diferentes módulos computacionais em sistemas de Tomografia Computadorizada (TC) modernos, especialmente aqueles que integram métodos tradicionais de processamento de sinal com arquiteturas de Inteligência Artificial (IA) e Aprendizado Profundo (*Deep Learning*, DL).

Na Física Médica e na Engenharia de Imagem Diagnóstica, o fluxo de trabalho (*pipeline*) de aquisição e reconstrução transforma dados brutos de fótons detectados — expressos tipicamente como perfis de atenuação em projeções angulares (sinograma) — em matrizes volumétricas tridimensionais de coeficientes de atenuação linear linearmente escalados (Unidades Hounsfield, HU). Historicamente, diferentes estágios desse pipeline (como a correção de espalhamento, calibração de feixe policromático, filtragem em espaço de Fourier e redes neurais de Redução de Ruído Baseada em Aprendizado Profundo - *DLR*) operavam em domínios próprios, com convenções arbitrárias de espaçamento de pixel, orientação de eixos, normalização de intensidade e tratamento de fronteiras. 

A adoção de convenções de pipeline compartilhado estabelece uma interoperabilidade rigorosa que previne artefatos de interpolação, desalinhamentos sub-pixel, viés radiométrico e degradação da resolução espacial efetiva. Sob a ótica metrológica, garantir um pipeline compartilhado assegura a rastreidade quantitativa das métricas de dose e qualidade de imagem, fundamentais para a dosimetria computacional e para a radiômica quantitativa baseada em IA.

---

## 2. Formulação Matemática e Propriedades

Para formalizar o pipeline compartilhado, considere o espaço de projeção contínuo e o espaço de imagem discretizado. Seja $p(s, \beta)$ o sinograma ideal, onde $s$ denota a coordenada do detector ao longo do arco de rotação e $\beta$ o ângulo de projeção. A relação com o objeto de coeficiente de atenuação $\mu(x,y)$ é descrita pela Transformada de Radon bidimensional:

$$
p(s, \beta) = \mathcal{R}\{\mu(x,y)\} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \mu(x,y) \delta\left(x \cos\beta + y \sin\beta - s\right) \, dx \, dy
$$

Em um pipeline fragmentado, operadores de Inteligência Artificial aplicados no domínio da imagem ou do sinograma frequentemente sofrem de incompatibilidades nas transformações de malha (*grid*). Seja $\mathcal{F}_{\theta}$ uma rede neural convolucional ou um modelo baseado em transformadores (*transformers*) parametrizado por $\theta$. A operação do pipeline compartilhado exige que a matriz de entrada $\mathbf{X}_{\text{in}} \in \mathbb{R}^{M \times N}$ e a saída $\hat{\mathbf{X}}_{\text{out}} \in \mathbb{R}^{M \times N}$ obedeçam estritamente às mesmas convenções de amostragem espacial e escala radiométrica.

Seja $\Delta_x$ o tamanho do voxel no espaço objeto e $\Delta_s$ o espaçamento físico do elemento de detecção. As convenções definem o mapeamento afim canônico $\mathcal{T}_{\text{conv}}$ que relaciona as coordenadas de pixel $(i, j)$ com as coordenadas físicas $(x, y)$:

$$
x_i = \left( i - \frac{M}{2} + \frac{1}{2} \right) \Delta_x, \quad y_j = \left( j - \frac{N}{2} + \frac{1}{2} \right) \Delta_y
$$

Qualquer módulo de IA inserido no pipeline (seja para correção pré-reconstrução no sinograma ou pós-processamento de DLR) deve preservar a integridade da norma do operador de retroprojeção filtrada (FBP):

$$
\mu_{\text{FBP}}(x,y) = \int_{0}^{\pi} \int_{-\infty}^{\infty} P(k, \beta) |k| e^{i 2\pi k (x \cos\beta + y \sin\beta)} \, dk \, d\beta
$$

Onde $P(k, \beta)$ é a transformada de Fourier unidimensional da projeção filtrada por um filtro rampa $|k|$. As convenções estipulam que:
1. **Normalização Radiométrica:** Os tensores alimentados nas redes neurais devem manter a linearidade com o coeficiente de atenuação mássica ou conversão direta para HU normalizadas:

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

2. **Tratamento de Fronteiras (Padding):** Operações convolucionais em redes de IA frequentemente reduzem a dimensionalidade espacial se não tratadas adequadamente. O pipeline compartilhado impõe condições de contorno periódicas ou reflexivas padronizadas para evitar artefatos de borda na reconstrução iterativa profunda.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A implementação de **Convenções de Pipeline Compartilhado** é indispensável em vários domínios avançados da Tomografia Computadorizada:

* **Reconstrução Híbrida e DLR (Deep Learning Reconstruction):** Algoritmos modernos de DLR operam muitas vezes no domínio híbrido (intercalando correções no sinograma cru e refinamento no domínio da imagem). Sem um pipeline compartilhado, erros de calibração de feixe policromático propagam-se e amplificam-se através das camadas latentes da rede neural, gerando alucinações de imagem ou perda de resolução espacial de alto contraste.
* **Redução de Dose e Otimização de Protocolos:** Em varreduras de baixa dose (*low-dose CT*), o ruído quântico assume distribuição Poisson-Gaussiana mista no sinograma. Redes de IA treinadas para denoising exigem que o pipeline compartilhado mantenha a exata correspondência estatística entre a variância do ruído estimado e a geometria real do scanner, permitindo manter a detectabilidade de lesões em estudos com observadores computacionais (ideal *observers*).
* **Radiômica Quantitativa e Biomarcadores de Imagem:** A extração de features radiômicas de textura depende criticamente do tamanho de voxel e da função de espalhamento de ponto (PSF). Convenções padronizadas asseguram que variações nos valores de características texturais reflitam exclusivamente a heterogeneidade patológica do tecido e não artefatos decorrentes de desalinhamentos ou divergências nas convenções de interpolação do pipeline.

---

## 4. Conexões e Wikilinks

* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Deep Learning Reconstruction (DLR)|Deep_Learning_Reconstruction_DLR]]
* [[Transformada de Radon|Transformada_de_Radon]]
* [[Filtro_Rampa_FBP]]
* [[Unidades Hounsfield|Unidades_Hounsfield]]
* [[Correcao_de_Espalhamento]]
* [[Dosimetria_Computacional]]
* [[Observadores de Modelo (Model Observers)|Observadores_Computacionais]]