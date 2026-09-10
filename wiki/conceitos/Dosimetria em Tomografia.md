---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, dosimetria, radioprotecao, metrologia-das-radiacoes]
data: 2026-08-25
---

# dosimetria-em-tomografia

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A dosimetria em Tomografia Computadorizada (TC) constitui o ramo da física médica dedicado à mensuração, cálculo e modelagem da deposição de energia decorrente da radiação X ionizante em meios materiais, com ênfase particular nos tecidos biológicos humanos. Diferentemente da radiografia planar convencional, onde o campo de radiação é estático e bidimensional, a TC emprega fontes móveis de raios X (usualmente tubos termoiónicos acoplados a geradores de alta tensão) que rotacionam em torno do paciente, gerando feixes colimados estreitos, com perfis de dose complexos caracterizados por caudas deradiação espalhada (*scatter tails*) substanciais ao longo do eixo longitudinal ($z$).

Metrologicamente, a complexidade da dosimetria em TC reside na geometria helicoidal ou axial de aquisição, na modulação dinâmica de corrente ($mA$), nos filtros de conformação do feixe (*bow-tie filters*) e nos protocolos com variação de pitch. Para padronizar a avaliação de risco estocástico e o controle de qualidade dos equipamentos, a Comissão Internacional de Unidades e Medidas de Radiação (ICRU) e a Associação Americana de Físicos em Medicina (AAPM), através dos relatórios clássicos AAPM TG-32, TG-111 e ICRU Report 87, estabeleceram grandezas dosimétricas padronizadas.

As grandezas fundamentais não medem diretamente a energia absorvida em um órgão específico (*Dose Absorvida*, $D$), mas utilizam detectores de câmara de ionização tipo lápis (*pencil ionization chamber*) com comprimento ativo padrão de $100\text{ mm}$ inseridos em fantasmas (*phantoms*) normalizados de polimetilmetacrilato (PMMA) de formas cilíndricas (representando a cabeça e o corpo, com diâmetros típicos de $16\text{ cm}$ e $32\text{ cm}$, respectivamente). A partir dessas medições padronizadas, derivam-se métricas operacionais que permitem estimar o risco radiológico populacional e otimizar protocolos clínicos, equilibrando a qualidade de imagem — inerentemente ligada ao ruído estatístico e à resolução espacial — e a restrição da dose efetiva entregue ao paciente.

---

## 2. Formulação Matemática e Propriedades

A pedra angular da dosimetria em TC é a **Dose Média no Tomograma** (*Computed Tomography Dose Index* - CTDI), derivada da integração espacial do perfil de dose ao longo do eixo longitudinal $z$ para uma única rotação do tubo.

### 2.1. CTDI e suas Variações

O **CTDI livre no ar** ($CTDI_{air}$) é definido pela integral do perfil de dose $D(z)$ ao longo de todo o eixo $z$, normalizado pela espessura nominal do feixe colimado $nT$:

$$
CTDI_{100} = \frac{1}{nT} \int_{-50\text{ cm}}^{+50\text{ cm}} D(z) \, dz
$$

Onde:
- $n$ é o número de cortes tomográficos adquiridos simultaneamente por rotação.
- $T$ é a largura nominal de cada corte (em mm) no eixo isocêntrico.
- $D(z)$ é o perfil de dose ao longo do eixo $z$.
- Os limites de integração $\pm 50\text{ mm}$ correspondem ao comprimento ativo padrão ($100\text{ mm}$) da câmara de ionização.

Para contemplar as heterogeneidades de atenuação e espalhamento no corpo humano, utiliza-se o **CTDI ponderado** ($CTDI_{w}$), que pondera as doses medidas na periferia ($CTDI_{supp}$) e no centro ($CTDI_{cent}$) do fantasma de PMMA:

$$
CTDI_{w} = \frac{1}{3} CTDI_{100,\text{cent}} + \frac{2}{3} CTDI_{100,\text{supp}}
$$

Em varreduras helicoidais (espirais), a introdução do conceito de *pitch* ($P$) afeta diretamente a dose acumulada. O **CTDI volume** ($CTDI_{vol}$) quantifica a dose média em um volume escaneado, corrigida pelo avanço da mesa por rotação:

$$
CTDI_{vol} = \frac{CTDI_{w}}{P}
$$

