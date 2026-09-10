---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, metrologia, processamento-de-sinal]
data: 2026-08-25
---

# Funcao_Transferencia_Modulacao_MTF

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Função de Transferência de Modulação (MTF - *Modulation Transfer Function*)** é a métrica padrão-ouro na Física Médica e na Engenharia de Imagem para quantificar a **resolução espacial** e a fidelidade de transferência de detalhes de um sistema de imagem. Em Tomografia Computadorizada (TC), a MTF descreve a capacidade do sistema — desde a geometria focal do tubo de raios X, passando pela amostragem dos detectores, até os filtros de retroprojeção e algoritmos de reconstrução — de reproduzir objetos de diferentes frequências espaciais.

Do ponto de vista físico, qualquer cena anatômica complexa pode ser decomposta em uma superposição de senoides espaciais de diferentes frequências, amplitudes e fases, graças à Transformada de Fourier. Quando um sistema de TC imageia essas senoides, a amplitude do sinal de saída é inevitavelmente menor do que a amplitude do sinal de entrada devido a limitações físicas (ex: tamanho finito do ponto focal gerando borramento penumbral, integração espacial finita nos elementos do detector, ruído eletrônico e amostragem digital). 

A MTF é definida formalmente como a razão entre a **modulação de saída** ($\text{MOD}_{\text{saída}}$) e a **modulação de entrada** ($\text{MOD}_{\text{entrada}}$) em função da frequência espacial ($u$), normalizada para o valor unitário na frequência zero ($u = 0$):

$$
\text{MTF}(u) = \frac{\text{MOD}_{\text{saída}}(u)}{\text{MOD}_{\text{entrada}}(u)} \times \left( \frac{\text{MOD}_{\text{entrada}}(0)}{\text{MOD}_{\text{saída}}(0)} \right)
$$

Onde a modulação (ou contraste Michelson) de um sinal periódico é dada por:

$$
\text{MOD} = \frac{I_{\text{máx}} - I_{\text{mín}}}{I_{\text{máx}} + I_{\text{mín}}}
$$

Uma $\text{MTF}(u) = 1$ indica reprodução perfeita do contraste (sem perda de detalhes), enquanto $\text{MTF}(u) = 0$ indica perda total de informação naquela frequência espacial específica (frequentemente além da frequência de Nyquist do sistema). O limite prático da resolução espacial em protocolos clínicos é frequentemente reportado na frequência onde a MTF cai para 10% ($u_{10}$) ou 50% ($u_{50}$) do seu valor máximo.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Matematicamente, a MTF é o módulo da **Función de Transferência Óptica (OTF - *Optical Transfer Function*)**, que por sua vez é a Transformada de Fourier bidimensional da **Função de Dispersão de Ponto (PSF - *Point Spread Function*)** normalizada:

$$
\text{OTF}(u, v) = \frac{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, e^{-i 2\pi (ux + vy)} \, dx \, dy}{\iint_{-\infty}^{\infty} \text{PSF}(x, y) \, dx \, dy}
\text{MTF}(u, v) = \left| \text{OTF}(u, v) \right|
$$

Onde:
- $\text{PSF}(x, y)$ é a resposta do sistema de TC a uma fonte pontual ideal (delta de Dirac).
- $u$ e $v$ são as frequências espaciais nas direções $x$ e $y$ (tipicamente expressas em $\text{lp/cm}$ - pares de linhas por centímetro, ou $\text{mm}^{-1}$).

Devido à simetria quase-circular dos sistemas de TC no plano axial, a MTF é frequentemente tratada de forma radial:

$$
\text{MTF}(f_r) = \mathcal{H} \left\{ \text{LSF}(x) \right\}
$$

Onde $\text{LSF}(x)$ é a **Função de Espalhamento de Linha (*Line Spread Function*)**, obtida analiticamente derivando a **Função de Espalhamento de Borda (*Edge Spread Function - ESF*)**:

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

### Propriedades Matemáticas Fundamentais da MTF:
1. **Normalização:** $\text{MTF}(0) = 1$.
2. **Linearidade e Superposição:** Válida apenas para sistemas lineares e shift-invariantes (aproximação aplicável localmente na TC).
3. **Teorema da Convolução:** Se um sistema é composto por múltiplos estágios em cascata (ex: foco do tubo, geometria do detector, filtro de reconstrução), a MTF total do sistema é o produto das MTFs individuais de cada componente:
   
   
$$
\text{MTF}_{\text{total}}(u) = \prod_{i=1}^{n} \text{MTF}_i(u)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Em Tomografia Computadorizada moderna, a MTF desempenha um papel central no Controle de Qualidade (CQ), no projeto de algoritmos de reconstrução e na otimização da dose de radiação.

### 1. Controle de Qualidade e Metrologia
Phantoms de CQ contêm inserções de alta densidade (fios de Tungstênio ou Platina para medir a PSF/LSF, ou bordas afiadas de teflon/acrílico para a ESF) para calcular empiricamente a MTF. As curvas de MTF permitem aos físicos médicos monitorar a degradação do tubo de raios X (aumento do ponto focal por desgaste térmico) e a integridade dos módulos de detecção.

### 2. Filtros de Reconstrução (Kernels) e Balanço Ruído-Resolução
Na [[Reconstrucao_Retroprojecao_Filtrada_FBP]], o filtro rampa (*ramp filter*) acentua as altas frequências espaciais para restaurar a nitidez, mas amplifica drasticamente o ruído quântico. Os fabricantes aplicam filtros apodizados (como *Hann*, *Hamming* ou *Butterworth*) que modificam a MTF do sistema:
- **Kernels de Alta Resolução (Sharp/Bone):** Mantêm a MTF elevada em frequências maiores, permitindo visualizar micro-estruturas (fraturas ósseas, ouvido interno), ao custo de alto ruído.
- **Kernels de Baixa Resolução (Smooth/Soft):** Atenuam rapidamente a MTF em frequências médias-altas, suprimindo o ruído, ideais para avaliação de partes moles e contraste de baixa atenuação.

### 3. Interação com Reconstrução Iterativa (IR) e Deep Learning (DLR)
Algoritmos de [[Reconstrução Iterativa|Reconstrucao_Iterativa]] e [[Reconstrucao_Baseada_em_IA_DLR]] introduzem não-linearidades espaciais. Em sistemas FBP tradicionais, a MTF é invariante ao nível de dose. No entanto, em DLR e IR avançadas, a MTF pode variar dependendo do nível de sinal (ruído dependente da dose). Isso gerou a necessidade de métricas estendidas, como a **Task-based MTF** (MTF baseada em tarefas) e a **NPSS** (*Noise Power Spectrum*), avaliadas através de abordagens de [[Teoria_Deteccao_Sinal_Observers]], integrando a resposta visual humana ou de observadores ideais (Hotelling/CHO) na avaliação de desempenho diagnóstico.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia_Computadorizada]]
- [[Reconstrucao_Retroprojecao_Filtrada_FBP]]
- [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
- [[Reconstrucao_Baseada_em_IA_DLR]]
- [[Noise Power Spectrum|Espectro_Potencia_Ruido_NPS]]
- [[Teoria_Deteccao_Sinal_Observers]]
- [[Qualidade_Imagem_Control_Qualidade]]