---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# camara-de-ionizacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **câmara de ionização** é o detector padrão primário e secundário para a medição absoluta de radiação ionizante (especificamente fótons de alta energia, como raios X e gama, bem como partículas carregadas) em física médica e metrologia das radiações. Seu princípio de funcionamento baseia-se na coleta de pares de íons (elétrons e íons positivos) gerados pela interação da radiação com um meio gasoso contido em um volume sensível delimitado por eletrodos.

Do ponto de vista físico, quando a radiação ionizante atravessa o gás de trabalho da câmara (geralmente ar seco nas condições normais de temperatura e pressão, ou gases nobres sob condições controladas), ocorre a transferência de energia que resulta na ionização das moléculas do gás. Aplicando-se uma diferença de potencial elétrico estática adequada entre o eletrodo coletor e a carcaça/parede externa da câmara, estabelece-se um campo elétrico no interior do volume sensível. Este campo provoca a migração dos íons positivos em direção ao catodo e dos elétrons livres (ou íons negativos) em direção ao anodo, gerando uma corrente elétrica mensurável (corrente de ionização) por meio de um eletrômetro de alta sensibilidade.

Operando estritamente na **região de ionização** da curva de características de uma câmara (onde o potencial aplicado é suficiente para evitar a recombinação iônica generalizada e inicial, mas insuficiente para causar ionização secundária por colisões ou efeitos multiplicativos do tipo Townsend), a carga total coletada é estritamente proporcional à energia total depositada pela radiação no volume gasoso. 

Na prática clínica e de controle de qualidade, as câmaras de ionização destacam-se pela excelente estabilidade temporal, alta reprodutibilidade, resposta linear em ampla faixa de taxas de dose e dependência energética previsível, sendo o instrumento mandatório para a calibração de feixes em equipamentos de [[Tomografia Computadorizada|tomografia-computadorizada]] e radioterapia.

---

## 2. Formulação Matemática e Propriedades

A grandeza fundamental medida por uma câmara de ionização em termos de exposição ou kerma no ar é a carga elétrica total $Q$ induzida no eletrodo coletor. A dose absorvida no meio ou o kerma no ar ($K$) correlacionam-se com a carga corrigida através de protocolos de dosimetria baseados na cavidade de Bragg-Gray e teorias correlatas.

A carga medida $M$ (em Coulombs ou unidades eletrostáticas) obtida pelo eletrômetro deve ser submetida a fatores de correção metrológicos rigorosos para determinar a carga real $Q$ sob condições padrão de referência:

$$
Q = M \cdot P_{\text{TP}} \cdot P_{\text{ion}} \cdot P_{\text{pol}} \cdot P_{\text{elec}}
$$

Onde os fatores de correção denotam:
* $P_{\text{TP}}$: Fator de correção para temperatura e pressão atmosférica (Lei dos Gases Ideais).
* $P_{\text{ion}}$: Fator de correção para a recombinação de íons (perda de carga por recombinação inicial e geral).
* $P_{\text{pol}}$: Fator de correção para a polaridade (assimetrias na coleta ao inverter o sinal do potencial aplicado).
* $P_{\text{elec}}$: Fator de calibração do eletrômetro (quando aplicável separadamente).

O fator de correção de temperatura e pressão é expresso por:

$$
P_{\text{TP}} = \left( \frac{273.15 + T}{273.15 + T_0} \right) \left( \frac{P_0}{P} \right)
$$

Onde $T$ e $P$ são a temperatura e a pressão no momento da medição, e $T_0$ ($22^\circ\text{C}$ ou $20^\circ\text{C}$) e $P_0$ ($101.3\,\text{kPa}$ ou $101.33\,\text{kPa}$) correspondem aos valores de referência padrão do laboratório de calibração.

Para feixes de raios X aplicados em Tomografia Computadorizada, utiliza-se frequentemente a câmara do tipo *pencil chamber* (câmara tipo lápis) para medir a grandeza CTDI (*Computed Tomography Dose Index*), integrando o perfil de dose ao longo do eixo $z$:

$$
\text{CTDI}_{100} = \frac{1}{N \cdot T} \int_{-50\,\text{cm}}^{+50\,\text{cm}} D(z) \, dz
$$

Onde $N$ é o número de cortes tomográficos adquiridos por rotação, $T$ é a espessura nominal do corte e $D(z)$ é o perfil de dose absorvida ao longo do eixo longitudinal $z$, medido analiticamente com o auxílio da câmara de ionização integrada.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema da Tomografia Computadorizada (TC), as câmaras de ionização desempenham papel vital na garantia da qualidade física, na otimização dos protocolos de aquisição e na conformidade com os limites regulatórios de dose ao paciente. 

### Controle de Qualidade e Dosimetria de Rotina
As câmaras do tipo caneta (*pencil chambers*, tipicamente com 100 mm de comprimento ativo) são inseridas em cavidades específicas de fantasmas (*phantoms*) acrílicos padronizados que simulam a cabeça e o corpo humano. Elas permitem quantificar índices essenciais como:
* $\text{CTDI}_{\text{w}}$ (CTDI ponderado), que pondera as doses periféricas e centrais.
* $\text{CTDI}_{\text{vol}}$ (CTDI volumétrico), que contabiliza o impacto do passo da hélice (*pitch*).
* DLP (*Dose-Length Product*), métrica integradora do risco estocástico associado ao exame.

### Otimização e Algoritmos de Reconstrução
Embora a câmara de ionização não participe diretamente do processo computacional de reconstrução de imagem (como [[Retroprojeção Filtrada (FBP)|FBP]], [[Reconstrução Iterativa|reconstrucao-iterativa]] ou [[reconstrucao-profunda-dlr]]), a acurácia dos dados dosimétricos coletados por elas fundamenta os modelos matemáticos de simulação de radiação baseados em Monte Carlo utilizados por softwares avançados de modulação de dose (por exemplo, *Organ Dose Estimation*). As medições precisas com câmaras de ionização validam os perfis de feixe (*beam shaping filters* e atenuação da calha do arco do tubo de raios X), permitindo que algoritmos de reconstrução ajustem as penalidades de ruído sem comprometer a integridade diagnóstica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[dosimetria-das-radiacoes]]
* [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
* [[ctdi-e-metricas-de-dose]]
* [[Efeitos Biologicos da Radiação|efeitos-biologicos-da-radiacao]]
* [[Retroprojeção Filtrada (FBP)|fbp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[reconstrucao-profunda-dlr]]