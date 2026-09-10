---
tipo: conceito
tags: [fisica-medica, radioterapia, controle-de-qualidade, dosimetria, inteligencia-artificial, seguranca-paciente]
data: 2026-08-25
---

# Controle de Qualidade em Radioterapia

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Controle de Qualidade em Radioterapia (CQ)** abrange o conjunto sistemático de procedimentos operacionais, físicos, metrológicos e administrativos destinados a garantir que a prescrição médica de tratamento radioterápico seja executada com máxima precisão espacial, exatidão dosimétrica e reprodutibilidade clínica. Do ponto de vista metrológico, o CQ fundamenta-se nos conceitos de rastreabilidade a padrões primários de dose absorvida (como câmaras de ionização calibradas em laboratórios secundários de calibração dosimétrica - SSCL, vinculados ao BIPM), incerteza expandida, tolerância e ação corretiva.

Na radioterapia moderna — que inclui técnicas avançadas como Radioterapia Conformal com Modulação de Intensidade ([[IMRT]]), Radioterapia Guiada por Imagem ([[IGRT]]), Radiocirurgia Estereotáxica ([[SRS/SRT]]) e Terapia de Arco Volumetricamente Modulado ([[VRAP]]) —, a margem de erro permitida para a entrega da dose ao volume alvo tumoral é estritamente restrita (tipicamente $\pm 5\%$ na dose absoluta e $\pm 1\text{ mm}$ no posicionamento espacial). O CQ atua em múltiplos níveis:

1. **Controle de Qualidade de Aceitação (Commissioning):** Testes exaustivos realizados após a instalação de um novo equipamento para estabelecer a linha de base dos dados de feixe, algoritmos de cálculo do sistema de planejamento de tratamento ([[TPS]]) e limites operacionais.
2. **Controle de Qualidade Periódico (Rutine):** Verificações diárias, mensais e anuais exigidas por agências reguladoras (como a CNEN no Brasil, AAPM e IAEA) para monitorar o desgaste, a deriva instrumental e a estabilidade mecânica e dosimétrica.
3. **Controle de Qualidade Específicos de Paciente (Patient-Specific QA):** Verificações pré-tratamento que validam a entrega do plano computacional específico de cada paciente utilizando matrizes de diodos, filmes poliméricos ou fantomas antropomórficos.

A integração de modalidades de imagem avançadas, como a [[Tomografia Computadorizada|Tomografia Computadorizada]] de planejamento e imagens de feixe cônico ([[CBCT]]), exige que o CQ também assegure a fidelidade geométrica e a conversão correta dos números Hounsfield ([[Unidades Hounsfield|HU]]) em densidades eletrônicas relativas para o cálculo preciso da atenuação e do espalhamento da radiação.

---

## 2. Formulação Matemática e Propriedades

Para quantificar a concordância entre a dose calculada pelo TPS e a dose medida experimentalmente (por exemplo, via matrizes de detetores ou análise gama), utiliza-se amplamente o **Critério do Índice Gama ($\gamma$)**, introduzido por Low et al. O índice gama combina simultaneamente critérios de diferença de dose e distância até a concordância (Distance-to-Agreement - DTA).

Seja $\mathbf{r}_e$ a posição espacial de um ponto de avaliação experimental e $\mathbf{r}_c$ a posição de um ponto calculado. O índice gama $\Gamma(\mathbf{r}_e)$ é definido pela minimização sobre todas as posições calculadas $\mathbf{r}_c$:

$$
\Gamma(\mathbf{r}_e) = \min_{\mathbf{r}_c} \left\{ \sqrt{ \left( \frac{|\mathbf{r}_c - \mathbf{r}_e|}{\Delta d} \right)^2 + \left( \frac{D(\mathbf{r}_c) - D(\mathbf{r}_e)}{\Delta D} \right)^2 } \right\}
$$

Onde:
- $\Delta d$ é o critério de distância máxima aceitável (ex.: $2\text{ mm}$ ou $3\text{ mm}$).
- $\Delta D$ é o critério de tolerância de dose percentual aceitável (ex.: $2\%$ ou $3\%$).
- $D(\mathbf{r}_c)$ e $D(\mathbf{r}_e)$ são as doses calculada e medida, respectivamente.

