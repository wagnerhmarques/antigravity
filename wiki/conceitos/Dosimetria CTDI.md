---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, ctdi]
data: 2026-08-25
---

# Dosimetria_CTDI

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **CTDI** (*Computed Tomography Dose Index* ou Índice de Dose em Tomografia Computadorizada) é a métrica padrão-ouro da física médica e da metrologia das radiações para quantificar a dose de radiação ionizante absorvida associada a uma única rotação do tubo de raios X em um tomógrafo computadorizado. Diferente da radiografia convencional, onde a dose é expressa tipicamente em termos de produto dose-área ($DAP$) ou dose na pele em um ponto específico, a geometria helicoidal e axial da tomografia computadorizada (TC) gera um perfil de dose ao longo do eixo longitudinal ($z$) que se estende para fora da região primária do feixe devido à radiação espalhada ($scatter$) interna ao paciente ou fantoma.

Fisicamente, o CTDI é definido como a integral ao longo do eixo longitudinal do perfil de dose de uma única variação ($z$), normalizada pela espessura nominal do feixe tomográfico ($N \times T$), onde $N$ é o número de canais de detetores tomografados simultaneamente e $T$ é a largura de cada canal individual no isocentro do gantry. 

Metrologicamente, a mensuração do CTDI requer o uso de uma câmara de ionização de tipo lápis (*pencil ionization chamber*), caracterizada por um volume sensível longo (tipicamente $100\text{ mm}$ de comprimento), projetada especificamente para integrar o perfil de dose axial completo gerado por feixes estreitos de raios X de TC, mesmo quando a dispersão excede a largura nominal do feixe. Os testes e padronizações seguem rigorosamente protocolos internacionais de agências como a AAPM (American Association of Physicists in Medicine) — notadamente nos relatórios TG-111 e TG-200 — e a IEC (International Electrotechnical Commission).

---

## 2. Formulação Matemática e Propriedades

A formulação matemática fundamental do CTDI para uma variação axial única é dada pela integral do perfil de dose ao longo do eixo $z$:

$$
CTDI = \frac{1}{N \cdot T} \int_{-\infty}^{+\infty} D(z) \, dz
$$

Onde:
- $D(z)$ é a taxa de dose absorvida em função da posição longitudinal $z$.
- $N$ é o número de cortes tomografados por rotação.
- $T$ é a espessura nominal do corte no isocentro.

Na prática metrológica, como a integração infinita é impossível, utiliza-se a câmara de $100\text{ mm}$, definindo-se o **$CTDI_{100}$**:

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Para contabilizar os efeitos de retroespalhamento e atenuação da radiação no corpo humano ou em fantomas acrílicos cilíndricos padronizados (PMMA com diâmetros de $16\text{ cm}$ para crânio/pediátrico e $32\text{ cm}$ para abdômen/adulto), introduzem-se o **$CTDI_w$** (Weighted CTDI ou CTDI Ponderado) e o **$CTDI_{vol}$** (Volume CTDI).

O CTDI ponderado combina as medidas feitas na periferia ($12\text{ horas}$, $3\text{ horas}$, $6\text{ horas}$ e $9\text{ horas}$) e no centro do fantoma cilíndrico para estimar a dose média na seção transversal:

$$
CTDI_w = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Quando se transiciona de uma variação axial isolada para exames clínicos helicoidais contínuos, surge o **$CTDI_{vol}$**, que normaliza o $CTDI_w$ pelo passo da hélice (*pitch*, denotado por $I$ ou $p$):

$$
CTDI_{vol} = \frac{CTDI_w}{p}
$$

Onde o *pitch* $p$ é definido como:
- Para varreduras helicoidais: $p = \frac{\Delta d}{N \cdot T}$ ($\Delta d$ é o avanço da mesa por rotação).
- Para varreduras axiais sequenciais: $p = \frac{I}{N \cdot T}$ ($I$ é o incremento da mesa entre varreduras consecutivas).

Finalmente, para estimar a energia total depositada em um varrimento anatômico completo de comprimento $L$, calcula-se o **DLP** (*Dose-Length Product*):

$$
DLP = CTDI_{vol} \times L
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria baseada no CTDI é o pilar regulatório e de controle de qualidade na operação de sistemas de [[Reconstrucao_FBP_IR_DLR|Tomografia Computadorizada]]. Suas principais aplicações e frentes de otimização incluem:

*   **Controle de Qualidade (CQ) e Conformidade Regulatória:** Os valores de $CTDI_{100}$, $CTDI_w$ e $CTDI_{vol}$ são medidos periodicamente por físicos médicos para assegurar que a saída de radiação do tubo de raios X esteja dentro das tolerâncias dos fabricantes e das normas governamentais (como ANVISA no Brasil ou FDA nos EUA).
*   **Otimização de Protocolos Clínicos:** O $CTDI_{vol}$ e o $DLP$ exibidos na interface do console do tomógrafo antes de cada varredura permitem que os tecnólogos e radiologistas ajustem parâmetros como corrente do tubo ($mAs$), tensão ($kVp$), filtragem em arco e modulação angular de dose.
*   **Integração com Inteligência Artificial e DLR:** Algoritmos de *Deep Learning Reconstruction* (DLR) e reconstrução iterativa avançada permitem obter imagens diagnósticas de alta qualidade com níveis de ruído aceitáveis mesmo sob reduções drásticas de $CTDI_{vol}$. A metrologia do CTDI serve como base quantitativa para validar a eficácia desses algoritmos na redução do risco estocástico associado à radiação.
*   **Limitações Atuais:** Embora indispensável, o CTDI clássico mede a dose em fantomas cilíndricos padronizados e homogêneos, desconsiderando a morfologia real do paciente, o tamanho anatômico específico e a atenuação heterogênea de diferentes tecidos (necessitando de métricas complementares como o *Size-Specific Dose Estimate* - SSDE).

---

## 4. Conexões e Wikilinks

*   [[Fisica Medica|Fisica_Medica]]
*   [[Tomografia Computadorizada|Tomografia_Computadorizada]]
*   [[Reconstrucao_FBP_IR_DLR]]
*   [[Radioprotecao_e_Otimizacao]]
*   [[Qualidade de Imagem em TC|Qualidade_de_Imagem_em_TC]]