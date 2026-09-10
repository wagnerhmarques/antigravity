---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiodiagnostico, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# Dosimetria em Radiodiagnóstico

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **dosimetria em radiodiagnóstico** engloba o conjunto de métodos teóricos, experimentais e computacionais empregados para quantificar a energia depositada por radiações ionizantes (majoritariamente raios X) nos tecidos biológicos e em meios materiais de referência durante procedimentos de imagem médica. Diferentemente da radioterapia — onde os feixes são altamente direcionados, fracionados e com foco primário na destruição tecidual local —, o radiodiagnóstico caracteriza-se por campos de radiação de baixa a média energia (tipicamente $20\text{ keV}$ a $150\text{ keV}$), geometrias complexas de irradiação rotacional ou helicoidal, e pelo objetivo diagnóstico primário, o que impõe restrições severas de otimização sob o princípio ALARA (*As Low As Reasonably Achievable*).

Metrologicamente, a grandeza fundamental de base para a quantificação da radiação em feixes de raios X diagnósticos é a **Kerma no ar** (*Air Kerma*, $K$, do inglês *Kinetic Energy Released in Matter*), medida em cinys ($\text{Gy}$). O Kerma representa a energia cinética inicial transferida pelas partículas ionizantes indiretamente ionizantes (fótons) para elétrons secundários por unidade de massa em um volume infinitesimal de ar livre. No entanto, para avaliação de risco estocástico e determinação de efetividade biológica, a metrologia moderna migrou para grandezas dosimétricas baseadas na **Dose Absorvida** ($D$, em $\text{Gy}$ ou $\text{mGy}$), além de grandezas de proteção e operacionais recomendadas pela *International Commission on Radiological Protection* (ICRP), tais como a **Dose Equivalente** ($H_T$) e a **Dose Efetiva** ($E$).

Devido à impossibilidade prática de medir diretamente a dose em órgãos internos de pacientes in vivo, a dosimetria em radiodiagnóstico fundamenta-se amplamente no uso de simuladores antropomórficos físicos (*phantoms*), câmaras de ionização de dedal padronizadas (ex: câmaras tipo Farmer ou de cavidade cilíndrica de pequeno volume), dosímetros termoluminescentes (TLD), dosímetros opticamente estimulados por luminescência (OSLD) e, preponderantemente na era contemporânea, em simulações computacionais de Monte Carlo baseadas em modelos anatômicos vetoriais e baseados em *mesh/voxel*.

---

## 2. Formulação Matemática e Propriedades

A formulação matemática da dosimetria em radiodiagnóstico varia conforme a grandeza de interesse e a modalidade de imagem. Na Tomografia Computadorizada (TC), a grandeza padrão para controle de qualidade e especificação de equipamentos é a **Dose Tomográfica Computadorizada no Índice** ($\text{CTDI}$, *Computed Tomography Dose Index*), definida a partir da integral ao longo do eixo longitudinal ($z$) do perfil de dose para uma única rotação do tubo:

$$
\text{CTDI}_{100} = \frac{1}{nT} \int_{-50\text{ cm}}^{+50\text{ cm}} D(z) \, dz
$$

Onde:
- $n$ é o número de tomografias (canais) adquiridos simultaneamente por rotação.
- $T$ é a largura nominal de cada corte tomográfico no isocentro ($mm$).
- $D(z)$ é o perfil de dose absorvida ao longo do eixo $z$.
- O limite de integração de $\pm 50\text{ mm}$ corresponde ao comprimento padrão de integração medido com uma câmara de ionização de lápis (*pencil chamber*) de $100\text{ mm}$ de comprimento.

Para contabilizar a variação espacial da dose entre as regiões periférica e central dos simuladores cilíndricos padrão de polimetilmetacrilato (PMMA) — com diâmetros de $16\text{ cm}$ (cabeça/pediátrico) e $32\text{ cm}$ (abdome/adulto) —, define-se a **CTDI ponderada** ($\text{CTDI}_{w}$):

$$
\text{CTDI}_{w} = \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}}
$$

Em sistemas helicoidais modernos, a introdução do avanço da mesa por rotação (passo ou *pitch*, denotado por $p$) exige o cálculo da **CTDI volume** ($\text{CTDI}_{vol}$), que normaliza a dose entregue considerando o espaçamento helicoidal:

$$
\text{CTDI}_{vol} = \frac{\text{CTDI}_{w}}{p}
$$

