---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, correcao-de-artefatos, processamento-de-sinal]
data: 2026-08-25
---

# artefatos-em-tomografia

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Em Tomografia Computadorizada (TC), define-se **artefato** como qualquer discrepância sistemática entre os valores numéricos de atenuação reconstruídos na imagem tomográfica (expressos em Unidades Hounsfield - UH) e o coeficiente de atenuação linear real do objeto escaneado. Do ponto de vista metrológico, os artefatos representam violações das premissas físicas e matemáticas assumidas pelos algoritmos de reconstrução de imagem, induzindo degradação severa da qualidade diagnóstica, mascaramento de patologias sutilezas ou geração de falsos positivos.

A formação de artefatos decorre de quatro fontes fundamentais de degradação do sinal:
1. **Limitações Físicas da Interação Radiação-Matéria:** Incluem a policromaticidade do feixe de raios X, o espalhamento Compton, o efeito volume parcial e a saturação de detectores.
2. **Dinâmica do Paciente e Imperfeições Geométricas:** Movimentos voluntários ou involuntários (cardíaco, respiratório, peristáltico) e desalinhamentos mecânicos do pórtico (gantry).
3. **Parâmetros de Aquisição Inadequados:** Amostragem insuficiente (subamostragem angular ou espacial) e limitações do conversor analógico-digital (A/D).
4. **Algoritmos de Reconstrução:** Erros de truncagem, aproximações na Retroprojeção Filtrada (FBP) e alucinações induzidas por Redes Neurais Profundas em reconstruções baseadas em aprendizado profundo (DLR).

Metrologicamente, a avaliação de artefatos é realizada por meio de fantasmas (*phantoms*) específicos de controle de qualidade, medindo-se a uniformidade do número tomográfico, o desvio padrão do ruído e os perfis de atenuação em regiões de interesse (ROIs).

---

## 2. Formulação Matemática e Propriedades

A formação de artefatos pode ser modelada analiticamente analisando-se o processo de aquisição e reconstrução. Seja o coeficiente de atenuação linear espacialmente variante dado por $\mu(x, y)$. A transformada de Radon ideal $p(\theta, t)$ é definida pela integral de linha ao longo do caminho de rayos $L_{\theta, t}$:

$$
p(\theta, t) = \iint_{-\infty}^{\infty} \mu(x, y) \, \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

### A. Endurecimento do Feixe (*Beam Hardening*)
Como fontes de raios X clínicas emitem um espectro policromático $I_0(E)$, a intensidade detectada $I(L)$ após atravessar um meio heterogêneo é dada por:

$$
I(L) = \int_{0}^{E_{\max}} I_0(E) \exp \left( - \int_{L} \mu(x, y, E) \, dl \right) dE
$$

O logaritmo negativo da razão de intensidades fornece a projeção medida $\hat{p}(\theta, t)$:

$$
\hat{p}(\theta, t) = -\ln \left( \frac{I(\theta, t)}{I_0} \right) = \int_{L_{\theta, t}} \mu(x, y; E) \, dl
$$

Esta não-linearidade viola a premissa de linearidade da transformada de Radon, resultando em artefatos de **endurecimento do feixe** (bandas escuras ou efeito *cupping* - abaulamento), cuja correção analítica aproxima-se por expansão polinomial:

$$
p_{\text{corrigido}}(\theta, t) = \hat{p}(\theta, t) + a_1 \hat{p}(\theta, t)^2 + a_2 \hat{p}(\theta, t)^3
$$

### B. Efeito Volume Parcial
Ocorre quando múltiplos tecidos com propriedades de atenuação distintas ocupam o mesmo voxel discreto de tamanho $\Delta x \times \Delta y \times \Delta z$. A função de resposta do sistema (SRF) do detector e o voxelizador atuam como um filtro passa-baixa espacial. Se $V$ representa o volume do voxel, o coeficiente medido $\bar{\mu}$ é a média ponderada:

$$
\bar{\mu} = \frac{1}{V} \iint_{V} \mu(x, y, z) \, dx \, dy \, dz
$$

Isso gera transições borradas e perda de amplitude em estruturas pequenas de alto contraste (ex.: ossos finos ou nódulos pulmonares).

### C. Artefatos de Movimento
Se o objeto sofre um deslocamento $\vec{d}(t) = [x(t), y(t)]^T$ durante a varredura angular de $\theta = 0$ até $2\pi$, a projeção inconsistente corrompe o domínio de Fourier (Teorema da Fatia Central). O erro residual $\epsilon(\theta, t)$ na imagem reconstruída por FBP é expresso como:

$$
\epsilon(x, y) = \int_{0}^{2\pi} \left[ p_{\text{real}}(\theta, t) - p_{\text{movimento}}(\theta, t; \vec{d}(t)) \right] \star \text{filtro}(t) \, \, d\theta
$$

Este erro manifesta-se tipicamente como **artefatos de sombreamento** (*shading*) e **fantasmas estruturais** (*ghosting*).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O gerenciamento e a mitigação de artefatos são pilares fundamentais na otimização da cadeia de imagem em TC, impactando diretamente os seguintes domínios:

* **Controle de Qualidade (CQ) e Metrologia:** Protocolos internacionais (como AAPM e IEC) exigem testes periódicos com fantasmas de QA para quantificar a magnitude de artefatos de anel (*ring artifacts*, causados por falhas ou descalibração de elementos individuais em detectores multislice de estado sólido) e artefatos metálicos.
* **Algoritmos de Redução de Artefatos Metálicos (MAR):** A presença de próteses ortopédicas ou materiais dentários gera atenuação extrema e dispersão massiva, resultando em bandas de streaking severas. Técnicas avançadas baseadas em projeção (ex.: *Normalized Metal Artifact Reduction* - NMAR) substituem os dados corrompidos nos projeções por interpolação matemática antes da reconstrução iterativa.
* **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Algoritmos de IR estatísticos modelam o ruído de Poisson e a distribuição estatística do feixe, reduzindo artefatos quânticos associados a exames de baixa dose. Modelos DLR modernos são treinados para discriminar artefatos de estruturas anatômicas reais, embora o risco de remoção excessiva de texturas clínicas exigem rigorosa validação por observadores computacionais e físicos médicos.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Unidades Hounsfield|unidades-hounsfield]]
* [[Dosimetria em TC|dosimetria-em-tc]]
* [[Qualidade de Imagem em TC|qualidade-de-imagem]]