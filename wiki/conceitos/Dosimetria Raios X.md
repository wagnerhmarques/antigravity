---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# Dosimetria_Raios_X

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **dosimetria de raios-X** em Tomografia Computadorizada (TC) engloba o conjunto de princípios físicos, grandezas metrológicas, métodos experimentais e modelos computacionais utilizados para quantificar a energia depositada pela radiação ionizante nos tecidos biológicos. Diferentemente da radiografia planar, onde o campo de radiação é estático e bidimensional, a TC emprega fontes de raios-X colimadas em geometria helicoidal ou axial, com rotação gantry contínua e modulação de corrente tridimensional, o que torna o campo de radiação altamente complexo, heterogêneo e dinâmico.

Do ponto de vista metrológico, a caracterização da dose em TC exige a superação de desafios associados à natureza transiente da exposição e à geometria de feixe estreito na direção longitudinal ($z$), combinada com a dispersão interna difusa. As grandezas operacionais fundamentais baseiam-se em medições padronizadas realizadas com câmaras de ionização cilíndricas (tipo lápis — *pencil ionization chambers*) de $100\text{ mm}$ de comprimento ativo, inseridas em phantom de Polimetilmetacrilato (PMMA) normalizados para simulação da atenuação e espalhamento em cabeças e corpos humanos adultos e pediátricos.

A fundamentação física repousa sobre a transferência de energia fóton-elétron, descrita pelas interações de Efeito Fotoelétrico, Espalhamento Compton e Produção de Pares (esta última irrelevante nas energias típicas de feixes de TC, que operam entre $80\text{ kVp}$ e $140\text{ kVp}$). A grandeza microscópica fundamental é a **dose absorvida** ($D$), definida pela energia média impartida ($d\bar{\varepsilon}$) pela radiação ionizante a um elemento de massa ($dm$) em um ponto de um meio material:

$$
D = \frac{d\bar{\varepsilon}}{dm}
$$

Cuja unidade no Sistema Internacional (SI) é o Gray ($\text{Gy} = \text{J}\cdot\text{kg}^{-1}$). No entanto, devido à complexidade do perfil de dose ao longo do eixo longitudinal em varreduras helicoidais e sequenciais, grandezas macroscópicas derivadas — como o **Computed Tomography Dose Index (CTDI)** e a **Dose-Length Product (DLP)** — foram estabelecidas para fins de padronização regulatória, controle de qualidade e otimização clínica.

---

## 2. Formulação Matemática e Propriedades

Para quantificar a dose em TC, a formulação matemática evoluiu de métricas puntuais para integrais espaciais do perfil de dose axial.

### A. Índice de Dose de Tomografia Computadorizada (CTDI)
O perfil de dose $D(z)$ ao longo do eixo longitudinal $z$, gerado por uma única rotação do tubo de raios-X com largura de colimação nominal $T$, é integrado ao longo de um limite padrão de $\pm 50\text{ mm}$ (definido pelo comprimento ativo da câmara de ionização padrão de $100\text{ mm}$). A grandeza resultante é o **$\text{CTDI}_{100}$**:

$$
\text{CTDI}_{100} = \frac{1}{T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde $T = N \times t$ (sendo $N$ o número de canais de detetores ativos simultâneos e $t$ a espessura de cada canal no isocentro).

### B. CTDI Ponderado ($\text{CTDI}_{w}$)
Como a distribuição da dose no interior de um phantom cilíndrico de PMMA não é homogênea — apresentando valores mais elevados na periferia devido à atenuação superficial e menores no centro devido ao endurecimento do feixe e atenuação intrínseca —, o **$\text{CTDI}_{w}$** pondera as medições centrais e periféricas para refletir a dose média na seção transversal:

$$
\text{CTDI}_{w} = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Onde $\text{CTDI}_{100,\text{periferia}}$ é a média aritmética obtida em quatro posições angulares distintas a $1\text{ cm}$ da superfície interna do phantom ($0^\circ, 90^\circ, 180^\circ, 270^\circ$).

### C. CTDI Volume ($\text{CTDI}_{\text{vol}}$)
Em varreduras helicoidais, o espaçamento entre as rotações consecutivas é regulado pelo *Pitch* ($P$). O **$\text{CTDI}_{\text{vol}}$** representa a dose média na região escaneada, corrigida pelo avanço da mesa por rotação:

$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_{w}}{P}
$$

Onde o *Pitch* ($P$) é definido formalmente como:
- Para varreduras helicoidais: $P = \frac{\text{Avanço da mesa por rotação}}{\text{Colimação total do feixe } (T_{\text{total}})}$
- Para varreduras axiais (sequenciais): $P = \frac{\text{Avanço da mesa entre varreduras}}{\text{Colimação total do feixe } (T_{\text{total}})}$

