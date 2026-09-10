---
tipo: tecnologia
tags: [fisica-medica, radioterapia, iort, radiobiologia, dosimetria, aceleradores-lineares, controle-de-qualidade]
data: 2026-08-25
---

# Radioterapia Intraoperatoria (IORT)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Radioterapia Intraoperatória (IORT) é uma modalidade terapêutica avançada que consiste na entrega de uma dose única, alta e precisa de radiação ionizante diretamente sobre o leito tumoral ou sobre um tumor residual visível, imediatamente após a ressecção cirúrgica e com o tecido exposto, antes do fechamento da ferida cirúrgica. Do ponto de vista da física médica e da radiobiologia, a principal vantagem da IORT reside na ablação de órgãos de risco (OARs) adjacentes — que podem ser fisicamente deslocados, afastados ou blindados pelo cirurgião — permitindo a escalada de dose no volume alvo (GTV/CTV) e a minimização da toxicidade nos tecidos sadios circundantes.

Historicamente, a IORT utilizava feixes de elétrons gerados por aceleradores lineares convencionais modificados (com o paciente sendo transportado da sala de cirurgia para o bunker de tratamento) ou unidades dedicadas de raios X de baixa energia. Atualmente, os sistemas modernos de IORT dividem-se primariamente em duas categorias tecnológicas:

1. **Aceleradores Lineares Móveis de Elétrons (IOERT):** Produzem feixes de elétrons com energias tipicamente variando entre $4\text{ MeV}$ e $12\text{ MeV}$ (às vezes até $9\text{ MeV}$ ou $10\text{ MeV}$). Os elétrons possuem a propriedade física de uma taxa de dose constante em profundidade seguida por uma queda abrupta (o "brush" ou alcance prático, $R_p$), o que protege estruturas profundas além do leito cirúrgico.
2. **Sistemas de Raios X de Baixa Energia (ex: Intrabeam):** Utilizam sondas esféricas que geram fótons de baixa energia (tipicamente $50\text{ kV}$). A taxa de dose decai de forma inversamente proporcional ao quadrado da distância e devido à atenuação fotoelétrica, resultando em um gradiente de dose extremamente acentuado nos primeiros milímetros de tecido.

A metrologia da radiação em IORT apresenta desafios singulares devido à altíssima taxa de dose por pulso (em aceleradores lineares) e aos gradientes extremos de dose. A calibração dos feixes é regida por protocolos internacionais rigorosos, como o AAPM TG-72 e o IAEA TRS-398, exigindo o uso de câmaras de ionização adequadas, filmes radiocrômicos e dosimetria termoluminescente (DTL) para mapeamento tridimensional de dose em meio homogêneo e fantomas de água sólida.

---

## 2. Formulação Matemática e Propriedades (se aplicável)

Do ponto de vista radiobiológico, a IORT entrega uma dose única equivalente elevada ($D$). Para correlacionar a dose única da IORT ($d_{\text{IORT}}$) com o fracionamento convencional, utiliza-se o modelo Linear-Quadrático (LQ), avaliando a Biologically Effective Dose ($\text{BED}$):

$$
\text{BED} = D \left( 1 + \frac{d}{\alpha/\beta} \right)
$$

Onde:
- $D$ é a dose total aplicada.
- $d$ é a dose por fração.
- $\alpha/\beta$ é a razão entre os parâmetros de radiosensibilidade celular para o tecido em questão (tipicamente $3\text{ Gy}$ para tecidos sadios tardio-repondentes e $10\text{ Gy}$ para tumores agudo-repondentes).

Para feixes de elétrons utilizados em IORT, a distribuição de dose em profundidade $z$ pode ser modelada analiticamente por aproximações semi-empíricas. A dose absorvida $D(z)$ ao longo do eixo central do aplicador cilíndrico é descrita por:

$$
D(z) = D_{\max} \cdot P(z) \cdot \prod_{i} \left( 1 - \mu_i x_i \right)
$$

Onde $D_{\max}$ é a dose máxima no eixo central, $P(z)$ representa a curva decentrada de penetração percentual em profundidade para elétrons, e o produtório termoelétrico/geométrico corrige para a presença de aplicadores de diâmetros finitos e efeitos de dispersão lateral (*side-scatter*).

Para sistemas de raios X de baixa energia baseados em sondas isotrópicas, a taxa de dose $\dot{D}(r)$ em função da distância radial $r$ a partir do centro da fonte esférica de raio $r_0$ é governada pela lei do inverso do quadrado da distância modificada por um fator de atenuação linear efetiva $\mu_{\text{eff}}$:

$$
\dot{D}(r) = \dot{D}(r_0) \left( \frac{r_0}{r} \right)^2 e^{-\mu_{\text{eff}}(r - r_0)}
$$

Onde o coeficiente $\mu_{\text{eff}}$ depende fortemente do espectro de energia polienergético dos fótons de $50\text{ kVp}$ e da composição elemental do tecido (efeito fotoelétrico predominante, proporcional a $Z^3/E^3$).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada, Imagem e Otimización

Embora a IORT ocorra no centro cirúrgico, a integração com métodos de imagem avançados — incluindo a [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]], Ressonância Magnética (RM) e Ultrassom Intraoperatório — é fundamental para o planejamento cirúrgico e dosimétrico:

1. **Planejamento Cirúrgico e Fusão de Imagens:** Imagens de TC pré-operatórias são frequentemente fundidas com exames funcionais ou volumétricos para definir com precisão o volume alvo clínico (CTV) antes da ressecção.
2. **Cálculo de Dose Baseado em Imagem (Monte Carlo):** Devido à heterogeneidade dos tecidos expostos durante a cirurgia (osso, gordura, ar, tecido muscular), o uso de algoritmos analíticos tradicionais falha. Softwares de planejamento dedicados à IORT utilizam simulações de Monte Carlo baseadas em geometrias extraídas de imagens de TC para calcular a distribuição exata de dose considerando as interfaces de densidade eletrônica.
3. **Controle de Qualidade (QC) Dosimétrico:** A garantia da qualidade em IORT exige testes diários e mensais rigorosos da energia do feixe, uniformidade do campo de radiação e constância da taxa de dose, utilizando arranjos de diodos semicondutores e matrizes de ionização de alta resolução espacial.
4. **Otimização do Blindamento e Proteção Radiológica:** Como a IORT é realizada em salas cirúrgicas convencionais adaptadas (e não em bunkers blindados dedicados), cálculos rigorosos de barreiras estruturais primárias e secundárias — considerando o fator de uso $U$, o fator de ocupação $T$ e a carga de trabalho $W$ — são mandatários para garantir a conformidade com as normas de radioproteção para equipe cirúrgica e público externo.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]
- [[Aceleradores Lineares (LINAC)]]
- [[Dosimetria em Radiologia|Dosimetria da Radiação]]
- [[Radiobiologia]]
- [[Controle de Qualidade em Radioterapia]]
- [[Sim Monte Carlo em Física Médica]]