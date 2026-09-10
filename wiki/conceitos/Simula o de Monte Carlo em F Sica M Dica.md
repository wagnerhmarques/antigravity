---
tipo: conceito
tags: [fisica-medica, tomografia-computadorizada, monte-carlo, dosimetria, radioterapia, inteligencia-artificial]
data: 2026-08-25
---

# Simulação de Monte Carlo em Física Médica

## 1. Definição Conceitual e Fundamentação Física / Metrológica

A **Simulação de Monte Carlo** em Física Médica constitui a classe de métodos estocásticos computacionais utilizada para modelar o transporte e a interação de radiação ionizante (fótons, elétrons, pósitrons, prótons e íons pesados) com a matéria biológica e inorgânica. Baseada na amostragem estatística de distribuições de probabilidade fundamentadas em seções de choque (cross-sections) microscópicas, esta técnica resolve numericamente a equação de transporte de Boltzmann sem as aproximações simplificadoras inerentes aos métodos determinísticos.

Do ponto de vista metrológico, o método de Monte Carlo é amplamente reconhecido como o **padrão-ouro (gold standard)** para o cálculo de dose absorvida, modelagem de fontes radioativas, projeto de blindagens e validação de algoritmos comerciais de planejamento de tratamento em radioterapia e de protocolos de otimização de dose em [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]. A simulação acompanha o histórico completo de partículas individuais (desde a sua origem até a sua absorção ou escape do sistema de interesse), simulando fenômenos físicos estocásticos como o efeito fotoelétrico, espalhamento Compton, produção de pares, espalhamento Rayleigh e interações coulombianas de partículas carregadas.

---

## 2. Formulação Matemática e Propriedades

O transporte de radiação é regido pela Equação de Transporte de Boltzmann (ETB). Em sua forma integro-diferencial estacionária, a densidade de fluxo de partículas $\psi(\mathbf{r}, E, \mathbf{\Omega})$ em um ponto $\mathbf{r}$, com energia $E$ e direção de movimento $\mathbf{\Omega}$, é descrita por:

$$
\mathbf{\Omega} \cdot 
abla \psi(\mathbf{r}, E, \mathbf{\Omega}) + \mu(\mathbf{r}, E)\psi(\mathbf{r}, E, \mathbf{\Omega}) = \int_{0}^{\infty} dE' \int_{4\pi} d\mathbf{\Omega}' \psi(\mathbf{r}, E', \mathbf{\Omega}') k(\mathbf{r}; E', \mathbf{\Omega}' \to E, \mathbf{\Omega}) + q(\mathbf{r}, E, \mathbf{\Omega})
$$

Onde:
- $\mu(\mathbf{r}, E)$ é o coeficiente de atenuação linear total.
- $k(\mathbf{r}; E', \mathbf{\Omega}' \to E, \mathbf{\Omega})$ é o núcleo de espalhamento que descreve a probabilidade de transição de um estado $(E', \mathbf{\Omega}')$ para $(E, \mathbf{\Omega})$.
- $q(\mathbf{r}, E, \mathbf{\Omega})$ representa a função fonte de radiação.

Na simulação de Monte Carlo, em vez de resolver diretamente esta equação integro-diferencial, amostram-se caminhos livres médios e distribuições angulares diferenciais com base nas seções de choque microscópicas $\sigma_i(E)$. A distância percorrida por uma partícula entre interações sucessivas, $s$, é obtida por amostragem inversa da probabilidade de atenuação exponencial:

$$
s = -\frac{\ln(\xi)}{\mu(\mathbf{r}, E)}
$$

Onde $\xi$ é um número pseudo-aleatório uniformemente distribuído no intervalo aberto $(0, 1]$.

### Estimativa Estatística e Incerteza

A dose absorvida $D$ em um volume de interesse $V$ é calculada como o valor esperado da energia depositada por unidade de massa. Pelo Teorema do Limite Central, a incerteza padrão associada à média da dose estimada após $N$ histórias independentes é proporcional a $1/\sqrt{N}$:

$$
\sigma_{\bar{D}} = \frac{1}{\sqrt{N(N-1)}} \sum_{i=1}^{N} \left( D_i - \bar{D} \right)^2
$$

Para mitigar o elevado custo computacional associado à exigência de grandes valores de $N$, utilizam-se técnicas de **redução de variância**, tais como:
- *Russian Roulette* e *Splitting* (Roleta Russa e Divisão de Partículas).
- *Cross-section biasing* (Polarização de seção de choque).
- *Forced interaction* (Interação forçada).

---

## 3. Aplicações e Relevância em Tomografia Computadorizada e Otimização

Embora amplamente difundido na radioterapia externa e braquiterapia, o uso de simulações de Monte Carlo na [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]] expandiu-se drasticamente devido à necessidade de precisão na avaliação de riscos radiobiológicos e no desenvolvimento tecnológico avançado:

1. **Dosimetria Específica do Paciente:** Modelagem detalhada de exames de TC a partir de conjuntos de dados de imagens volumétricas (matrizes DICOM convertidas em mapas de voxels de densidade eletrônica e composição elemental), permitindo o cálculo rigoroso de dose órgão a órgão ($D_T$) e dose efetiva ($E$).
2. **Correção de Artefatos e Modelagem de Sistema:** Simulação exata do espectro policromático de raios-X emitido pelo tubo, atenuação por feixe policromático (*beam hardening*), espalhamento Compton induzido no paciente e resposta geométrica dos detectores de estado sólido (ex: cerâmicas de gadolínio).
3. **Desenvolvimento de Algoritmos de Reconstrução e Inteligência Artificial:** 
   - Geração de dados sintéticos de alta fidelidade para treinamento de redes neurais em tarefas de **Redução de Ruído por Aprendizado Profundo (DLR)**.
   - Simulação de protocolos de dose ultra-baixa (*ultra-low dose CT*) para testar limites de detecção de lesões por [[Observadores de Modelo (Model Observers)|Observadores Computacionais]].
4. **Otimização de Geometrias de Aquisição:** Projeto de novos arranjos de collimadores, filtros borboleta (*bowtie filters*) e blindagens dinâmicas para varreduras de variação helicoidal complexa.

---

## 4. Conexões e Wikilinks

- [[Tomografia Computadorizada|Tomografia Computadorizada (TC)]]
- [[Dosimetria em Radiologia]]
- [[Redução de Ruído por Aprendizado Profundo (DLR)]]
- [[Observadores de Modelo (Model Observers)|Observadores Computacionais]]
- [[Artefatos em Tomografia Computadorizada]]
- [[Planejamento de Tratamento Radioterápico (TPS)]]