---tipo: tecnologia
titulo: "Photon-Counting Detector CT (PCD-CT)"
data_criacao: 2026-08-22
data_atualizacao: 2026-08-22
tags:
  - tecnologia-ct
  - detectores
  - fisica-medica
  - espectral
fontes_origem:
  - "[[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]"
aliases: [photon-counting-detector-ct, photon-counting-ct, pcd-ct, PCD-CT, "photon counting ct", "detectores de contagem de fótons"]
---

# Photon-Counting Detector CT (PCD-CT)

## 1. Visão Geral e Princípio de Funcionamento
O **Photon-Counting Detector Computed Tomography (PCD-CT)** representa uma transformação de paradigma na arquitetura de detectores de tomografia computadorizada. Em contraste com os detectores tradicionais de integração de energia (*Energy-Integrating Detectors* - EIDs), que convertem fótons de raios X indiretamente em luz cintilante antes de medi-los em fotodiodos, os detectores de contagem de fótons utilizam semicondutores de conversão direta (como telureto de cádmio, CdTe, ou telureto de cádmio e zinco, CZT).

Cada fóton de raio X incidente gera pares elétron-buraco proporcionais à sua energia instantânea, produzindo um pulso de voltagem individual. Esse sinal é processado por circuitos integrados de aplicação específica (ASICs) ultrarrápidos e categorizado em compartimentos de energia (*energy bins*).

```
[Fóton de Raio X] ---> [Semicondutor CdTe/CZT] ---> [Pulso de Tensão ∝ E]
                             │
                             ▼
           [Threshold de Baixa Energia (Elimina Ruído Eletrônico)]
                             │
                             ▼
              [Classificação em Energy Bins]
          Bin 1 | Bin 2 | Bin 3 | Bin 4 (PCD-CT)
```

---

## 2. Diferenças Físico-Instrumentais: EID-CT vs. PCD-CT

| Característica | Energy-Integrating Detector (EID-CT) | Photon-Counting Detector (PCD-CT) |
| :--- | :--- | :--- |
| **Modo de Detecção** | Indireto (Cintilador + Fotodiodo) | Direto (Semicondutor semicondutorizado) |
| **Ponderação de Energia** | Ponderada linearmente pela energia total depositada ($E$) | Cada fóton conta igualmente ($N$), com registro de sua energia individual |
| **Ruído Eletrônico** | Integrado cumulativamente ao sinal (prejudicial em baixas doses) | Rejeitado por *energy thresholding* no nível de hardware |
| **Resolução Espacial** | Limitada por septos ópticos reflexivos entre pixels | Sub-milimétrica sem septos ópticos (ex.: pixels nativos de $0,2 \times 0,2\text{ mm}^2$ ou $0,4\text{ mm}$) |
| **Capacidade Espectral** | Requer duas fontes, comutação rápida de $kV$ ou detector em dupla camada | Intrínseca em qualquer aquisição de rotina (modo multi-bin) |
| **Modo Padrão de Reconstrução** | Imagens policromáticas ($kV$) | Imagens monoenergéticas virtuais ([[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]) por padrão |

---

## 3. Vantagens Físicas e Clínicas

1. **Aumento do Contraste do Iodo:** Como os fótons de menor energia sofrem maior atenuação por [[Virtual Monoenergetic Imaging (VMI)|efeito fotoelétrico]] com o iodo ($Z=53$), o fato de o PCD-CT não sub-representar esses fótons (ao contrário do EID, que favorece fótons de alta energia por depositarem mais energia no cintilador) resulta em um ganho intrínseco de $11\%$ a $38\%$ na relação contraste-ruído ($CNR$) para meios iodados.
2. **Redução de Ruído em Baixas Doses:** A eliminação de ruído eletrônico estabiliza medições de atenuação e ruído em protocolos com baixa exposição ($CTDI_{vol} < 3\text{ mGy}$) e em pacientes de grande porte físico.
3. **Reconstruções Monoenergéticas por Padrão:** Elimina o dilema de seleção prospectiva de $kV$ para contraste; o feixe é emitido em voltagens ótimas de penetração (ex.: 120 ou 140 kV) e o contraste desejado é selecionado retrospectivamente em $keV$ ([[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]).
4. **Economia de Contraste e Dose:** Facilita protocolos clínicos com redução substancial de iodo (20% a 27%) sem degradar a qualidade diagnóstica, conforme demonstrado em estudos clínicos de abdome e tórax ([[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]).

---

## Referências Cruzadas
- [[Hoeijmakers 2026 - Qualidade de Imagem em TC Moderna|hoeijmakers-2026-image-quality-modern-ct]]
- [[Virtual Monoenergetic Imaging (VMI)|virtual-monoenergetic-imaging]]
- [[Otimização e Redução de Meio de Contraste em TC|otimizacao-meio-de-contraste-tc]]
- [[Métricas Objetivas de Qualidade de Imagem em TC|metricas-objetivas-qualidade-imagem-tc]]