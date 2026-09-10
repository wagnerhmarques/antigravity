---
tipo: tecnologia
tags: [fisica-medica, tomografia-computadorizada, inteligencia-artificial, reconstrucao-de-imagem\, dosimetria, equacoes-diferenciais]
data: 2026-08-25
---

# PINNs

## 1. Definição Conceitual e Fundamentação Física / Metrológica

As **PINNs** (*Physics-Informed Neural Networks*, ou Redes Neurais Informadas pela Física) representam um paradigma avançado de aprendizado de máquina onde leis físicas fundamentais — tipicamente expressas na forma de equações diferenciais parciais (EDPs), ordinárias (EDOs) ou restrições integrais — são incorporadas diretamente na função de custo (*loss function*) de uma rede neural artificial. 

No contexto da Física Médica e da Tomografia Computadorizada (TC), as abordagens tradicionais de inteligência artificial baseiam-se em aprendizado puramente supervisionado (*data-driven*). Embora eficazes, tais modelos frequentemente exigem grandes volumes de dados de treinamento, carecem de interpretabilidade e podem gerar artefatos alucinatórios clinicamente perigosos por violarem leis físicas elementares (como a conservação de energia, atenuação linear de fótons de raios X descrita pela lei de Beer-Lambert, ou suavidade espacial anatômica). 

As PINNs superam essas limitações ao atuar como um arcabouço de modelagem híbrida. Elas utilizam a rede neural como um aproximador universal de funções para mapear coordenadas espaciais e temporais (p.ex., $\mathbf{x} = (x, y, z)$ e $t$) aos campos de interesse físico (p.ex., o coeficiente de atenuação linear $\mu(\mathbf{x})$, mapas de dose absorvida $D(\mathbf{x})$, ou campos de velocidade de fluxo sanguíneo). A metrologia computacional e a garantia de qualidade (QA) beneficiam-se sobremaneira das PINNs, pois a rede não apenas se ajusta aos dados experimentais esparsos ou ruidosos, mas também é penalizada se violar os princípios físicos subjacentes ao problema, garantindo maior robustez, interpretabilidade e consistência quantitativa.

---

## 2. Formulação Matemática e Propriedades

Seja um sistema físico regido por uma Equação Diferencial Parcial geral parametrizada em um domínio $\Omega \subset \mathbb{R}^d$ e fronteira $\partial\Omega$:

$$
\mathcal{N}\left[ u(\mathbf{x}); \mathbf{\lambda} \right] = f(\mathbf{x}), \quad \mathbf{x} \in \Omega
$$

sujeita a condições de contorno e iniciais:

$$
\mathcal{B}\left[ u(\mathbf{x}); \mathbf{\lambda} \right] = g(\mathbf{x}), \quad \mathbf{x} \in \partial\Omega
$$

onde $\mathcal{N}$ é um operador diferencial linear ou não-linear (como o operador de transporte radiativo ou a equação do calor), $u(\mathbf{x})$ é a solução verdadeira (desejada), $\mathbf{\lambda}$ representa parâmetros físicos desconhecidos a serem identificados, e $f(\mathbf{x})$ e $g(\mathbf{x})$ são termos de fonte e condições de contorno conhecidos, respectivamente.

Em uma PINN, a solução exata $u(\mathbf{x})$ é aproximada por uma rede neural artificial parametrizada por seus pesos e vieses $\theta$\, denotada por $\hat{u}(\mathbf{x}; \theta)$. A propriedade fundamental das PINNs reside na construção da função de perda total $\mathcal{L}(\theta)$, que é a soma ponderada de termos que quantificam o ajuste aos dados observados e a aderência à física do problema, avaliada por meio de métodos de diferenciação automática (*automatic differentiation*):

$$
\mathcal{L}(\theta) = w_{data} \mathcal{L}_{data}(\theta) + w_{f} \mathcal{L}_{f}(\theta) + w_{b} \mathcal{L}_{b}(\theta)
$$

Onde os componentes individuais são definidos como:

