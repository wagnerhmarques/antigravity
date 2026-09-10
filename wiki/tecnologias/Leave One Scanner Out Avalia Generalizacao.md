---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, validacao-clinica, generalizacao, aprendizado-de-maquina, controle-de-qualidade]
data: 2026-08-25
---

# Leave_one_scanner_out_avalia_generalizacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **Leave-One-Scanner-Out (LOSO)** designa uma estratégia de validação cruzada estruturada, estritamente necessária no desenvolvimento e avaliação de modelos de Inteligência Artificial (IA) e aprendizado profundo (*Deep Learning*) aplicados à Física Médica e à Tomografia Computadorizada (TC). Em essência, o protocolo LOSO particiona o conjunto de dados com base na procedência física do equipamento de aquisição (o *scanner* de TC ou fabricante/modelo), em vez de realizar a divisão randômica convencional a nível de paciente ou de corte tomográfico.

Do ponto de vista metrológico e físico, imagens de Tomografia Computadorizada não são representações absolutas de unidades de atenuação, mas sim reconstruções matemáticas dependentes de inúmeras variáveis instrumentais e paramétricas. Diferentes tomógrafos introduzem variações sistêmicas irredutíveis decorrentes de:
* Geometria do sistema (distância fonte-detector, tamanho focal);
* Tecnologias e materiais de cintilação dos detectores (eficácia quântica de detecção - DQE);
* Filtros de conformação do feixe (*bow-tie filters*);
* Espectros de energia dos raios X (diferentes tensões de pico no tubo, $\text{kVp}$, e filtração inerente);
* Algoritmos proprietários de reconstrução (retroprojeção filtrada - FBP, reconstrução iterativa - IR, e redes de reconstrução baseadas em aprendizado profundo - DLR).

Quando um modelo de IA é treinado em dados provenientes de um subconjunto de scanners e testado em dados do scanner retido (*left-out*), o protocolo LOSO testa rigorosamente a **invariância de domínio** do algoritmo. Ele mede a capacidade do modelo de generalizar previsões (seja em segmentação, redução de ruído, conversão dose-baixa para dose-plena ou radiômica) perante artefatos de máquina, texturas de ruído específicas e vieses de calibração numérica (unidades Hounsfield - HU). O fracasso em um teste LOSO indica *overfitting* a assinaturas instrumentais específicas, o que compromete a tradutibilidade clínica do software em ambientes multicêntricos.

---

## 2. Formulação Matemática e Propriedades

Seja um conjunto global de dados de imagem $\mathcal{D}$ composto por $N$ exames de TC adquiridos em um parque tecnológico contendo $S$ scanners distintos, de modo que cada exame $\mathcal{X}_i$ está associado a uma etiqueta de scanner $s_i \in \{1, 2, \dots, S\}$. 

O conjunto de dados total pode ser particionado em $S$ subconjuntos disjuntos com base no scanner de origem:

$$
\mathcal{D} = \bigcup_{s=1}^{S} \mathcal{D}_s
$$

Onde $\mathcal{D}_s = \{(\mathbf{x}_j, y_j) \mid s_j = s\}$, com $\mathbf{x}_j$ representando a matriz tridimensional da imagem de TC e $y_j$ o alvo clínico ou físico correspondente.

Na validação cruzada **Leave-One-Scanner-Out**, o processo de treinamento e teste é iterado $S$ vezes. Para a $s$-ésima iteração, o conjunto de treinamento $\mathcal{T}_{\text{train}}^{(s)}$ e o conjunto de teste (ou validação cega) $\mathcal{T}_{\text{test}}^{(s)}$ são definidos estritamente como:

$$
\mathcal{T}_{\text{test}}^{(s)} = \mathcal{D}_s
\mathcal{T}_{\text{train}}^{(s)} = \bigcup_{k 
eq s} \mathcal{D}_k
$$

A função de otimização dos pesos $\theta$ do modelo de IA minimiza a perda empírica estritamente sobre o domínio de treinamento:

