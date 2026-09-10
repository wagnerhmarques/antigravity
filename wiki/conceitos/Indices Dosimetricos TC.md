---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia, otimizacao]
data: 2026-08-25
---

# Indices_Dosimetricos_TC

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Os **índices dosimétricos em Tomografia Computadorizada (TC)** constituem o arcabouço metrológico fundamental para a quantificação da energia depositada por feixes de raios X colimados em exames tomográficos. Diferentemente da radiografia planar convencional, onde a irradiação é estática e bidimensional, a TC emprega uma fonte de radiação em rotação contínua ao redor do paciente, associada a um movimento de translação da mesa (em varreduras helicoidais) ou a múltiplos cortes sequenciais (em varreduras axiais). Essa geometria complexa resulta em um perfil de dose espacialmente assimétrico e dinâmico, que decai ao longo do eixo longitudinal ($z$) do escâner.

Do ponto de vista metrológico, a medição direta da dose absorvida em tecidos biológicos *in vivo* durante um exame de TC é impraticável e metodologicamente imprecisa. Portanto, a Comissão Internacional de Unidades e Medidas de Radiação (ICRU), em relatórios clássicos como o ICRU Report 54 e posteriormente atualizados no ICRU Report 87, estabeleceu grandezas dosimétricas padronizadas baseadas em medições normalizadas efetuadas com **câmaras de ionização de formato cilíndrico e eixo longo** (tipicamente de $100\text{ mm}$ de comprimento, conhecidas como câmaras de lápis ou *pencil ionization chambers*) inseridas em **fantasmas cilíndricos de PMMA (polimetilmetacrilato)** de dimensões padronizadas para cabeça ($16\text{ cm}$ de diâmetro) e corpo ($32\text{ cm}$ de diâmetro).

Esses índices não representam a dose real absorvida por um paciente específico — visto que ignoram a morfologia individual, a composição tecidual heterogênea e o posicionamento anatômico —, mas funcionam como descritores rigorosos da saída de radiação do equipamento, permitindo o controle de qualidade, a conformidade regulatória, a otimização de protocolos e a estimativa de risco populacional ou individual por meio de grandezas secundárias (como a dose efetiva).

---

## 2. Formulação Matemática e Propriedades

A construção matemática dos índices dosimétricos na TC evoluiu de métricas de corte único para métricas volumétricas e específicas para protocolos com modulação de corrente. 

### A. Dose no Índice de Tomografia Computadorizada ($CTDI$)
O conceito básico é o *Computed Tomography Dose Index* ($CTDI$), definido inicialmente para um único corte como a integral ao longo do eixo longitudinal ($z$) do perfil de dose $D(z)$, normalizada pela espessura nominal do corte ($T$) e pelo número de tomografias adquiridas simultaneamente ($N$):

$$
CTDI = \frac{1}{N \cdot T} \int_{-\infty}^{+\infty} D(z) \, dz
$$

### B. $CTDI_{100}$
Como a integração de $-\infty$ a $+\infty$ é impraticável experimentalmente, o $CTDI_{100}$ restringe os limites de integração ao comprimento ativo padrão de uma câmara de ionização de $100\text{ mm}$:

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

### C. $CTDI_{w}$ (Dose Média Ponderada)
Devido à atenuação do feixe de raios X pela periferia do fantasma e ao endurecimento do feixe, a dose não é homogênea no interior do volume escaneado. O $CTDI_w$ (Weighted $CTDI$) pondera as medições realizadas no centro ($c$) e na periferia ($p$, tipicamente a média de posições a 0°, 90°, 180° e 270°) do fantasma de PMMA:

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Para fantasma de cabeça ($16\text{ cm}$):

$$
CTDI_{w,\text{cab}} = \frac{1}{3} CTDI_{100,c} + \frac{2}{3} CTDI_{100,p}
$$

Para fantasma de corpo ($32\text{ cm}$):

$$
CTDI_{w,\text{corpo}} = \frac{1}{3} CTDI_{100,c} + \frac{2}{3} CTDI_{100,p}
$$

