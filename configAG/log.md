# Log de Operações da Wiki

> **Linha do tempo cronológica (append-only)**  
> **Formato de entrada:** `## [YYYY-MM-DD] <ação> | <alvo>`  
> **Ações padronizadas:** `init`, `ingest`, `query`, `lint`, `refactor`

---

## [2026-08-22] init | Base de Conhecimento Karpathy
- **Ação:** Instanciação da infraestrutura base da LLM Wiki no diretório de trabalho.
- **Diretórios criados:** `raw/`, `raw/assets/`, `wiki/`, `wiki/fontes/`.
- **Arquivos criados:** `SPARK.md`, `ANTIGRAVITY.md`, `ANTIRGAVITY.md`, `index.md`, `log.md`.
- **Configuração:** Domínio definido como "ainda não definido". Regra dos 3+ e nascimento de páginas na raiz de `wiki/` gravadas como regras invioláveis no esquema.
- **Status:** Aguardando primeira fonte em `raw/`.

---

## [2026-08-22] ingest | Good News about CT Doses (McCollough, 2026)
- **Fonte processada:** `raw/Good News about CT Doses.md` (Editorial, *Radiology* 2026, DOI: 10.1148/radiol.261781).
- **Ficha criada:** `wiki/fontes/mccollough-2026-good-news-ct-doses.md`.
- **Páginas criadas:**
  - `wiki/conceitos/metricas-de-dose-tc.md` (`tipo: conceito`)
  - `wiki/conceitos/niveis-de-referencia-diagnostica-drl.md` (`tipo: conceito`)
  - `wiki/conceitos/otimizacao-de-dose-em-tc.md` (`tipo: conceito`)
  - `wiki/conceitos/risco-oncologico-radiacao-tc.md` (`tipo: conceito`)
  - `wiki/photon-counting-ct.md` (`tipo: tecnologia`, solta na raiz)
- **Aplicação da Regra dos 3+:**
  - O `tipo: conceito` atingiu 4 páginas -> criada subpasta `wiki/conceitos/`, arquivos organizados, `SPARK.md` e `index.md` atualizados.
- **Domínio consolidado:** Física Médica, Radiologia & Dosimetria em Tomografia Computadorizada.

---

## [2026-08-23] ingest | Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography
- **Fonte processada:** `Correlation between human detection accuracy and observer model-based image quality metrics in computed tomography.md`
- Processada fonte inicial: solomon-2016-observer-models
- Criada ficha da fonte em `wiki/fontes/solomon-2016-observer-models.md`
- Criadas páginas de conceito em `wiki/conceitos/`: [[Índice de Detectabilidade|detectability-index]], [[Observadores de Modelo (Model Observers)|model-observers]], [[Contrast To Noise Ratio|contrast-to-noise-ratio]]
- Criada página de tecnologia na raiz: [[ADMIRE (Advanced Modeled Iterative Reconstruction)|admire-reconstruction]]

---

## [2026-08-23] ingest | Model observers and detectability index in x-ray imaging: historical review, applications and future trends
- **Fonte processada:** `DOC-20250401-WA0005. (1) - Adobe cloud storage.md`
- Ingestão concluída da fonte 'model-observers-and-detectability-index-in-x-ray-imaging'.
- Criada a ficha analítica da fonte em wiki/fontes/.
- Criadas/atualizadas 3 páginas do tipo 'conceito' em wiki/conceitos/: [[Índice de Detectabilidade|indice-de-detectabilidade]], [[Observadores de Modelo (Model Observers)|observadores-de-modelo]], [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]].
- Catálogo index.md e diário log.md marcados para atualização.

---

## [2026-08-23] ingest | Model observers and detectability index in x-ray imaging: historical review, applications and future trends
- **Fonte processada:** `Model observers and detectability index in x-ray imaging historical review, applications and future trends.md`
- Fonte processada: Model observers and detectability index in x-ray imaging: historical review, applications and future trends
- Páginas criadas: wiki/fontes/model-observers-detectability-index-xray.md, wiki/detectability-index.md, wiki/model-observers.md

---

## [2026-08-23] ingest | Performance evaluation of computed tomography systems: Summary of AAPM Task Group 233
- **Fonte processada:** `Performance evaluation of computed tomography systems Summary of AAPM Task Group 233.md`
- Fonte processada: raw/Performance evaluation of computed tomography systems Summary of AAPM Task Group 233.md
- Ficha de fonte gerada: wiki/fontes/aapm-tg-233-summary.md
- Conceitos criados em wiki/conceitos/: ttf-task-transfer-function, indice-de-detectabilidade, espectro-de-potencia-de-ruido-nps
- Tecnologia criada em wiki/: controle-automatico-de-exposicao-ct

