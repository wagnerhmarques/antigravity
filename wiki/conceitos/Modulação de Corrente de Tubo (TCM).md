---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, otimização-de-dose\, dosimetria, processamento-de-sinal]
data: 2026-08-25
---

# tube-current-modulation

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Modulação de Corrente do Tubo** (*Tube-Current Modulation* - TCM) é uma técnica avançada de otimização da dose de radiação em Tomografia Computadorizada (TC) na qual a corrente do tubo de raios X (medida em miliamperes, $mA$) é dinamicamente variada durante a rotação do gantry e ao longo do eixo longitudinal ($z$) do paciente. O objetivo fundamental da TCM é adaptar a emissão de fótons à atenuação anatômica específica do indivíduo, mantendo a qualidade de imagem constante — tipicamente avaliada pela manUTENção do desvio padrão do ruído ou pelo ruído perceptual equivalente — e reduzindo a dose integral absorvida.

Anatomicamente, o corpo humano não é um cilindro uniforme; regiões como os ombros, a pelve e a coluna vertebral apresentam coeficientes de atenuação linear ($\mu$) e espessuras muito superiores às regiões do crânio, pescoço ou abdome delgado. Em protocolos tradicionais com corrente fixa ($mA$ constante), a aquisição é dimensionada para a região de maior atenuação para evitar artefatos quânticos severos (*quantum noise*). Consequentemente, as regiões menos espessas recebem uma irradiação excessiva. A TCM corrige essa ineficiência ao modular a intensidade do feixe em tempo real com base nos topogramas de planejamento (imagens *scout* ou *surview* nas incidências ântero-posterior e lateral) e/ou nos dados de realimentação instantânea do detector.

Metrologicamente, a implementação da TCM requer a sincronização precisa entre a rotação mecânica do sistema de raios X, a leitura do sinal do detector e o circuito gerador de alta tensão, garantindo que a modulação espacial corresponda exatamente à geometria de projeção instantânea.

---

## 2. Formulação Matemática e Propriedades

Para compreender a formulação matemática da TCM, parte-se da equação de atenuação de fótons de raios X (Lei de Beer-Lambert) para um feixe policromático:

$$
I(l) = I_0 \int_{0}^{E_{\max}} Φ(E) \exp \left( -\int_L \mu(x, y, E) \, dl \right) dE
$$

Onde:
- $I_0$ é a intensidade incidente proporcional ao produto da corrente do tubo pelo tempo de exposição ($mAs$).
- $Φ(E)$ é o espectro de energia dos fótons.
- $\mu(x, y, E)$ é o coeficiente de atenuação linear dependente da posição espacial $(x,y)$ e da energia $E$.
- $L$ é o trajeto do raio através do paciente.

O ruído quântico em uma projeção é governado pelas estatísticas de Poisson do número de fótons detectados $N$. A variância do ruído na imagem reconstruída por Retroprojeção Filtrada (*Filtered Backprojection* - FBP) é inversamente proporcional ao número total de fótons incidentes. Para manter a variância do ruído ($\sigma^2$) constante em diferentes ângulos de projeção $\theta$, a corrente do tubo $mA(\theta)$ deve ser ajustada em função da atenuação integral ao longo do perfil de projeção:

$$
mA(\theta) \propto \exp \left( \int_{L(\theta)} \mu(x, y) \, dl \right)
$$

As estratégias modernas de TCM dividem-se em três eixos principais:

### A. Modulação Longitudinal ($z$-DOM ou *Z-axis Dose Modulation*)
A intensidade da corrente é variada ao longo do eixo longitudinal do paciente em função do perfil de espessura determinado pelos topogramas ortogonais. A corrente média para uma dada posição $z$ é expressa como:

$$
mA(z) = mA_{base} \cdot f_{z}(z)
$$

Onde $mA_{base}$ é o parâmetro de referência definido pelo operador (frequentemente expresso como *Image Quality Reference mA* - IQRM) e $f_{z}(z)$ é o fator de correção longitudinal derivado da área de secção transversa ou do diâmetro efetivo $d_{ef}(z)$:

$$
d_{ef}(z) = \sqrt{D_{AP}(z) \cdot \vphantom{D_{AP}(z)} D_{LAT}(z)}
$$

### B. Modulação Angular ou Rotacional ($angular-DOM$ ou *Angular Dose Modulation*)
A corrente é modulada a cada grau de rotação do gantry para compensar a elipticidade do corpo humano (onde a atenuação ântero-posterior é tipicamente menor que a lateral):

$$
mA(\theta) = mA_{base} \cdot f_{\theta}(\theta)
$$

O perfil angular visa equilibrar o ruído estatístico entre as projeções laterais (que exigem maior $mA$) e as projeções ântero-posterior/póstero-anterior (que exigem menor $mA$).

### C. Modulação Combinada (Tridimensional)
Integra as modulações longitudinal e angular simultaneamente, resultando em uma matriz de corrente tridimensional otimizada:

$$
mA(z, \theta) = mA_{base} \cdot f_{z}(z) \cdot f_{\theta}(\theta, z)
$$

A dose efetiva total $E$ resultante da aplicação da TCM pode ser estimada pela integração das doses absorvidas nos órgãos ponderadas pelos respectivos coeficientes de sensibilidade tecidual $w_T$:

$$
E = \sum_T w_T \left( \frac{1}{M_T} \int_{M_T} D(x, y, z) \, dm \right)
$$

Onde $D(x, y, z)$ é a distribuição de dose espacial modulada pela variação de $mA(z, \theta)$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A implementação da TCM revolucionou a prática clínica da dosimetria em TC, consolidando-se como um pilar essencial do princípio **ALARA** (*As Low As Reasonably Achievable*). Suas principais aplicações e impactos na otimização incluem:

* **Redução da Dose Coletiva:** Permite reduções de dose que variam de 20% a 60% dependendo da região anatômica escaneada (com maiores ganhos em pelve, tórax e coluna lombar), sem perda de diagnosticabilidade.
* **Padronização da Qualidade de Imagem:** Garante que o ruído estatístico permaneça homogêneo em pacientes com biótipos variados (desde pacientes pediátricos até pacientes obesos), evitando tanto imagens degradadas por ruído excessivo quanto exposições desnecessárias.
* **Interação com Algoritmos de Reconstrução:** A TCM altera a distribuição espacial do ruído nas projeções brutas (*sinograma*). Enquanto na FBP o ruído modulado pode gerar artefatos visuais de riscas (*streaking artifacts* se o limite inferior de $mA$ for excessivamente agressivo), os algoritmos de **Reconstrução Iterativa (IR)** e **Reconstrução Baseada em Aprendizado Profundo (DLR)** lidam de forma excelente com o ruído não uniforme, permitindo reduções adicionais de dose combinadas com a TCM.
* **Desafios Metrológicos e CQ:** O controle de qualidade da TCM exige testes específicos para verificar se o sistema de varredura ajusta corretamente a corrente de acordo com simulações de fantomas antropomórficos ou de polietileno de diâmetros variáveis, avaliando a precisão do perfil de $mA$ reportado no arquivo DICOM *Radiation Dose Structured Report* (RDSR).

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|computed-tomography]]
* [[Radiation Dosimetry|radiation-dosimetry]]
* [[Retroprojeção Filtrada (FBP)|filtered-backprojection]]
* [[Reconstrução Iterativa|iterative-reconstruction]]
* [[Deep Learning Reconstruction (DLR)|deep-learning-reconstruction]]
* [[Image Quality Metrics|image-quality-metrics]]
* [[Ruído Quântico|quantum-noise]]
* [[alara-principle]]