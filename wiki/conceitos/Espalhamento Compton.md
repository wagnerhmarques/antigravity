---
tipo: conceito
titulo: "Espalhamento Compton (Inelástico) em Imagens Radiológicas e TC"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "interacao-radiacao-materia"
  - "espalhamento-compton"
  - "qualidade-de-imagem"
  - "fisica-medica"
  - "dosimetria"
---

# Espalhamento Compton (Inelástico) em Imagens Radiológicas e TC

## 1. Definição e Cinemática Relativística

O **Espalhamento Compton** (ou espalhamento inelástico / incoerente) é o processo no qual um fóton de raios X incidente colide com um elétron orbital fracamente ligado da camada externa de um átomo do meio absorvedor ($E_b \ll h\nu$), comportando-se essencialmente como um elétron livre.

Durante a colisão, o fóton transfere parte de sua energia e momento para o elétron (que é ejetado como elétron de recuo Compton) e emerge defletido por um ângulo de espalhamento $\theta$ com menor frequência e maior comprimento de onda ($\lambda' > \lambda$).

### Equação do Desvio Compton de Comprimento de Onda (Arthur Compton, 1923):

$$
\Delta \lambda = \lambda' - \lambda = \frac{h}{m_e c} (1 - \cos\theta) = \lambda_C (1 - \cos\theta)
$$

Onde:
- $\lambda_C = \frac{h}{m_e c} \approx 2{,}426 \times 10^{-12}\text{ m} = 0{,}02426\text{ \AA}$ é o **comprimento de onda Compton** do elétron;
- $m_e$ é a massa de repouso do elétron ($9{,}109 \times 10^{-31}\text{ kg}$);
- $c$ é a velocidade da luz no vácuo ($2{,}998 \times 10^8\text{ m/s}$);
- $\theta$ é o ângulo de deflexão do fóton espalhado em relação à trajetória incidente.

---

## 2. Balanço Energético e Seção de Choque de Klein-Nishina

### 2.1. Energia do Fóton Espalhado ($E'$):
Pela conservação relativística de energia e momento linear quadridimensional:

$$
E' = \frac{E}{1 + \frac{E}{m_e c^2} (1 - \cos\theta)}
$$

onde $m_e c^2 \approx 511\text{ keV}$ é a energia de repouso do elétron.

### 2.2. Energia Cinética do Elétron de Recuo ($E_e$):

$$
E_e = E - E' = E \left[ \frac{\frac{E}{m_e c^2}(1 - \cos\theta)}{1 + \frac{E}{m_e c^2}(1 - \cos\theta)} \right]
$$

### 2.3. Seção de Choque Diferencial de Klein-Nishina:
A probabilidade angular de espalhamento por elétron livre no ângulo sólido $d\Omega$ é regida pela eletrodinâmica quântica:

$$
\frac{d\sigma_{\text{KN}}}{d\Omega} = \frac{r_e^2}{2} \left( \frac{E'}{E} \right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - \sin^2\theta \right]
$$

onde $r_e = \frac{e^2}{4\pi \varepsilon_0 m_e c^2} \approx 2{,}818 \times 10^{-15}\text{ m}$ é o raio clássico do elétron.

---

## 3. Coeficiente de Atenuação e Comportamento em Diagnóstico por Imagem

O coeficiente de atenuação linear Compton $\sigma$ e o coeficiente mássico $\frac{\sigma}{\rho}$ dependem fundamentalmente da **densidade eletrônica** ($\rho_e$) do meio:

$$
\frac{\sigma}{\rho} \propto \rho_e = N_A \cdot \left( \frac{Z}{A} \right) \cdot f_{\text{KN}}(E)
$$

### Características Fundamentais em Tomografia Computadorizada:
1. **Quase Independência do Número Atômico ($Z$):** Como a razão $\frac{Z}{A} \approx 0{,}4 - 0{,}5$ é praticamente constante para a maioria dos elementos biológicos leves (exceto o hidrogênio, onde $\frac{Z}{A} = 1$), a atenuação Compton reflete a **densidade mássica física** ($\text{g/cm}^3$) e a densidade eletrônica dos tecidos.
2. **Degradação da Imagem:** Fótons espalhados que atingem os detectores de TC desviam da linha de projeção direta, adicionando um *background* espúrio homogêneo que reduz o contraste e eleva o [[Noise Power Spectrum|noise-power-spectrum]] (NPS).
3. **Mitigação:** Requer o emprego de colimadores pré-detector (*anti-scatter grids* - ASG) e algoritmos de correção de espalhamento via simulações [[Simulação de Monte Carlo|monte-carlo-simulation]].

---

## 4. Conexões no Acervo

- [[Efeito Fotoelétrico|efeito-fotoelectrico]]
- [[Atenuação|atenuacao]]
- [[Noise Power Spectrum|noise-power-spectrum]]
- [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]]
- [[Tomografia Computadorizada Espectral|tomografia-computadorizada-espectral]]
- [[Radioproteção|radioprotecao]]
- [[Simulação de Monte Carlo|monte-carlo-simulation]]