$$
\hat{\theta}^{(s)} = \arg\min_{\theta} \sum_{(\mathbf{x}, y) \in \mathcal{T}_{\text{train}}^{(s)}} \mathcal{L}\left(f_\theta(\mathbf{x}), y\right)
$$

O desempenho de generalização inter-scanner do modelo é avaliado no domínio não visto $\mathcal{T}_{\text{test}}^{(s)}$ através de uma métrica de avaliação $\mathcal{M}$ (como Erro Quadrático Médio, Índice de Dice, ou Erro Absoluto Médio em unidades Hounsfield):

$$
\text{Escore}_s = \frac{1}{|\mathcal{T}_{\text{test}}^{(s)}|} \sum_{(\mathbf{x}, y) \in \mathcal{T}_{\text{test}}^{(s)}} \mathcal{M}\left(f_{\hat{\theta}^{(s)}}(\mathbf{x}), y\right)
$$

O desempenho global robusto do algoritmo perante a variabilidade de fabricantes é dado pela média e desvio padrão dos escores obtidos em todas as $S$ dobras:

$$
\text{Performance}_{\text{LOSO}} = \frac{1}{S} \sum_{s=1}^{S} \text{Escore}_s \pm \sigma_{\text{LOSO}}
$$

### Propriedades Metrológicas:
1. **Ortogonalidade de Domínio:** Garante que $\mathcal{T}_{\text{train}}^{(s)} \cap \mathcal{T}_{\text{test}}^{(s)} = \emptyset$ tanto no nível de paciente quanto no nível de hardware, eliminando o vazamento de dados (*data leakage*) espacial e instrumental.
2. **Estimativa de Viés Sistemático:** Permite isolar se a degradação da acurácia do modelo é estocástica ou correlacionada a propriedades físicas específicas do fabricante (ex: artefatos de feixe cônico em TCs multislice de grande cobertura versus feixes paralelos/leque estreito).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A aplicação do protocolo *Leave-One-Scanner-Out* é indispensável para a translação clínica de algoritmos de inteligência artificial em ambientes hospitalares heterogêneos. Dentre os principais domínios de impacto na Tomografia Computadorizada, destacam-se:

* **Reconstrução de Domicílio Baixo (*Low-Dose CT - LDCT*) e Redução de Ruído:** Redutores de ruído baseados em redes neurais convolucionais (CNNs) ou modelos de difusão treinados em dados de um único tomógrafo frequentemente aprendem a textura de ruído específica daquele equipamento (frequências espaciais associadas ao filtro de retroprojeção). Ao aplicar o modelo em um scanner de outro fabricante, o algoritmo pode interpretar o ruído textural alheio como sinal patológico ou falhar na supressão adequada. O LOSO assegura que o filtro aprendido seja universalmente aplicável sem induzir perda de resolução espacial ou distorção radiométrica.
* **Radiômica Quantitativa e Biomarcadores de Imagem:** A extração de características de textura e formato (como assimetria, entropia e *glcm*) é notoriamente sensível a variações de scanner. Modelos preditivos baseados em radiômica que utilizam validação cruzada padrão frequentemente falham na validação clínica externa. O uso de LOSO na fase de seleção de features garante a robustez dos biomarcadores frente a mudanças de hardware.
* **Dosimetria Computacional e Segmentação Automática de Órgãos de Risco:** Em radioterapia, a segmentação precisa de volumes alvos e órgãos de risco (*OARs*) por IA deve operar independentemente de artefatos de endurecimento de feixe (*beam hardening*) ou de cortes espessos gerados por diferentes tomógrafos de planejamento. O LOSO valida a resiliência do segmentador perante contrastes de tecidos moles alterados por diferentes protocolos de aquisição.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[Reconstrucao_de_Imagem_FBP_IR_DLR]]
* [[Controle de Qualidade em TC|Controle_de_Qualidade_em_TC]]
* [[Radiomica_e_Biomarcadores_Quantitativos]]
* [[Dosimetria_em_Raio_X_e_TC]]
* [[Validacao_e_Generalizacao_de_IA]]
* [[Artefatos em Tomografia Computadorizada|Artefatos_em_Tomografia_Computadorizada]]