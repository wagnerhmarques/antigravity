---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, protecao-radiologica, metrologia]
data: 2026-08-25
---

# Radiation Dosimetry

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Dosimetria da Radiação** (_Radiation Dosimetry_) é o ramo da física médica e da metrologia das radiações que estuda, quantifica e correlaciona a energia depositada por radiações ionizantes em meios materiais, com ênfase particular nos tecidos biológicos. No contexto da radiologia diagnóstica e, de forma preeminente, na **[[Tomografia Computadorizada (TC)|Computed Tomography (CT)]]**, a dosimetria serve como a base fundamental para a otimização de protocolos, o balanceamento entre a qualidade de imagem e o risco estocástico, e o cumprimento de marcos regulatórios internacionais.

Do ponto de vista metrológico, a dosimetria ionizante fundamenta-se na medição rigorosa de grandezas físicas estabelecidas por comissões internacionais, tais como a _International Commission on Radiation Units and Measurements_ (ICRU) e a _International Commission on Radiological Protection_ (ICRP). O processo envolve a transição desde grandezas físicas diretamente mensuráveis no ar (como a exposição e o kerma no ar) até grandezas de proteção radiológica e estocásticas (como o equivalente de dose e a dose efetiva), que não podem ser medidas diretamente in vivo, mas são estimadas através de modelagem matemática, simulações de Monte Carlo e fatores de conversão padronizados.

## 2. Formulação Matemática e Propriedades

A quantificação da energia transferida e absorvida fundamenta-se em uma hierarquia de grandezas físicas rigorosamente definidas:

### Kerma no Ar ($K$)
O Kerma (_Kinetic Energy Released in MAtter_) representa a energia cinética inicial total transferida pelas partículas ionizantes indiretamente ionizantes (fótons X e gama) para partículas carregadas (elétrons) por unidade de massa em um ponto de interesse.

$$
K = \frac{dE_{tr}}{dm}
$$

Onde $dE_{tr}}$ é a energia cinética média transferida aos elétrons em uma massa elementar $dm$. A unidade no SI é o Joule por quilograma ($\text{J}\cdot\text{kg}^{-1}$), denominada Gray ($\text{Gy}$).

### Dose Absorvida ($D$)
A dose absorvida é a energia média repassada pela radiação ionizante à matéria por unidade de massa em um volume elementar.

$$
D = \frac{d\bar{E}}{dm}
$$

Onde $\bar{E}$ é a energia média radiante impartida à matéria de massa $dm$. 

### Grandezas Específicas em Tomografia Computadorizada
Devido à geometria helicoidal e axial dos feixes de raios X em [[Tomografia Computadorizada (TC)|Computed Tomography (CT)]], grandezas planares convencionais são inadequadas. Utiliza-se primariamente o **Kerma no ar integrado no eixo Z**, que dá origem ao Índice de Dose em Tomografia Computadorizada (_Computed Tomography Dose Index_, **[[Métricas de Dose em TC|CTDI]]**):

$$
CTDI_{100} = \frac{1}{nT} \int_{-50\text{ cm}}^{+50\text{ cm}} D(z) \, dz
$$

Onde $n$ é o número de tomografias por rotação, $T$ é a espessura nominal do tomograma no isocentro, e $D(z)$ é o perfil de dose absorvida ao longo do eixo longitudinal $z$.

Para ponderar a variação espacial da dose entre a periferia e o centro dos fantomas cilíndricos padronizados de Polimetilmetacrilato (PMMA) de 16 cm (cabeça) e 32 cm (corpo), define-se o **CTDI ponderado** ($CTDI_{w}$):

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Para sistemas helicoidais, o avanço da mesa por rotação ($I$) introduz o conceito de **CTDI volume** ($CTDI_{vol}$), que incorpora o passo helicoidal (_pitch_, $p$):

$$
CTDI_{vol} = \frac{CTDI_{w}}{p}
$$

Onde $p = \frac{I}{nT}$.

