> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Unidades Hounsfield]], [[Efeito Fotoelétrico]], [[Espalhamento Compton]], [[Endurecimento do Feixe]], [[Atenuação Linear]], [[Tomografia Computadorizada Espectral]]

## 1. Fundamentação Física da Dependência Energética do Número CT

A escala de [[Unidades Hounsfield]] (HU) é ancorada matematicamente em dois pontos fixos de referência: a água pura ($0\text{ HU}$) e o ar ($-1000\text{ HU}$). No entanto, o valor atribuído a qualquer outro material ou tecido biológico depende criticamente do espectro de energia dos fótons de raios X incidentes, o qual é diretamente determinado pela tensão de tubo aplicada ($kVp$, *kilovoltage peak*).

A atenuação de um feixe de raios X policromático ao atravessar a matéria é governada pela lei de atenuação de Lambert-Beer modificada pela distribuição espectral do feixe $I(E)$:

$$
I = \int_{0}^{E_{\max}} I_0(E) \cdot \exp\left( -\int \mu(x, y, E) \, dl \right) dE
$$

Onde o coeficiente de atenuação linear efetivo $\mu(E)$ de um elemento químico ou tecido composto depende fortemente da combinação de dois fenômenos físicos dominantes nas faixas de energia diagnóstica ($30 - 140\text{ keV}$):

1. **Efeito Fotoelétrico:** Cuja probabilidade de ocorrência varia com o número atômico efetivo ($Z_{\text{eff}}$) e a energia do fóton ($E$) segundo a relação aproximada:

$$
\tau \propto \frac{Z_{\text{eff}}^3}{E^3}
$$

2. **Espalhamento Compton:** Cuja seção de choque é proporcional à densidade eletrônica volumétrica e fracamente dependente da energia do fóton:

$$
\sigma_{\text{C}} \propto \rho_e = N_A \left(\frac{Z}{A}\right)
$$

Como o espectro policromático de um tubo operando a $80\text{ kVp}$ possui uma energia média significativamente menor que o de um feixe operando a $140\text{ kVp}$, os materiais com elevado número atômico (como ossos corticais, meios de contraste iodados e agentes de gadolínio ou bário) sofrem um aumento expressivo no coeficiente de atenuação linear $\mu$ devido à dominância do efeito fotoelétrico em baixas energias. Consequentemente, o valor em Unidades Hounsfield desses materiais exibe uma forte dependência inversa em relação à tensão de tubo.

---

## 2. Comportamento Quantitativo em Tecidos e Materiais de Contraste

A tabela abaixo ilustra o comportamento típico da variação dos valores de HU em função da alteração da tensão de tubo para diferentes materiais biológicos e sintéticos:

| Material / Tecido | $80\text{ kVp}$ | $100\text{ kVp}$ | $120\text{ kVp}$ | $140\text{ kVp}$ | Mecanismo Físico Dominante |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Água Destilada** | $0\text{ HU}$ | $0\text{ HU}$ | $0\text{ HU}$ | $0\text{ HU}$ | Ponto de ancoragem da escala |
| **Gordura (Tecido Adiposo)** | $-90 \text{ a } -100\text{ HU}$ | $-95 \text{ a } -100\text{ HU}$ | $-100\text{ HU}$ | $-100\text{ HU}$ | Baixo $Z_{\text{eff}}$, espalhamento Compton predominante |
| **Músculo Esquelético** | $\approx 55\text{ HU}$ | $\approx 50\text{ HU}$ | $\approx 45\text{ HU}$ | $\approx 42\text{ HU}$ | Equilíbrio entre Compton e fotoelétrico |
| **Osso Trabecular / Cortical** | $300 - 1200\text{ HU}$ | $250 - 1000\text{ HU}$ | $200 - 850\text{ HU}$ | $180 - 750\text{ HU}$ | Elevado $Z_{\text{eff}}$ (Cálcio), forte dependência do efeito fotoelétrico |
| **Contraste Iodado ($10\text{ mg I/mL}$)** | $\approx 420\text{ HU}$ | $\approx 310\text{ HU}$ | $\approx 240\text{ HU}$ | $\approx 180\text{ HU}$ | Altíssimo $Z_{\text{eff}}$ (Iodo, K-edge em $33.2\text{ keV}$), sensibilidade extrema a baixos $kVp$ |

---

## 3. Implicações Clínicas e Metrológicas

A variação das Unidades Hounsfield com a tensão do tubo acarreta consequências diretas na prática diagnóstica e na metrologia em [[Tomografia Computadorizada]]:

* **Dosimetria e Planejamento Radioterápico:** Algoritmos de cálculo de dose baseados em superposição/convolução dependem de tabelas de conversão empírica que relacionam HU com densidade eletrônica e número atômico. Se um exame de planejamento for adquirido a uma tensão diferente da calibrada pelo sistema, ocorrerão erros sistemáticos na estimativa da atenuação de tecidos heterogêneos (como o tecido ósseo e o parênquima pulmonar).
* **Angiografia e Otimização de Meio de Contraste:** Em protocolos de baixa tensão (ex.: $70\text{ - }80\text{ kVp}$), a atenuação do iodo aumenta substancialmente devido à proximidade com a borda de absorção K (*K-edge* do iodo em $33.2\text{ keV}$). Isso permite reduzir o volume total de meio de contraste injetado sem perda de conspicuidade vascular, sendo a base física das técnicas modernas de imagem espectral e de [[Photon Counting Detector CT (PCD-CT)]].
* **Artefatos de Endurecimento do Feixe (*Beam Hardening*):** Como o feixe policromático é filtrado preferencialmente pelos fótons de baixa energia ao atravessar estruturas densas (como o osso temporal ou ombros), a energia média do feixe aumenta ao longo do trajeto. Isso gera distorções quantitativas nos valores de HU, resultando em bandas de sombreamento escuro (*cupping artifact* ou *dark bands*).