### D. Produto Dose-Comprimento (DLP)
Para estimar a energia total impartida a um determinado volume anatômico durante um exame completo, introduz-se o **DLP** (*Dose-Length Product*), que integra o $\text{CTDI}_{\text{vol}}$ ao longo de todo o comprimento escaneado ($L$):

$$
\text{DLP} = \int_{0}^{L} \text{CTDI}_{\text{vol}}(z) \, dz = \text{CTDI}_{\text{vol}} \times L_{\text{total}}
$$

Expresso em $\text{mGy}\cdot\text{cm}$.

### E. Dose Efetiva ($E$)
A avaliação do risco estocástico radiogênico requer o cálculo da **Dose Efetiva** ($E$), expressa em Sieverts ($\text{Sv}$ ou $\text{mSv}$). Ela correlaciona a dose absorvida em diferentes tecidos/órgãos ponderada por seus respectivos coeficientes de sensibilidade radiológica ($w_T$), conforme recomendado pela Comissão Internacional de Proteção Radiológica (ICRP):

$$
E = \sum_{T} w_T \, H_T = \sum_{T} w_T \left( \sum_{R} w_R \, D_{T,R} \right)
$$

Onde $H_T$ é a dose equivalente no tecido $T$, $w_R$ é o fator de ponderação da radiação (para raios-X, $w_R = 1$), e $D_{T,R}$ é a dose absorvida média no órgão $T$ devida à radiação $R$. Em TC, a dose efetiva é frequentemente estimada multiplicando-se o DLP por coeficientes de conversão específicos de região anatômica ($k$, em $\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$):

$$
E \approx \text{DLP} \times k_{\text{região}}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria de raios-X em TC constitui o pilar central para o cumprimento dos princípios fundamentais da radioproteção: **Justificação**, **Limitação de Dose** e **Otimização** (*ALARA* - *As Low As Reasonably Achievable*). No ecossistema tecnológico contemporâneo da tomografia, a dosimetria interage diretamente com várias frentes de engenharia e física médica:

*   **Controle de Qualidade (CQ) e Conformidade Regulatória:** Os valores de $\text{CTDI}_{\text{vol}}$ e DLP exibidos no console do equipamento ("*Dose Display*") devem manter concordância estrita com os limites tolerados pelas agências reguladoras (como a CNEN no Brasil ou o FDA nos EUA), tipicamente exigindo desvios inferiores a $\pm 20\%$ em relação aos parâmetros nominais de fábrica.
*   **Sistemas de Reconstrução e Impacto Algorítmico:** O avanço tecnológico na reconstrução de imagens — migrando da Retroprojeção Filtrada (FBP) tradicional para algoritmos de **Reconstrução Iterativa (IR)** e, mais recentemente, **Aprendizado Profundo (*Deep Learning Reconstruction - DLR*)** — alterou profundamente o paradigma dosimétrico. Os algoritmos DLR conseguem suprimir o ruído quântico e os artefatos de feixe duro em níveis de $\text{CTDI}_{\text{vol}}$ drasticamente reduzidos (baixa dose), mantendo a detectabilidade de lesões de alto e baixo contraste.
*   **Modulação Automática de Corrente (ATCM):** Os sistemas modernos ajustam dinamicamente a corrente do tubo ($mA$) em função do diâmetro e da atenuação do paciente ao longo dos eixos angular ($x-y$) e longitudinal ($z$). A verificação dosimétrica nesses cenários exige o uso de fantomas antropomórficos e simulações avançadas, uma vez que o $\text{CTDI}_{\text{vol}}$ convencional assume perfis de exposição uniformes.
*   **Dosimetria Computacional Baseada em Monte Carlo:** Para estimativas individualizadas e de alta precisão (especialmente em exames pediátricos e protocolos de intervenção guiada por TC), códigos de transporte de radiação por Monte Carlo (como MCNP, GATE ou PENELOPE) modelam explicitamente a anatomia do paciente derivada de conjuntos de dados DICOM, calculando mapas tridimensionais de dose organ-specíficos com base na trajetória estocástica de milhões de fótons simulados.
*   **Observadores Computacionais e Avaliação de Tarefas:** Modelos de observadores humanos e ideais (como o *Channelized Hotelling Observer* - CHO) são acoplados a métricas dosimétricas para avaliar a eficiência diagnóstica em termos de relação dose-resposta (*Task-based Image Quality*), ponderando a otimização não apenas pela redução da dose, mas pela preservação da acurácia diagnóstica (ex: detectabilidade de nódulos pulmonares ou acidentes vasculares cerebrais precoces).

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia_Computadorizada]]
*   [[Fisica_Radi diagnostico]]
*   [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
*   [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]]
*   [[Qualidade Imagem TC|Qualidade_Imagem_TC]]
*   [[Radioprotecao_Medica]]
*   [[Monte_Carlo_Simulacao]]