Se $\Gamma(\mathbf{r}_e) \le 1$, o ponto atende aos critérios de aceitação clínicos. O mapa global de aprovação é dado pela porcentagem de pontos que satisfazem $\Gamma \le 1$ (geralmente exigindo-se uma taxa de aprovação superior a $95\%$ dos pontos avaliados com limiar de corte de dose inferior a $10\%$).

Adicionalmente, a incerteza combinada da dose absorvida em água sob condições de referência, $u_c(D_w)$, é propagada segundo o Guia para a Expressão da Incerteza na Medição (GUM):

$$
u_c^2(D_w) = \left( \frac{\partial D_w}{\partial M} \right)^2 u^2(M) + \left( \frac{\partial D_w}{\partial N_{D,w}} \right)^2 u^2(N_{D,w}) + \sum_{i} \left( \frac{\partial D_w}{\partial k_i} \right)^2 u^2(k_i)
$$

Onde $M$ é a leitura corrigida da câmara de ionização, $N_{D,w}$ é o fator de calibração da câmara em termos de dose absorvida em água, e $k_i$ representam os fatores de correção para qualidade de feixe, temperatura, pressão, recombinação iônica e polaridade.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A [[Tomografia Computadorizada|Tomografia Computadorizada]] (TC) desempenha um papel central no fluxo de trabalho de radioterapia, servindo como base geométrica para o contorno de órgãos-alvo e estruturas de risco, além de fornecer os mapas de densidade eletrônica necessários para os algoritmos de cálculo de dose (como o *Collapsed Cone Convolution* e *Monte Carlo*). Consequentemente, o CQ em radioterapia integra protocolos rigorosos de TC:

* **Calibração da Curva Hounsfield-to-Density:** Verificação periódica da relação entre os números de tomografia computacional ([[Unidades Hounsfield|HU]]) e a densidade eletrônica ($\rho_e$) utilizando fantomas específicos contendo inserções de tecidos equivalentes (tecido adiposo, osso cortical, pulmão, água). Desvios nessa curva introduzem erros sistemáticos no cálculo de dose.
* **Controle de Qualidade de Imagem por [[Inteligencia Artificial IA|Inteligência Artificial]] e [[Deep Learning|Deep Learning]]:** Algoritmos de reconstrução baseados em aprendizado profundo ([[Deep Learning Reconstruction (DLR)|DLR]]) e Redes Neurais Convolucionais ([[CNN]]) são cada vez mais utilizados para mitigação de artefatos de metal e redução de ruído em exames de TC de planejamento e [[CBCT]]. O CQ moderno exige a validação metrológica desses modelos para garantir que a melhoria visual da imagem não induza distorções geométricas ou perda de acurácia radiômica/densitométrica.
* **Controle de Qualidade em [[IGRT]] e Fusão de Imagens:** Avaliação da rigidez e precisão mecânica do sistema de imagem on-board (kV-CBCT, radiografia planar ortogonal) em relação ao isocentro do acelerador linear, assegurando que os vetores de correção de posicionamento do paciente calculados por algoritmos de registro rígido e deformável sejam fidedignos.
* **Observadores Computacionais e Radiômica:** Validação da estabilidade dos parâmetros de aquisição de TC para extração de biomarcadores de imagem (features radiômicas) utilizados na predição de resposta tumoral e toxicidade, onde variações nos protocolos de varredura ou reconstrução (FBP vs. Iterativa) afetam diretamente a reprodutibilidade dos dados.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[IMRT]]
- [[IGRT]]
- [[SRS/SRT]]
- [[VMAT]]
- [[Inteligencia Artificial IA|Inteligência Artificial]]
- [[Deep Learning|Deep Learning]]
- [[CNN]]
- [[Deep Learning Reconstruction (DLR)|DLR]]
- [[CBCT]]
- [[Unidades Hounsfield|HU]]