---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, resolucao-espacial, processamento-de-sinal]
data: 2026-08-25
---

# Funcao de Modulacao (FTM)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Modulação** (frequentemente referida como *Modulation Transfer Function* - MTF, ou FTM em português) constitui a ferramenta métrica fundamental na Física Médica e na Engenharia de Imagem para a caracterização quantitativa da **resolução espacial** e da **fidelidade de transferência de contraste** de sistemas de imagem, com ênfase particular na Tomografia Computadorizada (TC). 

Fisicamente, qualquer sistema de imagem real atua como um filtro passa-baixas linear e espacialmente invariante (ou localmente invariante) sobre a distribuição de atenuação real do objeto escaneado. Devido a limitações fundamentais — tais como o tamanho finito do ponto focal do tubo de raios X, o *pitch* e a abertura espacial dos elementos do arranjo de detetores (*detector array*), o processo de amostragem (*sampling*) e os núcleos de retroprojeção filtrada (*reconstruction kernels*) — detalhes espaciais finos sofrem atenuação em sua amplitude e perda de contraste.

A FTM é formalmente definida como o módulo da transformada de Fourier da **Função de Resposta ao Impulso** (FRIs ou *Point Spread Function* - PSF) do sistema. Em termos metrológicos, a FTM expressa a capacidade do sistema de reproduzir o contraste de um objeto senoidal em função da sua frequência espacial (normalmente expressa em pares de linhas por centímetro, $\text{lp/cm}$, ou ciclos por milímetro, $\text{mm}^{-1}$). 

Matematicamente, se uma entrada senoidal de frequência espacial $u$ e contraste inicial $C_0$ é imageada pelo sistema, produzindo uma saída com contraste $C_i$, a FTM para essa frequência específica é dada por:

$$
\text{FTM}(u) = \frac{C_i(u)}{C_0(u)}
$$

onde o contraste $C$ é tipicamente calculado em termos da modulação da intensidade (sinal máximo $I_{\max}$ e mínimo $I_{\min}$):

$$
C = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}
$$

Uma FTM ideal perfeita seria igual a $1$ para todas as frequências espaciais imagináveis. Contudo, em sistemas reais de TC, a FTM decresce monotonicamente de $1$ (na frequência zero, ou componente contínua) até $0$ (frequência de corte, onde o sistema deixa de resolver estruturas e o sinal funde-se completamente com o ruído quântico).

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Seja $h(x, y)$ a Função de Resposta ao Impulso bidimensional (PSF) de um sistema de aquisição e reconstrução de TC em um plano ortogonal ao eixo longitudinal do paciente ($z$). A FTM bidimensional, denotada por $M(u, v)$, onde $u$ e $v$ representam as frequências espaciais nas direções $x$ e $y$, é definida como a magnitude da Transformada de Fourier bidimensional de $h(x, y)$:

$$
M(u, v) = \left| \iint_{-\infty}^{\infty} h(x, y) e^{-j 2 \pi (ux + vy)} \, dx \, dy \right|
$$

Em virtude da simetria rotacional frequentemente assumida ou avaliada em tomografia, a FTM é comumente reduzida a uma função radial unidimensional $M(f)$, onde $f = \sqrt{u^2 + v^2}$.

### Propriedades Matemáticas Relevantes:

1. **Normalização:** A FTM é normalizada no limite de frequência zero para assegurar que a resposta ao sinal DC seja unitária:
   
   
$$
M(0) = 1
$$

2. **Teorema da Convolução:** Se um sistema complexo é composto por múltiplos estágios lineares sucessivos (por exemplo, tamanho do ponto focal $h_{\text{focal}}(x,y)$, abertura do detetor $h_{\text{det}}(x,y)$ e filtro de reconstrução $h_{\text{recon}}(x,y)$), a PSF total é a convolução das PSFs individuais:
   
   
$$
h_{\text{total}}(x, y) = h_{\text{focal}}(x, y) * h_{\text{det}}(x, y) * h_{\text{recon}}(x, y)
$$

   
   Consequentemente, pela propriedade da transformada de Fourier, a FTM global do sistema é o produto direto das FTMs de cada componente independente:
   
   
