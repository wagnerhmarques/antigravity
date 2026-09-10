---
tipo: fonte
titulo: "Image quality in modern CT imaging: optimization and quantification"
autores:
  - "Eva Janna Ina Hoeijmakers"
  - "Bibi Martens"
  - "Joachim E. Wildberger"
  - "Thomas G. Flohr"
  - "Cécile R. L. P. N. Jeukens"
ano: 2026
veiculo: "Doctoral Thesis, Maastricht University"
doi: "10.26481/dis.20260902eh"
fonte_bruta: "raw/2026_Image quality in modern CT imaging.pdf"
tags:
  - fisica-medica
  - tomografia-computadorizada
  - photon-counting-ct
  - qualidade-de-imagem
  - meio-de-contraste
  - dosimetria
  - revisao-sistematica
---

# Image quality in modern CT imaging: optimization and quantification

## Resumo Executivo
Tese de doutorado defendida por Eva J. I. Hoeijmakers na Universidade de Maastricht abordando a interseção crítica entre novas tecnologias de detecção em tomografia computadorizada (com foco em [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]), estratégias de [[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]] e o desenvolvimento de novas metodologias para quantificação de qualidade de imagem subjetiva ([[Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)|avaliacao-pareada-qualidade-imagem]]) e objetiva ([[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]).

A tese é estruturada em duas grandes frentes:
1. **Parte I — Exploração do Potencial Clínico do PCD-CT:** Diferenciação físico-matemática entre energia de tubo ($kV$) e energia de reconstrução monoenergética ($keV$ via [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]), seguida por ensaios clínicos demonstrando reduções de dose de iodo de 20,1% em abdome e 26,7% em angio-TC pulmonar ([[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]), concomitantemente à preservação ou ganho de relação contraste-ruído ($CNR$) e redução de radiação ($CTDI_{vol}$).
2. **Parte II — Avaliação e Métricas de Qualidade Diagnóstica de Imagem:** Superação dos vieses da escala Likert tradicional através do método de comparação aos pares (Pairwise Comparison via algoritmo de Ford-Johnson) e mapeamento sistemático de métricas objetivas de qualidade *reference-free* (ruído global, resolução espacial de bordo\, detectabilidade e abordagens de inteligência artificial).

---

## Estrutura e Síntese dos Capítulos

### Capítulo 2: Fundamentos Físicos de $kV$ vs. $keV$ e PCD-CT
- **Conceito Chave:** $kV$ (kilovoltagem de pico) define o espectro policromático de fótons emitido pelo anodo de tungstênio (limitado por *bremsstrahlung* e picos característicos), enquanto $keV$ em [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]] (VMI) representa uma reconstrução matemática sintetizada a partir da decomposição espectral de materiais.
- **Interações Fundamentais:**
  - *Efeito Fotoelétrico:* $\propto Z^3 / E^3$\, dominante em baixas energias e materiais de alto $Z$ (iodo $Z=53$, osso).
  - *Espalhamento Compton:* Predominante em altas energias e tecidos moles (baixo $Z$), relativamente independente de $Z$.
- **Vantagem Instrumental do PCD-CT:** Eliminação de ruído eletrônico via limiarização de energia (*energy thresholding*), contagem individual com ponderação equitativa de fótons de baixa energia (que carregam o maior contraste fotoelétrico), superando detectores convencionais de integração de energia ([[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]] vs. EID-CT).
- **Dados do Experimento de Fantoom (Kyoto PBU-60 + Varetas Gammex):**
  - Varetas de iodo (2,0 a 20,0 mg/mL), fígado e músculo avaliadas de 70 a 140 kV (EID-CT) e de 53 a 90 keV em VMI (PCD-CT a 120 kV fixo).
  - Para 10 mg I/mL, atenuação variou de ~420 HU (70 kV) a ~180 HU (140 kV) no EID-CT, e de ~460 HU (53 keV) a ~150 HU (90 keV) em VMIs de PCD-CT.
  - O ruído global ($GNL$) em PCD-CT decresce monotonicamente com o aumento de keV graças a algoritmos avançados de cancelamento de ruído espectral.

### Capítulo 3: Redução de Contraste em TC de Abdome com PCD-CT
- **Delineamento:** Comparação retrospectiva entre 91 exames de EID-CT (protocolo individualizado por peso e adaptado por kV via *Regra 10-para-10*) e 102 exames de PCD-CT (120 kV fixo, VMIs a 60 keV padrão e 55 keV secundário).
- **Parâmetros e Resultados Quantitativos:**
  - Carga Total de Iodo (*Total Iodine Load*, TIL): Redução de **20,1%** no PCD-CT ($22,6 \pm 5,0\text{ g I}$) vs. EID-CT ($28,3 \pm 7,2\text{ g I}$, $p < 0,001$).
  - Taxa de Entrega de Iodo (*IDR*): $0,7 \pm 0,2\text{ g I/s}$ (PCD-CT) vs. $0,9 \pm 0,2\text{ g I/s}$ (EID-CT, $p < 0,001$).
  - Fator de Dosagem (*DF*): $0,30\text{ g I/kg}$ vs. $0,38 \pm 0,02\text{ g I/kg}$ ($p < 0,001$).
  - $SNR$ Hepático: $9,9 \pm 1,7$ (PCD-CT) vs. $9,1 \pm 1,8$ (EID-CT, $p < 0,001$, aumento de 8,7%).
  - $CNR$ Hepático: $5,1 \pm 1,7$ (PCD-CT) vs. $4,3 \pm 1,3$ (EID-CT, $p < 0,001$, aumento de 18,6%).
  - Reconstruções a 55 keV no PCD-CT atingiram atenuação idêntica à do EID-CT ($120 \pm 17\text{ HU}$ vs. $120 \pm 14\text{ HU}$, $p = 0,959$).

### Capítulo 4: Redução de Contraste e Dose em Angio-TC Pulmonar (CTPA)
- **Delineamento:** 140 pacientes em EID-CT (70–120 kV com *CARE kV* e *CARE Dose 4D*) vs. 118 pacientes em PCD-CT (120 kV fixo, VMIs reconstruídos a 55 keV).
- **Parâmetros e Resultados Quantitativos:**
  - Redução de TIL: **26,7%** ($10,2 \pm 1,4\text{ g I}$ vs. $13,9 \pm 4,1\text{ g I}$, $p < 0,001$).
  - Redução de Dose de Radiação ($CTDI_{vol}$): **24,4%** ($3,4 \pm 1,1\text{ mGy}$ vs. $4,5 \pm 2,7\text{ mGy}$, $p < 0,001$).
  - Atenuação Arterial Pulmonar Média:
    - Proximal: $378,9 \pm 100,6\text{ HU}$ (PCD) vs. $384,7 \pm 105,8\text{ HU}$ (EID), $p = 0,66$.
    - Distal/Subsegmentar: $373,6 \pm 101,4\text{ HU}$ (PCD) vs. $368,7 \pm 107,4\text{ HU}$ (EID), $p = 0,71$.
  - Qualidade Subjetiva Diagnóstica: Classificada como moderada/boa em $\ge 96,5\%$ das leituras em ambos os leitores.

### Capítulo 5: Avaliação Subjetiva de Qualidade via Comparação aos Pares
- **Problema:** A escala Likert de 5 pontos sofre de *central tendency bias*\, dependência de calibração interna e alta variabilidade intra e interobservador.
- **Método:** Implementação de software com algoritmo de ordenação de Ford-Johnson ($N=50$ exames exigindo ~220 comparações binárias forçadas em vez de 1225).
- **Resultados:**
  - Dataset de Alta Variação: ICC interobservador aumentou de $0,665$ (Likert) para **$0,785$** (Pairwise Comparison).
  - Dataset de Baixa Variação: ICC interobservador saltou de $0,276$ (Likert) para **$0,562$** (Pairwise Comparison).
  - A concordância intraobservador aumentou expressivamente em 4 dos 6 observadores.

### Capítulo 6: Revisão Sistemática de Métricas Objetivas de Imagem em TC
- **Escopo:** Revisão PRISMA de 35 estudos propondo métricas *reference-free* além de ROIs simples.
- **Taxonomia Identificada:**
  - *Ruído (12 métodos):* Noise Power Spectrum ($NPS$) clínico, Global Noise Level ($GNL$), Global Noise Index ($GNI$), subtração de cortes adjacentes, redes neurais convolucionais (CNNs).
  - *Contraste (4 métodos):* Perfis de densidade linear\, distribuições histogramétricas de HUs em volumes corporais sem segmentação manual.
  - *Resolução Espacial (14 métodos):* Edge Rise Slope ($ERS$), Edge Spread Function ($ESF$), largura a meia altura ($FWHM$) da Task Transfer Function ($TTF$) na interface ar-pele, gradientes 2D.
  - *Métricas Globais/Compostas (7 métodos):* Índice de Detectabilidade ($d'$ com observador modelo), índice de estimabilidade de estenose, *Clarity* e modelos de IA para classificação direta de qualidade diagnóstica.

### Capítulo 7: Automação Total de Métricas de Ruído e Contraste
- Desenvolveu algoritmo baseado em segmentação automática de fígado e músculos paraespinhais, extraindo modas de atenuação e ruído global volumétrico ($ICC = 0,85-0,95$ contra medição manual de ROI), viabilizando auditoria em tempo real.

---

## Conceitos e Tecnologias Relacionados
- [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]]
- [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]
- [[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]
- [[Avaliação Subjetiva por Comparação aos Pares (Pairwise Comparison)|avaliacao-pareada-qualidade-imagem]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]