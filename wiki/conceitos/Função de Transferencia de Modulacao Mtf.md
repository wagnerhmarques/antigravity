---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, resolucao-espacial, metrologia, processamento-de-sinal]
data: 2026-08-25
---

# funcao-de-transferencia-de-modulacao-mtf

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Transferência de Modulação** (MTF - *Modulation Transfer Function*) é a métrica padrão-ouro na física médica e na metrologia de imagem para quantificar a **resolução espacial** e a fidelidade de reprodução de detalhes de sistemas de imageamento, com papel central na [[Tomografia Computadorizada|tomografia-computadorizada]]. Em termos fundamentais, a MTF descreve a capacidade de um sistema de imagem de transferir o contraste de um objeto para a imagem reconstruída, em função da frequência espacial (detalhes por unidade de comprimento, tipicamente expressos em pares de linhas por centímetro, $\text{lp/cm}$, ou milímetro, $\text{lp/mm}$).

Do ponto de vista da teoria linear de sistemas (LSI - *Linear Space-Invariant Systems*), um sistema de tomografia computadorizada pode ser modelado, sob certas aproximações, como um operador linear que degrada a informação espacial contida no objeto anatômico. Quando uma estrutura de alta frequência espacial — caracterizada por transições abruptas de densidade (como microcalcificações ou trabeculações ósseas finas) — é escaneada, o tamanho finito do ponto focal do tubo de raios X, os efeitos de amostragem (*sampling*) da matriz de detecção, os filtros de reamostragem e os algoritmos de reconstrução ([[FBP|filtro-de-retroprojecao-filtrada]], [[Reconstrução Iterativa|reconstrucao-iterativa]]) provocam um espalhamento e uma perda de amplitude do sinal.

A modulação $M$ de um sinal senoidal de densidade óptica ou número CT é definida como:

$$
M = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}
$$

onde $I_{\max}$ e $I_{\min}$ representam, respectivamente, as intensidades máxima e mínima do padrão senoidal. A MTF para uma dada frequência espacial $f$ é, portanto, a razão entre a modulação da imagem ($\text{Modulação}_{\text{imagem}}$) e a modulação do objeto original ($\text{Modulação}_{\text{objeto}}$):

$$
\text{MTF}(f) = \frac{\text{Modulação}_{\text{imagem}}(f)}{\text{Modulação}_{\text{objeto}}(f)}
$$

Por convenção, a MTF é normalizada para o valor unitário na frequência zero ($\text{MTF}(0) = 1$), indicando perfeita retenção do componente de fundo (DC). Conforme a frequência espacial aumenta, a MTF decresce monotonicamente até atingir valores próximos a zero, ponto no qual o sistema torna-se incapaz de distinguir o sinal do ruído de fundo. Na prática clínica e no controle de qualidade, a frequência em que a MTF decai para $10\%$ ($f_{10}$) ou $50\%$ ($f_{50}$) do seu valor máximo é frequentemente utilizada como descritor quantitativo da resolução espacial limiar e de meia-altura, respectivamente.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, a resposta de um sistema de imagem a um estímulo infinitesimal é descrita pela Função de Espalhamento de Ponto ([[esf-psf-lsf-em-tc|PSF - *Point Spread Function*]]). Se a PSF do sistema for bidimensional e denotada por $\text{PSF}(x, y)$, a imagem resultante de um objeto $O(x, y)$ é obtida pela operação de convolução ($\ast$):

$$
I(x, y) = O(x, y) \ast \text{PSF}(x, y) + n(x, y)
$$

onde $n(x, y)$ representa o ruído estocástico inerente ao sistema de aquisição.

A **Função de Transferência Óptica** (OTF - *Optical Transfer Function*) é definida como a Transformada de Fourier bidimensional da PSF normalizada:

$$
\text{OTF}(f_x, f_y) = \frac{\mathcal{F} \left\{ \text{PSF}(x, y) \right\}}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx\, dy}
$$