### D. $CTDI_{vol}$ (Dose Tomográfica Volumétrica)
O $CTDI_w$ descreve a dose apenas para uma rotação única (corte axial). Para contemplar a distância entre rotações adjacentes em varreduras helicoidais ou sequenciais, define-se o $CTDI_{vol}$, que incorpora o **Pitch** ($pitch$ ou $I$):

$$
CTDI_{vol} = \frac{CTDI_{w}}{pitch}
$$

Onde o *pitch* é definido, para sistemas helicoidais, como o avanço da mesa por rotação ($d$) dividido pela colimação total do feixe ($N \cdot T$):

$$
pitch = \frac{d}{N \cdot T}
$$

### E. Produto Dose-Comprimento ($DLP$)
O *Dose-Length Product* ($DLP$) quantifica a energia total depositada ao longo de todo o comprimento varrido ($L$) do paciente. É o produto do $CTDI_{vol}$ pelo comprimento total da aquisição anatômica:

$$
DLP = CTDI_{vol} \times L
$$

Sua unidade no Sistema Internacional é o miliGray-centímetro ($\text{mGy}\cdot\text{cm}$). O $DLP$ é a grandeza fundamental utilizada para estimar a dose efetiva ($E$, em $\text{mSv}$) através de coeficientes de conversão específicos por região anatômica ($k$):

$$
E = DLP \times k
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Os índices dosimétricos desempenham papéis críticos em múltiplas frentes da física médica moderna e da engenharia de imagem:

1. **Controle de Quality Assurance (QA) e Conformidade Regulatória:**
   Os valores de $CTDI_{vol}$ e $DLP$ exibidos no console do equipamento antes de cada escaneo (os chamados *CTDI_{\text{w/vol}} display values*) devem concordar com as medições empíricas com câmara de ionização dentro de margens de tolerância estritas (geralmente $\pm 20\%$, conforme protocolos da ACR e IAEA). Desvios indicam falhas na calibração do tubo, degradação do gerador ou problemas na geometria de colimação.

2. **Otimização de Protocolos e Reconstrução Avançada:**
   Com o advento de algoritmos de reconstrução sofisticados — como a **[[Reconstrução Iterativa|Reconstrucao_Iterativa]] (IR)** e a **[[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]] (DLR)** —, os índices dosimétricos permitem quantificar o ganho de eficiência de dose. Algoritmos de DLR conseguem manter a detectabilidade de lesões de baixo contraste (avaliada via *Task-Based Image Quality*) mesmo quando o $CTDI_{vol}$ é reduzido drasticamente em comparação aos protocolos legados de **[[Filtro_Retroprojetado]] (FBP)**.

3. **Gestão de Doses e Notificação de Doutrina Justificativa:**
   Sistemas modernos de TC registram o $DLP$ cumulativo e o $CTDI_{vol}$ no arquivo DICOM de cada série (DICOM Radiation Dose Structured Report - RDSR). Esses metadados alimentam softwares de monitoramento de dose institucional, fundamentais para estabelecer Níveis de Referência Diagnóstica (DRLs) e alertar equipes clínicas quando limiares de dose para efeitos determinísticos cutâneos são excedidos.

4. **Observadores Computacionais e Simulações de Monte Carlo:**
   Em pesquisas avançadas, os índices dosimétricos servem como pontos de ancoragem para validação de simulações de transporte de fótons por **[[Monte_Carlo_TC]]**. Modelos de pacientes virtuais (*phantoms* antropomórficos voxelizados) combinados com mapas de dose derivados do $CTDI$ permitem avaliar com precisão cirúrgica a dose absorvida em órgãos específicos, superando as limitações dos fatores globais de conversão $k$.

---

## 4. Conexões e Wikilinks

* [[Fisica_Radi diagnostico]]
* [[Interacao_Radiacao_Materia]]
* [[Filtro_Retroprojetado]]
* [[Reconstrução Iterativa|Reconstrucao_Iterativa]]
* [[Deep Learning Image Reconstruction (DLR)|Deep_Learning_Reconstruction]]
* [[Monte_Carlo_TC]]
* [[Qualidade Imagem TC|Qualidade_Imagem_TC]]