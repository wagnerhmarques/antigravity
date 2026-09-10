---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radioprotecao, dosimetria, metrologia-das-radiacoes]
data: 2026-08-25
---

# dosimetria-em-tc

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **dosimetria em Tomografia Computadorizada (TC)** engloba o conjunto de conceitos físicos, grandezas metrológicas, métodos experimentais e modelos computacionais empregados para quantificar a energia depositada pelas radiações ionizantes (raios X) nos tecidos biológicos durante exames e procedimentos intervencionistas guiados por TC. 

Diferente da radiografia planar convencional, a irradiação em TC caracteriza-se por uma geometria helicoidal ou axial complexa, onde um feixe de raios X estreito e altamente colimado orbita o paciente, resultando em um perfil de dose unidirecional ao longo do eixo longitudinal ($z$) que se sobrepõe a espalhamentos internos significativos.

Metrologicamente, a complexidade do campo de radiação na TC exigiu o desenvolvimento de grandezas padronizadas que superassem as limitações das grandezas tradicionais de proteção (como a dose absorvida pontual). As fundações metrológicas baseiam-se na utilização de câmaras de ionização de comprimento específico (tipicamente câmaras do tipo *pencil* de $100\text{ mm}$ de comprimento ativo) calibradas em termos de kerma no ar em ar livre, a partir das quais derivam-se as grandezas operacionais e de avaliação de risco otimizadas para protocolos de TC:

*   **Kerma no ar ($K$):** A energia cinética transferida aos elétrons por unidade de massa liberada por fótons em um ponto no ar.
*   **Dose Absorvida ($D$):** A energia média repassada pela radiação ionizante à matéria por unidade de massa em um ponto anatômico de interesse ($D = \frac{d\bar{E}}{dm}$).

A quantificação rigorosa na TC é vital para equilibrar o compromisso fundamental da modalidade: maximizar a qualidade diagnóstica da imagem (relação sinal-ruído e contraste-ruído) enquanto minimiza-se o detrimento estocástico e determinístico induzido ao paciente.

---

## 2. Formulação Matemática e Propriedades

A base matemática da dosimetria em TC fundamenta-se na integração espacial do perfil de dose ao longo do eixo de rotação do equipamento. A grandeza primária de medição em manequins padronizados é o **Kerma no ar integrado no perfil de dose**, que dá origem ao Índice de Dose da Tomografia Computadorizada ($CTDI$).

### 2.1. CTDI (Computed Tomography Dose Index)
O $CTDI_{100}$ é definido pela integral do perfil de dose ao longo de uma linha paralela ao eixo de rotação ($z$), dividido pelo produto do número de tomografias ($N$) e a espessura nominal do feixe individual ($T$):

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ cm}}^{+50\text{ cm}} D(z) \, dz
$$

Na prática, com uma câmara de ionização de $100\text{ mm}$, o $CTDI_{100}$ é medido diretamente em uma única varredura axial:

$$
CTDI_{100} = \frac{T}{100\text{ mm}} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

### 2.2. CTDI ponderado ($CTDI_{w}$)
Como a distribuição da dose no interior de um manequim cilíndrico de polimetilmetacrilato (PMMA) — simulando a cabeça ($16\text{ cm}$ de diâmetro) ou o corpo ($32\text{ cm}$ de diâmetro) — é heterogênea (maior na periferia do que no centro devido à atenuação geométrica e atenuamento do feixe), define-se o $CTDI_{w}$ para ponderar estas contribuições:

$$
CTDI_{w} = \frac{1}{3} CTDI_{\text{centro}} + \frac{2}{3} CTDI_{\text{periferia}}
$$

Onde $CTDI_{\text{periferia}}$ é a média aritmética obtida nas quatro posições periféricas do manequim (geralmente ângulos de $0^\circ, 90^\circ, 180^\circ \text{ e } 270^\circ$).

### 2.3. CTDI volumétrico ($CTDI_{vol}$)
Para contemplar o efeito do espaçamento entre cortes axiais ou o passo (*pitch*, $p$) em varreduras helicoidais, o $CTDI_{vol}$ introduz a correção pelo avanço da mesa por rotação:

$$
CTDI_{vol} = \frac{CTDI_{w}}{p}
$$

