> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]], [[Photon Counting Detector CT (PCD-CT)]], [[Deep Learning Image Reconstruction (DLR)]]

## 1. Visão Geral e Estatísticas do Acervo

A análise sistemática de todo o acervo da **LLM Wiki de Física Médica & Tomografia Computadorizada** revela uma estrutura altamente conectada e hiperlinkada. O acervo conta atualmente com **57 documentos markdown**\, distribuídos em 4 pilares taxonômicos principais de acordo com o esquema `SPARK.md`:

* **Páginas de Conceito (`wiki/conceitos/`):** 34 páginas (Métricas, modelos matemáticos, grandezas físicas e princípios de IA);
* **Páginas de Fonte (`wiki/fontes/`):** 13 páginas (Fichas analíticas de teses, artigos e relatórios de força-tarefa);
* **Páginas de Tecnologia (`wiki/tecnologias/`):** 8 páginas (Sistemas de hardware, algoritmos comerciais e simuladores);
* **Páginas de Síntese (`wiki/sinteses/`):** 1 página (Compilações transversais integradas);
* **Configuração e Metadados (`configAG/`):** Esquema e registros do agente.

---

## 2. Top 10 Termos e Conceitos Mais Frequentes

Abaixo apresenta-se o ranqueamento dos termos e conceitos com maior frequência de citação, co-ocorrência em tags e densidade de wikilinks (``) em toda a base de conhecimento:

