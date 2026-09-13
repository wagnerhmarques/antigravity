# Índice da Base de Conhecimento

> **Domínio:** Física Médica, Radiologia & Dosimetria em Tomografia Computadorizada  
> **Última Atualização:** 2026-08-23  
> **Total de Fontes:** 8 | **Total de Páginas:** 34

---

## 📚 Fontes Ingeridas (`wiki/fontes/`)
- [[Inteligência Artificial em Física Médica (Nuovo Cimento)|artificial-intelligence-in-medical-physics-nuovo-cimento]] — *Artificial intelligence in medical physics - La Rivista del Nuovo Cimento*: Ingestão da revisão sobre Inteligência Artificial na Física Medica, cobrindo imageamento\, diagnóstico, radioterapia\, dosimetria e cirurgia assistida.
- [[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]] — *Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom*: Ingestão do artigo Greffier et al. (2026) avaliando algoritmos de DLR e IR em 4 tomógrafos (Canon, GE, Philips, United Imaging) através de física médica baseada em tarefas (NPS, TTF, d').
- [[Schilder 2026 - IA em Imagens Médicas|schilder-2026-anticipating-ai-medical-imaging]] — *Anticipating Moral and Economic Considerations, Opportunities, and Potential Frictions for AI in Medical Imaging: Multistakeholder Cocreation Study*: Estudo de co-criação multi-stakeholder (Schilder et al., 2026) detalhando aspectos morais, econômicos e organizacionais do uso da IA em radiologia intramural e extramural.
- [[Wong 2026 - IA no Imageamento Biomédico|wong-2026-ai-biomedical-imaging]] — *Artificial intelligence-powered biomedical imaging: Recent achievements and challenges*: Síntese dos avanços (2020-2025) em IA para imagem biomédica: segmentação\, diagnóstico\, dados sintéticos, XAI, modelos de fundação (GMAI) e desafios de integração clínica e privacidade.
- [[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]] — *Projeto FAPESP Doutorado Direto - Observadores de Aprendizado Profundo para Otimização de Protocolos de TC*: Projeto FAPESP de Doutorado Direto (FMUSP) sobre desenvolvimento e validação de observadores de deep learning com atenção para otimização multiobjetivo de dose, tempo e detectabilidade em TC.

- [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]] — *Image quality in modern CT imaging: optimization and quantification*: Tese de Eva Hoeijmakers (2026) sobre otimização e quantificação de qualidade de imagem em TC moderna (PCD-CT, redução de meio de contraste em abdome/tórax, Pairwise Comparison e métricas objetivas).
- [[Pasyar 2026 - Impressão 3D de Phantoms para TC|dual-filament-3d-printing-ct-phantoms-pasyar-2026]] — *Dual-Filament 3D Printing of Patient-Specific CT Phantoms with Embedded Implants and Tunable Metal-Artifact Intensity*: Artigo de Pasyar et al. (2026) sobre impressão 3D duplo-filamento com PixelPrint para fantomas de TC com artefatos metálicos controlados.
- [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]] — *Comprehensive Assessment of CT Performance: AAPM Task Group 233 Report*: Relatório do AAPM TG-233 detalhando metodologia padronizada de avaliação de desempenho em TC (TTF, NPS, d' e AEC).
- [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg-233-summary]] — *Performance evaluation of computed tomography systems: Summary of AAPM Task Group 233*: Resumo das diretrizes baseadas em tarefas diagnósticas para avaliação de tomógrafos.
- [[McCollough 2026 - Evolução das Doses de Radiação em TC|mccollough-2026-good-news-ct-doses]] — *Good News about CT Doses (Editorial, Radiology 2026)*: Análise histórica demonstrando queda média de 36% nas doses de TC nos EUA (2006–2025), evolução dos DRLs e impacto de novas tecnologias.
- [[Solomon 2016 - Modelos de Observadores em TC|solomon-2016-observer-models]] — *Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography*: Estudo de Solomon & Samei (2016) correlacionando percepção humana (2AFC) e observadores matemáticos em TC com FBP e ADMIRE.
- [[Model Observers e Índice de Detectabilidade em Raios X|model-observers-detectability-index-xray]] — *Model observers and detectability index in x-ray imaging: historical review, applications and future trends*: Revisão histórica e tendências sobre observadores de modelo e cálculo de $d'$ em raios-X e TC.
- [[Model Observers e Detectabilidade em Raios X|model-observers-and-detectability-index-in-x-ray-imaging]] — *Model observers and detectability index in x-ray imaging*: Aplicações em controle de qualidade e otimização clínica.

