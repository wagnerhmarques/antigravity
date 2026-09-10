---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, deteccao-de-raios-x, metrologia, relacao-sinal-ruido]
data: 2026-08-25
---

# Detective Quantum Efficiency (DQE)

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A *Detective Quantum Efficiency* (DQE), ou Eficiência Quântica Detetiva, é a métrica de desempenho físico-metrológico mais abrangente e rigorosa utilizada para caracterizar sistemas de imagem baseados em raios-X, incluindo os detectores de estado sólido (geralmente baseados em cintiladores acoplados a fotodiodos de silício ou detectores de conversão direta como o telureto de cádmio - CdTe) empregados em Tomografia Computadorizada (TC).

Conceitualmente, a DQE quantifica a eficiência com que um sistema de detecção converte o fluxo de fótons incidentes de raios-X em um sinal de imagem útil (digital ou analógico), mantendo ou degradando o mínimo possível a Relação Sinal-Ruído (SNR - *Signal-to-Noise Ratio*). Em termos puramente físicos, a DQE avalia a degradação da SNR imposta pelo detector em comparação a um detector ideal teoreticamente perfeito, o qual operaria sob o regime estocástico puro da estatística de Poisson (limite quântico de ruído).

Historicamente derivada da teoria de sistemas lineares aplicada à óptica e à engenharia de comunicação, a DQE engloba dois fenômenos fundamentais que ocorrem durante o processo de detecção:
1. **Eficiência de Absorção Quântica ($\eta$):** A probabilidade de um fóton X incidente interagir fisicamente com o material detector (por efeito fotoelétrico ou espalhamento Compton).
2. **Propagação e Amplificação de Ruído Estocástico (Fator de Amplificação ou Fator de Swank, $I$):** A variabilidade inerente na quantidade de portadores de carga ou fótons de luz visível gerados por fóton X absorvido, além dos efeitos de granulosidade espacial induzidos pela estrutura do detector (por exemplo, o espalhamento óptico em cintiladores granulares ou a diafonia eletrostática - *crosstalk* - entre elementos adjacentes em matrizes semicondutoras).

Um sistema com $\text{DQE} = 1$ (ou 100%) seria um detector ideal capaz de detectar 100% dos fótons incidentes sem introduzir nenhum ruído adicional. Na prática dos sistemas modernos de TC multislice e de contagem de fótons (*Photon-Counting Computed Tomography* - PCCT), a DQE é sempre inferior à unidade e varia fortemente em função da frequência espacial ($
u$), da energia do feixe de raios-X (espectro polienergético), da taxa de fluência de fótons (efeitos de empilhamento de pulsos ou saturação) e da dose de radiação aplicada.

---

## 2. Formulação Matemática e Propriedades

A formulação matemática da DQE baseia-se na teoria da transferência linear de sistemas estocásticos e na análise de Fourier. A DQE é expressa como uma função da frequência espacial bidimensional ($
u_x, 
u_y$) ou unidimensional ($
u$):

$$
\text{DQE}(
u) = \frac{\text{SNR}_{\text{out}}^2(
u)}{\text{SNR}_{\text{in}}^2(
u)}
$$

Onde:
- $\text{SNR}_{\text{in}}(
u)$ é a relação sinal-ruído do feixe de fótons de raios-X incidente no plano do detector.
- $\text{SNR}_{\text{out}}(
u)$ é a relação sinal-ruído do sinal elétrico digitalizado ou da imagem gerada pelo sistema.

Considerando a estatística Poissoniana do feixe de raios-X incidente, a $\text{SNR}_{\text{in}}^2$ pode ser expressa em função da fluência de fótons incidentes por unidade de área ($\Phi$, em $\text{mm}^{-2}$):

$$
\text{SNR}_{\text{in}}^2 = \Phi
$$

Para o lado da saída, a $\text{SNR}_{\text{out}}^2(
u)$é calculada utilizando a função de transferência de modulação do sistema ($\text{MTF}(
u)$) e o espectro de potência de ruído digital ($\text{NPS}(
u)$ - *Noise Power Spectrum*):

$$
\text{SNR}_{\text{out}}^2(
u) = \frac{\bar{g}^2 \cdot \Phi \cdot \text{MTF}^2(
u)}{\text{NPS}(
u)}
$$

Substituindo estas expressões na equação fundamental, obtém-se a formulação operacional padrão da DQE para sistemas de imagem médica (conforme os protocolos da norma IEC 62220-1):

