---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, metrologia, oalidade-de-imagem-tc, ruido, resolucao-espacial, artefatos]
data: 2026-08-25
---

# Qualidade_Imagem_TC

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Qualidade de Imagem em Tomografia Computadorizada (TC)** engloba o conjunto de propriedades físicas, visuais e metrológicas que determinam a precisão com que uma imagem tomográfica representa a anatomia tridimensional do paciente e patologias subjacentes. Diferente da radiografia planar convencional, a formação de imagem em TC envolve a reconstrução matemática de matrizes de coeficientes de atenuação linear ($µ$) a partir de projeções angulares múltiplas, tornando a qualidade da imagem um balanço complexo e multidimensional entre parâmetros físicos, limitações tecnológicas e restrições de dose de radiação ionizante.

Do ponto de vista metrológico, a qualidade da imagem em TC é avaliada por meio de métricas objetivas, subjetivas e baseadas em observadores, fundamentadas na Teoria da Informação e na Física Estatística. Os pilares fundamentais que regem a qualidade de imagem em TC são:

1. **Resolução Espacial:** Capacidade do sistema em distinguir duas estruturas anatômicas pequenas e de alto contraste espacialmente próximas.
2. **Resolução de Contraste (Baixo Contraste):** Capacidade de diferenciar estruturas com coeficientes de atenuação linear muito similares (ex: parênquima hepático e lesões focais sutis).
3. **Ruído da Imagem:** Flutuação estatística aleatória dos valores de número de Hounsfield (HU) em uma região homogênea, diretamente governada pela contagem de fótons detectados ($\text{Poisson noise}$).
4. **Linearidade e Uniformidade:** A constância dos valores de HU em diferentes regiões do phantom sob as mesmas condições de irradiação e a fidelidade da relação entre o coeficiente de atenuação do material e o número de Hounsfield atribuído.
5. **Artefatos:** Discrepâncias geométricas ou de intensidade entre os valores reais do coeficiente de atenuação do objeto escaneado e os valores representados na imagem reconstruída.

Estes parâmetros são interligados pelo princípio da otimização e pelo conceito ALARA (*As Low As Reasonably Achievable*), onde a melhoria de um parâmetro (ex: aumento da resolução espacial através de filtros de convolução mais agudos) inevitavelmente degrada outro (ex: aumento severo do ruído, exigindo maior dose de radiação).

---

## 2. Formulação Matemática e Propriedades

A quantificação rigorosa da qualidade de imagem em TC exige formulações matemáticas que descrevem o comportamento espacial e estocástico do sistema de imageamento.

### 2.1. Função de Espalhamento de Ponto (PSF) e Função de Transferência de Modulação (MTF)
A resposta de um sistema de TC a uma fonte pontual ideal é descrita pela *Point Spread Function* ($\text{PSF}(x,y)$). A Transformada de Fourier bidimensional da PSF normalizada define a **Função de Transferência de Modulação ($\text{MTF}$)**, que quantifica a preservação do contraste em função da frequência espacial ($f$):

$$
\text{MTF}(f_x, f_y) = \left| \frac{\iint \text{PSF}(x,y) e^{-j 2\pi (f_x x + f_y y)} \, dx\, dy}{\iint \text{PSF}(x,y) \, dx\, dy} \right|
$$

A frequência espacial limite, frequentemente avaliada no limiar de $\text{MTF} = 0.1$ (10%), define a resolução espacial limitante do sistema de TC.

### 2.2. Ruído da Imagem e Espectro de Potência de Ruído (NPS)
O ruído em TC é predominantemente regido pela estatística de fótons de Poisson. A desvio-padrão do ruído ($\sigma$) em uma imagem reconstruída por Retroprojeção Filtrada (FBP) com um filtro rampa de corte $f_c$ e espessura de corte $T$ é proporcional a:

$$
\sigma \propto \frac{1}{\sqrt{E \cdot \Phi_0 \cdot \Delta x^3 \cdot T}}
$$

Onde $E$ representa a energia efetiva do feixe, $\Phi_0$ o fluxo de fótons incidente e $\Delta x$ o tamanho do pixel.

Para uma caracterização espacial completa do ruído, utiliza-se o **Espectro de Potência de Ruído ($\text{NPS}$)**, definido como a Transformada de Fourier bidimensional da função de autocorrelação do ruído espacial $\mathcal{R}(\Delta x, \Delta y)$ em uma região de interesse homogênea:

$$
\text{NPS}(f_x, f_y) = \lim_{X,Y \to \infty} \frac{1}{X Y} \left| \iint_{X,Y} [\mu(x,y) - \bar{\mu}] e^{-j 2\pi (f_x x + f_y y)} \, dx\, dy \right|^2
$$

### 2.3. Detectability Index ($d'$) e Modelos de Observadores
A avaliação moderna da qualidade de imagem integra o desempenho humano ou matemático na detecção de sinais através do **Índice de Detectabilidade ($d'$)**, derivado da Teoria da Detecção de Sinais e frequentemente computado utilizando o Observador de Modelagem de Canal (channels-ized Hotelling observer - CHO):

$$
d'^2 = \frac{\left[ \iint W(f_x, f_y) S(f_x, f_y) \, df_x\, df_y \right]^2}{\iint W(f_x, f_y)^2 \text{NPS}(f_x, f_y) \, df_x\, df_y}
$$

Onde $S(f_x, f_y)$ é a Transformada de Fourier do sinal de interesse e $W(f_x, f_y)$ representa a função de ponderação do observador.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A gestão e otimização da Qualidade de Imagem em TC são mandatórias na prática clínica e na física médica regulatória. Suas principais frentes de aplicação englobam:

* **Controle de Qualidade (CQ) Periódico:** Utilização de phantoms padronizados (como o phantom ACR ou Catphan) para monitorar desvios na calibração de número de Hounsfield, linearity, espessura de corte, uniformidade e resolução espacial ao longo do ciclo de vida do equipamento.
* **Algoritmos de Reconstrução Avançados:** 
  * *Reconstrução Iterativa (IR):* Redução significativa do ruído mantendo a resolução espacial em doses mais baixas, modelando estatísticas complexas do sistema físico.
  * *Reconstrução Baseada em Deep Learning (DLR):* Redução de artefatos de ruído quântico e preservação de texturas anatômicas sutis através de redes neurais convolucionais treinadas com dados de alta dose ou simulações Monte Carlo.
* **Dosimetria e Otimização do Protocolo:** Balanceamento métrico rigoroso utilizando indicadores como CTDIvol e DLP em conjunto com a avaliação da qualidade de imagem (ex: métricas de contraste-ruído CNR) para garantir que o diagnóstico não seja comprometido pela redução de dose.
* **Controladores Automáticos de Corrente (AEC):** Sistemas dinâmicos que ajustam a corrente do tubo (mA) em tempo real baseados na atenuação angular e longitudinal do paciente, mantendo a qualidade de imagem (ruído constante) otimizada.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[Fisica_Radiologica]]
* [[Reconstrucao_Imagem_TC]]
* [[Filtro_Retroprojecao_FBP]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Inteligencia_Artificial_TC]]
* [[Dose_Radiacao_TC]]
* [[Numero_Hounsfield]]
* [[Artefatos em TC|Artefatos_TC]]
* [[Controle_Qualidade_Radiodiagnostico]]