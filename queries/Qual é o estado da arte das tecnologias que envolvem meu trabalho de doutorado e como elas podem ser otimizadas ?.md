> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Photon Counting Detector CT (PCD-CT)]], [[Deep Learning Image Reconstruction (DLR)]], [[Deep Learning Model Observer]], [[Otimização Multiobjetivo em TC]], [[Phantoms Híbridos]]

## 1. Visão Geral e Alinhamento do Projeto
O projeto de Doutorado Direto (`[[projeto-dd-fapesp-wagner-2026]]`) foca na intersecção entre a **física médica metrológica**, a **inteligência artificial aplicada** e a **otimização operacional em Tomografia Computadorizada (TC)**. O objetivo central é desenvolver e validar um Observador-Modelo de Aprendizado Profundo (`[[deep-learning-model-observer]]` - DLMO) com mecanismos de atenção para estimar o Índice de Detectabilidade (`[[indice-de-detectabilidade|detectability-index]]` / $d'$) em cenários de alta não-linearidade, calibrado via testes psicofísicos (`[[2afc-observer-study]]`) em `[[phantoms-hibridos]]` antropomórficos, integrando-o a um arcabouço de `[[otimizacao-multiobjetivo-tc]]` no espaço de Pareto.

---

## 2. Estado da Arte das Tecnologias Envolvidas

### A. Reconstrução de Imagem Baseada em Deep Learning (`[[Deep Learning Image Reconstruction (DLR)]]` - DLR)
* **Panorama Atual:** A DLR representa a terceira geração de algoritmos de reconstrução (sucedendo a FBP e a `[[reconstrucao-iterativa]]` - IR). Algoritmos comerciais de ponta (como AiCE, TrueFidelity, Precise Image e DELTA) empregam redes neurais profundas (DNNs/CNNs) treinadas com vastos bancos de dados clínicos e phantoms.
* **Desempenho Metrológico:** Conforme demonstrado por `[[greffier-2026-dlr-ct-phantom]]`, a DLR supera as limitações da IR ao reduzir a magnitude do ruído (até $-83,8\%$ em ultrabaixa dose) mantendo a frequência espacial média ($f_{av}$) do `[[Noise Power Spectrum]]` (NPS) em níveis elevados. Isso preserva a textura de ruído natural e eleva drasticamente o índice $d'$ sem o aspecto borrado ou "plástico" característico da IR.

### B. Detectores de Contagem de Fótons (`[[Photon Counting Detector CT (PCD-CT)]]` / `[[photon-counting-detector-ct|photon-counting-ct]]` - PCD-CT)
* **Paradigma Instrumental:** Substituição dos detectores cintiladores convencionais de integração de energia (EID) por semicondutores de conversão direta (CdTe/CZT).
* **Vantagens Clicadas e Dosimétricas:**
  1. Eliminação total do ruído eletrônico via *energy thresholding*;
  2. Resolução espacial sub-milimétrica nativa;
  3. Capacidade de `[[virtual-monoenergetic-imaging]]` (VMI) em todas as varreduras, permitindo reduções substanciais da carga total de iodo ($20\%$ a $27\%$) e da dose de radiação ($CTDI_{vol}$ reduzido em $>24\%$), conforme comprovado em `[[hoeijmakers-2026-image-quality-modern-ct]]` e contextualizado em `[[mccollough-2026-good-news-ct-doses]]`.

### C. Observadores-Modelo de Aprendizado Profundo (`[[deep-learning-model-observer]]` - DLMO)
* **Superação dos Modelos Lineares:** Observadores clássicos como `[[npwe-model-observer]]` e `[[cho-model-observer]]` (`[[solomon-2016-observer-models]]`, `[[aapm-tg233-ct-performance]]`) assumem linearidade e estacionaridade de ruído. Em sistemas com DLR e reconstrução adaptativa, essas premissas falham.
* **Arquiteturas de Ponta:** O estado da arte emprega Vision Transformers (ViTs) e CNNs com mecanismos de atenção contextual, treinados para estimar diretamente a detectabilidade humana em anatomias complexas e heterogêneas (`[[wong-2026-ai-biomedical-imaging]]`).

### D. Avaliação Antropomórfica com `[[phantoms-hibridos]]` e Manufatura Aditiva
* **Design Modular:** Combinação de geometria analítica para extração de NPS/TTF com anatomia antropomórfica impressa em 3D (`[[impressao-3d-duplo-filamento]]`, `[[pixelprint]]`). Permite reproduzir o ruído estrutural de órgãos (fígado, pulmão, crânio) e inserir lesões simuladas para estudos `[[2afc-observer-study]]` sem submeter pacientes a exames repetidos.

### E. Otimização Multiobjetivo da Tríade $(D, T, -W)$ (`[[otimizacao-multiobjetivo-tc]]`)
* **Formulação Matemática:** Modelação formal do trade-off entre Dose de Radiação ($D$: `[[metricas-de-dose-tc]]` $CTDI_{vol}$/DLP), Tempo Operacional ($T$) e Desempenho na Tarefa Diagnóstica ($W$: $d'$ ou AUC):

$$
\min_{\mathbf{p} \in \Omega} \Big( D(\mathbf{p}), T(\mathbf{p}), -W(\mathbf{p}) \Big)
$$

* **Fronteira de Pareto:** Uso de algoritmos evolutivos elitistas (`[[nsga-ii]]`) combinados a modelos substitutos por Processos Gaussianos e retenção por $\varepsilon$-dominância para acomodar incertezas metrológicas.

---

## 3. Diretrizes para Otimização e Avanço Metodológico do Projeto

Para maximizar o impacto científico e a aplicabilidade clínica do seu trabalho, as seguintes estratégias de otimização devem ser implementadas:

### 1. Calibração e Validação Psicofísica Rigorosa do DLMO
* **Estudos 2AFC Robustos:** Conduzir ensaios de escolha forçada entre duas alternativas (`[[2afc-observer-study]]`) com pelo menos 20 radiologistas especialistas por anatomia (tórax, abdome, crânio), calculando a concordância via Coeficiente de Correlação Intraclasse (ICC) e curvas ROC/AUC.
* **Ajuste Fino Perceptual:** Calibrar as saídas do DLMO contra a matriz de respostas humanas para assegurar que a rede capture o filtro ocular e o ruído interno da visão humana em tarefas de baixo e alto contraste.

### 2. Automação e Padronização Metrológica (NPS, TTF, d')
* **Pipeline Automatizado:** Implementar algoritmos de segmentação automática de regiões de interesse (ROIs) em tecidos homogêneos e bordas anatômicas para dispensar a seleção manual de ROIs.
* **Verificação de Reprodutibilidade:** Assegurar que os cálculos de `[[Noise Power Spectrum]]` (NPS) e `[[Task Transfer Function]]` (TTF) atinjam nível de reprodutibilidade elevado ($\text{ICC} \ge 0{,}90$), conforme os critérios do `[[aapm-tg233-ct-performance]]`.

### 3. Transferibilidade Inter-Fabricantes (*Leave-One-Scanner-Out*)
* **Generalização de Modelos:** Avaliar a robustez do DLMO e das soluções da Fronteira de Pareto em múltiplos tomógrafos (mínimo de 7 equipamentos de 4 fabricantes distintos).
* **Mitigação de Desvio de Domínio:** Testar o desempenho da rede em scanners ausentes do treinamento para garantir que o observador de DL não aprenda artefatos específicos de um único fabricante.

### 4. Integração Sinergística com Controle Automático de Exposição (`[[controle-automatico-de-exposicao-ct]]`) e Espectrometria
* **Otimização Conjunta de Dose e Contraste:** Incorporar a modulação automática de corrente ($mA$) e as reconstruções em baixas energias monoenergéticas ($50\text{--}60\text{ keV}$ em `[[virtual-monoenergetic-imaging]]`) no vetor de parâmetros $\mathbf{p}$. Isso viabiliza a otimização simultânea da dose de radiação e do volume de meio de contraste iodado (`[[otimizacao-meio-de-contraste-tc]]`).

---

## 🔗 Conexões e Referências na Wiki
- [[projeto-dd-fapesp-wagner-2026]]
- [[deep-learning-model-observer]]
- [[Deep Learning Image Reconstruction (DLR)]]
- [[Photon Counting Detector CT (PCD-CT)]]
- [[task-based-image-quality]]
- [[otimizacao-multiobjetivo-tc]]
- [[phantoms-hibridos]]
- [[2afc-observer-study]]
- [[greffier-2026-dlr-ct-phantom]]
- [[hoeijmakers-2026-image-quality-modern-ct]]
- [[solomon-2016-observer-models]]