---

## 🧠 Conceitos, Modelos & Métricas (`wiki/conceitos/`)

### Dosimetria & Otimização Clínica
- [[Métricas de Dose em TC|metricas-de-dose-tc]] — Definições padronizadas de $CTDI_{vol}$ (mGy) e $DLP$ (mGy·cm) para quantificação e auditoria de dose.
- [[Níveis de Referência Diagnóstica (DRL)|niveis-de-referencia-diagnostica-drl]] — Papel dos DRLs (percentil 75) e Achievable Doses (percentil 50) como benchmarking clínico.
- [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]] — Pilares da redução de dose em TC (ALARA, modulação de corrente e reconstruções não-lineares).
- [[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]] — Protocolos de redução de volume de contraste iodado combinados com baixa energia de feixe ($kVp$) e imagens monoenergéticas virtuais.
- [[Risco Oncológico e Epidemiologia da Radiação em TC|risco-oncologico-radiacao-tc]] — Risco radiogênico, análise de coortes epidemiológicas (EPI-CT) e o contraste com as doses clínicas substancialmente menores atuais.

### Qualidade de Imagem Baseada em Tarefa
- [[Task Transfer Function|task-transfer-function]] / [[Task Transfer Function|ttf-task-transfer-function]] — Função de transferência de tarefa (TTF) para resolução espacial em sistemas de reconstrução não-lineares.
- [[Noise Power Spectrum|noise-power-spectrum]] / [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]] — Espectro de potência de ruído (NPS) quantificando textura e magnitude espectral do ruído.
- [[Detectabilidade Index|detectabilidade-index]] / [[Índice de Detectabilidade|indice-de-detectabilidade]] / [[Índice de Detectabilidade|detectability-index]] — Formulação matemática do índice de detectabilidade ($d'$) em tarefas de detecção e discriminação.
- [[Observadores de Modelo (Model Observers)|model-observers]] / [[Observadores de Modelo (Model Observers)|observadores-de-modelo]] — Observadores matemáticos (Channelized Hotelling, NPW) simulando percepção humana.
- [[Contrast To Noise Ratio|contrast-to-noise-ratio]] — Relação sinal/ruído e contraste/ruído tradicional vs. limitações em algoritmos não-lineares.
- [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]] — Princípios psicofísicos de detecção de sinal (SDT), matrizes de decisão e curvas ROC.
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]] — Framework consolidado de métricas objetivas para automação de controle de qualidade.
- [[Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)|avaliacao-pareada-qualidade-imagem]] — Metodologia de Pairwise Comparison (2AFC/4AFC) para avaliação clínica visual padronizada.

### Fantomas & Simulação Física
- [[Pixelprint]] — Algoritmo de mapeamento pixel-a-filamento para simulação contínua de atenuação em radiologia.
- [[Impressão 3D com Duplo Filamento|impressao-3d-duplo-filamento]] — Manufatura aditiva de fantomas paciente-específicos com controle de densidade radiológica.
- [[Métrica Gumbel p-index para Quantificação de Artefatos|metrica-gumbel-p-index]] — Modelagem de valores extremos para quantificar severidade e dispersão de artefatos metálicos.

### Reconstrução & Processamento Espectral
- [[Reconstrução Iterativa|reconstrucao-iterativa]] — Princípios de reconstrução iterativa estatística e modelada para redução de ruído.
- [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]] — Reconstruções monoenergéticas virtuais (VMI em keV) para realce de iodo e redução de artefatos de endurecimento de feixe.
- [[Modulação de Corrente de Tubo (TCM)|controle-automatico-exposicao]] — Modulação angular ($x,y$) e longitudinal ($z$) de corrente de tubo.

---

## 🔬 Tecnologias & Hardware (`wiki/tecnologias/`)

- [[Photon Counting Detector CT (PCD-CT)|photon-counting-ct]] / [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]] — Tomografia por Detectores de Contagem de Fótons (PCD-CT): detectores semicondutores diretos (CdTe/CZT), resolução ultra-alta e eliminação de ruído eletrônico.
- [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]] — Advanced Modeled Iterative Reconstruction (Siemens Healthineers).
- [[Controle Automático de Exposição em TC|controle-automatico-de-exposicao-ct]] — Sistemas de controle e modulação dinâmica de dose em tomógrafos modernos.

