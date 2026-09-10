---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, reconstrucao-de-imagem, processamento-de-sinal, fbp, filtragem-espacial]
data: 2026-08-25
---

# filtro-de-reconstrucao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **filtro de reconstrução** (frequentemente referido na literatura como *kernel* de reconstrução ou filtro de retroprojeção) é um operador matemático fundamental aplicado no domínio das projeções (sinograma) durante o processo de reconstrução de imagens em Tomografia Computadorizada (TC) por varredura helicoidal ou axial, especificamente no algoritmo de **Retroprojeção Filtrada** (*Filtered Backprojection* - FBP).

Do ponto de vista da física médica e da teoria de sistemas lineares invariantes no espaço (*Shift-Invariant Systems*), a varredura tomográfica reconstrói o objeto medindo a atenuação dos raios X ao longo de múltiplos ângulos, processo formalizado pela **Transformada de Radon**. Quando aplicamos a retroprojeção simples (*Simple Backprojection*) de forma ingênua sobre os dados de projeção adquiridos, o resultado sofre de um desfoque inerente e severo, caracterizado analiticamente no domínio espacial por uma resposta ao impulso pontual proporcional a $\frac{1}{r}$ (onde $r$ é a distância radial). No domínio da frequência espacial, isso equivale a uma ponderação excessiva das baixas frequências espaciais e a uma atenuação inadequada das altas frequências, gerando imagens com perda drástica de resolução de borda e artefatos de borramento.

Para corrigir essa distorção física e matemática, o teorema da fatia central (*Central Slice Theorem*) dita que a transformada de Fourier bidimensional da imagem é equivalente à transformada de Fourier unidimensional das projeções paralelas tomadas em cada ângulo. Para compensar a densidade de amostragem no espaço de Fourier (que cresce linearmente com a frequência radial $f$), aplica-se um filtro corretivo — o **filtro rampa** (*ramp filter*), cuja resposta em frequência é $|f|$. 

Contudo, como o filtro rampa puro amplifica de maneira desmedida as altas frequências espaciais, ele também amplifica o ruído quântico de alta frequência inerente à contagem de fótons de raios X. Portanto, os filtros de reconstrução reais aplicados na prática clínica combinam o filtro rampa com funções de **apodização** (janelamento), criando kernels específicos (ex: suaves/soft, agudos/sharp, dedicados a osso, pulmão ou tecidos moles) que operam como um compromisso otimizado (*trade-off*) entre a **resolução espacial** e a **relação sinal-ruído (SNR)**, impactando diretamente a detectabilidade de lesões e a metrologia quantitativa da imagem tomográfica.

---

## 2. Formulação Matemática e Propriedades

Matematicamente, a operação de filtragem na Retroprojeção Filtrada (FBP) é formulada como uma convolução unidimensional no domínio das projeções ou uma multiplicação no domínio da frequência. 

Seja $P_\theta(t)$ a projeção paralela adquirida no ângulo $\theta$, onde $t$ representa a coordenada espacial ao longo do detector. A projeção filtrada $\tilde{P}_\theta(t)$ é obtida pela convolução de $P_\theta(t)$ com a resposta ao impulso do filtro de reconstrução $k(t)$:

$$
\tilde{P}_\theta(t) = P_\theta(t) * k(t) = \int_{-\infty}^{\infty} P_\theta(\tau) k(t - \tau) \, d\tau
$$

No domínio da frequência espacial, aplicando a Transformada de Fourier unidimensional $\mathcal{F}$, a operação de convolução torna-se uma multiplicação simples:

$$
\mathcal{F}\{\tilde{P}_\theta(t)\} = \hat{P}_\theta(f) \cdot H(f)
$$

Onde:
*   $\hat{P}_\theta(f)$ é a transformada de Fourier da projeção $P_\theta(t)$.
*   $H(f)$ é a função de transferência do filtro no domínio da frequência.

### O Filtro Rampa Ideal e Janelas de Apodização

O filtro rampa ideal é definido por:

$$
H_{\text{ramp}}(f) = |f|
$$

