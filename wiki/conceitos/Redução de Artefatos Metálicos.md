---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, processamento-de-imagem, reducao-de-artefatos, inteligencia-artificial]
data: 2026-08-25
---

# reducao-de-artefatos-metalicos

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Redução de Artefatos Metálicos (MAR — *Metal Artifact Reduction*) engloba o conjunto de técnicas físicas, matemáticas e computacionais desenvolvidas para mitigar ou eliminar degradações na qualidade da imagem de Tomografia Computadorizada (TC) causadas pela presença de implantes metálicos de alta densidade e número atômico efetivo elevado (como próteses ortopédicas, clipes cirúrgicos, amálgamas dentárias e parafusos de coluna).

Do ponto de vista físico, a interação dos fótons de raios X com materiais metálicos é dominada pelo Efeito Fotoelétrico (especialmente em energias mais baixas) e pelo espalhamento Compton. Os principais mecanismos físicos responsáveis pelos artefatos são:

1. **Enrijecimento do Feixe (*Beam Hardening*):** Feixes policromáticos de raios X sofrem filtração preferencial dos fótons de baixa energia ao atravessarem o metal. O feixe emergente torna-se, portanto, mais "duro" (com energia média superior), violando a premissa de atenuação monocromática linear subjacente aos algoritmos de retroprojeção (como a Retroprojeção Filtrada - FBP). Isso gera as faixas escuras (*dark streaks*) entre estruturas metálicas.
2. **Efeito de Volume Parcial e Saturação do Detector:** Gradientes extremos de atenuação em pixels adjacentes excedem a faixa dinâmica dos detectores ou o limite de amostragem espacial, corrompendo a leitura dos perfis de projeção.
3. **Perda de Informação por Supressão (*Photon Starvation*):** Implantes altamente densos e espessos atenuam praticamente 100% dos fótons em determinados ângulos de projeção. O sinal remanescente cai abaixo do nível de ruído eletrônico do sistema, resultando em sinogramas com dados corrompidos ou zerados, o que gera artefatos radiados em forma de estrela ou faixas brilhantes e escuras (*streaks*).
4. **Espalhamento Compton e Ruído Estatístico:** O espalhamento de alta intensidade gerado pelo metal atinge detectores fora da trajetória geométrica primária, introduzindo vieses severos na quantificação do coeficiente de atenuação linear ($\mu$).

Metrologicamente, a presença de artefatos metálicos compromete a acurácia dos números de Hounsfield (HU), invalida mapas de densidade eletrônica necessários para o planejamento de radioterapia baseada em TC, e mascara patologias adjacentes.

---

## 2. Formulação Matemática e Propriedades

O processo de aquisição em TC é modelado pela Transformada de Radon. Seja $\mu(x,y)$ a distribuição espacial dos coeficientes de atenuação linear no plano de corte. O sinograma $p(\theta, l)$, que representa a projeção paralela a um ângulo $\theta$ na distância $l$ ao longo da linha de integração $\mathcal{L}_{\theta,l}$, é definido por:

$$
p(\theta, l) = \int_{\mathcal{L}_{\theta,l}} \mu(x,y) \, ds = -\ln \left( \frac{I(\theta, l)}{I_0} \theta, l \right)
$$

Onde $I(\theta, l)$ é a intensidade do feixe transmitido e $I_0$ é a intensidade incidente.

Quando há metal na região $\Omega_{\text{metal}} \subset \mathbb{R}^2$, os dados medidos $p_{\text{med}}(\theta, l)$ sofrem corrupções severas $\Delta p$:

$$
p_{\text{med}}(\theta, l) = p_{\text{ideal}}(\theta, l) + \Delta p(\theta, l)
$$

As abordagens tradicionais baseadas em sinograma (como o algoritmo **Normalized Metal Artifact Reduction - NMAR**) operam substituindo os dados corrompidos na região do metal por estimativas interpoladas. 

Seja $\mathcal{M}$ o conjunto de índices do sinograma correspondentes às projeções que atravessam o metal. O processo de restauração define um sinograma corrigido $p_{\text{corr}}(\theta, l)$ por meio de interpolação ponderada:

