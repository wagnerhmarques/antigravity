---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada\, dosimetria, radioprotecao, radiacao-ionizante]
data: 2026-08-25
---

# radiação ionizante

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **radiação ionizante** define-se como qualquer tipo de radiação composta por fótons de alta energia ou partículas subatômicas capazes de produzir íons — isto é\, de arrancar elétrons ligados de átomos ou moléculas — ao interagir com a matéria. Para que ocorra a ionização, a energia da radiação incidente deve ser superior à energia de ligação dos elétrons mais externos do átomo-alvo, tipicamente da ordem de dezenas de elétron-volts ($\text{eV}$). Na prática da física médica e radiológica, os limiares energéticos situam-se acima de aproximadamente $10\text{ eV}$ a $15\text{ eV}$, correspondendo a comprimentos de onda no espectro eletromagnético inferiores ao ultravioleta extremo, abrangendo os raios X e os raios $\gamma$, bem como partículas carregadas (elétrons/pósitrons, prótons, íons pesados) e não carregadas (nêutrons).

Do ponto de vista metrológico, a quantificação da radiação ionizante baseia-se em grandezas físicas rigorosamente definidas pelo *International Commission on Radiation Units and Measurements* (ICRU) e pelo *International System of Units* (SI):
* **Atividade ($A$):** Número de decaimentos nucleares por unidade de tempo, medida em Becquerels ($\text{Bq} = \text{s}^{-1}$).
* **Exposição ($X$):** Medida da ionização produzida por fótons no ar, expressa em Coulombs por quilograma ($\text{C/kg}$).
* **Dose Absorvida ($D$):** Energia média impartida pela radiação ionizante à matéria por unidade de massa, expressa em Grays ($\text{Gy} = \text{J/kg}$).
* **Dose Equivalente ($H$) e Dose Efetiva ($E$):** Grandezas de proteção radiológica que ponderam a dose absorvida pelo tipo de radiação (fator $w_R$) e pela sensibilidade dos diferentes tecidos biológicos expostos (fator $w_T$), ambas expressas em Sieverts ($\text{Sv}$).

## 2. Formulação Matemática e Propriedades (se aplicável)

A interação de fótons de raios X (gerados em sistemas de Tomografia Computadorizada) com a matéria obedece a leis estatísticas de atenuação exponencial. Quando um feixe monoenergético de intensidade inicial $I_0$ atravessa um meio material de espessura $x$ e coeficiente de atenuação linear $\mu$, a intensidade transmitida $I(x)$ é descrita pela Lei de Beer-Lambert:

$$
I(x) = I_0 e^{-\mu x}
$$

O coeficiente de atenuação linear $\mu$ depende da energia do fóton $E$\, da densidade mássica do meio $\rho$ e do número atômico efetivo $Z_{\text{eff}}$ do tecido ou material. Em energias típicas de diagnóstico por imagem ($\sim 30\text{ keV}$ a $120\text{ keV}$), os principais mecanismos de interação microscópica são o **Efeito Fotoelétrico** e o **Espalhamento Compton**. A seção atômica total de atenuação pode ser aproximada pela soma das contribuições dos principais processos:

$$
\mu_{\text{m}} = \frac{\mu}{\rho} \approx \tau_{\text{m}} + \sigma_{\text{m}} + \kappa_{\text{m}}
$$

Onde:
* $\tau_{\text{m}}$ representa a contribuição do efeito fotoelétrico (proporcional a $\approx Z^4 / E^3$).
* $\sigma_{\text{m}}$ representa o espalhamento Compton (incoerente), fracamente dependente de $Z$ e decrescente com $1/E$.
* $\kappa_{\text{m}}$ representa a produção de pares (relevante apenas em energias superiores a $1,022\text{ MeV}$, fora do escopo do diagnóstico por imagem convencional, mas presente em aplicações de alta energia e medicina nuclear baseada em PET).

A dose absorvida $D$ em um ponto infinitesimal de um meio com densidade $\rho$ e coeficiente de transferência de massa de energia $\left(\frac{\mu_{\text{tr}}}{\rho}\right)$, submetido a um campo de radiação caracterizado pelafluência de energia $\Psi$, é expressa por:

$$
D = \Psi \left( \frac{\mu_{\text{tr}}}{\rho} \right)
$$

Sob condições de equilíbrio eletrônico lateral e transacional, a taxa de dose relaciona-se diretamente com a distribuição espacial da energia depositada pelas partículas secundárias carregadas (elétrons Compton e fotoelétrons).

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada (TC), a radiação ionizante na faixa dos raios X é o meio fundamental de sondagem não invasiva da anatomia e patologia humanas. Um tubo de raios X rotativo emite fótons que atravessam o paciente em múltiplos ângulos de projeção, gerando conjuntos de dados brutos (*sinogramas*) que são subsequentemente convertidos em matrizes volumétricas tridimensionais.

A otimização do uso da radiação ionizante na TC é guiada pelo princípio **ALARA** (*As Low As Reasonably Achievable*). O gerenciamento da dose abrange pilares tecnológicos fundamentais:
* **Dosimetria Específica:** O uso de grandezas padronizadas como o **CTDI** (*Computed Tomography Dose Index*), em suas variações $\text{CTDI}_{\text{w}}$ e $\text{CTDI}_{\text{vol}}$, além do **Dose Length Product (DLP)** e da estimativa de Dose Efetiva baseada em modelos antropomórficos.
* **Modulação Automática de Corrente (mA):** Ajuste dinâmico da intensidade do feixe de raios X em função da atenuação e espessura do paciente ao longo dos eixos angular ($x-y$) e longitudinal ($z$).
* **Filtros de Reconstrução Avançados:** Migração histórica de métodos analíticos puramente determinísticos como a **Retroprojeção Filtrada (FBP)** — que exige maiores doses para suprimir artefatos de ruído quântico — para técnicas de **Reconstrução Iterativa (IR)** e, contemporaneamente, **Reconstrução Baseada em Aprendizado Profundo (DLR)**. Algoritmos DLR permitem suprimir agressivamente o ruído estatístico mantendo a resolução espacial e a detectabilidade de lesões de baixo contraste mesmo sob reduções significativas de dose de radiação ionizante.
* **Controle de Qualidade (CQ):** Auditorias metrológicas periódicas garantem a exatidão dos parâmetros de feixe (como a camada semirredutora - CSR e o potencial do tubo em $\text{kVp}$), assegurando que a conversão de energia seja previsível e clinicamente segura.

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Dose Absorvida|dose-absorvida]]
* [[Métricas de Dose em TC|ctdi]]
* [[Métricas de Dose em TC|dlp]]
* [[Filtro de Reconstrução|filtro-de-reconstrucao]]
* [[retroprojetor-filtrado]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Machine Learning|aprendizado-profundo]]
* [[Radioproteção|alara]]
* [[Controle de Qualidade em TC|controle-de-qualidade]]