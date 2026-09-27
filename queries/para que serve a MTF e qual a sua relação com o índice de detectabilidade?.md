> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Task Transfer Function|Função de Transferência de Modulação (MTF)]], [[Índice de Detectabilidade]], [[Task Transfer Function]], [[Noise Power Spectrum]], [[Observadores de Modelo (Model Observers)]]

## 1. Propósito e Fundamentação Física da MTF

A **Função de Transferência de Modulação (MTF)** é a métrica padrão-ouro na física radiológica e teoria de sistemas lineares para avaliar quantitativamente a **resolução espacial** de um sistema de imagem. O seu principal propósito é descrever a capacidade do tomógrafo de preservar e transferir o contraste de um objeto de entrada para a imagem reconstruída em função da frequência espacial ($f$).

Matematicamente, em sistemas lineares e invariantes no espaço (LSI), a MTF representa o módulo normalizado da Transformada de Fourier 2D da [[Point Spread Function (PSF)]]:

$$
\text{MTF}(u, v) = \frac{\left| \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-i 2\pi (ux + vy)} \\, dx \\, dy \right|}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \\, dx \\, dy}
$$

### Aplicações Primárias da MTF:
* **Caracterização da Nitidez do Sistema:** Quantifica a atenuação de altas frequências espaciais (bordas e detalhes finos).
* **Pontos de Corte Diagnósticos:** Utiliza-se a $\text{MTF}_{50\%}$ para avaliar o contraste intermediário e a $\text{MTF}_{10\%}$ para determinar o limite teórico de resolução espacial de alto contraste.
* **Benchmarking de Hardware:** Permite comparar detectores, focos do tubo de raios-X e filtros de reconstrução padrão (kernels duros vs. macios).

---

## 2. Transição da MTF para a TTF em Tomografia Computadorizada

Em [[Tomografia Computadorizada]] moderna, o uso de algoritmos de [[Reconstrução Iterativa]] e [[Deep Learning Image Reconstruction (DLR)]] introduz comportamento **não-linear e dependente de ruído/contraste**. Nessas condições, a MTF clássica perde sua validade universal.

Para contornar essa limitação, o relatório **[[AAPM TG-233 - Avaliação de Desempenho em TC]]** padronizou o uso da **[[Task Transfer Function]] (TTF)**. A TTF mede a resposta em frequência adaptada para inserções de contrastes específicos ($\Delta \text{HU}$), servindo como a generalização prática da MTF para sistemas modernos não-lineares.

---

## 3. Relação Direta entre a MTF/TTF e o Índice de Detectabilidade ($d'$)

A relação entre a MTF/TTF e o **[[Índice de Detectabilidade]] ($d'$)** é de **interdependência matemática e física fundamental**: enquanto a MTF/TTF mede unicamente a resolução espacial, o índice $d'$ sintetiza a qualidade de imagem baseada em tarefas (*Task-Based Image Quality*), combinando a MTF/TTF, o espectro de ruído e a geometria da lesão em uma única métrica de desempenho de detecção.

### A. Formulação do Observador Ideal (Hotelling / Prewhitening)
No domínio de Fourier bidimensional $\mathbf{u} = (u, v)$, a resposta de resolução espacial dada pela $\text{TTF}(u, v)$ (ou $\text{MTF}$) atua modulando diretamente a **Função de Tarefa** $W_{\text{task}}(u, v)$ do sinal diagnóstico:

$$
d'^2_{\text{PW}} = \iint_{-\infty}^{\infty} \frac{\left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2}{\text{NPS}(u, v)} \\, du \\, dv
$$

Onde:
* $W_{\text{task}}(u, v)$: Representação no domínio da frequência do tamanho e formato da lesão/sinal ($
\mathcal{F}\{\Delta \mu(x,y)\}$).
* $\text{NPS}(u, v)$: [[Noise Power Spectrum]], que descreve a potência e textura estocástica do ruído.

### B. Formulação do Observador Antropomórfico (NPWE)
Ao modelar a percepção visual do médico radiologista via [[Observadores de Modelo (Model Observers)]], o filtro do olho humano $E(u, v)$ e o ruído interno de decisão $\sigma_{\text{int}}$ são integrados. A MTF/TTF determina o ganho de sinal transmitido ao observador:

$$
d'^2_{\text{NPWE}} = \frac{\left[ \iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \left[ E(u, v) \right]^2 \\, du \\, dv \right]^2}{\iint_{-\infty}^{\infty} \left| W_{\text{task}}(u, v) \right|^2 \cdot \left[ \text{TTF}(u, v) \right]^2 \cdot \text{NPS}(u, v) \cdot \left[ E(u, v) \right]^4 \\, du \\, dv + \sigma_{\text{int}}^2}
$$

### C. Impacto Prático da MTF no Cálculo do $d'$:
1. **Filtro de Frequência do Sinal:** A MTF/TTF funciona como um filtro passa-baixas do sistema. Quanto maior a MTF nas frequências onde o sinal $W_{\text{task}}$ possui maior energia, maior será o valor do numerador de $d'$, resultando em maior facilidade de detecção da lesão.
2. **Acoplamento Sinal-Ruído:** Uma MTF elevada em frequências altas melhora a definição das bordas do sinal, mas se a reconstrução também inflar o $\text{NPS}$ nessas mesmas frequências (ruído de alta frequência), o índice $d'$ pondera esse compromisso (*trade-off*).

---

## 4. Comparativo Síntese das Métricas

| Métrica | O que mede? | Dependência de Tarefa Clinica? | Sensível ao Ruído? | Papel no Projeto de TC |
| :--- | :--- | :--- | :--- | :--- |
| **MTF / TTF** | Resolução espacial e transferência de contraste por frequência. | Não (MTF) / Parcial (TTF por contraste). | Não (calculada isoladamente). | Parâmetro isolado de nitidez do sistema. |
| **NPS** | Potência e textura espacial do ruído estocástico. | Não. | Sim (é a própria métrica de ruído). | Parâmetro isolado de textura e variância. |
| **$d'$ (Detectabilidade)** | Capabilidade de um observador detectar/localizar uma lesão. | **Sim** (depende de $W_{\text{task}}$ e do observador). | **Sim** (integra TTF e NPS no denominador/numerador). | **Métrica Mestre de Otimização** (Qualidade Baseada em Tarefas). |