| Ranks  | Termo / Conceito                                             | Wikilinks Associados                                                                                        |                                 Frequência Relativa                                  | Eixo Temático Dominante             |                                        |
| :----: | :----------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------: | :---------------------------------- | -------------------------------------- |
| **1**  | **Índice de Detectabilidade ($d'$)**                         | `[[indice-de-detectabilidade|detectability-index]]`, `[[Índice de Detectabilidade]]`, `[[detectabilidade-index]]` | **Muito Alta** ($\ge 25$ ref.)      | Qualidade de Imagem Baseada em Tarefas |
| **2**  | **TC por Contagem de Fótons (PCD-CT)**                       | `[[photon-counting-detector-ct|photon-counting-ct]]`, `[[Photon Counting Detector CT (PCD-CT)]]`               | **Muito Alta** ($\ge 20$ ref.)      | Hardware & Imagem Espectral            |
| **3**  | **Observadores de Modelo (*Model Observers*)**               | `[[model-observers]]`, `[[model-observers|observadores-de-modelo]]`, `[[deep-learning-model-observer]]`             | **Alta** ($\ge 18$ ref.)            | Avaliação Psicofísica e SDT            |
| **4**  | **Reconstrução por Deep Learning (DLR) e Iterativa (IR)**    | `[[Deep Learning Image Reconstruction (DLR)]]`, `[[reconstrucao-iterativa]]`, `[[admire-reconstruction]]`         |                               **Alta** ($\ge 16$ ref.)                               | Reconstrução de Imagem              |                                        |
| **5**  | **Espectro de Potência de Ruído (NPS)**                      | `[[Noise Power Spectrum]]`, `[[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]]`                         | **Alta** ($\ge 15$ ref.)            | Textura e Metrologia do Ruído          |
| **6**  | **Task Transfer Function (TTF)**                             | `[[Task Transfer Function]]`, `[[task-transfer-function|ttf-task-transfer-function]]`, `[[task-based-image-quality]]`             | **Alta** ($\ge 15$ ref.)            | Resolução Espacial Não-Linear          |
| **7**  | **Dosimetria e Métricas de Dose ($CTDI_{vol}$, $DLP$, DRL)** | `[[metricas-de-dose-tc]]`, `[[otimizacao-de-dose-em-tc]]`, `[[niveis-de-referencia-diagnostica-drl]]`       |                               **Alta** ($\ge 14$ ref.)                               | Dosimetria & Radioproteção          |                                        |
| **8**  | **Virtual Monoenergetic Imaging (VMI)**                      | `[[virtual-monoenergetic-imaging]]`, `[[otimizacao-meio-de-contraste-tc]]`                                  |                            **Média-Alta** ($\ge 12$ ref.)                            | TC Espectral e Agentes de Contraste |                                        |
| **9**  | **Inteligência Artificial & XAI**                            | `[[generalist-medical-ai]]`, `[[explainable-ai-em-imagem-medica]]`, `[[modos-de-integracao-de-ia-clinica]]` |                            **Média-Alta** ($\ge 11$ ref.)                            | Aprendizado Profundo e Governança   |                                        |
| **10** | **Phantoms Híbridos & PixelPrint (3D)**                      | `[[phantoms-hibridos]]`, `[[pixelprint]]`, `[[impressao-3d-duplo-filamento]]`                               |                               **Média** ($\ge 8$ ref.)                               | Instrumentação e Manufatura Aditiva |                                        |

---

## 3. Estrutura dos Clusters Temáticos Principais

Os termos mais frequentes organizam-se em **5 grandes clusters do conhecimento**, que representam os eixos de pesquisa mantidos na wiki:

### Cluster 1: Qualidade de Imagem Baseada em Tarefas (*Task-Based Image Quality*)
* **Termos Núcleo:** [[indice-de-detectabilidade|detectability-index]] ($d'$), [[Task Transfer Function]] (TTF), [[Noise Power Spectrum]] (NPS), [[model-observers]] (NPW, NPWE, CHO).
* **Contexto:** Constitui o referencial metrológico central da base, fundamentado no relatório AAPM TG-233 ([[aapm-tg233-ct-performance]]). Substitui métricas pixel-a-pixel tradicionais, como o [[contrast-to-noise-ratio]] (CNR), na avaliação de sistemas não-lineares.

### Cluster 2: Avanços em Detectores e Reconstrução em TC
* **Termos Núcleo:** [[Photon Counting Detector CT (PCD-CT)]] (PCD-CT), [[virtual-monoenergetic-imaging]] (VMI), [[Deep Learning Image Reconstruction (DLR)]] (DLR), [[reconstrucao-iterativa]] (IR).
* **Contexto:** Abrange as inovações tecnológicas de ponta na física da imagem\, destacando a conversão direta de fótons ( CdTe/CZT ) e o treinamento de redes neurais profundas para preservação de textura de ruído e redução drástica de dose.

### Cluster 3: Dosimetria, Otimização e Proteção Radiológica
* **Termos Núcleo:** [[metricas-de-dose-tc]] ($CTDI_{vol}$, $DLP$), [[niveis-de-referencia-diagnostica-drl]], [[otimizacao-de-dose-em-tc]], [[risco-oncologico-radiacao-tc]].
* **Contexto:** Examina a tendência histórica de redução de doses (estudo McCollough, 2026), estratégias de calibração de [[controle-automatico-de-exposicao-ct]] (AEC) e a revisão de riscos epidemiológicos populacionais.

### Cluster 4: Inteligência Artificial, Modelos de Fundação e Governança Clínica
* **Termos Núcleo:** [[generalist-medical-ai]] (GMAI), [[explainable-ai-em-imagem-medica]] (XAI / Grad-CAM / CBM), [[modos-de-integracao-de-ia-clinica]], [[inovacao-responsavel-em-saude]] (RRI).
* **Contexto:** Cobre a transição de modelos dedicados para modelos generalistas e copilotos radiológicos ([[tecnologia-ia-copilot-radiologia]]), com foco em interpretabilidade pós-hoc e preservação da privacidade via [[aprendizado-federado-e-privacidade-em-imagem-medica]].

### Cluster 5: Fantomas Customizados, Metrologia e Impressão 3D
* **Termos Núcleo:** [[phantoms-hibridos]], [[pixelprint]], [[impressao-3d-duplo-filamento]], [[metrica-gumbel-p-index]].
* **Contexto:** Foca no desenvolvimento e fabricação de simuladores físicos antropomórficos e geométricos para validação psicofísica via estudos [[2afc-observer-study]] e mitigação de artefatos metálicos.

---

## 4. Análise Frequencial das Tags YAML

Ao verificar o frontmatter YAML de todos os arquivos, as *tags* mais recorrentes são:

1. `tomografia-computadorizada` / `ct` / `tecnologia-tc` ($\sim 22$ arquivos)
2. `dosimetria` / `fisica-medica` ($\sim 18$ arquivos)
3. `qualidade-de-imagem` / `image-quality` ($\sim 16$ arquivos)
4. `photon-counting` / `photon-counting-ct` ($\sim 12$ arquivos)
5. `model-observers` / `detectabilidade` ($\sim 11$ arquivos)
6. `inteligencia-artificial` / `ai` / `deep-learning` ($\sim 10$ arquivos)

---

## 5. Conclusão e Recomendações de Crescimento Orgânico

O mapeamento revela que a arquitetura da wiki está madura e bem fundamentada em **Física da TC**, **Qualidade Baseada em Tarefas** e **Inteligência Artificial**. 

Conforme estipulado no esquema `SPARK.md` (Regra dos 3+), a atribuição rigorosa do campo `tipo:` permitiu a consolidação orgânica das subpastas `wiki/conceitos/`, `wiki/fontes/` e `wiki/tecnologias/`. Recomenda-se manter o nascimento de novos artigos conceituais e tecnológicos na raiz até que novos tipos (como `sintese` ou `algoritmo`) atinjam o limiar de 3 páginas para criação de novas subpastas físicas.
