---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radioprotecao, radiobiologia, dosimetria, inteligencia-artificial]
data: 2026-08-25
---

# efeitos-biologicos-da-radiacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os **efeitos biológicos da radiação** ionizante compreendem o conjunto de alterações físico-químicas, bioquímicas, celulares e sistêmicas que ocorrem em sistemas biológicos vivos após a absorção de energia oriunda de campos de radiação eletromagnética de alta energia (raios X, raios $\gamma$) ou corpuscular (prótons, nêutrons, elétrons e íons pesados). Do ponto de vista da física médica, a interação da radiação ionizante com a matéria viva é estocástica no nível atômico, iniciando-se através de processos de ionização e excitação que ocorrem em frações de picossegundos.

A cadeia de eventos radiobiológicos divide-se cronologicamente em três fases distintas:

1. **Fase Física ($10^{-15}$ s a $10^{-12}$ s):** Ocorre a incidência e a absorção de fótons ou partículas, resultando na ejeção de elétrons secundários (*elétrons Compton* ou *fotoelétrons* no escopo da Tomografia Computadorizada - TC). A energia é depositada de forma heterogênea ao longo de trajetórias denominadas *tracks* de radiação, formando íons e radicais excitados.
2. **Fase Químico-Física e Química ($10^{-12}$ s a $10^{-6}$ s):** Os íons e moléculas excitadas reagem rapidamente. Na água, que constitui cerca de 70-80% da célula, ocorre a **radiólise da água**, processo que gera espécies reativas de oxigênio (EROs) e radicais livres altamente reativos, destacando-se o radical hidroxila ($\cdot\text{OH}$), hidrogênio ($\cdot\text{H}$), hidronato ($\text{e}^-_{\text{aq}}$) e peróxido de hidrogênio ($\text{H}_2\text{O}_2$). Cerca de dois terços do dano ao DNA em irradiações de baixa Transferência Linear de Energia (LET) decorrem da ação indireta desses radicais livres.
3. **Fase Biológica (milissegundos a décadas):** Os radicais livres e a ação direta da radiação atacam macromoléculas celulares, com ênfase crítica na molécula de ácido desoxirribonucleico (DNA). O dano ao DNA manifesta-se sob diversas formas: aberrações cromossômicas, quebras de fita simples (*single-strand breaks* - SSB) e quebras de fita dupla (*double-strand breaks* - DSB). Se as DSBs não forem reparadas de maneira correta pelos mecanismos enzimáticos celulares (como *Non-Homologous End Joining* - NHEJ ou *Homologous Recombination* - HR), a célula pode sofrer apoptose, senescência ou mutações viáveis.

Metrologicamente, a quantificação do dano potencial e a regulação de segurança baseiam-se em grandezas dosimétricas padronizadas pela *International Commission on Radiation Units and Measurements* (ICRU) e pela *International Commission on Radiological Protection* (ICRP). As principais grandezas incluem a **Dose Absorvida ($D$)**, a **Dose Equivalente ($H_T$)**, e a **Dose Efetiva ($E$)**.

Do ponto de vista clínico e epidemiológico, os efeitos biológicos classificam-se em duas grandes categorias:
* **Efeitos Determinísticos (ou te Theshold / Reais):** Caracterizam-se pela existência de um limiar de dose abaixo do qual o efeito não ocorre. Acima do limiar, a gravidade da lesão aumenta com o aumento da dose. Decorrem da morte celular em massa e exaustão da capacidade de regeneração tecidual (exemplos: eritema, catarata, epilação, necrose tecidual e síndrome aguda de radiação). Na prática da TC moderna, raramente ocorrem, exceto em procedimentos intervencionistas prolongados ou exames de perfusão mal otimizados.
* **Efeitos Estocásticos (ou Probabilísticos):** Não possuem limiar de dose conhecido; a probabilidade de ocorrência do efeito é função da dose, enquanto a sua gravidade é independente da dose. Resultam primariamente de mutações somáticas não letais em células sobreviventes. Os principais exemplos são a indução de neoplasias malignas (carcinogênese radioinduzida) e efeitos hereditários (transmissíveis à descendência).

