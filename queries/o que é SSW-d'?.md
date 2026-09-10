> ⚠️ **LLM Wiki:** *Houve uma instabilidade temporária na API do Gemini. Tente pressionar Option + Enter novamente em alguns instantes.*

> 📅 **Data:** 2026-09-08 | 🔗 **Conexões:** [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]], [[Deep Learning Image Reconstruction (DLR)]], [[AAPM TG-233 - Avaliação de Desempenho em TC]]

## 1. Definição Conceitual e Fundamentação Física

O **SSW-$d'$** (*Slice-Summed Weighted Detectability Index* ou *Spatial-Spectral Windowed $d'$*) é uma extensão volumétrica tridimensional (3D) do [[Índice de Detectabilidade]] ($d'$) clássico, desenvolvida no âmbito da metrologia tomográfica baseada em tarefas (*Task-Based Image Quality*).

Enquanto a formulação convencional de $d'$ estabelecida pelo relatório [[AAPM TG-233 - Avaliação de Desempenho em TC]] avalia a detectabilidade em um único plano tomográfico bidimensional ($2\text{D}$ axial) — assumindo implicitamente que a lesão é cilíndrica ou que o observador clínico restringe sua leitura a um corte isolado —, o **SSW-$d'$** modela realisticamente o processo de detecção volumétrica. Em exames clínicos de [[Tomografia Computadorizada]], médicos radiologistas realizam a varredura e o diagnóstico navegando através de múltiplos cortes adjacentes (modo *cine* ou reconstruções multiplanares). O SSW-$d'$ quantifica matematicamente o ganho estatístico de informação proveniente da integração do sinal e da correlação do ruído ao longo do eixo longitudinal ($z$), ponderando cada corte de acordo com a morfologia volumétrica da lesão e a resposta do sistema.

---

## 2. Formulação Matemática Rigorosa

### A. Estatística de Decisão Multi-Corte (*Slice-Summed Decision Model*)
Seja uma lesão tridimensional discretizada cuja atenuação se estende por $K$ cortes tomográficos adjacentes ao longo do eixo $z$. Sob o paradigma linear de detecção de hipótese nula $\mathcal{H}_0$ (apenas fundo e ruído) contra $\mathcal{H}_1$ (sinal presente em fundo estocástico), a estatística de decisão global $\lambda_{\text{3D}}$ é dada pela combinação linear ponderada das variáveis de decisão de cada corte individual $\lambda_k$:

$$
\lambda_{\text{3D}} = \sum_{k=1}^{K} w_z(k) \cdot \lambda_k = \mathbf{w}_z^T \boldsymbol{\lambda}
$$

Onde $\mathbf{w}_z = [w_z(1), w_z(2), \dots, w_z(K)]^T$ é o vetor de ponderação longitudinal ótimo, derivado do perfil de espessura de corte e da geometria do sinal.

### B. Equação Integral no Domínio da Frequência ($3\text{D}$ Fourier Space)
Para um observador de modelo acoplado ao sistema visual humano e à resposta espectral 3D, o índice SSW-$d'$ é formalizado por:

$$
(d'_{\text{SSW}})^2 = \frac{\left[ \iiint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v, f_z) \right|^2 \cdot \left[ \text{TTF}_{xy}(u, v) \right]^2 \cdot \left[ \text{TTF}_z(f_z) \right]^2 \cdot \left[ E(u, v) \right]^2 \\, du \\, dv \\, df_z \right]^2}{\iiint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v, f_z) \right|^2 \cdot \left[ \text{TTF}_{xy}(u, v) \right]^2 \cdot \left[ \text{TTF}_z(f_z) \right]^2 \cdot \text{NPS}_{3\text{D}}(u, v, f_z) \cdot \left[ E(u, v) \right]^4 \\, du \\, dv \\, df_z + \sigma_{\text{int}}^2}
$$

Onde:
* $W_{\text{task}}(u, v, f_z) = \mathcal{F}_{3\text{D}}\{\Delta \mu(x, y, z)\}$: Função de tarefa tridimensional da patologia;
* $\text{TTF}_{xy}(u, v)$: [[Task Transfer Function]] no plano axial;
* $\text{TTF}_z(f_z)$: Função de transferência de modulação longitudinal, intimamente relacionada ao Perfil de Sensibilidade de Corte (*Slice Sensitivity Profile* - SSP);
* $\text{NPS}_{3\text{D}}(u, v, f_z)$: [[Noise Power Spectrum]] tridimensional, que captura tanto a textura de ruído no plano quanto a correlação estocástica entre cortes vizinhos induzida pela interpolação helicoidal ou regularização longitudinal;
* $E(u, v)$: Função de sensibilidade ao contraste do olho humano (*eye filter*);
* $\sigma_{\text{int}}^2$: Variância do ruído interno intrínseco do observador humano.

### C. Caso Discreto Descorrelacionado vs. Correlacionado
Quando o ruído entre cortes exibe correlação moderada (frequente em reconstruções axiais com espaçamento menor que a espessura de corte nominal, $\Delta z < \text{FWHM}_{\text{SSP}}$), o SSW-$d'$ matricial opera sobre a matriz de covariância entre cortes $\mathbf{K}_{z}$:

$$
d'_{\text{SSW}} = \sqrt{\Delta \mathbf{s}_z^T \mathbf{K}_{z}^{-1} \Delta \mathbf{s}_z}
$$

Onde $\Delta \mathbf{s}_z$ expressa a integral do sinal da lesão convoluída com o perfil de corte em cada fatia $k$.

---

## 3. Comparação Metrológica: $d'_{2\text{D}}$ Clássico vs. SSW-$d'$

| Característica Metrológica | $d'_{2\text{D}}$ Convencional (AAPM TG-233) | SSW-$d'$ (Volumétrico / Ponderado) |
| :--- | :--- | :--- |
| **Dimensionalidade da Tarefa** | Puramente planar ($x, y$) | Totalmente volumétrica ($x, y, z$) |
| **Modelagem da Lesão** | Cilindro de comprimento infinito ou disco $2\text{D}$ | Esfera/elipsoide anatômico 3D real |
| **Sensibilidade à Espessura ($z$)** | Ignora espessura de corte e SSP | Modela explicitamente o borramento do SSP e o pitch helicoidal |
| **Correlação de Ruído Inter-cortes** | Assume independência ($0\text{D}$ em $z$) | Modela a matriz de covariância longitudinal $\text{NPS}(f_z)$ |
| **Correlação com Radiologistas** | Moderada a alta em leituras de corte único | Altíssima em modos de leitura clínica real (*stack scrolling/cine*) |
| **Sensibilidade a DLR/IR** | Avalia apenas a regularização planar | Detecta suavizações excessivas ou distorções anisotrópicas no eixo $z$ |

---

## 4. Aplicações em Tomografia Computadorizada Contemporânea

1. **Avaliação de [[Deep Learning Image Reconstruction (DLR)]]:** Algoritmos baseados em redes neurais convolucionais 3D frequentemente aplicam filtragens não-lineares agressivas ao longo do eixo $z$. O SSW-$d'$ é a métrica capaz de diagnosticar se a redução de ruído promovida por DLR preserva a detectabilidade de nódulos pulmonares esféricos milimétricos sem causar o desaparecimento (*smooth-out*) de cortes periféricos da lesão.
2. **Otimização de Espessura e Incremento de Reconstrução:** Permite determinar matematicamente o ponto ótimo de sobreposição de cortes (*slice overlap*), balanceando o aumento de carga computacional contra o ganho efetivo no índice $d'$.
3. **Validação de [[Observadores de Modelo (Model Observers)]] em Fantomas Físicos:** Utilizado em bancadas de controle de qualidade avançadas com fantomas antropomórficos para predizer com precisão os resultados de estudos psicofísicos 2AFC (*Two-Alternative Forced Choice*).

---

## 5. Conexões e Wikilinks

* [[Índice de Detectabilidade]]
* [[Task Transfer Function]]
* [[Noise Power Spectrum]]
* [[Observadores de Modelo (Model Observers)]]
* [[Deep Learning Image Reconstruction (DLR)]]
* [[Reconstrução Iterativa]]
* [[Tomografia Computadorizada]]
* [[AAPM TG-233 - Avaliação de Desempenho em TC]]
* [[Qualidade de Imagem em TC]]
