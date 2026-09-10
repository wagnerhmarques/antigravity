---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, raio-x, radiologia-diagnóstica, interacao-radiacao-materia, dosimetria]
data: 2026-08-25
---

# Física do Raio-X

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O termo **Raio-X** designa a radiação eletromagnética ionizante de alta frequência e comprimento de onda curto, situando-se no espectro eletromagnético entre o ultravioleta extremo e os raios gama. Em termos metrológicos e físicos, os raios-X compreendem fótons com comprimentos de onda tipicamente variando de $0,01$ a $10\,\text{nm}$ (o que corresponde a energias de fótons de aproximadamente $0,1\,\text{keV}$ a $100\,\text{keV}$ na prática diagnóstica). A distinção fundamental entre raios-X e raios gama não reside na natureza física do fóton em si, mas sim em sua **origem**: enquanto os raios gama são emitidos a partir de transições nucleares (desexcitação do núcleo atômico), os raios-X são gerados por processos atômicos extranucleares — especificamente, por aceleração ou desaceleração de elétrons (gerando radiação de frenagem ou *Bremsstrahlung*) e por transições eletrônicas entre camadas internas de átomos pesados (gerando raios-X característicos).

Em um tubo de raios-X convencional, o processo de geração requer três elementos essenciais:
1. Uma fonte de elétrons (filamento de tungstênio aquecido por efeito termoiónico).
2. Um meio de aceleração dos elétrons (uma diferença de potencial elétrico de alta tensão, $kVp$, aplicada entre o cátodo e o ânodo).
3. Um alvo metálico de alto número atômico ($Z$, tipicamente tungstênio, $Z=74$, ou ligas de rénio-tungstênio), onde ocorre a conversão da energia cinética dos elétrons incidentes em radiação eletromagnética e calor.

Quando os elétrons altamente acelerados colidem com o ânodo, duas interações atômicas principais dão origem ao feixe policromático de raios-X:

* **Radiação de Frenagem (*Bremsstrahlung*):** Ocorre quando um elétron incidente passa próximo ao núcleo atômico do material do ânodo. Devido ao campo eletromagnético coulombiano positivo do núcleo, o elétron é desviado e desacelerado bruscamente. Essa perda de energia cinética $\Delta E$ é convertida diretamente na emissão de um fóton de raio-X cuja energia pode assumir qualquer valor contínuo desde zero até a energia máxima cinética do elétron incidente ($E_{\max} = e \cdot kVp$). O espectro resultante do *Bremsstrahlung* é contínuo.
* **Raios-X Característicos:** Ocorrem quando um elétron incidente colide com um elétron firmemente ligado às camadas internas do átomo do alvo (camadas $K$ ou $L$), ejectando-o e deixando uma lacuna eletrônica. Um elétron de uma camada externa de maior energia desce para preencher essa lacuna. A diferença de energia entre as camadas é emitida sob a forma de um fóton de raio-X com uma energia estritamente definida, correspondente à estrutura eletrônica específica do elemento alvo. O espectro resultante apresenta linhas discretas sobrepostas ao fundo contínuo de *Bremsstrahlung*.

Metrologicamente, a caracterização do feixe de raios-X envolve grandezas fundamentais como a **Fluência de Fótons**, a **Taxa de Kerma no Ar** ($\text{Gy/s}$), a **Camada Sem-Redução** (CSR ou *Half-Value Layer* - $\text{HVL}$), que quantifica a qualidade (dureza/penetração) do feixe, e a **Tensão de Pico** ($kVp$).

---

## 2. Formulação Matemática e Propriedades (se aplicável)

A distribuição espectral da intensidade da radiação de *Bremsstrahlung* em função do comprimento de onda ($\lambda$) é descrita empiricamente pela **Lei de Duane-Hunt**, que define o limite de comprimento de onda mínimo ($\lambda_{\min}$) associado à máxima energia do fóton gerado por elétrons acelerados por uma voltagem $V$:

$$
\lambda_{\min} = \frac{hc}{e \cdot V} \approx \frac{1,24}{V_{\text{(kV)}}}, \quad [\text{nm}]
$$

Onde:
* $h$ é a constante de Planck ($6,626 \times 10^{-34}\,\text{J}\cdot\text{s}$);
* $c$ é a velocidade da luz no vácuo ($3 \times 10^8\,\text{m/s}$);
* $e$ é a carga elementar do elétron ($1,602 \times 10^{-19}\,\text{C}$);
* $V$ é a tensão aplicada ao tubo (em quilovolts, $\text{kVp}$).

