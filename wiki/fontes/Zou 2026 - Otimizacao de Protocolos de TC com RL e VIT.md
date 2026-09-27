---
tipo: fonte
titulo: "Task-Based CT Protocol Optimization Using Reinforcement Learning and Virtual Imaging Trials"
data_criacao: 2026-09-18
data_atualizacao: 2026-09-18
autores:
  - Jiaqi Zou
  - David Fenwick
  - Vahid Tarokh
  - Nicholas Felice
  - Jayasai Rajagopal
  - Anuj Kapadia
  - Ehsan Samei
  - Navid NaderiAlizadeh
  - Ehsan Abadi
ano: 2026
veiculo: "arXiv (Duke University & Oak Ridge National Laboratory)"
doi: "arXiv:2609.13309"
fonte_bruta: "raw/2609.13309v1.pdf"
tags:
  - tomografia-computadorizada
  - otimizacao-de-protocolos
  - task-based-image-quality
  - aprendizado-por-reforco
  - virtual-imaging-trials
  - indice-de-detectabilidade
  - vision-transformer
fontes_origem: []
---

# Task-Based CT Protocol Optimization Using Reinforcement Learning and Virtual Imaging Trials

## Resumo Executivo (Guia Conceitual Didático)

### 1. O Dilema Clínico: O "Quebra-Cabeça" dos Protocolos de TC
Na Tomografia Computadorizada (TC), o objetivo principal é encontrar o equilíbrio ideal entre **dois lados opostos de uma balança**:
* **Dose de Radiação:** Deve ser a mais baixa possível para proteger a saúde do paciente (princípio ALARA / radioproteção).
* **Qualidade da Imagem:** Deve ser suficientemente boa para que o médico radiologista consiga enxergar e diagnosticar lesões sutis (como um tumor pequeno no fígado).

O grande desafio prático é que um tomógrafo moderno possui dezenas de parâmetros ajustáveis: tensão do tubo ($kV$), corrente do tubo ($mAs$), espessura de corte, tamanho do pixel e filtros matemáticos de reconstrução (*kernels*). Combinando essas opções, chega-se facilmente a **centenas de protocolos possíveis** (neste estudo, foram **468 combinações**). Testar todas as combinações em pacientes reais é **inviável e antiético** (devido ao excesso de radiação), e testar manualmente em simuladores físicos consome tempo e recursos proibitivos.

---

### 2. Os Quatro Conceitos Fundamentais Usados no Estudo

Para resolver esse dilema de forma inteligente, o estudo da Duke University uniu quatro tecnologias de ponta:

1. **Virtual Imaging Trials (VIT - Ensaios Clínicos Virtuais):**
   * *O que é:* Em vez de irradiar pessoas reais, os pesquisadores utilizaram **63 "corpos humanos virtuais" tridimensionais** hiper-realistas criados em computador (fantomáticos computacionais XCAT) com lesões simuladas no fígado.
   * *Para que serve:* Permite simular a física do feixe de raios X e testar dezenas de protocolos no computador sem risco a ninguém.

