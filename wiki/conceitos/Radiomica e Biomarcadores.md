---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, radiomica, biomarcadores-de-imagem, pos-processamento]
data: 2026-08-25
---

# Radiomica_e_Biomarcadores

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Radiômica** (do inglês *Radiomics*) é um campo quantitativo da imagem médica que visa extrair, de forma automatizada e em larga escala, um vasto conjunto de características quantitativas (features) de imagens digitais. O princípio fundamental da radiômica postula que as imagens médicas contêm informações inerentes sobre a heterogeneidade microestrutural, arquitetural e funcional do tecido que excedem a capacidade de percepção visual humana. 

Quando esses recursos quantitativos extraídos de exames de Tomografia Computadorizada (TC) são validados, padronizados e correlacionados com endpoints clínicos, genotípicos ou fenotípicos, eles se transformam em **Biomarcadores de Imagem**. 

Do ponto de vista metrológico, a transição da imagem qualitativa (gradação visual por escores) para o dado quantitativo (radiômica) exige rigorosa padronização. A Tomografia Computadorizada é particularmente adequada para a radiômica devido à sua calibração inerente em unidades Hounsfield (HU), onde a intensidade de cada voxel reflete diretamente o coeficiente de atenuação linear do raio X em relação à água e ao ar. 

No entanto, a reprodutibilidade dos biomarcadores radiômicos enfrenta desafios físicos severos associados à variabilidade dos protocolos de aquisição e reconstrução em TC:
* **Parâmetros de Aquisição:** Tensão do tubo ($kVp$), corrente-tempo ($mAs$), espessura de corte e geometria do feixe.
* **Algoritmos de Reconstrução:** A transição de Retroprojeção Filtrada (FBP) para Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (DLR) altera drasticamente a textura da imagem, a resolução espacial e o ruído, impactando diretamente as características de 1ª e alta ordem.
* **Processos de Pré-processamento:** Resampling espacial, quantização de intensidade (número de bins de cinza) e normalização.

A rastreabilidade metrológica e a conformidade com diretrizes internacionais (como as da *Image Biomarker Standardization Initiative* - IBSI) são mandatórias para evitar artefatos sistemáticos que comprometam a acurácia diagnóstica e prognóstica.

---

## 2. Formulação Matemática e Propriedades

O pipeline radiômico transforma uma região de interesse (ROI) tridimensional $V$ (segmentada em uma matriz de imagem de TC) em um vetor de características quantitativas $\Phi$. 

Seja $f(x, y, z)$ a função de intensidade de imagem em unidades Hounsfield dentro do volume $V$, composto por $N$ voxels. As características radiômicas são comumente divididas em várias classes matemáticas:

### A. Estatísticas de Primeira Ordem (Histogram-based Features)
Descrevem a distribuição dos valores de intensidade de voxels dentro do ROI, desconsiderando suas relações espaciais.
* **Média:**
  
$$
\mu = \frac{1}{N} \sum_{i=1}^{N} X(i)
$$

* **Variância:**
  
$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} \left( X(i) - \mu \right)^2
$$

* **Assimetria (Skewness):**
  
$$
\text{Skewness} = \frac{\frac{1}{N} \sum_{i=1}^{N} \left( X(i) - \mu \right)^3}{\left(\sqrt{\sigma^2}\right)^3}
$$

* **Curtose (Kurtosis):**
  
$$
\text{Kurtosis} = \frac{\frac{1}{N} \sum_{i=1}^{N} \left( X(i) - \mu \right)^4}{\left(\sigma^2\right)^2}
$$

### B. Características de Textura Baseadas em Matrizes
Descrevem a distribuição espacial e as relações estatísticas entre os níveis de cinza dos voxels vizinhos.

* **Matriz de Co-ocorrência de Níveis de Cinza (GLCM - Gray Level Co-occurrence Matrix):**
  Representa a probabilidade conjunta $P_{\delta, \theta}(i, j)$ de dois voxels separados por um deslocamento espacial $\delta$ ao longo de um ângulo $\theta$ possuírem níveis de cinza $i$ e $j$.
  * *Energia (Angular Second Moment):*
    