---

## 2. Formulação Matemática e Propriedades

Para modelar o risco e a dosimetria associada aos efeitos biológicos, diversas formulações matemáticas são empregadas na física médica e na radiobiologia.

### 2.1. Transferência Linear de Energia (LET) e Eficácia Biológica Relativa (RBE)
A **LET** ($L$) expressa a energia média transferida por unidade de comprimento de trajetória da partícula ionizante na matéria:

$$
L = \frac{dE}{dl}
$$

A **Eficácia Biológica Relativa (RBE)** correlaciona a dose de uma radiação de referência ($D_{\text{ref}}$, tipicamente raios X de 250 kVp) com a dose da radiação de interesse ($D$) necessária para produzir o mesmo nível de efeito biológico:

$$
\text{RBE} = \left. \frac{D_{\text{ref}}}{D} \right|_{\text{efeito isotécnico}}
$$

### 2.2. O Modelo Linear-Quadrático (LQ) de Sobrevivência Celular
O modelo linear-quadrático é o formalismo matemático padrão para descrever a curva de sobrevivência celular ($S(D)$) em função da dose absorvida $D$, refletindo a hipótese de que as lesões letais podem ser induzidas por uma única trilha de radiação (componente linear) ou pela interação cumulativa de duas trilhas independentes (componente quadrático):

$$
S(D) = \frac{N(D)}{N_0} = \exp \left( -\alpha D - \beta D^2 \right)
$$

Onde:
* $S(D)$ é a fração de células sobreviventes após a irradiação com dose $D$.
* $\alpha$ representa o coeficiente de mortalidade celular proporcional à dose (lesão de uma única trilha), medido em $\text{Gy}^{-1}$.
* $\beta$ representa o coeficiente quadrático associado à letalidade por sub-lesões acumuladas de duas trilhas distintas, medido em $\text{Gy}^{-2}$.
* A razão $\alpha/\beta$ indica o nível de dose (em Gy) no qual o componente linear e o quadrático contribuem igualmente para a morte celular. Tecidos com alta taxa de renovação e sensibilidade a efeitos agudos apresentam altos valores de $\alpha/\beta$ (tipicamente $10$ Gy para tecidos de resposta rápida), enquanto tecidos de resposta tardia (como medula espinhal e sistema nervoso central) apresentam baixos valores ($\approx 2$ a $3$ Gy).

### 2.3. Grandezas Dosimétricas e Risco Estocástico
A **Dose Equivalente** em um tecido ou órgão $T$, $H_T$, considera a qualidade da radiação através do fator de ponderação $w_R$:

$$
H_T = \sum_{R} w_R D_{T,R}
$$

A **Dose Efetiva** $E$, expressa em Sieverts ($\text{Sv}$), agrega o risco estocástico ponderado para o corpo humano inteiro, incorporando os fatores de ponderação tecidual $w_T$ (que somam 1,0):

$$
E = \sum_{T} w_T H_T = \sum_{T} w_T \sum_{R} w_R D_{T,R}
$$

Para fins de avaliação de risco populacional e otimização em TC, utiliza-se o conceito de risco atribuível com base no modelo linear sem limiar (*Linear Non-Threshold - LNT*), onde o excesso de risco relativo ou absoluto de indução de câncer proporcional à dose efetiva é dado por:

$$
\text{Risco} = E \times r_{\text{nominal}}
$$

Onde $r_{\text{nominal}}$ representa o coeficiente de probabilidade nominal de morte por câncer induzido por radiação para toda a população (aproximadamente $5,5 \times 10^{-2} \, \text{Sv}^{-1}$ segundo as diretrizes da ICRP Publ. 103).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A Tomografia Computadorizada (TC) é a modalidade de diagnóstico por imagem de maior contribuição para a dose coletiva da população decorrente de exposições médicas. Portanto, a compreensão profunda dos efeitos biológicos da radiação fundamenta toda a estratégia de **radioproteção** e **otimização** clínica.