---

## 💡 Sínteses & Consultas (`wiki/sinteses/`)

- [[O Índice de Detectabilidade em Tomografia Computadorizada|indice-de-detectabilidade-em-tomografia-computadorizada]] — *O Índice de Detectabilidade ($d'$) em Tomografia Computadorizada: Fundamentação, Métricas e Formulação Matemática*: Síntese definitiva sobre a fundamentação teórica, formulação matemática e métodos de cálculo do Índice de Detectabilidade (d') em Tomografia Computadorizada.

---

## 💡 Consultas & Sínteses (`queries/`)
- [[queries/faça um resumo do último artigo que anexei]] — Resumo executivo da revisão de Amoroso et al. (2025) em La Rivista del Nuovo Cimento sobre aplicações de IA, PINNs e Deep Learning em Física Médica e Tomografia.
- [[queries/o que é SSW-d'?]] — O SSW-d' é a extensão tridimensional do Índice de Detectabilidade que pondera a resposta espectral e a correlação de ruído longitudinal entre múltiplos cortes em TC.
- [[queries/faça um resumo sobre o anexo "CT texture phantom dataset with paired image quality assessments for quantitative imaging"]] — Síntese técnica do dataset CT texture phantom com avaliações de qualidade de imagem pareadas para NPS, TTF e índice de detectabilidade em TC.
- [[queries/faça um resumo sobre CT texture phantom dataset with paired image quality assessments for quantitative imaging]] — Resumo do dataset de phantoms de textura em TC com avaliações pareadas de qualidade de imagem (NPS, TTF, d' e radiômica) para validação de reconstruções não-lineares e imagem quantitativa.
- [[queries/para que serve a biblioteca OpenCV?]] — Visão geral e aplicações da biblioteca OpenCV no processamento de imagens médicas e análises quantitativas de TC.
- [[Aula 2 - PLN]] — Análise técnica da palestra de Rodrigo Nogueira (Maritaca AI) sobre o panorama da IA generativa, leis de escala, especialização de domínio e o gargalo da infraestrutura computacional no Brasil.
- [[queries/Test_Video_Micrograd]] — Análise técnica do vídeo de Andrej Karpathy sobre o micrograd, desconstruindo autograd, backpropagation e a otimização de redes neurais do nível escalar ao PyTorch.
- [[queries/Quando surgiu a tomografia computadorizada?]] — A Tomografia Computadorizada foi inventada por Godfrey Hounsfield em 1971, com fundamentação matemática de Johann Radon e Allan Cormack.
- [[queries/Do que se trata o projeto universal CNPQ? Dê detalhes.]] — A Chamada Universal CNPq é o principal edital de fomento à pesquisa no Brasil, apoiando projetos de todas as áreas do conhecimento, incluindo Física Médica e Tomografia Computadorizada, através de auxílios de custeio, capital e bolsas.
- [[queries/Comente sobre a evolução dos modelos de observadores computacionais. Preciso entender como se deu o avanço, como cada um deles complementa o outro e como posso melhorar a questao da não-linearidade]]
- [[queries/Como devo começar a estruturar o observador profundo, por onde começo?]]
- [[queries/Como funciona o NPS?]]
- [[queries/Já existe DLMO validado na literatura ?]]
- [[queries/O que são phantoms ?]]
- [[queries/O que é pixel print ?]]
- [[queries/O que é raios X ?]]
- [[queries/O que é ttf e porque ele é importante?]]
- [[queries/Quais são as grandes áreas da física médica ?]]
- [[queries/Qual a influencia da tensão de tubo no HU ?]]
- [[queries/Qual é o estado da arte das tecnologias que envolvem meu trabalho de doutorado e como elas podem ser otimizadas ?]]
- [[queries/como funciona a física da tomografia computadorizada? mencione equações]]
- [[queries/o que o projeto de doutorado complementa o projeto AIR e o universal CNPQ?]]
- [[queries/o que é dito no ICRU 95?]]
- [[queries/o que é índice de detectabilidade e como ele pode ser calculado ?]]
- [[queries/quais são os termos mais frequentes na minha estruturaco aqui no obsidian?]]
- [[queries/qual é o diferencial do photon counting detector e como ele pode contribuir para o avanço da tomografia computadorizada?]]