Onde o *pitch* ($p$) é definido como:
*   Para TC helicoidal: $p = \frac{d}{N \cdot T}$ (sendo $d$ o deslocamento da mesa por rotação de $360^\circ$).
*   Para TC axial (sequencial): $p = \frac{I}{N \cdot T}$ (sendo $I$ o incremento da mesa entre varreduras consecutivas).

### 2.4. Dose-Length Product (DLP)
O Produto Dose-Comprimento (*Dose-Length Product* - $DLP$) correlaciona a energia total depositada ao longo de todo o volume escaneado, sendo expresso em $\text{mGy}\cdot\text{cm}$:

$$
DLP = CTDI_{vol} \cdot L_{\text{scan}}
$$

Onde $L_{\text{scan}}$ representa o comprimento total da varredura anatômica (excluindo as extensões de transição do feixe em alguns contextos normativos).

### 2.5. Dose Efetiva ($E$)
A estimativa do risco estocástico populacional requer o cálculo da dose efetiva ($E$), expressa em Sieverts ($\text{Sv}$ ou $\text{mSv}$), que pondera as doses absorvidas nos diferentes órgãos e tecidos sensíveis ($D_T$) pelos respectivos fatores de peso tecidual ($w_T$) recomendados pela ICRP (Comissão Internacional de Proteção Radiológica):

$$
E = \sum_T w_T \cdot D_T = \sum_T w_T \left( \frac{D_{T, \text{organ}}}{DLP} \right) \cdot DLP = k_{\text{e}}\cdot DLP
$$

Onde $k_{\text{e}}$ representa o coeficiente de conversão específico da região anatômica escaneada ($\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria em TC não se restringe à mera conformidade regulatória; ela é o pilar central para a **otimização da proteção radiológica** (princípio ALADA / ALARA) e o controle de qualidade clínico.

### 3.1. Controle de Qualidade (CQ) e Homologação de Sistemas
Manutenção e testes de aceitação de tomógrafos exigem a verificação periódica do rendimento do feixe e da concordância entre o $CTDI_{vol}$ exibido pelo console do equipamento e os valores medidos por meio de matrizes de manequins padronizados e eletsômetros calibrados. Desvios superiores aos limites aceitáveis (tipicamente $\pm 20\%$) indicam falhas na calibração da filtração, colimação ou corrente do tubo de raios X.

### 3.2. Dosimetria Baseada em Reconstrução e Inteligência Artificial (DLR)
Com o advento de técnicas avançadas de reconstrução de imagem — como a Retroprojeção Filtrada ($FBP$), Reconstrução Iterativa ($IR$) e, mais recentemente, algoritmos de Aprendizado Profundo (*Deep Learning Reconstruction* - $DLR$) — a dosimetria moderna evoluiu para além do $CTDI_{vol}$ macroscópico. 
*   **Redução de Dose via DLR:** Permite operar com reduções significativas no $CTDI_{vol}$ (frequentemente superiores a $50\%$) mantendo ou melhorando a detectabilidade de lesões de baixo contraste.
*   **Mapas de Dose Específicos do Paciente (Patient-Specific Dosimetry):** Métodos computacionais baseados em simulações de Monte Carlo acopladas a modelos anatômicos derivados de inteligência artificial calculam a distribuição tridimensional exata da dose absorvida voxel a voxel, considerando a geometria particular, o índice de massa corporal (IMC) e a atenuação individual do paciente, superando as limitações dos manequins cilíndricos padronizados.

### 3.3. Gestão de Protocolos e Alertas de Dose
Sistemas modernos de TC integram rastreamento automatizado de doses acumuladas por paciente, englobando protocolos multipásicos. A integração de protocolos baseados em *Automatic Tube Current Modulation* (ATCM) exige monitoramento rigoroso da dosimetria para garantir que a modulação espacial (nas direções angular e longitudinal) responda adequadamente à atenuação do paciente sem introduzir ruídos diagnósticos inaceitáveis.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|tomografia-computadorizada]]
*   [[qualidade-da-imagem-em-tc]]
*   [[Reconstrução de Imagem|reconstrucao-de-imagem]]
*   [[Inteligencia Artificial IA|inteligencia-artificial-em-radiologia]]
*   [[radiobiologia]]
*   [[Processamento de Sinais e Imagens|processamento-de-sinais-e-imagens]]