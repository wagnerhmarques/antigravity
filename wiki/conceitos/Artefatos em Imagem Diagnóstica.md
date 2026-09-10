---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, qualidade-de-imagem, inteligencia-artificial, reconstrucao-de-imagem]
data: 2026-08-25
---

# Artefatos em Imagem Diagnóstica

## 1. Definição Conceitual e Fundamentação Física / Metrológica

Em Tomografia Computadorizada (TC) e outras modalidades de imagem diagnóstica, um **artefato** é definido como qualquer discrepância sistemática entre os valores numéricos dos pixels (ou voxels) na imagem reconstruída e os coeficientes de atenuação linear verdadeiros ($extmu$) do objeto anatômico escaneado. Metrologicamente, os artefatos representam erros de exatidão (acurácia) que degradam a qualidade da imagem, podendo imitar patologias reais (falsos positivos) ou obscurecer lesões sutis (falsos negativos).

A formação de artefatos na TC decorre fundamentalmente de violações das premissas físicas e matemáticas assumidas pelos algoritmos de reconstrução padrão (como a Retroprojeção Filtrada - FBP). Essas premissas incluem:
1. A radiação X é perfeitamente monoenergética.
2. Os raios X viajam em linhas retas infinitesimais (feixes perfeitamente colimados e sem dispersão).
3. O detector responde de forma linear, instantânea e sem ruído ao fluxo de fótons incidentes.
4. O paciente é estático durante toda a aquisição angular.

Quando a física real do feixe policromático, a dispersão Compton, o movimento fisiológico, a saturação eletrônica ou o ruído quântico interagem com o sistema de aquisição, ocorrem inconsistências nos dados de projeção (sinograma). Essas inconsistências propagam-se geometricamente durante o processo de retroprojeção, manifestando-se sob formas visuais características, tais como:

*   **Endurecimento do Feixe (*Beam Hardening*):** Causado pela atenuação preferencial de fótons de baixa energia em feixes policromáticos, gerando artefatos em forma de faixa (*cupping artifact* ou *dark bands*).
*   **Volparcial (*Partial Volume Effect*):** Ocorre quando múltiplos tecidos de densidades distintas compartilham o mesmo voxel, ou quando estruturas de alta densidade ocupam apenas uma fração do feixe ao longo do eixo z.
*   **Movimento (*Motion Artifacts*):** Desalinhamentos espaciais entre projeções consecutivas geram sombreamentos\, duplicação de bordas e artefatos de risca (*streaks*).
*   **Metálicos (*Metal Artifacts*):** Causados por atenuação extrema e saturação de fótons na presença de próteses ortopédicas ou clipes cirúrgicos, resultando em fortes riscas de alto e baixo contraste.
*   **Ruído Quântico e Efeitos Estatísticos:** Em doses baixas de radiação, a contagem insuficiente de fótons gera ruído poissoniano severo, amplificado por algoritmos lineares de reconstrução.

---

## 2. Formulação Matemática e Propriedades

Para compreender a gênese matemática dos artefatos, considere o modelo ideal da Transformada de Radon para um objeto bidimensional representado pelo coeficiente de atenuação $f(x,y) = \mu(x,y)$. O sinograma $p(\theta, t)$ é dado por:

$$
p(\theta, t) = \iint_{-\infty}^{\infty} f(x,y) \delta(x \cos\theta + y \sin\theta - t) \, dx \, dy
$$

Onde $\theta$ é o ângulo de projeção e $t$ é a distância do detector ao centro de rotação.

### A. Inconsistência de Projeção e O Princípio da Superposição Linear
Se um fenômeno físico perturba a atenuação de modo não linear (violando a lei de Beer-Lambert pura para feixe policromático), a projeção medida $\tilde{p}(\theta, t)$ difere da projeção ideal $p(\theta, t)$ por um termo de erro $\varepsilon(\theta, t)$:

$$
\tilde{p}(\theta, t) = p(\theta, t) + \varepsilon(\theta, t)
$$

Quando o operador de Retroprojeção Filtrada $\mathcal{R}^{-1}\{\cdot\}$ é aplicado, a imagem reconstruída $\tilde{f}(x,y)$ torna-se:

