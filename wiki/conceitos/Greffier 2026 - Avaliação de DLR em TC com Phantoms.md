---
tipo: literatura
aliases: [greffier-2026-dlr-ct-phantom]
tags: [fisica-medica, tomografia-computadorizada\, dlr, qualidade-de-imagem, ruído, fantomas]
data: 2026-08-25
---

# greffier-2026-dlr-ct-phantom

## 1. Definição Conceitual e Fundamentação Física
O termo **`greffier-2026-dlr-ct-phantom`** representa uma referência central no acervo da pesquisa de doutorado em Física Médica e Tomografia Computadorizada (USP/FAPESP) sobre a avaliação experimental e metrológica de algoritmos de **Reconstrução Baseada em Aprendizado Profundo (Deep Learning Reconstruction - DLR)** em TC. 

No contexto da física de imagem moderna, a introdução de redes neurais profundas para a supressão de ruído e artefatos substituiu de forma disruptiva as abordagens analíticas tradicionais (Filtered Backprojection - FBP) e de Reconstrução Iterativa (IR - Iterative Reconstruction). Contudo, a DLR introduz uma complexidade não linear severa, tornando obsoletas as métricas de qualidade de imagem baseadas apenas em pixels (como ruído padrão e desvio padrão em regiões de interesse homogêneas). 

A literatura associada a este registro investiga o desempenho metrológico de sistemas DLR utilizando fantomas antropomórficos e de controle de qualidade físicos. O foco reside em como algoritmos baseados em deep learning se comportam sob condições extremas de dose ultrabaixa ($CTDI_{vol} < 2\text{ mGy}$), avaliando a preservação da resolução espacial de alto contraste — medida pela Função de Transferência de Tarefa (Task Transfer Function - TTF) — e a modulação do Espectro de Potência do Ruído (Noise Power Spectrum - NPS), elementos fundamentais para o cálculo robusto do Índice de Detectabilidade ($d'$) em modelos de observadores computacionais.

---

## 2. Formulação Matemática e Propriedades
A avaliação metrológica de sistemas de DLR em fantomas de TC exige o uso de métricas avançadas que capturem a não-linearidade espacial e espectral. 

O **Espectro de Potência do Ruído 2D (NPS)**, essencial para caracterizar a textura do ruído espacial gerado por algoritmos DLR, é definido a partir da transformada de Fourier bidimensional da matriz de diferença de ruído $\Delta I(x, y)$:

$$
NPS(f_x, f_y) = \frac{\Delta x \Delta y}{N_x N_y} \sum_{m=1}^{N_x} \sum_{n=1}^{N_y} \left\langle \left| \mathcal{F} \left\{ \Delta I(x, y) \right\} \right|^2 \right\rangle
$$

Onde:
- $\Delta x$ e $\Delta y$ representam o tamanho dos voxels no plano de reconstrução.
- $N_x$ e $N_y$ são as dimensões da região de interesse (ROI).
- $\mathcal{F}\{\cdot\}$ denota o operador de transformada de Fourier bidimensional.
- $\langle \cdot \rangle$ representa o operador de ensemble (média em múltiplos cortes ou varreduras).

Para quantificar a resolução espacial dependente da tarefa em imagens processadas por DLR (que frequentemente exibem degradação ou preservação não linear de texturas finas), utiliza-se a **Task Transfer Function (TTF)**, calculada a partir do perfil de borda linearizado $s(r)$ de um inserto no fantoma:

$$
TTF(f) = \left| \frac{d}{df} \left( \mathcal{F} \left\{ \frac{d s(r)}{dr} \right\} \right) \right|
$$

Com essas grandezas, o **Índice de Detectabilidade ($d'$)** para uma tarefa de detecção de sinal binário (modelo de observador não pré-whitenizado com canal - NPWE) é formulado integrando o NPS e a TTF sobre as frequências espaciais:

$$
(d')^2 = \frac{\left[ \iint W(f_x, f_y) \cdot |TTF(f_x, f_y)|^2 \cdot |W_{object}(f_x, f_y)|^2 \, df_x \, df_y \right]^2}{\iint W(f_x, f_y)^2 \cdot NPS(f_x, f_y) \cdot |W_{object}(f_x, f_y)|^4 \, df_x \, df_y}
$$

Onde $W(f_x, f_y)$ representa a função de resposta dos canais do observador e $W_{object}$ é a transformada de Fourier da tarefa a ser detectada. O acervo aponta reduções na magnitude do ruído de até $-83,8\%$ em protocolos de ultrabaixa dose, cuja fidelidade diagnóstica só pode ser garantida por meio desta formulação baseada em tarefas.

---

## 3. Contexto no Acervo do Pesquisador & Aplicações
O rótulo `[[Greffier 2026 - Avaliação de DLR em TC com Phantoms|greffier-2026-dlr-ct-phantom]]` atua como um nó integrador estrutural no acervo do doutorado, conectando dimensões experimentais e teóricas da seguinte forma:

* **Controle de Qualidade e Fantomas:** Fornece a base empírica de validação para protocolos de varredura otimizados em baixas doses ($CTDI_{vol} < 2\text{ mGy}$) conforme discutido em `queries/O que é ttf e porque ele é importante?.md`.
* **Desempenho Metrológico e DLR:** Em `queries/Qual é o estado da arte das tecnologias...`, o documento valida a superação das limitações da Reconstrução Iterativa (IR) pela DLR\, detalhando a supressão de ruído de alta magnitude sem perda catastrófica de detectabilidade.
* **Não-Linearidade e Modelos de Observadores:** Citado em `queries/Comente sobre a evolução dos modelos de observadores computacionais...`, evidencia como algoritmos DLR modernos modificam a textura do ruído de forma altamente não linear, invalidando aproximações clássicas baseadas estritamente em sistemas lineares invariantes no espaço (LSI).
* **Qualidade de Imagem Baseada em Tarefas (TBIQ):** Conecta-se diretamente aos módulos conceituais de `wiki/conceitos/task-based-image-quality.md` e `wiki/conceitos/detectability-index.md`, servindo de referência bibliográfica primária para a implementação prática de avaliações de desempenho de imagem em TC na plataforma FAPESP/USP.

---

## 4. Conexões e Wikilinks
- [[Deep Learning Image Reconstruction (DLR)|Deep Learning Image Reconstruction (DLR)]]
- [[Task Based Image Quality|Task-Based Image Quality (TBIQ)]]
- [[Índice de Detectabilidade|Índice de Detectabilidade (d')]]
- [[AAPM TG-233 - Avaliação de Desempenho em TC|AAPM TG-233 Summary & Performance]]
- [[Projeto Doutorado Direto FAPESP Wagner 2026|Projeto de Doutorado FAPESP]]
- [[Solomon 2016 - Modelos de Observadores em TC|Modelos de Observadores Computacionais]]