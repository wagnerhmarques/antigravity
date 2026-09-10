---
tipo: tecnologia
titulo: "Eliminação do Ruído Eletrônico em PCD-CT"
data_criacao: 2026-08-27
tags: ["photon-counting", "detectores", "ruido-quantico", "qualidade-de-imagem"]
---

# Eliminação do Ruído Eletrônico em PCD-CT

## 1. Princípio Físico da Discriminação de Limiar
Nos detectores convencionais integradores de energia (EID), o sinal é a soma contínua de cargas geradas no cintilador. Pequenas flutuações térmicas e eletrônicas nos amplificadores somam-se ao sinal, gerando **ruído eletrônico de fundo** que degrada exames em baixa dose.

Nos Detectores de Contagem de Fótons ([[Photon Counting Detector CT (PCD-CT)]]), cada pulso de corrente gerado no semicondutor de conversão direta (ex.: CdTe/CZT) é comparado com um **limiar de energia inferior** (*low-energy threshold*, tipicamente $20 - 25\text{ keV}$):

$$
V_{\text{pulso}} > V_{\text{threshold}} \implies \text{Contador} = \text{Contador} + 1
$$

Como o ruído eletrônico ocorre em amplitudes inferiores ao limiar, ele é **100% rejeitado**, eliminando completamente o ruído de fundo mesmo em doses ultra-baixas de radiação.

## 2. Impacto na Relação Contraste-Ruído e Dose
- Permite reduções drásticas de $mAs$ sem que o ruído eletrônico domine a imagem.
- Eleva o [[Noise Power Spectrum]] a um comportamento puramente de Poisson (quântico).
- Maximiza o [[Índice de Detectabilidade]] ($d'$).

## 3. Conexões
- [[Photon Counting Detector CT (PCD-CT)]]
- [[Ruído Quântico]]
- [[Noise Power Spectrum]]
- [[Virtual Monoenergetic Imaging (VMI)]]
- [[Otimização de Dose em TC]]