---

## [2026-08-23] ingest | Comprehensive Assessment of CT Performance: AAPM Task Group 233 Report
- **Fonte processada:** `AAPM Journal  Wiley Online Library.md`
- Fonte processada: raw/AAPM Journal  Wiley Online Library.md
- Páginas criadas: wiki/fontes/aapm-tg233-ct-performance.md, wiki/reconstrucao-iterativa.md, wiki/controle-automatico-exposicao.md, wiki/task-transfer-function.md, wiki/noise-power-spectrum.md, wiki/detectabilidade-index.md

---

## [2026-08-23] ingest | Dual-Filament 3D Printing of Patient-Specific CT Phantoms with Embedded Implants and Tunable Metal-Artifact Intensity
- **Fonte processada:** `2026.07.17.26358319v1.full.pdf`
- Fonte processada: dual-filament-3d-printing-ct-phantoms-pasyar-2026.md
- Páginas de conceitos criadas na raiz: pixelprint.md, impressao-3d-duplo-filamento.md, metrica-gumbel-p-index.md
- Atualização do index.md e log.md realizada com sucesso.

---

## [2026-08-23] ingest | Image quality in modern CT imaging: optimization and quantification
- **Fonte processada:** `2026_Image quality in modern CT imaging.pdf`
- Fonte processada: 2026_Image quality in modern CT imaging.pdf (Tese de Doutorado de Eva J. I. Hoeijmakers, Maastricht University)
- Ficha analítica criada: wiki/fontes/hoeijmakers-2026-image-quality-modern-ct.md
- Páginas de conceito/tecnologia criadas/atualizadas:
  - wiki/photon-counting-detector-ct.md (tipo: tecnologia)
  - wiki/conceitos/virtual-monoenergetic-imaging.md (tipo: conceito)
  - wiki/conceitos/otimizacao-meio-de-contraste-tc.md (tipo: conceito)
  - wiki/conceitos/avaliacao-pareada-qualidade-imagem.md (tipo: conceito)
  - wiki/conceitos/metricas-objetivas-qualidade-imagem-tc.md (tipo: conceito)

---

## [2026-08-23] ingest | Projeto FAPESP Doutorado Direto - Observadores de Aprendizado Profundo para Otimização de Protocolos de TC
- **Fonte processada:** `1408_RASCUNHO_Projeto_DD_FAPESP_Wagner.md`
- Fonte processada: `raw/1408_RASCUNHO_Projeto_DD_FAPESP_Wagner.md`
- Ficha analítica criada: `wiki/fontes/projeto-dd-fapesp-wagner-2026.md`
- Conceitos extraídos e criados:
  - `wiki/task-based-image-quality.md` (tipo: conceito)
  - `wiki/detectability-index.md` (tipo: conceito)
  - `wiki/deep-learning-model-observer.md` (tipo: tecnologia)
  - `wiki/otimizacao-multiobjetivo-tc.md` (tipo: conceito)
  - `wiki/phantoms-hibridos.md` (tipo: tecnologia)

---

## [2026-08-23] refactor | USP/TCC - Modelos perceptivos.md
- **Ação:** Enriquecimento e linkagem interna da nota de TCC com a LLM Wiki.
- **Conceitos e Tecnologias Conectados:**
  - [[Observadores de Modelo (Model Observers)|observadores-de-modelo]], [[Observadores de Modelo (Model Observers)|model-observers]], [[Teoria de Detecção de Sinais|teoria-de-deteccao-de-sinais]], [[Índice de Detectabilidade|indice-de-detectabilidade]] ($d'$).
  - [[Task Transfer Function|task-transfer-function]] (TTF), [[Noise Power Spectrum|noise-power-spectrum]] (NPS), [[Contrast To Noise Ratio|contrast-to-noise-ratio]].
  - [[Task Based Image Quality|task-based-image-quality]], [[Otimização de Dose em TC|otimizacao-de-dose-em-tc]], [[Métricas de Dose em TC|metricas-de-dose-tc]] ($CTDI_{vol}$).
  - [[Reconstrução Iterativa|reconstrucao-iterativa]] (HIR, MBIR, DLR), [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]] / [[Photon Counting Detector CT (PCD-CT)|photon-counting-ct]].
  - [[Deep Learning Model Observer|deep-learning-model-observer]], [[Otimização Multiobjetivo em TC|otimizacao-multiobjetivo-tc]], [[Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)|avaliacao-pareada-qualidade-imagem]] (2AFC).
  - [[Phantoms Híbridos|phantoms-hibridos]], [[Impressão 3D com Duplo Filamento|impressao-3d-duplo-filamento]], [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]], [[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]].