Como $H_{\text{ramp}}(f)$ diverge em altas frequências, amplificando o ruído estatístico a níveis inaceitáveis, multiplicamos o filtro rampa por uma função de janela de apodização $W(f)$ (como Hamming, Hann, Butterworth ou Shepp-Logan). A formulação geral de um filtro de reconstrução prático torna-se:

$$
H(f) = |f| \cdot W(f)
$$

Por exemplo, o **filtro de Shepp-Logan** frequentemente utilizado possui uma formulação analítica no domínio da frequência dada por:

$$
H_{\text{SL}}(f) = |f| \frac{\sin(\pi f / f_c)}{\pi f / f_c} \quad \text{para} \quad |f| \le f_c
$$

Onde $f_c$ representa a frequência de corte (*cut-off frequency*), que define a largura de banda passante e controla diretamente o balanço de ruído e resolução. 

*   **Kernels Agudos (High-pass / Bone):** $W(f)$ decresce lentamente ou estende-se até altas frequências, preservando arestas finas e maximizando a resolução espacial à custa de aumento severo do ruído ($R$).
*   **Kernels Suaves (Low-pass / Soft tissue):** $W(f)$ atenua agressivamente as altas frequências, reduzindo o ruído e suavizando a imagem, o que é ideal para discriminação de contraste de baixo contraste (ex: fígado, cérebro), porém sacrificando a resolução espacial de alto contraste.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A escolha e a calibração do filtro de reconstrução afetam profundamente todas as etapas do fluxo de trabalho em tomografia computadorizada, desde a inspeção visual pelo radiologista até a extração de métricas quantitativas avançadas.

1.  **Controle de Qualidade (CQ) e Metrologia:** Em testes periódicos de aceitação e desempenho de sistemas de TC (seguindo protocolos como ACR, AAPM ou IEC), a função de transferência de modulação (MTF) e o espectro de potência de ruído (NPS - *Noise Power Spectrum*) são estritamente dependentes do kernel de reconstrução selecionado. Alterar o filtro altera a textura do ruído e a resolução limite do sistema.
2.  **Dosimetria e Otimização da Dose:** O princípio ALARA (*As Low As Reasonably Achievable*) exige otimização da dose de radiação. Em varreduras de baixa dose (baixo número de fótons), o uso de kernels muito agudos resulta em imagens excessivamente ruidosas e diagnosticamente imprestáveis. Historicamente, médicos recorriam a doses maiores para viabilizar kernels agudos; hoje, a sinergia entre filtros otimizados, algoritmos de reconstrução iterativa (IR) e inteligência artificial / reconstrução baseada em aprendizado profundo (DLR) permite mitigar o ruído mantendo a nitidez anatómica.
3.  **Radiômica e Biomarcadores de Imagem:** Na era da medicina de precisão, a extração de features radiômicas (texturais, de forma e de intensidade) é altamente sensível a variações técnicas. O filtro de reconstrução atua como um filtro passa-faixa que altera a textura da imagem. Alterar o kernel de reconstrução sem a devida harmonização (*feature harmonization* ou *filter-based image standardization*) invalida modelos preditivos de machine learning, tornando a padronização do kernel um requisito crítico em estudos multicêntricos.
4.  **Aparate de Visualização (Janelamento de Imagem):** Diferentes estruturas anatômicas exigem kernels específicos (ex: pulmão com kernel afiado para visualização do interstício e pequenos nódulos; cérebro com kernel suave para evitar ruído em áreas homogêneas de parênquima).

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|tomografia-computadorizada]]
*   [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
*   [[Transformada de Radon|transformada-de-radon]]
*   [[Teorema da Fatia Central|teorema-da-fatia-central]]
*   [[Modulation Transfer Function (MTF)|funcao-de-transferencia-de-modulacao-mtf]]
*   [[Noise Power Spectrum|espectro-de-potencia-de-ruido-nps]]
*   [[Reconstrução Iterativa|reconstrucao-iterativa]]
*   [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction-dlr]]
*   [[Radiomica]]
*   [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]