$$
p_{\text{corr}}(\theta, l) = \begin{cases} 
p_{\text{med}}(\theta, l), & \text{se } (\theta, l) 
otin \mathcal{M} \\ 
\tilde{p}(\theta, l), & \text{se } (\theta, l) em \mathcal{M} 
\end{cases}
$$

Onde $\tilde{p}(\theta, l)$ é obtido a partir de uma imagem prior $I_{\text{prior}}(x,y)$ segmentada do metal, re-projetada para estimar a atenuação esperada:

$$
\tilde{p}(\theta, l) = W(\theta, l) \cdot p_{\text{prior}}(\theta, l) + (1 - W(\theta, l)) \cdot p_{\text{interpolado}}(\theta, l)
$$

Sendo $W(\theta, l)$ uma função de ponderação que mitiga descontinuidades abruptas nas bordas do sinograma.

Na era da Inteligência Artificial, algoritmos baseados em Aprendizado Profundo (*Deep Learning*) modelam a redução de artefatos como um problema de mapeamento não linear de domínios. Dado um operador de rede neural convolucional (CNN) ou transformador $f_{\theta}$ parametrizado por $\theta_{\text{rede}}$, a imagem livre de artefatos $\hat{I}_{\text{limpa}}$ é otimizada minimizando uma função de perda (*loss function*) mista que combina o Erro Quadrático Médio (MSE), a perda perceptual baseada em redes pré-treinadas (como VGG) e termos de variação total ($\text{TV}$):

$$
\mathcal{L}(\theta_{\text{rede}}) = \frac{1}{N} \sum_{i=1}^{N} \left\| f_{\theta}(I_{\text{artefato}}^{(i)}) - I_{\text{ref}}^{(i)} \right\|_2^2 + \lambda_{\text{perc}} \mathcal{L}_{\text{perc}} + \lambda_{\text{TV}} \text{TV}\left(f_{\theta}(I_{\text{artefato}}^{(i)})\right)
$$

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A implementação de algoritmos de MAR é crítica em diversos domínios da física médica clínica e da pesquisa avançada:

* **Planejamento de Radioterapia (RTP):** Erros nos números de Hounsfield causados por artefatos metálicos propagam-se diretamente para os cálculos de dose baseados em algoritmos de superposição/convolução ou Monte Carlo. A correção precisa via MAR é mandatória para evitar subdosagem do volume alvo tumoral (GTV/CTV) ou sobredosagem de órgãos em risco (OARs) adjacentes a próteses.
* **Ortopedia e Neurocirurgia:** A avaliação de osteointegração de próteses de quadril e joelho, bem como a detecção de hemorragias intracranianas ou isquemias em pacientes com clipes aneurismáticos ou eletrodos de estimulação cerebral profunda (DBS)\, depende criticamente de imagens limpas de artefatos.
* **Integração com Reconstrução Iterativa (IR) e Aprendizado Profundo (DLR):** Sistemas modernos de TC combinam correções físicas no domínio dos dados brutos (*raw data*) com algoritmos de reconstrução iterativa estatística (ASiR, Veo, IMR) e redes neurais profundas. Abordagens de aprendizado de máquina em duas etapas (*dual-domain*), que operam simultaneamente no domínio do sinograma e da imagem, têm demonstrado superioridade na preservação de texturas anatômicas reais e na supressão de artefatos residuais "em vidro fosco".
* **Controle de Qualidade (QC) e Dosimetria Computacional:** Em simuladores antropomórficos com inserções metálicas, o uso de MAR assegura que métricas de ruído, resolução espacial e estimativas de dose organonuclear mantêm validade metrológica.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|tomografia-computadorizada]]
* [[Reconstrução de Imagem|reconstrucao-de-imagem]]
* [[Retroprojeção Filtrada (FBP)|retroprojecao-filtrada]]
* [[Reconstrução Iterativa|reconstrucao-iterativa]]
* [[Deep Learning Image Reconstruction (DLR)|inteligencia-artificial-em-tc]]
* [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
* [[Métricas de Dose em TC|dosimetria-em-tomografia]]
* [[efeito-fotoetrico-e-compton]]