Onde o *pitch* helicoidal $P$ é definido por:

$$
P = \frac{d}{n \cdot T}
$$

sendo $d$ o deslocamento longitudinal da mesa por rotação de $360^\circ$.

### 2.2. Dose Integral e Dose Efetiva

Para estimar o risco estocástico associado a um exame completo, calcula-se a **Dose Específica do Tamanho do Paciente** (*Size-Specific Dose Estimate* - SSDE), que corrige o $CTDI_{vol}$ com base no diâmetro efetivo $D_{eff}$ ou na área transversal do paciente obtida a partir do topograma (*scout view*):

$$
SSDE = f_{size} \cdot CTDI_{vol}
$$

O fator de correção $f_{size}$ é uma função exponencial do diâmetro transversal equivalente ou da soma das dimensões anteroposterior ($AP$) e lateral ($LAT$):

$$
f_{size} \approx a \cdot e^{-b \cdot (AP + LAT)}
$$

Finalmente, a **Dose Efetiva** ($E$), expressa em Sieverts ($Sv$), correlaciona a estocasticidade do dano biológico integrado sobre os diferentes tecidos irradiados, ponderados por seus respectivos coeficientes de sensibilidade radiológica ($w_T$, definidos pela ICRP 103):

$$
E = \sum_{T} w_T \cdot D_T = \sum_{T} w_T \left( \frac{1}{M_T} \int_{M_T} D(x,y,z) \, dm \right)
$$

Onde $D_T$ é a dose absorvida média no tecido ou órgão $T$ de massa $M_T$. Na prática clínica, $E$ é frequentemente estimado multiplicando-se o **Produto Dose-Comprimento** ($DLP$) por um fator de conversão específico da região anatômica ($k$):

$$
DLP = CTDI_{vol} \cdot L
E = DLP \cdot k
$$

sendo $L$ o comprimento total da varredura anatômica.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A dosimetria em TC desempenha um papel central na garantia da qualidade clínica, na conformidade regulatória e no avanço tecnológico dos sistemas de imagem moderna. Suas principais frentes de aplicação englobam:

1. **Controle de Qualidade (CQ) e Conformidade Regulatória:** As medições periódicas de $CTDI$ com câmaras de ionização e fantasmas padronizados asseguram que o rendimento do tubo de raios X e a calibração do gerador operem dentro dos limites tolerados pelas agências reguladoras (como CNEN no Brasil e FDA internacionalmente).
2. **Otimização de Protocolos e Princípio ALARA:** A dosimetria quantitativa permite aos físicos médicos ajustar os parâmetros de aquisição — como quilovoltagem de pico ($kVp$), corrente efetiva ($mAs$), tempo de rotação e algoritmos de modulação espacial de dose — para minimizar a dose sem degradar a detectabilidade de lesões.
3. **Integração com Algoritmos de Reconstrução Avançados:** Com o advento da **Retroalimentação de Reconstrução Iterativa (IR)** e da **Reconstrução Baseada em Aprendizado Profundo (DLR)**, os sistemas modernos conseguem operar com doses substancialmente menores ($CTDI_{vol}$ reduzido) mantendo a relação sinal-ruído (SNR) e a resolução espacial em patamares diagnósticos ideais. A dosimetria fornece a métrica de entrada e validação para essas abordagens computacionais.
4. **Dosimetria Baseada em Paciente e Sistemas de Rastreamento:** Softwares modernos de monitoramento de dose coletam automaticamente o $DLP$ e o $CTDI_{vol}$ de cada exame realizado no setor de radiodiagnóstico, integrando-os ao prontuário eletrônico do paciente para auditorias de níveis de referência diagnóstica (NRD / *Diagnostic Reference Levels* - DRL).
5. **Avaliação de Risco em Observadores Computacionais:** Estudos fantasma virtuais e simulações de Monte Carlo acoplam a modelagem física da dosimetria a observadores ideais/humanos simulados matematicamente para avaliar o impacto estocástico de novas tecnologias de hardware (ex: detectores de contagem de fótons - PCD-CT).

---

## 4. Conexões e Wikilinks

- [[Fisica dos Raios X|fisica-dos-raios-x]]
- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
- [[Artefatos em TC|artefatos-em-tomografia]]
- [[detector-de-contagem-de-foton]]
- [[otimizacao-e-radioprotecao]]