Onde o *pitch* $p$ é definido matematicamente por:

$$
p = \frac{d}{nT}
$$

Sendo $d$ o deslocamento linear da mesa por rotação de $360^\circ$.

Para estimar a energia total depositada ao longo de um exame completo de tomografia, emprega-se o **Produto Dose-Comprimento** ($\text{DLP}$, *Dose-Length Product*), expresso em $\text{mGy}\cdot\text{cm}$:

$$
\text{DLP} = \text{CTDI}_{vol} \times L
$$

Onde $L$ é o comprimento total escaneado anatomicamente.

A transição da dose física para o risco biológico radi Induzido é formalizada através da **Dose Efetiva** ($E$), calculada pela soma ponderada das doses equivalentes médias nos tecidos irradiados ($H_T$), multiplicadas pelos fatores de peso tecidual específicos da ICRP ($w_T$):

$$
E = \sum_{T} w_T H_T = \sum_{T} w_T \left( \sum_{R} w_R D_{T,R} \right)
$$

Onde $w_R$ é o fator de ponderação da radiação (para fótons de raios X, $w_R = 1$) e $D_{T,R}$ é a dose absorvida média no tecido $T$ devida à radiação $R$. Alternativamente, no contexto de exames de TC, a Dose Efetiva pode ser estimada pragmaticamente a partir do DLP utilizando coeficientes de conversão específicos por região anatômica ($k$, em $\text{mSv}\cdot\text{mGy}^{-1}\cdot\text{cm}^{-1}$):

$$
E \approx \text{DLP} \times k_{região}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria em Tomografia Computadorizada assume papel central devido às altas taxas de dose absorvida inerentes à modalidade em comparação à radiografia convencional. A otimização dos protocolos de TC depende diretamente da capacidade de monitorar, prever e mitigar a dose sem comprometer a diagonsabilidade da imagem, que é avaliada por métricas como a relação sinal-ruído ($\text{SNR}$) e a função de transferência de modulação ($\text{MTF}$).

### Controle de Qualidade e Conformidade Regulatória
Os índices $\text{CTDI}_{100}$, $\text{CTDI}_{w}$ e $\text{CTDI}_{vol}$ são mandatórios em programas de controle de qualidade (CQ) para assegurar que os tubos de raios X e os geradores operem dentro de tolerâncias estritas (tipicamente $\pm 20\%$ dos valores nominais informados pelo fabricante). O monitoramento sistemático previne falhas catastróficas de calibração e exposições iatrogênicas desnecessárias.

### Integração com Algoritmos de Reconstrução e IA
Historicamente, a redução da dose em TC resultava em degradação severa da imagem por aumento do ruído quântico na retroprojeção filtrada tradicional ($\text{FBP}$). A dosimetria moderna atua em simbiose com:
- **Reconstrução Iterativa (IR):** Modelam estatísticas de ruído e física de aquisição para permitir reduções de dose da ordem de $30\%$ a $60\%$.
- **Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction* - DLR):** Redes neurais convolucionais (CNNs) e arquiteturas baseadas em *Transformers* treinadas para remover ruído de texturas em doses ultra-baixas, mantendo a integridade estrutural anatômica. A dosimetria nestes cenários estuda a preservação de detalhes espaciais finos (ex: microestruturas do osso trabecular ou pequenos nódulos pulmonares) sob restrições severas de $\text{CTDI}_{vol}$.

### Gestão Automatizada de Dose e Observadores Computacionais
Sistemas modernos de TC registram o DLP e a $\text{CTDI}_{vol}$ diretamente no cabeçalho DICOM (*Radiation Dose Structured Report* - RDSR). Ferramentas de inteligência artificial e mineração de dados analisam esses registros em larga escala para auditorias institucionais. Adicionalmente, a dosimetria computacional acoplada a **observadores computacionais** (como o observador ideal e o *Channelized Hotelling Observer* - CHO) permite modelar matematicamente a capacidade de detecção de lesões por tarefas específicas (ex: detecção de AVC isquêmico precoce), correlacionando diretamente a dose física administrada com o desempenho diagnóstico final.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Física das Radiações|Física da Radiação]]
- [[Controle de Qualidade em TC|Controle de Qualidade em Radiodiagnóstico]]
- [[Simulação de Monte Carlo em Medicina]]
- [[Reconstrução de Imagem (FBP, IR e DLR)]]
- [[Radioproteção e Bioética]]
- [[Processamento de Imagens Médicas]]