1. **Perda de Dados ($\mathcal{L}_{data}$):** Quantifica o desvio entre as previsões do modelo e as medições empíricas (p.ex., projeções sinogramas ruidosas ou doses medidas por dosímetro):
   

$$
\mathcal{L}_{data}(\theta) = \frac{1}{N_{d}} \sum_{i=1}^{N_{d}} \left| \hat{u}(\mathbf{x}_i^{(d)}; \theta) - u_i^{(d)} \right|^2
$$

2. **Perda Física / Residual ($\mathcal{L}_{f}$):** Avalia o resíduo da EDP em um conjunto de pontos de colocation $\mathbf{x}_j^{(f)}$ espalhados pelo domínio $\Omega$:
   

$$
\mathcal{L}_{f}(\theta) = \frac{1}{N_{f}} \sum_{j=1}^{N_{f}} \left| \mathcal{N}\left[ \hat{u}(\mathbf{x}_j^{(f)}; \theta); \mathbf{\lambda} \right] - f(\mathbf{x}_j^{(f)}) \right|^2
$$

3. **Perda de Fronteira/Condição Inicial ($\mathcal{L}_{b}$):** Garante o cumprimento das restrições nas bordas do domínio $\partial\Omega$:
   

$$
\mathcal{L}_{b}(\theta) = \frac{1}{N_{b}} \sum_{k=1}^{N_{b}} \left| \mathcal{B}\left[ \hat{u}(\mathbf{x}_k^{(b)}; \theta); \mathbf{\lambda} \right] - g(\mathbf{x}_k^{(b)}) \right|^2
$$

Os pesos hiper-reguladores $w_{data}$, $w_{f}$ e $w_{b}$ equilibram o gradiente estocástico durante a otimização por descida de gradiente (p.ex., Adam combinado com L-BFGS).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

No ecossistema da Tomografia Computadorizada e da Física Médica moderna, as PINNs encontram aplicações cruciais em frentes críticas:

* **Reconstrução de Imagem Esparsa e de Baixa Dose (Low-Dose CT):** A varredura de TC com redução drástica de corrente no tubo ($mA$) gera projeções severamente corrompidas por ruído quântico e artefatos de enrijecimento de feixe (*beam hardening*). PINNs podem ser formuladas para resolver o problema inverso da transformada de Radon incorporando diretamente a equação de atenuação linear e a física do espalhamento de fótons. Isso permite a reconstrução de imagens diagnósticas de alta fidelidade a partir de conjuntos de dados extremamente limitados (esparsos angularmente).
* **Correção de Artefatos e Modelagem de Sistema:** Modelar a geometria exata do feixe cônico (*cone-beam CT*) e os efeitos polianergéticos torna-se computacionalmente tratável via PINNs, parametrizando o espectro de raios X diretamente no operador de projeção e retroprojeção.
* **Dosimetria Computacional Avançada:** Em radioterapia guiada por imagem (IGRT) e verificação de dose em tratamentos complexos, as PINNs são aplicadas para resolver a equação de transporte de Boltzmann ou equações de difusão de radiação de maneira acelerada, mapeando campos de dose tridimensionais com base em geometrias de pacientes obtidas via TC, sem a necessidade de simulações de Monte Carlo completas e demoradas para cada fração de tratamento.
* **Resolução de Problemas Inversos Mal-Postos:** A estimativa de parâmetros hemodinâmicos em TC de perfusão (como fluxo sanguíneo cerebral - CBF, e volume sanguíneo - CBV) é inerentemente mal-posta devido ao ruído. PINNs impõem a conservação de massa e a cinética de indicadores diretamente na otimização, estabilizando as soluções.

---

## 4. Conexões e Wikilinks

* [[Tomografia Computadorizada|Tomografia Computadorizada]]
* [[Reconstrução de Imagem]]
* [[Retroprojeção Filtrada (FBP)|FBP]]
* [[Reconstrução Iterativa|Iterative Reconstruction]]
* [[Deep Learning Image Reconstruction (DLR)|DLR]]
* [[Dosimetria]]
* [[Problemas Inversos|problemas-inversos]]
* [[Controle de Qualidade em TC]]