$$
\text{DQE}(
u) = \frac{\bar{g}^2 \cdot \text{MTF}^2(
u)}{\Phi \cdot \text{NPS}(
u)}
$$

Onde:
- $\bar{g}$ representa o ganho médio de conversão do sistema (relação entre os números digitais ou carga elétrica de saída e o número de fótons X incidentes).
- $\text{MTF}(
u)$ é a Função de Transferência de Modulação, que descreve a resposta espacial do detector a frequências espaciais crescentes.
- $\text{NPS}(
u)$ é o Espectro de Potência de Ruído, que quantifica a textura e a variância espacial do ruído na imagem.

### Propriedades Matemáticas Relevantes:
1. **Comportamento em Frequência Zero ($
u \to 0$):** 
   No limite de baixa frequência espacial ($
u = 0$), a$\text{DQE}(0)$aproxima-se do produto entre a eficiência de absorção quântica ($\eta$) e o fator de Swank ($I$):
   
$$
\text{DQE}(0) \approx \eta \cdot I
$$

2. **Queda com a Frequência Espacial:** 
   À medida que a frequência espacial ($
u$) aumenta, a$\text{DQE}(
u)$decresce monotonicamente. Isso ocorre porque a$\text{MTF}^2(
u)$decai mais rapidamente do que o$\text{NPS}(
u)$ (ou devido ao aumento relativo do ruído de alta frequência associado à granulosidade do detector e à eletrônica de leitura).
3. **Invariância e Linearidade:** 
   A validade rigorosa das equações acima pressupõe que o sistema seja linear e estacionário no espaço (ou fracamente não-linear, exigindo o uso de Gained-MTF e NPS generalizados).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Na Tomografia Computadorizada contemporânea, a DQE desempenha um papel central no projeto de hardware, no controle de qualidade regulatório e nas estratégias de otimização da dose de radiação ionizante.

### 1. Otimização da Dose e Gerenciamento de Risco
Como a dose absorvida pelo paciente ($D$) é diretamente proporcional à fluência de fótons incidentes ($\Phi$), maximizar a DQE do sistema de detecção significa que uma maior proporção de fótons úteis é convertida em informação diagnóstica. Em termos práticos, detectores com maior DQE permitem a aquisição de imagens com a mesma SNR utilizando menores correntes no tubo de raios-X (mAs), viabilizando protocolos de TC de baixa dose cruciais para exames pediátricos, exames cardiorrespiratórios e rastreamentos pulmonares de rotina.

### 2. Controle de Qualidade e Homologação de Scanners
A medição da DQE serve como o teste definitivo de desempenho para novos arranjos de detectores em TC. Enquanto parâmetros isolados como a eficiências de absorção ou a resolução espacial geométrica contam apenas parte da história, a DQE revela defeitos ocultos de fabricação, como diafonia cruzada (*crosstalk*) excessiva entre canais adjacentes, falhas no ganho dos fotodiodos ou degradação do material cintilador ao longo do tempo de uso devido ao dano por radiação.

### 3. Impacto nas Tecnologias Avançadas de Reconstrução
- **Tomografia Computadorizada de Contagem de Fótons (PCCT):** Os detectores de contagem de fótons baseados em semicondutores de conversão direta (como CdTe ou CdZnTe) eliminam o ruído eletrônico térmico associado aos detectores integradores tradicionais e evitam a ponderação inadequada de baixa energia. Isso resulta em curvas de DQE significativamente superiores, especialmente em frequências espaciais médias e altas, além de preservar a DQE mesmo em regimes de dose extremamente baixos.
- **Reconstrução Baseada em Inteligência Artificial (DLR - *Deep Learning Reconstruction*):** Algoritmos de DLR modernos são treinados para mitigar o ruído e artefatos em imagens de TC de baixa dose. No entanto, o limite fundamental da informação recuperável é imposto pela DQE do detector físico. Se a DQE for deficiente em certas bandas de frequência espacial, a perda de informação quântica é irreversível, tornando essencial que o projeto do hardware otimize a DQE antes que o pós-processamento algorítmico seja aplicado.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada]]
- [[Funcao de Transferencia de Modulação (MTF)]]
- [[Noise Power Spectrum|Espectro de Potencia de Ruido (NPS)]]
- [[Photon-Counting Computed Tomography (PCCT)]]
- [[Relacao Sinal-Ruido (SNR)]]
- [[Controle de Qualidade em Radiologia Diagnostica]]
- [[Dosimetria em Radiologia]]
- [[Reconstrucao Iterativa e Deep Learning em TC]]