> 📅 **Data:** 2026-08-27 | 🔗 **Conexões:** [[Radiodiagnóstico e Imagem Médica]], [[Radioterapia e Dosimetria]], [[Medicina Nuclear]], [[Radioproteção]]

## 1. Fundamentação e Escopo da Física Médica

A **Física Médica** é a disciplina que aplica os conceitos, métodos e teorias da física à medicina e à biologia humana, atuando como o alicerce científico e tecnológico para a garantia de qualidade\, dosimetria avançada, segurança radiológica e otimização de sistemas de diagnóstico e tratamento. A atuação do físico médico divide-se em grandes domínios especializados, cada qual fundamentado em rigorosos princípios metrológicos e regulatórios.

Historicamente consolidada nas frentes de radioterapia\, diagnóstico por imagem e medicina nuclear, a disciplina expandiu-se vertiginosamente com a incorporação de métodos computacionais avançados, incluindo a [[Tomografia Computadorizada]] espectral ([[Photon Counting Detector CT (PCD-CT)]]), algoritmos de reconstrução baseados em inteligência artificial ([[Deep Learning Image Reconstruction (DLR)]]) e a metrologia baseada em tarefas ([[task-based-image-quality]]).

---

## 2. Taxonomia das Grandes Áreas de Atuação

A tabela abaixo sintetiza as principais divisões da Física Médica, especificando suas frentes tecnológicas, grandezas metrológicas fundamentais e aplicações clínicas:

| Grande Área | Subdomínios Principais | Grandezas Físico-Metrológicas | Tecnologias e Ferramentas | Relacionamento na Wiki |
| :--- | :--- | :--- | :--- | :--- |
| **Radiodiagnóstico & Imagem** | [[Tomografia Computadorizada]], Radiografia, Ressonância Magnética, Ultrassom | $\text{CTDI}_{\text{vol}}$, $\text{DLP}$, $\text{MTF}$, $\text{NPS}$, $\text{t-MTF}$, $d'$ | [[Photon Counting Detector CT (PCD-CT)]], [[reconstrucao-iterativa]], [[Deep Learning Image Reconstruction (DLR)]], [[tube-current-modulation]] | [[aapm-tg233-ct-performance]], [[Índice de Detectabilidade]], [[Noise Power Spectrum]] |
| **Radioterapia** | Teleterapia (Aceleradores Lineares), Braquiterapia, Prótons e Íons Pesados | Dose Absorvida ($Gy$), Kerma no Ar, DVH (Histograma Dose-Volume) | Feixes de Fótons/Elétrons, Planejamento de Tratamento (TPS), [[monte-carlo-simulation|Simulacao_Monte_Carlo]] | [[radioterapia-e-dosimetria]], [[dosimetria]] |
| **Medicina Nuclear** | Imageamento SPECT e PET, Teranóstica (Lu-177, Y-90, I-131) | Atividade ($\text{Bq}$), Taxa de Contagem, SUV (Standardized Uptake Value) | Radiofármacos emissores gama/pósitrons, Câmaras Gama, PET-CT | [[tomografia-computadorizada-espectral]] |
| **Proteção Radiológica** | Dosimetria Ocupacional, Blindagem Estrutural, Otimização ALARA | Dose Efetiva ($E$), Dose Equivalente ($H_T$), Coeficientes de Conversão | Dosímetros OSL/TLD, Salas Blindadas, DRLs ([[niveis-de-referencia-diagnostica-drl]]) | [[otimizacao-de-dose-em-tc]], [[risco-oncologico-radiacao-tc]] |

---

## 3. Intersecção com a Metrologia de Tomografia Computadorizada

No escopo específico do imageamento transaxial e da [[Tomografia Computadorizada]], a física médica moderna exige a união entre a dosimetria macroscópica e a percepção de imagem baseada em tarefas ([[task-based-image-quality]]):

- **Dosimetria Quantitativa:** A avaliação do risco estocástico e da conformidade regulatória fundamenta-se em descritores como o Índice de Dose volumétrico ($\text{CTDI}_{\text{vol}}$) e o Produto Dose-Comprimento ($\text{DLP}$):

$$
\text{CTDI}_{\text{vol}} = \frac{1}{\text{pitch}} \cdot \left[ \frac{1}{3} \text{CTDI}_{100,\text{centro}} + \frac{2}{3} \text{CTDI}_{100,\text{periferia}} \right]
$$

- **Qualidade de Imagem Baseada em Tarefas:** Com a introdução de algoritmos não-lineares como [[Deep Learning Image Reconstruction (DLR)]], as métricas tradicionais de ruído foram substituídas pelo acoplamento entre a [[Task Transfer Function]] ($\text{TTF}$), o [[Noise Power Spectrum]] ($\text{NPS}$) e o [[Índice de Detectabilidade]] ($d'$), assegurando que reduções na dose absorvida não comprometam a acurácia diagnóstica do observador humano ou computacional ([[model-observers]]).

---

## 4. Conexões e Wikilinks
- [[fisica-medica]]
- [[Tomografia Computadorizada]]
- [[aapm-tg233-ct-performance]]
- [[Índice de Detectabilidade]]
- [[Task Transfer Function]]
- [[Noise Power Spectrum]]
- [[model-observers]]
- [[Deep Learning Image Reconstruction (DLR)]]
- [[Photon Counting Detector CT (PCD-CT)]]
- [[metricas-de-dose-tc]]