- **Sincronização:** Atualizado no Obsidian Vault (`USP/TCC - Modelos perceptivos.md`).

---

## [2026-08-25] ingest | Artificial intelligence-powered biomedical imaging: Recent achievements and challenges
- **Fonte processada:** `Artificial intelligence-powered biomedical imaging Recent achievements and challenges.md`
- Ingestão da fonte: Artificial intelligence-powered biomedical imaging (Wong, 2026)
- Ficha da fonte criada em wiki/fontes/wong-2026-ai-biomedical-imaging.md
- Conceitos compilados: generalist-medical-ai, explainable-ai-em-imagem-medica, modos-de-integracao-de-ia-clinica, aprendizado-federado-e-privacidade-em-imagem-medica

---

## [2026-08-25] ingest | Anticipating Moral and Economic Considerations, Opportunities, and Potential Frictions for AI in Medical Imaging: Multistakeholder Cocreation Study
- **Fonte processada:** `Anticipating Moral and Economic Considerations, Opportunities, and Potential Frictions for AI in Medical Imaging Multistakeholder Cocreation Study.md`
- Fonte processada: schilder-2026-anticipating-ai-medical-imaging.md
- Criada ficha analítica em wiki/fontes/schilder-2026-anticipating-ai-medical-imaging.md
- Páginas de conceitos criadas: inovacao-responsavel-em-saude (wiki/conceitos/), triagem-e-rastreamento-extramural-ia (wiki/conceitos/)
- Página de tecnologia criada: tecnologia-ia-copilot-radiologia (wiki/ - solta na raiz por ser < 3 páginas)

---

## [2026-08-25] ingest | Deep-learning image reconstruction algorithms for CT: A task-based image quality assessment of four CT systems using a phantom
- **Fonte processada:** `Deep-learning image reconstruction algorithms for CT A task-based image quality assessment of four CT systems using a phantom.md`
- Fonte processada: `Deep-learning image reconstruction algorithms for CT A task-based image quality assessment of four CT systems using a phantom.md`
- Ficha da fonte criada: `wiki/fontes/greffier-2026-dlr-ct-phantom.md`
- Páginas de conceitos criadas: `wiki/conceitos/task-based-image-quality.md`, `wiki/conceitos/noise-power-spectrum.md`, `wiki/conceitos/detectability-index.md`
- Página de tecnologia criada na raiz: `wiki/deep-learning-image-reconstruction.md`

---

## [2026-08-25] ingest | Artificial intelligence in medical physics - La Rivista del Nuovo Cimento
- **Fonte processada:** `Artificial intelligence in medical physics - La Rivista del Nuovo Cimento.md`
- Fonte processada: Artificial intelligence in medical physics - La Rivista del Nuovo Cimento
- Páginas criadas: wiki/fontes/artificial-intelligence-in-medical-physics-nuovo-cimento.md, wiki/fisica-medica.md, wiki/inteligencia-artificial-em-saude.md, wiki/radioterapia-e-dosimetria.md

---

## [2026-08-25] query | O Índice de Detectabilidade ($d'$) em Tomografia Computadorizada: Fundamentação, Métricas e Formulação Matemática
- Consulta processada: `queries/o que é índice de detectabilidade e como ele pode ser calculado ?.md`
- Síntese gerada: `wiki/sinteses/indice-de-detectabilidade-em-tomografia-computadorizada.md`

---

## [2026-08-25] query | Estado da Arte e Estratégias de Otimização no Projeto de Doutorado em Física Médica e Tomografia Computadorizada
- Consulta processada: `Qual é o estado da arte das tecnologias que envolvem meu trabalho de doutorado e como elas podem ser otimizadas ?.md`

---

## [2026-08-25] query | Evolução dos Modelos de Observadores Computacionais e Mitigação da Não-Linearidade em Tomografia Computadorizada
- Consulta processada via atalho: `Comente sobre a evolução dos modelos de observadores computacionais. Preciso entender como se deu o avanço, como cada um deles complementa o outro e como posso melhorar a questao da não-linearidade.md`

---

## [2026-08-25] query | Mapeamento e Análise Frequencial de Termos, Conceitos e Wikilinks na LLM Wiki
- Consulta processada via atalho: `quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md`

---

