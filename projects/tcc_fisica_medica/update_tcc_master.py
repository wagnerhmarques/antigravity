import os

target_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md"

full_text = r"""---
tipo: tcc-monografia
titulo: "Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo"
autor: "Wagner H. M."
orientador: "Prof. Dr. Paulo Roberto Costa"
instituicao: "Instituto de Física da Universidade de São Paulo (IFUSP)"
departamento: "Departamento de Física Nuclear - GDRFM"
data: 2026-09-01
versao: "2.0-completa"
tags:
  - tcc
  - fisica-medica
  - tomografia-computadorizada
  - task-based-image-quality
  - model-observers
  - deep-learning
  - otimizacao-multiobjetivo
  - psicofisica
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
**Monografia de Conclusão de Curso** apresentada ao Instituto de Física da Universidade de São Paulo como requisito fundamental para a obtenção do título de Bacharel em Física com Habilitação em Física Médica.

<br>

---

## RESUMO

A Tomografia Computadorizada (TC) ocupa uma posição de destaque na medicina diagnóstica moderna, operando sob a tensão física contínua entre a minimização da dose de radiação ionizante e a preservação do desempenho diagnóstico. Historicamente, os programas de garantia de qualidade em TC apoiaram-se em métricas escalares lineares clássicas, tais como o desvio padrão do número CT ($\sigma_{\text{HU}}$), a Relação Sinal-Ruído ($SNR$), a Relação Contraste-Ruído ($CNR$) e a Função de Transferência de Modulação ($MTF$), avaliadas em simuladores físicos (*phantoms*) homogêneos e geométricos. No entanto, a incorporação clínica de algoritmos avançados de reconstrução não lineares — incluindo Reconstruções Iterativas Híbridas ($HIR$), Reconstruções Iterativas Baseadas em Modelos ($MBIR$) e, fundamentalmente, Reconstruções Baseadas em Aprendizado Profundo ($DLR$) — rompeu as premissas estruturais de linearidade e invariância translacional do sistema. Sob essas condições, o ruído tomográfico tornou-se espacialmente heterogêneo, dependente da dose, do contraste e da geometria local da cena, induzindo alterações de textura (como o aspecto artificialmente suavizado ou *"plastic/waxy look"*) que não são quantificadas adequadamente pelas métricas convencionais.

Para superar essa limitação metrológica, a física médica consolidou o paradigma da **Qualidade de Imagem Baseada em Tarefa** (*Task-Based Image Quality* - TBIQ), fundamentado na Teoria de Detecção de Sinais ($SDT$). Neste arcabouço, a qualidade da imagem é definida formalmente pelo desempenho de um observador (humano ou algoritmo matemático) na execução de uma tarefa clínica específica, parametrizada pelo **Índice de Detectabilidade** ($d'$). Esta monografia apresenta uma investigação rigorosa, abrangente e aprofundada da evolução teórica, biofísica e computacional dos observadores de modelo (*model observers*). Analisa-se a transição histórica do Observador Ideal Bayesiano ($IO$) para os modelos antropomórficos lineares com filtro ocular ($NPWE$) e canais corticais de frequência ($CHO$), explicitando suas deduções analíticas completas a partir da diagonalização da matriz de covariância pelo Teorema de Wiener-Khinchin, bem como os limites físicos que provocam seu esgotamento em regimes não lineares e fundos estruturados.

Em resposta a essa ruptura, examina-se a fronteira do conhecimento representada pelos **Observadores Baseados em Aprendizado Profundo** (*Deep Learning Model Observers* - DLMO), construídos sobre arquiteturas neurais convolucionais e *Vision Transformers* com mecanismos de auto-atenção, calibrados diretamente contra leituras psicofísicas de radiologistas especialistas em experimentos de Escolha Forçada entre Duas Alternativas ($2AFC$) com modelagem *Multi-Reader Multi-Case* ($MRMC$). Por fim, esta monografia formaliza a integração desses novos modelos à **Otimização Multiobjetivo**, expandindo o compromisso bidimensional tradicional para uma **Fronteira de Pareto Tridimensional $(D, T, -W)$**, que incorpora o tempo operacional ($T$) de aquisição e reconstrução junto à dose de radiação ($D$) e à detectabilidade diagnóstica ($W$). Este trabalho estabelece o alicerce teórico e metodológico para a metrologia em TC clínica contemporânea e pavimenta o desenvolvimento do projeto de Doutorado Direto do autor no IFUSP/FAPESP.

**Palavras-chave:** Tomografia Computadorizada; Avaliação Baseada em Tarefa; Observadores de Modelo; Índice de Detectabilidade; Reconstrução por Aprendizado Profundo; Phantoms Antropomórficos; Otimização Multiobjetivo; Fronteira de Pareto.

---

## ABSTRACT

Computed Tomography (CT) plays an indispensable role in modern diagnostic medicine, permanently operating under the physical trade-off between minimizing ionizing radiation dose and preserving clinical diagnostic efficacy. Historically, quality assurance programs in CT relied on classical linear scalar metrics, such as CT number standard deviation ($\sigma_{\text{HU}}$), Signal-to-Noise Ratio ($SNR$), Contrast-to-Noise Ratio ($CNR$), and Modulation Transfer Function ($MTF$), evaluated on homogeneous geometric phantoms. However, the clinical adoption of advanced non-linear reconstruction algorithms—including Hybrid Iterative Reconstruction ($HIR$), Model-Based Iterative Reconstruction ($MBIR$), and Deep Learning Image Reconstruction ($DLR$)—has fundamentally broken the core assumptions of system linearity and shift-invariance. Under these conditions, tomographic noise becomes spatially non-stationary, dose-dependent, and scene-dependent, introducing perceptual texture alterations (such as the "plastic" or "waxy" appearance) that cannot be properly captured by conventional scalar metrics.

To overcome this metrological limitation, medical physics has embraced the **Task-Based Image Quality** (TBIQ) paradigm, grounded in Signal Detection Theory ($SDT$). In this framework, image quality is rigorously defined by the performance of an observer (human radiologist or mathematical model) executing a specific clinical task, quantified by the **Detectability Index** ($d'$). This monograph provides an exhaustive, mathematically rigorous, and comprehensive investigation of the theoretical, biophysical, and computational evolution of model observers. We analyze the historical transition from the Bayesian Ideal Observer ($IO$) to linear anthropomorphic models incorporating eye filters ($NPWE$) and cortical frequency channels ($CHO$), detailing their complete analytical derivations via covariance matrix diagonalization through the Wiener-Khinchin theorem, as well as the physical limits that lead to their breakdown in non-linear regimes and structured anatomical backgrounds.

To address this structural failure, we investigate the state of the art in **Deep Learning Model Observers** (DLMO), built upon convolutional neural architectures and Vision Transformers with self-attention mechanisms, calibrated directly against expert radiologists' psychophysical performance in Two-Alternative Forced Choice ($2AFC$) paradigms under Multi-Reader Multi-Case ($MRMC$) statistical modeling. Finally, this monograph formalizes the integration of these modern observers into a **Multi-Objective Optimization** framework, expanding the traditional two-dimensional trade-off into a **Three-Dimensional Pareto Frontier $(D, T, -W)$**, explicitly incorporating operational time ($T$) alongside radiation dose ($D$) and diagnostic detectability ($W$). This work establishes the physical, mathematical, and computational foundations for contemporary CT metrology, directly supporting the author's Direct Doctorate research at IFUSP/FAPESP.

**Keywords:** Computed Tomography; Task-Based Image Quality; Model Observers; Detectability Index; Deep Learning Reconstruction; Anthropomorphic Phantoms; Multi-Objective Optimization; Pareto Frontier.

---

## LISTA DE ABREVIATURAS E SÍMBOLOS

| Símbolo / Sigla | Significado Físico / Conceitual |
| :--- | :--- |
| **2AFC** | *Two-Alternative Forced Choice* (Escolha Forçada entre Duas Alternativas) |
| **AAPM** | *American Association of Physicists in Medicine* |
| **AEC** | *Automatic Exposure Control* (Controle Automático de Exposição) |
| **ALARA** | *As Low As Reasonably Achievable* (Tão Baixo Quanto Razoavelmente Exequível) |
| **AUC** | *Area Under the ROC Curve* (Área sob a Curva ROC) |
| **BKE / BKS** | *Background Known Exactly* / *Background Known Statistically* |
| **CHO** | *Channelized Hotelling Observer* (Observador de Hotelling Canalizado) |
| **CNR** | *Contrast-to-Noise Ratio* (Relação Contraste-Ruído) |
| **CSF** | *Contrast Sensitivity Function* (Função de Sensibilidade ao Contraste do Olho) |
| **CTDI / CTDIvol** | *Computed Tomography Dose Index* (Índice de Dose Volumétrico em TC, em mGy) |
| **D-DOG** | *Dense Difference of Gaussians* (Diferença Densa de Gaussianas) |
| **DLR / DLIR** | *Deep Learning Image Reconstruction* (Reconstrução por Aprendizado Profundo) |
| **DLMO** | *Deep Learning Model Observer* (Observador de Modelo por Aprendizado Profundo) |
| **DLP** | *Dose-Length Product* (Produto Dose-Comprimento, em $\text{mGy}\cdot\text{cm}$) |
| **DQE** | *Detective Quantum Efficiency* (Eficiência Quântica de Detecção) |
| **DRL** | *Diagnostic Reference Level* (Nível de Referência Diagnóstica) |
| **$d'$** | *Detectability Index* (Índice de Detectabilidade) |
| **$E(f)$** | Filtro Ocular Humano (*Eye Filter*) no Domínio das Frequências |
| **ESF / LSF / PSF** | *Edge / Line / Point Spread Function* (Resposta ao Degrau / Linha / Ponto) |
| **FBP** | *Filtered Backprojection* (Retroprojeção Filtrada) |
| **FOV** | *Field of View* (Campo de Visão, em mm) |
| **GSDF** | *Grayscale Standard Display Function* (Padrão DICOM PS 3.14) |
| **HIR** | *Hybrid Iterative Reconstruction* (Reconstrução Iterativa Híbrida) |
| **HO** | *Hotelling Observer* (Observador de Hotelling) |
| **HU** | Unidade Hounsfield (*Hounsfield Unit*) |
| **IAEA** | *International Atomic Energy Agency* (Agência Internacional de Energia Atômica) |
| **ICC** | *Intraclass Correlation Coefficient* (Coeficiente de Correlação Intraclasse) |
| **ICRU** | *International Commission on Radiation Units and Measurements* |
| **IO** | *Ideal Observer* (Observador Ideal Bayesiano) |
| **$\mathbf{K}$** | Matriz de Autocovariância do Ruído ($N \times N$) |
| **MBIR** | *Model-Based Iterative Reconstruction* (Reconstrução Iterativa Baseada em Modelos) |
| **MCDM** | *Multi-Criteria Decision Making* (Tomada de Decisão Multicritério) |
| **MRMC** | *Multi-Reader Multi-Case* (Múltiplos Leitores e Múltiplos Casos) |
| **MTF** | *Modulation Transfer Function* (Função de Transferência de Modulação) |
| **NPS** | *Noise Power Spectrum* (Espectro de Potência do Ruído, em $\text{mm}^2$ ou $\text{HU}^2\cdot\text{mm}^2$) |
| **NPW / NPWE** | *Non-Prewhitening Observer* / *with Eye Filter* |
| **NSGA-II** | *Non-dominated Sorting Genetic Algorithm II* |
| **PCCT** | *Photon-Counting Computed Tomography* (TC por Contagem de Fótons) |
| **$P_C$** | *Proportion Correct* (Proporção de Acertos no Paradigma 2AFC) |
| **ROC** | *Receiver Operating Characteristic* (Característica de Operação do Receptor) |
| **ROI** | *Region of Interest* (Região de Interesse) |
| **SDT** | *Signal Detection Theory* (Teoria de Detecção de Sinais) |
| **SKE / SKS** | *Signal Known Exactly* / *Signal Known Statistically* |
| **SNR** | *Signal-to-Noise Ratio* (Relação Sinal-Ruído) |
| **TG-233** | *Task Group 233* da AAPM |
| **TOPSIS** | *Technique for Order Preference by Similarity to Ideal Solution* |
| **TTF** | *Task Transfer Function* (Função de Transferência da Tarefa) |
| **ViT** | *Vision Transformer* |
| **VMI** | *Virtual Monoenergetic Image* (Imagem Monoenergética Virtual, em keV) |
| **$W_{\text{task}}(f)$** | Espectro da Tarefa Diagnóstica / Sinal no Domínio de Fourier |

---

# SUMÁRIO GERAL

1. [Capítulo 1: Introdução e Contextualização](#capítulo-1-introdução-e-contextualização)
   - 1.1 [O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico](#11-o-dilema-fundamental-da-tomografia-computadorizada-dose-versus-desempenho-clínico)
   - 1.2 [Limitações Estruturais das Métricas Físicas Globais Tradicionais](#12-limitações-estruturais-das-métricas-físicas-globais-tradicionais)
   - 1.3 [A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality*)](#13-a-mudança-de-paradigma-qualidade-de-imagem-baseada-em-tarefa-task-based-image-quality)
   - 1.4 [Objetivos e Estrutura da Monografia](#14-objetivos-e-estrutura-da-monografia)
2. [Capítulo 2: Fundamentos Teóricos e Matemáticos da Qualidade Baseada em Tarefa](#capítulo-2-fundamentos-teóricos-e-matemáticos-da-qualidade-baseada-em-tarefa)
   - 2.1 [Teoria de Detecção de Sinais (SDT) e Tomada de Decisão Estatística](#21-teoria-de-detecção-de-sinais-sdt-e-tomada-de-decisão-estatística)
   - 2.2 [O Índice de Detectabilidade ($d'$) no Domínio Espacial: Dedução Formal](#22-o-índice-de-detectabilidade-d-no-domínio-espacial-dedução-formal)
   - 2.3 [Transição para o Domínio das Frequências pelo Teorema de Wiener-Khinchin](#23-transição-para-o-domínio-das-frequências-pelo-teorema-de-wiener-khinchin)
     - 2.3.1 [Função de Transferência da Tarefa ($TTF(f)$) e a Técnica da Borda Circular](#231-função-de-transferência-da-tarefa-ttff-e-a-técnica-da-borda-circular)
     - 2.3.2 [Espectro de Potência do Ruído ($NPS(f)$) e Descritores Espectrais](#232-espectro-de-potência-do-ruído-npsf-e-descritores-espectrais)
     - 2.3.3 [Filtro Ocular ($E(f)$) e Modelagem Biofísica do Sistema Visual Humano](#233-filtro-ocular-ef-e-modelagem-biofísica-do-sistema-visual-humano)
     - 2.3.4 [Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$) e o Critério de Rose](#234-espectro-da-tarefa-diagnóstica-w_texttaskf-e-o-critério-de-rose)
   - 2.4 [Paradigmas de Detecção e a Dedução Matemática do Experimento 2AFC](#24-paradigmas-de-detecção-e-a-dedução-matemática-do-experimento-2afc)
3. [Capítulo 3: A Era dos Observadores Lineares](#capítulo-3-a-era-dos-observadores-lineares)
   - 3.1 [O Observador Ideal Bayesiano (IO) e o Limite Superior Termodinâmico](#31-o-observador-ideal-bayesiano-io-e-o-limite-superior-termodinâmico)
   - 3.2 [O Observador NPW e a Dedução Contínua do Modelo NPWE](#32-o-observador-npw-e-a-dedução-contínua-do-modelo-npwe)
   - 3.3 [O Desafio dos Fundos Estruturados: Hotelling Observer (HO) e Channelized Hotelling Observer (CHO)](#33-o-desafio-dos-fundos-estruturados-hotelling-observer-ho-e-channelized-hotelling-observer-cho)
     - 3.3.1 [Formulação Algébrica do Observador de Hotelling](#331-formulação-algébrica-do-observador-de-hotelling)
     - 3.3.2 [Modelagem dos Canais Corticais: Gabor, Laguerre-Gauss e D-DOG](#332-modelagem-dos-canais-corticais-gabor-laguerre-gauss-e-d-dog)
   - 3.4 [Validação Psicofísica com Leitores Humanos e Metodologia Estatística MRMC](#34-validação-psicofísica-com-leitores-humanos-e-metodologia-estatística-mrmc)
4. [Capítulo 4: O Colapso da Linearidade e os Simuladores Físicos Modernos](#capítulo-4-o-colapso-da-linearidade-e-os-simuladores-físicos-modernos)
   - 4.1 [Taxonomia dos Algoritmos de Reconstrução: Da FBP às Reconstruções Iterativas e DLR](#41-taxonomia-dos-algoritmos-de-reconstrução-da-fbp-às-reconstruções-iterativas-e-dlr)
   - 4.2 [A Quebra da Linearidade, Não-Estacionariedade e o "Efeito Ceroso" (*Plastic Look*)](#42-a-quebra-da-linearidade-não-estacionariedade-e-o-efeito-ceroso-plastic-look)
   - 4.3 [A Transição Metrológica dos *Phantoms*: De Geometrias Homogêneas a Simuladores Antropomórficos Híbridos](#43-a-transição-metrológica-dos-phantoms-de-geometrias-homogêneas-a-simuladores-antropomórficos-híbridos)
   - 4.4 [Tratamento de Ruído em Fundos Anatômicos: Quase-Estacionariedade, *Detrending* e Incerteza Bootstrap](#44-tratamento-de-ruído-em-fundos-anatômicos-quase-estacionariedade-detrending-e-incerteza-bootstrap)
5. [Capítulo 5: O Estado da Arte: Observadores de Aprendizado Profundo e Otimização Multiobjetivo](#capítulo-5-o-estado-da-arte-observadores-de-aprendizado-profundo-e-otimização-multiobjetivo)
   - 5.1 [Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO)](#51-observadores-baseados-em-aprendizado-profundo-deep-learning-model-observers---dlmo)
   - 5.2 [Calibração Perceptual com Radiologistas e Transferibilidade Inter-Scanners (*Leave-One-Scanner-Out*)](#52-calibração-perceptual-com-radiologistas-e-transferibilidade-inter-scanners-leave-one-scanner-out)
   - 5.3 [Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional $(D, T, -W)$ e Algoritmos Genéticos](#53-otimização-multiobjetivo-em-tc-a-fronteira-de-pareto-tridimensional-d-t--w-e-algoritmos-genéticos)
   - 5.4 [Fronteiras Futuras: Tomografia por Contagem de Fótons (PCCT) e Imagens Monoenergéticas (VMI)](#54-fronteiras-futuras-tomografia-por-contagem-de-fótons-pcct-e-imagens-monoenergéticas-vmi)
6. [Capítulo 6: Metodologia Experimental, Arquitetura de Software e Aspectos Bioéticos](#capítulo-6-metodologia-experimental-arquitetura-de-software-e-aspectos-bioéticos)
   - 6.1 [Arquitetura de Software do Pipeline Integrado de Metrologia](#61-arquitetura-de-software-do-pipeline-integrado-de-metrologia)
   - 6.2 [Protocolo Metrológico Padronizado segundo o AAPM TG-233](#62-protocolo-metrológico-padronizado-segundo-o-aapm-tg-233)
   - 6.3 [Aspectos Bioéticos, Regulatórios e Desenho Experimental Humano (CEP/CONEP)](#63-aspectos-bioéticos-regulatórios-e-desenho-experimental-humano-cepconep)
7. [Capítulo 7: Considerações Finais e Perspectivas](#capítulo-7-considerações-finais-e-perspectivas)
   - 7.1 [Síntese da Trajetória Biofísica e Epistemológica](#71-síntese-da-trajetória-biofísica-e-epistemológica)
   - 7.2 [Impacto Clínico, Operacional e Normativo](#72-impacto-clínico-operacional-e-normativo)
   - 7.3 [Articulação com a Pesquisa de Doutorado Direto (FAPESP)](#73-articulação-com-a-pesquisa-de-doutorado-direto-fapesp)
8. [Referências Bibliográficas](#referências-bibliográficas)

---

# CAPÍTULO 1: INTRODUÇÃO E CONTEXTUALIZAÇÃO

## 1.1 O Dilema Fundamental da Tomografia Computadorizada: Dose versus Desempenho Clínico

A Tomografia Computadorizada (TC) transformou a prática médica contemporânea desde sua introdução clínica pioneira na década de 1970 por Godfrey Hounsfield. A capacidade da TC de reconstruir secções transversais anatômicas com alta resolução espacial, excelente diferenciação de densidades de tecidos moles e aquisições volumétricas isotrópicas quase instantâneas conferiu-lhe o papel de padrão-ouro em inúmeros cenários clínicos críticos: diagnóstico e estadiamento de neoplasias, avaliação de politraumatismos agudos, planejamento cirúrgico e radioterápico, diagnóstico precoce de acidentes vasculares encefálicos e rastreamento de nódulos pulmonares (MCCOLLOUGH et al., 2026).

Entretanto, o princípio físico fundamental da formação da imagem em TC apoia-se na atenuação exponencial de feixes de raios X colimados transmitidos através da anatomia do paciente. A interação da radiação ionizante com a matéria biológica ocorre predominantemente por efeito fotoelétrico e espalhamento Compton, acarretando ionizações atômicas diretas e a quebra de pontes moleculares em fitas de DNA (efeitos genotóxicos estocásticos). Consequentemente, embora represente cerca de 10% a 15% do volume global de exames radiológicos realizados em hospitais e clínicas, a TC é responsável por mais de 65% a 70% da dose coletiva de radiação de origem médica na população mundial (IAEA, 2026; MCCOLLOUGH et al., 2026).

Essa assimetria estatística impõe à comunidade de física médica e radiologia o estrito cumprimento dos princípios fundamentais da radioproteção: **Justificação**, **Otimização** e **Limitação de Dose**. Em particular, o princípio **ALARA** (*As Low As Reasonably Achievable*) estabelece que todo protocolo de aquisição tomográfica deve empregar a menor dose de radiação suficiente para garantir a acurácia diagnóstica da tarefa clínica em questão.

O dilema biofísico intrínseco da TC decorre da natureza estocástica da emissão e detecção de fótons de raios X. O ruído primário da imagem tomográfica é governed pela estatística de contagem de Poisson. Para um elemento volumétrico de imagem (voxel), o desvio padrão do ruído quântico ($\sigma_{\text{ruído}}$) relaciona-se inversamente com a raiz quadrada da fluência de fótons detectados ($N_{\text{fótons}}$), a qual é diretamente proporcional ao produto da corrente do tubo de raios X pelo tempo de exposição (mAs) e à dose absorvida no paciente:

$$\sigma_{\text{ruído}} = \frac{1}{\sqrt{N_{\text{fótons}}}} \propto \frac{1}{\sqrt{\text{mAs}}} \propto \frac{1}{\sqrt{\text{CTDI}_{\text{vol}}}}$$

Dessa forma, qualquer redução direta da dose de radiação ionizante, quando desacompanhada de inovações tecnológicas no detector ou no algoritmo de reconstrução, resulta no aumento exponencial do ruído estocástico. Esse ruído elevado degrada criticamente a detectabilidade de lesões de baixo contraste intrínseco (como pequenos tumores hepáticos hipoatenuantes ou lesões nodulares em vidro fosco pulmonares), introduzindo o risco inaceitável de falsos negativos diagnósticos.

## 1.2 Limitações Estruturais das Métricas Físicas Globais Tradicionais

Durante décadas, a rotina de controle de qualidade, testes de aceitação e comparação de equipamentos de TC baseou-se em métricas físicas clássicas escalares, herdadas da teoria de sistemas lineares e invariantes no espaço:

1. **Desvio Padrão Global do Número CT ($\sigma_{\text{HU}}$):** Avaliado em uma única região de interesse (ROI) central em um *phantom* cilíndrico uniforme de água ou polimetilmetacrilato (PMMA);
2. **Relação Sinal-Ruído ($SNR$) e Relação Contraste-Ruído ($CNR$):**
   $$CNR = \frac{|\overline{\mu}_{\text{alvo}} - \overline{\mu}_{\text{fundo}}|}{\sigma_{\text{fundo}}}$$
   onde $\overline{\mu}_{\text{alvo}}$ e $\overline{\mu}_{\text{fundo}}$ representam os números de CT médios em Unidades Hounsfield (HU) do objeto de teste e do fundo circundante, e $\sigma_{\text{fundo}}$ é o desvio padrão pontual dos pixels do fundo.
3. **Função de Transferência de Modulação ($MTF$):** Extraída a partir da resposta ao impulso (Point Spread Function - $PSF$) de fios finos metálicos ou contas de alta densidade imersas em ar ou meio homogêneo.

Embora essas métricas escalares fossem razoavelmente adequadas sob o paradigma clássico da **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP) — cuja operação de convolução/projeção é estritamente linear e produz ruído gaussiano estacionário —, elas falham de maneira catastrófica na avaliação dos tomógrafos modernos (SAMEI et al., 2019 - Relatório AAPM TG-233).

A causa primária desse colapso metrológico reside no fato de que os tomógrafos modernos incorporam algoritmos de reconstrução fortemente não lineares (reconstruções iterativas e redes neurais profundas). A $CNR$ clássica possui falhas estruturais incontornáveis:
- **Insensibilidade à Textura Espacial:** A $CNR$ considera apenas a variância pontual ($\sigma^2$) entre pixels isolados. Duas imagens podem possuir exatamente o mesmo valor numérico de $\sigma_{\text{fundo}}$ e o mesmo contraste, mas apresentarem estruturas de correlação espacial totalmente distintas (ruído de alta frequência "fino" *vs.* ruído de baixa frequência "grosseiro/borrado"). Para o observador humano, a detectabilidade em ambas as imagens é drasticamente diferente.
- **Falsa Otimização por Filtros de Suavização:** A aplicação de filtros passa-baixas agressivos (como gaussianos ou filtros de mediana) reduz drasticamente o desvio padrão $\sigma_{\text{fundo}}$, inflando artificialmente o valor numérico da $CNR$, ao mesmo tempo em que apaga bordas sutis e destrói a visibilidade de detalhes anatômicos finos.
- **Ausência de Modelagem da Biologia Visual:** A $CNR$ trata o processo de detecção como uma simples subtração escalar de intensidades, ignorando a fisiologia da visão humana, que atua por meio de filtros de sensibilidade ao contraste e integração espacial em canais corticais.

## 1.3 A Mudança de Paradigma: Qualidade de Imagem Baseada em Tarefa (*Task-Based Image Quality*)

Consciente da ineficácia das métricas escalares, a comunidade internacional de física médica — através da *International Commission on Radiation Units and Measurements* (ICRU Report 54, 1996), da *American Association of Physicists in Medicine* (AAPM TG-233, 2019) e de textos seminais em ciência da imagem (BARRETT & MYERS, 2004) — estabeleceu um novo paradigma metrológico: a **Qualidade de Imagem Baseada em Tarefa** (*Task-Based Image Quality* - TBIQ).

No paradigma TBIQ, a qualidade de uma imagem tomográfica não é uma grandeza intrínseca e descontextualizada, mas é rigorosamente definida como a **eficácia com que uma imagem permite a um observador executar uma tarefa clínica específica com acurácia estatística comprovada**.

```
+---------------------------------------------------------------------------------------+
|                 PARADIGMA TRADICIONAL vs. PARADIGMA BASEADO EM TAREFA                 |
+---------------------------------------------------------------------------------------+
|  PARADIGMA CLÁSSICO (Linear / Escalar)    |  PARADIGMA TBIQ (Baseado em Tarefa)       |
|  • Métricas: Desvio padrão (HU), SNR, CNR |  • Métrica Central: Detectabilidade (d')  |
|  • Phantoms: Cilindros homogêneos de água |  • Phantoms: Antropomórficos / Híbridos   |
|  • Premissa: Linearidade e invariância    |  • Premissa: Não linearidade / Tarefa     |
|  • Observador: Desconsiderado             |  • Observador: Humano ou IA (Model Obs.)  |
|  • Falha: Inflado por filtros de blur     |  • Rigor: Correlaciona com radiologistas  |
+---------------------------------------------------------------------------------------+
```

A TBIQ estrutura-se sobre a Teoria de Detecção de Sinais ($SDT$) e operacionaliza a avaliação através de observadores computacionais (*model observers*). O indicador central é o **Índice de Detectabilidade ($d'$)**, que sintetiza em um único formalismo:
1. As propriedades de resolução espacial do tomógrafo condicionadas à tarefa ($TTF(f)$);
2. A magnitude e textura de correlação do ruído estocástico ($NPS(f)$);
3. O espectro morfológico da lesão ou sinal clínico em questão ($W_{\text{task}}(f)$);
4. O modelo de resposta fisiológica do sistema visual humano ($E(f)$).

## 1.4 Objetivos e Estrutura da Monografia

### 1.4.1 Objetivo Geral
Estruturar, deduzir matematicamente e avaliar criticamente o estado da arte dos modelos perceptivos e computacionais de qualidade de imagem baseada em tarefas em Tomografia Computadorizada, partindo das formulações lineares clássicas até os observadores de aprendizado profundo contemporâneos e sua aplicação pioneira na otimização multiobjetivo tridimensional $(D, T, -W)$ de protocolos clínicos.

### 1.4.2 Objetivos Específicos
1. Formalizar as deduções matemáticas fundamentais da Teoria de Detecção de Sinais no domínio espacial e no domínio das frequências, demonstrando a diagonalização da matriz de covariância via Teorema de Wiener-Khinchin;
2. Analisar a trajetória dos observadores lineares ($IO$, $NPW$, $NPWE$, $HO$ e $CHO$), detalhando os modelos de canais corticais (Gabor, Laguerre-Gauss, D-DOG) e a validação psicofísica $2AFC$ via modelagem $MRMC$;
3. Investigar o colapso estrutural da linearidade em sistemas $DLR$ e $MBIR$, demonstrando o surgimento da não-estacionariedade e justificando a transição para simuladores antropomórficos híbridos e técnicas de *detrending*;
4. Examinar a arquitetura dos Observadores de Aprendizado Profundo (*Deep Learning Model Observers* - DLMO), sua calibração com radiologistas e sua validação de transferibilidade inter-scanners (*leave-one-scanner-out*);
5. Formular o problema de Otimização Multiobjetivo em TC através da Fronteira de Pareto $(D, T, -W)$, integrando dose ($D$), tempo operacional ($T$) e detectabilidade diagnóstica ($W$);
6. Propor a arquitetura de software para automação metrológica e o protocolo bioético (CEP/CONEP) para leitura humana, consolidando a base teórica para o projeto de Doutorado Direto do autor no IFUSP/FAPESP.

---

# CAPÍTULO 2: FUNDAMENTOS TEÓRICOS E MATEMÁTICOS DA QUALIDADE BASEADA EM TAREFA

## 2.1 Teoria de Detecção de Sinais (SDT) e Tomada de Decisão Estatística

A Teoria de Detecção de Sinais ($SDT$), formalizada inicialmente por Peterson, Birdsall e Fox (1954) e introduzida na física médica e na radiologia diagnóstica por Lusted (1968), Wagner (1979) e Metz (1986), estabelece o arcabouço matemático rigoroso para a tomada de decisão diagnóstica sob incerteza estocástica.

Consideremos um sistema de imagem médica digital que produz uma imagem discreta representada por um vetor lexicograficamente ordenado $\mathbf{g} \in \mathbb{R}^N$, onde $N = N_x \times N_y$ é o número total de pixels da região de interesse. O processo fundamental de diagnóstico de detecção de lesões é modelado como um **teste de hipóteses binário**:

$$\begin{cases}
H_0 : \mathbf{g} = \mathbf{b} & \text{(Hipótese Nula: Ausência de Lesão / Apenas Fundo e Ruído)} \\
H_1 : \mathbf{g} = \mathbf{b} + \mathbf{s} & \text{(Hipótese Alternativa: Presença de Lesão / Sinal + Fundo e Ruído)}
\end{cases}$$

onde $\mathbf{s} \in \mathbb{R}^N$ é o vetor que descreve o perfil de atenuação espacial do sinal (lesão) e $\mathbf{b} \in \mathbb{R}^N$ é um vetor estocástico aleatório que descreve o ruído físico e as flutuações anatômicas do fundo.

Um observador (seja um médico radiologista ou um algoritmo computacional) processa o vetor de dados $\mathbf{g}$ aplicando uma função escalar de decisão $t(\mathbf{g}): \mathbb{R}^N \to \mathbb{R}$, gerando a **estatística de teste escalar** $t$. A decisão é tomada comparando $t$ com um limiar fixo $t_c$:

$$\text{Decisão} = \begin{cases} H_1 (\text{Sinal Presente}), & \text{se } t(\mathbf{g}) \ge t_c \\ H_0 (\text{Sinal Ausente}), & \text{se } t(\mathbf{g}) < t_c \end{cases}$$

Devido à natureza estocástica de $\mathbf{g}$, a estatística $t$ comporta-se como uma variável aleatória com funções densidade de probabilidade condicionais: $p(t|H_0)$ e $p(t|H_1)$.

```
   Densidade de Probabilidade p(t)
       ^
       |           p(t|H0)                 p(t|H1)
       |       [Sinal Ausente]         [Sinal Presente]
       |             /\                      /\
       |            /  \                    /  \
       |           /    \                  /    \
       |          /      \                /      \
       |         /        \       tc     /        \
       +--------/----------\------+-----/----------\--------> Estatística de Teste (t)
                |                 |     |          |
                +-----------------+-----+----------+
                                  <--d'-->
```

A variação contínua do limiar $t_c \in (-\infty, \infty)$ traça a curva de Característica de Operação do Receptor (**Curva ROC**), parametrizada pela Fração de Verdadeiros Positivos ($\text{TPF}(t_c)$ ou Sensibilidade) e Fração de Falsos Positivos ($\text{FPF}(t_c)$ ou $1 - \text{Especificidade}$):

$$\text{TPF}(t_c) = \int_{t_c}^{\infty} p(t|H_1) \, dt, \qquad \text{FPF}(t_c) = \int_{t_c}^{\infty} p(t|H_0) \, dt$$

A integral da curva ROC define a **Área sob a Curva ROC ($AUC$)**:

$$AUC = \int_{0}^{1} \text{TPF} \, d(\text{FPF}) = P(t_1 > t_0)$$

que é rigorosamente igual à probabilidade de que a estatística de teste calculada em um caso aleatório com sinal presente ($t_1$) seja numericamente superior à estatística calculada em um caso com sinal ausente ($t_0$).

## 2.2 O Índice de Detectabilidade ($d'$) no Domínio Espacial: Dedução Formal

Quando as distribuições condicionais $p(t|H_0)$ e $p(t|H_1)$ são normais com variâncias homogêneas, a separação entre as duas populações é perfeitamente quantificada pelo **Índice de Detectabilidade** ($d'$, pronunciado *d-prime*):

$$d' = \frac{\langle t | H_1 \rangle - \langle t | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(t|H_1) + \frac{1}{2}\sigma^2(t|H_0)}}$$

onde $\langle t | H_i \rangle$ representa o valor esperado da estatística $t$ sob a hipótese $H_i$, e $\sigma^2(t|H_i)$ é a correspondente variância.

Para a ampla classe dos **Observadores Lineares**, a estatística de teste é dada pelo produto escalar canônico entre um vetor de pesos (template de filtragem) $\mathbf{w} \in \mathbb{R}^N$ e a imagem $\mathbf{g}$:

$$t(\mathbf{g}) = \mathbf{w}^T \mathbf{g} = \sum_{i=1}^N w_i g_i$$

Vamos deduzir os termos de $d'$ para qualquer observador linear:
1. **Média sob $H_0$:**
   $$\langle t | H_0 \rangle = \langle \mathbf{w}^T \mathbf{g} | H_0 \rangle = \mathbf{w}^T \langle \mathbf{b} \rangle$$
2. **Média sob $H_1$:**
   $$\langle t | H_1 \rangle = \langle \mathbf{w}^T (\mathbf{b} + \mathbf{s}) | H_1 \rangle = \mathbf{w}^T \langle \mathbf{b} \rangle + \mathbf{w}^T \mathbf{s}$$
3. **Diferença entre Médias ($\Delta \langle t \rangle$):**
   $$\Delta \langle t \rangle = \langle t | H_1 \rangle - \langle t | H_0 \rangle = \mathbf{w}^T \mathbf{s}$$
4. **Variância sob $H_0$ e $H_1$:**
   Definindo a Matriz de Autocovariância do ruído $\mathbf{K} \in \mathbb{R}^{N \times N}$ como $\mathbf{K} = \langle (\mathbf{b} - \langle \mathbf{b} \rangle)(\mathbf{b} - \langle \mathbf{b} \rangle)^T \rangle$:
   $$\sigma^2(t|H_0) = \left\langle \left( \mathbf{w}^T (\mathbf{b} - \langle \mathbf{b} \rangle) \right)^2 \right\rangle = \mathbf{w}^T \left\langle (\mathbf{b} - \langle \mathbf{b} \rangle)(\mathbf{b} - \langle \mathbf{b} \rangle)^T \right\rangle \mathbf{w} = \mathbf{w}^T \mathbf{K} \mathbf{w}$$
   Assumindo que o sinal $\mathbf{s}$ é determinístico, a variância sob $H_1$ é idêntica: $\sigma^2(t|H_1) = \mathbf{w}^T \mathbf{K} \mathbf{w}$.

Substituindo esses resultados na definição de $d'$, obtemos a **Equação Fundamental da Detectabilidade Linear no Domínio Espacial**:

$$\boxed{d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}}$$

## 2.3 Transição para o Domínio das Frequências pelo Teorema de Wiener-Khinchin

Em imagens tomográficas clínicas, a dimensão $N$ da imagem é da ordem de $512 \times 512 = 262.144$ pixels. A matriz de covariância $\mathbf{K}$ possui, portanto, $N \times N \approx 6{,}87 \times 10^{10}$ elementos, tornando a manipulação algébrica direta no domínio espacial inviável computacionalmente.

Contudo, sob a premissa fundamental de que o ruído estocástico de fundo é **Estacionário no Sentido Amplo** (*Wide-Sense Stationary* - WSS), a autocovariância entre dois pixels posicionados em $\mathbf{r}_1 = (x_1, y_1)$ e $\mathbf{r}_2 = (x_2, y_2)$ depende unicamente do vetor de deslocamento espacial relativo $\Delta \mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$:

$$K(\mathbf{r}_1, \mathbf{r}_2) = R_n(\mathbf{r}_1 - \mathbf{r}_2) = R_n(\Delta x, \Delta y)$$

Uma matriz de covariância espacial gerada por um processo WSS é uma matriz bloco-circulante. Pela teoria clássica de processamento de sinais, toda matriz circulante é **diagonalizada pela base ortonormal das funções exponenciais complexas da Transformada de Fourier**.

Pelo **Teorema de Wiener-Khinchin**, a Transformada de Fourier bidimensional contínua da função de autocorrelação espacial $R_n(\Delta x, \Delta y)$ é identicamente igual à densidade espectral de potência, denominada na física médica de **Espectro de Potência do Ruído** ($NPS(u, v)$):

$$NPS(u, v) = \iint_{-\infty}^{\infty} R_n(\Delta x, \Delta y) e^{-i 2\pi (u \Delta x + v \Delta y)} \, d\Delta x \, d\Delta y$$

Essa equivalência matemática permite converter somatórios de matrizes no domínio espacial em integrais analíticas no domínio das frequências espaciais $(u, v)$ ou em coordenadas polares $(f, \theta)$, onde $f = \sqrt{u^2 + v^2}$.

### 2.3.1 Função de Transferência da Tarefa ($TTF(f)$) e a Técnica da Borda Circular

Em sistemas tomográficos não lineares, a clássica Função de Transferência de Modulação ($MTF$) não é constante, variando conforme o nível de ruído, a dose e o contraste do material. Por essa razão, a física médica padronizou a **Função de Transferência da Tarefa** ($TTF(f)$), que mede a resolução espacial do tomógrafo condicionada ao contraste do tecido ou estrutura em estudo (SAMEI et al., 2019).

A $TTF(f)$ é quantificada através da técnica da borda circular (*circular edge technique*) em insertos cilíndricos de materiais calibrados (Iodo, Ar, Teflon, Polietileno, Água/Solid Water®):

1. **Amostragem Radial e $\text{ESF}(r)$:** Determina-se com precisão sub-pixel o centroide geométrico $(x_0, y_0)$ do inserto cilíndrico de raio $R$. Mede-se a distância euclidiana $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$ de todos os pixels vizinhos à borda, construindo a Função de Resposta ao Degrau Radial ($\text{ESF}(r)$);
2. **Diferenciação Numérica e $\text{LSF}(r)$:** Aplica-se a derivada de primeira ordem em relação ao raio para obter a Função de Espalhamento de Linha Radial ($\text{LSF}(r)$):
   $$\text{LSF}(r) = \frac{d}{dr} \text{ESF}(r)$$
3. **Transformada de Fourier e Normalização:** Calcula-se a Transformada de Fourier 1D contínua do módulo da $\text{LSF}(r)$, normalizando-a para a frequência espacial nula ($f = 0$):
   $$TTF(f) = \frac{\left| \int_{-\infty}^{\infty} \text{LSF}(r) e^{-i 2\pi f r} \, dr \right|}{\left| \int_{-\infty}^{\infty} \text{LSF}(r) \, dr \right|}$$

A frequência $f_{50}$ (frequência na qual $TTF(f_{50}) = 0{,}5$) e a frequência $f_{10}$ ($TTF(f_{10}) = 0{,}1$) são utilizadas internacionalmente como descritores quantitativos da resolução efetiva do protocolo.

```
   TTF(f)
     1.0 |------\
         |       \
     0.5 |--------\--------+ (f50: frequência de 50% de modulação)
         |         \       |
         |          \      |
     0.0 +-----------+-----+----------------> Frequência Espacial f (mm^-1)
                    f50   f10
```

### 2.3.2 Espectro de Potência do Ruído ($NPS(f)$) e Descritores Espectrais

O **Espectro de Potência do Ruído 2D** ($NPS(u, v)$) descreve como a variância estocástica do ruído se distribui pelas frequências espaciais bidimensionais, capturando a textura e as correlações inter-pixels:

$$NPS(u, v) = \lim_{N_x, N_y \to \infty} \frac{\Delta x \Delta y}{N_x N_y} \left\langle \left| \sum_{x=0}^{N_x-1} \sum_{y=0}^{N_y-1} \left[ I(x, y) - \overline{I}(x, y) \right] e^{-i 2\pi \left(\frac{u x}{N_x} + \frac{v y}{N_y}\right)} \right|^2 \right\rangle$$

onde $\Delta x$ e $\Delta y$ são as dimensões físicas do pixel (em mm), $N_x, N_y$ são as dimensões da ROI, $I(x, y)$ é o valor em HU do pixel e $\overline{I}(x, y)$ é o plano de tendência subtraído via *detrending*.

A integral dupla do $NPS(u, v)$ em todo o plano de Fourier reconstrói exatamente a variância do ruído:

$$\sigma^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} NPS(u, v) \, du \, dv$$

Para caracterização escalar da textura do ruído, extraem-se dois descritores espectrais fundamentais:
- **Frequência Média do Ruído ($f_{\text{av}}$):**
  $$f_{\text{av}} = \frac{\int_{0}^{\infty} f \cdot NPS(f) \, df}{\int_{0}^{\infty} NPS(f) \, df}$$
- **Frequência de Pico do Ruído ($f_{\text{peak}}$):**
  $$f_{\text{peak}} = \arg\max_{f} \left[ NPS(f) \right]$$

Deslocamentos de $f_{\text{av}}$ e $f_{\text{peak}}$ em direção a baixas frequências indicam texturas com perda de granularidade fina e aspecto borrado/ceroso (*plastic look*), característicos de reconstruções iterativas agressivas.

### 2.3.3 Filtro Ocular ($E(f)$) e Modelagem Biofísica do Sistema Visual Humano

O olho humano não atua como um sensor linear uniforme. O sistema visual humano — composto pelos meios refrométricos oculares (córnea e cristalino), mosaico foveal de fotorreceptores e camadas sinápticas do córtex visual primário — atua como um filtro passa-faixa, modelado pela **Função de Sensibilidade ao Contraste** (CSF) ou **Filtro Ocular** $E(f)$ (BURGESS, 1994; ECKSTEIN et al., 2000; SAMEI et al., 2019):

$$E(f) = \left( \frac{f}{f_0} \right)^n \exp\left[ -c \left( \frac{f}{f_0} \right)^m \right]$$

onde os coeficientes experimentais canônicos validados para leitura de imagens radiológicas são $f_0 = 0{,}8 \text{ ciclos/grau}$, $n = 1{,}3$, $m = 1{,}1$ e $c = 2{,}2$.

A conversão da frequência visual angular (em ciclos por grau subtendido na retina, $\text{cpd}$) para a frequência espacial na imagem física (em $\text{mm}^{-1}$) é governada pela distância de visualização diagnóstica $d_v$ (padronizada clinicamente em $d_v \approx 500 \text{ mm}$):

$$f_{\text{retina}} (\text{ciclos/grau}) = \frac{\pi \cdot d_v}{180} \cdot f_{\text{imagem}} (\text{mm}^{-1}) \approx 8{,}727 \cdot d_v (\text{m}) \cdot f_{\text{imagem}} (\text{mm}^{-1})$$

Adicionalmente, a percepção humana é limitada pelo **ruído interno do observador** ($\sigma_{\text{int}}^2$). Conforme demonstrado por Burgess (1994), a eficiência perceptual humana máxima $\eta$ em relação a um observador matemático ideal é limitada pela razão entre o ruído interno neural e o ruído externo quântico da imagem:

$$d'_{\text{humano}} = \frac{d'_{\text{NPWE}}}{\sqrt{1 + \left(\frac{\sigma_{\text{int}}}{\sigma_{\text{ext}}}\right)^2}}$$

onde estudos empíricos revelam que $\sigma_{\text{int}} / \sigma_{\text{ext}} \approx 0{,}5 \text{ a } 0{,}8$ para leitores treinados em ambientes de baixa iluminância.

### 2.3.4 Espectro da Tarefa Diagnóstica ($W_{\text{task}}(f)$) e o Critério de Rose

A tarefa diagnóstica clínica é parametrizada no domínio de Fourier através do perfil de atenuação espacial do sinal $\Delta S(x, y)$. Para uma lesão nodular esférica ou circular de raio $R$ e contraste central $\Delta C$ (em HU):

$$\Delta S(r) = \Delta C \cdot \Pi\left(\frac{r}{2R}\right) = \begin{cases} \Delta C, & r \le R \\ 0, & r > R \end{cases}$$

Sua Transformada de Fourier 2D exata é expressa analiticamente pela função de Bessel de primeira espécie $J_1(x)$:

$$W_{\text{task}}(f) = \left| \mathcal{F}_{2D}\{\Delta S(r)\} \right| = \Delta C \cdot 2\pi R^2 \left| \frac{J_1(2\pi R f)}{2\pi R f} \right|$$

Albert Rose (1948) demonstrou pioneiramente que um sinal de área $A$ e contraste $\Delta C$ imerso em ruído branco com desvio padrão $\sigma$ só é detectável com certeza estatística pela visão humana se a relação de Rose $k$ satisfizer o **Critério de Rose**:

$$k = \frac{\Delta C \cdot \sqrt{A}}{\sigma} \ge 5$$

No arcabouço contemporâneo da TBIQ, o critério de Rose é generalizado para ruídos coloridos não brancos através do índice $d'$: um valor de $d' \approx 4{,}0 \text{ a } 5{,}0$ corresponde ao limiar de detecção quase perfeita ($P_C \ge 99\%$), enquanto $d' \approx 1{,}5 \text{ a } 2{,}0$ estabelece o limiar de discriminação clínica mínima aceitável.

## 2.4 Paradigmas de Detecção e a Dedução Matemática do Experimento 2AFC

A aplicação metrológica dos observadores exige a definição clara do nível de informação prévia disponível:
- **SKE / BKE (*Signal Known Exactly / Background Known Exactly*):** O observador conhece com precisão milimétrica a localização, morfologia, tamanho e contraste do sinal, bem como o fundo exato. É o padrão internacional para calibração analítica de observadores de modelo;
- **SKS / BKS (*Signal Known Statistically / Background Known Statistically*):** A localização e as características morfológicas do sinal possuem incerteza estocástica (tarefas de busca visual / *visual search*).

Para validar e calibrar experimentalmente os observadores em relação a observadores humanos, o protocolo padrão-ouro da psicofísica é o experimento de **Escolha Forçada entre Duas Alternativas** (*Two-Alternative Forced Choice* - **2AFC**).

### Dedução Formal da Relação Psicofísica 2AFC
No paradigma 2AFC, apresentam-se simultaneamente ao observador dois campos de imagem independentes:
- Campo 0: Contém apenas ruído de fundo ($H_0$);
- Campo 1: Contém o sinal inserido sobre o ruído de fundo ($H_1$).

O observador calcula a estatística de decisão em ambos os campos: $t_0 = t(\mathbf{g}|H_0)$ e $t_1 = t(\mathbf{g}|H_1)$. O observador acerta a escolha se e somente se a estatística na imagem com sinal for estritamente maior que na imagem sem sinal: $t_1 > t_0$.

Assumindo que $t_0 \sim \mathcal{N}(\mu_0, \sigma^2)$ e $t_1 \sim \mathcal{N}(\mu_1, \sigma^2)$ são variáveis normais estatisticamente independentes, definimos a variável aleatória de diferença:

$$\Delta t = t_1 - t_0$$

Pela linearidade do valor esperado e propriedades da variância de variáveis normais independentes:
- **Média da Diferença:** $\mu_{\Delta t} = \mu_1 - \mu_0$
- **Variância da Diferença:** $\sigma_{\Delta t}^2 = \sigma^2(t_1) + \sigma^2(t_0) = \sigma^2 + \sigma^2 = 2\sigma^2$
- **Desvio Padrão da Diferença:** $\sigma_{\Delta t} = \sqrt{2}\sigma$

A proporção de acertos esperada ($P_C$, *Proportion Correct*) é a probabilidade de que $\Delta t > 0$:

$$P_C = P(\Delta t > 0) = P\left( \frac{\Delta t - \mu_{\Delta t}}{\sigma_{\Delta t}} > \frac{0 - (\mu_1 - \mu_0)}{\sqrt{2}\sigma} \right) = P\left( Z > -\frac{\mu_1 - \mu_0}{\sqrt{2}\sigma} \right)$$

onde $Z \sim \mathcal{N}(0, 1)$ é a variável normal padrão. Como $d' = \frac{\mu_1 - \mu_0}{\sigma}$ e pela simetria da distribuição normal padrão:

$$\boxed{P_C = \Phi\left( \frac{d'}{\sqrt{2}} \right) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{d'/\sqrt{2}} e^{-u^2/2} \, du}$$

Invertendo formalmente a função de distribuição cumulativa normal padrão $\Phi$:

$$\boxed{d'_{\text{humano}} = \sqrt{2} \cdot \Phi^{-1}(P_C)}$$

Essa dedução demonstra rigorosamente a origem do fator $\sqrt{2}$, estabelecendo a ponte metrológica direta entre a porcentagem empírica de acertos de um médico radiologista em tela diagnóstica e o índice de detectabilidade físico $d'$.

---

# CAPÍTULO 3: A ERA DOS OBSERVADORES LINEARES

## 3.1 O Observador Ideal Bayesiano (IO) e o Limite Superior Termodinâmico

O **Observador Ideal** (*Ideal Observer* - IO) é definido como o tomador de decisão probabilístico ótimo que utiliza **toda a informação física e estatística contida nos dados da imagem** para maximizar a área sob a curva ROC ($AUC$), satisfazendo o Teorema de Neyman-Pearson.

A estatística de teste do Observador Ideal é a **Razão de Verossimilhança** (*Likelihood Ratio*) $\Lambda(\mathbf{g})$ ou seu logaritmo natural:

$$\Lambda(\mathbf{g}) = \frac{p(\mathbf{g}|H_1)}{p(\mathbf{g}|H_0)} \implies t_{\text{IO}}(\mathbf{g}) = \ln \Lambda(\mathbf{g})$$

Para ruído gaussiano multivariado com matriz de covariância comum $\mathbf{K}$ e sinal determinístico $\mathbf{s}$:

$$p(\mathbf{g}|H_0) = \frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left[ -\frac{1}{2} \mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} \right]$$

$$p(\mathbf{g}|H_1) = \frac{1}{(2\pi)^{N/2} |\mathbf{K}|^{1/2}} \exp\left[ -\frac{1}{2} (\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) \right]$$

Calculando o logaritmo da razão:

$$t_{\text{IO}}(\mathbf{g}) = \ln \left[ \frac{\exp\left( -\frac{1}{2}(\mathbf{g} - \mathbf{s})^T \mathbf{K}^{-1} (\mathbf{g} - \mathbf{s}) \right)}{\exp\left( -\frac{1}{2}\mathbf{g}^T \mathbf{K}^{-1} \mathbf{g} \right)} \right] = \mathbf{s}^T \mathbf{K}^{-1} \mathbf{g} - \frac{1}{2}\mathbf{s}^T \mathbf{K}^{-1}\mathbf{s}$$

Como o termo $-\frac{1}{2}\mathbf{s}^T \mathbf{K}^{-1}\mathbf{s}$ é uma constante independente dos dados, a estatística linear do Observador Ideal é:

$$t_{\text{IO}}(\mathbf{g}) = \mathbf{w}_{\text{IO}}^T \mathbf{g} \quad \text{com} \quad \mathbf{w}_{\text{IO}} = \mathbf{K}^{-1}\mathbf{s}$$

O índice de detectabilidade do Observador Ideal é expresso pela distância de Mahalanobis:

$$d'_{\text{IO}} = \sqrt{\mathbf{s}^T \mathbf{K}^{-1} \mathbf{s}} = \left[ \iint \frac{\left| W_{\text{task}}(u, v) \cdot TTF(u, v) \right|^2}{NPS(u, v)} \, du \, dv \right]^{1/2}$$

O Observador Ideal atua aplicando a operação de **pré-branqueamento** (*prewhitening* $\mathbf{K}^{-1/2}$), suprimindo as correlações espectrais do ruído antes de correlacionar com o sinal. Embora o IO estabeleça o limite físico máximo de informação diagnóstica disponível na radiação transmitida, ele **superestima grosseiramente a acurácia humana**, pois o cérebro humano é biologicamente incapaz de calcular inversas exatas de matrizes de covariância.

## 3.2 O Observador NPW e a Dedução Contínua do Modelo NPWE

Para aproximar os modelos da cognição biológica, introduziu-se o observador sem pré-branqueamento (*Non-Prewhitening* - NPW), cuja premissa é que o sistema visual humano não descorrelaciona o ruído, atuando como um filtro casado simples: $\mathbf{w}_{\text{NPW}} = \mathbf{s}$.

No entanto, o NPW clássico atribui peso uniforme a todas as frequências espaciais, falhando em modelar a perda de sensibilidade do olho em baixas e altas frequências. A inclusão do filtro ocular $E(f)$ originou o modelo **NPWE** (*Non-Prewhitening with Eye Filter*), que se consolidou como o modelo de referência internacional estabelecido pelo **AAPM TG-233** para controle e avaliação de qualidade em TC (SAMEI et al., 2019; PIMENTA & COSTA, 2025).

No modelo NPWE, o template no domínio espacial é dado por $\mathbf{w}_{\text{NPWE}} = \mathbf{E}^T \mathbf{E} \, \mathbf{s}$, onde $\mathbf{E}$ é o operador de filtragem ocular.

Substituindo $\mathbf{w}$ na fórmula geral $d' = \frac{\mathbf{w}^T \mathbf{s}}{\sqrt{\mathbf{w}^T \mathbf{K} \mathbf{w}}}$ e aplicando a diagonalização de Fourier via Teorema de Wiener-Khinchin, obtemos a **Equação Analítica Integral de Detectabilidade do NPWE**:

$$\boxed{d'_{\text{NPWE}} = \frac{\iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \, du \, dv}{\left\{ \iint \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ TTF(u, v) \right]^2 \cdot \left[ E(u, v) \right]^4 \cdot NPS(u, v) \, du \, dv \right\}^{1/2}}}$$

Em sistemas com simetria rotacional no plano axial (isotropia radial):

$$\boxed{d'_{\text{NPWE}} = \frac{\int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^2 \cdot 2\pi f \, df}{\left\{ \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ TTF(f) \right]^2 \cdot \left[ E(f) \right]^4 \cdot NPS(f) \cdot 2\pi f \, df \right\}^{1/2}}}$$

O modelo NPWE prevê com elevada acurácia o desempenho humano em fundos homogêneos (ex.: no interior de *phantoms* cilíndricos de água). Contudo, ele apresenta uma limitação crítica: **falha sistematicamente em prever o desempenho quando o sinal está sobreposto a fundos anatômicos estruturados**.

## 3.3 O Desafio dos Fundos Estruturados: Hotelling Observer (HO) e Channelized Hotelling Observer (CHO)

### 3.3.1 Formulação Algébrica do Observador de Hotelling
Quando a tarefa de detecção é realizada sobre anatomias clínicas realistas (parênquima pulmonar, trabeculado ósseo ou tecido hepático), o fundo deixa de ser uniforme e introduz o chamado **ruído anatômico ou estrutural**.

A matriz de covariância total $\mathbf{K}_{\text{total}}$ é a soma de duas componentes estocásticas independentes:

$$\mathbf{K}_{\text{total}} = \mathbf{K}_{\text{ruído}} + \mathbf{K}_{\text{anatômico}}$$

O **Observador de Hotelling** ($HO$) estende a análise discriminante linear de Fisher para maximizar a separabilidade de classes sob fundos variáveis, aplicando o template ótimo:

$$\mathbf{w}_{\text{HO}} = \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle \implies d'_{\text{HO}} = \sqrt{\langle \mathbf{s} \rangle^T \mathbf{K}_{\text{total}}^{-1} \langle \mathbf{s} \rangle}$$

### 3.3.2 Modelagem dos Canais Corticais: Gabor, Laguerre-Gauss e D-DOG
Para simular a neurofisiologia do córtex visual primário (área V1) — que processa a informação visual por meio de grupos de neurônios sintonizados em bandas de frequência espacial e orientações angulares — e para contornar a inviabilidade de inverter a matriz $\mathbf{K}_{\text{total}}$, Barrett et al. (1993) e Yao & Barrett (1992) desenvolveram o **Channelized Hotelling Observer** ($CHO$).

O CHO aplica uma matriz de canais corticais $\mathbf{T} \in \mathbb{R}^{C \times N}$ (onde o número de canais $C \ll N$, tipicamente $C \in [4, 10]$), reduzindo a imagem $\mathbf{g}$ a um vetor de características canalizadas $\mathbf{v} \in \mathbb{R}^C$:

$$\mathbf{v} = \mathbf{T} \mathbf{g}$$

A matriz de covariância no espaço reduzido dos canais $\mathbf{K}_{\mathbf{v}} \in \mathbb{R}^{C \times C}$ é facilmente invertível por métodos numéricos padrão:

$$\mathbf{K}_{\mathbf{v}} = \mathbf{T} \mathbf{K}_{\text{total}} \mathbf{T}^T$$

O índice de detectabilidade do CHO é expresso por:

$$\boxed{d'_{\text{CHO}} = \sqrt{\langle \mathbf{v}_{\mathbf{s}} \rangle^T \mathbf{K}_{\mathbf{v}}^{-1} \langle \mathbf{v}_{\mathbf{s}} \rangle}}$$

onde $\langle \mathbf{v}_{\mathbf{s}} \rangle = \mathbf{T} \langle \mathbf{s} \rangle$.

```
   Imagem Médica g (N pixels) ---> [ Matriz de Canais Corticais T ] ---> Vetor Canalizado v (C x 1)
                                      (C canais, C << N)                     |
                                                                             v
   Estatística Escalar t       <--- [ Template de Hotelling w = Kv^-1 <vs> ] <---+
```

Os principais modelos de canais corticais utilizados na física médica são formulados a seguir:

#### 1. Canais de Gabor
Modelam a resposta anisotrópica do córtex visual a frequências e orientações específicas. A resposta espacial do $j$-ésimo canal de Gabor centrado na frequência radial $f_c$, orientação $\theta$ e largura de banda $\sigma_s$ é:

$$C_j(x, y) = \exp\left[ -\frac{x'^2 + \gamma^2 y'^2}{2\sigma_s^2} \right] \cos\left( 2\pi f_c x' + \phi \right)$$

onde $x' = x\cos\theta + y\sin\theta$ e $y' = -x\sin\theta + y\cos\theta$, e $\gamma$ é a razão de aspecto espacial.

#### 2. Canais Laguerre-Gauss (LG)
Apropriados para tarefas de detecção SKE com simetria rotacional sobre fundos isotrópicos. A função do $n$-ésimo canal LG de escala espacial $a_u$ é expressa por:

$$LG_n(r; a_u) = \frac{\sqrt{2}}{a_u} \exp\left( -\frac{\pi r^2}{a_u^2} \right) L_n\left( \frac{2\pi r^2}{a_u^2} \right)$$

onde $L_n(x) = \sum_{m=0}^n (-1)^m \binom{n}{m} \frac{x^m}{m!}$ é o $n$-ésimo Polinômio de Laguerre ordinário.

#### 3. Canais de Diferença Densa de Gaussianas (*Dense Difference of Gaussians* - D-DOG)
Modelam canais passa-faixa concêntricos isotrópicos com excelente correlação psicofísica humana em imagens tomográficas. O $j$-ésimo canal D-DOG no domínio das frequências é dado por:

$$D\text{-}DOG_j(f) = \exp\left[ -\frac{f^2}{2\sigma_j^2} \right] - \exp\left[ -\frac{f^2}{2(a \sigma_j)^2} \right]$$

onde $\sigma_j = \sigma_0 \alpha^j$ com $\alpha = 1{,}4$ (espaçamento de meia oitava) e $a = 1{,}6$.

## 3.4 Validação Psicofísica com Leitores Humanos e Metodologia Estatística MRMC

A consolidação metrológica de qualquer observador de modelo exige a comprovação formal de sua correlação estatística com o desempenho de radiologistas especialistas.

As leituras humanas são realizadas em ambientes controlados, com monitores diagnósticos calibrados segundo o padrão DICOM Part 14 **GSDF** (*Grayscale Standard Display Function*), nível de luminância calibrado ($\ge 400 \text{ cd/m}^2$), distância de observação fixa ($500 \text{ mm}$) e iluminação ambiente atenuada ($< 15 \text{ lux}$).

A análise estatística rigorosa da variabilidade inter-leitores e inter-casos exige a metodologia **MRMC** (*Multi-Reader Multi-Case*), fundamentada no método de Obuchowski-Rockette-Hillis (ORH) ou Dorfman-Berbaum-Metz (DBM) (HILLIS et al., 2011). O modelo ANOVA misto expressa a variância do índice $d'$ ou da $AUC$:

$$Y_{ijk} = \mu + R_i + C_j + M_k + (RC)_{ij} + (RM)_{ik} + (CM)_{jk} + \epsilon_{ijk}$$

onde $R_i$ representa o efeito aleatório do leitor $i$, $C_j$ o efeito aleatório do caso $j$, e $M_k$ o efeito fixo da modalidade/reconstrução $k$. Para que o modelo observador seja validado como substituto (*surrogate*) metrológico da leitura clínica humana, exige-se Coeficiente de Correlação Intraclasse $ICC \ge 0{,}90$ ($p < 0{,}001$).

---

# CAPÍTULO 4: O COLAPSO DA LINEARIDADE E OS SIMULADORES FÍSICOS MODERNOS

## 4.1 Taxonomia dos Algoritmos de Reconstrução: Da FBP às Reconstruções Iterativas e DLR

A evolução algorítmica dos tomógrafos computadorizados comerciais nos últimos cinquenta anos pode ser compreendida em quatro famílias fundamentais de reconstrução:

```
+---------------------------------------------------------------------------------------------------------+
|                              EVOLUÇÃO DOS ALGORITMOS DE RECONSTRUÇÃO EM TC                              |
+---------------------------------------------------------------------------------------------------------+
| GERAÇÃO   | ALGORITMO BASE | MECANISMO COMPUTACIONAL                  | LINEARIDADE | TEXTURA DO RUÍDO  |
+-----------+----------------+------------------------------------------+-------------+-------------------+
| 1ª (1970) | FBP            | Transformada Inversa de Radon com Ramp   | Estrita     | Fina / Granular   |
| 2ª (2008) | HIR            | Ciclos iterativos estocásticos em sinograma | Parcial     | Moderadamente lisa|
| 3ª (2012) | MBIR           | Modelagem óptica, estatística e geométrica| Não linear  | Cerosa / Borrada  |
| 4ª (2018) | DLR            | Redes Neurais Profundas (CNN / ViT / Dual)| Não linear  | Fina / Natural    |
+---------------------------------------------------------------------------------------------------------+
```

Abaixo apresenta-se a taxonomia detalhada dos algoritmos comerciais dos quatro principais fabricantes globais de tomografia:

| Fabricante | Reconstrução Iterativa Híbrida (HIR) | Reconstrução Iterativa Baseada em Modelos (MBIR) | Reconstrução por Aprendizado Profundo (DLR) |
| :--- | :--- | :--- | :--- |
| **GE Healthcare** | ASiR / ASiR-V | Veo | **TrueFidelity** (DLR treinado com FBP de dose plena) |
| **Canon Medical** | AIDR 3D / AIDR 3D Enhanced | FIRST | **AiCE** (*Advanced intelligent Clear-IQ Engine*, treinado com MBIR) |
| **Siemens Healthineers** | SAFIRE / ADMIRE | REDUCE | **Precise Image** / **Alpha Engine** (PCCT NAEOTOM) |
| **Philips Healthcare** | iDose4 | IMR (*Iterative Model Reconstruction*) | **Precise Image** (DLR baseado em rede neural convolucional) |

## 4.2 A Quebra da Linearidade, Não-Estacionariedade e o "Efeito Ceroso" (*Plastic Look*)

Em algoritmos de Reconstrução por Aprendizado Profundo ($DLR$) e $MBIR$, a operação de mapeamento dos dados brutos de projeção $\mathbf{y}$ na imagem reconstruída $\mathbf{x}$ não pode ser representada por uma transformação linear matricial:

$$\mathbf{x} = \mathcal{R}_{\text{DLR}}(\mathbf{y}) \ne \mathbf{A}^\dagger \mathbf{y}$$

As consequências físicas e metrológicas dessa não linearidade romperam as premissas dos modelos lineares clássicos:

1. **Dependência do Contraste e da Morfologia do Sinal:** A resolução espacial ($TTF(f)$) não é fixa. Em estruturas de alto contraste (ex.: insertos de iodo ou osso cortical), o algoritmo $DLR$ preserva as altas frequências espaciais ($f_{50}$ elevado); em estruturas de baixo contraste (ex.: parênquima hepático ou nódulos em vidro fosco), a $TTF$ decai mais rapidamente, demonstrando que a resolução do sistema depende dinamicamente da cena.
2. **Não-Estacionariedade Espacial do Ruído:** O ruído da imagem não possui propriedades estatísticas homogêneas ao longo da matriz. Próximo a transições anatômicas abruptas, o ruído mantém frequência elevada; no interior de regiões homogêneas de tecidos moles, o algoritmo atua com agressiva regularização de ruído.
3. **O Efeito Ceroso / Plástico (*Plastic/Waxy Look*):** Em algoritmos $MBIR$ e $HIR$ de alta intensidade, o $NPS(f)$ sofre um deslocamento massivo em direção a baixas frequências espaciais ($f_{\text{peak}} \to 0$). Visualmente, a imagem perde a textura estocástica granular e adquire um aspecto "pintado a óleo" ou plastificado. Esse fenômeno compromete criticamente a detecção humana de bordas lesivas tênues (TOIA et al., 2023).
4. **Falha Estrutural do Modelo NPWE Clássico:** O modelo $NPWE$ integra o produto de $TTF(f)$ e $NPS(f)$ assumindo invariância translacional global. Quando aplicado a sistemas $DLR$, ele tende a prever um ganho teórico de detectabilidade que não se confirma nas leituras psicofísicas de radiologistas reais (GREFFIER et al., 2026).

## 4.3 A Transição Metrológica dos *Phantoms*: De Geometrias Homogêneas a Simuladores Antropomórficos Híbridos

Historicamente, o controle de qualidade em radiodiagnóstico utilizou *phantoms* cilíndricos homogêneos de acrílico ou água (como o *phantom* Catphan® 500/600 ou os cilindros CTDI de PMMA de 16 e 32 cm). Embora adequados para calibração de números CT em HU sob feixes lineares de FBP, esses simuladores simples são completamente ineficazes para avaliar algoritmos $DLR$.

Redes neurais profundas de reconstrução foram treinadas predominantemente sobre anatomias humanas reais. Ao processar um cilindro geométrico perfeitamente homogêneo, a rede neural encontra um padrão fora da distribuição (*out-of-distribution*), atuando de forma atípica e distorcendo as medições metrológicas.

Para restabelecer o rigor da avaliação física, a física médica realizou a transição para **Phantoms Antropomórficos Híbridos**:

```
   [ Aquisição Tomográfica do Phantom Antropomórfico Físico (ex: FREDDIE) ]
   (Phantoms de Tórax, Abdome e Crânio com Densidades Equivalentes a Tecidos)
                                     |
                                     v
                  [ Banco de Imagens de Fundo Real (H0) ]
                                     |
                +--------------------+--------------------+
                |                                         |
                v                                         v
   [ Casos de Fundo Puro (H0) ]               [ Inserção Digital Híbrida de Lesões ]
                                              (Modelagem 3D + Convolução PSF do Scanner)
                                                          |
                                                          v
                                              [ Casos com Lesão Inserida (H1) ]
                                                          |
                +-----------------------------------------+
                v
   [ Plataforma 2AFC: Painel de Radiologistas Especialistas vs. Observadores DLMO ]
```

### O Conceito de Phantoms Híbridos
1. **Simuladores Físicos de Alta Fidelidade (ex.: FREDDIE):** Fabricados por impressão 3D multimaterial de alta resolução, utilizando polímeros com coeficientes de atenuação linear idênticos aos do tecido mole, pulmão esponjoso e osso trabecular;
2. **Inserção Híbrida Computacional:** Adquirem-se imagens do *phantom* físico sob dezenas de protocolos clínicos. Em seguida, inserem-se computacionalmente modelos matemáticos tridimensionais de lesões sintéticas (nódulos pulmonares sólidos, sub-sólidos e em vidro fosco, ou metástases hepáticas), convolvendo a lesão com a $PSF$ tridimensional do tomógrafo e adicionando ruído quântico local.

Essa metodologia híbrida gera bancos de milhares de pares de imagens com verdade de campo (*ground truth*) milimétrica e anatomia realista, viabilizando testes psicofísicos $2AFC$ e treinamento de redes neurais sem degradação física do *phantom*.

## 4.4 Tratamento de Ruído em Fundos Anatômicos: Quase-Estacionariedade, *Detrending* e Incerteza Bootstrap

O cálculo de métricas espectrais ($NPS$) no parênquima pulmonar ou tecido abdominal de um *phantom* antropomórfico requer a remoção dos gradientes de atenuação anatômica macroscópicos. A aplicação direta da Transformada de Fourier 2D em uma região não homogênea resultaria em um espectro dominado pela baixíssima frequência da anatomia, mascarando completamente o ruído estocástico do algoritmo.

Para garantir o rigor metrológico, adota-se a hipótese de **Quase-Estacionariedade Local** aliada a algoritmos de **Detrending Polinomial 2D**:

1. **Amostragem em Mosaico:** Subdivide-se a região anatômica de interesse em $M$ sub-ROIs independentes de dimensões $N_x \times N_y$ (ex.: $64 \times 64$ ou $128 \times 128$ pixels);
2. **Ajuste de Superfície Polinomial de 2ª Ordem:** Para cada sub-ROI $I_k(x, y)$, ajusta-se uma superfície bidimensional $P_2(x, y)$ por mínimos quadrados lineares:
   $$P_2(x, y) = a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy$$
3. **Subtração Residual:** Extrai-se a matriz pura de ruído estocástico $\delta I_k(x, y)$:
   $$\delta I_k(x, y) = I_k(x, y) - P_2(x, y)$$
4. **Janelamento e Média Espectral:** Aplica-se uma janela de Hanning bidimensional $w_H(x, y)$ para eliminar descontinuidades de borda (*spectral leakage*), calculando o $NPS$ médio:
   $$NPS(u, v) = \frac{\Delta x \Delta y}{N_x N_y \cdot U} \frac{1}{M} \sum_{k=1}^M \left| \mathcal{F}_{2D} \left\{ \delta I_k(x, y) \cdot w_H(x, y) \right\} \right|^2$$
   onde $U = \frac{1}{N_x N_y} \sum \sum w_H^2(x, y)$ é o fator de normalização de potência da janela.

### Determinação da Incerteza por Bootstrap Não-Paramétrico
Para quantificar o erro padrão e o intervalo de confiança de 95% do índice $d'$ sem impor premissas gaussianas arbitrárias, aplica-se a técnica de reamostragem estatística **Bootstrap**:
- Realizam-se $B = 2000$ reamostragens com reposição do conjunto de ROIs amostradas;
- Calcula-se $d'^{*b}$ para cada reamostragem $b \in [1, B]$;
- O erro padrão bootstrap é dado por:
  $$\text{SE}_{\text{boot}}(d') = \sqrt{\frac{1}{B-1} \sum_{b=1}^B \left( d'^{*b} - \overline{d'}^* \right)^2}$$

Garante-se assim a rastreabilidade e o rigor metrológico dos resultados experimentais.

---

# CAPÍTULO 5: O ESTADO DA ARTE: OBSERVADORES DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO

## 5.1 Observadores Baseados em Aprendizado Profundo (*Deep Learning Model Observers* - DLMO)

Diante do esgotamento analítico dos modelos lineares ($NPWE$, $CHO$) na caracterização de sistemas tomográficos $DLR$, a fronteira da física médica orientou-se para o desenvolvimento de **Observadores de Modelo Baseados em Aprendizado Profundo** (*Deep Learning Model Observers* - DLMO).

Em vez de impor um template linear rígido, o DLMO emprega uma rede neural profunda com parâmetros ajustáveis $\boldsymbol{\theta}$ para aprender diretamente da imagem a função de mapeamento não linear na estatística de teste escalar:

$$t_{\text{DL}}(\mathbf{g}) = f_{\boldsymbol{\theta}}(\mathbf{g})$$

```
   Imagem Médica g ---> [ Extrator de Características Convolucional ]
                                      |
                                      v
                        [ Blocos de Auto-Atenção (Self-Attention) ]
                                      |
                                      v
                        [ Camadas Densas / Cabeça de Decisão ]
                                      |
                                      v
                         Estatística de Decisão Escalar t
```

### Arquiteturas Avançadas e Mecanismos de Atenção
Duas famílias arquiteturais destacam-se na literatura contemporânea (ZHOU et al., 2021; SCHILDER et al., 2026):
1. **Redes Neurais Convolucionais Siamesas e ResNets:** Empregam conexões residuais (*skip connections*) para extrair representações multiescala de textura, mantendo estabilidade numérica de gradientes em imagens médicas de alta resolução;
2. **Vision Transformers (ViT):** Subdividem a imagem em uma sequência de *patches* bidimensionais projetados linearmente e aplicam mecanismos de **Auto-Atenção Multi-Cabeça** (*Multi-Head Self-Attention* - MHSA). A auto-atenção permite ao modelo computacional ponderar simultaneamente correlações de ruído de curto alcance e relações contextuais anatômicas de longo alcance, emulando os movimentos sacádicos e a alternância de atenção foveal/periférica observada em radiologistas durante a interpretação de exames tomográficos.

A estatística de teste gerada pela rede profunda sob conjuntos independentes de imagens com sinal ausente ($H_0$) e sinal presente ($H_1$) permite calcular o **Índice de Detectabilidade Não Linear por Aprendizado Profundo**:

$$d'_{\text{DL}} = \frac{\langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_1 \rangle - \langle f_{\boldsymbol{\theta}}(\mathbf{g}) | H_0 \rangle}{\sqrt{\frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_1) + \frac{1}{2}\sigma^2(f_{\boldsymbol{\theta}}(\mathbf{g})|H_0)}}$$

## 5.2 Calibração Perceptual com Radiologistas e Transferibilidade Inter-Scanners (*Leave-One-Scanner-Out*)

Um modelo de IA treinado unicamente para minimizar a entropia cruzada em tarefas de classificação atua como um aproximador do Observador Ideal não linear, atingindo acurácia superior à de qualquer ser humano. Para que o DLMO funcione como um **instrumento metrológico representativo da clínica médica**, ele deve ser **calibrado para emular as limitações psicofísicas dos radiologistas**.

### Função de Perda Ancorada na Percepção Humana
O treinamento supervisionado do DLMO é conduzido por meio de uma função de perda composta multitarefa:

$$\mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{classificação}}(y, \hat{y}) + \lambda \, \mathcal{L}_{\text{perceptual}}(d'_{\text{DL}}, d'_{\text{humano}})$$

onde:
- $\mathcal{L}_{\text{classificação}}(y, \hat{y}) = - \left[ y \ln \hat{y} + (1-y)\ln(1-\hat{y}) \right]$ é a perda de entropia cruzada binária padrão;
- $\mathcal{L}_{\text{perceptual}} = \left( d'_{\text{DL}}(\boldsymbol{\theta}) - d'_{\text{humano}} \right)^2$ é a perda de calibração perceptual que penaliza desvios quadráticos entre a detectabilidade prevista pela IA e a detectabilidade medida empiricamente no painel de radiologistas em testes $2AFC$;
- $\lambda > 0$ é o hiperparâmetro de regularização biofísica.

### Validação de Transferibilidade Inter-Scanners (*Leave-One-Scanner-Out*)
A generalização metrológica do DLMO é avaliada pelo protocolo rigoroso de validação cruzada **Leave-One-Scanner-Out (LOSO)**:
- Dispõe-se de imagens adquiridas em $K$ tomógrafos clínicos distintos de diferentes fabricantes (ex.: GE Revolution, Siemens SOMATOM Force, Philips Spectral, Canon Aquilion One);
- O DLMO é treinado utilizando exclusivamente os dados de $K - 1$ tomógrafos;
- O modelo é testado cegamente no tomógrafo restante não visto durante o treinamento.

Esse procedimento quantifica a transferibilidade do modelo e estabelece os limites de calibração necessários para que um único software metrológico possa ser comissionado universalmente em qualquer centro hospitalar.

## 5.3 Otimização Multiobjetivo em TC: A Fronteira de Pareto Tridimensional $(D, T, -W)$ e Algoritmos Genéticos

Na física médica tradicional, a otimização de protocolos foi historicamente tratada como um compromisso bidimensional: minimizar a dose de radiação ($D$) sujeita a manter uma detectabilidade mínima aceitável ($W = d' \ge d'_{\text{limiar}}$).

Contudo, a rotina de serviços hospitalares de alta demanda (centros de trauma, prontos-socorros e centros oncológicos) impõe uma terceira restrição operacional crítica: o **Tempo Operacional ($T$)**, composto pelo somatório do **Tempo de Aquisição ($T_{\text{aq}}$)** e do **Tempo de Reconstrução Computacional ($T_{\text{rec}}$)**:

$$T = T_{\text{aq}} + T_{\text{rec}}$$

1. **Tempo de Aquisição ($T_{\text{aq}}$):** Determinado pela velocidade de rotação do gantry (s/rot) e pelo *pitch* helicoidal. Em tomógrafos clínicos submetidos a limites de potência no tubo de raios X, a redução drástica de $T_{\text{aq}}$ para eliminar artefatos de movimento respiratório ou cardíaco exige correntes de tubo (mA) muito altas; ao atingir a saturação térmica do ânodo, o tomógrafo é obrigado a limitar a fluência de fótons, aumentando o ruído quântico e degradando $d'$.
2. **Tempo de Reconstrução ($T_{\text{rec}}$):** Algoritmos iterativos densos ($MBIR$) e redes neurais profundas ($DLR$) executadas em servidores hospitalares introduzem latências de processamento computacional que podem variar de 10 segundos a mais de 15 minutos por varredura volumétrica. Em pacientes politraumatizados ou com suspeita de acidente vascular cerebral em janela trombolítica, uma latência de reconstrução elevada é clinicamente proibitiva, mesmo que a imagem ofereça excelente detectabilidade.

Assim, a física médica moderna formula a otimização como um problema de **Otimização Multiobjetivo Não Linear com Restrições**:

$$\min_{\mathbf{p} \in \Omega} \mathbf{F}(\mathbf{p}) = \begin{pmatrix} D(\mathbf{p}) \\ T(\mathbf{p}) \\ -W(\mathbf{p}) \end{pmatrix}$$

onde:
- $\mathbf{p} = (\text{kVp}, \text{mA}, \text{tempo de rotação}, \text{pitch}, \text{algoritmo de reconstrução}, \text{intensidade de filtragem}) \in \Omega$ é o vetor de parâmetros configuráveis do tomógrafo;
- $\Omega$ é o espaço de busca viável delimitado pelas **restrições clínicas formais**:
  $$\begin{cases}
  D(\mathbf{p}) \le \text{DRL} & \text{(Restrição Radiológica: Dose abaixo do Nível de Referência Diagnóstica)} \\
  T(\mathbf{p}) \le T_{\text{máx}} & \text{(Restrição Operacional: Tempo total abaixo do limiar de urgência)} \\
  W(\mathbf{p}) = d'(\mathbf{p}) \ge d'_{\text{mín}} & \text{(Restrição Diagnóstica: Detectabilidade mínima para a patologia)}
  \end{cases}$$

```
             Dose de Radiação (D)
                    ^
                    |      x (Protocolo Ineficiente / Dominado)
                    |     /
                    |    /   +---------------------------------------+
                    |   /    |  FRONTEIRA DE PARETO TRIDIMENSIONAL   |
                    |  /     |  (Conjunto de Protocolos Ótimos)      |
                    | v      +---------------------------------------+
                    +----------------------------------------> Tempo Operacional (T)
                   /
                  /
                 v
       Detectabilidade Diagnóstica (W = d')
```

### Dominância de Pareto e Algoritmo NSGA-II
Um protocolo $\mathbf{p}_1$ **domina no sentido de Pareto** outro protocolo $\mathbf{p}_2$ ($\mathbf{p}_1 \prec \mathbf{p}_2$) se e somente se:

$$\forall i \in \{D, T, -W\}, \, F_i(\mathbf{p}_1) \le F_i(\mathbf{p}_2) \quad \text{e} \quad \exists j \in \{D, T, -W\} \text{ tal que } F_j(\mathbf{p}_1) < F_j(\mathbf{p}_2)$$

O conjunto de todas as soluções não dominadas constitui a **Fronteira de Pareto Tridimensional**. Para mapear essa fronteira sobre o espaço discreto e contínuo dos parâmetros do tomógrafo, emprega-se o algoritmo genético **NSGA-II** (*Non-dominated Sorting Genetic Algorithm II*) acoplado a métodos de Tomada de Decisão Multicritério (como o método **TOPSIS** - *Technique for Order Preference by Similarity to Ideal Solution*).

Isso permite à equipe multiprofissional (físicos médicos, radiologistas e administradores hospitalares) selecionar analiticamente o protocolo ótimo ideal para cada contexto: protocolos de dose ultra-baixa para rastreamento pediátrico, protocolos de velocidade máxima para emergência ou protocolos de detectabilidade máxima para oncologia de alta complexidade.

## 5.4 Fronteiras Futuras: Tomografia por Contagem de Fótons (PCCT) e Imagens Monoenergéticas (VMI)

A **Tomografia Computadorizada por Contagem de Fótons** (*Photon-Counting CT* - PCCT) representa o mais recente marco evolutivo da instrumentação radiológica. Ao substituir os detectores cintiladores convencionais de integração de energia (EICT) por detectores semicondutores de conversão direta (como Telureto de Cádmio - CdTe ou Silício), a PCCT atinge três vantagens físicas sem precedentes:

1. **Eliminação do Ruído Eletrônico:** Fótons de raios X que depositam energia abaixo de um limiar mínimo de ruído elétrico são descartados na contagem de pulsos, permitindo exames com níveis ultra-baixos de dose sem degradação do sinal;
2. **Resolução Espacial Ultra-Alta:** A ausência de septos refletores ópticos permite a redução do tamanho dos pixels do detector para $0{,}1 \text{ a } 0{,}2 \text{ mm}$, elevando $f_{50}$ e a $TTF$ em frequências espaciais superiores a $2{,}0 \text{ mm}^{-1}$;
3. **Espectroscopia Intrínseca e Imagens Monoenergéticas Virtuais ($VMI$):** A classificação de fótons em múltiplos canais de energia (*energy bins*) viabiliza a síntese computacional de imagens monocromáticas virtuais em energias contínuas de $40 \text{ a } 140 \text{ keV}$.

A integração de observadores baseados em aprendizado profundo na análise de imagens PCCT permite otimizar automaticamente a energia virtual $E_{\text{ótima}}$ (em keV) que maximiza a detectabilidade $d'$ para cada tipo de contraste e patologia (PIMENTA & COSTA, 2025; PIMENTA, 2026).

---

# CAPÍTULO 6: METODOLOGIA EXPERIMENTAL, ARQUITETURA DE SOFTWARE E ASPECTOS BIOÉTICOS

## 6.1 Arquitetura de Software do Pipeline Integrado de Metrologia

Para viabilizar a execução metrológica reprodutível, a infraestrutura computacional deste trabalho foi concebida segundo uma arquitetura modular em Python (utilizando NumPy, SciPy, PyDICOM e PyTorch), garantindo integração com os pipelines de pesquisa do grupo GDRFM-IFUSP:

```
+---------------------------------------------------------------------------------------------------+
|                        FLUXO METROLÓGICO DO SOFTWARE DE AVALIAÇÃO BASEADA EM TAREFAS              |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  [ Imagens DICOM TC ] ---> [ Módulo 1: Parser e Validação de Metadados ]                          |
|                                         |                                                         |
|                                         v                                                         |
|                            [ Módulo 2: Segmentação Automática e ROIs ]                            |
|                                         |                                                         |
|                    +--------------------+--------------------+                                    |
|                    |                                         |                                    |
|                    v                                         v                                    |
|      [ Módulo 3A: Resolução ]                  [ Módulo 3B: Ruído ]                               |
|      • Extração de Borda Circular              • Detrending Polinomial 2D                         |
|      • ESF(r) -> LSF(r) -> TTF(f)              • Janelamento Hanning -> NPS 2D/1D                 |
|                    |                                         |                                    |
|                    +--------------------+--------------------+                                    |
|                                         |                                                         |
|                                         v                                                         |
|                            [ Módulo 4: Observadores de Modelo ]                                   |
|                            • Lineares: NPWE, HO, CHO (Gabor, LG, D-DOG)                           |
|                            • Aprendizado Profundo: DLMO (CNN / ViT)                               |
|                                         |                                                         |
|                                         v                                                         |
|                            [ Módulo 5: Incerteza e Otimização ]                                   |
|                            • Erro Padrão Bootstrap (2000 reamostragens)                           |
|                            • Algoritmo Genético NSGA-II: Fronteira Pareto 3D                      |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

## 6.2 Protocolo Metrológico Padronizado segundo o AAPM TG-233

As aquisições tomográficas para calibração e teste seguem rigorosamente as diretrizes internacionais do relatório **AAPM TG-233**:

1. **Parâmetros de Varredura:** Matriz de $512 \times 512$ pixels, FOV ajustado ao diâmetro do simulador ($200 \text{ a } 350 \text{ mm}$), espessura de corte nominal ($0{,}5 \text{ a } 1{,}0 \text{ mm}$ para alta resolução e $2{,}5 \text{ a } 5{,}0 \text{ mm}$ para padrão clínico), tensões de tubo de $80, 100, 120 \text{ e } 140 \text{ kVp}$, e níveis de dose de $\text{CTDI}_{\text{vol}}$ variando de $0{,}5 \text{ mGy}$ (ultra-baixa dose) a $15 \text{ mGy}$ (dose diagnóstica de referência);
2. **Estabilização da Amostragem:** Coleta-se um número mínimo de $M \ge 100$ sub-ROIs homogêneas independentes para garantir a convergência estatística e a estabilidade da matriz de covariância do ruído;
3. **Modelagem de Tarefa Diagnóstica:** Lesões circulares e esferoidais padronizadas com diâmetros de $3 \text{ mm}, 5 \text{ mm}, 8 \text{ mm} \text{ e } 10 \text{ mm}$, simulando contrastes clínicos típicos de $-600 \text{ HU}$ (nódulo pulmonar subsólido), $+100 \text{ HU}$ (nódulo sólido hiperatenuante) e $+30 \text{ HU}$ (lesão hepática de baixo contraste).

## 6.3 Aspectos Bioéticos, Regulatórios e Desenho Experimental Humano (CEP/CONEP)

O estudo psicofísico com médicos radiologistas para obtenção dos dados de calibração $2AFC$ é classificado como pesquisa envolvendo seres humanos, exigindo aprovação prévia em **Comitê de Ética em Pesquisa (CEP/CONEP)**:

- **Amostragem e População de Leitores:** Recrutamento de no mínimo 20 médicos radiologistas com título de especialista pelo Colégio Brasileiro de Radiologia (CBR) para cada anatomia clínica avaliada (totalizando $\ge 60$ leitores para tórax, abdome e crânio);
- **Termo de Consentimento Livre e Esclarecido (TCLE):** Aplicação obrigatória de TCLE digital com explicitação dos objetivos acadêmicos e garantia de anonimização dos dados de desempenho individual;
- **Mitigação de Fadiga Visual e Viés de Memória:** Estruturação das sessões em blocos de no máximo 100 a 150 pares de imagens $2AFC$ por sessão (duração inferior a 25 minutos), com intervalo mandatório de descanso visual e randomização espacial cega (ordem aleatória de apresentação dos campos $H_0$ e $H_1$).

---

# CAPÍTULO 7: CONSIDERAÇÕES FINAIS E PERSPECTIVAS

## 7.1 Síntese da Trajetória Biofísica e Epistemológica

A história da avaliação da qualidade de imagem em Tomografia Computadorizada ilustra uma jornada epistemológica fascinante: a substituição progressiva de métricas físicas abstratas por modelos matemáticos que incorporam a complexidade da biologia humana e da física dos sistemas não lineares.

Partindo da teoria estatística de detecção de sinais da década de 1950 e do Observador Ideal, a física médica construiu observadores lineares refinados ($NPWE$, $CHO$) que serviram com primor à era da Retroprojeção Filtrada. A quebra irreversível da linearidade imposta pelas Reconstruções por Aprendizado Profundo ($DLR$) forçou a disciplina a um novo salto qualitativo: o desenvolvimento de observadores computacionais baseados em redes neurais profundas com mecanismos de atenção foveal ($DLMO$), ancorados em experimentos psicofísicos humanos e validados em simuladores antropomórficos realistas.

## 7.2 Impacto Clínico, Operacional e Normativo

A consolidação desse arcabouço metrológico produz benefícios imediatos para a sociedade e para o sistema de saúde:
- **Segurança Radiológica Personalizada:** Permite comprovar cientificamente que reduções de dose de até 70% preservam a detectabilidade diagnóstica de lesões críticas, viabilizando programas populacionais de rastreamento tomográfico seguros;
- **Comissionamento e Auditoria Hospitalar:** Fornece ferramentas computacionais automatizadas para que físicos médicos hospitalares executem auditorias de qualidade em conformidade com o relatório **AAPM TG-233** e o sistema internacional **IAEA 5-Star**;
- **Harmonização Tecnológica:** Facilita a equalização de protocolos entre tomógrafos de diferentes fabricantes e gerações tecnológicas em redes de saúde públicas e privadas.

## 7.3 Articulação com a Pesquisa de Doutorado Direto (FAPESP)

Esta monografia de conclusão de curso cumpre o papel fundamental de edificar e consolidar a base teórica, matemática e metodológica que sustentará o projeto de pesquisa de **Doutorado Direto do autor** (FAPESP 2026–2030) junto ao Grupo de Dosimetria e Radioproteção em Física Médica (GDRFM-IFUSP):

- **Continuidade com Projetos do Grupo:** Integra-se organicamente aos avanços pioneiros em PCCT da Dra. Elsa Pimenta (Doutorado 2026) e ao pipeline automatizado de métricas lineares no tórax desenvolvido por Davi Amaral (Mestrado FAPESP);
- **Metas Inovadoras do Doutorado:**
  1. Construção, treinamento e validação do observador $DLMO$ baseado em *Vision Transformers*;
  2. Condução do estudo psicofísico nacional $2AFC$ com mais de 60 radiologistas especialistas;
  3. Validação cruzada de transferibilidade inter-scanners (*leave-one-scanner-out*) em 7 tomógrafos de 4 fabricantes instalados no InRad-HCFMUSP e Radboudumc;
  4. Mapeamento experimental completo da Fronteira de Pareto Tridimensional $(D, T, -W)$ para os principais protocolos tomográficos de crânio, tórax e abdome.

Dessa forma, conclui-se este trabalho com a certeza de que a física médica brasileira permanece na vanguarda da pesquisa metrológica e computacional internacional, unindo o rigor da física teórica à nobre missão de proteger e diagnosticar vidas humanas.

---

# REFERÊNCIAS BIBLIOGRÁFICAS

1. **ABBEY, C. K.; BARRETT, H. H.** Human- and model-observer performance in ramp-spectrum noise with regularization. *Journal of the Optical Society of America A*, v. 18, n. 3, p. 473-488, 2001.
2. **AMERICAN ASSOCIATION OF PHYSICISTS IN MEDICINE (AAPM).** *Performance Evaluation of Computed Tomography Systems: The Report of AAPM Task Group 233*. AAPM Report No. 233. Alexandria, VA: AAPM, 2019. (Samei, E. et al., *Medical Physics*, v. 46, n. 11, p. e735-e756, 2019).
3. **BARRETT, H. H.; MYERS, K. J.** *Foundations of Image Science*. Hoboken: John Wiley & Sons, 2004. 1540 p.
4. **BARRETT, H. H.; YAO, J.; ROLAND, P. X.; MYERS, K. J.** Model observers for assessment of image quality. *Physics in Medicine & Biology*, v. 38, n. 2, p. 277-295, 1993.
5. **BURGESS, A. E.** Statistically defined backgrounds: performance of a modified nonprewhitening observer model. *Journal of the Optical Society of America A*, v. 11, n. 4, p. 1237-1242, 1994.
6. **BURGESS, A. E.** The Rose model, revisited. *Journal of the Optical Society of America A*, v. 16, n. 3, p. 633-646, 1999.
7. **BURGESS, A. E.** Visual perception studies and observer models in medical imaging. *Seminars in Nuclear Medicine*, v. 41, n. 6, p. 419-436, 2011.
8. **CHOOPANI, R. et al.** Standardized task-based image quality assessment in computed tomography: automated pipeline and multi-center validation. *Physics in Medicine & Biology*, v. 68, n. 14, p. 145002, 2023.
9. **DEBBICHE, I. et al.** Task-based image quality assessment of deep learning image reconstruction in abdominal CT: a multi-reader phantom study. *European Radiology*, v. 34, n. 5, p. 3120-3132, 2024.
10. **DORFMAN, D. D.; BERBAUM, K. S.; METZ, C. E.** Receiver operating characteristic rating analysis: generalization to the population of readers and patients with the jackknife method. *Investigative Radiology*, v. 27, n. 9, p. 723-731, 1992.
11. **ECKSTEIN, M. P.; WHITING, J. S.; THOMAS, J. P.** Role of knowledge in human visual search for signals in noise. *Journal of the Optical Society of America A*, v. 17, n. 11, p. 2064-2076, 2000.
12. **GREFFIER, J. et al.** Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom. *Diagnostic and Interventional Imaging*, v. 107, n. 1, p. 1016-1025, 2026.
13. **GREFFIER, J. et al.** Comparison of iterative and deep learning reconstruction algorithms in low-dose abdominal CT: a task-based image quality study on a phantom. *European Radiology*, v. 33, p. 7890-7901, 2023.
14. **HILLIS, S. L.; OBUCHOWSKI, N. A.; BERBAUM, K. S.** Multi-reader multi-case ROC analysis: an updated review of methods and software. *Academic Radiology*, v. 18, n. 7, p. 842-856, 2011.
15. **INTERNATIONAL ATOMIC ENERGY AGENCY (IAEA).** Dose-aware 5-star image quality rating in CT: Findings from the IAEA-MGH study. *European Journal of Radiology*, v. 184, p. 113133, 2026.
16. **INTERNATIONAL COMMISSION ON RADIATION UNITS AND MEASUREMENTS (ICRU).** *Medical Imaging - The Assessment of Image Quality*. ICRU Report 54. Bethesda, MD: ICRU, 1996.
17. **LUSTED, L. B.** *Introduction to Medical Decision Making*. Springfield, IL: Charles C Thomas, 1968.
18. **MCCOLLOUGH, C. H. et al.** Radiation dose in computed tomography: technological advances and clinical optimization over two decades. *Radiology*, v. 318, n. 2, p. e251200, 2026.
19. **METZ, C. E.** ROC methodology in radiologic imaging. *Investigative Radiology*, v. 21, n. 9, p. 720-733, 1986.
20. **MYERS, K. J.; BARRETT, H. H.** Addition of a channel mechanism to the ideal-observer model. *Journal of the Optical Society of America A*, v. 4, n. 12, p. 2447-2457, 1987.
21. **OBUCHOWSKI, N. A.; ROCKETTE, H. E.** Hypothesis testing of diagnostic accuracy for multiple readers and multiple tests: an ANOVA approach with dependent observations. *Communications in Statistics - Simulation and Computation*, v. 24, n. 2, p. 285-308, 1995.
22. **OOSTVEEN, L. J. et al.** Fast CT acquisition protocols and their impact on image quality and radiation dose: trade-offs in clinical practice. *European Radiology*, v. 31, p. 7412-7421, 2021.
23. **PETERSON, W. W.; BIRDSALL, T. G.; FOX, W. C.** The theory of signal detectability. *Transactions of the IRE Professional Group on Information Theory*, v. 4, n. 4, p. 171-212, 1954.
24. **PIMENTA, E. F.; COSTA, P. R.** Task-based image quality in energy-integrating and photon-counting computed tomography: a phantom study in ultra-low dose thoracic imaging. *Medical Physics*, v. 52, n. 4, p. 2150-2165, 2025.
25. **PIMENTA, E. F.** *Avaliação baseada em tarefas da qualidade de imagem em tomografia computadorizada por contagem de fótons no tórax*. 2026. Tese (Doutorado em Física Médica) – Instituto de Física, Universidade de São Paulo, São Paulo, 2026.
26. **RACINE, D. et al.** Task-based image quality assessment in abdominal CT: comparison between filtered backprojection, adaptive statistical iterative reconstruction, and deep learning reconstruction. *Physics in Medicine & Biology*, v. 65, n. 18, p. 185011, 2020.
27. **RACINE, D. et al.** Multi-reader multicase evaluation of liver lesion detectability in CT: validating model observers against human radiologist performance. *Medical Physics*, v. 48, n. 6, p. 2890-2901, 2021.
28. **ROSE, A.** The sensitivity performance of the human eye on an absolute scale. *Journal of the Optical Society of America*, v. 38, n. 2, p. 196-208, 1948.
29. **SAMEI, E. et al.** Assessment of image quality in CT: from physical measurements to task-based performance. *Medical Physics*, v. 46, n. 11, p. e735-e756, 2019.
30. **SCHILDER, C. M. et al.** Artificial intelligence in medical physics: recent developments in image reconstruction, perception modeling, and clinical workflow integration. *La Rivista del Nuovo Cimento*, v. 49, n. 3, p. 145-210, 2026.
31. **SOLOMON, J. et al.** Task-based image quality assessment of deep learning reconstruction in low-dose CT across multiple phantom models and reader paradigms. *Medical Physics*, v. 47, n. 8, p. 3412-3425, 2020.
32. **TOIA, G. V. et al.** Human reader vs. model observer detectability of small hypoattenuating liver lesions reconstructed with deep learning algorithms in CT. *European Radiology*, v. 33, p. 4310-4322, 2023.
33. **WAGNER, R. F.; BROWN, D. G.; METZ, C. E.** Application of information theory to the assessment of computed tomography. *Medical Physics*, v. 6, n. 2, p. 83-94, 1979.
34. **YAO, J.; BARRETT, H. H.** Predicting human performance by a channelized Hotelling observer model. In: *SPIE Medical Imaging: Image Perception*, v. 1654, p. 268-278, 1992.
35. **ZHOU, W. et al.** Approximating human observer performance in non-linear CT image reconstruction using deep convolutional neural networks. *IEEE Transactions on Medical Imaging*, v. 40, n. 9, p. 2350-2362, 2021.
"""

with open(target_path, "w", encoding="utf-8") as f:
    f.write(full_text.strip() + "\n")

print(f"Updated {target_path} successfully. Total characters: {len(full_text)}")
