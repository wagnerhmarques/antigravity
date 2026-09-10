---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radioprotecao, interacao-da-radiacao, dosimetria, metrologia]
data: 2026-08-25
---

# fisica-da-radiacao

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Física da Radiação** abrange o estudo detalhado da natureza das radiações ionizantes e não-ionizantes, seus mecanismos fundamentais de interação com a matéria biológica e inorgânica, e os princípios metrológicos que regem a sua medição, quantificação e controle. No contexto específico da Física Médica e da Tomografia Computadorizada (TC), o foco recai primordialmente sobre os raios X — radiação eletromagnética de alta energia produzida pela desaceleração abrupta de elétrons (radiação de frenagem ou *Bremsstrahlung*) e por transições eletrônicas em camadas internas (raios X característicos) no interior de um tubo de raios X.

Metrologicamente, a caracterização da radiação ionizante exige grandezas rigorosas fundamentadas pelo *International Commission on Radiation Units and Measurements* (ICRU) e pelo *International Bureau of Weights and Measures* (BIPM). As grandezas fundamentais incluem:
- **Fluência ($\Phi$):** Número de partículas incidentes por unidade de área transversal.
- **Kerma ($K$, *Kinetic Energy Released in Matter*):** A soma das energias cinéticas iniciais de todas as partículas carregadas liberadas por partículas não-carregadas por unidade de massa em um meio específico (medido em Gray, Gy).
- **Dose Absorvida ($D$):** A energia média depositada pela radiação ionizante por unidade de massa em um elemento de volume de matéria ($D = \frac{d\bar{E}}{dm}$), sendo a grandeza central para a avaliação de efeitos biológicos determinísticos e estocásticos.

A interação dos fótons de raios X com os átomos do meio ocorre de maneira probabilística, sendo dominada na faixa de energia diagnóstica (tipicamente entre 20 keV e 140 keV) por dois fenômenos principais:
1. **Efeito Fotoelétrico:** O fóton incidente transfere toda a sua energia para um elétron ligado (geralmente das camadas K ou L), que é ejectado como um fotoelétron. A probabilidade de ocorrência varia com o número atômico ($Z$) do meio e inversamente com a energia do fóton ($E$), aproximando-se de $\propto Z^3 / E^3$. Este efeito é o principal responsável pelo contraste tecidual em imagens de tomografia, mas contribui significativamente para a dose local absorvida pelo paciente.
2. **Espalhamento Compton (Inelástico):** O fóton interage com um elétron fracamente ligado (livre, em aproximação), transferindo parte de sua energia para o elétron de recuo e sendo espalhado em um ângulo $\theta$. A energia do fóton espalhado é independente do número atômico e depende estritamente do ângulo de espalhamento. Na Tomografia Computadorizada, fótons espalhados que atingem os detectores sem correlação espacial geram artefatos de degradação de imagem, como sombreamento e perda de contraste.

O espalhamento coerente (Rayleigh) e a produção de pares (em energias acima de 1,022 MeV) possuem relevância menor ou nula na faixa de energia diagnóstica padrão, embora a correção para espalhamento seja computacionalmente crítica em algoritmos avançados de reconstrução.

---

## 2. Formulação Matemática e Propriedades

A atenuação de um feixe de fótons estritamente monoenergético ao atravessar um meio material homogêneo é descrita pela **Lei de Atenuação de Beer-Lambert**:

$$
I(x) = I_0 \, e^{-\mu x}
$$

Onde:
- $I_0$ é a intensidade (ou fluência de energia) incidente.
- $I(x)$ é a intensidade após atravessar uma espessura $x$ do material.
- $\mu$ é o **coeficiente de atenuação linear** ($\text{cm}^{-1}$), que expressa a probabilidade de interação por unidade de comprimento percorrido.

O coeficiente de atenuação linear depende da densidade física ($\rho$) do meio. Para remover essa dependência e normalizar o comportamento atômico puro, utiliza-se o **coeficiente de atenuação mássica** ($\mu_m$), definido como:

$$
\mu_m = \frac{\mu}{\rho}
$$

