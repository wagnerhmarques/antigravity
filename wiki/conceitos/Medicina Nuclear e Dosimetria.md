---
tipo: conceito
tags: [fisica-medica, medicina-nuclear, dosimetria, radioterapia-interna, imageamento-hibrido, tomografia-computadorizada, pet-ct, spect-ct]
data: 2026-08-25
---

# Medicina Nuclear e Dosimetria

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Medicina Nuclear (MN) é uma especialidade médica e tecnológica que emprega fontes radioativas seladas e não seladas (radiofármacos) para fins diagnósticos (in vivo e in vitro) e terapêuticos. Do ponto de vista da Física Médica, o princípio fundamental fundamenta-se na administração de radionuclídeos conjugados a moléculas carreadoras biologicamente ativas, permitindo o mapeamento funcional, metabólico e molecular de processos fisiopatológicos em nível celular e subcelular. 

Enquanto modalidades anatômicas como a radiografia convencional e a Tomografia Computadorizada (TC) dependem de contrastes baseados na atenuação de fótons de raios X externos, a Medicina Nuclear baseia-se na emissão interna de radiação ionizante decorrente do decaimento radioativo. Os emissores gama puros ou pósitrons ($\beta^+$) são utilizados primariamente para imageamento por cintilografia planar, Tomografia por Emissão de Fóton Único ([[Tomografia por Emissão de Pósitrons (PET)|SPECT]]) e Tomografia por Emissão de Pósitrons ([[Tomografia por Emissão de Pósitrons (PET)|PET]]). Em contrapartida, radionuclídeos emissores de partículas corpusculares de alta transferência linear de energia (LET), como partículas beta negativas ($\beta^-$), alfa ($\alpha$) e elétrons de Auger, são aplicados na Teranóstica e na radioterapia molecular interna.

A **Dosimetria em Medicina Nuclear** representa o ramo da metrologia das radiações dedicado à quantificação da energia absorvida por unidade de massa (dose absorvida, com unidade no SI em Gray, Gy) em tecidos e órgãos-alvo decorrente da administração de radiofármacos. Diferente da radioterapia externa, onde os campos de radiação são estáticos e externalizados, a dosimetria interna apresenta complexidade estocástica e cinemética acentuada:
1. **Distribuição Espaço-Temporal Variável:** A concentração do radiofármaco é dinâmica, governada por processos farmacocinéticos (absorção, metabolização, excreção) e pelo decaimento físico do radionuclídeo.
2. **Exposição Multidirecional e Difusa:** A radiação ionizante origina-se de dentro do próprio organismo, exigindo modelos matemáticos que integrem a retenção temporal da atividade e os caminhos de trajetória das radiações corpusculares e eletromagnéticas.

Metrologicamente, a padronização e a rastreabilidade das medições de atividade em Medicina Nuclear dependem de calibradores de dose (câmaras de ionização do tipo poço) aferidos por padrões primários e secundários, vinculados a institutos nacionais de metrologia (como o BIPM e o NIST).

---

## 2. Formulação Matemática e Propriedades

O formalismo matemático clássico para o cálculo de dose absorvida em órgãos na Medicina Nuclear é o **Esquema MIRD** (*Medical Internal Radiation Dose*), desenvolvido pelo comitê homônimo da *Society of Nuclear Medicine and Molecular Imaging* (SNMMI).

A dose absorvida média ($D$) em um órgão-alvo ($r_T$) proveniente de um ou mais órgãos-fonte ($r_S$) contendo o radiofármaco é expressa pela equação fundamental do MIRD:

$$
\bar{D}(r_T \leftarrow r_S) = \tilde{A}(r_S) \cdot S(r_T \leftarrow r_S)
$$

Onde:
- $\tilde{A}(r_S)$ é o **número acumulado de desintegrações** (ou atividade integrada no tempo) no órgão-fonte $r_S$ durante o intervalo de integração (frequentemente de $t = 0$ até $t = \infty$):
  
$$
\tilde{A}(r_S) = \int_{0}^{\infty} A(r_S, t) \, dt
$$

  com $A(r_S, t)$ sendo a atividade do radiofármaco no órgão-fonte no tempo $t$.
- $S(r_T \leftarrow r_S)$ é o **Fator S** (ou fator de dose específica absorvida), que representa a dose absorvida média por unidade de atividade integrada no órgão-alvo por desintegração no órgão-fonte:
  
$$
S(r_T \leftarrow r_S) = \sum_i \Delta_i \frac{\Phi_i(r_T \leftarrow r_S)}{M(r_T)}
$$

Na expressão do Fator S:
- $\Delta_i$ é a energia média emitida por transposição nuclear para a $i$-ésima radiação (transição isomérica, partícula $\beta$, conversão interna, raio X, etc.), expressa em $\text{Gy}\cdot\text{kg}/(\text{Bq}\cdot\text{s})$ ou equivalentes.
- $\phi_i(r_T \leftarrow r_S)$ é a **fração de absorção** (fração da energia emitida no órgão-fonte $r_S$ que é absorvida pelo órgão-alvo $r_T$).
- $M(r_T)$ é a massa do órgão-alvo $r_T$.

