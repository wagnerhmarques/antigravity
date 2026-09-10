> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Deep Learning Model Observer]], [[Estudo de Observadores 2AFC]], [[Phantoms Híbridos]], [[Curva ROC e AUC]], [[Índice de Detectabilidade]]

A construção de um **Observador-Modelo de Aprendizado Profundo** ([[deep-learning-model-observer]]) para avaliação de qualidade de imagem baseada em tarefas ([[task-based-image-quality]]) em Tomografia Computadorizada (TC) deve seguir uma metodologia bem definida. Como a IA deve atuar em substituição aos observadores humanos para prever o desempenho em algoritmos não-lineares ([[Deep Learning Image Reconstruction (DLR)]] e [[reconstrucao-iterativa]]), o projeto deve ser desenvolvido em fases encadeadas, conforme detalhado na proposta metodológica de [[projeto-dd-fapesp-wagner-2026]].

---

## Fase 1: Fundação Metrológica e Baselines Clássicos
Antes de treinar redes neurais, é indispensável estabelecer a automação das métricas físicas e dos observadores matemáticos lineares clássicos recomendados pelo [[aapm-tg233-ct-performance]] e [[aapm-tg233-ct-performance|aapm-tg-233-summary]].

1. **Automação do [[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]]:** Implementar o cálculo do $NPS_{2D}$ e $NPS_{1D}$ para quantificar a magnitude e textura do ruído em regiões homogêneas de phantoms.
2. **Automação da [[Task Transfer Function]]:** Implementar a extração da $TTF(u,v)$ via método de borda circular para mensurar a resolução espacial dependente de contraste.
3. **Implementação de Observadores Lineares Baselines:**
   - **NPWE ([[model-observers|observadores-de-modelo]]):** *Non-Pre-Whitening Observer with Eye Filter*, que incorpora a resposta do olho humano $E(u,v)$.
   - **CHO ([[model-observers|observadores-de-modelo]]):** *Channelized Hotelling Observer* com canais de Gabor para processamento de frequência espacial.
4. **Cálculo Físico do [[Índice de Detectabilidade]] ($d'$):**
   

$$
d'^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot E^2(u, v) \, du \, dv \right]^2}{\iint_{-\infty}^{\infty} |W(u, v)|^2 \cdot \text{TTF}^2(u, v) \cdot \text{NPS}(u, v) \cdot E^4(u, v) \, du \, dv + \sigma_{\text{int}}^2}
$$

---

## Fase 2: Aquisição e Preparação do Corpus de Imagens (Datasets e Phantoms)
O treinamento de observadores profundos requer pares de imagens contendo sinal (*Signal Present*) e apenas fundo (*Signal Absent*).

1. **Uso de [[phantoms-hibridos]]:** Combinar regiões geométricas homogêneas para calibração física com estruturas antropomórficas e ruído anatômico realista (ex.: parênquima hepático, pulmonar ou calota craniana).
2. **Inserção Controlada de Lesões Simuladas:** Inserir matematicamente ou fisicamente alvos de baixo contraste (ex.: lesões hepáticas de $85\text{ HU}$) e alto contraste com diferentes dimensões ($2\text{ mm}$ a $10\text{ mm}$).
3. **Variabilidade de Protocolos e Equipamentos:** Coletar aquisições sob múltiplos níveis de dose ($CTDI_{vol}$ de $1,8\text{ mGy}$ a $11\text{ mGy}$) e diferentes algoritmos de reconstrução ([[Deep Learning Image Reconstruction (DLR)]], [[admire-reconstruction]], FBP).

---

## Fase 3: Arquitetura e Formulação do Observador Profundo (DLMO)
Os observadores lineares falham em capturar as não-estacionariedades e a dependência de sinal causadas por redes profundas de reconstrução. O DLMO supera essa limitação:

1. **Escolha da Arquitetura:**
   - **Vision Transformers (ViT) com Atenção Multicabeça:** Ideal para modelar a dependência espacial global e a textura de ruído não local.
   - **CNNs Profundas com Mecanismos de Atenção (Squeeze-and-Excitation / Spatial Attention):** Eficientes para filtrar variações locais de alto e baixo contraste.
2. **Formulação do Problema:**
   - **Treinamento 2AFC (Two-Alternative Forced Choice):** Apresentar à rede pares de imagens (uma com lesão, outra sem lesão) e calcular a Porcentagem de Escolhas Corretas ($PC$).
   - **Conversão para Índice de Detectabilidade ($d'_{\text{DLMO}}$):**
     

$$
d' = 2 \cdot \Phi^{-1}(PC)
$$

     onde $\Phi^{-1}$ é a inversa da função de distribuição acumulada normal padrão.

---

## Fase 4: Estudo Perceptual de Calibração com Radiologistas
Para garantir que o DLMO reflita fielmente a visão humana e não seja um mero classificador de ruído estatístico, ele deve ser calibrado contra observadores humanos especializados.

1. **Experimento psicofísico [[2afc-observer-study]]:** Conduzir leitura controlada com radiologistas especialistas (mínimo de 20 observadores por anatomia, conforme [[projeto-dd-fapesp-wagner-2026]]).
2. **Validação da Correlação:** Comparar o desempenho humano ($d'_{\text{Humano}}$ ou AUC) com o $d'_{\text{DLMO}}$ calculando o Coeficiente de Correlação Intraclasse (ICC).
3. **Criterio de Aceitação:** Atingir $ICC \ge 0,90$, comprovando alta fidelidade perceptual.

---

## Fase 5: Aplicação na Otimização Multiobjetivo (Tríade D-T-W)
Uma vez validado, o DLMO passa a atuar como função objetivo quantitativa de desempenho no planejamento de protocolos clínicos via [[otimizacao-multiobjetivo-tc]]:

$$
\min_{\mathbf{p} \in \Omega} \Big( D(\mathbf{p}), \, T(\mathbf{p}), \, -W(\mathbf{p}) \Big)
$$

* **$D(\mathbf{p})$:** Dose de radiação ([[metricas-de-dose-tc|$CTDI_{vol}$]] / DLP);
* **$T(\mathbf{p})$:** Tempo operacional total (aquisição + reconstrução);
* **$W(\mathbf{p})$:** Desempenho diagnóstico quantificado pelo $d'_{\text{DLMO}}$.

O espaço de soluções otimizadas é extraído através de algoritmos genéticos ([[nsga-ii]]) mapeando a Fronteira de Pareto sob a restrição de $\varepsilon$-dominância.