Para estimar a energia total absorvida ao longo de todo o volume escaneado, utiliza-se o **Produto Dose-Comprimento** (_Dose-Length Product_, **[[Métricas de Dose em TC|DLP]]**):

$$
DLP = CTDI_{vol} \times L
$$

Onde $L$ é o comprimento total da varredura anatômica (em $\text{cm}$).

Por fim, a **Dose Efetiva** ($E$), expressa em Sieverts ($\text{Sv}$), traduz o risco estocástico global considerando a radiossecundariedade específica de cada órgão ou tecido irradia:

$$
E = \sum_{T} w_T \, H_T = \sum_{T} w_T \left( \sum_{R} w_R \, D_{T,R} \right)
$$

Onde $w_T$ é o fator de ponderação tecidual, $H_T$ é a dose equivalente no tecido $T$, $w_R$ é o fator de ponderação da radiação (igual a $1$ para raios X) e $D_{T,R}$ é a dose absorvida média no órgão $T$ devida à radiação $R$. Na prática clínica de TC, $E$ é frequentemente estimado multiplicando-se o $DLP$ por um coeficiente de conversão específico da região anatômica ($k$, em $\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria em [[Tomografia Computadorizada (TC)|Computed Tomography (CT)]] constitui o pilar central para o cumprimento do princípio **ALARA** (_As Low As Reasonably Achievable_). Suas aplicações práticas desdobram-se em várias frentes tecnológicas e clínicas:

1. **Controle de Qualidade e Garantia de Qualidade (QA):**
   Físicos médicos utilizam câmaras de ionização cilíndricas do tipo lápis (_pencil ionization chambers_) acopladas a eletrômetros e fantomas de acrílico padronizados para verificar periodicamente se a saída dos tubos de raios X e a modulação automática de corrente de tubo ([[Automatic Tube Current Modulation - ATCM]]) operam conforme as especificações do fabricante e as tolerâncias normativas.

2. **Reconstrução de Imagem e Algoritmos Avançados:**
   A integração entre algoritmos modernos de reconstrução — como a **[[FBP|Filtered Back Projection (FBP)]]**, **[[Reconstrução Iterativa|Iterative Reconstruction (IR)]]** e **[[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction (DLR)]]** — depende intrinsecamente da dosimetria. Métodos baseados em inteligência artificial e reconstrução iterativa permitem a redução drástica do $CTDI_{vol}$ sem perda de detectabilidade de baixo contraste, mitigando o ruído quântico inerente a varreduras de baixa dose.

3. **Monitoramento e Gestão de Dose do Paciente:**
   Sistemas modernos de TC registram o $CTDI_{vol}$ e o $DLP$ diretamente nos metadados DICOM ([[DICOM Structured Reporting - SR]]). Softwares de gerenciamento de dose agregam esses dados para estabelecer Níveis de Referência Diagnóstica ([[Diagnostic Reference Levels - DRL]]), permitindo auditorias institucionais e a mitigação de riscos decorrentes de exames repetidos ou protocolos excessivamente agressivos.

4. **Simulações Computacionais e Dosimetria Baseada em Monte Carlo:**
   A avaliação de doses específicas em órgãos sensíveis (como cristalino, tireoide e mama) frequentemente utiliza simulações de transporte de radiação por [[Monte Carlo Simulations]] acopladas a modelos antropomórficos computacionais baseados em voxels ou malhas poligonais (_mesh-based computational phantoms_).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada (TC)|Computed Tomography (CT)]]
* [[Métricas de Dose em TC|CTDI]]
* [[Métricas de Dose em TC|DLP]]
* [[Automatic Tube Current Modulation - ATCM]]
* [[FBP|Filtered Back Projection (FBP)]]
* [[Reconstrução Iterativa|Iterative Reconstruction (IR)]]
* [[Deep Learning Reconstruction (DLR)|Deep Learning Reconstruction (DLR)]]
* [[DICOM Structured Reporting - SR]]
* [[Diagnostic Reference Levels - DRL]]
* [[Monte Carlo Simulations]]