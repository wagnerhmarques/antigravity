---
tipo: conceito
aliases: [llm-wiki]
tags: [fisica-medica, tomografia-computadorizada, epistemologia, inteligencia-artificial]
data: 2026-08-25
---

# llm-wiki

## 1. Definição Conceitual e Fundamentação Física
A **llm-wiki** representa a infraestrutura de conhecimento híbrida — computacional, epistemológica e metrológica — desenvolvida no âmbito do laboratório USP/FAPESP para a gestão, recuperação e síntese de acervos científicos em Física Médica e Tomografia Computadorizada (TC). Diferente de sistemas de recuperação de informação convencionais (RAG estático), a arquitetura da `llm-wiki` fundamenta-se no princípio da **Imutabilidade do Raw**, assegurando que os dados primários de aquisição, as notas de campo metrológicas e os artigos de referência permaneçam inalterados e invioláveis em uma pasta `raw/`, servindo como âncora ontológica irredutível para o crescimento orgânico cumulativo da base.

Epistemologicamente, a `llm-wiki` atua como um sistema dinâmico de âncoras vetoriais e hipertextuais que mapeia o espaço de parâmetros da imagem médica — desde a física da interação fóton-matéria (atribuição do coeficiente de atenuação linear $\mu(x,y)$) até os algoritmos de reconstrução iterativa e reconstrução baseada em aprendizado profundo (DLR - *Deep Learning Reconstruction*). A integração de Modelos de Linguagem de Grande Escala (LLMs) permite a destituição de barreiras semânticas na exploração de catálogos complexos de controle de qualidade, otimização de dose e avaliação de detectabilidade de lesões.

## 2. Formulação Matemática e Propriedades
O ecossistema informacional e vetorial da `llm-wiki` pode ser modelado formalmente como um grafo direcionado ponderado $G = (V, E, W)$, onde o conjunto de vértices $V$ representa os documentos de conhecimento (conceitos fundamentais, notas de controle de qualidade, artigos analíticos), o conjunto de arestas $E$ representa as relações hipertextuais explícitas (wikilinks) e $W$ denota a matriz de similaridade semântica no espaço de incorporação (*embedding space*).

Seja um documento $d_i \in V$ mapeado por uma função de vetorização induzida pela LLM:

$$
\vec{e}_i = \mathcal{F}_{\text{LLM}}(d_i) \in \mathbb{R}^{d_m}
$$

onde $d_m$ é a dimensionalidade do espaço vetorial latente. A relevância semântica e a recuperação de contexto para uma dada consulta (query) do pesquisador baseiam-se na similaridade de cosseno restrita ao subespaço epistêmico gerado pelas fontes brutas:

$$
\text{Sim}(q, d_i) = \frac{\vec{q} \cdot \vec{e}_i}{\|\vec{q}\| \|\vec{e}_i\|} \cdot \delta(\text{raw}_j, d_i)
$$

onde $\delta(\text{raw}_j, d_i)$ é a função indicadora que garante a fidelidade e rastreabilidade estrita à fundação metrológica da camada `raw/`, impondo que nenhuma inferência sintética supere a evidência empírica primária dos fantomas\, dos arquivos DICOM brutos ou dos relatórios de dosimetria ($\text{CTDI}_{\text{vol}}$, $\text{DLP}$).

A evolução temporal do acervo obedece a uma equação de crescimento orgânico cumulativo:

$$
\frac{d\mathcal{K}(t)}{dt} = \alpha \cdot \Phi_{\text{analitica}}(t) - \beta \cdot \mathcal{H}_{\text{entropia}}(t)
$$

onde $\mathcal{K}(t)$ representa o corpo de conhecimento consolidado, $\Phi_{\text{analitica}}(t)$ é o fluxo de novas entradas validadas criticamente, e $\mathcal{H}_{\text{entropia}}(t)$ representa a degradação informacional combatida ativamente pelas rotinas de curadoria automatizada e humana da USP/FAPESP.

## 3. Contexto no Acervo do Pesquisador & Aplicações
No acervo persistente do laboratório, a `llm-wiki` opera como a espinha dorsal metodológica para a estruturação de conceitos avançados e intersecções disciplinares. Conforme documentado no arquivo de consultas [[queries/você tem a capacidade de obter informações por meio de fontes que não estão na pasta raw?.md]], a integridade da base repousa estritamente sobre a **Imutabilidade do Raw**, garantindo que algoritmos de reconstrução ou métricas de qualidade de imagem mantenham sua rastreabilidade metrológica primária inalterada.

Ademais, análises sistemáticas da taxonomia e do vocabulário da base, exploradas em [[queries/quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md]]\, demonstram que a `llm-wiki` catalisa a conexão entre conceitos fundamentais da física de raios-X, protocolos de redução de dose em tomografia computadorizada multidetectores (MDCT), e a avaliação objetiva da qualidade de imagem através de funções de transferência de modulação (MTF), ruído de Wiener (NPS) e detectabilidade tarefa-dependente (NEQ e d' - *detectability index*).

## 4. Conexões e Wikilinks
- [[queries/você tem a capacidade de obter informações por meio de fontes que não estão na pasta raw?.md]]
- [[queries/quais são os termos mais frequentes na minha estruturaco aqui no obsidian?.md]]
- [[Conceitos Imutabilidade do Raw|conceitos/Imutabilidade do Raw]]
- [[Deep Learning Image Reconstruction (DLR)|DLR]]
- [[Métricas de Dose em TC|metricas-de-dose-tc]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]