Como a OTF é uma função complexa, ela pode ser decomposta em sua magnitude e fase:

$$
\text{OTF}(f_x, f_y) = \text{MTF}(f_x, f_y) \cdot e^{i \Phi(f_x, f_y)}
$$

A **MTF** corresponde estritamente ao módulo da OTF:

$$
\text{MTF}(f_x, f_y) = \left| \text{OTF}(f_x, f_y) \right| = \left| \frac{\iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-i 2\pi (f_x x + f_y y)} \, dx\, dy}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx\, dy} \right|
$$

A fase $\Phi(f_x, f_y)$ representa o deslocamento de fase ou assimetria introduzido pelo sistema, que idealmente é nulo em sistemas simétricos.

### Métodos Metrológicos de Medição da MTF em TC:
1. **Método da PSF Direta:** Utilização de um fio fino de alto número atômico (ex: tungstênio ou platina) posicionado axialmente para estimar a PSF ou a Função de Espalhamento de Linha ([[esf-psf-lsf-em-tc|LSF]]). A LSF unidimensional é obtida por perfilometria e sua Transformada de Fourier gera diretamente a MTF:
   
$$
\text{MTF}(f) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-i 2\pi f x} \, dx \right|
$$

2. **Método da ESF (*Edge Spread Function*):** Utilização de uma borda afiada (fantasmas de teste com interfaces de teflon, poliestireno ou ar). Derivando a ESF obtém-se a LSF, cuja transformada fornece a MTF. É o método mais amplamente automatizado nos protocolos de garantia de qualidade.
3. **Método do Ruído (Power Spectrum Analysis):** Análise do espectro de potência do ruído espacial em imagens de uniformidade de água, correlacionando a textura do ruído com a MTF do sistema sob certas condições de estacionaridade.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A MTF é um pilar indispensável no design, comissionamento, controle de qualidade e otimização de protocolos em tomografia computadorizada. Suas aplicações práticas desdobram-se em várias frentes:

* **Escolha do Kernel de Reconstrução:** Os núcleos de reconstrução (filtros de rampa, *sharp*, *smooth*) modificam diretamente a MTF do sistema. Kernels agudos (*sharp*) elevam a MTF em altas frequências, preservando bordas finas e melhorando a resolução espacial, em detrimento de uma amplificação severa do ruído quântico. Kernels suaves (*smooth*) suprimem altas frequências, degradando a MTF, mas reduzindo o ruído, sendo ideais para a detecção de lesões hepáticas de baixo contraste.
* **Compromiso entre Resolução e Ruído:** Na otimização da dose de radiação, a relação entre a MTF e a [[funcao-de-dispersao-do-negativoruido-npd]] (NPS - *Noise Power Spectrum*) dita a Detectabilidade Visual de Lesões através da Teoria de Observadores (ex: *Detective Quantum Efficiency* - DQE).
* **Inteligência Artificial e Reconstrução Baseada em Aprendizado Profundo (DLR):** Algoritmos modernos de DLR frequentemente alteram a MTF de maneira não-linear dependendo do nível de sinal e da frequência espacial. O monitoramento da MTF em redes neurais de reconstrução é crucial para evitar artefatos de alucinação e perda de textura anatômica sutil, assegurando que a resolução espacial permaneça isotrópica e clinicamente fiel.
* **Controle de Qualidade Regulatório:** Programas de garantia de qualidade exigem o rastreamento periódico da MTF ($50\%$ e $10\%$ da linha de base) para detectar degradações mecânicas no tubo de raios X, desgaste do gerador ou desalinhamentos no eixo de rotação do gantry.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[esf-psf-lsf-em-tc]]
* [[funcao-de-dispersao-do-negativoruido-npd]]
* [[FBP|filtro-de-retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Artefatos em Tomografia Computadorizada|artefatos-em-tomografia-computadorizada]]
* [[Dosimetria em Radiologia|dosimetria-e-otimizacao-em-tc]]