## [2026-08-25] query | Roteiro Estruturado para o Desenvolvimento e Calibração de Observadores de Aprendizado Profundo (DLMO) em Tomografia Computadorizada
- Consulta processada sobre estruturação e roadmap de desenvolvimento de Observadores-Modelo de Aprendizado Profundo (DLMO).

---

## [2026-08-25] query | Capacidade de Ingestão e Obtenção de Informações Externas na Arquitetura da LLM Wiki
- Consulta processada via atalho: `você tem a capacidade de obter informações por meio de fontes que não estão na pasta raw?.md`

---

## [2026-08-25] query | Limites Epistemológicos e Operacionais da LLM Wiki: Imutabilidade do Raw e Conhecimento Paramétrico vs. Documental
- Consulta processada via atalho: `você tem a capacidade de obter informações por meio de fontes que não estão na pasta raw?.md`

---

## [2026-08-25] query | Funcionamento, Formulação Matemática e Aplicação do Espectro de Potência do Ruído (NPS) em Tomografia Computadorizada
- Consulta processada e sintetizada via atalho de pesquisa: `Como funciona o NPS?.md`

---

## [2026-08-25] query | Task Transfer Function (TTF): Fundamentação, Importância e Aplicação em Tomografia Computadorizada
- Consulta processada via atalho: `O que é ttf e porque ele é importante?.md`

---

## [2026-08-25] query | O Diferencial do Detector de Contagem de Fótons (PCD-CT) e seu Impacto no Avanço da Tomografia Computadorizada
- Consulta processada via atalho de pesquisa e síntese wiki: `qual é o diferencial do photon counting detector e como ele pode contribuir para o avanço da tomografia computadorizada?.md`

---

## [2026-08-25] query | O que são Phantoms em Imagem Médica e Tomografia Computadorizada
- Consulta processada e sintetizada: `O que são phantoms ?`

---

## [2026-08-25] query | O Arcabouço PixelPrint e a Impressão 3D de Duplo Filamento em Fantomas de Tomografia Computadorizada
- Consulta processada via atalho: `O que é pixel print ?.md`

---

## [2026-08-25] query | Complementaridade Estrutural entre o Projeto de Doutorado Direto, o Projeto AIR e o Universal CNPq na Tomografia Computadorizada
- Consulta processada via atalho: `o que o projeto de doutorado complementa o projeto AIR e o universal CNPQ?.md`

---

## [2026-08-25] query | As Grandes Áreas da Física Médica: Fundamentação, Domínios de Atuação e Metrologia
- Consulta processada via atalho: `Quais são as grandes áreas da física médica ?.md`

---

## [2026-08-25] query | Fundamentos Físicos e Formulação Matemática da Tomografia Computadorizada
- Consulta processada via atalho: `como funciona a física da tomografia computadorizada? mencione equações.md`

---

## [2026-08-26] query | Raios X: Fundamentos Físicos, Mecanismos de Interação e Aplicações em Tomografia Computadorizada
- Consulta processada via atalho RAG: `O que é raios X ?.md`

---

## [2026-08-26] query | Fundamentos Físicos, Produção e Aplicações dos Raios X em Física Médica e Tomografia Computadorizada
- Consulta processada via atalho RAG: `O que é raios X ?.md`

---

## [2026-08-26] query | Influência da Tensão de Tubo nas Unidades Hounsfield em Tomografia Computadorizada
- Consulta processada via atalho RAG: `Qual a influencia da tensão de tubo no HU ?.md`

---

## [2026-08-26] query | Validação Científica de Observadores-Modelo de Aprendizado Profundo (DLMO) na Literatura de Tomografia Computadorizada
- Consulta processada via atalho RAG: `Já existe DLMO validado na literatura ?.md`

---

## [2026-08-26] query | O Relatório ICRU 95: Fundamentos Metrológicos e Diretrizes para Dosimetria e Qualidade de Imagem em Imagem Médica
- Consulta processada via atalho RAG: `o que é dito no ICRU 95?.md`

---

## [2026-08-26] query | Relatório ICRU 95: Novas Grandezas Operacionais para Proteção Radiológica contra Exposição Externa
- Consulta processada via atalho RAG: `o que é dito no ICRU 95?.md`

---

## [2026-08-26] query | ICRU Report 95: Redefinição das Grandezas Operacionais em Proteção Radiológica
- Consulta processada via atalho RAG: `o que é dito no ICRU 95?.md`

---

