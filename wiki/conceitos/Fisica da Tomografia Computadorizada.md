---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, radiologia, formacao-de-imagem, metrologia-das-radiacoes]
data: 2026-08-25
---

# Fisica_da_Tomografia_Computadorizada

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A Física da Tomografia Computadorizada (TC) abrange os princípios fundamentais que regem a geração, modulação, atenuação, detecção e reconstrução digital de imagens tomográficas de raios X. Diferente da radiografia convencional, na qual ocorre a superposição de estruturas anatômicas tridimensionais em um plano bidimensional receptor, a TC resolve o problema da superposição espacial através da aquisição de múltiplos perfis de projeção obtidos sob diversos ângulos em torno do paciente.

Do ponto de vista metrológico, o processo físico central é a atenuação da radiação ionizante descrita pela Lei de Beer-Lambert para feixes policromáticos. Quando um feixe de raios X polimórfico de intensidade inicial $I_0$ atravessa um meio material heterogêneo, a intensidade transmitida $I$ é dada por:

$$
I = I_0 \exp\left( -\int_{L} \mu(x, y, z; E) \, dl \right)
$$

onde $\mu(x, y)$ representa o coeficiente de atenuação linear espacialmente variante (expresso em $\text{cm}^{-1}$) e o integral linha $dl$ é traçado ao longo da trajetória do fóton. O objetivo primário da física da TC é resolver este problema inverso, recuperando a distribuição espacial exata de $\mu(x, y)$ a partir de um conjunto discreto e ruidoso de medições de intensidade (projeções).

A unidade padrão utilizada para expressar os valores dos pixels na imagem reconstruída é o **Número de Tomografia Computadorizada (NTC)**, comumente medido em unidades Hounsfield (UH), definidas em relação ao coeficiente de atenuação da água ($\mu_{\text{água}}$) e do ar ($\mu_{\text{ar}}$ $\approx 0$):

$$
\text{UH} = 1000 \times \frac{\mu - \mu_{\text{água}}}{\mu_{\text{água}} - \mu_{\text{ar}}}
$$

Essa escala padronizada assegura a reprodutibilidade quantitativa da densidade eletrônica e do número atômico efetivo dos tecidos biológicos escaneados, sendo fundamental para o diagnóstico clínico, radioterapia e análises quantitativas baseadas em [[Reconstrucao_Iterativa_e_Profunda]] e [[Radiomics_e_Biomarcadores_de_Imagem]].

---

## 2. Formulação Matemática e Propriedades

O fundamento matemático para a reconstrução de imagens em TC baseia-se na **Transformada de Radon** e no célebre **Teorema da Fatia Central** (*Central Slice Theorem*).

### A Transformada de Radon
Seja $f(x, y) = \mu(x, y)$ a função contínua que descreve a distribuição do coeficiente de atenuação. A projeção paralela $p(r, \theta)$, obtida a uma distância $r$ do centro de rotação e sob um ângulo de projeção $\theta$, é formalmente definida pela Transformada de Radon bidimensional:

$$
p(r, \theta) = \iint_{-\infty}^{\infty} f(x, y) \delta(x \cos\theta + y \sin\theta - r) \, dx \, dy
$$

onde $\delta$ é a função delta de Dirac. Cada perfil de projeção angular forma um sinograma quando visualizado no plano $(r, \theta)$.

### O Teorema da Fatia Central
O Teorema da Fatia Central estabelece que a Transformada de Fourier unidimensional de uma projeção paralela $p(r, \theta)$, tomada em relação à coordenada espacial $r$, é idêntica à fatia radial bidimensional da Transformada de Fourier bidimensional de $f(x, y)$, extraída sob o mesmo ângulo $\theta$. 

Matematicamente, definindo $P(f_r, \theta)$ como a transformada de Fourier de $p(r, \theta)$ com frequência espacial $f_r$:

$$
P(f_r, \theta) = \int_{-\infty}^{\infty} p(r, \theta) e^{-j 2 \pi f_r r} \, dr = F(f_r \cos\theta, f_r \sin\theta)
$$

onde $F(f_x, f_y)$ é a transformada de Fourier bidimensional de $f(x, y)$.

### Retroprojeção Filtrada (FBP)
Para recuperar a imagem $f(x, y)$ a partir das projeções no domínio espacial, utiliza-se o algoritmo analítico de **Retroprojeção Filtrada (Filtered Backprojection - FBP)**. A formulação contínua da FBP é dada por:

$$
f(x, y) = \int_{0}^{\pi} \left[ \int_{-\infty}^{\infty} P(f_r, \theta) \, |f_r| \, e^{j 2 \pi f_r r} \, df_r \right]_{\theta = x\cos\theta + y\sin\theta} \, d\theta
$$

O termo $|f_r|$ representa o filtro rampa (*ramp filter*), essencial para compensar o desfoque inerente à simples retroprojeção geométrica ($1/r$). Na prática discreta, filtros de suavização ou realce (como *Hamming*, *Hann* ou *Shepp-Logan*) são convoluídos com o filtro rampa para controlar o balanço entre resolução espacial e atenuação de ruído quântico.

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

A compreensão rigorosa da física da TC é pré-requisito indispensável para a otimização dos protocolos de imagem, garantia da qualidade metrológica e desenvolvimento de novas tecnologias de reconstrução e dosimetria.

### Otimização da Qualidade de Imagem e Dosimetria
O balanço entre a dose de radiação ionizante absorvida pelo paciente e a qualidade diagnóstica da imagem é regido por leis físicas estritas. A variação da dose efetiva correlaciona-se diretamente com o produto corrente-tempo ($mAs$) e quadraticamente com a redução do potencial do tubo ($kVp$). Métodos físicos de otimização incluem:
* **Modulação Automática de Corrente (mA):** Ajuste dinâmico do feixe em função da atenuação angular e longitudinal do paciente.
* **Filtros de Corrente e Asas de Compensação:** Minimização da dose periférica na pele e equalização do fluxo de fótons nos detectores.
* **Métricas Dosimétricas:** Aplicação rigorosa de grandezas como o Índice de Dose em Tomografia Computadorizada ($CTDI_{vol}$) e o Produto Dose-Comprimento ($DLP$).

### Evolução dos Algoritmos de Reconstrução
As limitações físicas dos algoritmos analíticos (FBP) na presença de ruído elevado e artefatos de feixe endurecido (*beam hardening*) impulsionaram a transição tecnológica para paradigmas avançados:
1. **Reconstrução Iterativa (IR):** Incorporam modelos estatísticos de ruído e modelos físicos do sistema de aquisição (óptica do feixe, geometria focal), permitindo reduções substanciais de dose sem perda perceptível de detectabilidade de baixo contraste.
2. **Reconstrução Baseada em Aprendizado Profundo (DLR):** Redes neurais artificiais treinadas para realizar o mapeamento não linear de dados ruidosos de baixa dose para espaços de alta fidelidade diagnóstica, mitigando artefatos de forma adaptativa.

---

## 4. Conexões e Wikilinks

* [[Reconstrucao_Iterativa_e_Profunda]]
* [[Dosimetria_e_Seguranca_em_Radiologia]]
* [[Qualidade_de_Imagem_e_Artefatos_em_TC]]
* [[Processamento_de_Sinais_e_Filtros_Lineares]]
* [[Inteligencia_Artificial_em_Radiologia_Diagnostica]]