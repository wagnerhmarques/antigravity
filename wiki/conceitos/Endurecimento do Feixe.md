---
tipo: conceito
titulo: "Endurecimento do Feixe (Beam Hardening) em TC"
data_criacao: 2026-08-27
tags: ["qualidade-de-imagem", "artefatos", "espectro-raios-x", "fisica-medica"]
---

# Endurecimento do Feixe (Beam Hardening) em TC

## 1. Princípio Físico
O **Endurecimento do Feixe** (*Beam Hardening*) ocorre porque os tubos de raios X produzem um **espectro policromático** de fótons ($0 < E \le E_{\max}$). Como a atenuação por [[Efeito Fotoelétrico]] diminui acentuadamente com a energia ($\mu \propto E^{-3}$), os fótons de menor energia são preferencialmente absorvidos nas primeiras camadas de tecido.

Consequentemente, a energia média $\bar{E}$ do feixe emergente se desloca para valores mais altos ("endurece"), reduzindo a taxa de atenuação efetiva nas regiões centrais dos pacientes ou objetos cilíndricos.

$$
I(L) = \int_{0}^{E_{\max}} I_0(E) \exp\left( -\int_{L} \mu(x, y, z; E) \, dl \right) dE \ne I_0 \exp(-\bar{\mu} L)
$$

## 2. Impacto em Unidades Hounsfield (HU) e Artefatos
1. **Artefato de Cupping (Taça):** Redução artificial dos números CT no centro de objetos homogêneos (ex.: fantomas de água), fazendo o centro parecer menos denso que a periferia.
2. **Bandas Escuras (Streaks):** Entre estruturas de alto $Z$ (como ossos densos ou próteses metálicas).
3. **Dependência com kVp:** Tubos operando a menor kVp sofrem maior endurecimento relativo, enquanto feixes em alto kVp já iniciam mais penetrantes e filtrados.

## 3. Conexões
- [[Efeito Fotoelétrico]]
- [[Unidades Hounsfield]]
- [[Filtragem Bowtie]]
- [[Tomografia Computadorizada Espectral]]
