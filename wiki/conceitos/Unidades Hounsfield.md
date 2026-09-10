---
tipo: conceito
aliases: [Unidades_Hounsfield, Número_TC, Escala_Hounsfield]
tags: [fisica-medica, tomografia-computadorizada, metrologia, calibracao]
data: 2026-08-25
---

# Unidades_Hounsfield

## 1. Definição Conceitual e Fundamentação Física
As **Unidades Hounsfield (UH)**, também referidas na literatura como **Número Tomográfico (CT Number)**, constituem a unidade de medida quantitativa padronizada utilizada na Tomografia Computadorizada (TC) para expressar a atenuação de feixes de raios X pela matéria. Nomeada em homenagem a Sir Godfrey Hounsfield, co-inventor da TC, a escala mapeia os coeficientes de atenuação linear linearmente reconstruídos a partir dos dados de projeção em uma escala adimensional normalizada e clinicamente interpretável.

A fundamentação física baseia-se na dependência do coeficiente de atenuação linear ($\mu$), medido em $\text{cm}^{-1}$, em relação à energia dos fótons incidentes e ao número atômico efetivo ($Z_{eff}$) e à densidade eletrônica do meio material. Como o feixe de raios X na TC convencional é policromático, a atenuação sofre o fenômeno de *beam hardening* (endurecimento do feixe), exigindo correções rigorosas para que as Unidades Hounsfield permaneçam constantes e reprodutíveis independentemente do tamanho do objeto escaneado ou do protocolo de aquisição.

A escala é fixada em pontos de referência biológicos e físicos fundamentais sob condições padrão (geralmente água destilada a $20^\circ\text{C}$ e pressão atmosférica com energia efetiva equivalente):
* **Água:** Definida estritamente como $0\text{ UH}$.
* **Ar:** Definido estritamente como $-1000\text{ UH}$.

Valores extremos na escala clínica abrangem tecidos altamente densos, como o osso cortical, que podem ultrapassar $+1000\text{ UH}$ ou $+3000\text{ UH}$ dependendo do tipo de scanner e da formulação do algoritmo de reconstrução.

---

## 2. Formulação Matemática e Propriedades
Matematicamente, o valor do número tomográfico em Unidades Hounsfield para um determinado voxel com coeficiente de atenuação linear médio $\mu_{\text{tecido}}$ é expresso pela seguinte equação fundamental:

$$
\text{UH} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{agua}}}{\mu_{\text{agua}} - \mu_{\text{ar}}}
$$

Considerando que o coeficiente de atenuação linear do ar é aproximadamente zero ($\mu_{\text{ar}} \approx 0\text{ cm}^{-1}$), a equação é comumente simplificada para a forma operacional:

$$
\text{UH} = 1000 \times \frac{\mu_{\text{tecido}} - \mu_{\text{agua}}}{\mu_{\text{agua}}}
$$

### Propriedades Estatísticas e Incerteza de Medição
Em termos de processamento de imagem e metrologia, o ruído quântico e eletrônico inerente ao sistema de aquisição reflete-se diretamente na variabilidade espacial das Unidades Hounsfield. Para uma região de interesse (ROI) homogênea, a incerteza associada à determinação do número tomográfico é quantificada pelo desvio padrão $\sigma_{\text{UH}}$:

$$
\sigma_{\text{UH}} = \frac{1000}{\mu_{\text{agua}}} \cdot \sigma_{\mu}
$$

Onde $\sigma_{\mu}$ representa o desvio padrão dos coeficientes de atenuação linear na região analisada. A estabilidade temporal e espacial da média e do desvio padrão das UH em fantomas de referência são métricas fundamentais para o controle de qualidade quantitativo em exames avançados.

---

## 3. Contexto no Acervo do Pesquisador & Aplicações
No escopo das pesquisas desenvolvidas no laboratório (USP/FAPESP) sobre física médica e otimização de imagem, o rigor das **Unidades Hounsfield** desempenha um papel central em múltiplos frentes metodológicas:

1. **Controle de Qualidade e Metrologia em TC:** Conforme apontado no documento [[wiki/conceitos/auditoria_pipeline_davi_yyyymm.md|auditoria_pipeline_davi_yyyymm.md]], a calibração precisa das UH é o alicerce para assegurar a reprodutibilidade radiômica. Desvios na linearidade da escala Hounsfield comprometem a extração de *features* texturais e de primeira ordem.
2. **Radiômica e Aprendizado de Profundo (*Deep Learning*):** Como destacado em [[wiki/conceitos/dataset_.md|dataset_.md]], redes neurais convolucionais voltadas para segmentação e classificação de lesões dependem de uma normalização consistente dos inputs baseada estritamente nas faixas de UH (por exemplo, *windowing* pulmonar, mediastinal ou ósseo). Variações não corrigidas nas UH introduzem artefatos de domínio que degradam a generalização de modelos de Aprendizado de Profundo.
3. **Redução de Ruído e Reconstrução Iterativa:** Algoritmos avançados de reconstrução (como a reconstrução iterativa estatística e DLR) buscam preservar a exatidão quantitativa das UH mesmo em doses reduzidas de radiação, equilibrando a supressão de ruído (medida através do [[Noise Power Spectrum|NPS]]) sem viés no número tomográfico de estruturas anatômicas de baixo contraste.

---

## 4. Conexões e Wikilinks
* [[Controle de Qualidade em TC|Controle_de_Qualidade_TC]]
* [[Controle de Qualidade em TC|Controle_Qualidade_TC]]
* [[Transformada de Radon|Transformada de Radon]]
* [[Retroprojeção Filtrada (FBP)|FBP]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Reducao Ruído Deep Learning|Reducao_Ruido_Deep_Learning]]
* [[Deep Learning|Aprendizado_Profundo]]
* [[Radiomica|Radiomica]]
* [[Noise Power Spectrum|Espectro_Potencia_Ruido_NPS]]
* [[Função Transferencia Modulacao Mtf|Funcao_Transferencia_Modulacao_MTF]]