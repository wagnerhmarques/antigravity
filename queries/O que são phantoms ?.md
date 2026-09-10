> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Phantoms Antropomórficos]], [[Impressão 3D com Duplo Filamento]], [[Phantoms Híbridos]], [[Pixelprint]], [[Controle de Qualidade em TC]]

## 1. Definição e Papel Fundamental em Física Médica

Os **phantoms** (ou simuladores antropomórficos e geométricos) são dispositivos físicos desenvolvidos para reproduzir com alta fidelidade as propriedades de atenuação radiológica\, densidade e características geométricas dos tecidos biológicos humanos. Na [[fisica-medica]] e na [[Tomografia Computadorizada]], os phantoms são instrumentos indispensáveis para o controle de qualidade, metrologia radiológica, calibração de dosimetria ([[metricas-de-dose-tc]]) e validação de algoritmos avançados de reconstrução ([[reconstrucao-iterativa]] e [[Deep Learning Image Reconstruction (DLR)]]).

A utilização de phantoms elimina a necessidade de expor pacientes ou animais a testes de radiação ionizante repetidos, permitindo avaliar de forma padronizada e reprodutível o desempenho físico do sistema de imagem, tais como a resolução espacial ([[Task Transfer Function]]), a textura do ruído ([[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]]) e a detectabilidade de lesões ([[Índice de Detectabilidade]]).

---

## 2. Taxonomia e Classificação dos Phantoms

Os phantoms utilizados em radiologia diagnóstica e tomografia computadorizada dividem-se em três grandes categorias operacionais:

| Categoria | Descrição Estrutural | Aplicação Principal | Exemplo na Wiki |
| :--- | :--- | :--- | :--- |
| **Geométricos / Homogêneos** | Cilindros ou blocos padronizados de materiais uniformes (ex.: PMMA, polietileno) | Medição de ruído global, uniformidade, número de Hounsfield e perﬁs de dose | Cilindros QA de 16/32 cm |
| **Antropomórficos Clássicos** | Moldes plásticos preenchidos com materiais tecido-equivalentes simulando órgãos | Avaliação anatômica qualitativa e estimativa de dose absorvida em órgãos | Fantomas de tórax e abdome comerciais |
| **Híbridos / Impressos em 3D** | Estruturas modulares combinando geometrias metrológicas e parênquima complexo | Validação de [[task-based-image-quality]] e estudos psicofísicos | [[phantoms-hibridos]] / [[pixelprint]] |

---

## 3. Avanços Tecnológicos: Impressão 3D e Fantomas Específicos para Pacientes

Com o avanço da manufatura aditiva na física médica, os phantoms estáticos tradicionais vêm sendo substituídos por modelos avançados personalizados:

- **Arcabouço [[pixelprint]]:** Permite converter diretamente imagens clínicas DICOM em código geométrico de impressão 3D (G-code) sem intermediários de malha de superfície, preservando a textura original do voxel do paciente.
- **[[impressao-3d-duplo-filamento]]:** Técnica que emprega deposição voxel a voxel intercalada de dois materiais distintos, como filamentos de ácido polilático (PLA) dopados com cálcio (para tecidos moles e osso trabecular) e PLA dopado com metal (para simulação de implantes ortopédicos e estudo de [[reducao-de-artefatos-metalicos]]).
- **Quantificação de Artefatos:** O uso de phantoms com implantes metálicos embutidos permite avaliar com rigor métricas objetivas como o [[metrica-gumbel-p-index]], quantificando a severidade de estrias de endurecimento de feixe sem viés de operador.

---

## 4. Aplicação em Estudos Psicofísicos e Observadores de Modelo

Phantoms modernos — em especial os [[phantoms-hibridos]] desenvolvidos em centros de pesquisa como a USP/FAPESP ([[projeto-dd-fapesp-wagner-2026]]) — servem de base para ensaios [[2afc-observer-study]] com radiologistas e calibração de [[deep-learning-model-observer]]. Ao submeter o phantom a diferentes níveis de dose e algoritmos não-lineares, pesquisadores mapeiam a fronteira entre a dose aplicada e o [[Índice de Detectabilidade]], otimizando protocolos clínicos sob o princípio ALARA.

## 🔗 Conexões e Referências na Wiki
- [[phantoms-hibridos]]
- [[pixelprint]]
- [[impressao-3d-duplo-filamento]]
- [[metrica-gumbel-p-index]]
- [[task-based-image-quality]]
- [[Índice de Detectabilidade]]
