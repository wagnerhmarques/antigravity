---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, resolucao-espacial, processamento-de-sinal]
data: 2026-08-25
---

# Funcao_de_Transferencia_Modular_MTF

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Transferência Modular** (do inglês *Modulation Transfer Function* - **MTF**) é a métrica padrão-ouro na física de imagens médicas e na metrologia de sistemas de Tomografia Computadorizada (TC) para quantificar a **resolução espacial**. Ela descreve a capacidade de um sistema de imagem em transferir o contraste de detalhes espaciais de um objeto real para a imagem reconstruída, em função da frequência espacial (frequência de ciclos por unidade de comprimento, tipicamente expressa em pares de linhas por centímetro, $\text{lp/cm}$, ou milímetro, $\text{lp/mm}$).

Do ponto de vista da teoria de sistemas lineares e Invariantes no Espaço (LSI - *Linear Space-Invariant*), o sistema de formação de imagem da TC é modelado como um operador linear que mapeia a distribuição espacial do coeficiente de atenuação linear real $\mu(x, y, z)$ para a matriz de números de tomografia (unidades Hounsfield - HU). Como nenhum sistema é perfeito, o desfoque (*blurring*) óptico e geométrico degrada os detalhes finos. 

A MTF é definida rigorosamente como a razão entre a modulação do contraste da imagem e a modulação do contraste do objeto original, em função da frequência espacial $f$:

$$
\text{MTF}(f) = \frac{M_{\text{imagem}}(f)}{M_{\text{objeto}}(f)}
$$

Onde a modulação $M$ de uma febre sinusoidal de intensidade é calculada em termos de intensidades máximas ($I_{\max}$) e mínimas ($I_{\min}$) como:

$$
M = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}
$$

Por definição matemática, a MTF corresponde ao valor absoluto da **Função de Transferência Óptica (OTF)**, que por sua vez é a transformada de Fourier da **Função de Espalhamento de Ponto** (PSF - *Point Spread Function*):

$$
\text{OTF}(f_x, f_y) = \iint_{-\infty}^{\infty} \text{PSF}(x, y) e^{-j 2\pi (f_x x + f_y y)} \, dx \, dy
\text{MTF}(f_x, f_y) = \left| \text{OTF}(f_x, f_y) \right|
$$

Em TC, devido à simetria axial e à natureza da amostragem, a análise bidimensional da MTF em um plano transaxial ($x, y$) é frequentemente reduzida a perfis radiais e tangenciais, ou avaliada por meio da **Função de Espalhamento de Linha** (LSF - *Line Spread Function*) e da **Função de Espalhamento de Borda** (ESF - *Edge Spread Function*), onde a LSF é a derivada espacial da ESF, e a MTF é o módulo da transformada de Fourier unidimensional da LSF.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Para fins práticos em controle de qualidade e engenharia de sistemas, a relação entre as funções fundamentais de resolução espacial é expressa pelas seguintes identidades matemáticas:

Seja $\text{ESF}(x)$ a resposta do sistema a uma interface degrau ideal (borda abrupta). A LSF, denotada por $L(x)$, é obtida por diferenciação:

$$
L(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

A MTF é obtida aplicando-se a transformada de Fourier normalizada a $L(x)$:

$$
\text{MTF}(f) = \frac{\left| \int_{-\infty}^{\infty} L(x) e^{-j 2\pi f x} \, dx \right|}{\int_{-\infty}^{\infty} L(x) \, dx}
$$

### Propriedades Matemáticas Cruciais da MTF:
1. **Normalização na Origem:** Por definição de conservação de energia e ganho DC do sistema, a MTF na frequência zero é sempre unitária:
   
$$
\text{MTF}(0) = 1
$$

2. **Teorema da Convolução:** Se um sistema de TC é composto por múltiplos estágios lineares independentes (foco do tubo de raios-X, geometria de amostragem dos detectores, filtros de reconstrução/kernels), a MTF total do sistema é o produto das MTFs de cada componente individual:
   
$$
\text{MTF}_{\text{total}}(f) = \text{MTF}_{\text{foco}}(f) \cdot \text{MTF}_{\text{detector}}(f) \cdot \text{MTF}_{\text{reconstrução}}(f)
$$

3. **Adinensionalidade:** A frequência espacial $f$ é medida em $\text{mm}^{-1}$ ou $\text{lp/mm}$, tornando a MTF uma grandeza adimensional com valores estritamente no intervalo $[0, 1]$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na prática clínica e física de Tomografia Computadorizada, a MTF é a base para o projeto, comissionamento e controle de qualidade dos scanners. Suas principais aplicações e implicações incluem:

* **Seleção de Filtros de Reconstrução (*Kernels*):** Diferentes algoritmos de retroprojeção filtrada (FBP) utilizam filtros de rampa modificados. Filtros agudos (*sharp kernels*, ex. para osso) amplificam as altas frequências, elevando a MTF e preservando bordas nítidas, porém ao custo de amplificar drasticamente o ruído quântico. Filtros suaves (*smooth kernels*, ex. para cérebro ou fígado) atenuam as altas frequências, deprimindo a MTF mas reduzindo o ruído.
* **Frequência de Corte (*Cut-off Frequency*):** A frequência na qual a MTF cai para um limiar específico (geralmente $10\%$ ou $2\%$ do valor máximo, i.e., $\text{MTF}_{10}$) define a resolução espacial limite do sistema de TC para um dado protocolo.
* **Compromisso com o Ruído (Trade-off):** A otimização de dose em TC é inseparável da análise da MTF. O Teorema de Wiener relaciona o ruído da imagem ( através do Espectro de Potência de Ruído - NPS) com a MTF e a dose de radiação absorbida. 
* **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Sistemas modernos de reconstrução não linear quebram parcialmente a premissa de Invariância Espacial estrita. A MTF em algoritmos DLR pode ser dependente do contraste (variando para objetos de alto versus baixo contraste), exigindo métricas avançadas como a MTF de tarefa específica (*Task-based MTF*).
* **Observadores Computacionais:** Em tarefas de detecção de lesões (como nódulos pulmonares ou microcalcificações), a detectabilidade de um sinal por modelos de percepção visual humana ou ideal (*Channelized Hotelling Observer*) depende criticamente do balanço entre a MTF do sistema e o NPS.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia_Computadorizada]]
* [[Filtro_de_Retroprojetor_FBP]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa_IR]]
* [[Deep Learning Reconstruction (DLR)|Deep_Learning_Reconstruction_DLR]]
* [[Noise Power Spectrum|Espectro_de_Potencia_de_Ruido_NPS]]
* [[Funcao_de_Espalhamento_de_Ponto_PSF]]
* [[Controle de Qualidade em TC|Controle_de_Qualidade_em_TC]]
* [[Otimizacao_de_Dose_em_Radiologia]]