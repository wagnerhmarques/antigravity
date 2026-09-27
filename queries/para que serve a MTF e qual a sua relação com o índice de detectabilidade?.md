> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Task Transfer Function|Função de Transferência de Modulação (MTF)]], [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]]

> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Task Transfer Function|Função de Transferência de Modulação (MTF)]], [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]]

## 1. Fundamentação e Papel da MTF na Qualidade de Imagem

A **Função de Transferência de Modulação (MTF)** é a métrica padrão-ouro para caracterizar a **resolução espacial** de sistemas de imagem linear e invariante no espaço (LSI). Ela quantifica a capacidade do sistema tomográfico em reproduzir a modulação de contraste de um objeto em função da frequência espacial ($f$).

Matematicamente, a MTF é a magnitude normalizada da Transformada de Fourier da [[Point Spread Function (PSF)|point-spread-function]] ($\text{PSF}$):

$$
\text{MTF}(u, v) = \frac{\left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-i 2\pi (ux + vy)} \\, dx \\, dy \right|}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \\, dx \\, dy}
$$

A principal utilidade da MTF reside na avaliação objetiva da nitidez e da preservação de detalhes anatômicos de alto contraste, estabelecendo os limites de resolução do sistema por meio das frequências de corte (como $\text{MTF}_{10\%}$ e $\text{MTF}_{50\%}$). Em sistemas modernos com [[Reconstrução Iterativa|reconstrucao-iterativa]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]], a MTF tradicional perde validade devido à não-linearidade, sendo substituída pela **[[Task Transfer Function|Task Transfer Function]]** ($\text{TTF}$), que incorpora a dependência do contraste e do nível de ruído.

---

## 2. Relação Direta entre MTF/TTF e o Índice de Detectabilidade ($d'$)

O **Índice de Detectabilidade** ($d'$) formalizado pelo relatório [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]] unifica as dimensões físicas da imagem em um único descritor de desempenho em tarefas diagnósticas específicas. A resolução espacial representada pela $\text{MTF}$ (ou $\text{TTF}$) atua como o numerador na transferência de sinal do observador.

No modelo do observador linear ideal com pré-branqueamento (Hotelling / PW), o quadrado do índice de detectabilidade é expresso no domínio da frequência espacial bidimensional por:

$$
{d'}^2_{\text{PW}} = \iint_{-\infty}^{\infty} \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2}{\text{NPS}(u, v)} \\, du \\, dv
$$

Onde:
* $W_{\text{task}}(u, v)$ é a transformada de Fourier da função de tarefa (geometria e contraste da lesão);
* $\text{TTF}(u, v)$ é a extensão da MTF para tarefas específicas e sistemas não-lineares;
* $\text{NPS}(u, v)$ é o [[Noise Power Spectrum|Noise Power Spectrum]], que caracteriza a magnitude e a textura estocástica do ruído.

Para observadores antropomórficos com filtro visual humano ([[Observadores de Modelo (Model Observers)|model-observers]] do tipo NPWE), a relação assume a forma:

$$
{d'}^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \\, du \\, dv \right]^2}{\iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \text{NPS}(u, v) \cdot \left[ E(u, v) \right]^4 \\, du \\, dv + \sigma_{\text{int}}^2}
$$

---

## 3. Síntese Comparativa das Métricas de Desempenho

| Métrica Física / Tarefa | Domínio de Avaliação | Função Principal no Sistema | Dependência de Ruído | Inclusão de Percepção Humana |
| :--- | :--- | :--- | :--- | :--- |
| **[[Task Transfer Function|MTF]]** | Frequência Espacial | Medir resolução espacial em sistemas lineares | Não | Não |
| **[[Task Transfer Function|TTF]]** | Frequência Espacial | Medir resolução dependente de contraste e ruído | Sim (indiretamente) | Não |
| **[[Noise Power Spectrum|NPS]]** | Frequência Espacial | Caracterizar textura e potência do ruído | Sim (diretamente) | Não |
| **[[Índice de Detectabilidade]] ($d'$)** | Estatístico / Tarefa | Unificar qualidade diagnóstica em termos de $H_0$ vs $H_1$ | Sim (NPS no denominador) | Sim (via modelos PW, NPWE ou CHO) |

---

## 4. Relevância para o Projeto de Doutorado e Prática Clínica

No escopo da otimização multiobjetivo em Tomografia Computadorizada no InRad-HCFMUSP:
1. **Trade-off Dose vs. Resolução:** A simples maximização da MTF/TTF eleva o ruído na imagem ($\text{NPS}$). O índice $d'$ resolve este dilema ao ponderar rigorosamente o ganho de resolução espacial frente à amplificação do ruído estocástico.
2. **Validação de Algoritmos Avançados:** Permite mensurar objetivamente se técnicas de reconstrução iterativa e deep learning preservam o sinal patológico sem introduzir artefatos de textura indesejados.
