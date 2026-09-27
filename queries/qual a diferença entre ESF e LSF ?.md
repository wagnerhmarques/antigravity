> 📅 **Data:** 2026-09-27 | 🔗 **Conexões:** [[Task Transfer Function]], [[Índice de Detectabilidade]], [[Noise Power Spectrum]], [[Tomografia Computadorizada]]

## 1. Fundamentação Física e Definições Fundamentais

A caracterização da resolução espacial em sistemas de raios-X e [[Tomografia Computadorizada]] exige o uso de funções de resposta impulsional e degrau. A **Edge Spread Function (ESF)** e a **Line Spread Function (LSF)** representam respostas fundamentais do sistema de imagem a estímulos ideais unidimensionais (uma borda afiada e uma linha infinitesimal, respectivamente).

Enquanto a ESF descreve a resposta do sistema de imagem a uma descontinuidade abrupta do tipo degrau de atenuação (como a interface entre um fantoma de alta densidade e o ar ou água), a LSF representa a resposta do sistema a uma linha extremamente fina e infinitamente longa de material atenuante.

---

## 2. Formulação Matemática e Relação Operacional

Matematicamente, as funções estão intimamente interconectadas através de operações de diferenciação e integração no domínio espacial, além de guardarem relação direta com a Função de Transferência de Modulação ([[Task Transfer Function|Task Transfer Function]] - TTF).

### A. Derivada da ESF para obtenção da LSF
A LSF é obtida analiticamente calculando a derivada espacial da ESF medindo o perfil perpendicular à borda do fantoma:

$$
\text{LSF}(x) = \frac{d}{dx} \left[ \text{ESF}(x) \right]
$$

Onde $x$ representa a coordenada espacial transversal à borda ou linha. Inversamente, a ESF pode ser expressa pela integral da LSF:

$$
\text{ESF}(x) = \int_{-\infty}^{x} \text{LSF}(x') \\, dx'
$$

### B. Conexão com a Função de Dispersão de Ponto (PSF) e a MTF
A LSF representa o perfil unidimensional da Função de Dispersão de Ponto bi-dimensional ([[Task Transfer Function|PSF]]) integrada ao longo da direção longitudinal:

$$
\text{LSF}(x) = \int_{-\infty}^{\infty} \text{PSF}(x, y) \\, dy
$$

A partir da LSF, aplica-se a Transformada de Fourier 1D para computar a Função de Transferência de Modulação ([[Task Transfer Function|MTF]] ou $\text{TTF}$):

$$
\text{TTF}(f_x) = \left| \int_{-\infty}^{\infty} \text{LSF}(x) e^{-j 2 \pi f_x x} \\, dx \right|
$$

---

## 3. Tabela Comparativa Prática

| Característica / Parâmetro | Edge Spread Function (ESF) | Line Spread Function (LSF) |
| :--- | :--- | :--- |
| **Estímulo Físico** | Borda afiada (degrau deg/step) | Fio fino ou linha de alta atenuação |
| **Dimensionalidade** | Perfil 1D acumulado | Perfil 1D simétrico de linha |
| **Operação Matemática** | Integral da LSF / Base para derivada | Derivada da ESF / Projeção 1D da PSF |
| **Sensibilidade a Ruído** | Menor sensibilidade (efeito de integração reduz ruído) | Maior sensibilidade (requer suavização prévia de perfis) |
| **Aplicação em [[Tomografia Computadorizada]]** | Análise de resolução em interfaces ar-tecido em phantoms de CQ | Medição de largura a meia altura ([[Task Transfer Function|FWHM]]) e corte espacial |

---

## 4. Relevância para a Otimização e Projeto de Doutorado

No contexto do desenvolvimento de estratégias de otimização multiobjetivo e avaliação de algoritmos avançados de reconstrução em TC — incluindo técnicas de Reconstrução Iterativa e redes neurais de Aprendizado Profundo —, a extração precisa de ESF e LSF é etapa mandatória. Erros na derivação da ESF para a obtenção da LSF propagam-se diretamente para o cálculo da [[Task Transfer Function|Task Transfer Function (TTF)]]. Como a $\text{TTF}$ compõe o numerador do [[Índice de Detectabilidade]] ($d'$), a acurácia metrológica na mensuração de bordas e linhas em phantoms antropomórficos impacta diretamente a predição da detectabilidade de lesões de baixo contraste em exames clínicos.