$$
\tilde{f}(x,y) = \mathcal{R}^{-1}\{\tilde{p}(\theta, t)\} = f(x,y) + \mathcal{R}^{-1}\{\varepsilon(\theta, t)\}
$$

O termo $\mathcal{R}^{-1}\{\varepsilon(\theta, t)\}$ é o campo de artefatos na imagem espacial. Devido à natureza do filtro rampa na reconstrução FBP (que amplifica altas frequências espaciais), pequenos erros locais $\varepsilon(\theta, t)$ no domínio do sinograma projetam-se como riscas (*streaks*) de alta amplitude que atravessam toda a imagem.

### B. Modelo para Endurecimento do Feixe
Para um feixe policromático com espectro de energia $I_0(E)$, a intensidade medida $I(t)$ é descrita por:

$$
I(t) = \int_{0}^{E_{\max}} I_0(E) \exp \left( - \int L_t \mu(x,y,E) \, ds \right) dE
$$

Como a atenuação $\mu$ diminui à medida que a energia $E$ aumenta, a relação entre $-\ln(I/I_0)$ e a espessura do material deixa de ser linear. O algoritmo reconstrutor, assumindo $\mu$ constante e independente de $E$, subestima os coeficientes de atenuação no centro de objetos homogêneos densos, gerando o perfil de *cupping*:

$$
f_{\text{reconstruído}}(r) = f_{\text{verdadeiro}}(r) - \Delta_{\text{bh}}(r)
$$

Onde $\Delta_{\text{bh}}(r)$ representa a depressão parabólica induzida no centro do perfil radial $r$.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A gestão e a mitigação de artefatos são pilares fundamentais no Controle de Qualidade (CQ) físico-médico e na otimização do protocolo de aquisição (balanço entre dose e qualidade de imagem diagnóstica).

### A. Controle de Qualidade (CQ) e Fantomas
Físicos médicos utilizam fantomas padronizados (como o fantoma ACR de TC) para quantificar a presença de artefatos de uniformidade, linearidade e ruído. O teste de uniformidade mede o desvio padrão e a variação de número Hounsfield (HU) em regiões de interesse (ROIs) periféricas e centrais, avaliando a eficácia dos algoritmos de correção de endurecimento de feixe do escâner.

### B. Mitigação via Reconstrução e Processamento Avançado
A evolução tecnológica permitiu transpor as limitações puramente físicas através de métodos computacionais avançados:
*   **Correções no Sinograma (Pré-reconstrução):** Técnicas baseadas em modelagem física estimam o espectro policromático e aplicam linearização prévia dos dados brutos ou interpolação em lacunas de dados metálicos (*metal trace interpolation*).
*   **Reconstrução Iterativa (IR) e Modelagem Estatística:** Algoritmos como IR e **Model-Based Iterative Reconstruction (MBIR)** incorporam estatísticas de ruído (distribuição de Poisson e Gaussiana) e modelos precisos do sistema (*system matrix*), reduzindo drasticamente artefatos de ruído quântico e feixes truncados.
*   **Deep Learning Reconstruction (DLR) e Inteligência Artificial:** Redes neurais profundas (ex: redes convolucionais e modelos de difusão) são treinadas para mapear imagens corrompidas por artefatos (baixa dose, feixe endurecido, metal) diretamente para o domínio de alta qualidade de referência. Em IA aplicada à imagem diagnóstica, um desafio crítico é evitar a *alucinação* estrutural — ou seja, garantir que a rede não remova patologias reais ou crie falsas anatomias ao tentar suprimir artefatos severos de risca.

---

## 4. Conexões e Wikilinks

*   [[Tomografia Computadorizada|Tomografia Computadorizada]]
*   [[Retroprojeção Filtrada (FBP)|Retroprojecao Filtrada]]
*   [[Reconstrução Iterativa|Reconstrucao Iterativa]]
*   [[Inteligencia Artificial IA|Inteligencia Artificial em Imagem Medica]]
*   [[Física das Radiações|Fisica da Radiacao]]
*   [[Dosimetria em Radiologia]]
*   [[Controle de Qualidade em TC]]