### Modelagem Cinética e Farmacocinética
A atividade temporal $A(r_S, t)$ é tipicamente modelada por uma soma de exponenciais, descrevendo a captação e a depuração biológica combinada com o decaimento radioativo:

$$
A(t) = A_0 \sum_{j} a_j e^{-\lambda_{eff, j} t}
$$

Onde $\lambda_{eff, j}$ é a constante de decaimento efetiva, definida em função da constante de decaimento físico ($\lambda = \frac{\ln 2}{T_{1/2}}$) e da constante de depuração biológica ($\lambda_{b, j} = \frac{\ln 2}{T_{biol, j}}$):

$$
\lambda_{eff, j} = \lambda + \lambda_{b, j} = \frac{\ln 2}{T_{1/2}} + \frac{\ln 2}{T_{biol, j}}
$$

### Extensão para Dosimetria Voxel a Voxel (3D)
Com o advento de imagens quantitativas de alta resolução obtidas por SPECT/CT e PET/CT, o formalismo MIRD evoluiu para a **dosimetria baseada em voxels**, substituindo o conceito de órgãos macroscópicos por matrizes tridimensionais de elementos de volume ($v_x, v_y, v_z$). A dose em um voxel alvo $r_t$ devido à atividade em um voxel fonte $r_s$ é calculada por:

$$
\bar{D}(r_T) = \sum_{r_S} \tilde{A}(r_S) \cdot S(r_T \leftarrow r_S)
$$

Onde os fatores $S$ voxelizados são tipicamente pré-calculados por simulações de Monte Carlo baseadas em geometrias anatômicas derivadas de imagens de [[Tomografia Computadorizada|Tomografia Computadorizada]] (fantasmas antropomórficos computacionais ou imagens específicas do paciente).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A integração sinérgica entre a Medicina Nuclear e a Tomografia Computadorizada — corporificada nos sistemas híbridos **SPECT/CT** e **PET/CT** — revolucionou o imageamento molecular quantitativo. A TC exerce papéis fundamentais e insubstituíveis nestes sistemas:

### 1. Correção de Atenuação (Attenuation Correction - AC)
Os fótons emitidos no decaimento radioativo sofrem atenuação e espalhamento Compton ao atravessarem os tecidos corporais antes de atingirem os detectores da gama-câmara ou do PET. Sem a correção adequada, ocorrem subestimações severas na atividade profunda dos tecidos. 
- **Procedimento:** A imagem de TC (adquirida tipicamente em unidades Hounsfield - HU) é convertida em mapas de coeficientes de atenuação linear ($\mu$) para a energia específica do radionuclídeo (ex: 511 keV para PET com ${}^{18}\text{F}$).
- **Impacto na Dosimetria:** Mapas de atenuação precisos garantem a quantificação absoluta da atividade, pré-requisito indispensável para a acurácia do cálculo de dose absorvida via formalismo MIRD ou simulações de Monte Carlo.

### 2. Correção de Espalhamento e Resolução Espacial
Algoritmos avançados de reconstrução de imagem, como [[Retroprojeção Filtrada (FBP)|FBP]] (Retroprojeção Filtrada) modificada, [[Reconstrução Iterativa|IR]] (Reconstrução Iterativa) e algoritmos baseados em Aprendizagem Profunda ([[Deep Learning Reconstruction (DLR)|DLR]] - *Deep Learning Reconstruction*), incorporam matrizes de resposta do sistema (PSF - *Point Spread Function*) modeladas diretamente a partir de dados anatômicos de alta resolução da TC. Isso mitiga os artefatos de transbordamento de contagem (*partial volume effect*), otimizando a exatidão espacial para a dosimetria de pequenos tumores e metástases.

### 3. Otimização de Protocolos Híbridos e Dosimetria de Pacientes
Embora a TC nos sistemas híbridos seja primariamente voltada para a localização anatômica e correção de atenuação (frequentemente operando em baixas correntes de tubo, como modo *low-dose CT*), a dose cumulativa de radiação ionizante decorrente do exame híbrido total (radiofármaco + varredura de TC) deve ser rigorosamente otimizada. O físico médico atua no controle de qualidade e na otimização de parâmetros de aquisição da TC (kVp, mAs, filtros de reconstrução) para minimizar a dose radiológica desnecessária sem comprometer a acurácia diagnóstica e a segmentação de órgãos críticos para a radioterapia interna seletiva (SIRT ou PRRT).

---

## 4. Conexões e Wikilinks

- [[Tomografia por Emissão de Pósitrons (PET)|SPECT]]
- [[Tomografia por Emissão de Pósitrons (PET)|PET]]
- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Retroprojeção Filtrada (FBP)|FBP]]
- [[Reconstrução Iterativa|IR]]
- [[Deep Learning Reconstruction (DLR)|DLR]]