### 3.1. Métricas de Dose Específicas em TC
Diferente da radiografia planar, a TC expõe o paciente a um feixe rotativo colimado. As grandezas fundamentais no ecossistema da TC incluem:
* **CTDI_{w} (Computed Tomography Dose Index - Weighted):** Média ponderada da dose absorvida medida em câmaras de ionização nos acrílicos de cabeça e corpo (fantasmas de 16 cm e 32 cm de diâmetro):
  
$$
\text{CTDI}_w = \frac{1}{3}\text{CTDI}_{\text{centro}} + \frac{2}{3}\text{CTDI}_{\text{periferia}}
$$

* **CTDI_{vol}:** Normaliza o $\text{CTDI}_w$ pelo passo da hélice (*pitch* $P$), expressando a dose média dentro do volume escaneado:
  
$$
\text{CTDI}_{\text{vol}} = \frac{\text{CTDI}_w}{P}
$$

* **DLP (Dose-Length Product):** Produto do $\text{CTDI}_{\text{vol}}$ pelo comprimento total da varredura ($L$), correlacionando-se fortemente com a energia total depositada e o risco estocástico:
  
$$
\text{DLP} = \text{CTDI}_{\text{vol}} \times L
$$

### 3.2. Estratégias de Otimização e o Princípio ALARA
O princípio **ALARA** (*As Low As Reasonably Achievable*) é implementado na aquisição tomográfica através de:
* **Modulação Automática de Corrente (ATCM):** Ajuste dinâmico do produto corrente-tempo ($mAs$) em função da atenuação angular e longitudinal do paciente, mitigando o excesso de dose em regiões de menor espessura (ombros, pelve anterior).
* **Controle de Tensão do Tubo ($kVp$):** Reduções em $kVp$ (ex: de 120 kVp para 80 ou 70 kVp em protocolos pediátricos ou angio-TCs) alteram o contraste fotoelétrico e reduzem drasticamente a dose absorvida, desde que acompanhadas por algoritmos de reconstrução avançados para suprimir o ruído quântico resultante.

### 3.3. O Papel da Inteligência Artificial e Reconstrução Avançada na Mitigação de Efeitos Biológicos
A evolução computacional e a introdução da Inteligência Artificial (IA) na reconstrução de imagens alteraram o paradigma da dosimetria em TC:
* **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR - Deep Learning Reconstruction):** Tradicionalmente, a redução da dose em TC (diminuição de $mAs$ ou $kVp$) gerava degradação severa da imagem por artefatos de ruído quântico e estrias (*streak artifacts*). Os algoritmos de *Deep Learning Image Reconstruction* (DLIR) e Redes Neurais Convolucionais treinadas para Redução de Ruído (*Denoising*) permitem recuperar a textura e a resolução espacial a partir de dados brutos (*raw data*) adquiridos sob baixíssimas doses. Isso viabiliza reduções de dose efetiva da ordem de 50% a 80% sem perda de acurácia diagnóstica, reduzindo diretamente a probabilidade de efeitos estocásticos.
* **Observadores Computacionais e Avaliação de Qualidade de Imagem baseada em Tarefas:** Modelos matemáticos do sistema visual humano e observadores ideais (como o *Hotelling Observer* e *Channelized Hotelling Observer* - CHO) são empregados na otimização de protocolos de IA em TC, garantindo que a supressão de ruído não elimine detalhes estruturais críticos (como microcalcificações ou pequenos nódulos pulmonares), mantendo o balanço ideal entre o risco biológico e o benefício diagnóstico.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Dosimetria em TC|dosimetria-em-tc]]
* [[ctdi-e-dlp]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[deep-learning-reconstruction-dlir]]
* [[Controle de Qualidade em TC|controle-de-qualidade-em-tc]]
* [[Radioproteção|radioprotecao]]
* [[Artefatos em TC|artefatos-em-tc]]