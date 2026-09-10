---
tipo: conceito
titulo: "Artefatos em Tomografia Computadorizada (TC)"
data_criacao: 2026-08-27
data_atualizacao: 2026-08-27
tags:
  - "artefatos"
  - "tomografia-computadorizada"
  - "qualidade-de-imagem"
  - "fisica-medica"
---

# Artefatos em Tomografia Computadorizada (TC)

## 1. Definição e Fundamentação Física
Em Tomografia Computadorizada, um **artefato** é definido como qualquer discrepância sistemática entre os coeficientes de atenuação linear calculados ($\mu$) ou Unidades Hounsfield ($ext{HU}$) na imagem reconstruída e os valores reais dos tecidos examinados.

Os artefatos degradam a [[Qualidade de Imagem em TC|qualidade-de-imagem-em-tc]], reduzem o [[Índice de Detectabilidade|indice-de-detectabilidade]] ($d'$) e podem mimetizar patologias ou ocultar estruturas anatômicas críticas.

### Classificação Física dos Artefatos:
1. **Físicos / Feixe de Raios X:**
   - **Endurecimento do Feixe (*Beam Hardening*):** Feixes policromáticos sofrem absorção preferencial de fótons moles, gerando estrias e *cupping* (vide [[Crânio e Atenuação Óssea|cr-nio]]).
   - **Efeito de Volume Parcial:** Ocorre quando um vóxel abrange tecidos de atenuações distintas (ex.: osso e parênquima cerebral).
   - **Espalhamento de Fótons (*Photon Scatter*):** Radiação espalhada que atinge os detectores, reduzindo contraste.
2. **Relacionados ao Paciente:**
   - **Movimento:** Respiratório, cardíaco ou involuntário, causando borramento e imagens duplas.
   - **Artefatos Metálicos (*Metal Artifacts*):** Causados por próteses e implantes de alto $Z$ ($\mu_{\text{metal}} \gg \mu_{\text{tecido}}$), gerando estrias brilhantes e bandas escuras (vide [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]]).
3. **Relacionados ao Equipamento / Scanner:**
   - **Artefatos em Anel (*Ring Artifacts*):** Calibração defeituosa ou não-linearidade em canais individuais de detectores.
   - **Artefatos de Cone-Beam / Pitch:** Distorções em geometrias helicoidais com pitch elevado (vide [[Pitch Helicoidal|pitch-helicoidal]]).

---

## 2. Métodos de Mitigação e Inovação Tecnológica
- **Algoritmos MAR:** [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]] (ex.: NMAR).
- **Reconstruções Avançadas:** [[Reconstrução Iterativa|reconstrucao-iterativa]] e [[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]], que utilizam modelos físicos estocásticos para eliminar ruído e estrias.
- **TC com Contagem de Fótons:** [[Photon Counting Detector CT (PCD-CT)|photon-counting-detector-ct]], que elimina artefatos de feixe policromático via binning espectral direto.

---

## 3. Conexões no Acervo
- [[Redução de Artefatos Metálicos|reducao-de-artefatos-metalicos]]
- [[Crânio e Atenuação Óssea|cr-nio]]
- [[Reconstrução de Imagem|reconstrucao-de-imagem]]
- [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]]