2. **Qualidade de Imagem Baseada em Tarefa (*Task-Based*) e o Índice de Detectabilidade ($d'$):**
   * *O que é:* Métricas tradicionais (como medir o desvio-padrão do ruído geral da imagem) não dizem se a imagem é clinicamente útil. A abordagem *task-based* foca na **tarefa médica específica**: *"A imagem permite enxergar esta lesão com clareza?"*
   * *Métrica ($d'$):* O **índice de detectabilidade ($d'$)** é um número que quantifica matematicamente o quão fácil é separar a lesão do ruído de fundo. Quanto maior o $d'$, maior a certeza de detecção.

3. **Visão Computacional no Topograma (*Scout View* com Vision Transformer):**
   * *O que é:* Antes de fazer a tomografia axial completa, o aparelho sempre tira uma radiografia panorâmica rápida de corpo inteiro para planejamento, chamada **topograma** (ou *scout view / localizer*).
   * *O que o modelo fez:* Uma rede de inteligência artificial baseada em atenção (**Vision Transformer - ViT**) "olha" para esse topograma e traduz o tamanho, a espessura, o peso e a densidade anatômica daquele paciente específico em um resumo numérico compacto (*embedding*).

4. **Aprendizado por Reforço (*Reinforcement Learning* - PPO):**
   * *O que é:* O Aprendizado por Reforço funciona como ensinar um agente inteligente através de **recompensas e penalidades**:
     * Se o agente escolhe um protocolo que gera imagem nítida (alto $d'$) com pouca radiação, ele ganha uma **recompensa**.
     * Se ele escolhe um protocolo com muita radiação ou imagem borrada, ele sofre uma **penalidade**.
   * *O algoritmo (PPO):* *Proximal Policy Optimization* é um algoritmo moderno e estável de aprendizado por reforço que ajusta a tomada de decisão do agente passo a passo.

---

### 3. A Conclusão e o Impacto Prático do Estudo

* **Eficiência Revolucionária:** Em vez de simular todas as 468 combinações possíveis para cada paciente, o agente de IA precisou "experimentar" apenas **8 protocolos por paciente** no simulador para encontrar a configuração quase perfeita.
* **Acurácia Quase Total:** Com apenas essas 8 tentativas inteligentes (menos de 2% do esforço de busca exaustiva), o sistema recuperou **98,2% da qualidade e benefício máximo** possível.
* **Adaptação Automática ao Biotipo:** O modelo aprendeu sozinho que pacientes com sobrepeso ou obesidade demandam tensões de feixe mais altas (140 kV) e filtros de reconstrução mais suaves para compensar a atenuação da gordura corporal, enquanto pacientes magros conseguem excelentes diagnósticos com tensões e doses menores.

Em termos simples: o artigo demonstra que é possível criar um **"piloto automático inteligente"** para tomógrafos, capaz de olhar a radiografia inicial do paciente e escolher, em segundos, a combinação exata de parâmetros que maximiza a visibilidade da doença administrando o mínimo de radiação necessária.

---

## 💡 O que tem de Original (Diferencial Metodológico)

1. **Agente de Otimização PPO com Espaço de Busca Amplo e Discreto:**
   Ao contrário de abordagens clássicas baseadas em algoritmos genéticos genéricos ou superfícies de resposta estáticas, o trabalho modela a seleção de protocolos de TC como um processo de decisão sequencial/reforço, permitindo que a política de varredura aprenda dinamicamente os compromissos entre dose e qualidade.

2. **Embeddings Anatômicos de Paciente via Vision Transformer:**
   Como a coorte de pacientes virtuais não permite treinar um codificador do zero sem *overfitting*, os autores congelaram um Vision Transformer pré-treinado em imagens naturais para processar diretamente os *scout views* (localizers) em resolução $224 \times 896$ (mantendo o aspecto 1:4 anatômico). Esses embeddings transmitem ao agente de RL o biotipo (*body habitus*), atenuação global e dimensões do paciente antes de qualquer decisão de protocolo.

3. **Duplo Modo Operacional: Offline vs. Online:**
   - **Modo Offline (Zero Simulação Adicional):** Apenas com o embedding do *scout* e a política pré-treinada, o modelo recuperou **89,7%** do desempenho do oráculo ótimo, superando regras clínicas fixas estabelecidas (81,6% a 84,4%).
   - **Modo Online (Simulação Ativa guiada por Orçamento):** Com um teto de apenas até 8 simulações de protocolos por paciente, o agente subiu a recuperação para **98,2%** da recompensa ótima, eliminando 98% do custo computacional do VIT.

4. **Incorporação Direta do Índice de Detectabilidade ($d'$) na Função de Recompensa:**
   A recompensa do agente é expressa diretamente pela detectabilidade diagnóstica da tarefa clínica ($d'$) penalizada linearmente pela dose de radiação ionizante ($\text{mAs}$):
   $$
   \mathcal{R}(s, a) = d'(s, a) - \lambda \cdot \text{mAs}(a)
   $$

---

## 📈 O que Agrega (Achados e Métricas Quantitativas)

* **Espaço Amostral Mapeado:**
  * **Tensão do Tubo ($kV$):** 100, 120, 140 kVp.
  * **Corrente do Tubo ($\text{mAs}$):** 25, 80, 150 mAs.
  * **Kernels de Reconstrução:** Ram-Lak, Cosine, Smooth, Sharp, Enhancing ($f_{50} = 0{,}4; 0{,}6; 0{,}8\text{ mm}^{-1}$).
  * **Espessura de Corte & Tamanho de Pixel:** 0,5 mm e 1,0 mm.
  * **Total:** $3 \times 3 \times 5 \times 3 \times 2 \times 2 = 468$ protocolos únicos por paciente.
* **Impacto do Biotipo na Política Ótima:**
  * Em pacientes magros (ex.: BMI = 22,5; lesão de 2 mm), a detectabilidade máxima atinge $d' = 3{,}68$, e o agente seleciona tensões moderadas (120 kV) com filtros intermediários.
  * Em pacientes com obesidade (ex.: BMI = 38,8; lesão de 5 mm), a seleção migra para **140 kVp** e filtros mais suaves (*Smooth/Cosine*), demonstrando que tensões mais altas são estritamente necessárias para penetrar o arcabouço adiposo e não afogar o sinal sob ruído de baixa fluência de fótons.
* **Curva de Compromisso Dose–Detectabilidade:**
  Variando-se o hiperparâmetro de penalidade de dose $\lambda \in [0{,}14; 0{,}20]$, o $d'$ médio selecionado declinou monotonicamente de 4,05 para 3,59, permitindo ao gestor clínico traçar uma curva de calibração entre dose institucional e sensibilidade diagnóstica.

---

## 🎯 Conexão com o Projeto de Doutorado (Wagner Marques - Física Médica / FMUSP)

Este artigo é de **máxima relevância estratégica** para a tese de doutorado e para a proposta FAPESP de Wagner Marques, fornecendo subsídios de comparação direta e reforçando a originalidade do projeto da FMUSP:

| Dimensão Metodológica | Zou et al. (Duke / ORNL, 2026) | Projeto de Doutorado Wagner Marques (FMUSP, 2026) | Vantagem / Diferencial do Doutorado |
| :--- | :--- | :--- | :--- |
| **Domínio Experimental** | 100% Virtual (*Virtual Imaging Trials* em simulador analítico de TC com modelos voxelizados XCAT). | **Físico-Experimental Híbrido** (3 *phantoms* antropomórficos físicos impressos em 3D: tórax, abdome e crânio). | Validação com dados de radiação reais, espalhamento físico, *beam hardening* real e limitações mecânicas dos gantries. |
| **Parque Tecnológico** | 1 simulador computacional parametrizado. | **7 tomógrafos clínicos reais de 4 fabricantes** (GE, Siemens, Philips, Canon) no InRad-HCFMUSP. | Avaliação inédita de transferibilidade e robustez inter-fabricantes (*leave-one-scanner-out*). |
| **Dimensões de Otimização** | 2 Dimensões: $(D, W)$ $\rightarrow$ Dose ($\text{mAs}$) vs. Detectabilidade ($d'$). | **3 Dimensões: $(D, T, W)$** $\rightarrow$ Dose ($\text{CTDI}_{\text{vol}}$), **Tempo Operacional ($T$)** e Detectabilidade ($d'$). | **Originalidade Crítica:** A tese inclui o tempo de aquisição e reconstrução (latência clínica), essencial para rastreamento populacional e rotina hospitalar. |
| **Papel do Vision Transformer (ViT)** | Extrator de *features* congelado apenas para codificar o *scout view* (topograma). | **O próprio Observador-Modelo (DLMO)** com atenção, treinado para inferir $d'$ em imagens complexas sob DLR/IR. | Inovação na arquitetura psicofísica do observador, e não apenas no pré-processamento anatômico. |
| **Validação Perceptual** | Puramente matemática (cálculo de $d'$ analítico). | **Calibração psicofísica direta com Radiologistas** especialistas via estudos 2AFC e FROC/AFROC no InRad. | Ancoragem clínica real no desempenho visual humano. |

> **Oportunidade de Citação na Proposta FAPESP:**
> O trabalho de Zou et al. (2026) deve ser explicitamente citado no item **2 (Introdução e Justificativa)** e no **Eixo 3 (Otimização Multiobjetivo)** como a comprovação mais recente de que a comunidade internacional de ponta (grupo de Samei em Duke) reconhece a inviabilidade de buscas exaustivas e valida a otimização *task-based*. Ao mesmo tempo, ele serve como o contraponto ideal para demonstrar que a tese de Wagner vai além ao incorporar **phantoms físicos híbridos**, **equipamentos clínicos reais de múltiplos fabricantes** e a **variável crítica do tempo operacional**.

---

## Dados Metodológicos & Fórmulas

### 1. Formulação do Agente PPO (Proximal Policy Optimization)
A política $\pi_\theta(a|s)$ e a rede de valor foram modeladas por Perceptrons Multicamadas (MLP) compostos por um codificador de estado de 128 neurônios alimentando 2 camadas ocultas de 256 neurônios com ativações ReLU:

$$
L^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}_t \right) \right]
$$

Onde:
* $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$ é a razão de probabilidades de ação.
* $\hat{A}_t$ é o estimador de vantagem calculado via Generalized Advantage Estimation (GAE) com $\lambda_{\text{GAE}} = 0{,}95$.
* Intervalo de recorte $\epsilon = 0{,}20$, taxa de desconto $\gamma = 0{,}99$ e taxa de aprendizado $\eta = 3 \times 10^{-4}$.

### 2. Índice de Detectabilidade ($d'$)
A detectabilidade foi estimada analiticamente em conformidade com as formulações do AAPM TG-233 para sinal de lesão esférica conhecida em fundo anatômico:

$$
(d')^2 = \iint \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \text{TTF}^2(u, v)}{\text{NPS}(u, v)} \, du \, dv
$$

---

## 🛠️ Roteiro Metodológico: Engenharia dos Algoritmos e Aplicação na Tese

### 1. Arquitetura Técnica do Artigo (Pipeline Duke/ORNL)
* **Extração Anatômica:** Vision Transformer (`ViT-B/16` pré-treinado no ImageNet) com pesos congelados. Recebe o scout view ($224 \times 896$ pixels) e extrai o embedding do biotipo do paciente.
* **Agente de Decisão:** Algoritmo PPO da biblioteca aberta `Stable-Baselines3` com política MLP (camadas de 128 -> 256 -> 256 neurônios).
* **Função de Custo:** $\mathcal{R} = d' - \lambda \cdot \text{mAs}$, operando em ambiente padrão `Gymnasium`.

### 2. Análise Crítica para a Tese de Doutorado (Wagner Marques / FMUSP)
* **O que NÃO reproduzir fielmente:** Não é viável nem recomendado usar PPO puro com 100.000 passos no mundo físico dos 7 tomógrafos do InRad, nem restringir-se a simulações puramente analíticas (VIT) que não refletem os algoritmos fechados de DLR (TrueFidelity, AiCE, etc.).
* **O Caminho de Evolução da Tese:**
  1. Utilizar os **3 phantoms híbridos físicos** (tórax, abdome, crânio) para gerar matrizes experimentais reais.
  2. Substituir a busca massiva por **Modelos Substitutos (Surrogate Models / Processos Gaussianos)** acoplados a algoritmos genéticos multiobjetivo (**NSGA-II**), mapeando a Fronteira de Pareto real no espaço tridimensional $(D, T, W)$.
  3. Posicionar o Vision Transformer **como o próprio Observador-Modelo (DLMO)** com mecanismo de atenção para estimar $d'$, e não apenas como leitor passivo de topogramas.

---

## 📚 Notas Conceituais Relacionadas
- [[Deep Learning Model Observers e Tempo Operacional na Otimizacao de TC]] — Superação do Sim-to-Real gap, formulação do DLMO e inclusão do tempo de aquisição/reconstrução no espaço de Pareto $(D, T, W)$.