$$
\text{Energy} = \sum_{i} \sum_{j} P(i, j)^2
$$

  * *Entropia:*
    
$$
\text{Entropy} = -\sum_{i} \sum_{j} P(i, j) \log_2 \left( P(i, j) + \epsilon \right)
$$

    onde $\epsilon$ é um valor infinitesimal para evitar indefinição matemática.
  * *Correlação:*
    
$$
\text{Correlation} = \sum_{i} \sum_{j} \frac{(i - \mu_i)(j - \mu_j) P(i, j)}{\sigma_i \sigma_j}
$$

* **Matriz de Comprimento de Corrida de Níveis de Cinza (GLRLM - Gray Level Run Length Matrix):**
  Mede o tamanho das sequências consecutivas (runs) de voxels com o mesmo nível de cinza ao longo de uma direção específica.
  * *Não Uniformidade de Níveis de Cinza (GLN):*
    
$$
\text{GLN} = \frac{\sum_{i=1}^{N_g} \left( \sum_{j=1}^{N_r} P(i, j) \right)^2}{\sum_{i=1}^{N_g} \sum_{j=1}^{N_r} P(i, j)}
$$

### C. Características Morfométricas e de Forma (Shape-based)
Descreviam as propriedades geométricas do volume $V$ segmentado, independentemente das intensidades dos voxels de TC.
* **Esfericidade (Sphericity):** Uma medida de quão próximo o tumor está de uma esfera perfeita.
  
$$
\text{Sphericity} = \frac{\pi^{\frac{1}{3}} \left( 6 \cdot V_{\text{vol}} \right)^{\frac{2}{3}}}{A_{\text{area}}}
$$

  onde $V_{\text{vol}}$ é o volume e $A_{\text{area}}$ é a área de superfície da lesão.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No contexto da Tomografia Computadorizada moderna, a integração da radiômica e o desenvolvimento de biomarcadores desempenham papéis críticos em múltiplas frentes da física médica e da prática clínica:

* **Oncologia de Precisão e Fenotipagem Tumoral:** Biomarcadores radiômicos derivados de exames de TC de tórax (para nódulos pulmonares) ou abdômen (para tumores hepáticos e pancreáticos) permitem a predição não invasiva de assinaturas genômicas (radiogenômica), resposta a terapias-alvo e estratificação de risco prognóstico.
* **Otimização de Protocolos e Dose:** Como a variabilidade no ruído e na resolução espacial afeta diretamente as features de textura, os algoritmos de controle de qualidade radiômicos exigem o uso de simuladores antropomórficos e phantoms de textura. Isso auxilia na otimização de parâmetros de aquisição que equilibram a redução de dose de radiação (ALARA) com a preservação da integridade informacional para a análise quantitativa.
* **Mitigação de Artefatos em Reconstrução (DLR e IR):** A adoção de Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction*) alterou os limiares de textura das imagens de TC. Estudos de harmonização radiômica (como ComBat) são aplicados para mitigar viés induzido por diferentes fabricantes de scanners e métodos de reconstrução, viabilizando a comparabilidade de biomarcadores em estudos multicêntricos.
* **Avaliação de Resposta Terapêutica:** Superando os critérios tradicionais baseados estritamente em mudanças dimensionais (como RECIST), a radiômica longitudinal avalia alterações na heterogeneidade interna do tumor (por exemplo, necrose induzida por terapia anti-angiogênica) muito antes de ocorrer a redução volumétrica mensurável.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[Processamento de Imagens Médicas|Processamento_de_Imagem]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa_e_DLR]]
* [[Qualidade_de_Imagem_e_Ruidos]]
* [[Inteligencia Artificial IA|Inteligencia_Artificial_em_Radiologia]]
* [[Dosimetria_e_Radioprotecao]]