$$
M_{\text{total}}(f) = M_{\text{focal}}(f) \cdot M_{\text{det}}(f) \cdot M_{\text{recon}}(f)
$$

3. **Frequência de Corte ($f_c$):** Definida como a frequência espacial na qual a FTM decresce a um limiar perceptivo ou técnico específico (frequentemente $M(f_c) = 0.1$ ou $0.02$, correspondendo a $10\%$ ou $2\%$ da modulação original), delimitando a máxima resolução espacial recuperável antes que a relação sinal-ruído se torne proibitiva.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica e industrial da Tomografia Computadorizada, a FTM é o parâmetro central para o **Controle de Qualidade (CQ)**, otimização de protocolos de aquisição e desenvolvimento de algoritmos avançados de reconstrução.

### 1. Seleção de Filtros de Reconstrução (*Kernels*)
Os fabricantes de scanners de TC fornecem uma vasta gama de *kernels* de retroprojeção filtrada (FBP). *Kernels* agudos (*sharp kernels*, ex: para osso ou alta resolução pulmonar) amplificam as altas frequências espaciais, preservando uma FTM elevada em frequências maiores, o que melhora a visualização de trabecular óssea ou microestruturas pulmonares — em detrimento, contudo, de uma severa degradação da relação sinal-ruído (aumento drástico do ruído quântico). Em contrapartida, *kernels* suaves (*smooth kernels*, ex: para fígado ou cérebro) deprimem a FTM nas altas frequências, suprimindo o ruído às custas da borramento (*blurring*) de bordas anatômicas.

### 2. Métodos de Medição Experimental
Como a medição direta da PSF por meio de uma fonte pontual ideal é impraticável na física médica devido à impossibilidade de criar um ponto infinitesimal de raios X com fluxo adequado, a FTM na TC é comumente derivada por meio de métodos alternativos normalizados:
* **Método do Fio Delgado (*Wire Method*):** Imageamento de um fio metálico de alta atenuação (geralmente tungstênio ou platina com diâmetro $< 0.1 \text{ mm}$), cuja linha de perfil fornece a Função de Resposta de Linha (LSF). A FTM é obtida pela transformada de Fourier unidimensional da LSF.
* **Método da Borda (*Edge Method*):** Utilização de um cilindro ou placa de alto contraste (teflon, poliestireno ou metal) para gerar uma Função de Resposta ao Degrau (*Edge Spread Function* - ESF). A diferenciação da ESF produz a LSF, e subsequentemente, a FTM.

### 3. Impacto da Inteligência Artificial e Reconstrução Iterativa (IR / DLR)
Com a ascensão da Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR) e algoritmos iterativos avançados, a manutenção de uma FTM linear e invariante tornou-se um desafio complexo. Redes neurais convolucionais (CNNs) treinadas para redução de ruído podem introduzir respostas dependentes do contraste e não-lineares. A avaliação da FTM em sistemas DLR requer metodologias baseadas em tarefas (*task-based MTF*), muitas vezes acopladas à [[Detectabilidade Ideal]] e ao [[Noise Power Spectrum|Espectro de Potência de Ruído (NPS)]], garantindo que a supressão de ruído não ocorra à custa da perda de detectabilidade de lesões de baixo contraste (como nódulos hepáticos incipientes).

---

## 4. Conexões e Wikilinks

* [[Função de Resposta ao Impulso (PSF)]]
* [[Noise Power Spectrum|Espectro de Potência de Ruído (NPS)]]
* [[Detectabilidade Ideal e Observadores Computacionais]]
* [[FBP|Retroprojeção Filtrada (FBP)]]
* [[Reconstrução Baseada em Aprendizado Profundo (DLR)]]
* [[Controle de Qualidade em Tomografia Computadorizada]]
* [[Resolução Espacial e Contraste em Imagem Médica]]