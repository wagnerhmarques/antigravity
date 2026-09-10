---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, radioprotecao\, dosimetria, qualidade-de-imagem]
data: 2026-08-25
---

# colimação

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **colimação** em Tomografia Computadorizada (TC) é o processo físico-mecânico e eletrônico de restrição da geometria espacial, largura e divergência do feixe de raios X antes da sua interação com o paciente e/ou após a travessia do volume anatômico. Do ponto de vista metrológico e radiológico, a colimação atua como o principal meio de controle primário para a conformação do campo de radiação\, determinando diretamente a espessura do corte tomográfico nominal, o perfil de dose no eixo longitudinal ($z$) e a mitigação da radiação dispersa (*scatter*) que incide sobre os elementos do detector.

Historicamente e estruturalmente, a colimação em sistemas modernos de TC helicoidal e multidetectores (MDCT) divide-se em duas etapas fundamentais:
1. **Colimação Pré-paciente (ou Pré-objeto):** Localizada na saída do tubo de raios X, antes que o feixe atinja o paciente. É composta por lâminas pesadas de tungstênio que moldam o feixe no plano axial ($x$-$
u$) e longitudinal ($z$). Sua função principal é eliminar fótons periféricos que não contribuem para a formação da imagem diagnóstica, reduzindo drasticamente a dose integral absorvida pelo paciente e minimizando o volume de tecido irradiado, o que, por conseguinte, reduz a geração de radiação espalhada.
2. **Colimação Pós-paciente (ou Pós-objeto / Anti-scatter grids):** Posicionada imediatamente antes do arranjo de detectores de estado sólido (geralmente compostos por tungstato de cádmio ou cerâmicas de gadolínio). Consiste em lamelas finas de metal (frequentemente chumbo ou tungstênio) alinhadas focalmente com o foco do tubo. Sua função é absorver fótons que sofreram espalhamento Compton dentro do corpo do paciente e que se desviaram de sua trajetória retilínea, impedindo que atinjam os detectores com informações direcionais errôneas, o que degradaria a relação contraste-ruído (CNR) e geraria artefatos de endurecimento de feixe e sombreamento.

---

## 2. Formulação Matemática e Propriedades

A geometria da colimação define o perfil de sensibilidade do corte e a eficiência geométrica do sistema. Seja $T$ a espessura nominal do corte selecionada no console, $N$ o número de fileiras de detectores ativas e $S$ a largura física de cada elemento detector individual medido no isocentro do gantry. A colimação total no eixo $z$\, denotada por $W_z$, é expressa por:

$$
W_z = N \times S
$$

Em sistemas de TC helicoidal, a velocidade de translação da mesa ($d$) em relação à rotação do gantry ($360^\circ$) define o parâmetro de passo helicoidal (*pitch*), representado por $p$:

$$
p = \frac{d}{W_z} = \frac{d}{N \cdot S}
$$

O perfil de dose ao longo do eixo longitudinal, $D(z)$, gerado por uma varredura de rotação única ou helicoidal, está diretamente correlacionado com a abertura da colimação pré-paciente. A Dose Integral Relativa ($DI$) em função da largura de colimação pode ser modelada considerando o espalhamento longitudinal por meio da integral do perfil de dose:

$$
DI = \int_{-\infty}^{+\infty} D(z) \, dz
$$

Para feixes colimados estreitos ($W_z$ pequeno), a dispersão de radiação secundária é proporcionalmente menor em relação ao volume primário do que em feixes largos. A eficiência geométrica da colimação pré-paciente ($\eta_g$) é definida como a razão entre a largura do feixe efetiva no plano de imagem e a largura total emitida pelo ponto focal:

$$
\eta_g = \frac{\int_{-\infty}^{+\infty} \Phi(x, y, z) \, dz}{\Phi_{\text{total}}}
$$

Onde $\Phi(x, y, z)$ representa a fluência de fótons transmitida pelo sistema de colimadores. A presença de imperfeições mecânicas ou um ponto focal finito ($F$) introduz uma região de penumbra geométrica ($P_g$), calculada pela semelhança de triângulos entre a distância focal ao anteparo ($SID$), a distância do foco ao colimador ($FCD$) e a abertura do colimador ($A$):

$$
P_g = F \cdot \left( \frac{SID - FCD}{FCD} \right)
$$

Esta penumbra afeta diretamente a modulação do perfil de dose e a resolução espacial na direção $z$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A otimização da colimação é um dos pilares da gestão da qualidade e da radioproteção em [[Tomografia Computadorizada|tomografia-computadorizada]]. 

### Controle de Qualidade e Dosimetria
Em protocolos de controle de qualidade, a precisão da colimação pré-paciente é avaliada por meio de testes com filmes radiocrômicos ou câmaras de ionização tipo lápis (pencil ionization chambers). Discrepâncias entre a espessura de colimação nominal ($W_z$) e a medida causam erros severos no cálculo dos índices dosimétricos padronizados, como o [[Métricas de Dose em TC|ctdi]] ($CTDI_{w}$ e $CTDI_{vol}$) e a Dose Eficaz. Se o feixe real for mais estreito que o nominal (situação comum em larguras de corte muito finas, abaixo de $1 \, \text{mm}$), a dose medida por centímetro de varredura aumenta devido à superposição de perfis de dose (efeito de cauda de dispersão), fenômeno conhecido como *overbeaming* ou eficiência de dose geométrica reduzida.

### Otimização da Imagem e Redução de Artefatos
Uma colimação inadequada compromete a fidelidade quantitativa das unidades Hounsfield (HU). A ausência de uma colimação pós-paciente eficiente permite a entrada de radiação espalhada ($I_{\text{scatter}}$) no detector\, degradando o sinal primário ($I_{\text{primary}}$):

$$
\text{Relação Sinal-Ruído}_{\text{efetiva}} \propto \frac{I_{\text{primary}}}{\sqrt{I_{\text{primary}} + I_{\text{scatter}}}}
$$

Essa contaminação resulta em perdas de contraste em tecidos moles e gera artefatos de feixe endurecido e faixas (*cupping artifacts*) em regiões de alta atenuação, como a base do crânio e os ombros.

### Interação com Algoritmos de Reconstrução
Com o advento da [[Reconstrução Iterativa|reconstrucao-iterativa]] (IR) e de algoritmos baseados em [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]] (DLR), a modelagem matemática exata da geometria de colimação e da penumbra do feixe tornou-se mandatória. Os projetores e retroprojetores analíticos avançados (como a retroprojeção filtrada exata para geometria cone-beam) utilizam matrizes de sensibilidade espacial derivadas das funções de transferência de colimação para compensar a divergência do feixe cone-beam, evitando artefatos de cone (*cone-beam artifacts*) em varreduras com grande número de canais em $z$.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[Métricas de Dose em TC|ctdi]]
- [[Reconstrução Iterativa|reconstrucao-iterativa]]
- [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem]]
- [[Radioproteção|radioprotecao]]
- [[Artefatos em TC|artefatos-em-tc]]