## [2026-08-26] query | Observadores-Modelo de Aprendizado Profundo com Mecanismos de Atenção para Estimativa do Índice de Detectabilidade
- Consulta processada via atalho RAG: `Já há na literatua moderna um Observador-Modelo de Aprendizado Profundo com mecanismos de atenção para estimar o Índice de Detectabilidade?.md`

---

## [2026-08-26] query | Observadores-Modelo de Aprendizado Profundo (DLMO) com Mecanismos de Atenção para Estimativa de Detectabilidade em TC
- Consulta processada via atalho RAG: `Já há na literatua moderna um Observador-Modelo de Aprendizado Profundo com mecanismos de atenção para estimar o Índice de Detectabilidade?.md`

---

## [2026-08-27] query | Chamada Universal CNPq: Estrutura, Objetivos e Aplicação na Física Médica
- Consulta processada via atalho RAG: `Do que se trata o projeto universal CNPQ? Dê detalhes..md`

---

## [2026-08-27] query | Surgimento e Evolução Histórica da Tomografia Computadorizada
- Consulta processada via atalho RAG: `Quando surgiu a tomografia computadorizada?.md`

---

## [2026-08-27] query | Surgimento e Evolução Histórica da Tomografia Computadorizada
- Consulta processada via atalho RAG: `Surgimento da Tomografia Computadorizada.md`

---

## [2026-08-27] query | Surgimento e Evolução Histórica da Tomografia Computadorizada
- Consulta processada via atalho RAG: `Quando surgiu a tomografia computadorizada?.md`

---

## [2026-08-29] query | The spelled-out intro to neural networks and backpropagation: building micrograd
- Vídeo do YouTube interpretado in-place: `The spelled-out intro to neural networks and backpropagation: building micrograd` (ID: `VMj-3S1tku0`)
- Resumo técnico e mapeamento matemático realizados com sucesso sob as diretrizes do SPARK.md.

---

## [2026-08-29] query | Um panorama da IA Generativa no Brasil e no Mundo: Presente e Futuro
- Vídeo do YouTube interpretado in-place: `Um panorama da IA Generativa no Brasil e no Mundo: Presente e Futuro` (ID: nXzUAubH8kg).

---

## [2026-08-29] query | Aplicação da Biblioteca OpenCV em Visão Computacional e Física Médica
- Consulta processada via atalho RAG: `para que serve a biblioteca OpenCV?.md`

---

## [2026-09-03] query | Dataset de Phantoms de Textura em TC com Avaliações Pareadas de Qualidade de Imagem para Imagem Quantitativa
- Consulta processada via atalho RAG: `faça um resumo sobre CT texture phantom dataset with paired image quality assessments for quantitative imaging`
- Unificação de taxonomia canônica: [[Phantoms Híbridos]], [[Índice de Detectabilidade]], [[Noise Power Spectrum]], [[Task Transfer Function]], [[Deep Learning Image Reconstruction (DLR)]].

---

## [2026-09-03] query | CT Texture Phantom Dataset e Avaliações Pareadas de Qualidade de Imagem
- Consulta processada via atalho RAG: `faça um resumo sobre CT texture phantom dataset with paired image quality assessments for quantitative imaging.md`

---

## [2026-09-03] query | CT Texture Phantom Dataset with Paired Image Quality Assessments for Quantitative Imaging
- Consulta processada via atalho RAG: `faça um resumo sobre o anexo 'CT texture phantom dataset with paired image quality assessments for quantitative imaging'`

---

## [2026-09-08] query | SSW-d' (Índice de Detectabilidade Ponderado por Cortes / Espaço-Espectral)
- Consulta processada via atalho RAG: `o que é SSW-d'?.md`

---

## [2026-09-13] query | Síntese do Artigo: Inteligência Artificial em Física Médica (Nuovo Cimento 2025)
- Consulta processada via atalho RAG: `resumo do último artigo anexado (Amoroso et al., 2025)`

---

## [2026-09-13] query | Avaliação Baseada em Tarefas de Algoritmos de Deep Learning Image Reconstruction (DLR) em Tomografia Computadorizada
- Consulta processada via RAG semântico híbrido: recuperação de `wiki/fontes/Greffier 2026 - Avaliação de DLR em TC com Phantoms.md` com score 0.48.

---

## [2026-09-18] query | Otimização de Protocolos de TC Baseada em Tarefas Utilizando Aprendizado por Reforço e Ensaios de Imagem Virtuais
- Consulta processada via atalho RAG: `vc tem acesso ao trabalho Task-Based CT Protocol Optimization Using Reinforcement Learning and Virtual Imaging Trials?.md`