> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]], [[Função de Sensibilidade Visual Humana]], [[Teoria de Detecção de Sinais]]

## 1. Definição Física e Metrológica do Índice de Detectabilidade ($d'$)

O **Índice de Detectabilidade** ($d'$, *d-prime*) é a métrica objetiva padrão-ouro recomendada pelo relatório **[[aapm-tg233-ct-performance]]** da AAPM e pelas normas ICRU para avaliar a **qualidade de imagem baseada em tarefas clínicas** (*Task-Based Image Quality* - [[task-based-image-quality]]) em Tomografia Computadorizada (TC).

Diferente de métricas clássicas e simplificadas como a Relação Contraste-Ruído convencional ([[contrast-to-noise-ratio|CNR]]), que ignoram a frequência espacial e a textura do ruído, o $d'$ quantifica a separação estatística entre a hipótese de presença de uma lesão ($H_1$) e a hipótese de apenas ruído de fundo ($H_0$), integrando em uma única grandeza:
1. O espectro morfológico e de contraste da lesão ou sinal anatômico ($W_{\text{task}}$);
2. A resolução espacial não-linear e dependente de contraste do tomógrafo ([[task-transfer-function|TTF]]);
3. A amplitude e correlação espacial (textura) do ruído estocástico ([[noise-power-spectrum|NPS]]);
4. A sensibilidade do sistema visual humano ($E(u, v)$) ou do observador matemático ([[model-observers]]).

---

## 2. Formulações Matemáticas e Métodos de Cálculo

### A. Observador Não-Branqueador com Filtro Visual Humano (NPWE)
Para predizer a acurácia de radiologistas na detecção de lesões de baixo contraste em imagens tomográficas, a formulação bidimensional no espaço de frequências de Fourier $(u, v)$ é dada por:

$$
d'^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \, du \, dv \right]^2}{\iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \text{NPS}(u, v) \cdot \left[ E(u, v) \right]^4 \, du \, dv + \sigma_{\text{int}}^2}
$$

Onde:
* $W_{\text{task}}(u, v) = \mathcal{F}\{\Delta \mu(x, y)\}$ é a **Função de Tarefa**, obtida pela Transformada de Fourier 2D da diferença de atenuação do objeto em relação ao fundo circundante;
* $\text{TTF}(u, v)$ é a **Task-based Transfer Function**, que mede a resposta em frequência espacial para o contraste específico do sinal;
* $\text{NPS}(u, v)$ é o **Noise Power Spectrum**, que caracteriza a distribuição de variância do ruído nas frequências espaciais;
* $E(u, v)$ é a **Função de Resposta do Olho Humano** (filtro passa-faixa visual de Burgess/Samei, parametrizado pela distância de visualização e abertura angular);
* $\sigma_{\text{int}}^2$ representa o ruído interno estocástico do observador humano.

---

### B. Observador Linear Ideal (Prewhitening - PW / Hotelling)
Sob condições ideais em que o observador possui capacidade perfeita de descorrelacionar (branquetear) o ruído:

$$
d'^2_{\text{PW}} = \iint_{-\infty}^{\infty} \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2}{\text{NPS}(u, v)} \, du \, dv
$$

---

### C. Integração Radial (Coordenadas Polares com Simetria Isotrópica)
Em fantomas homogêneos circulares (como o fantoma AAPM TG-233) com alvos cilíndricos, a integração pode ser simplificada em frequência radial $f = \sqrt{u^2 + v^2}$:

$$
d'^2 = \frac{\left[ 2\pi \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ \text{TTF}(f) \right]^2 \cdot \left[ E(f) \right]^2 \cdot f \, df \right]^2}{2\pi \int_{0}^{\infty} \left| W_{\text{task}}(f) \right|^2 \cdot \left[ \text{TTF}(f) \right]^2 \cdot \text{NPS}(f) \cdot \left[ E(f) \right]^4 \cdot f \, df + \sigma_{\text{int}}^2}
$$

---

### D. Relação Psicofísica com Estudos 2-AFC (Two-Alternative Forced Choice)
Em experimentos psicofísicos de detecção forçada entre duas alternativas ([[2afc-observer-study]]), a porcentagem de acertos observados ($P_c$) relaciona-se rigorosamente com $d'$ através da função de distribuição acumulada da normal padrão ($\Phi$):

$$
P_c = \Phi\left( \frac{d'}{\sqrt{2}} \right) \iff d' = \sqrt{2} \cdot \Phi^{-1}(P_c)
$$

---

## 3. Aplicação Prática no Doutorado Direto (USP/FAPESP)

1. **Otimização de Algoritmos Deep Learning ([[Deep Learning Image Reconstruction (DLR)]] - DLR):**  
   Algoritmos como TrueFidelity, AiCE e Precise Image alteram a estacionariedade do ruído. O cálculo de $d'$ permite quantificar ganhos reais de detectabilidade (superiores a $+100\%$) mesmo com redução substancial de dose ([[otimizacao-de-dose-em-tc]]).
2. **Treinamento de Observadores Profundos ([[deep-learning-model-observer]]):**  
   O observador computacional convolucional com atenção estima $d'$ diretamente de fantomas antropomórficos ([[phantoms-hibridos]] e [[pixelprint]]), sendo validado contra experimentos 2-AFC com radiologistas.
3. **Otimização Multiobjetivo no Espaço de Pareto ([[nsga-ii]]):**  
   Maximizar $d'$ ($\max d'$) balanceando simultaneamente a minimização da dose de radiação ($\min \text{CTDI}_{\text{vol}}$) e do volume de contraste iodado ([[otimizacao-meio-de-contraste-tc]]).
