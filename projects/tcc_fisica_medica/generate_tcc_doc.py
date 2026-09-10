import os

target_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md"

content = r"""---
tipo: tcc-monografia
titulo: "Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo"
autor: "Wagner H. M."
orientador: "Prof. Dr. Paulo Roberto Costa"
instituicao: "Instituto de Física da Universidade de São Paulo (IFUSP)"
departamento: "Departamento de Física Nuclear - GDRFM"
data: 2026-09-01
versao: "1.0-draft"
tags:
  - tcc
  - fisica-medica
  - tomografia-computadorizada
  - task-based-image-quality
  - model-observers
  - deep-learning
  - otimizacao-multiobjetivo
---

# UNIVERSIDADE DE SÃO PAULO
## INSTITUTO DE FÍSICA
### DEPARTAMENTO DE FÍSICA NUCLEAR
#### GRUPO DE DOSIMETRIA E RADIOPROTEÇÃO EM FÍSICA MÉDICA (GDRFM-IFUSP)

---

<br>

# **MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA**
### *Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo*

<br>

**Autor:** Wagner H. M.  
**Orientador:** Prof. Dr. Paulo Roberto Costa  
**Monografia de Conclusão de Curso** apresentada ao Instituto de Física da Universidade de São Paulo como parte dos requisitos para obtenção do título de Bacharel em Física com Habilitação em Física Médica.

<br>

---

## RESUMO

A tomografia computadorizada (TC) desempenha papel central no diagnóstico médico moderno, operando sob a tensão contínua entre a redução da dose de radiação ionizante e a preservação da acurácia diagnóstica. Tradicionalmente, o controle e a garantia da qualidade de imagem em TC basearam-se em métricas físicas globais lineares, tais como a Relação Sinal-Ruído ($SNR$), a Relação Contraste-Ruído ($CNR$) e a Função de Transferência de Modulação ($MTF$), avaliadas em *phantoms* homogêneos e geométricos. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares — incluindo Reconstruções Iterativas Híbridas ($HIR$), Reconstruções Iterativas Baseadas em Modelos ($MBIR$) e, fundamentalmente, Reconstruções Baseadas em Aprendizado Profundo ($DLR$) — rompeu as premissas clássicas de linearidade e invariância translacional do sistema. Nessas condições, a textura e a magnitude do ruído tornaram-se espacialmente heterogêneas, dependentes da dose e do contraste local da estrutura anatômica, resultando em alterações perceptuais (como o aspecto artificialmente suavizado ou *"plastic/waxy look"*) que não são adequadamente capturadas por métricas escalares convencionais.

Para superar essas limitações, a metrologia em física médica convergiu para o paradigma da **Qualidade de Imagem Baseada em Tarefa** (*Task-Based Image Quality* - TBIQ), fundamentado na Teoria de Detecção de Sinais ($SDT$). Neste arcabouço, a qualidade da imagem é quantificada pela capacidade de um observador (humano ou matemático) executar uma tarefa diagnóstica clínica específica, expressa pelo **Índice de Detectabilidade** ($d'$). Este trabalho apresenta uma revisão crítica e aprofundada da evolução conceitual, matemática e experimental dos observadores de modelo (*model observers*). Analisa-se a transição histórica do Observador Ideal Bayesiano ($IO$) para os modelos lineares que incorporam filtros oculares ($NPWE$) e canais corticais de frequência ($CHO$), evidenciando suas forças em fundos estacionários e sua incapacidade de modelar a percepção humana sob reconstruções não lineares e fundos anatômicos complexos.

Em resposta a esse esgotamento analítico, discute-se o estado da arte representado pelos **Observadores de Modelo Baseados em Aprendizado Profundo** (*Deep Learning Model Observers* - DLMO), capazes de aprender correlações não lineares complexas calibradas diretamente contra o desempenho psicofísico de médicos radiologistas em experimentos de Escolha Forçada entre Duas Alternativas ($2AFC$). Por fim, este trabalho articula a integração desses novos modelos à **Otimização Multiobjetivo**, expandindo o tradicional compromisso bidimensional (dose *vs.* detectabilidade) para uma fronteira de Pareto tridimensional $(D, T, -W)$, que incorpora o tempo operacional ($T$) de aquisição e reconstrução junto à dose de radiação ($D$) e ao desempenho diagnóstico ($W$). Esta monografia consolida as bases teóricas que subsidiam a próxima geração de metrologia em TC e pavimenta o desenvolvimento do projeto de Doutorado Direto do autor.

**Palavras-chave:** Tomografia Computadorizada; Avaliação Baseada em Tarefa; Observadores de Modelo; Índice de Detectabilidade; Reconstrução por Aprendizado Profundo; Phantoms Antropomórficos; Otimização Multiobjetivo; Fronteira de Pareto.

---

## ABSTRACT

Computed Tomography (CT) plays a pivotal role in modern clinical diagnosis, continuously operating under the trade-off between ionizing radiation dose reduction and the preservation of diagnostic accuracy. Historically, image quality assurance in CT relied on linear global physical metrics, such as Signal-to-Noise Ratio ($SNR$), Contrast-to-Noise Ratio ($CNR$), and Modulation Transfer Function ($MTF$), evaluated on homogeneous geometric phantoms. However, the widespread clinical adoption of non-linear reconstruction algorithms—including Hybrid Iterative Reconstruction ($HIR$), Model-Based Iterative Reconstruction ($MBIR$), and Deep Learning Image Reconstruction ($DLR$)—has broken the fundamental assumptions of system linearity and shift-invariance. Under non-linear processing, noise texture and magnitude become spatially non-stationary, dose-dependent, and scene-dependent, introducing perceptual alterations (such as the "plastic" or "waxy" appearance) that cannot be properly quantified by standard scalar metrics.

To address these shortcomings, medical physics metrology has converged toward the **Task-Based Image Quality** (TBIQ) paradigm, grounded in Signal Detection Theory ($SDT$). In this framework, image quality is rigorously defined by the performance of an observer (human or mathematical model) in executing a specific clinical diagnostic task, quantified by the **Detectability Index** ($d'$). This monograph provides an in-depth, rigorous review of the conceptual, mathematical, and experimental evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer ($IO$) to linear anthropomorphic models incorporating eye filters ($NPWE$) and cortical frequency channels ($CHO$), highlighting their strengths in stationary backgrounds as well as their failure in non-linear reconstruction regimes and structured anatomical backgrounds.

To overcome these structural limitations, we investigate the state of the art in **Deep Learning Model Observers** (DLMO), which leverage non-linear neural representations calibrated against expert radiologists' psychophysical performance in Two-Alternative Forced Choice ($2AFC$) paradigms. Finally, this work integrates these modern observers into a **Multi-Objective Optimization** framework, expanding the traditional two-dimensional trade-off (dose *vs.* detectability) into a three-dimensional Pareto frontier $(D, T, -W)$ that explicitly incorporates operational time ($T$) alongside radiation dose ($D$) and diagnostic performance ($W$). This study establishes the theoretical and physical foundation required for next-generation CT metrology, setting the stage for the author's Direct Doctorate research.

**Keywords:** Computed Tomography; Task-Based Image Quality; Model Observers; Detectability Index; Deep Learning Reconstruction; Anthropomorphic Phantoms; Multi-Objective Optimization; Pareto Frontier.

---

## LISTA DE ABREVIATURAS E SÍMBOLOS

| Sigla / Símbolo | Significado |
| :--- | :--- |
| **2AFC** | *Two-Alternative Forced Choice* (Escolha Forçada entre Duas Alternativas) |
| **AAPM** | *American Association of Physicists in Medicine* |
| **AEC** | *Automatic Exposure Control* (Controle Automático de Exposição) |
| **ALARA** | *As Low As Reasonably Achievable* |
| **AUC** | *Area Under the ROC Curve* (Área sob a Curva ROC) |
| **BKE** | *Background Known Exactly* (Fundo Conhecido Exatamente) |
| **BKS** | *Background Known Statistically* (Fundo Conhecido Estatisticamente) |
| **CHO** | *Channelized Hotelling Observer* (Observador de Hotelling Canalizado) |
| **CNR** | *Contrast-to-Noise Ratio* (Relação Contraste-Ruído) |
| **CSF** | *Contrast Sensitivity Function* (Função de Sensibilidade ao Contraste) |
| **CTDI / CTDIvol** | *Computed Tomography Dose Index* (Índice de Dose Volumétrico em TC) |
| **D-DOG** | *Dense Difference of Gaussians* (Diferença Densa de Gaussianas) |
| **DLR / DLIR** | *Deep Learning Image Reconstruction* (Reconstrução por Aprendizado Profundo) |
| **DLMO** | *Deep Learning Model Observer* (Observador de Modelo por Aprendizado Profundo) |
| **DQE** | *Detective Quantum Efficiency* (Eficiência Quântica de Detecção) |
| **$d'$** | *Detectability Index* (Índice de Detectabilidade) |
| **$E(f)$** | Filtro Ocular Humano (*Eye Filter*) no Domínio das Frequências |
| **FBP** | *Filtered Backprojection* (Retroprojeção Filtrada) |
| **HO** | *Hotelling Observer* (Observador de Hotelling) |
| **HU** | Unidade Hounsfield (*Hounsfield Unit*) |
| **IAEA** | *International Atomic Energy Agency* (Agência Internacional de Energia Atômica) |
| **ICRU** | *International Commission on Radiation Units and Measurements* |
| **IO** | *Ideal Observer* (Observador Ideal Bayesiano) |
| **IR / HIR / MBIR** | Reconstrução Iterativa / Híbrida / Baseada em Modelos |
| **MRMC** | *Multi-Reader Multi-Case* (Múltiplos Leitores e Múltiplos Casos) |
| **MTF** | *Modulation Transfer Function* (Função de Transferência de Modulação) |
| **NPS** | *Noise Power Spectrum* (Espectro de Potência do Ruído) |
| **NPW / NPWE** | *Non-Prewhitening Observer / with Eye Filter* |
| **PCCT** | *Photon-Counting Computed Tomography* (TC por Contagem de Fótons) |
| **ROC** | *Receiver Operating Characteristic* (Característica de Operação do Receptor) |
| **ROI** | *Region of Interest* (Região de Interesse) |
| **SDT** | *Signal Detection Theory* (Teoria de Detecção de Sinais) |
| **SKE** | *Signal Known Exactly* (Sinal Conhecido Exatamente) |
| **SNR** | *Signal-to-Noise Ratio* (Relação Sinal-Ruído) |
| **TG-233** | *Task Group 233* da AAPM |
| **TTF** | *Task Transfer Function* (Função de Transferência da Tarefa) |
| **ViT** | *Vision Transformer* |
| **VMI** | *Virtual Monoenergetic Image* (Imagem Monoenergética Virtual) |
| **$W_{\text{task}}(f)$** | Espectro de Potência da Tarefa Diagnóstica / Sinal |

---

# SUMÁRIO

1. [Capítulo 1: Introdução e Contextualização](#capítulo-1-introdução-e-contextualização)
   - 1.1 [O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico](#11-o-dilema-fundamental-da-tomografia-computadorizada-dose-versus-desempenho-clínico)
   - 1.2 [Limitações das Métricas Físicas Globais Tradicionais na Prática Hospitalar](#12-limitações-das-métricas-físicas-globais-tradicionais-na-prática-hospitalar)
   - 1.3 [A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality*)](#13-a-mudança-de-paradigma-qualidade-de-imagem-baseada-em-tarefa-task-based-image-quality)
   - 1.4 [Objetivos e Estrutura da Monografia](#14-objetivos-e-estrutura-da-monografia)
2. [Capítulo 2: Fundamentos Teóricos e Matemáticos da Qualidade Baseada em Tarefa](#capítulo-2-fundamentos-teóricos-e-matemáticos-da-qualidade-baseada-em-tarefa)
   - 2.1 [Teoria de Detecção de Sinais (SDT) e Tomada de Decisão Estatística](#21-teoria-de-detecção-de-sinais-sdt-e-tomada-de-decisão-estatística)
   - 2.2 [O Índice de Detectabilidade ($d'$) no Domínio Espacial](#22-o-índice-de-detectabilidade-d-no-domínio-espacial)
   - 2.3 [Caracterização no Domínio das Frequências: TTF, NPS e Filtro Ocular](#23-caracterização-no-domínio-das-frequências-ttf-nps-e-filtro-ocular)
     - 2.3.1 [Função de Transferência da Tarefa ($TTF(f)$)](#231-função-de-transferência-da-tarefa-ttff)
     - 2.3.2 [Espectro de Potência do Ruído ($NPS(f)$)](#232-espectro-de-potência-do-ruído-npsf)
     - 2.3.3 [Filtro Ocular ($E(f)$) e a Função de Sensibilidade ao Contraste Humano](#233-filtro-ocular-ef-e-a-função-de-sensibilidade-ao-contraste-humano)
     - 2.3.4 [Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$)](#234-espectro-da-tarefa-diagnóstica-w_texttaskf)
   - 2.4 [Paradigmas de Detecção e a Metodologia Psicofísica 2AFC](#24-paradigmas-de-detecção-e-a-metodologia-psicofísica-2afc)
3. [Capítulo 3: A Era dos Observadores Lineares](#capítulo-3-a-era-dos-observadores-lineares)
   - 3.1 [O Observador Ideal Bayesiano (IO) e o Limite Superior de Desempenho](#31-o-observador-ideal-bayesiano-io-e-o-limite-superior-de-desempenho)
   - 3.2 [O Observador NPW e a Inclusão do Filtro Ocular (NPWE)](#32-o-observador-npw-e-a-inclusão-do-filtro-ocular-npwe)
   - 3.3 [O Desafio dos Fundos Estruturados: Hotelling Observer (HO) e Channelized Hotelling Observer (CHO)](#33-o-desafio-dos-fundos-estruturados-hotelling-observer-ho-e-channelized-hotelling-observer-cho)
   - 3.4 [Validação com Leitores Humanos: Estudos 2AFC e Metodologia MRMC](#34-validação-com-leitores-humanos-estudos-2afc-e-metodologia-mrmc)
4. [Capítulo 4: O Colapso da Linearidade e os Simuladores Físicos Modernos](#capítulo-4-o-colapso-da-linearidade-e-os-simuladores-físicos-modernos)
   - 4.1 [Evolução dos Algoritmos de Reconstrução: Da FBP às Reconstruções Iterativas e DLR](#41-evolução-dos-algoritmos-de-reconstrução-da-fbp-às-reconstruções-iterativas-e-dlr)
   - 4.2 [A Quebra da Linearidade e a Não-Estacionariedade do Ruído](#42-a-quebra-da-linearidade-e-a-não-estacionariedade-do-ruído)
   - 4.3 [A Transição dos *Phantoms*: De Geometrias Homogêneas a Simuladores Antropomórficos e Híbridos](#43-a-transição-dos-phantoms-de-geometrias-homogêneas-a-simuladores-antropomórficos-e-híbridos)
   - 4.4 [Tratamento de Ruído em Fundos Complexos: *Detrending* e Quase-Estacionariedade](#44-tratamento-de-ruído-em-fundos-complexos-detrending-e-quase-estacionariedade)
5. [Capítulo 5: O Estado da Arte: Observadores de Aprendizado Profundo e Otimização Multiobjetivo](#capítulo-5-o-estado-da-arte-observadores-de-aprendizado-profundo-e-otimização-multiobjetivo)
   - 5.1 [Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO)](#51-observadores-baseados-em-aprendizado-profundo-deep-learning-model-observers---dlmo)
   - 5.2 [Calibração Perceptual com Radiologistas e Transferibilidade Inter-Scanners](#52-calibração-perceptual-com-radiologistas-e-transferibilidade-inter-scanners)
   - 5.3 [Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional $(D, T, -W)$](#53-otimização-multiobjetivo-em-tc-a-fronteira-de-pareto-tridimensional-d-t--w)
   - 5.4 [Novas Tecnologias: Tomografia por Contagem de Fótons (PCCT) e Imagens Monoenergéticas](#54-novas-tecnologias-tomografia-por-contagem-de-fótons-pcct-e-imagens-monoenergéticas)
6. [Capítulo 6: Considerações Finais e Perspectivas](#capítulo-6-considerações-finais-e-perspectivas)
   - 6.1 [Síntese da Trajetória Biofísica e Metrológica](#61-síntese-da-trajetória-biofísica-e-metrológica)
   - 6.2 [Impacto Clínico, Operacional e Normativo](#62-impacto-clínico-operacional-e-normativo)
   - 6.3 [Articulação com a Pesquisa de Doutorado Direto](#63-articulação-com-a-pesquisa-de-doutorado-direto)
7. [Referências Bibliográficas](#referências-bibliográficas)

---

# CAPÍTULO 1: INTRODUÇÃO E CONTEXTUALIZAÇÃO

## 1.1 O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico

A Tomografia Computadorizada (TC) revolucionou a medicina diagnóstica desde sua introdução clínica por Godfrey Hounsfield na década de 1970. Sua capacidade de fornecer secções transversais anatômicas de alta resolução espacial e diferenciação de tecidos moles consolidou-a como a principal modalidade tomográfica de suporte a decisões clínicas agudas e crônicas, abrangendo o estadiamento oncológico, o planejamento cirúrgico, o rastreamento pulmonar e a avaliação de traumas graves.

Contudo, a aquisição tomográfica fundamenta-se na atenuação de feixes de raios X transmitidos através do paciente. A interação da radiação ionizante com o tecido biológico confere aos exames de TC uma contribuição desproporcional à dose coletiva de radiação de origem médica na população global: embora represente aproximadamente 10% a 15% do total de procedimentos radiológicos diagnósticos, a TC é responsável por mais de 60% a 70% da dose de radiação ionizante acumulada pela medicina diagnóstica em países desenvolvidos (MCCOLLOUGH et al., 2026; IAEA, 2026).

Essa realidade impõe aos físicos médicos e radiologistas a obrigatoriedade de cumprir o princípio **ALARA** (*As Low As Reasonably Achievable*), buscando a otimização contínua dos protocolos de aquisição. O dilema central da TC reside na relação estocástica intrínseca entre a fluência de fótons de raios X e o ruído da imagem. Em termos físicos elementares:

$$\sigma_{\text{ruído}} \propto \frac{1}{\sqrt{N_{\text{fótons}}}} \propto \frac{1}{\sqrt{\text{Dose}}}$$

Assim, qualquer tentativa de reduzir a dose de radiação ionizante sem intervenção algorítmica resulta em um aumento imediato do ruído quântico da imagem, o que pode degradar a visibilidade de estruturas críticas e de baixo contraste — como pequenos nódulos pulmonares, metástases hepáticas ou lesões isquêmicas encefálicas precoces —, comprometendo a segurança diagnóstica do paciente.

## 1.2 Limitações das Métricas Físicas Globais Tradicionais na Prática Hospitalar

Durante décadas, a rotina de controle de qualidade e a avaliação de desempenho de tomógrafos clínicos apoiaram-se em métricas físicas clássicas escalares, derivadas da teoria de sistemas lineares invariantes no espaço:

1. **Desvio Padrão do Número CT ($\sigma_{\text{HU}}$) / Nível Global de Ruído:** Medido em regiões de interesse (ROIs) posicionadas no centro de *phantoms* cilíndricos homogêneos de água ou PMMA.
2. **Relação Sinal-Ruído ($SNR$) e Relação Contraste-Ruído ($CNR$):**
   $$CNR = \frac{|\overline{HU}_{\text{alvo}} - \overline{HU}_{\text{fundo}}|}{\sigma_{\text{fundo}}}$$
3. **Função de Transferência de Modulação ($MTF$):** Extraída a partir da resposta ao impulso (Point Spread Function - $PSF$) de fios finos ou esferas de alto contraste em ar/fundo uniforme.

Embora essas métricas sejam úteis para testes de constância sob a hipótese de **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP), elas falham sistematicamente quando aplicadas aos sistemas de TC contemporâneos (SAMEI et al., 2019 - AAPM TG-233). 

A causa fundamental dessa falha é a introdução de técnicas de reconstrução não lineares. A $CNR$, por exemplo, considera apenas o contraste médio e a variância pontual dos números de CT, ignorando completamente:
- A correlação espacial entre pixels vizinhos (textura do ruído);
- A dependência da resolução espacial em relação ao contraste local e ao nível de dose;
- A capacidade de processamento do sistema visual humano, que não atua como um integrador simples de variância pontual.

Uma imagem processada por filtros de suavização espacial agressivos pode apresentar desvio padrão ($\sigma$) muito baixo e $CNR$ formalmente elevada, porém com perda severa de bordas e alteração grosseira da textura do ruído, tornando lesões sutis completamente invisíveis ao radiologista.

## 1.3 A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality*)

Diante das limitações das métricas escalares, a comunidade internacional de física médica estabeleceu que a qualidade de uma imagem médica não é uma propriedade física intrínseca e abstrata, mas sim uma medida de sua utilidade para uma **tarefa diagnóstica específica** (ICRU Report 54, 1996; BARRETT & MYERS, 2004; SAMEI et al., 2019).

O arcabouço de **Qualidade de Imagem Baseada em Tarefa** (*Task-Based Image Quality* - TBIQ) ancora-se na Teoria de Detecção de Sinais ($SDT$). A qualidade de imagem é operacionalizada por meio da capacidade de um observador (um radiologista humano ou um modelo computacional que emula a visão humana) de discriminar entre duas hipóteses clínicas fundamentais:
- $H_0$: Ausência de patologia (imagem com ruído de fundo apenas);
- $H_1$: Presença de patologia (sinal/lesão de tamanho, morfologia e contraste conhecidos sobreposto ao ruído de fundo).

A métrica quantitativa central da TBIQ é o **Índice de Detectabilidade** ($d'$), que quantifica a separação estatística entre as distribuições de decisão do observador sob $H_0$ e $H_1$. Diferente da $CNR$, o cálculo de $d'$ integra a resolução espacial modulada pela tarefa ($TTF$), a estrutura espectral do ruído ($NPS$), as propriedades morfológicas do sinal ($W_{\text{task}}$) e a sensibilidade do sistema visual humano ($E(f)$).

```
   +-------------------------------------------------------------+
   |              AVALIAÇÃO BASEADA NA TAREFA (TBIQ)             |
   +-------------------------------------------------------------+
          |                         |                        |
          v                         v                        v
   [Resolução do Sistema]     [Textura do Ruído]    [Biologia Humana]
   Função de Transferência   Espectro de Potência   Filtro Ocular CSF
     da Tarefa: TTF(f)        do Ruído: NPS(f)            E(f)
          |                         |                        |
          +-------------------------+------------------------+
                                    |
                                    v
                     +-----------------------------+
                     | ÍNDICE DE DETECTABILIDADE   |
                     |         d' (d-prime)        |
                     +-----------------------------+
```

## 1.4 Objetivos e Estrutura da Monografia

### 1.4.1 Objetivo Geral
Investigar, analisar criticamente e estruturar a evolução dos modelos perceptivos e matemáticos de avaliação de qualidade de imagem baseada em tarefas em Tomografia Computadorizada, partindo das formulações lineares clássicas até os observadores de aprendizado profundo contemporâneos e sua aplicação na otimização multiobjetivo de protocolos clínicos.

### 1.4.2 Objetivos Específicos
1. Formalizar a dedução matemática e a base física da Teoria de Detecção de Sinais aplicada à TC, demonstrando a transição do domínio espacial para o domínio das frequências ($TTF$, $NPS$, $E(f)$ e $d'$);
2. Descrever a trajetória dos observadores de modelo lineares ($IO$, $NPW$, $NPWE$, $HO$, $CHO$), explicitando as aproximações biológicas do córtex visual e os métodos psicofísicos de validação humana ($2AFC$, $MRMC$);
3. Analisar o colapso das premissas de linearidade e estacionariedade induzido pelas reconstruções não lineares ($IR$ e $DLR$), detalhando a necessidade de *phantoms* antropomórficos híbridos e técnicas de *detrending*;
4. Examinar a fronteira do conhecimento em Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO), sua calibração perceptual com radiologistas e sua generalização inter-scanners;
5. Propor a formulação de um espaço de Otimização Multiobjetivo tridimensional $(D, T, -W)$, integrando dose de radiação ($D$), tempo operacional ($T$) e desempenho diagnóstico ($W$) na tomada de decisão clínica.

---

# CAPÍTULO 2: FUNDAMENTOS TEÓRICOS E MATEMÁTICOS DA QUALIDADE BASEADA EM TAREFA

## 2.1 Teoria de Detecção de Sinais (SDT) e Tomada de Decisão Estatística

A Teoria de Detecção de Sinais ($SDT$), originada na engenharia de telecomunicações e radares na década de 1950, estabelece a base probabilística para a tomada de decisão sob incerteza estocástica. Em radiologia e física médica, a detecção de uma lesão pode ser formalizada como um teste de hipóteses binário sobre um vetor de imagem $\mathbf{g} \in \mathbb{R}^N$, formado por $N$ pixels ordenados lexicograficamente:

$$\begin{aligned}
H_0 &: \mathbf{g} = \mathbf{b} \quad & \text{(Hipótese Nula: Sinal Ausente / Apenas Fundo e Ruído)} \\
H_1 &: \mathbf{g} = \mathbf{b} + \mathbf{s} \quad & \text{(Hipótese Alternativa: Sinal Presente + Fundo e Ruído)}
\end{aligned}$$

onde $\mathbf{s} \in \mathbb{R}^N$ representa o vetor de sinal da lesão e $\mathbf{b} \in \mathbb{R}^N$ é o vetor estocástico que representa o ruído e a estrutura anatômica de fundo.

Um observador (seja ele humano ou um algoritmo matemático) atua aplicando um operador ou funcional $t(\mathbf{g}): \mathbb{R}^N \to \mathbb{R}$, mapeando a imagem multidimensional $\mathbf{g}$ em uma única variável escalar $t$, denominada **estatística de teste** (*scalar decision variable*).

A tomada de decisão clínica é realizada comparando $t$ com um limiar de decisão pré-estabelecido $t_c$:
- Se $t \ge t_c \implies$ o observador declara a hipótese $H_1$ (Sinal Presente);
- Se $t < t_c \implies$ o observador declara a hipótese $H_0$ (Sinal Ausente).

Sob condições repetidas de aquisição com ruído estocástico, a variável escalar $t$ assume distribuições de probabilidade condicionais: $p(t|H_0)$ e $p(t|H_1)$.

```
   Probabilidade p(t)
       ^
       |          p(t|H0)               p(t|H1)
       |        [Sinal Ausente]      [Sinal Presente]
       |             /\                   /\
       |            /  \                 /  \
       |           /    \               /    \
       |          /      \             /      \
       |         /        \     tc    /        \
       +--------/----------\----+----/----------\--------> Estatística de Teste (t)
                            <---d'--->
```

A separação entre essas distribuições governa as taxas fundamentais da curva de Característica de Operação do Receptor (*Receiver Operating Characteristic* - ROC):
- **Fração de Verdadeiros Positivos (Sensibilidade):**
  $$\text{TPF}(t_c) = \int_{t_c}^{\infty} p(t|H_1) \, dt$$
- **Fração de Falsos Positivos (1 - Especificidade):**
  $$\text{FPF}(t_c) = \int_{t_c}^{\infty} p(t|H_0) \, dt$$

## 2.2 O Índice de Detectabilidade ($d'$) no Domínio Espacial

Quando as distribuições condicionais $p(t|H_0)$ e $p(t|H_1)$ são gaussianas (ou aproximadamente gaussianas pelo Teorema Central do Limite para combinações lineares de muitos pixels), o desempenho do observador é totalmente parametrizado pela separação entre as médias normalizada pela variância combinada:

$$d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}$$

Para a classe de **observadores lineares**, a estatística de teste é dada pelo produto interno entre a imagem $\mathbf{g}$ e um vetor de template linear (filtro) $\mathbf{w} \in \mathbb{R}^N$:

$$t = \mathbf{w}^T \mathbf{g} = \sum_{i=1}^N w_i g_i$$

Substituindo $t = \mathbf{w}^T \mathbf{g}$ na definição estatística de $d'$, obtemos:
- Média sob $H_0$: $\langle t | H_0 \rangle = \mathbf{w}^T \langle \mathbf{b} \rangle$
- Média sob $H_1$: $\langle t | H_1 \rangle = \mathbf{w}^T (\langle \mathbf{b} \rangle + \mathbf{s}) = \mathbf{w}^T \langle \mathbf{b} \rangle + \mathbf{w}^T \mathbf{s}$
- Diferença entre médias: $\Delta \langle t \rangle = \mathbf{w}^T \mathbf{s}$
- Variância sob $H_0$ e $H_1$ (assumindo matriz de covariância de ruído estacionária $\mathbf{K}$):
  $$\sigma^2(t|H_0) = \sigma^2(t|H_1) = \mathbf{w}^T \mathbf{K} \mathbf{w}$$

Portanto, a formulação espacial do índice de detectabilidade para qualquer observador linear é:

$$d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}$$

onde $\mathbf{K} = \langle (\mathbf{g} - \langle \mathbf{g} \rangle)(\mathbf{g} - \langle \mathbf{g} \rangle)^T \rangle$ é a **Matriz de Autocovariância** do ruído ($N \times N$).

## 2.3 Caracterização no Domínio das Frequências: TTF, NPS e Filtro Ocular

A inversão explícita da matriz de covariância $\mathbf{K} \in \mathbb{R}^{N \times N}$ no domínio espacial é computacionalmente proibitiva para imagens clínicas (para uma ROI modesta de $128 \times 128$ pixels, $N = 16.384$ e $\mathbf{K}$ possui mais de $2,68 \times 10^8$ elementos). 

Sob a premissa de **sistemas lineares e invariantes no espaço** com ruído **estacionário no sentido amplo** (*Wide-Sense Stationary* - WSS), a matriz de covariância $\mathbf{K}$ é circulante e se diagonaliza através da Transformada de Fourier 2D. Isso permite transpor o cálculo de $d'$ integralmente para o domínio das frequências espaciais $(u, v)$ ou frequência radial $f = \sqrt{u^2 + v^2}$.

### 2.3.1 Função de Transferência da Tarefa ($TTF(f)$)

Em sistemas não lineares (como TC com reconstrução iterativa ou aprendizado profundo), a clássica $MTF$ não é invariante ao objeto. Para contornar essa não linearidade local, introduziu-se a **Função de Transferência da Tarefa** ($TTF(f)$), que mede a resolução espacial do sistema condicionada ao contraste e ao material específico da estrutura de interesse (SAMEI et al., 2019; GREFFIER et al., 2026).

A $TTF(f)$ é medida utilizando a técnica da borda circular (*circular edge technique*) em insertos cilíndricos de diferentes materiais inseridos em *phantoms* (ex.: insertos de Iodo para alto contraste, Polietileno, Delrin, Água/Solid Water® ou Teflon para baixo contraste):

1. Calcula-se o perfil radial de atenuação em torno do centro do inserto cilíndrico para obter a Função de Resposta ao Degrau Radial ($\text{ESF}(r)$);
2. Deriva-se a $\text{ESF}(r)$ para obter a Função de Espalhamento de Linha Radial ($\text{LSF}(r) = \frac{d}{dr}\text{ESF}(r)$);
3. Aplica-se a Transformada de Fourier 1D à $\text{LSF}(r)$ e normaliza-se para a frequência zero:
   $$TTF(f) = \frac{|\mathcal{F}\{\text{LSF}(r)\}|}{|\mathcal{F}\{\text{LSF}(r)\}|_{f=0}}$$

A métrica escalar $f_{50}$ (frequência espacial na qual a $TTF$ decai para 50% de sua amplitude máxima) é amplamente utilizada para quantificar e comparar a resolução efetiva entre protocolos.

### 2.3.2 Espectro de Potência do Ruído ($NPS(f)$)

O **Espectro de Potência do Ruído** ($NPS$) quantifica não apenas a variância pontual (magnitude), mas a distribuição da energia do ruído ao longo das frequências espaciais (textura e correlação):

$$NPS(u, v) = \frac{\Delta x \Delta y}{N_x N_y} \left\langle \left| \mathcal{F}_{2D} \left\{ I(x, y) - \overline{I}(x, y) \right\} \right|^2 \right\rangle$$

onde $\Delta x, \Delta y$ são os tamanhos físicos dos pixels, $N_x, N_y$ são as dimensões da sub-região de interesse (ROI) homogênea, e $\overline{I}(x, y)$ é o plano polinomial de baixa ordem subtraído para remover variações de baixa frequência (*detrending*).

A integral 2D do $NPS(u, v)$ reproduz exatamente a variância física do ruído no domínio espacial:

$$\sigma^2 = \iint_{-\infty}^{\infty} NPS(u, v) \, du \, dv$$

Para meios isotrópicos, calcula-se o $NPS$ radial 1D por média angular:

$$NPS(f) = \frac{1}{2\pi} \int_{0}^{2\pi} NPS(f \cos\theta, f \sin\theta) \, d\theta$$

A frequência de pico do ruído ($f_{\text{peak}}$) e a frequência média do ruído ($f_{\text{av}}$) fornecem descritores diretos da textura visual: curvas deslocadas para altas frequências correspondem a ruído fino/granular (típico de FBP com filtros duros), enquanto curvas concentradas em baixas frequências indicam ruído grosseiro, borrado ou ceroso (*plastic look* de reconstruções iterativas agressivas).

### 2.3.3 Filtro Ocular ($E(f)$) e a Função de Sensibilidade ao Contraste Humano

O sistema visual humano não possui resposta em frequência plana. A córnea, o cristalino, a retina e o córtex visual primário atuam em conjunto como um filtro passa-faixa, modelado pela **Função de Sensibilidade ao Contraste** (CSF) ou Filtro Ocular $E(f)$. 

Uma das formulações matemáticas mais consolidadas para $E(f)$ (BURGESS, 1994; ECKSTEIN et al., 2000; SAMEI et al., 2019) é dada por:

$$E(f) = \left( \frac{f}{f_0} \right)^n \exp\left[ -c \left( \frac{f}{f_0} \right)^m \right]$$

com parâmetros típicos ajustados experimentalmente para $f_0 \approx 0{,}8 \text{ ciclos/grau}$, $n = 1{,}3$, $m = 1{,}1$ e $c = 2{,}2$. Convertendo para a frequência na imagem em $\text{mm}^{-1}$ para uma distância típica de visualização diagnóstica $d_v$ (ex.: $500 \text{ mm}$):

$$f_{\text{retina}} (\text{ciclos/grau}) = \frac{\pi \cdot d_v}{180} \cdot f_{\text{imagem}} (\text{mm}^{-1})$$

O filtro ocular atenua severamente tanto frequências espaciais muito baixas (onde a visão humana não percebe contrastes amplos e suaves) quanto frequências muito altas (limitadas pela densidade foveal dos fotorreceptores e aberrações ópticas), apresentando pico de sensibilidade visual em torno de $3 \text{ a } 5 \text{ ciclos/grau}$.

### 2.3.4 Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$)

A tarefa diagnóstica clínica é parametrizada pelo sinal da lesão no domínio de Fourier. Para um nódulo ou lesão circular uniforme de raio $R$ e contraste central $\Delta C$:

$$\Delta S(r) = \begin{cases} \Delta C, & r \le R \\ 0, & r > R \end{cases}$$

Sua Transformada de Fourier 2D analítica resulta no perfil de Bessel de primeira ordem $J_1$:

$$W_{\text{task}}(f) = \left| \mathcal{F}_{2D}\{\Delta S(r)\} \right| = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|$$

Se o sinal for modulado pela resolução finita do tomógrafo, o espectro do sinal detectável na imagem é dado por:

$$S_{\text{imagem}}(f) = W_{\text{task}}(f) \cdot TTF(f)$$

## 2.4 Paradigmas de Detecção e a Metodologia Psicofísica 2AFC

A aplicação prática dos modelos exige a especificação do grau de conhecimento a priori do observador. Os principais paradigmas padronizados na literatura são:

1. **SKE / BKE (*Signal Known Exactly / Background Known Exactly*):** O observador conhece com precisão absoluta a posição, morfologia, tamanho, contraste e orientação da lesão, bem como o fundo exato. Este é o paradigma clássico que permite soluções analíticas rigorosas.
2. **SKS / BKS (*Signal Known Statistically / Background Known Statistically*):** A lesão e o fundo possuem incerteza espacial, variabilidade de forma ou localização desconhecida (tarefas de busca visual / *search tasks*).

Para validar experimentalmente os observadores matemáticos em relação à visão humana, o protocolo padrão-ouro da psicofísica é o experimento de **Escolha Forçada entre Duas Alternativas** (*Two-Alternative Forced Choice* - **2AFC**).

No 2AFC, apresentam-se simultaneamente ao leitor dois campos de imagem idênticos em tamanho e fundo: um contendo exclusivamente o ruído de fundo ($H_0$) e o outro contendo o sinal de interesse inserido sobre o fundo ($H_1$). O leitor deve indicar obrigatoriamente qual dos dois campos contém a lesão.

A fração de acertos observada ($P_C$, *Proportion Correct*) relaciona-se diretamente com o índice de detectabilidade experimental humano ($d'_{\text{humano}}$) através da função erro de Gauss:

$$P_C = \Phi\left( \frac{d'}{\sqrt{2}} \right) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{d'/\sqrt{2}} e^{-x^2/2} \, dx$$

Invertendo a equação:

$$d'_{\text{humano}} = \sqrt{2} \cdot \Phi^{-1}(P_C)$$

Essa correspondência direta permite calibrar e testar observadores computacionais contra painéis de médicos radiologistas com rigor metrológico absoluto.

---

# CAPÍTULO 3: A ERA DOS OBSERVADORES LINEARES

## 3.1 O Observador Ideal Bayesiano (IO) e o Limite Superior de Desempenho

O **Observador Ideal** (*Ideal Observer* - IO) é definido como o algoritmo de decisão que utiliza **toda** a informação estatística disponível na imagem para maximizar a área sob a curva ROC ($AUC$), de acordo com o Teorema de Neyman-Pearson.

A estatística de teste do Observador Ideal é a Razão de Verossimilhança (*Likelihood Ratio*) $\Lambda(\mathbf{g})$:

$$\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)}$$

Para ruído gaussiano multivariado com matriz de covariância comum $\mathbf{K}$, a estatística equivalente (log-verossimilhança) reduz-se a uma operação linear com template $\mathbf{w}_{\text{IO}} = \mathbf{K}^{-1} \mathbf{s}$:

$$t_{\text{IO}}(\mathbf{g}) = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g}$$

O índice de detectabilidade do Observador Ideal é dado pela distância de Mahalanobis:

$$d'_{\text{IO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}} = \left[ \iint \frac{|W_{\text{task}}(f) \cdot TTF(f)|^2}{NPS(f)} \, df_x \, df_y \right]^{1/2}$$

O Observador Ideal atua aplicando uma operação de **pré-branqueamento** (*prewhitening* $\mathbf{K}^{-1/2}$), descorrelacionando completamente a estrutura de frequências do ruído antes de aplicar o filtro casado (*matched filter*). Embora o IO estabeleça o limite físico e termodinâmico máximo de informação contida no feixe de raios X, ele **superestima grosseiramente** a percepção humana, pois os seres humanos são incapazes de realizar a inversão matemática perfeita de matrizes de covariância no córtex cerebral.

## 3.2 O Observador NPW e a Inclusão do Filtro Ocular (NPWE)

Para emular as limitações do processamento perceptual humano, foram introduzidos os observadores sem pré-branqueamento (*Non-Prewhitening* - NPW).

O observador **NPW** clássico assume que o sistema visual humano não descorrelaciona o ruído, aplicando apenas o template do sinal esperado como filtro casado: $\mathbf{w}_{\text{NPW}} = \mathbf{s}$.

No entanto, o NPW trata todas as frequências espaciais com o mesmo peso, falhando em modelar a perda de sensibilidade em frequências muito baixas e muito altas. A adição do filtro ocular $E(f)$ deu origem ao modelo **NPWE** (*Non-Prewhitening Observer with Eye Filter*), que se tornou o modelo padrão recomendado pelo relatório **AAPM TG-233** para controle e avaliação de qualidade em TC clínica (SAMEI et al., 2019; PIMENTA & COSTA, 2025).

A formulação analítica contínua do índice de detectabilidade para o modelo $NPWE$ é expressa por:

$$\boxed{d'_{\text{NPWE}} = \frac{\iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \, du \, dv}{\left\{ \iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^4 \cdot NPS(u, v) \, du \, dv \right\}^{1/2}}}$$

Em sistemas com simetria rotacional no plano axial, a integral 2D pode ser expressa em coordenadas polares radiais $f$:

$$d'_{\text{NPWE}} = \frac{\int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^2 \cdot 2\pi f \, df}{\left\{ \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^4 \cdot NPS(f) \cdot 2\pi f \, df \right\}^{1/2}}$$

O modelo NPWE tem excelente acurácia para prever o desempenho humano em fundos homogêneos e tarefas de detecção simples (SKE/BKE). Contudo, ele apresenta uma fraqueza fundamental: **não consegue lidar com fundos anatômicos complexos e estruturados**.

## 3.3 O Desafio dos Fundos Estruturados: Hotelling Observer (HO) e Channelized Hotelling Observer (CHO)

Quando a tarefa diagnóstica ocorre sobre anatomias realistas (ex.: parênquima pulmonar, trabeculado ósseo ou parênquima hepático), a imagem contém dois tipos distintos de variabilidade estocástica:
1. **Ruído Quântico/Eletrônico ($\mathbf{K}_{\text{ruído}}$):** Decorrente da fluência finita de fótons de raios X e do detector;
2. **Ruído Anatômico/Estrutural ($\mathbf{K}_{\text{anatômico}}$):** Decorrente da sobreposição de estruturas anatômicas complexas do próprio paciente.

A matriz de covariância total é a soma de ambas: $\mathbf{K}_{\text{total}} = \mathbf{K}_{\text{ruído}} + \mathbf{K}_{\text{anatômico}}$.

O **Observador de Hotelling** ($HO$) estende o formalismo linear para maximizar a razão de variâncias de classes em distribuições não gaussianas com fundos variáveis, empregando o template ótimo:

$$\mathbf{w}_{\text{HO}} = \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle$$

$$d'_{\text{HO}} = \sqrt{\langle \mathbf{s} \rangle^T \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle}$$

### O Observador de Hotelling Canalizado (CHO)
Estudos de neurofisiologia da visão (BARRETT et al., 1993; MYERS & BARRETT, 1987; YAO & BARRETT, 1992) demonstraram que os neurônios do córtex visual primário (área V1) realizam uma decomposição espectro-espacial da imagem através de campos receptivos seletivos a faixas de frequência espacial e orientação.

Para incorporar essa biologia e resolver o problema computacional da inversão da matriz $\mathbf{K}_{\text{total}}$, desenvolveu-se o **Channelized Hotelling Observer** ($CHO$). O CHO aplica uma matriz de canais $\mathbf{T} \in \mathbb{R}^{C \times N}$ (onde $C \ll N$, tipicamente $C \in [4, 10]$ canais), reduzindo o vetor de imagem $\mathbf{g}$ a um vetor de características canalizadas $\mathbf{v} \in \mathbb{R}^C$:

$$\mathbf{v} = \mathbf{T} \mathbf{g}$$

A matriz de covariância reduzida nos canais $\mathbf{K}_{\mathbf{v}} \in \mathbb{R}^{C \times C}$ é facilmente invertida:

$$\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K}_{\text{total}} \mathbf{T}^T$$

O índice de detectabilidade do CHO é expresso por:

$$d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}$$

onde $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \langle \mathbf{s} \rangle$.

```
   Imagem Médica (g)  ---> [ Matriz de Canais Corticais T ] ---> Vetor Canalizado v (C x 1)
   (N pixels, ex: 16384)       (Gabor / Laguerre-Gauss / DOG)           |
                                                                        v
   Estatística de Teste (t) <--- [ Filtro de Hotelling w = Kv^-1 <vs> ] <---+
```

Os principais modelos de canais utilizados na física médica são:
- **Canais de Gabor:** Funções sinusoidais moduladas por gaussianas com orientação angular, modelando a anisotropia do córtex visual;
- **Canais Laguerre-Gauss:** Polinômios ortogonais com simetria circular, eficientes para tarefas com simetria rotacional em SKE;
- **Canais de Diferença Densa de Gaussianas (*Dense Difference of Gaussians* - D-DOG):** Canais passa-faixa concêntricos isotrópicos que simulam com alta fidelidade a percepção psicofísica humana em fundos anatômicos.

## 3.4 Validação com Leitores Humanos: Estudos 2AFC e Metodologia MRMC

Para que um observador de modelo seja aceito como substituto (*surrogate*) metrológico do leitor humano, sua correlação com o desempenho de radiologistas deve ser validada quantitativamente.

As sessões de leitura humana são conduzidas por meio de protocolos $2AFC$ cegos, randomizados e com controle de luminância do monitor diagnóstico calibrado conforme o padrão DICOM Grayscale Standard Display Function (GSDF).

A análise estatística rigorosa da variabilidade inter-leitores e inter-casos exige a aplicação de modelos **MRMC** (*Multi-Reader Multi-Case*), fundamentados na metodologia de Dorfman-Berbaum-Metz (DBM) ou Obuchowski-Rockette-Hillis (ORH) (HILLIS et al., 2011). O coeficiente de correlação de Pearson ($r$) ou o Coeficiente de Correlação Intraclasse ($ICC$) entre $d'_{\text{modelo}}$ e $d'_{\text{humano}}$ deve atingir $r \ge 0{,}90$ para que o modelo seja considerado representativo da clínica.

---

# CAPÍTULO 4: O COLAPSO DA LINEARIDADE E OS SIMULADORES FÍSICOS MODERNOS

## 4.1 Evolução dos Algoritmos de Reconstrução: Da FBP às Reconstruções Iterativas e DLR

A evolução algorítmica da reconstrução tomográfica pode ser compreendida em quatro gerações sucessivas:

| Geração | Paradigma Algorítmico | Princípio de Funcionamento | Comportamento Físico |
| :--- | :--- | :--- | :--- |
| **1ª Geração** | Retroprojeção Filtrada (**FBP**) | Solução analítica da Transformada Inversa de Radon com convolução por filtro rampa (*ramp filter*). | Estritamente linear e invariante no espaço. Ruído gaussiano estacionário. |
| **2ª Geração** | Reconstrução Iterativa Estatística Híbrida (**HIR**) | Combinação de filtragem analítica com ciclos iterativos no domínio das projeções e da imagem (ex.: ASiR-V, AIDR 3D, iDose4, Safire). | Parcialmente não linear. Dependência de contraste moderada. |
| **3ª Geração** | Reconstrução Iterativa Baseada em Modelos (**MBIR**) | Otimização iterativa completa com modelagem detalhada da óptica dos fótons, tamanho do foco e estatística dos detectores (ex.: Veo, IMR, FIRST). | Fortemente não linear. Ruído altamente não-estacionário. Custo computacional elevado. |
| **4ª Geração** | Reconstrução por Aprendizado Profundo (**DLR**) | Redes Neurais Profundas treinadas com pares de sinogramas/imagens de baixa dose e alta dose de referência (FBP/MBIR) (ex.: TrueFidelity, AiCE, Precise Image, ClariCT.AI). | Altamente não linear. Redução massiva de ruído preservando resolução de bordas. |

## 4.2 A Quebra da Linearidade e a Não-Estacionariedade do Ruído

Nas reconstruções por aprendizado profundo ($DLR$) e iterativas ($MBIR$), a função que mapeia o sinograma de projeções $\mathbf{y}$ na imagem reconstruída $\mathbf{x}$ é não linear:

$$\mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}$$

As consequências físicas e metrológicas dessa não linearidade são profundas:

1. **Dependência do Sinal e Contraste:** A resolução espacial ($TTF$) varia ponto a ponto e deixa de ser uma propriedade puramente do tomógrafo: ela depende do tamanho, da morfologia e do contraste específico do objeto.
2. **Não-Estacionariedade Espacial do Ruído:** O ruído da imagem deixa de ser uniforme ao longo do campo de visão. Em torno de bordas anatômicas de alto contraste (ex.: osso/ar ou parênquima pulmonar/costela), o algoritmo $DLR$ preserva as altas frequências; em regiões homogêneas de tecidos moles, o algoritmo atua com agressiva suavização de ruído.
3. **O "Efeito Ceroso / Plástico" (*Plastic/Waxy Look*):** Reconstruções iterativas e algumas redes neurais profundas alteram drasticamente o espectro $NPS$, concentrando a energia em baixas frequências espaciais. Isso gera uma imagem sem o ruído granular clássico da FBP, mas com uma textura visualmente "artificial" que pode mascarar lesões de baixíssimo contraste (TOIA et al., 2023; GREFFIER et al., 2026).
4. **Colapso dos Modelos Lineares:** Como o modelo $NPWE$ integra o produto de $TTF$ e $NPS$ assumindo estacionariedade global, ele falha em capturar o impacto diagnóstico real do $DLR$, superestimando ou subestimando a capacidade real de detecção dos radiologistas.

## 4.3 A Transição dos *Phantoms*: De Geometrias Homogêneas a Simuladores Antropomórficos e Híbridos

Historicamente, o controle de qualidade em TC utilizava *phantoms* geométricos cilíndricos de acrílico ou água (como o *phantom* Catphan® ou os cilindros CTDI de PMMA). Embora excelentes para verificar calibração de números CT em HU, esses simuladores homogêneos são completamente inadequados para testar algoritmos $DLR$ e observadores computacionais em condições clinicamente representativas.

A física médica moderna realizou a transição para **Phantoms Antropomórficos e Híbridos**:

- **Phantoms Físicos Antropomórficos de Alta Fidelidade (ex.: FREDDIE):** Construídos com materiais equivalentes a tecidos biológicos humanos (tecido mole, osso trabecular, parênquima pulmonar esponjoso) fabricados por impressão 3D de alta precisão e densidades radiológicas calibradas.
- **Inserção Híbrida de Lesões Computacionais:** Para permitir milhares de repetições com verdade de campo (*ground truth*) absoluta sem destruir o *phantom*, adquirem-se imagens do *phantom* antropomórfico real em múltiplos níveis de dose e scanners. Em seguida, inserem-se computacionalmente modelos tridimensionais de lesões sintéticas com perfis de atenuação e bordas fisicamente convolvidas pela $PSF$ do sistema.

Essa abordagem híbrida permite gerar bancos de dados massivos de imagens com e sem sinal sobre fundos anatômicos pulmonares, abdominais e cranianos realistas.

```
   [ Aquisição Tomográfica do Phantom Antropomórfico Real (ex: Tórax) ]
                                |
                                v
               [ Banco de Imagens de Fundo Real (H0) ]
                                |
             +------------------+------------------+
             |                                     |
             v                                     v
   [ Casos Sem Lesão (H0) ]             [ Inserção de Lesão Sintética ]
                                        (Convolução com PSF do Scanner)
                                                   |
                                                   v
                                        [ Casos Com Lesão (H1) ]
                                                   |
             +-------------------------------------+
             v
   [ Teste Cego em Plataforma 2AFC: Leitores Humanos vs. Observadores de IA ]
```

## 4.4 Tratamento de Ruído em Fundos Complexos: *Detrending* e Quase-Estacionariedade

O cálculo do Espectro de Potência do Ruído ($NPS$) em fundos anatômicos antropomórficos exige a superação do gradiente de atenuação estrutural da própria anatomia. A aplicação direta da Transformada de Fourier 2D sobre uma ROI pulmonar resultaria em um $NPS$ dominado pela baixa frequência do gradiente anatômico, mascarando o ruído quântico e a textura algorítmica.

Para contornar essa limitação, aplica-se a hipótese de **Quase-Estacionariedade Local** aliada a algoritmos de **Detrending**:

1. Subdivide-se a região anatômica em um mosaico de pequenas ROIs locais (ex.: $64 \times 64$ ou $128 \times 128$ pixels);
2. Para cada ROI $I(x, y)$, ajusta-se uma superfície polinomial bidimensional de 2ª ordem $P_2(x, y)$ por mínimos quadrados:
   $$P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy$$
3. Subtrai-se a superfície polinomial para extrair exclusivamente as flutuações estocásticas de ruído:
   $$\delta I(x, y) = I(x, y) - P_2(x, y)$$
4. Calcula-se o $NPS$ sobre a matriz residual de ruído $\delta I(x, y)$ com janelamento espacial (Hanning/Hamming) para evitar vazamento espectral (*spectral leakage*).

Esse tratamento garante o rigor físico necessário para a alimentação de modelos observadores em anatomias complexas.

---

# CAPÍTULO 5: O ESTADO DA ARTE: OBSERVADORES DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO

## 5.1 Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO)

Diante do colapso dos modelos analíticos lineares ($NPWE$, $CHO$) em capturar as não linearidades e a não-estacionariedade do $DLR$, a fronteira da física médica orientou-se para o desenvolvimento de **Observadores de Modelo Baseados em Aprendizado Profundo** (*Deep Learning Model Observers* - DLMO).

Em vez de impor um template linear analítico pré-definido, o DLMO utiliza uma arquitetura de rede neural profunda parametrizada por pesos $\boldsymbol{\theta}$ para aprender diretamente a função não linear de mapeamento da imagem na estatística de teste:

$$t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$$

```
   Imagem de Entrada (g) ---> [ Camadas Convolucionais / Patches ]
                                             |
                                             v
                              [ Mecanismos de Auto-Atenção (Self-Attention) ]
                                             |
                                             v
                              [ Camadas Densas de Decisão ]
                                             |
                                             v
                                Estatística de Teste Escalar t
```

### Arquiteturas e Mecanismos de Atenção
Duas classes principais de arquiteturas dominam a literatura recente:
1. **Redes Neurais Convolucionais Profundas (CNNs Siamesas e ResNets):** Extraem mapas de características hierárquicas locais, preservando a equivariância translacional;
2. **Vision Transformers (ViT):** Utilizam mecanismos de auto-atenção (*self-attention*) para ponderar correlações espaciais globais e locais entre diferentes regiões da imagem, emulando os mecanismos cognitivos de atenção foveal e periférica do olho humano.

A estatística de teste gerada pela rede profunda sob conjuntos de teste independentes com sinal presente ($H_1$) e ausente ($H_0$) permite calcular o índice de detectabilidade empírico não linear:

$$d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}$$

## 5.2 Calibração Perceptual com Radiologistas e Transferibilidade Inter-Scanners

Para garantir a validade metrológica do DLMO, o modelo não deve ser treinado apenas para ser um classificador ótimo (o que o aproximaria de um Observador Ideal não linear), mas sim calibrado para **reproduzir a curva psicofísica de humanos**.

### Função de Perda Ancorada em Leituras Humanas
O treinamento do DLMO incorpora uma função de perda composta:

$$\mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{classificação}}(y, \hat{y}) + \lambda \, \mathcal{L}_{\text{perceptual}}(d'_{\text{DL}}, d'_{\text{humano}})$$

onde $\mathcal{L}_{\text{perceptual}} = \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2$ penaliza qualquer desvio entre o índice de detectabilidade previsto pelo modelo e o índice de detectabilidade medido no painel de radiologistas em estudos $2AFC$.

### Transferibilidade Inter-Scanners (*Leave-One-Scanner-Out*)
Um dos maiores desafios científicos é a capacidade de generalização do observador de IA. Um modelo treinado em dados de um tomógrafo GE não pode falhar ao avaliar imagens de tomógrafos Siemens, Philips ou Canon.

A metodologia de validação cruzada **Leave-One-Scanner-Out (LOSO)** é o padrão-ouro: treina-se o DLMO com dados de $N-1$ tomógrafos e testa-se sua acurácia no tomógrafo restante não visto pelo modelo. Mede-se assim a robustez da métrica e a eventual necessidade de estratégias de calibração por aprendizado por transferência (*transfer learning*).

## 5.3 Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional $(D, T, -W)$

A otimização de protocolos clínicos em física médica foi historicamente formulada como um problema bidimensional: minimizar a dose de radiação ($D$) sob a restrição de manter uma detectabilidade diagnóstica mínima aceitável ($W \ge W_{\text{limiar}}$).

No entanto, a prática hospitalar contemporânea impõe uma terceira restrição crítica frequentemente negligenciada: o **tempo operacional ($T$)**, que engloba tanto o **tempo de aquisição** do exame quanto o **tempo de reconstrução computacional**.

1. **Tempo de Aquisição ($T_{\text{aq}}$):** Condicionado pelo tempo de rotação do gantry e pelo *pitch* helicoidal. Em tomógrafos clínicos com tubos de raios X de potência limitada, a redução do tempo de rotação para minimizar artefatos de movimento respiratório ou cardíaco exige aumento proporcional da corrente do tubo (mA); ao atingir a potência máxima, o tomógrafo é forçado a reduzir a fluência de fótons por voxel, aumentando o ruído e degradando $d'$.
2. **Tempo de Reconstrução ($T_{\text{rec}}$):** Algoritmos iterativos densos ($MBIR$) e redes neurais profundas ($DLR$) de alta complexidade introduzem uma latência de processamento que pode variar de segundos a vários minutos por exame. Em ambientes de emergência e trauma (*pronto-socorro*), uma latência de reconstrução de 15 minutos é clinicamente inaceitável, mesmo que a imagem apresente excelente detectabilidade.

Assim, o problema de otimização em TC é rigorosamente formulado como um problema de **Otimização Multiobjetivo**:

$$\min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}$$

onde $\mathbf{p} = (\text{kVp}, \text{mA}, \text{tempo de rotação}, \text{pitch}, \text{algoritmo}, \text{filtro})$ é o vetor de parâmetros do protocolo, $D(\mathbf{p})$ é a dose de radiação ($\text{CTDI}_{\text{vol}}$ ou Dose Efetiva), $T(\mathbf{p}) = T_{\text{aq}} + T_{\text{rec}}$ é o tempo operacional total, e $W(\mathbf{p}) = d'(\mathbf{p})$ é a detectabilidade na tarefa diagnóstica.

```
       Dose (D)
          ^
          |      x (Protocolo Ineficiente / Dominado)
          |     /
          |    /  +--------------------------------+
          |   /   |  FRONTEIRA DE PARETO 3D        |
          |  /    |  Nenhum objetivo pode ser      |
          | v     |  melhorado sem degradar outro  |
          +-------+--------------------------------+---------> Tempo Operacional (T)
         /
        /
       v
   Detectabilidade (W = d')
```

Um protocolo $\mathbf{p}_1$ **domina no sentido de Pareto** outro protocolo $\mathbf{p}_2$ se e somente se:
$$\forall i \in \{D, T, -W\}, \, F_i(\mathbf{p}_1) \le F_i(\mathbf{p}_2) \quad \text{e} \quad \exists j \text{ tal que } F_j(\mathbf{p}_1) < F_j(\mathbf{p}_2)$$

O conjunto de todas as soluções não dominadas define a **Fronteira de Pareto Tridimensional**, permitindo que os físicos médicos e gestores clínicos selecionem o protocolo ótimo sob medida para cada cenário institucional (ex.: protocolo de ultrabaixa dose em pediatria, protocolo ultrarrápido em pronto-socorro ou protocolo de máxima detectabilidade em oncologia).

## 5.4 Novas Tecnologias: Tomografia por Contagem de Fótons (PCCT) e Imagens Monoenergéticas

A **Tomografia Computadorizada por Contagem de Fótons** (*Photon-Counting CT* - PCCT) representa o salto tecnológico mais recente na instrumentação tomográfica. Diferente dos detectores tradicionais integradores de energia (EICT), os detectores de semicondutores diretos (ex.: Telureto de Cádmio - CdTe / CZT) contam fótons individuais de raios X e os classificam em múltiplos canais de energia (*energy bins*).

A PCCT elimina o ruído eletrônico de leitura em baixas doses e permite a síntese de **Imagens Monoenergéticas Virtuais** (*Virtual Monoenergetic Images* - VMI) em níveis de energia selecionáveis (ex.: $40 \text{ a } 140 \text{ keV}$).

- Em baixas energias ($40 \text{ a } 50 \text{ keV}$), maximiza-se a absorção fotoelétrica do iodo, aumentando espetacularmente o contraste vascular e tumoral ($TTF$ e sinal);
- Em energias médias ($65 \text{ a } 75 \text{ keV}$), minimiza-se a variância relativa do ruído ($NPS$).

A incorporação de observadores de aprendizado profundo na análise de dados de PCCT abre a possibilidade de otimização automatizada do nível ótimo de keV para cada tarefa diagnóstica específica, consolidando a fronteira máxima da física médica tomográfica.

---

# CAPÍTULO 6: CONSIDERAÇÕES FINAIS E PERSPECTIVAS

## 6.1 Síntese da Trajetória Biofísica e Metrológica

A trajetória da avaliação da qualidade de imagem em tomografia computadorizada reflete uma evolução contínua da abstração matemática em direção à complexidade biofísica:

1. **A Fase Analítica Linear (1950 - 1990):** Partiu da física de telecomunicações e do Observador Ideal Bayesiano, introduzindo filtros oculares lineares ($NPWE$) para simular as limitações fisiológicas humanas em fundos uniformes.
2. **A Modelagem Cortical (1990 - 2015):** Desenvolveu o Observador de Hotelling Canalizado ($CHO$), incorporando canais de frequência inspirados na arquitetura do córtex visual primário para superar o ruído estrutural anatômico.
3. **A Ruptura da Linearidade (2015 - 2026):** A introdução clínica massiva de algoritmos não lineares de Reconstrução por Aprendizado Profundo ($DLR$) quebrou as premissas de invariância e estacionariedade, expondo o esgotamento dos modelos analíticos clássicos.
4. **O Paradigma da Inteligência Artificial Perceptual e Otimização Multiobjetivo (2026+):** O advento dos observadores baseados em redes profundas com mecanismos de atenção ($DLMO$), calibrados psicofisicamente contra leitores humanos e acoplados a espaços de otimização tridimensionais $(D, T, -W)$.

## 6.2 Impacto Clínico, Operacional e Normativo

A consolidação de observadores computacionais baseados em aprendizado profundo transcende o exercício acadêmico e produz impacto direto nas seguintes frentes:

- **Normatização e Aceitação de Sistemas:** Proporciona ferramentas metrológicas automatizadas que atendem às recomendações do relatório **AAPM TG-233** e da **IAEA** (como o sistema internacional de avaliação *5-star image quality*), permitindo que hospitais realizem o comissionamento de tomógrafos de forma padronizada.
- **Harmonização de Protocolos Inter-Institucionais:** Permite igualar o desempenho diagnóstico entre tomógrafos de diferentes gerações e fabricantes, eliminando a discrepância de qualidade no atendimento aos pacientes.
- **Segurança Radiológica Personalizada:** Viabiliza reduções drásticas de dose de radiação ionizante com garantia quantitativa de não degradação da detectabilidade clínica.

## 6.3 Articulação com a Pesquisa de Doutorado Direto

Esta monografia de conclusão de curso cumpre o papel de sistematizar a fundamentação teórica, metodológica e computacional que sustenta o projeto de pesquisa de Doutorado Direto do autor (FAPESP).

O arcabouço aqui construído articula-se organicamente com a linha de pesquisa do Grupo de Dosimetria e Radioproteção em Física Médica (GDRFM-IFUSP):
- **Fundação Experimental:** Ancorada nas aquisições tomográficas de *phantoms* híbridos em centros parceiros (InRad-HCFMUSP e Radboudumc);
- **Infraestrutura Linear de Baseline:** Integrada ao pipeline computacional automatizado de NPS, TTF e observadores lineares ($NPWE$, $CHO$) em desenvolvimento no projeto de mestrado do grupo;
- **Contribuição Inovadora do Doutorado:** Desenvolvimento, calibração psicofísica ($2AFC$ com $\ge 60$ radiologistas e análise MRMC), validação de transferibilidade inter-scanners ($7$ tomógrafos de $4$ fabricantes) e modelagem da Fronteira de Pareto $(D, T, -W)$ dos observadores de aprendizado profundo.

Dessa forma, o presente trabalho encerra a etapa de graduação estabelecendo as bases sólidas para a investigação experimental e computacional de ponta na física médica brasileira.

---

# REFERÊNCIAS BIBLIOGRÁFICAS

1. **ABBEY, C. K.; BARRETT, H. H.** Human- and model-observer performance in ramp-spectrum noise with regularization. *Journal of the Optical Society of America A*, v. 18, n. 3, p. 473-488, 2001.
2. **AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM).** *Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233*. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., *Medical Physics*, v. 46, n. 11, p. e735-e756, 2019).
3. **BARRETT, H. H.; MYERS, K. J.** *Foundations of Image Science*. Hoboken: John Wiley & Sons, 2004. 1540 p.
4. **BARRETT, H. H.; YAO, J.; ROLAND, P. X.; MYERS, K. J.** Model observers for assessment of image quality. *Physics in Medicine & Biology*, v. 38, n. 2, p. 277-295, 1993.
5. **BURGESS, A. E.** Statistically defined backgrounds: performance of a modified nonprewhitening observer model. *Journal of the Optical Society of America A*, v. 11, n. 4, p. 1237-1242, 1994.
6. **BURGESS, A. E.** Visual perception studies and observer models in medical imaging. *Seminars in Nuclear Medicine*, v. 41, n. 6, p. 419-436, 2011.
7. **CHOOPANI, R. et al.** Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. *Physics in Medicine & Biology*, v. 68, n. 14, p. 145002, 2023.
8. **ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P.** Role of knowledge in human visual search for signals in noise. *Journal of the Optical Society of America A*, v. 17, n. 11, p. 2064-2076, 2000.
9. **GREFFIER, J. et al.** Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. *Diagnostic and Interventional Imaging*, v. 107, n. 1, p. 1016-1025, 2026.
10. **HILLIS, S. L.; OB церковный, N. A.; BERBAUM, K. S.** Multi-reader multi-case ROC analysis: an updated review of methods and software. *Academic Radiology*, v. 18, n. 7, p. 842-856, 2011.
11. **INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA).** Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. *European Journal of Radiology*, v. 184, p. 113133, 2026.
12. **INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU).** *Medical Imaging - The Assessment of Image Quality*. ICRU Report 54. Bethesda, MD: ICRU, 1996.
13. **MCCOLLOUGH, C. H. et al.** Radiation dose in computed tomography: technological advances and clinical optimization over two decades. *Radiology*, v. 318, n. 2, p. e251200, 2026.
14. **MYERS, K. J.; BARRETT, H. H.** Addition of a channel mechanism to the ideal-observer model. *Journal of the Optical Society of America A*, v. 4, n. 12, p. 2447-2457, 1987.
15. **OOSTVEEN, L. J. et al.** Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. *European Radiology*, v. 31, p. 7412-7421, 2021.
16. **PIMENTA, E. F.; COSTA, P. R.** Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. *Medical Physics*, v. 52, n. 4, p. 2150-2165, 2025.
17. **PIMENTA, E. F.** *Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax*. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.
18. **RACINE, D. et al.** Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. *Physics in Medicine & Biology*, v. 65, n. 18, p. 185011, 2020.
19. **RACINE, D. et al.** Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. *Medical Physics*, v. 48, n. 6, p. 2890-2901, 2021.
20. **SCHILDER, C. M. et al.** Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. *La Rivista del Nuovo Cimento*, v. 49, n. 3, p. 145-210, 2026.
21. **TOIA, G. V. et al.** Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. *European Radiology*, v. 33, p. 4310-4322, 2023.
22. **WAGNER, R. F.; BROWN, D. G.; METZ, C. E.** Application of information theory to the assessment of computed tomography. *Medical Physics*, v. 6, n. 2, p. 83-94, 1979.
23. **YAO, J.; BARRETT, H. H.** Predicting human performance by a channelized Hotelling observer model. In: *SPIE Medical Imaging: Image Perception*, v. 1654, p. 268-278, 1992.
24. **ZHOU, W. et al.** Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. *IEEE Transactions on Medical Imaging*, v. 40, n. 9, p. 2350-2362, 2021.
"""

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print(f"Successfully wrote {len(content)} characters to {target_path}")
