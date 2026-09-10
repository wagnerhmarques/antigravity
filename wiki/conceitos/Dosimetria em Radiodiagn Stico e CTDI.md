---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiodiagnostico, dosimetria, ctdi, radioprotecao]
data: 2026-08-25
---

# Dosimetria em Radiodiagnóstico e CTDI

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A dosimetria em radiodiagnóstico abrange o conjunto de métodos analíticos, experimentais e numéricos empregados para quantificar a energia depositada por radiações ionizantes em meios materiais (tecidos biológicos ou simuladores antropomórficos) decorrente de procedimentos diagnósticos. Diferente da radioterapia — onde a precisão volumétrica absoluta na região tumoral é o foco primário —, a dosimetria diagnóstica prioriza a estimativa de riscos estocásticos populacionais e a verificação do cumprimento de Níveis de Referência Diagnósticos (NRD), balanceando a qualidade de imagem necessária para o diagnóstico médico com a otimização da dose (princípio ALARA — *As Low As Reasonably Achievable*).

No contexto específico da Tomografia Computadorizada (TC), a complexidade geométrica da irradiação — caracterizada por um feixe estreito colimado em rotação contínua ao redor do paciente — tornou impraticável o uso direto de grandezas tradicionais de ponto, como a kerma no ar livre no eixo de rotação. Para contornar essa limitação metrológica, o *Computed Tomography Dose Index* (**CTDI**, ou Índice de Dose em Tomografia Computadorizada) foi estabelecido como a grandeza padrão fundamental. 

O CTDI fundamenta-se na premissa de integrar o perfil de dose ao longo do eixo longitudinal de varredura ($z$), utilizando uma câmara de ionização de comprimento padrão (geralmente $100\text{ mm}$) posicionada em simuladores cilíndricos padronizados de PMMA (polimetilmetacrilato) que representam a cabeça (diâmetro de $16\text{ cm}$) e o corpo (diâmetro de $32\text{ cm}$). A grandeza mede a energia total absorvida por unidade de massa ao longo de uma rotação completa do tubo de raios X, normalizada pela espessura nominal do feixe colimado.

---

## 2. Formulação Matemática e Propriedades

A formulação matemática do CTDI evoluiu para contemplar perfis de dose assimétricos e espalhamento multifásicos. A base de todas as métricas é o **CTDI elementar** ou perfil de dose ao longo do eixo $z$, denotado por $D(z)$, gerado por uma única rotação axial.

### 1. CTDI no Ar ($CTDI_{\text{air}}$)
Medido no ponto isocêntrico do gantry, sem a presença de simuladores, utilizando uma câmara de ionização tipo Lapis (lápis) de comprimento ativo $L$:

$$
CTDI_{\text{air}} = \frac{1}{N \cdot T} \int_{-\infty}^{+\infty} D_{\text{air}}(z) \, dz
$$

Onde:
* $N$ é o número de canais de detecção ativados simultaneamente por rotação.
* $T$ é a espessura nominal do tomograma (colimação) adquirida por cada canal no eixo isocêntrico.
* O produto $N \cdot T$ representa a espessura total do feixe nominal ($d$).

### 2. $CTDI_{100}$
Medido no interior de um simulador cilíndrico padrão de PMMA (16 cm para crânio, 32 cm para abdômen) utilizando a mesma câmara de ionização de $100\text{ mm}$ de comprimento:

$$
CTDI_{100} = \frac{1}{N \cdot T} \int_{-50\text{ mm}}^{+50\text{ mm}} D(z) \, dz
$$

Onde os limites de integração correspondem exatamente ao comprimento padrão de integração da câmara ($100\text{ mm}$).

### 3. $CTDI_{\text{w}}$ (Weighted CTDI - CTDI Ponderado)
Como a dose não é homogênea ao longo da secção transversal do paciente (sendo tipicamente mais alta na periferia devido à atenuação da radiação e mais baixa no centro), o $CTDI_{\text{w}}$ introduz ponderações geométricas entre as medidas centrais e periféricas do simulador:

$$
CTDI_{\text{w}} = \frac{1}{3} CTDI_{100,\text{centro}} + \frac{2}{3} CTDI_{100,\text{periferia}}
$$

Onde $CTDI_{100,\text{periferia}}$ é a média aritmética das medições obtidas nas quatro posições periféricas do simulador (geralmente nos ângulos de $0^\circ, 90^\circ, 180^\circ$ e $270^\circ$).

