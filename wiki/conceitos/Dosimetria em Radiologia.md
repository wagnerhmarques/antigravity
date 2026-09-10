---
tipo: conceito
aliases: ["Dosimetria em Raio-X", "Dosimetria em Tomografia Computadorizada", "Dosimetria em Radiologia Diagnóstica", "Dosimetria da Radiação", "Dosimetria de Radiação", "Dosimetria e Segurança em Radiologia", "Dosimetria de Radiais", "Dosimetria em Medicina Nuclear", "Dosimetria e Otimizacao em TC", Dosimetria_e_Otimizacao_Dose_TC]
tags: [fisica-medica, tomografia-computadorizada]
data: 2026-08-25
---

# Dosimetria em Radiologia

## 1. Definição Conceitual e Fundamentação Física
A dosimetria em radiologia é o ramo da física médica dedicado à quantificação, cálculo e avaliação da energia depositada por radiações ionizantes nos tecidos biológicos e em meios materiais equivalentes durante procedimentos diagnósticos e intervencionistas, com ênfase particular na Tomografia Computadorizada (TC). Diferente da radioterapia, onde o objetivo é a entrega de doses altas e localizadas em volumes tumorais, a radiologia diagnóstica lida com campos de radiação heterogêneos, feixes polienergéticos de raios X e doses fracionadas que visam à otimização da relação entre o benefício clínico diagnóstico e o risco estocástico (principalmente indução de neoplasias) e determinístico. 

A fundamentação física baseia-se na interação da radiação eletromagnética (fótons de raios X) com a matéria através de processos como o Efeito Fotoelétrico, Espalhamento Compton e Produção de Pares. A energia transferida por esses fótons aos elétrons secundários e a subsequente energia absorvida por unidade de massa definem as grandezas dosimétricas fundamentais. Na prática de TC, a complexidade geométrica do feixe — caracterizada por uma colimação estrita no eixo longitudinal ($z$) e rotação contínua da fonte ao redor do paciente — exige o desenvolvimento de métricas padronizadas que permitam correlacionar a saída do equipamento com o risco populacional e individual estimado.

## 2. Formulação Matemática e Propriedades
As grandezas dosimétricas na Tomografia Computadorizada partem da medição do perfil de dose ao longo do eixo longitudinal utilizando câmaras de ionização tipo lápis (geralmente de $100\text{ mm}$ de comprimento) inseridas em fantomas cilíndricos padronizados de polimetilmetacrilato (PMMA) para cabeça ($16\text{ cm}$ de diâmetro) e corpo ($32\text{ cm}$ de diâmetro).

A grandeza básica de saída é a Dose Absorvida Integrada ao longo do eixo $z$, que leva à definição do **CTDI (Computed Tomography Dose Index)** normalizado pelo passo da hélice (*pitch*, $p$):

$$
\text{CTDI}_{100} = \frac{1}{nT} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde:
- $n$ é o número de cortes tomados por varredura axial.
- $T$ é a espessura nominal de cada corte (em mm).
- $D(z)$ é o perfil de dose ao longo do eixo $z$.

Para contemplar a variação espacial da dose entre a periferia e o centro do fantoma\, define-se o **CTDI ponderado ($\text{CTDI}_w$)**:

$$
\text{CTDI}_w = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Em sistemas helicoidais, o avanço da mesa por rotação ($I$) introduz o parâmetro de *pitch* ($p = \frac{I}{nT}$), resultando no **CTDI volume ($\text{CTDI}_{\text{vol}}$)**, que representa a dose média na região escaneada para um protocolo específico:

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_w}{p}
$$

Para avaliar a energia total depositada em todo o volume corpóreo inspecionado, utiliza-se o **Dose Length Product (DLP)**\, dado por:

$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

Onde $L$ é o comprimento total da varredura anatômica ($\text{cm}$).

Finalmente, a estimativa do risco radiológico global é obtida por meio da **Dose Efetiva ($E$)**, expressa em Sieverts ($\text{Sv}$), que pondera a dose absorvida em cada órgão ou tecido $T$ ($D_T$) pelos respectivos fatores de sensibilidade tecidual recomendados pela ICRP ($w_T$):

$$
E = \sum_T w_T \cdot D_T \approx \text{DLP} \times E_{\text{spec}}
$$

Onde $E_{\text{spec}}$ é o coeficiente de conversão específico para a região anatômica irradiada ($\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$).

## 3. Contexto no Acervo do Pesquisador & Aplicações
No escopo do acervo da LLM Wiki de Física Médica & Tomografia Computadorizada (USP/FAPESP), a **Dosimetria em Radiologia** atua como uma âncora fundamental para o princípio ALARA (*As Low As Reasonably Achievable*), contrapondo-se às exigências de otimização da [[Qualidade de Imagem em TC]]. 

Conforme documentado em [[Estudo de Observadores 2AFC|2-AFC]], a avaliação de desempenho de sistemas de imagem frequentemente utiliza a [[Fun o de Pot Ncia de Ru do NPS|Função de Potência de Ruído - NPS]] e a detectabilidade para mensurar artefatos e granulosidade. No entanto, ganhos em qualidade de imagem obtidos por métodos avançados — como a [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]] ou algoritmos baseados em [[U-Net|Redes U-Net]] e [[Controle de Qualidade em TC]] — devem ser rigorosamente validados dosimetricamente para garantir que a redução de ruído não seja acompanhada por um incremento indesejado na dose ao paciente ou, inversamente, para quantificar o fator de redução de dose possibilitado por tais tecnologias de inteligência artificial. Além disso, a calibração precisa das [[Unidades Hounsfield|Unidades Hounsfield]] depende de protocolos de aquisição cujos parâmetros influenciam diretamente a $\text{CTDI}_{\text{vol}}$ gerada.

## 4. Conexões e Wikilinks
- [[Qualidade de Imagem em TC]]
- [[Controle de Qualidade em TC]]
- [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
- [[Unidades Hounsfield|Unidades Hounsfield]]
- [[Fun o de Pot Ncia de Ru do NPS|Função de Potência de Ruído - NPS]]
- [[U-Net|Redes U-Net]]