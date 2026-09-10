---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, artefatos, qualidade-de-imagem, reconstrucao-de-imagem]
data: 2026-08-25
---

# Efeito de Volume Parcial

## 1. Definição Conceitual e Fundamentação Física / Metrológica

O **Efeito de Volume Parcial (EVP)** é um artefato físico inerente aos sistemas de imagem digital volumétrica, com relevância crítica em [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]] e [[Medicina Nuclear]]. O fenômeno ocorre quando um único elemento de volume fundamental do espaço digital — o voxel — engloba simultaneamente tecidos ou estruturas anatômicas com coeficientes de atenuação linear (em TC) ou concentrações de radioindicador (em PET/SPECT) drasticamente distintos.

Na formação da imagem por TC, o tubo de raios X e os detectores digitalizam o espaço através de feixes colimados. Cada voxel reconstruído representa a média matemática dos sinais de raios X atenuados ao longo de todo o seu volume tridimensional. Consequentemente, se uma interface tecidual (por exemplo, a transição entre o parênquima pulmonar com ar e a parede de um vaso sanguíneo, ou a interface osso-tecido mole) cruza o interior de um voxel, a intensidade atribuída a esse voxel será um valor intermediário, ponderado pelas frações volumétricas de cada componente.

Metrologicamente, o EVP induz a dois problemas principais:
1. **Erro de Quantificação (Bias de Intensidade):** A atenuação real de uma estrutura pequena ou periférica é subestimada ou superestimada, pois é diluída pelo tecido circundante.
2. **Degradação de Bordas (Borramento Espacial):** As interfaces nítidas entre estruturas anatômicas perdem definição, simulando transições graduais onde existem limites abruptos.

O EVP manifesta-se em duas dimensões principais em TC: no plano de corte (afetado pelo tamanho da matriz de reconstrução e pela função de interpolação do pixel) e na direção do eixo z (eixo longitudinal de deslocamento da mesa), onde a espessura do corte (*slice thickness*) e o perfil de sensibilidade do corte (*slice sensitivity profile - SSP*) determinam a magnitude do artefato.

---

## 2. Formulação Matemática e Propriedades

Para modelar o Efeito de Volume Parcial matematicamente, considere um voxel $V$ no espaço tridimensional. O valor de número de TC (expresso em unidades Hounsfield, $\text{HU}$) ou o coeficiente de atenuação linear efetivo $\mu_{\text{ef}}$, atribuído a este voxel, é a média espacial do coeficiente de atenuação $\mu(x, y, z)$ ponderada pela função de resposta do sistema de imagem (representada pelo ponto de dispersão pontual, ou *Point Spread Function - PSF*):

$$
\mu_{\text{ef}} = \frac{\iiint_V \mu(x, y, z) \cdot \text{PSF}(x - x_0, y - y_0, z - z_0) \, dx\, dy\, dz}{\iiint_V \text{PSF}(x - x_0, y - y_0, z - z_0) \, dx\, dy\, dz}
$$

Em uma abordagem simplificada de voxel ideal (assumindo uma função de amostragem retangular sem sobreposição e desconsiderando o desfoque da PSF por ora), o voxel contém $N$ tipos diferentes de tecidos perfeitamente homogêneos, onde o $i$-ésimo tecido possui um coeficiente de atenuação $\mu_i$ e ocupa uma fração volumétrica $f_i$ do voxel total. A conservação do volume exige que:

$$
\sum_{i=1}^{N} f_i = 1 \quad \text{onde} \quad 0 \le f_i \le 1
$$

O coeficiente de atenuação médio medido $\mu_{\text{med}}$ para este voxel é dado por:

$$
\mu_{\text{med}} = \sum_{i=1}^{N} f_i \cdot \mu_i
$$

Convertendo para a escala Hounsfield ($\text{HU}$), onde $\mu_{\text{água}}$ é o coeficiente de atenuação da água e $\mu_{\text{ar}}$ o do ar (tipicamente 0):

$$
\text{HU}_{\text{med}} = 1000 \times \frac{\mu_{\text{med}} - \mu_{\text{água}}}{\mu_{\text{água}}}
$$

Substituindo a média ponderada:

$$
\text{HU}_{\text{med}} = \sum_{i=1}^{N} f_i \cdot \text{HU}_i
$$

### Propriedades Matemáticas do EVP:
* **Linearidade de Média:** O valor medido é estritamente uma combinação convexa dos valores dos componentes individuais contidos no voxel.
* **Perda de Amplitude em Pequenas Estruturas:** Seja uma estrutura esférica de raio $r$ e coeficiente $\mu_{\text{objeto}}$ imersa em um fundo $\mu_{\text{fundo}}$. Se o diâmetro da estrutura for menor ou da mesma ordem de grandeza que a largura a meio máximo ($\text{FWHM}$) da PSF do sistema, o valor máximo de pico medido ($\mu_{\text{pico}}$) decai severamente em relação ao valor real:

$$
\lim_{r \to 0} \mu_{\text{pico}} = \mu_{\text{fundo}}
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

O controle e a mitigação do Efeito de Volume Parcial são fundamentais na otimização de protocolos de aquisição e algoritmos de reconstrução em Tomografia Computadorizada:

* **Protocolos de Aquisição e Colimação:** Para minimizar o EVP no eixo longitudinal ($z$), utiliza-se a aquisição com colimações mais finas (cortes submilimétricos) e reconstruções com sobreposição de fatias (*overlapping slices*). No entanto, fatias mais finas aumentam o ruído quântico, exigindo um balanço com a dose de radiação administrada ao paciente de acordo com o princípio [[Radioproteção|ALARA]].
* **Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Algoritmos modernos de reconstrução, como a [[Reconstrução Iterativa|Reconstrução Iterativa]] e redes neurais baseadas em [[Inteligência Artificial (IA)]], incorporam modelos complexos do sistema físico (*system modeling*), incluindo a modelagem exata da PSF e da geometria do feixe de raios X. Isso permite mitigar os artefatos de borramento e restaurar parcialmente a nitidez em bordas afetadas pelo EVP sem amplificar excessivamente o ruído.
* **Dosimetria e Radioterapia:** O EVP afeta diretamente a segmentação de volumes alvo tumorais e órgãos-alvo de risco em planejamento radioterápico. Erros na definição de bordas decorrentes do EVP podem resultar em subdosagem do tumor ou irradiação excessiva de tecidos sadios.
* **Controle de Qualidade (QC):** Em fantomas de teste (como os de ACR ou Catphan), o EVP é avaliado indiretamente ao medir a função de transferência de modulação ([[Modulation Transfer Function (MTF)|MTF]]) e a resolução espacial, garantindo que o sistema de TC mantenha sua capacidade de discriminar pequenas estruturas de alto contraste.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]
* [[Física das Radiações|Física da Radiação]]
* [[Reconstrução de Imagem]]
* [[Reconstrução Iterativa|Reconstrução Iterativa]]
* [[Inteligência Artificial (IA)]]
* [[Control de Qualidade em TC]]
* [[Ruído Quântico e Dose]]
* [[Task Transfer Function|Função de Transferência de Modulação (MTF)]]