A intensidade total ($I$) da radiação de *Bremsstrahlung* emitida por um tubo de raios-X é proporcional ao número atômico do alvo ($Z$), à corrente do tubo ($I_{\text{tube}}$) e ao quadrado da tensão aplicada ($V$):

$$
I \propto Z \cdot I_{\text{tube}} \cdot V^2
$$

### Atenuação da Radiação na Matéria

Ao interagir com a matéria (tecidos biológicos ou filtros de atenoação), a intensidade de um feixe de raios-X monoenergético decresce exponencialmente de acordo com a **Lei de Beer-Lambert**:

$$
I(x) = I_0 \, e^{-\mu x}
$$

Onde:
* $I_0$ é a intensidade do feixe incidente;
* $I(x)$ é a intensidade após atravessar uma espessura $x$ do material;
* $\mu$ é o **coeficiente de atenuação linear** ($\text{cm}^{-1}$), que depende da energia do fóton ($E$) e do número atômico efetivo ($Z_{eff}$) e da densidade ($\rho$) do meio.

Para feixes policromáticos (como os gerados em tubos clínicos de raios-X), a atenuação não é estritamente exponencial, sendo descrita de forma mais geral pela integração sobre o espectro energético $I(E)$:

$$
I(x) = \int_{0}^{E_{\max}} I_0(E) \, e^{-\mu(E)x} \, dE
$$

O **coeficiente de atenuação mássica** ($\mu/\rho$) é frequentemente utilizado para remover a dependência da densidade física do meio, permitindo expressar a probabilidade de interação por unidade de massa por área:

$$
\left( \frac{\mu}{\rho} \right) = \left( \frac{\mu_{\text{fotoelétrico}}}{\rho} \right) + \left( \frac{\mu_{\text{Compton}}}{\rho} \right) + \left( \frac{\mu_{\text{par}}}{\rho} \right)
$$

No intervalo de energias típicas da radiologia diagnóstica e da Tomografia Computadorizada ($30\,\text{keV}$ a $140\,\text{keV}$), os mecanismos dominantes de interação são o **Efeito Fotoelétrico** (proporcional a $\approx Z^3 / E^3$) e o **Espalhamento Compton** (quase independente de $Z$, dependente da densidade eletrônica volumétrica).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão rigorosa da física do raio-X é o alicerce operacional e metodológico da **Tomografia Computadorizada (TC)** moderna:

* **Modulação de Corrente e Tensão (mA/kVp):** O controle preciso da emissão de raios-X permite técnicas avançadas de otimização de dose, como a modulação automática de corrente (*Automatic Tube Current Modulation* - ATCM) no eixo angular ($x, y$) e longitudinal ($z$), adaptando a fluência de fótons à atenuação variável do paciente para manter o ruído da imagem constante.
* **Filtragem do Feixe e *Beam Hardening*:** Como o feixe gerado é policromático, os fótons de menor energia são preferencialmente absorvidos ao atravessar as estruturas mais profundas do corpo (fenômeno de endurecimento do feixe ou *beam hardening*). Isso gera artefatos de imagem (bandas escuras ou estrias) e imprecisões nos valores de Unidades Hounsfield ($\text{HU}$). Algoritmos de correção de endurecimento de feixe (*Beam Hardening Correction* - BHC) no espaço de projeção ou pós-processamento dependem diretamente da modelagem matemática da física de atenuação espectral.
* **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** A modelagem exata do sistema físico de aquisição — incluindo a geometria do feixe cônico (*cone-beam*), a distribuição estatística dos fótons (ruído quântico regido pela estatística de Poisson) e a resposta espacial do detector — é essencial para os algoritmos de **Reconstrução Iterativa (IR)** e algoritmos baseados em **Inteligência Artificial (DLR)**, permitindo reduzir drasticamente a dose de radiação mantendo a diagnósticabilidade.
* **Dosimetria e Controle de Qualidade (QC):** Métodos metrológicos rigorosos medem parâmetros como o índice de dose em tomografia computadorizada ($CTDI_{w}$, $CTDI_{vol}$) e o produto dose-comprimento ($DLP$), que quantificam o risco estocástico associado à exposição aos raios-X.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Efeito Fotoelétrico]]
* [[Espalhamento Compton]]
* [[Atenuação da Radiação]]
* [[Unidades Hounsfield|Unidades Hounsfield]]
* [[Reconstrução de Imagem]]
* [[Filtro de retroprojeção (FBP)]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Inteligência Artificial em Imagem Médica (DLR)]]
* [[Controle de Qualidade em TC]]
* [[Dosimetria em Radiologia]]