### 4. $CTDI_{\text{vol}}$ (Volume CTDI)
Para aquisições helicoidais (*spiral*) ou axiais sequenciais com espaçamento, o *pitch* helicoidal ($p$) altera a sobreposição ou o espaçamento entre as rotações. O $CTDI_{\text{vol}}$ reflete a dose média real administrada no volume escaneado, corrigida pelo fator de avanço da mesa:

$$
CTDI_{\text{vol}} = \frac{CTDI_{\text{w}}}{p}
$$

Onde o *pitch* ($p$) é definido por:
* Para TC Helicoidal: $p = \frac{\text{Avanço da mesa por rotação}}{\text{Colimação total do feixe } (N \cdot T)}$
* Para TC Axial (Seqüencial): $p = \frac{\text{Avanço da mesa entre varreduras}}{\text{Colimação total do feixe } (N \cdot T)}$

### 5. DLP (Dose-Length Product - Produto Dose-Comprimento)
Embora o $CTDI_{\text{vol}}$ quantifique a intensidade da dose na região irradiada, ele não depende da extensão anatômica. O DLP integra a dose ao longo de todo o comprimento da varredura ($L_{\text{scan}}$):

$$
\text{DLP} = CTDI_{\text{vol}} \times L_{\text{scan}}
$$

A unidade do DLP é $\text{mGy}\cdot\text{cm}$. A partir do DLP, é possível estimar a **Dose Efetiva** ($E$, em $\text{mSv}$) através de coeficientes de conversão específicos por região anatômica ($k$, em $\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$):

$$
E = \text{DLP} \times k
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria baseada em CTDI constitui a espinha dorsal dos programas de **Controle de Qualidade (CQ)** e gestão de dose em equipamentos de tomografia computadorizada modernos. Sua relevância técnica manifesta-se em diversas frentes:

* **Conformidade Regulatória e NRDs:** Órgãos reguladores utilizam limites de $CTDI_{\text{vol}}$ e DLP para estabelecer Níveis de Referência Diagnósticos. Desvios sistemáticos para cima indicam falhas de calibração do tubo, filtragem inadequada ou protocolos clínicos excessivamente agressivos.
* **Sistemas de Reconstrução e Gestão Automática de Dose:** Com o advento de algoritmos avançados de reconstrução — como a Reconstrução Iterativa (IR) e técnicas baseadas em Deep Learning Reconstruction (DLR) —, a dependência de altos valores de $CTDI_{\text{vol}}$ para mitigar o ruído quântico foi drasticamente reduzida. Os sistemas modernos de controle automático de corrente (*Automatic Tube Current Modulation - ATCM*) ajustam dinamicamente a exposição com base no $CTDI_{\text{vol}}$ projetado para manter o ruído constante em diferentes espessuras corporais.
* **Limitações Metrológicas Atuais:** O $CTDI_{100}$ convencional apresenta restrições físicas quando aplicado a TCs de múltiplos canais de grande cobertura longitudinal (ex: scanners de $160\text{ cm}$ ou $320$ fileiras de detetores, cobrindo até $16\text{ cm}$ por rotação). Devido ao espalhamento em grandes volumes, a integração limitada a $100\text{ mm}$ subestima a dose real. Para solucionar isso, a força-tarefa AAPM TG-200 introduziu o conceito de **$CTDI_{\infty}$** e metodologias baseadas em simuladores estendidos e integração de perfil irrestrita.
* **Simulações Computacionais e Dosimetria Baseada em Voxels:** Em ambientes de pesquisa avançada, os valores de CTDI servem de calibração para simulações de Monte Carlo executadas em fantomas computacionais (como os modelos baseado em NURBS e malhas computacionais dos simuladores ICRP/MIRD), permitindo calcular a dose órgão a órgão com alta fidelidade anatômica e avaliar riscos biológicos específicos para observadores computacionais e avaliações de qualidade de imagem baseadas em tarefas.

---

## 4. Conexões e Wikilinks

* [[Física da Tomografia Computadorizada]]
* [[Controle de Qualidade em TC|Controle de Qualidade em Radiodiagnóstico]]
* [[Reconstrução Iterativa|Reconstrução Iterativa e DLR]]
* [[Efeitos Biológicos das Radiações Ionizantes]]
* [[Princípio ALARA e Radioproteção]]
* [[Simula o de Monte Carlo em F Sica M Dica|Simulação de Monte Carlo em Física Médica]]