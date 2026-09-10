> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Noise Power Spectrum]], [[Transformada de Fourier 2D]], [[Ruído Quântico]], [[Reconstrução Iterativa]], [[Deep Learning Image Reconstruction (DLR)]]

## 1. Introdução e Definição Conceitual

O **Espectro de Potência do Ruído** (*Noise Power Spectrum* - NPS), formalmente conhecido na literatura clássica como a função de Wiener do ruído, é a métrica padrão-ouro estabelecida pela física médica moderna (e recomendada pelo relatório do [[aapm-tg233-ct-performance|aapm-tg-233-summary]]) para caracterizar as propriedades estatísticas e espaciais do ruído em imagens de Tomografia Computadorizada (TC).

Enquanto o desvio padrão convencional ($\sigma$) mede apenas a **magnitude** (amplitude absoluta) da flutuação de densidade em unidades Hounsfield ($HU$), o NPS descreve a **textura do ruído** (granulometria espacial), quantificando como a potência das flutuações estocásticas está distribuída ao longo das diferentes frequências espaciais no domínio de Fourier.

Com o advento de algoritmos avançados de reconstrução não-linear — como a [[reconstrucao-iterativa]] (IR) e a [[deep-learning-image-reconstruction|reconstrução baseada em deep learning (DLR)]] —, o ruído da imagem deixou de se comportar como um "ruído branco" uniforme e passou a exibir padrões texturais complexos, tornando o NPS indispensável para a avaliação de qualidade de imagem baseada em tarefas ([[task-based-image-quality]]).

---

## 2. Formulação Matemática do NPS Bidimensional ($NPS_{2D}$)

O cálculo prático do NPS bidimensional a partir de imagens digitais de TC envolve a extração de regiões de interesse ($ROI$) homogêneas (geralmente em phantoms de água ou acrílico) e a aplicação da Transformada Rápida de Fourier ($FFT$).

Matematicamente, o $NPS_{2D}$ em coordenadas de frequência espacial $(f_x, f_y)$ é definido como:

$$
NPS_{2D}(f_x, f_y) = \frac{\Delta_x \Delta_y}{L_x L_y} \cdot \frac{1}{N_{\text{ROI}}} \sum_{i=1}^{N_{\text{ROI}}} \left| \text{FFT}_{2D} \left\{ \text{ROI}_i(x,y) - \text{FIT}_i(x,y) \right\} \right|^2
$$

Onde:
* $\Delta_x, \Delta_y$: Tamanho físico do pixel nas direções $x$ e $y$ (em mm);
* $L_x, L_y$: Dimensões físicas da região de interesse ($ROI$) nas respectivas direções;
* $N_{\text{ROI}}$: Número total de amostras de $ROI$ analisadas;
* $\text{ROI}_i(x,y)$: Matriz de densidades (em $HU$) da $i$-ésima região;
* $\text{FIT}_i(x,y)$: Ajuste polinomial (geralmente de 2ª ordem) subtraído da $ROI$ para remover variações de baixa frequência decorrentes de artefatos de inomogeneidade ou de feixe (*beam hardening*).

---

## 3. Redução Radial e Métricas Derivadas

Para facilitar a comparação visual e quantitativa entre diferentes algoritmos e protocolos de aquisição, o $NPS_{2D}$ cartesiano é frequentemente convertido em um perfil unidimensional radial ($NPS_{1D}$) através de integração polar:

$$
NPS_{1D}(f) = \int_{0}^{2\pi} NPS_{2D}(f \cos\theta, f \sin\theta) \, \, d\theta
$$

A partir do perfil do NPS\, duas métricas fundamentais são extraídas:

1. **Magnitude Global do Ruído:** Calculada pela raiz quadrada da área integrada sob a curva do NPS, correspondendo diretamente ao desvio padrão global da imagem:
   

$$
\sigma_{\text{NPS}} = \sqrt {\iint NPS_{2D}(f_x, f_y)\, df_x\, df_y}
$$

2. **Frequência Espacial Média ($f_{av}$):** Indicador quantitativo da textura do ruído\, definido como o primeiro momento ponderado do espectro:
   

$$
f_{av} = \frac{\int f \cdot NPS_{1D}(f)\, df}{\int NPS_{1D}(f)\, df}
$$

   * **Valores elevados de $f_{av}$:** Indicam granulação de ruído fina (frequências espaciais altas), que é visualmente mais aceita por radiologistas.
   * **Valores baixos de $f_{av}$:** Indicam deslocamento do ruído para baixas frequências, gerando texturas grosseiras, borramentos ou o indesejado "aspecto plástico" típico de gerações antigas de IR ([[solomon-2016-observer-models]]).

---

## 4. O NPS na Prática: Comportamento Comparativo (IR vs. DLR)

Estudos multicêntricos recentes ([[greffier-2026-dlr-ct-phantom]]) demonstram que a análise por NPS revela o real impacto físico de diferentes abordagens de reconstrução em exames de tomografia:

| Característica Espectral | Retroprojeção Filtrada (FBP) | Reconstrução Iterativa (IR) | Reconstrução Deep Learning (DLR) |
| :--- | :--- | :--- | :--- |
| **Formato da Curva NPS** | Amplo, próximo ao ruído branco | Deslocado para baixas frequências (*red noise*) | Deslocado para altas frequências (*blue noise*) |
| **Magnitude do Ruído** | Alta (dependente da dose) | Moderadamente reduzida | Drasticamente reduzida (até $-80\%$ em ultrabaixa dose) |
| **Textura Visual** | Granular e uniforme | Borrada ou plástica | Fina, preservando o parênquima natural |

---

## 5. Importância Crítica para o Índice de Detectabilidade ($d'$)

O Espectro de Potência de Ruído não atua apenas como uma métrica isolada de física instrumental; ele é componente obrigatório e no denominador da formulação matemática do [[Índice de Detectabilidade]] ($d'$), conforme a teoria de observadores de modelo ([[model-observers|observadores-de-modelo]]):

$$
{d'}^2 = \frac{ \left[ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot E^2(u,v)\, du\, dv \right]^2 }{ \iint \left| W(u,v) \right|^2 \cdot \text{TTF}^2(u,v) \cdot \mathbf{NPS}(u,v) \cdot E^2(u,v)\, du\, dv }
$$

Como o $NPS(u,v)$ pondera o impacto estatístico do ruído em cada frequência espacial, variações na textura do ruído causadas por algoritmos de processamento são capturadas com rigor matemático pelo $d'$, permitindo correlacionar perfeitamente a física do equipamento com a acurácia diagnóstica humana em estudos psicofísicos ([[projeto-dd-fapesp-wagner-2026]]).

---

## 🔗 Referências Cruzadas na Wiki
- [[noise-power-spectrum|espectro-de-potencia-de-ruido-nps]]
- [[Task Transfer Function]]
- [[indice-de-detectabilidade|detectability-index]]
- [[aapm-tg233-ct-performance|aapm-tg-233-summary]]
- [[greffier-2026-dlr-ct-phantom]]
- [[model-observers|observadores-de-modelo]]
- [[solomon-2016-observer-models]]