Para compostos e misturas complexas, como os tecidos biológicos, o coeficiente de atenuação efetivo é calculado pela regra aditiva dos elementos constituintes ponderados por suas frações mássicas ($w_i$):

$$
\left(\frac{\mu}{\rho}\right)_{\text{tecido}} = \sum_{i} w_i \left(\frac{\mu}{\rho}\right)_i
$$

No contexto de feixes **policromáticos** gerados por tubos de raios X clínicos, a atenuação não segue uma exponencial simples, pois os fótons de menor energia (mais facilmente absorvidos ou "soft x-rays") são attenuados preferencialmente nas camadas iniciais do material, endurecendo o feixe ($HVL$ — *Half-Value Layer* crescente). A intensidade transmitida para um feixe policromático é modelada por uma integral sobre o espectro de energia $\Phi(E)$:

$$
I(x) = \int_{0}^{E_{\max}} \Phi_0(E) \, e^{-\mu(E)x} \, dE
$$

Onde $\mu(E)$ é o coeficiente de atenuação dependente da energia do fóton $E$.

Para a quantificação dos coeficientes em unidades de tomografia, introduz-se a escala de **Número Hounsfield ($\text{HU}$)**, normalizada com base no coeficiente de atenuação da água ($\mu_{\text{água}}$) e do ar ($\mu_{\text{ar}}$):

$$
\text{HU} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Dada a calibração padrão, $\mu_{\text{ar}} \approx 0$, simplificando a métrica para:

$$
\text{HU} = 1000 \times \left( \frac{\mu}{\mu_{\text{água}}} - 1 \right)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão profunda da física da radiação é o alicerce para o projeto, controle de qualidade e otimização de sistemas modernos de Tomografia Computadorizada. As ramificações práticas incluem:

- **Filtragem do Feixe e Endurecimento (*Beam Hardening*):** A natureza policromática do feixe gera artefatos de endurecimento de feixe (faixas escuras e bandas brilhantes, especialmente em regiões anatômicas densas como a base do crânio ou pelve). Modelos físicos da atenuação espectral permitem o desenvolvimento de algoritmos de correção baseados em pré-processamento de projeções ou abordagens iterativas baseadas em decomposição material.
- **Gestão de Dose e Dosimetria:** Grandezas como o **CTDI** (*Computed Tomography Dose Index*), o **$CTDI_{w}$** (ponderado) e o **$CTDI_{vol}$** (volumétrico), além do **DLP** (*Dose-Length Product*), são derivadas diretamente da integração espacial e temporal da taxa de kerma no ar medida com câmaras de ionização cilíndricas (tipo *pencil chamber*) em fantasmas (*phantoms*) de acrílico padronizados ($16\,\text{cm}$ para crânio e $32\,\text{cm}$ para corpo).
- **Reconstrução e Modelagem de Sistemas (FBP vs. DLR):** Algoritmos de reconstrução analítica como a Retroprojeção Filtrada (FBP) assumem idealizações físicas que podem ser violadas (ruído quântico governado por estatística de Poisson, ruído eletrônico gaussiano). Métodos modernos de Reconstrução Iterativa (IR) e Reconstrução Baseada em Aprendizado Profundo (*Deep Learning Reconstruction - DLR*) incorporam modelos estatísticos avançados da física do fóton e da formação da imagem para suprimir ruído sem sacrificar a resolutibilidade espacial, permitindo reduções drásticas na dose administrada ao paciente sem perda de diagnosticabilidade.
- **TC de Dupla Energia (*Dual-Energy CT - DECT*):** Aproveitando a dependência energética distinta do efeito fotoelétrico e do espalhamento Compton (separação de curvas de atenuação em diferentes energias), a física da radiação viabiliza a decomposição material quantitativa, permitindo a diferenciação de iodo, cálcio, ácido úrico e a geração de mapas virtuais de monoenergização e imagens de número atômico efetivo ($Z_{\text{eff}}$).

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|tomografia-computadorizada]]
- [[interacao-da-radiacao-com-a-materia]]
- [[Dosimetria em TC|dosimetria-em-tc]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
- [[Otimização de Dose|otimizacao-de-dose]]
- [[Artefatos em TC|artefatos-em-tc]]
- [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]