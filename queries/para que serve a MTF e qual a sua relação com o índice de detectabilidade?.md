> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Task Transfer Function|Função de Transferência de Modulação (MTF)]], [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]]

> 📅 **Data:** 2026-08-28 | 🔗 **Conexões:** [[Task Transfer Function|Função de Transferência de Modulação (MTF)]], [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]]

## 1. Papel e Fundamentação da Função de Transferência de Modulação (MTF)

A **Função de Transferência de Modulação (MTF)** é a métrica padrão-ouro para caracterizar a resolução espacial em sistemas lineares e invariantes no espaço (LSI). Ela expressa quantitativamente a capacidade de um sistema de imagem tomográfica de reproduzir o contraste de um objeto em função da frequência espacial ($f$). 

Matematicamente, a MTF é obtida a partir da magnitude normalizada da Transformada de Fourier da [[Point Spread Function (PSF)|point-spread-function]] ($\text{PSF}$):

$$
\text{MTF}(u, v) = \frac{\left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-i 2\pi (ux + vy)} \\, dx \\, dy \right|}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \\, dx \\, dy}
$$

Em sistemas radiológicos e tomográficos modernos, a MTF atua como o descritor fundamental da fidelidade espacial de alto contraste, definindo os limites operacionais de frequências de corte (como $\text{MTF}_{50%}$ e $\text{MTF}_{10%}$). No entanto, devido à não-linearidade imposta por algoritmos avançados de [[Reconstrução Iterativa|reconstrucao-iterativa]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]], a MTF tradicional evolui para a **Função de Transferência de Tarefa** ([[Task Transfer Function|task-transfer-function]]), que incorpora a dependência do contraste e do nível de ruído local.

---

## 2. Relação Teórica entre MTF (ou TTF) e o Índice de Detectabilidade ($d'$)

O **Índice de Detectabilidade** ($d'$, *d-prime*), formalizado pelo relatório [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]], unifica a resolução espacial e a textura do ruído em um único indicador objetivo de qualidade de imagem baseada em tarefas ([[Task Based Image Quality|task-based-image-quality]]). 

No modelo analítico para um observador linear ideal com pré-branqueamento (Hotelling / PW) no domínio da frequência espacial bidimensional $\mathbf{u} = (u, v)$, a MTF (substituída pela [[Task Transfer Function|Task Transfer Function]] para contemplar o contraste específico do objeto) compõe o numerador do índice $d'$:

$$
{d'}^2_{\text{PW}} = \iint_{-\infty}^{\infty} \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2}{\text{NPS}(u, v)} \\, du \\, dv
$$

Onde:
* $W_{\text{task}}(u, v)$ representa a transformada de Fourier da função de tarefa clínica (geometria e diferença de atenuação do sinal de interesse);
* $\text{TTF}(u, v)$ é a extensão da MTF para tarefas específicas de baixo ou alto contraste;
* $\text{NPS}(u, v)$ é o [[Noise Power Spectrum|Noise Power Spectrum]], que quantifica a potência e a distribuição espacial do ruído estocástico.

---

## 3. Análise Crítica e Otimização Multiobjetivo

A relação matemática evidencia que a detectabilidade de uma lesão não depende isoladamente de uma alta resolução espacial ($\text{TTF}$ alta), mas sim do equilíbrio rigoroso entre a preservação do sinal em altas frequências e a amplificação do ruído descrita pelo $\text{NPS}$. 

No contexto do projeto de Doutorado Direto FAPESP no InRad-HCFMUSP, o uso conjunto de $d'$ e da $\text{TTF}$ permite avaliar de forma robusta os 7 tomógrafos clínicos, otimizando protocolos de varredura frente a reduções drásticas de dose e quantidade de meio de contraste.
